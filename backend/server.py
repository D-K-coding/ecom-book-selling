# import required flask 
from flask import Flask, render_template, request

# create the app 
app = Flask(__name__)

# create the route
@app.route('/')
def index():
    return '<h1>Hello World</h1>'

# create the login route
@app.route('/login')
def login():
    return render_template('index.html')



# run the app
if __name__ == '__main__':
    app.run(debug=True)