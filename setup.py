from setuptools import setup

setup(
    name='ci-slack-poster',
    version='0.1',
    py_modules=['notifier'],
    install_requires=[
        'Click', 'pytest', 'jinja2', 'requests'
    ],
    entry_points='''
        [console_scripts]
        slack_post=notifier:cli
    ''',
)
