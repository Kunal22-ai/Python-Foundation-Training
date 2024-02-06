from datetime import datetime

class JobApplication:
    def __init__(self, application_id, job_id, applicant_id, application_date, cover_letter):
        self.application_id = application_id
        self.job_id = job_id
        self.applicant_id = applicant_id
        self.application_date = application_date
        self.cover_letter = cover_letter

    def get_application_details(self):
        return {
            "ApplicationID": self.application_id,
            "JobID": self.job_id,
            "ApplicantID": self.applicant_id,
            "ApplicationDate": self.application_date,
            "CoverLetter": self.cover_letter
        }


from exceptions import DeadlineExceededError

class JobApplication:
    def __init__(self, application_id, job_id, applicant_id, application_date, cover_letter, deadline):
        self.application_id = application_id
        self.job_id = job_id
        self.applicant_id = applicant_id
        self.application_date = application_date
        self.cover_letter = cover_letter
        self.deadline = deadline

    def submit_application(self):
        current_date = datetime.now()
        if current_date > self.deadline:
            raise DeadlineExceededError("Application deadline has passed. Applications are no longer accepted.")
        else:
            # Proceed with application submission
            pass
