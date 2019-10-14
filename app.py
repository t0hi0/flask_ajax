import datetime
from flask import Flask, render_template, json


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_rand')
def get_time():
    num = datetime.datetime.now()
    # Count for datetime changes (1 to sec)
    return json.dumps({
        'rand': num
    })


if __name__ == '__main__':
    app.run()
