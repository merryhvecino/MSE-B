# Import Flask
from flask import Flask, request
import os

app = Flask(__name__)

# Create static folder
if not os.path.exists('static'):
    os.makedirs('static')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    result = '''
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    '''
    
    if request.method == 'POST':
        file = request.files['file']
        file.save(f'static/{file.filename}')
        result += f'<img src="/static/{file.filename}">'
    
    return result

app.run(debug=True)