
from notifier.render import Renderer


def test_render_string():

    rnd = Renderer()
    rnd.set_vars({
        'VAR1': '42'
    })
    res = rnd.render('Check me {{VAR1}}')
    assert res == 'Check me 42'
