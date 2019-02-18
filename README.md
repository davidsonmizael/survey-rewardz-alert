# Survey Rewardz alert

[![Python 3.6](https://img.shields.io/badge/Python-3.5+-blue.svg)](https://www.python.org/downloads/release/python-360/)

Just a simple bot that will play a sound whenever you get a new survey.

## Getting Started

These instructions will tell you how to set up to run the code locally with your account.

### Prerequisites

- [Python](https://www.python.org/downloads/release/python-360/)
- [Pip](https://pypi.org/project/pip/)
- [EditThisCookie](http://www.editthiscookie.com/)

### Set up
##### Cookies
- Install the `EditThisCookie` expansion in your browser;
- Log into the *Survey Rewardz* website with your account;
- Click in the cookie icon and then click in **Export** to copy the cookies to your clipboard
- Paste these cookies into the file `cookies.json` and save

##### Install Dependencies

Use `pip` to install the dependencies listed in the file `requirements.txt`.
```sh
$ pip install -r requirements.txt
```
##### Alert sound
Feel free to download any `.wav` and use as your alert by simply replacing the file `untitled.wav` with yours.

### Running

To run you simply need to use your python to run the code.

```sh
$ python run.py
```

Whenever a survey is available for you, you will receive a sound alert and an ouput like this will show in your terminal.

```sh
MESSAGE: We have selected the following survey for you:
SURVEY NAME: Study
VALUE: $0.36
```

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)

