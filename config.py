import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_TOKEN =getenv("API_TOKEN","")
OPEN_AI = getenv("OPEN_AI","")
