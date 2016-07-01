import os
import sys
import requests
import browser_cookie

team_name = input("Enter your team name: ")
folder = input("Enter path to folder that contains emojis: ")
session_cookie = browser_cookie.chrome()
url = "https://{}.slack.com/customize/emoji"
