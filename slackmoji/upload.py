import os
import sys
import requests
import browsercookie

from bs4 import BeautifulSoup

team_name = input("Enter your team name: ")
folder_path = input("Enter path to folder that contains emojis: ")
session_cookie = browsercookie.chrome()
url = "https://{}.slack.com/customize/emoji".format(team_name)

for file in os.listdir(folder_path):
    emoji_name = os.file.splitext(os.path.basename(file))[0]

    print("Processing {}...".format(emoji_name))

    # Need to get the page and generate a crumb to spoof the Slack API
    r = requests.get(url, cookies=session_cookie)
    r.raise_for_status()
    page_text = BeautifulSoup(r.text)
    crumb = page_text.find("input", attrs={"name": "crumb"})["value"]

    # Generate payload data for POST request
    data = {
        "name": emoji_name,
        "add": 1,
        "crumb": crumb,
        "mode": data
    }

    emoji = {
        "img": open(file, "rb")
    }

    # Upload emoji
    print("Uploading {}...".format(emoji_name))

    r = requests.post(url, cookies=session_cookie, data=data, files=emoji, allow_redirects=False)
    r.raise_for_status()

    print("{} upload complete!".format(emoji_name))
