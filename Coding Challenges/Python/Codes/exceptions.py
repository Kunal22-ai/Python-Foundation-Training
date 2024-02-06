from datetime import datetime
from jobapplication import JobApplication
from applicant import Applicant
from company import Company
from joblisting import JobListing


import mysql.connector

class InvalidEmailError(Exception):
    def __init__(self, message="Invalid email format. Please provide a valid email address."):
        self.message = message
        super().__init__(self.message)

class NegativeSalaryError(Exception):
    def __init__(self, message="Salary must be a non-negative value."):
        self.message = message
        super().__init__(self.message)

class FileUploadError(Exception):
    def __init__(self, message="Error uploading file."):
        self.message = message
        super().__init__(self.message)

class DeadlineExceededError(Exception):
    def __init__(self, message="Application deadline has passed. Applications are no longer accepted."):
        self.message = message
        super().__init__(self.message)

class DatabaseConnectionError(Exception):
    def __init__(self, message="Error establishing a database connection."):
        self.message = message
        super().__init__(self.message)

class DatabaseConnector:
    def __init__(self):
        self.connection = None

    def open_connection(self, host, user, password, database):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
        except mysql.connector.Error as e:
            raise DatabaseConnectionError(str(e))

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def create_database(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS careerhub")
            cursor.close()
            self.connection.database = "careerhub"
        except mysql.connector.Error as e:
            raise DatabaseConnectionError(str(e))

    def create_tables(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Jobs (
                    JobID INTEGER PRIMARY KEY,
                    CompanyID INTEGER,
                    JobTitle TEXT,
                    JobDescription TEXT,
                    JobLocation TEXT,
                    Salary REAL,
                    JobType TEXT,
                    PostedDate DATETIME
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Companies (
                    CompanyID INTEGER PRIMARY KEY,
                    CompanyName TEXT,
                    Location TEXT
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Applicants (
                    ApplicantID INTEGER PRIMARY KEY,
                    FirstName TEXT,
                    LastName TEXT,
                    Email TEXT,
                    Phone TEXT,
                    Resume TEXT
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Applications (
                    ApplicationID INTEGER PRIMARY KEY,
                    JobID INTEGER,
                    ApplicantID INTEGER,
                    ApplicationDate DATETIME,
                    CoverLetter TEXT,
                    FOREIGN KEY (JobID) REFERENCES Jobs(JobID),
                    FOREIGN KEY (ApplicantID) REFERENCES Applicants(ApplicantID)
                )
            ''')

            self.connection.commit()
            cursor.close()
        except mysql.connector.Error as e:
            raise DatabaseConnectionError(str(e))


