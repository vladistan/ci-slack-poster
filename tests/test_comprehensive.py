import json

from notifier.render import Renderer
from notifier.slack import post_message
from tests.util import fixture_path


def test_render_and_post():
    rnd = Renderer()
    rnd.use_os_env()
    text = rnd.parse_file(fixture_path('complex_message.json'))
    assert post_message(text)
