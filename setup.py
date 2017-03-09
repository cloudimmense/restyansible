from distutils.core import setup

setup(
    name = 'restyansible',
    version = '0.0.1',
    description = 'A flask server over ansible',
    author = 'samvaran kashyap rallabandi',
    author_email = 'samvaran.kashyap@gmail.com',
    url = '',
    install_requires=[
    'flask',
    'ansible'
    # list of this package dependencies
    ]
)
