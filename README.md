# masterblog-with-flask
A simple blog web application built with Flask, using JSON files for data storage. Users can create, update, delete, and like blog posts.

##Features:
Add new blog posts (author, title, content)

Update existing blog posts

Delete blog posts

Like blog posts

JSON-based storage (no database)

Clean and responsive layout (basic CSS)

##Getting Started
Prerequisites:
Python 3.x

Flask installed
pip install flask

Run the App
python app.py

Then open your browser and go to http://localhost:5000.

##Data Format
The blog posts are saved in a blog_posts.json file as a list of dictionaries:
[
  {
    "id": 1,
    "author": "John Doe",
    "title": "First Post",
    "content": "This is my first post.",
    "likes": 0
  }
]

##Created by:
JQSwain

##Collaboration:
Feel free to collaborate and exoeriemtn as lomng as you branch from the main before you change anything and make a pull request.

