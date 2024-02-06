import mysql.connector
from joblisting import JobListing
from company import Company
from applicant import Applicant
from jobapplication import JobApplication
from datetime import datetime
class DatabaseConnector:
    def __init__(self):
        self.connection = None
    def create_tables(self):
        cursor = self.connection.cursor()

    def open_connection(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
        )
        self.create_database()
        self.connection.database = "careerhub"
        self.create_tables()

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def create_database(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS careerhub")
        except Exception as e:
            print(f"Error creating database: {e}")
        finally:
            cursor.close()


    def initialize_database(self):



        self.cursor.execute('''
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

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Companies (
                CompanyID INTEGER PRIMARY KEY,
                CompanyName TEXT,
                Location TEXT
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Applicants (
                ApplicantID INTEGER PRIMARY KEY,
                FirstName TEXT,
                LastName TEXT,
                Email TEXT,
                Phone TEXT,
                Resume TEXT
            )
        ''')

        self.cursor.execute('''
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

    def insert_job_listing(self, job):
        # Implement the insert_job_listing method
        self.cursor.execute('''
            INSERT INTO Jobs (CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (job.company_id, job.job_title, job.job_description, job.job_location, job.salary,
              job.job_type, job.posted_date))
        self.connection.commit()

    def insert_company(self, company):
        # Implement the insert_company method
        self.cursor.execute('''
            INSERT INTO Companies (CompanyName, Location)
            VALUES (?, ?)
        ''', (company.company_name, company.location))
        self.connection.commit()

    def insert_applicant(self, applicant):
        # Implement the insert_applicant method
        self.cursor.execute('''
            INSERT INTO Applicants (FirstName, LastName, Email, Phone, Resume)
            VALUES (?, ?, ?, ?, ?)
        ''', (applicant.first_name, applicant.last_name, applicant.email, applicant.phone, applicant.resume))
        self.connection.commit()

    def insert_job_application(self, application):
        # Implement the insert_job_application method
        self.cursor.execute('''
            INSERT INTO Applications (JobID, ApplicantID, ApplicationDate, CoverLetter)
            VALUES (?, ?, ?, ?)
        ''', (application.job_id, application.applicant_id, application.application_date, application.cover_letter))
        self.connection.commit()

    def get_job_listings(self):
        # Implement the get_job_listings method
        self.cursor.execute('SELECT * FROM Jobs')
        rows = self.cursor.fetchall()
        job_listings = [JobListing(*row) for row in rows]
        return job_listings

    def get_companies(self):
        self.cursor.execute('SELECT * FROM Companies')
        rows = self.cursor.fetchall()
        companies = [Company(*row) for row in rows]
        return companies

    def get_applicants(self):
        self.cursor.execute('SELECT * FROM Applicants')
        rows = self.cursor.fetchall()
        applicants = [Applicant(*row) for row in rows]
        return applicants

    def get_applications_for_job(self, job_id):
        self.cursor.execute('SELECT * FROM Applications WHERE JobID = ?', (job_id,))
        rows = self.cursor.fetchall()
        applications = [JobApplication(*row) for row in rows]
        return applications


from exceptions import NegativeSalaryError, DatabaseConnectionError


class DatabaseQueryError:
    pass


class DatabaseManager:
    def __init__(self, database_name):
        self.connection = mysql.connect(database_name)
        self.cursor = self.connection.cursor()



    def calculate_average_salary(self):
        try:
            self.cursor.execute('SELECT Salary FROM Jobs')
            salaries = self.cursor.fetchall()
            valid_salaries = [salary[0] for salary in salaries if salary[0] >= 0]
            if not valid_salaries:
                raise NegativeSalaryError("No valid salaries found.")
            average_salary = sum(valid_salaries) / len(valid_salaries)
            return average_salary
        except NegativeSalaryError as e:
            print(f"Error calculating average salary: {e}")
        except Exception as e:
            print(f"Error calculating average salary: {e}")

    def retrieve_job_listings(self):
        try:
            self.connect()
            self.cursor.execute("SELECT JobTitle, CompanyID, Salary FROM Jobs")
            job_listings = self.cursor.fetchall()
            return job_listings
        except DatabaseConnectionError as e:
            print(f"Database Connection Error: {e}")
        except DatabaseQueryError as e:
            print(f"Database Query Error: {e}")
        finally:
            self.disconnect()

    def create_applicant_profile(self, first_name, last_name, email, phone, resume):
        try:
            self.connect()
            self.execute_query(
                "INSERT INTO Applicants (FirstName, LastName, Email, Phone, Resume) VALUES (1, 2, 3, 4, 5)",
                (first_name, last_name, email, phone, resume))
            print("Applicant profile created successfully.")
        except DatabaseConnectionError as e:
            print(f"Database Connection Error: {e}")
        except DatabaseQueryError as e:
            print(f"Database Query Error: {e}")
        finally:
            self.disconnect()

    def submit_job_application(self, job_id, applicant_id, application_date, cover_letter):
        try:
            self.connect()
            self.execute_query(
                "INSERT INTO Applications (JobID, ApplicantID, ApplicationDate, CoverLetter) VALUES (1, 3, 5, 6)",
                (job_id, applicant_id, application_date, cover_letter))
            print("Job application submitted successfully.")
        except DatabaseConnectionError as e:
            print(f"Database Connection Error: {e}")
        except DatabaseQueryError as e:
            print(f"Database Query Error: {e}")
        finally:
            self.disconnect()

    def post_job_listing(self, company_id, job_title, job_description, job_location, salary, job_type, posted_date):
        try:
            self.connect()
            self.execute_query("INSERT INTO Jobs (CompanyID, JobTitle, JobDescription, JobLocation, "
                               "Salary, JobType, PostedDate) VALUES (1, 2, 3, 4, 5, 6, 7)",
                               (company_id, job_title, job_description, job_location, salary, job_type, posted_date))
            print("Job listing posted successfully.")
        except DatabaseConnectionError as e:
            print(f"Database Connection Error: {e}")
        except DatabaseQueryError as e:
            print(f"Database Query Error: {e}")
        finally:
            self.disconnect()

    def search_job_listings_by_salary_range(self, min_salary, max_salary):
        try:
            self.connect()
            self.cursor.execute("SELECT JobTitle, CompanyID, Salary FROM Jobs WHERE Salary BETWEEN ? AND ?",
                                (min_salary, max_salary))
            job_listings = self.cursor.fetchall()
            return job_listings
        except DatabaseConnectionError as e:
            print(f"Database Connection Error: {e}")
        except DatabaseQueryError as e:
            print(f"Database Query Error: {e}")
        finally:
            self.disconnect()




