import os
from flask import Flask, render_template, send_from_directory


app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/about")
def about():
    return render_template("about.html")

@app.get("/support")
def support():
    return render_template("support.html")

@app.post("/support")
def support_post():
    return render_template("support.html", )

@app.get("/favicon.ico")
def favicon_ico():
    print(app.root_path)
    return send_from_directory(app.root_path,
                          'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.get("/favicon.webp")
def favicon_png():
    print(app.root_path)
    return send_from_directory(app.root_path,
                          'favicon.webp', mimetype='image/webp')

if __name__ == "__main__":
    app.run("0.0.0.0", 8000)
