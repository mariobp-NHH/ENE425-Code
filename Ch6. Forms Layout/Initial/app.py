from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/app_calculator')
def app_calculator():
    return render_template('app_calculator.html', title='App Calculator')

if __name__ == '__main__':
    app.run(debug=True)
