# Step 1: Import required modules
from flask import Flask, request  # Flask for web app, request to handle file uploads
import os  # os is needed to create folders

# Step 2: Create Flask application
app = Flask(__name__)

# Step 3: Make sure we have a static folder for uploads
if not os.path.exists('static'):
    os.makedirs('static')

# Step 4: Create our webpage with upload form and image display
@app.route('/', methods=['GET', 'POST'])  # Handle both GET (view page) and POST (upload file)
def upload_file():
    # Create the upload form HTML
    result = '''
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    '''
    
    # When a file is uploaded (POST request)
    if request.method == 'POST':
        # Get the uploaded file
        file = request.files['file']
        # Save it in the static folder
        file.save(f'static/{file.filename}')
        # Add the image to our page
        result += f'<img src="/static/{file.filename}">'
    
    # Show the webpage
    return result

# Step 5: Run the Flask app
if __name__ == '__main__':
    app.run(debug=True) 