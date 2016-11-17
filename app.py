from flask import Flask
import os
import sys

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello Software Crafters!"

if __name__ == "__main__":
        app.run("0.0.0.0")
