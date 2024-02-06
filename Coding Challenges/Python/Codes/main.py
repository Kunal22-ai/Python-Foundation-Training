from datetime import datetime
from jobapplication import JobApplication
from applicant import Applicant
from company import Company
from joblisting import JobListing

# Example usage of JobApplication
job_application = JobApplication(
    application_id=1,
    job_id=1,
    applicant_id=1,
    application_date=datetime.now(),
    cover_letter="I am interested in this position."
)

application_details = job_application.get_application_details()
print("Job Application Details:", application_details)
print()

# Example usage of Applicant
applicant = Applicant(
    applicant_id=1,
    first_name="kunal",
    last_name="Mishra",
    email="kunal.22@gmail.com",
    phone="9823567128",
    resume="path/to/resume.pdf"
)

applicant.create_profile(
    email="akash.ded@gmail.com",
    first_name="akash",
    last_name="dedhi",
    phone="1234567890"
)

applicant.apply_for_job(
    job_id=1,
    cover_letter="I am applying for the job."
)

print()

# Example usage of Company
company = Company(
    company_id=1,
    company_name="Tech Solutions",
    location="City Center"
)

company.post_job(
    job_title="Software Engineer",
    job_description="Developing innovative software solutions",
    job_location="Tech Park",
    salary=80000.0,
    job_type="Full-time"
)

jobs_posted = company.get_jobs()
print("Jobs Posted by the Company:", jobs_posted)
print()

# Example usage of JobListing
job_listing = JobListing(
    job_id=1,
    company_id=1,
    job_title="Data Analyst",
    job_description="Analyzing and interpreting complex data sets",
    job_location="Downtown",
    salary=60000.0,
    job_type="Part-time",
    posted_date=datetime.now()
)

job_listing.apply(applicant_id=1, cover_letter="I have relevant experience.")
applicants_list = job_listing.get_applicants()
print("Applicants for the Job Listing:", applicants_list)
