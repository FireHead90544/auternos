# Auternos
Automate starting of Aternos Minecraft servers with a Discord bot.

***Warning:*** **This is really dumb. You put your Aternos login info into a plaintext python script. I will look into making it more intiutive, but for now it's kinda a poop thing I use for my friends and I.**

#### Video Demonstration:
![Demonstration](https://i.imgur.com/uloHx0k.gif)

[Mirror on Streamable](https://streamable.com/2s87xi)

# Guide
A couple of notes before we start:

I set this up using [ungoogled-chromium](https://ungoogled-software.github.io/ungoogled-chromium-binaries/), simply because the binaries were easily available to me.

This script kills any instance of Chromium (or if you're on Windows, it kills 'chrome.exe', so Chrome / Chromium will get killed) at the end of it. Solution: Either rewrite the portion of this script that kills Chrome / Chromium (and maybe submit a pull request too?), or use Firefox (chad browser) like me. Edit: idk might swap to PhantomJS, we'll see.

Chromium-based browsers require [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/) for this script to work. Make sure you have that properly set up. macOS users can do 
`brew cask install chromedriver` via [brew](https://brew.sh/).

## Really the guide now

Download the repo either from https://github.com/hipeopeo/auternos/archive/master.zip, or
`git clone https://github.com/hipeopeo/auternos`

#### Open auternos.py in your text editor (Windows users, don't use Notepad. It will mess up the files. I suggest [Notepad++](https://notepad-plus-plus.org/) instead.)

Change `driver = webdriver.Chrome('/path/to/bin/chromedriver')` to wherever you put chromedriver. For example, if you use Windows, and put 'chromedriver.exe' in your Documents, the path would be 'C:\Users\User\Documents\chromedriver.exe'.

Change `options.binary_location = "/path/to/bin/chromium"` to wherever you put your Chromium (or whatever you are using) binary. For example, if you use Windows, and put 'chromium.exe' in your Documents, the path would be 'C:\Users\User\Documents\chromium.exe'

Change 'username' in `text_area.send_keys("username")` to your Aternos username.

Change 'password' in `text_area.send_keys("password")` to your Aternos password.

This next step depends on what OS you are running, and what browser you chose.

For Linux, it should work, and kill all Chromium processes.

For Windows, change `os.system("killall chromium")` to `os.system("taskkill /f /im chrome.exe")`, and it will kill all Chromium / Chrome processes.

For macOS, change `os.system("killall chromium")` to whatever the process is named. For example" `os.system('killall "Google Chrome"')` for normal Chrome, and probably something similar for Chromium.

Remove this line if you do not want to kill any processes.

#### Open bot.py in your text editor.

You will need to create a Discord bot at https://discord.com/developers/applications. Generate a token (*Not* Client ID or Client Secret), and copy it.

Change "token" in `client.run('token')` to your bot token.

#### Running

Install the latest python (I am using 3.8.3) from  https://python.org/

Install the dependencies `python -m pip install discord.py selenium webdriver-manager`

Run the bot with `python bot.py`

Done!
