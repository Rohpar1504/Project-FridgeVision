**Project Fridge Vision** 

Developed a website where blind people could submit pictures of their fridges and ask where items in the fridge are located. An AI would both understand what they said and locate the item. The website also tracks the items in the fridge/pantry, maintains a shopping list, and maintains/generates recipes using the items in the fridge/pantry. Used Python to implement the user-functionality. Used HTML to implement the web design aspect and Javascript to handle the frontend to backend connection. 


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
