from flask import Flask, flash, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/Home')
def run_template():
    return render_template('index.html')

@app.route('/Hospitals') 
def Hospitals():
    return render_template('Hospitals.html')

@app.route('/Query')
def Query():
    return render_template('Query.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
