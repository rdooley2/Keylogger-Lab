<h1>Visual Studio Code - Keylogger Development</h1>

<h2>Overview</h2>
This project utilized Visual Studio Code to develop a Keylogger in Python. This lab is strictly educational and is not intended for malicious use. This project aimed to achieve the following goals:
<br><br>
<ul>
 <li>Understand how python, or coding languages in general, can interact with our devices</li>
 <li>Learn more about the libraries and functions python offers</li>
 <li>Gain insight on how a keylogger functions</li>
 <ul><li>Understanding how malware works can help professionals detect, prevent, and respond to threats</li></ul>
</ul>
<h2>Summary</h2>
The program records user keystrokes and writes them to a text file. Upon termination, the program sends an email with the keystrokes log file attached.

<h2>Languages and Utilities Used</h2>

- <b>Python</b> 
- <b>Visual Studio Code</b>

<h2>Project walk-through:</h2>

<p align="center">
Import libraries that allow for email creation and keyboard functions: <br/><br />
<img src="https://i.imgur.com/WtrXHbH.png" height="80%" width="80%" alt="Keylogger Steps"/>
<br />
<br />
<br />
Build the keyPressed function that creates and appends to a log file: <br/><br />
<img src="https://i.imgur.com/970vsLC.png" height="80%" width="80%" alt="Keylogger Steps"/>
<br />
<br />
<br />
Add a try block that stores the most recent keystroke in a char variable and writes it to the log file: <br/><br />
<img src="https://i.imgur.com/Ay6zW8c.png" height="80%" width="80%" alt="Keylogger Steps"/>
<br />
<br />
<br />
Add an except block that deals with special characters such as tab and enter and write it to the log file manually: <br/><br />
<img src="https://i.imgur.com/RWmsJh7.png" height="80%" width="80%" alt="Keylogger Steps"/>
<br />
<br />
<br />
Build the send_email function and have it store important information as variables: <br/><br />
<img src="https://i.imgur.com/KGRA9s2.png" height="80%" width="80%" alt="Keylogger Steps"/>
<br />
<br />
<br />
Implement email creation and connection logic: <br/><br />
<img src="https://i.imgur.com/MNUhkRD.png" height="80%" width="80%" alt="Keylogger Steps"/>
<br />
<br />
<br />
Build the main function that will only execute code when the code is manually run: <br/><br />
<img src="https://i.imgur.com/0Y7eoMi.png" height="80%" width="80%" alt="Keylogger Steps"/>
<br />
<br />
<br />
Example keystroke log after testing: <br/><br />
<img src="https://i.imgur.com/grD2u61.png" height="80%" width="80%" alt="Keylogger Steps"/>
<br />
<br />
<br />
 
<h2>Program demonstration:</h2>
 <p align="center">
And we're done <br/><br />
