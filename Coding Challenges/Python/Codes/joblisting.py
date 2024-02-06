from datetime import datetime

class JobListing:
    def __init__(self, job_id, company_id, job_title, job_description, job_location, salary, job_type, posted_date):
        self.job_id = job_id
        self.company_id = company_id
        self.job_title = job_title
        self.job_description = job_description
        self.job_location = job_location
        self.salary = salary
        self.job_type = job_type
        self.posted_date = posted_date
        self.applicants = []  # List to store applicants

    def apply(self, applicant_id, cover_letter):
        application_date = datetime.now()
        application = {"applicant_id": applicant_id, "cover_letter": cover_letter, "application_date": application_date}
        self.applicants.append(application)

    def get_applicants(self):
        return self.applicants

    def get_job_details(self):
        return {
            "JobID": self.job_id,
            "CompanyID": self.company_id,
            "JobTitle": self.job_title,
            "JobDescription": self.job_description,
            "JobLocation": self.job_location,
            "Salary": self.salary,
            "JobType": self.job_type,
            "PostedDate": self.posted_date
        }

