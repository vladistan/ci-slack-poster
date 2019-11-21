import os

import requests

hook_url = os.environ['HOOK_URL']


def post_message(message):
    r = requests.post(hook_url, data=message)
    return r.status_code == 200
