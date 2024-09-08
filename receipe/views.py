# Import necessary modules at the top
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *

# Define the view function

@login_required(login_url= "/")
def receipes(request):
    if request.method == 'POST':
        data = request.POST
        recipeName = data.get('recipeName')
        recipeDescription = data.get('recipeDescription')
        recipeImage = request.FILES.get('recipeImage')

        Recipe.objects.create(name = recipeName, 
                              description= recipeDescription, 
                              image= recipeImage, )
        return redirect("/recipes/")
    
    quereyset = Recipe.objects.all()

    if request.GET.get('search'):
        quereyset = quereyset.filter(name__icontains = request.GET.get('search'))
    context = {'recepies' : quereyset}
    return render(request, 'receipes.html', context)

@login_required(login_url= "/")
def update_recipe(request, id):
    queryset = Recipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        recipeName = data.get('recipeName')
        recipeDescription = data.get('recipeDescription')
        recipeImage = request.FILES.get('recipeImage')

        if recipeName:
            queryset.name = recipeName
        
        if recipeDescription:
            queryset.description = recipeDescription
        
        if recipeImage:
            queryset.image = recipeImage

        queryset.save()
        return redirect(  "/recipes/" )
    return render(request, 'update.html', context= {'recipe' : queryset})

@login_required(login_url= "/")
def delete_recipe(request, id):
    quereyset = Recipe.objects.get(id = id)
    quereyset.delete()
    return redirect("/recipes/")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid username')
            return redirect("/")
        
        user = authenticate(request, username = username, password = password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect( "/" )
        else:
            login(request, user)
            return redirect("/recipes/")

    return render(request, 'login.html')

@login_required(login_url= "/")
def logout_page(request):
    logout(request)

    return redirect("/")

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.error(request, 'Username already taken')
            return redirect('/register/')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        user.set_password(password)
        user.save()

        messages.success(request, 'Account created sucessfully')

        return redirect("/")

    return render(request, 'register.html')

