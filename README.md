
# Django Chat Application

This application chat platform developed using Django and Django Channels, offering a range of features including account creation, login functionality, real-time visibility of online users, and the ability to initiate chats with those currently active.

## Features

* User registration and authentication.
* Real-time chat using Django Channels and WebSocket.
* Online user status display.
* Responsive design for both desktop and mobile devices.

## Installation
1. Clone the repository to your local machine.
2. Create a virtual environment (Virtualenv env) and activate it (.\env\Scripts\activate).
3. Intall the project dependencies. (pip install -r requirements.txt).
4. Apply database migrations.
5. Start the development server (python manage.py runserver).
6. Access the application in web browser at `http://127.0.0.1:8000/chat/`.

## API Endpoints
* User registration: `http://127.0.0.1:8000/chat/register`
* User login: `http://127.0.0.1:8000/chat/login`
* Create/ Join room: `http://127.0.0.1:8000/chat/`
* Chat room: `http://127.0.0.1:8000/chat/<your_chat_room>/`

## Video link: 

## Screenshots of project

### Register: 
![register](https://github.com/MihirChhabria/chattingapp/assets/67017533/3bfb6d14-6e46-45f3-9c66-2eaa4dea2804)

### Login: 
![login](https://github.com/MihirChhabria/chattingapp/assets/67017533/615e59ce-c939-4f05-8e7d-8a218ecb9fd9)

### Home Screen: 
![room](https://github.com/MihirChhabria/chattingapp/assets/67017533/66d9dda5-b0c9-4eec-a046-b8b154ff24bb)

### Chatting Interface:
![chatapp](https://github.com/MihirChhabria/chattingapp/assets/67017533/197de998-c29f-4ded-9964-0b986c0e5933)
