# Django Portfolio Project

This Django portfolio project is designed to showcase skills in web development using the Django framework. It includes features for creating chat rooms, sending and receiving messages in real-time via websockets, user authentication using AllAuth with social account integration, and more.

## Getting Started

To get started with this project, follow these steps:

1. **Clone the Repository**

2. **Install Dependencies**: Navigate to the project directory and install the required dependencies using:

```sh
pip install -r requirements.txt
```


3. **Set Up Environment Variables**: Set up the necessary environment variables in a `.env` file. Ensure you have the following variables set:
- `SECRET_KEY`: Django secret key for security
- `DEBUG`: Set to 'True' for development mode
- `DB_NAME`: Name of your PostgreSQL database
- `DB_USER`: Username for the PostgreSQL database
- `DB_USER_PASSWORD`: Password for the PostgreSQL database user
- `DB_HOST`: Host for the PostgreSQL database
- `DB_PORT`: Port for the PostgreSQL database

4. **Run Migrations**: Apply database migrations using the following command:
```sh
python manage.py migrate
```


5. **Create Superuser (Optional)**: Create a superuser to access the Django admin panel:
```sh
python manage.py createsuperuser
```



6. **Run the Development Server**: Start the development server using:
```sh
python manage.py runserver
```


7. **Access the Application**: Access the application in your web browser at `http://127.0.0.1:8000/`.

8. **Configure AllAuth**: Connect the AllAuth related platforms such as Google, GitHub, etc. To do this, follow these steps:
- Create a new site: In the Django admin panel (`/admin/`), add a new site with the domain `127.0.0.1:8000` for local development.
- Create social applications: For each platform (Google, GitHub, etc.), create social applications in the Django admin panel and configure the respective client IDs and secrets.


## Project Structure

The project structure is organized as follows:

- **ChatPrj/**: Main project directory containing settings, URL configurations, and ASGI/WSGI configurations.
- **ChatApp/**: Django app directory containing models, views, templates, and static files for the chat application.
- **models.py**: Defines database models for rooms and messages.
- **views.py**: Contains views for creating chat rooms and displaying messages.
- **templates/**: Directory for HTML templates.
- **static/**: Directory for static files such as CSS and JavaScript.
- **consumers.py**: ASGI consumer for handling websocket connections.
- **routing.py**: Defines websocket URL routing.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Create a new Pull Request

## License

This project is licensed under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND)](LICENSE).

Under this license, you are free to:

- Share — copy and redistribute the material in any medium or format.

Under the following terms:

- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
  
- **NonCommercial** — You may not use the material for commercial purposes.
  
- **NoDerivatives** — If you remix, transform, or build upon the material, you may not distribute the modified material.