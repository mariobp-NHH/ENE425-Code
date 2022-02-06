from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "<h1>Home page</h1>" \
           "<p>In this project we develop and app...</p>"

@app.route('/developers')
def developers():
    return "<h1>Developers</h1>" \
           "<p>In this webpage, we introduce the developers of the app...</p>"

@app.route('/app_calculator')
def app_calculator():
    return "<h1>App Calculator</h1>" \
           "<p>In this webpage, we develop an app to work out transport carbon emissions...</p>"

if __name__ == '__main__':
    app.run(debug=True)
