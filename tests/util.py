import os

fixtures_dir = os.path.join(os.path.dirname(__file__), 'fixtures')


def fixture_path(name):
    return os.path.join(fixtures_dir, name)
