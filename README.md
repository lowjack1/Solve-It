# Solve It
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/lowjack1/Solve-It/pulls)
[![Code Grade](https://www.code-inspector.com/project/14400/status/svg)](https://frontend.code-inspector.com/public/project/14400/Solve-It/dashboard)
[![Code Quality Score](https://www.code-inspector.com/project/14400/score/svg)](https://frontend.code-inspector.com/public/project/14400/Solve-It/dashboard)

#### Solve It is a Sublime Text 3 plugin which is used to submit the solution of problems of Codeforces directly from the Sublime Text just by pressing ('CTRL + M') on (Windows or Linux) or ('Super + M') key on Mac OS.

## What it does
Solve IT gets contest ID and problem ID from user and uses Selenium module of Python to submit currently active file of Sublime Text to Codeforces.

## Set Up Instructions

Assuming Google Chrome and Python3 is installed in your system.
* Clone Solve-It repository in your home directory.
* Setup Selenium with ChromeDriver.
* Copy urllib3 and selenium module of Python from Python library and paste it to `sublime-text-3/Lib/Python3.3` folder.
* In Linux head over to `/home/{YOUR USERNAME}/.config/sublime-text-3/Packages/` <br> and in Windows 
`C:/Users/{YOUR_USERNAME}/Appdata/Roaming/Sublime Text 3/Packages/` <br> and paste the cloned repository in this directory.
* Now Setup Chrome so that Selenium may Connect to the existing Chrome Session.
  *	First Make a directory in the desired location with name **Google** and make sure the path to chrome executable is added to the environment variable path.

  * Now Close all the instances of the Google Chrome.
  * In Linux run this command in your terminal <br>`google-chrome --remote-debugging-port=9222 --user-data-dir="path/to/Google"` <br>
you can specify any port which is open but if you do then you need to change the **port number** in **solve_it.py** file.
 	
  * This command will open the browser and all the information of your login in Chrome and Codeforces will be Stored there. So you don't need to login when you open this session again. You need to log in only for the first type. 

  * **Solve_It** plugin will work only when the Chrome is opened by this command. So make sure you open Codeforces in this browser session.

* You need to do the same thing in Windows. The only thing which change is this command <br>
`chrome.exe --remote-debugging-port=9222 --user-data-dir="path/to/Google"`	

