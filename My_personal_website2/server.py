from flask import Flask, render_template
app = Flask(__name__)
# document.body.contentEditable=true this way you can make the objects in html editable from the browser
@app.route('/')
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)