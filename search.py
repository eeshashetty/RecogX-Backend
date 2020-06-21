import os

from googleapiclient.discovery import build
from googleapiclient.errors import Error

client_service = build('jobs', 'v3')
project_id = 'projects/' + os.environ['GOOGLE_CLOUD_PROJECT']
def get_jobs(query):
    job_query = {'query': query}
    company_final = []
    title_final = []
    desc_final = []
    # 1) Define RequestMetadata object
    request_metadata = {
        'domain':     'recogx.tech',
        'session_id': 'a5ed434a3f5089b489576cceab824f25',
        'user_id':    '426e428fb99b609d203c0cdb6af3ba36',
    }

    try:
        # 2) Throw RequestMetadata object in a request
        request = {
            'request_metadata': request_metadata,
            'job_query': job_query
        }

        # 3) Make the API call
        response = client_service.projects().jobs().search(
            parent=project_id, body=request).execute()
        
        response_comp = client_service.projects().companies().list(
                parent=project_id).execute()
        companies = response_comp.get('companies')
        # 4) Inspect the results
        if response.get('matchingJobs') is not None:
            # print('Search Results:')
            for job in response.get('matchingJobs'):
                for comp in companies:
                    if comp.get('name')==job.get('job').get('companyName'):
                        company_final.append(comp.get('displayName'))
                title_final.append(job.get('job').get('title'))
                desc_final.append(job.get('searchTextSnippet'))
        else:
            return "","","","No Jobs Found"
   
    except Error as e:
        # Alternate 3) or 4) Surface error if things don't work.
        print('Got exception while searching')
        raise e
    return company_final, title_final, desc_final, None