from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>home</title>
        </head>
        <body>
            <h1 style="color:blue; text-align: center">Home</h1>
            <p style="font-size:18px">
                <strong>Carbon emissions</strong> constitute the 60% of the ecological footprint, and are one of the 
                main contributors to climate change.
                </br>
                </br>
                <strong>Transport carbon emissions</strong> are an important share of carbon emissions. We develop a <strong>methodology</strong> to 
                compute transport carbon emissions, and we develop an <strong>app</strong> to track those emissions.
            </p>
        </body>
    </html>
    '''

@app.route('/developers')
def developers():
    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>developers</title>
        </head>
        <body>
            <h1 style="color:blue; text-align: center">Developers</h1>
            
            <p style="font-size:18px">
                The developers of this webpage come from different backgrounds. Most of us are enrolled in the ENE
                master program at NHH, and share a common interest in policies to mitigate climate change and in the 
                promotion of a fair and inclusive green transition. 
                </br>
                </br>
                We have a strong background in quantitative analysis complemented with our skills in programming and 
                app development. We are also committed with the big transformations and debates taken place in the society
                and we are involved in the political debates participating actively in political forums. 
            </p>
            
            <p style="font-size:24px; text-align: center">
                <strong>Developers:</strong>
                <ul style="font-size:24px; text-align: center">
                    <li>
                        <strong>Developer 1</strong>: Brief bio. Link to cv.
                    </li>
                    <li>
                        <strong>Developer 2</strong>: Brief bio. Link to cv.
                    </li>
                </ul>
            </p>
            
        </body>
    </html>
    '''

@app.route('/app_calculator')
def app_calculator():
    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>app calculator</title>
        </head>
        <body>
            <h1 style="color:blue; text-align: center">App Calculator</h1>
            
            <p style="font-size:18px">
                We develop the transport carbon emissions app focusing our analysis in the main transport modes
                and the their fuel type.
            </p>
            
            <p style="font-size:24px; text-align: center">
                <strong>Methodology:</strong>
                <ol style="font-size:24px; text-align: center">
                    <li>
                        We assume that the fuel type employed by a particular transport mode is the most popular for that
                        category
                    </li>
                    <li>
                        We assume that the transport carbon emissions of cyclist and  pedestrians are nill.
                    </li>
                </ol>
            </p>
            
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
