from flask import Flask, render_template, request, url_for
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '7BLYkEfBA6O6donxWlSihAXox8C0sKR6b'

year = datetime.datetime.now().year


@app.route("/")
def home():
    return render_template("index.html", year=year)


if __name__ == '__main__':
    app.run(debug=True)
