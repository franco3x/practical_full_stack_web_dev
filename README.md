# Internal Image Search Website

## Overview

This project is an internal web application that allows users to search for and view images by leveraging the Unsplash API. The application is designed for seamless performance, scalability, and ease of use.

## Features

Image Search: Search for images using keywords and view results fetched from the Unsplash API.

Frontend: Built with React for an interactive and responsive user experience.

Backend: Flask API integrated with MongoDB for data storage and retrieval.

Database: MongoDB for managing and storing application data.

Docker: Fully containerized using Docker, enabling easy deployment and environment replication.

## Technologies Used

Frontend: React

Backend: Python (Flask)

Database: MongoDB, MongoDB Express

Containerization: Docker

## Project Structure

images_gallery/
├── api/
│   ├── main.py
│   ├── mongo_client.py
│   ├── requirements.txt
│   ├── docker-compose.yml
├── frontend/
│   ├── src
│       ├── App.js
│   ├── components
│       ├── Header.js
│       ├── ImageCard.js
│       ├── Search.js
│       ├── Spinner.js
│       ├── Welcome.js

## API Folder

main.py: The main Flask application file handling backend logic.

mongo_client.py: MongoDB connection configuration.

requirements.txt: Python dependencies required for the backend.

docker-compose.yml: Configuration file to set up Docker containers for the project.

## Frontend Folder

App.js: Main React component that ties the application together.

Header.js: Header component for branding and navigation.

ImageCard.js: Component for displaying individual image results.

Search.js: Search bar component to interact with the Unsplash API.

Spinner.js: Loading spinner component for improved UX.

Welcome.js: Initial welcome screen component.



## Acknowledgements

Unsplash API for providing free image access.

React, Flask, Python, Docker and MongoDB communities for excellent tools and documentation.

