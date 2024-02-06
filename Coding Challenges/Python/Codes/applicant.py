from datetime import datetime
from jobapplication import JobApplication

class Applicant:
    def __init__(self, applicant_id, first_name, last_name, email, phone, resume):
        self.applicant_id = applicant_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.resume = resume
        self.applied_jobs = []  # List to store applied jobs

    def create_profile(self, email, first_name, last_name, phone):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def apply_for_job(self, job_id, cover_letter):
        application_id = len(self.applied_jobs) + 1
        application_date = datetime.now()
        job_application = JobApplication(application_id, job_id, self.applicant_id, application_date, cover_letter)
        self.applied_jobs.append(job_application)
        return job_application

    def get_applied_jobs(self):
        return self.applied_jobs

    def get_applicant_details(self):
        return {
            "ApplicantID": self.applicant_id,
            "FirstName": self.first_name,
            "LastName": self.last_name,
            "Email": self.email,
            "Phone": self.phone,
            "Resume": self.resume
        }


from exceptions import InvalidEmailError

class Applicant:
    def __init__(self, applicant_id, first_name, last_name, email, phone, resume):
        self.applicant_id = applicant_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.resume = resume

    def create_profile(self, email, first_name, last_name, phone):
        try:

            self.validate_email(email)
        except InvalidEmailError as e:
            print(f"Error: {e}")

    def validate_email(self, email):

        if "@" not in email or "." not in email:
            raise InvalidEmailError()


from exceptions import FileUploadError
class Applicant:
    def __init__(self):


        def upload_resume(self, resume_file):
            try:

                with open(resume_file, 'rb') as file:

                    pass
            except FileNotFoundError:
                raise FileUploadError("File not found. Please check the file path.")
            except IOError as e:
                raise FileUploadError(f"Error uploading file: {e}")
            except Exception as e:
                raise FileUploadError(f"Unknown error occurred: {e}")
