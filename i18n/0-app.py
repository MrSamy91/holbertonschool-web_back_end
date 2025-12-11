#!/usr/bin/env python3
"""
Basic Flask app for Task 0
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Route '/' that renders the index template."""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
