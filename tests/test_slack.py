import json

from notifier.slack import post_message


def test_post_simple():
    payload = {
        'text': 'Hello',
        'channel': 'gocd-pipelines',
        'icon_emoji': ':crying_cat_face:',
        'displayname': 'test',
    }

    assert post_message(json.dumps(payload))
