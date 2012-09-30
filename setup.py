from setuptools import setup

setup(
    name='dynconf',
    author='Jorge E. Cardona',
    author_email='jorgeecardona@gmail.com',
    version='0.1',
    packages=['dynconf'],
    entry_points = {
        'console_scripts': [
            'dynconf = dynconf.cli:main'
            ]}
    )
