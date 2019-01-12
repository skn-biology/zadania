# Setup

* Install (python3)[https://www.python.org/downloads/]
* Install (virtualenvwrapper)[https://virtualenvwrapper.readthedocs.io/en/latest/install.html] (skip this step if you want to create a virtualenv via e.g. PyCharm)
  - linux, mac: `pip install virtualenvwrapper`
  - windows: `pip install virtualenvwrapper-win`
  - windows PowerShell: `pip install virtualenvwrapper-powershell`
* Add a new virualenv:

    mkvirtualenv -p <path to python3> zadania

on a Slackware machine this will be:

    mkvirtualenv -p /usr/bin/python3 zadania

* Install all requirements:

    python setup.py develop

# What to do

Once you have the project set up, you can proceed to solving the exercises. Simply open the file you
want to solve and fill in the functions so that they work according to their descriptions.

# How to check your solutions

Run pytest:

 * all tests: `pytest -v`
 * only tests in a given file/folder: `pytest <path to file/s>`, e.g. `pytest tests/test_something.py`
 * only tests which start with a given prefix: `pytest -k <prefix>`, e.g. `pytest -k test_my_function`

# What else to keep in mind

* Most code is written once, but read multiple times, so make sure yours is readable:
  - conform with (PEP8)[https://www.python.org/dev/peps/pep-0008/] (try `pylama` for hints)
  - add docstrings to your functions
* (DRY)[https://en.wikipedia.org/wiki/Don%27t_repeat_yourself] and (KISS)[https://en.wikipedia.org/wiki/KISS_principle]
* Use standard functions if possible - they're usually better
* The debugger is your friend: `import  pdb; pdb.set_trace()` is something worth using from time to time