-------------------------------
# Flask Healthcare Application: Income and Expense Survey Tool
-------------------------------


## Project Overview
----------------
- This project is a web-based Income and Expense Survey Tool designed to collect and analyze participants' data to aid in the launch of a new healthcare product. 
- The application is built using Flask for the backend, MongoDB for data storage, and Python for data processing and visualization.
--------------------------

## Project Structure

- ├── application.py
- ├── templates
- │   └── index.html
- ├── process_data.py
- ├── survey_data.csv
- ├── data_analysis.ipynb
- └── README.md
-------------------------

## Files Description

- **application.py**: Main Flask application file. This is the first file to be executed, which will render the 'index.html' file.
- **index.html**: Frontend HTML form for collecting survey data and submitting to the mongoDB database. Ensure that this file is in a folder named 'templates', as Flask automatically looks for 'index.html' in a 'templates' folder.
- **process_data.py**: Python Script for processing data, exporting data from MongoDB to CSV, loading CSV data into a DataFrame, and saving as 'survey_data.csv'.
- **survey_data.csv**: CSV file containing the survey data downloaded from the mongoDB database.
- **data_analysis.ipynb**: Jupyter Notebook for loading the downloaded csv file for data analysis and visualization.
- **README.md**: This is the file you have open, which gives you a detailed instruction on how to run the other files in the system and to properly execute the project.
------------------------------

## Requirements

- Python 3.x (Python 3.11.9 and below is recommended, as AWS hosting services are not yet compatible with Python 3.12)
- Flask
- pymongo
- pandas
- matplotlib
- seaborn
- MongoDB (Download and install the MongoDBCompass database application)
-----------------------------

## Setup Instructions

** Step 1: Install Dependencies**

Install the required Python packages using pip:

    pip install Flask pymongo pandas matplotlib seaborn
-----
**Step 2: Run the Flask Application**

- Ensure MongoDB is running on your local machine. Then, start the Flask application:

    python application.py

- Open a web browser and navigate to `http://127.0.0.1:5000` to access the rendered html survey form. 
- All submitted survey data via the form, goes to the mongoDB database.
------
**Step 3: Process Data**

- Run the data processing script to export the survey data from MongoDB to CSV and load it into a DataFrame:

    python process_data.py
-----
**Step 4: Data Analysis**

- Open the `data_analysis.ipynb` Jupyter Notebook to perform data analysis and generate visualizations. Ensure you have Jupyter Notebook installed, and start it with:

    jupyter notebook data_analysis.ipynb
----------------------------------------------------

## Hosting on AWS

**Step 1: Create an EC2 Instance**

1. Log in to the AWS Management Console.
2. Navigate to the EC2 Dashboard.
3. Click on "Launch Instance".
4. Choose an Amazon Machine Image (AMI) (e.g., Amazon Linux 2 AMI).
5. Select an instance type (e.g., t2.micro for free tier eligibility).
6. Configure instance details, add storage, and configure security group (allow HTTP (port 80) and SSH (port 22)).
7. Review and launch the instance, creating a new key pair for SSH access.
-----
**Step 2: Connect to Your EC2 Instance**

- Use the key pair created during the instance launch to connect via SSH
-----
**Step 3: Install Dependencies on EC2**

- Update the package manager and install required packages:

    sudo yum update -y
    sudo yum install python3 -y
    sudo yum install git -y

- Install pip and necessary Python packages:

    sudo amazon-linux-extras install python3.8
    python3 -m pip install Flask pymongo pandas matplotlib seaborn
-----
**Step 4: Deploy the Flask Application**

- Clone your project repository from GitHub or upload your project files to the EC2 instance
-----
**Step 5: Configure and Start the Flask Application**

- Ensure MongoDB is configured (either install MongoDB on the EC2 instance or use MongoDB Atlas for a managed solution).

- Start the Flask application:

    python3 application.py
-----
**Step 6: Configure Nginx as a Reverse Proxy**

- Install Nginx:

    sudo amazon-linux-extras install nginx1.12
    sudo service nginx start

- Configure Nginx to forward requests to the Flask application.

- Edit the Nginx configuration file. Add the following configuration within the `http` block:

    server {
        listen 80;
        server_name your-ec2-public-dns;

        location / {
            proxy_pass http://127.0.0.1:5000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }

- Restart Nginx to apply the changes:

    sudo service nginx restart
----
**Step 7: Access Your Application**

- Open a web browser and navigate to your EC2 instance's public DNS to access the Income and Expense Survey Tool. 
-------

_(Issue encountered: I had issues with my debit card registration during the AWS account signup process, but a friend's AWS account was used to practice.)_
