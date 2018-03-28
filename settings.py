import os
from configparser import ConfigParser

settings = ConfigParser()
settings.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), "settings.ini"))

USER_ID = settings["CONNECTION"]["User"]
BEARER = settings["CONNECTION"]["Bearer"]
HQ_URL = f"https://api-quiz.hype.space/shows/now?type=hq&userId={USER_ID}"
HQ_HEADERS = {"Authorization": f"Bearer {BEARER}",
              "x-hq-client": "Android/1.3.0"}


def get(section, key):
    value = settings[section][key]
    if value == "True":
        return True
    elif value == "False":
        return False
    return value



