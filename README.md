# Recipe Adding App

This is a Django-based web application that allows users to add, update, and delete their favorite recipes. The app also includes user authentication features, such as login and registration, to ensure that each user's recipes are secure.

## Features

- **User Authentication**: 
  - Users can register for an account.
  - Users can log in and log out securely.
  
- **Recipe Management**: 
  - Users can add new recipes.
  - Users can update or modify existing recipes.
  - Users can delete recipes they no longer need.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript (Django Templates)
- **Database**: SQLite (default Django database)
- **Security**: Django's built-in authentication system for login and registration.

## Getting Started

### Prerequisites

Ensure you have the following installed on your machine:

- Python (version 3.x)
- Django (version 4.x or newer)
- 
### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/BHARATHKUMARREDDY2004/Recipe-App-Using-Django.git
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m .venv env
   source .venv/bin/activate  # For Windows: .venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser account to access the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000` to access the app.

### Usage

1. Register for an account.
2. Log in to manage your recipes.
3. Use the app to add, update, or delete recipes as desired.

### Folder Structure

```
recipe-adding-app/
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── recipe/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   └── ...
└── ...
```

### Screenshots
![image](https://github.com/user-attachments/assets/faa8516e-d22c-4c1d-ab87-226a926d808d)
![image](https://github.com/user-attachments/assets/811b37e7-f917-4ec0-b8a0-0f1f8ddd5cc7)
![image](https://github.com/user-attachments/assets/fe2ae0ea-1276-482b-be70-7de39a411b32)

## Contributing

Contributions are welcome! Please submit a pull request or create an issue if you would like to add features or fix bugs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or feedback, feel free to contact me.
