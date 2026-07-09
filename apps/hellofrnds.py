from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define the root route to handle web requests
@app.route('/')
def hello_friends():
    return 'Hello Friends... I am anuradha!'

# Start the local development server
if __name__ == '__main__':
    app.run(debug=True)
