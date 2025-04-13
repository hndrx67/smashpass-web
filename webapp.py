from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
import os
from werkzeug.utils import secure_filename
import uuid
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'test'  # For flash messages





@app.route('/')
def index():
    return render_template('index6.html')





if __name__ == '__main__':
    app.run(debug=True)
