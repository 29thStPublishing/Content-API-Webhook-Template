# A Content-API webhook template

## Preamble

This is a python app, using tornado. Uses `pip` as the package manager. Make sure you have python and pip installed on your system:

- python `python -V`
- pip `pip -V`

If you are missing these, please see [Downloading Python](https://wiki.python.org/moin/BeginnersGuide/Download).

- *virtualenv* check with: `virtualenv --version`. To install: `pip install virtualenv`

## Install

1. `git clone https://github.com/29thStPublishing/Content-API-Webhook-Template.git`
2. `cd Content-API-Webhook-Template`
3. Create a virtual environment in the project root. The directory named `venv/` is already gitignored, so let's call it that: `virtualenv venv`
4. Start up virtual environment using the command `source venv/bin/activate` (turn it off with `deactivate`)
5. With the virtualenv running use the command `pip install -r requirements.txt` to install the dependencies for this app.
6. `python app.py --dev=True`
