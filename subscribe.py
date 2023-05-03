import csv
import os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
# from google.oauth2 import  InstalledAppFlow
from google.oauth2.credentials import Credentials
# from google.oauth2 import  client
from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import csv
import os

# Set up the YouTube Data API client with OAuth2 authentication
CLIENT_SECRETS_FILE = 'client_secrets.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def get_authenticated_service():
    # Load the client secrets file and obtain an access token
    credentials = None
    if os.path.exists('token.json'):
        credentials = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            credentials = flow.run_local_server(port=0)
        with open('token.json', 'w') as token_file:
            token_file.write(credentials.to_json())

    # Build the YouTube Data API client with the access token
    youtube = build(API_NAME, API_VERSION, credentials=credentials)
    return youtube

# Define a function to subscribe to a YouTube channel given its channel ID
def subscribe_to_channel(youtube, channel_id):
    try:
        # Call the YouTube Data API's subscriptions.insert method to subscribe to the channel
        subscription = youtube.subscriptions().insert(
            part='snippet',
            body={
                'snippet': {
                    'resourceId': {
                        'kind': 'youtube#channel',
                        'channelId': channel_id
                    }
                }
            }
        ).execute()

        print(f"Subscribed to channel '{subscription['snippet']['title']}' (ID: {channel_id})")

    except HttpError as e:
        print(f"An error occurred while trying to subscribe to channel ID {channel_id}: {e}")

# Read the CSV file containing channel IDs
with open('channel_ids.csv') as f:
    reader = csv.reader(f)

    # Get an authenticated YouTube Data API client
    youtube = get_authenticated_service()

    # Iterate over each row in the CSV file
    for row in reader:
        channel_id = row[0]

        # Call the subscribe_to_channel function to subscribe to the channel
        subscribe_to_channel(youtube, channel_id)
