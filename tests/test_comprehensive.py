import json
import os
import requests

hook_url = os.environ['HOOK_URL']


def test_post_simple():
    payload = {
        'text': 'Hello',
        'channel': 'gocd-pipelines',
        'icon_emoji': ':crying_cat_face:',
        'displayname': 'test',
    }
    r = requests.post(hook_url, data=json.dumps(payload))
    assert r.status_code == 200

