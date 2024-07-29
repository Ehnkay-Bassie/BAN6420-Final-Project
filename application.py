from flask import Flask, render_template, request
from pymongo import MongoClient

# Initialize Flask application
app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['survey_db']
collection = db['responses']

@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Extract form data
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = request.form['age']
    gender = request.form['gender']
    income = request.form['income']
    
    # Extract expenses data directly
    expenses = {
        'utilities': request.form.get('utilities'),
        'entertainment': request.form.get('entertainment'),
        'school_fees': request.form.get('school_fees'),
        'shopping': request.form.get('shopping'),
        'healthcare': request.form.get('healthcare')
    }
    
    # Filter out None values
    expenses = {k: v for k, v in expenses.items() if v}

    # Create a response dictionary to insert into MongoDB
    response = {
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'gender': gender,
        'income': income,
        'expenses': expenses
    }
    
    # Insert the response into the MongoDB collection
    collection.insert_one(response)
    
    # Render the index.html template with a success flag
    return render_template('index.html', success=True)

if __name__ == '__main__':
    # Enable debug mode for development
    app.run(debug=True)