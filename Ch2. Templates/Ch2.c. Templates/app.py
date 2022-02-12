from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/developers')
def developers():
    return render_template('developers', title='developers')

@app.route('/app_calculator')
def app_calculator():
    return render_template('app_calculator', title='app_calculator')

if __name__ == '__main__':
    app.run(debug=True)
