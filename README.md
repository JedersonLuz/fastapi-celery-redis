# FastAPI with Celery and Redis

This repository is a playground for experimenting with FastAPI, Celery, and Redis using Docker Compose.

## Prerequisites

Before getting started, make sure you have the following installed:

- Docker
- Docker Compose

## Getting Started

To run the application, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Run `docker-compose up --build` to start the containers.
4. Access the FastAPI application at `http://localhost:8000/docs`.

## Usage

Once the application is up and running, you can perform various tasks through the FastAPI docs interface:

- Submit a task to Celery: `POST /task`
- Check the status of a task: `GET /task/{task_id}`
- Get the result of a completed task: `GET /task/{task_id}/result`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
