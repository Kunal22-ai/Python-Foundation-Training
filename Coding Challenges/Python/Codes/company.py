from datetime import datetime
from joblisting import JobListing

class Company:

    def __init__(self, company_id, company_name, location):
        self.company_id = company_id
        self.company_name = company_name
        self.location = location
        self.job_listings = []  # List to store job listings

    def post_job(self, job_title, job_description, job_location, salary, job_type):
        job_id = len(self.job_listings) + 1
        posted_date = datetime.now()
        job_listing = JobListing(job_id, self.company_id, job_title, job_description, job_location, salary,
                                 job_type, posted_date)
        self.job_listings.append(job_listing)
        return job_listing

    def get_jobs(self):
        return self.job_listings

    def get_company_details(self):
        return {
            "CompanyID": self.company_id,
            "CompanyName": self.company_name,
            "Location": self.location
        }

