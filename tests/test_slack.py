import json
import os

from notifier.render import Renderer

fixtures_dir = os.path.join(os.path.dirname(__file__), 'fixtures')


def fixture_path(name):
    return os.path.join(fixtures_dir, name)


def test_render_string():
    rnd = Renderer()
    rnd.set_vars({
        'VAR1': '42'
    })
    res = rnd.render('Check me {{VAR1}}')
    assert res == 'Check me 42'


def test_correct_render_json():
    rnd = Renderer()
    rnd.set_vars({
        'USER': 'John',
        'USER_E': 'Jorge',
        'USER_W': 'Jack',
    })
    text = rnd.parse_file(fixture_path('tmpl_simple.json'))
    rsp = json.loads(text)
    assert rsp['Hello'] == 'John'
    assert rsp['Hola'] == 'Jorge'
    assert rsp['Hi'] == 'Jack'


def test_render_with_envs():

    rnd = Renderer()
    rnd.use_os_env()
    text = rnd.parse_file(fixture_path('tmpl_simple.json'))
    rsp = json.loads(text)
    os = rsp['OS']

    assert os['Path'] != ''
    assert os['User'] != ''
    assert os['Term'] != ''




