from flask import Flask, render_template, url_for

formula = Flask(__name__)

@formula.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    formula.run(debug=True, port=5001)
