# DJS Clothing Store - React Frontend with Flask Backend

Welcome to DJS Clothing Store! This full-stack web application is designed to provide a smooth shopping experience. Users can browse and shop for clothing items, manage their cart and favorites, write reviews, and perform various actions seamlessly.


## Project Overview

The DJS Clothing Store project comprises two main components:

1. Frontend - The frontend of the application is developed using React.js, a popular JavaScript library for building user interfaces. Its main purpose is to provide users with a smooth and intuitive shopping experience.

2. Backend - The backend of the DJS Clothing Store is powered by Flask, a lightweight Python web framework. It handles all the logic and data management, including user authentication, managing product data, shopping cart, favorites, and reviews.

## Frontend Functionality

The frontend of the DJS Clothing Store focuses on delivering user experience and several essential functionalities, including:

- User Authentication: Allows users to create accounts, log in, and maintain their profile information.
- Navigation: Seamless routing to different pages using React Router. Pages include Home, Men's Collection, Women's Collection, and Kids Collection.
- Shopping Cart: Enables users to add and remove items to/from their cart.
- Favorites: Allows users to add and remove items to/from their favorites list for quick access and future purchases.
- Product Reviews: Users can write reviews for products they have purchased and delete their existing reviews if needed.
- User Sessions: Keeps users logged in and maintains session data throughout their shopping journey.

## Backend Functionality

The backend of the DJS Clothing Store handles critical functionalities using Flask and various supporting libraries, including:

- User Authentication: Implements session-based authentication for secure login and registration.
- Bcrypt: Utilizes bcrypt for hashing and salting user passwords, ensuring safe storage in the database.
- SQLAlchemy: Manages data models and performs database operations using an object-relational mapper (ORM).
- Database Migration: Utilizes Flask-Migrate for smooth database schema changes and updates.
- API Routes: Implements multiple API routes (GET, POST, PATCH, DELETE) to handle frontend requests and ensure smooth communication.
  
## Getting Started

To run the DJS Clothing Store project locally, follow these steps:

1. Install `pipenv` and `npm` if you haven't already.
2. Clone the project repository from [GitHub](https://github.com/dayarmush/DJS-Clothing-Store).
3. Navigate to the server folder and set up the backend environment:

- `cd server`
- `pipenv install`
- `pipenv shell`
- `flask db upgrade`
- `python seed.py`
- `python app.py`

4. Open a new terminal window, navigate to the client folder, and set up the frontend environment:

- `cd client`
- `npm install`
- `npm run`

## Contributing
Contributions to the DJS Clothing Store project are highly appreciated. If you encounter any issues or have suggestions for improvements, please create a pull request or open an issue on the GitHub repository.

Happy shopping! 🛍️
