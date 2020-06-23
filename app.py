from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', title="Home")


@app.route('/explore')
def explore():
    return render_template('explore.html', title="Listen Now")


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Us')


@app.route('/register')
def register():
    return render_template('register.html', title='Register to Start Listening')


if __name__ == "__main__":
    app.run(debug=True)
