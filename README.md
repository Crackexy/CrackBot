# CrackBot

## Use Repo At Your Own Risk...
![Enterprise](https://telegra.ph/file/3feaa0629756e0e45a2b7.jpg)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)



Best User Bot To Manage Your Telegram Account 
## Best, Powerful, And Safest Userbot.

## CrackBot By [Crackexy](t.me/Crackexy).

### For any query or to know how it works join Group And Channel 

<a href="https://t.me/CrackbotSupport"><img src="https://img.shields.io/badge/Join-Telegram%20Channel-red.svg?logo=Telegram"></a>
<a href="https://t.me/CrackbotUB"><img src="https://img.shields.io/badge/Join-Telegram%20Group-blue.svg?logo=telegram"></a>

## HOW TO DEPLOY 





## Installing Heroku 

### The Easy Way
[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Crackexy/CrackBot)

## GET STRING SESSION FROM REPL RUN 

## [![Get String Session online](https://repl.it/badge/github/Crackexy/StringSession)](https://stringsession.crackexy.repl.run/)


### The Simple Way

Simply clone the repository and run the main file:
```sh
git clone https://github.com/starkGang/Fridayuserbot
cd Userbot
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m userbot
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```


### UniBorg Configuration


The UniBorg Config is situated in `userbot/uniborgConfig.py`.

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.

