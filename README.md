<h1>Solve It </h1><br />
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

Solve_It is a Sublime Text 3 plugin which is used to submit the solution of problems of Codeforces directly from the Sublime Text just by pressing ('CTRL + M') on (Windows or Linux) or (Super + M) key on Mac OS.

## What it does
Solve_IT gets contest ID and problem Id from user and uses Selenium module of Python to submit currently active file of Sublime Text to Codeforces.

## Set Up Instructions

Assuming Google Chrome and Python3 is installed in your system.
<ul>
<li> Clone Solve_It repository in your home directory and open <strong> solve_it.py </strong> and change <strong> pathToPython </strong> by your python lib path.</li>
<li> Setup Selenium with ChromeDriver.</li>
<li> In Linux head over to 
    
    /home/{YOUR USERNAME}/.config/sublime-text-3/Packages/	
   and In Windows 
    
    C:/Users/{YOUR_USERNAME}/Appdata/Roaming/Sublime Text 3/Packages/' 
   and paste the cloned repository in this directory. </li>
<li> Now Setup Chrome so that Selenium may Connect to the existing Chrome Session. </li>
<ul>
<li>	First Make a directory in the desired location with name <strong> Google </strong> and make sure the path to chrome executable is added to the environment variable path. </li>

<li> Now Close all the instances of the Google Chrome. </li>
<li> In Linux run this command in your terminal
  
 	google-chrome --remote-debugging-port=9222 --user-data-dir="path/to/Google"
you can specify any port that is open but if you do then you need to change the <strong> port number </strong> in <strong> solve_it.py </strong> file </li>
 	
<li>This command will open the browser and all the information of your login in Chrome and Codeforces will be Stored there. So you don't need to login when you open this session again. You need to log in only for the first type. </li>

<li><strong>Solve_It</strong> plugin will work only when the Chrome is opened by this command. So make sure you open Codeforces in this browser session. </li>
</ul>
<li> You need to do the same thing in Windows. The only thing which change is this command

    chrome.exe --remote-debugging-port=9222 --user-data-dir="path/to/Google"	
</li>
</ul>
