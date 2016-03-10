from oauth2client.client import GoogleCredentials
credentials = GoogleCredentials.get_application_default()
credentials.get_access_token()
print credentials.access_token
