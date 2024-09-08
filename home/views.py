from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import format_html


# Create your views here.

def home(request):
    return render(request, 'index.html')

def scores_page(request):
    results = [
    {"subject": "Object Oriented Programming", "marks": 100},
    {"subject": "Data Structures and Algorithms", "marks": 95},
    {"subject": "Computer Organization and Design", "marks": 85},
    {"subject": "Computer Networks", "marks": 90},
    {"subject": "Internetworking Essentials", "marks": 95},
    {"subject": "Community Development Project", "marks": 90},
    {"subject": "Probability and Statistics", "marks": 85},
    {"subject": "Upper Intermediate Communication Skills-II", "marks": 90},
]
    return render(request, 'scores.html', context= {'results' : results})

def skills_page(request):
    return render(request, 'skills.html')

def projects_page(request):
    return render(request, 'projects.html')

def success_page(request):
    return HttpResponse('<h1>This is Success Page</h1>')

from django.http import HttpResponse

def example(request):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Binomial Expansion</title>
    </head>
    <body>
        <h1>Derivation of (a + b)<sup>3</sup></h1>
        <p>To derive the equation for (a + b)<sup>3</sup>, we can use the binomial theorem or expand it step-by-step. Here's the detailed derivation:</p>
        
        <ol>
            <li>
                <p>Start with the binomial expansion formula for (a + b)<sup>n</sup>:</p>
                <p style="text-align: center;">(a + b)<sup>n</sup> = &sum;<sub>k=0</sub><sup>n</sup> C(n, k) a<sup>n-k</sup> b<sup>k</sup></p>
                <p>For n = 3, the binomial expansion is:</p>
                <p style="text-align: center;">(a + b)<sup>3</sup> = &sum;<sub>k=0</sub><sup>3</sup> C(3, k) a<sup>3-k</sup> b<sup>k</sup></p>
            </li>
            <li>
                <p>Calculate the individual terms in the expansion:</p>
                <ul>
                    <li>
                        <p>For k = 0:</p>
                        <p style="text-align: center;">C(3, 0) a<sup>3-0</sup> b<sup>0</sup> = 1 &middot; a<sup>3</sup> &middot; 1 = a<sup>3</sup></p>
                    </li>
                    <li>
                        <p>For k = 1:</p>
                        <p style="text-align: center;">C(3, 1) a<sup>3-1</sup> b<sup>1</sup> = 3 &middot; a<sup>2</sup> &middot; b = 3a<sup>2</sup>b</p>
                    </li>
                    <li>
                        <p>For k = 2:</p>
                        <p style="text-align: center;">C(3, 2) a<sup>3-2</sup> b<sup>2</sup> = 3 &middot; a &middot; b<sup>2</sup> = 3ab<sup>2</sup></p>
                    </li>
                    <li>
                        <p>For k = 3:</p>
                        <p style="text-align: center;">C(3, 3) a<sup>3-3</sup> b<sup>3</sup> = 1 &middot; 1 &middot; b<sup>3</sup> = b<sup>3</sup></p>
                    </li>
                </ul>
            </li>
            <li>
                <p>Combine all the terms:</p>
                <p style="text-align: center;">(a + b)<sup>3</sup> = a<sup>3</sup> + 3a<sup>2</sup>b + 3ab<sup>2</sup> + b<sup>3</sup></p>
            </li>
        </ol>
        
        <p>So, the derived equation for (a + b)<sup>3</sup> is:</p>
        <p style="text-align: center;"><b>(a + b)<sup>3</sup> = a<sup>3</sup> + 3a<sup>2</sup>b + 3ab<sup>2</sup> + b<sup>3</sup></b></p>
    </body>
    </html>
    """
    return HttpResponse(html_content, content_type="text/html")


