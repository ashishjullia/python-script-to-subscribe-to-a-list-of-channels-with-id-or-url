# Python Script to Subscribe to a List of Channels with ID or URL

This is a simple Python script that allows you to subscribe to a list of YouTube channels using either their channel IDs or channel URLs.

This project was bootstrapped using `ChatGPT`.

## Requirements
- Python 3.x
- Google API client library
- Google Authentication credentials

## Setup
1. Clone this repository using `git clone https://github.com/ashishjullia/python-script-to-subscribe-to-a-list-of-channels-with-id-or-url.git`.
2. Create a project on the [Google Cloud Console](https://console.cloud.google.com/).
3. Enable the YouTube Data API v3 in your project and create a set of authentication credentials (OAuth 2.0 client ID).
4. Download the JSON file containing your client ID and client secret and save it as `client_secret.json` in the root directory of the cloned repository.
5. Install the required Python packages by running `pip install -r requirements.txt` in your terminal.

## Usage
1. Open `subscribe.py` in your text editor of choice.
2. Replace the contents of `channel_ids.csv` with a list of YouTube channel IDs or channel URLs that you want to subscribe to.
3. Run `python subscribe.py` in your terminal to subscribe to the channels.

**Note**: As per the quota of free API access, a user can only subscribe to a maximum of 200 YouTube channels in a 24-hour period. If you exceed this limit, your requests will be rejected by the YouTube API.

## Disclaimer
This script is intended for educational purposes only. Use it at your own risk. The developer is not responsible for any misuse of this script or any damage caused by it.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more information.
