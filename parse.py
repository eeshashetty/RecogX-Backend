from google.cloud import documentai_v1beta2 as documentai


def parse_form(project_id='YOUR_PROJECT_ID',
               input_uri='gs://cloud-samples-data/documentai/form.pdf'):
    """Parse a form"""

    client = documentai.DocumentUnderstandingServiceClient()

    gcs_source = documentai.types.GcsSource(uri=input_uri)

    # mime_type can be application/pdf, image/tiff,
    # and image/gif, or application/json
    input_config = documentai.types.InputConfig(
        gcs_source=gcs_source, mime_type='application/pdf')

    # Improve form parsing results by providing key-value pair hints.
    # For each key hint, key is text that is likely to appear in the
    # document as a form field name (i.e. "DOB").
    # Value types are optional, but can be one or more of:
    # ADDRESS, LOCATION, ORGANIZATION, PERSON, PHONE_NUMBER, ID,
    # NUMBER, EMAIL, PRICE, TERMS, DATE, NAME
    key_value_pair_hints = [
        documentai.types.KeyValuePairHint(key='Emergency Contact',
                                          value_types=['NAME']),
        documentai.types.KeyValuePairHint(
            key='Referred By')
    ]

    # Setting enabled=True enables form extraction
    form_extraction_params = documentai.types.FormExtractionParams(
        enabled=True, key_value_pair_hints=key_value_pair_hints)

    # Location can be 'us' or 'eu'
    parent = 'projects/{}/locations/us'.format(project_id)
    request = documentai.types.ProcessDocumentRequest(
        parent=parent,
        input_config=input_config,
        form_extraction_params=form_extraction_params)

    document = client.process_document(request=request)
    text = document.text
    t = text.split('\n')
    skills = []
    for i in range(0,len(t)):
        x = t[i]
        if 'SKILLS' in x:
            j = i+1
            y = t[j]
            while("●" in y or "•" in y or y.isupper()==False):
                new_y = y.replace("●", "")
                new_y = new_y.replace("•", "")
                skills.append(new_y)
                j+=1
                y = t[j]
    return skills
   

# projectId = 'recogx-603c8'
# gcsInputUri = 'gs://recogx-603c8.appspot.com/Resume.pdf'

# skills = parse_form(project_id=projectId, input_uri=gcsInputUri)
# print(skills)
