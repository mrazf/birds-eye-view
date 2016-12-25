## Synopsis

Example app that logs out the current ambient temperature of all the nest thermostats connected to an account.

## Installation

Developed against Python 3.4 but 2.x should probably work

To get it running:

Get the code `git clone https://github.com/mrazf/birds-eye-view.git`
cd `cd birds-eye-view`
Install packages `pip install -r requirements.txt`

Add your 'client_secret' into the authenticate.py and `python authenticate.py`
Follow the instructions and login with your nest account.

`python read.py` should then log out the temperature of your nests
