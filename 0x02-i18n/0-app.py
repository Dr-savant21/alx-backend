#!/usr/bin/env python3
from flask import Flask, render_template, redirect, url_for, request;

app = Flask (__name__, template_folder="templates", static_folder="staticFolder")

@app.route("/")
def index():
    return render_template("0-index.html")

    
if __name__ == "__main__":
    app.run(debug=True)