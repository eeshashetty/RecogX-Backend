from googleapiclient.discovery import build

def create_company(client_service, company_to_be_created):
    try:
        request = {'company': company_to_be_created}
        company_created = client_service.projects().companies().create(
            parent='projects/recogx-603c8', body=request).execute()
        print('Company created: %s' % company_created)
        return company_created
    except Error as e:
        print('Got exception while creating company')
        raise e

client_service = build('jobs', 'v3')

from random import randint

# name = input('Name: ')
# displayName = input('Display Name: ')
# headquartersAddress = input('Headquarters: ')
# websiteUri = input('Company Website: ')
# keywords = []
# while True:
#     c = input('Enter Attribute (* to cancel) = ')
#     if(c=='*'):
#         break
#     keywords.append(c)

# sample = {
#     'displayName': 'Jade Vision Technologies Ltd',
#     'externalId': str(randint(100,9999)),
#     'headquartersAddress': 'Bengaluru',
#     'websiteUri': 'jade-vis.tech',
#     'keywordSearchableJobCustomAttributes': ['Computer Vision', 'NodeJS', 'Frontend']
# }
sample = {
    'displayName': 'Codart Systems Ltd',
    'externalId': str(randint(100,9999)),
    'headquartersAddress': 'Mumbai',
    'websiteUri': 'codart.com',
    'keywordSearchableJobCustomAttributes': ['IOS Developer', 'NodeJS', 'Frontend']
}
# company_new = {
#     'name': name,
#     'displayName': displayName,
#     'externalId': randint(100,9999),
#     'headquartersAddress': headquartersAddress,
#     'websiteUri': websiteUri,
#     'keywordSearchableJobCustomAttributes': keywords
# }



create_company(client_service, sample)