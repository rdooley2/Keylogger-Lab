<h1>Visual Studio Code - Keylogger Development and Analysis</h1>

 ### [YouTube Demonstration]()

<h2>Description</h2>
This project utilizes Visual Studio Code to develop a Keylogger in Python. The primary objective is to gain insight into how certain malware might function, providing a hands-on understanding of its mechanics. This lab is strictly educational and is not intended for malicious use. The program records user keystrokes and writes them to a text file. Upon termination, the program sends an email with the keystrokes log file attached.



<h2>Languages and Utilities Used</h2>

- <b>Python</b> 


<h2>Environments Used </h2>

- <b>Visual Studio Code</b>

<h2>Project walk-through:</h2>

<p align="center">
Import libraries that allow for email creation and keyboard functions: <br/><br />
<img src="https://i.imgur.com/XKQ3ChE.png" height="80%" width="80%" alt="Keylogger Steps"/>
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
And we're done <br/><br />
