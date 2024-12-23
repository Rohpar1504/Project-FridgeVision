**Presentation**
CS 222 Project Fridge Vision. We aim to develop a website where blind people could submit pictures of their fridges and ask where items in the fridge are located. An AI would both understand what they said and locate the item. The website also tracks the items in the fridge/pantry, maintains a shopping list, and maintains/generates recipes using the items in the fridge/pantry. We are using Python to implement the user-functionality. We are using HTML to implement the web design aspect and Javascript to handle the frontend to backend connection. 

**Technical Architecture**
Frontend:

index.html (javascript included)

fridge_contents.html (javascript included)

Javascript connects to routes.py via GET and POST requests

Routes.py uses backend classes and functions to implement functionality

Backend:

Fridge, Food, Recipes, Shopping List (uses openai, connects to ChatGPT via an API key)

Shelf Detection (uses OpenCV)

Item Detection (uses OpenCV and YOLO)

**Installation**
Open a VSCode window, ensure python3 is downloaded so that you can run python in VSCode
Choose "Clone Git Repository", then insert the GitHub url for the git repository

On your command line, run:

pip install numpy

pip install opencv-python

To host the website locally, see: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

TLDR: Paste the following into your command line

$ python3 -m venv venv

$ source venv/bin/activate

(venv) $ pip install flask

import flask

Then run the website by clicking the play button on the routes file in the app directory

**Group Members**
John Fabrycky - Team Lead, Full Stack Web Developer, Image Recognition Engineer

I coordinated team meetings, ensured team members knew how to use the technology required for the course (i.e. GitHub, Python, VSCode, Numpy), and coordinated pull requests and pull reviews. I designed the website frontend and integrated the backend with the scripts created by the rest of the team. I implemented an image recognition model using openCV to find shelves within a fridge.

Jacob Reynolds - Image Recognition Engineer

I built an image recognition model capable of detecting specific food items within a fridge. The model uses OpenCV and YOLO as a base and is able to detect some food items with a high level of accuracy.

Rohan Pareek - Voice Recognition Engineer

I developed the voice recognition component for the Food Finder system of the Fridge Vision project using Python's PocketSphinx library. My role involved designing and implementing the software that allows users to interact with the application through spoken commands. The voice recognition system captures audio input, processes it using PocketSphinx to convert speech into text, and then generates queries for the fridge database based on the recognized text.

Toby Perlstadt - Software Developer

I created the fridge classes and functions including the shopping list, keeping track of the contents of the fridge as they change, and the list of recipes. Furthermore, I implemented OpenAI integration to the recipes feature in order to create recipes based on the contents of the fridge along with instructions to help the user make use of the food they have on hand, even if they don't have cooking experience. 
