from googleapiclient.discovery import build
def create_job(client_service, job_to_be_created):
    try:
        request = {'job': job_to_be_created}
        job_created = client_service.projects().jobs().create(
            parent='projects/recogx-603c8', body=request).execute()
        print('Job created: %s' % job_created)
        return job_created
    except Error as e:
        print('Got exception while creating job')
        raise e

client_service = build('jobs', 'v3')
from random import randint
import string
rid =  randint(10000,99999)
application_info = {'uris': ['codart.com']}
job = {
    'companyName': 'projects/recogx-603c8/companies/5c6fb812-f31f-4ce7-86c8-189acbf5b3f4',
    'requisitionId': str(rid),
    'title': 'IOS Developer',
    'description': 'Full time iOS Developer. Pays 15,000 a month plus benefits.',
    "application_info": application_info
}

create_job(client_service, job)