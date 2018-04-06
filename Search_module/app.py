from flask import Flask
from flask import render_template, redirect
from flask import request, url_for
from main import main
# from time import sleep


app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        author = request.form['author']
        title = request.form['title']
        keywords = request.form['keywords']
        year1 = request.form['year1']
        year2 = request.form['year2']
        main(author, title, keywords, year1, year2)
        return redirect(url_for('index'))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
