from flask import Flask, request, redirect, url_for, session, send_from_directory, render_template, jsonify
import os
from find_shelves import image_resize

app = Flask(__name__)
app.secret_key = 'FridgeFinder'
app.config['UPLOAD_FOLDER'] = './fridge-pics'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', username="John Fabrycky")

@app.route('/fridge_contents.html')
def fridge_contents():
    return render_template('fridge_contents.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'fridgePic' not in request.files or False:
        return jsonify({"message": "No file part"}), 400
    
    file = request.files['fridgePic']
    user_message = request.form.get('stringInput', '')
    
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    
    if user_message == '':
        return jsonify({"message": "No selected item"})
    
    if file:
        # Save the file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        # # Return the message and the image URL
        # image_url = url_for('uploaded_file', filename=file.filename, _external=True)
        location_description, _ = image_resize(file_path, 300, 400)
        location_description = "The " + user_message + " " + location_description
        return jsonify({"message": location_description}) #, "image_url": image_url})
    
    return jsonify({"message": "Error occurred"}), 500


if __name__ == '__main__':
    app.run(debug=True)