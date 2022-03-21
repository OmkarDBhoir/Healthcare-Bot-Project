from flask import Flask, flash, render_template
app = Flask(__name__)


@app.route('/')
def run_template():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True, port=8000)
