# Import Flask Dependecies 
from flask import Flask

app = Flask(__name__)

# Route all the HTML page
@app.route('/"index.html')


# Main Implementation
def index():
    return "Hello World"


if __name__=="__main__":
    app.run(debug=True)