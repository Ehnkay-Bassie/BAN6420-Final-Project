import csv
import pandas as pd
from pymongo import MongoClient

class User:
    def __init__(self, first_name, last_name, age, gender, income, expenses):
        """
        Initialize the User object with personal details and expenses.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.income = income
        self.expenses = expenses

    def to_csv_row(self):
        """
        Convert the User object to a list suitable for a CSV row.
        """
        return [
            self.first_name,
            self.last_name,
            self.age,
            self.gender,
            self.income,
            # Retrieve the expense amount for each of the below, default to 0 if not present
            self.expenses.get('utilities', 0),
            self.expenses.get('entertainment', 0),
            self.expenses.get('school_fees', 0),
            self.expenses.get('shopping', 0),
            self.expenses.get('healthcare', 0)
        ]

def export_mongo_to_csv(file_path='survey_data.csv'):
    """
    Export data from MongoDB to a CSV file.
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['survey_db']
    collection = db['responses']
    cursor = collection.find()

    # Define CSV header
    header = ['first_name', 'last_name', 'age', 'gender', 'income', 'utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']

    try:
        # Open the CSV file for writing
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            # Write each document from MongoDB as a row in the CSV
            for document in cursor:
                user = User(
                    first_name=document.get('first_name', ''),
                    last_name=document.get('last_name', ''),
                    age=document.get('age', ''),
                    gender=document.get('gender', ''),
                    income=document.get('income', ''),
                    expenses=document.get('expenses', {})
                )
                writer.writerow(user.to_csv_row())
    except Exception as e:
        print(f"Error exporting from MongoDB to CSV: {e}")

def load_csv_to_dataframe(file_path='survey_data.csv'):
    """
    Load data from a CSV file into a pandas DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading CSV into DataFrame: {e}")

# Call the functions
if __name__ == "__main__":
    # Export data from MongoDB to CSV
    export_mongo_to_csv()
    # Load CSV data into DataFrame
    df = load_csv_to_dataframe()
    
    if df is not None:
        print("Data loaded successfully!")
        print(df.head())  # Display the first few rows of the DataFrame