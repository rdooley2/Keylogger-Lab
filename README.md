<h1>Keylogger Development in Python using VSCode</h1>

<h2>Overview</h2>
This project utilized Visual Studio Code to develop a Keylogger in Python. This lab is strictly educational and does not serve malicious use. This project aimed to achieve the following goals:
<br><br>
<ul>
 <li>Understand how Python, or coding languages in general, can interact with our devices</li>
 <li>Learn more about the libraries and functions Python offers</li>
 <li>Gain insight on how a keylogger functions</li>
 <ul><li>Understand how malware functions</li></ul>
</ul>
<h2>Summary</h2>
This program records user keystrokes and writes them to a text file. Upon termination, the program emails the attacker with the keystrokes log file attached. I want to acknowledge that a keylogger has much more potential than I've coded. However, I am uncomfortable developing a fully-fledged keylogger that the whole internet can view. A normal keylogger, upon execution by an unknowing party, would establish persistence within a system. Persistence can be as simple as having the code hide itself in AppData and then creating a shortcut to itself in the Windows startup folder. It starts at machine startup and automatically sends the email at system shutdown. 

<h2>Languages and Utilities Used</h2>

- <b>Python</b> 
- <b>Visual Studio Code</b>

<h2>Program walk-through:</h2>

<p align="center">
In the first section, I wrote all of the import statements. Most of these are for crafting the email at shutdown:  <br/><br />
<img src="https://i.imgur.com/wqtLnXg.png" height="50%" width="50%" alt="Keylogger Steps"/>
<br />
<br />
<br />
This next section of the code deals with email creation. In this first part, I created all the variables needed to craft an email. I also blacked out the smtp_pass variable because it ties to my email account: <br/><br />
<img src="https://i.imgur.com/VliSp0L.png" height="50%" width="50%" alt="Keylogger Steps"/>
<br />
<br />
<br />
This section creates the email. It is similar to clicking the create email button in Gmail and being greeted with an empty email that you would fill out:  <br/><br />
<img src="https://i.imgur.com/v2cJfGt.png" height="30%" width="30%" alt="Keylogger Steps"/>
<br />
<br />
<br />
Next, this block of code opens keystrokes.txt, encodes it, and attaches it to the email: <br/><br />
<img src="https://i.imgur.com/hWlfxUM.png" height="80%" width="80%" alt="Keylogger Steps"/>
<br />
<br />
<br />
The final piece of the send_email function is to send the email that the script crafts. In this part, the Transport Layer Security (TLS) starts, the code logs into the SMTP server, and it sends the email: <br/><br />
<img src="https://i.imgur.com/WmuwQbx.png" height="70%" width="70%" alt="Keylogger Steps"/>
<br />
<br />
<br />
In this next part, the code defines what to do if a key gets pressed. First, it checks if keystrokes.txt exists and either creates the file or appends to it: <br/><br />
<img src="https://i.imgur.com/EA8yv76.png" height="60%" width="60%" alt="Keylogger Steps"/>
<br />
<br />
<br />
The try block retrieves each character pressed, stores them in the char variable, and then writes that char variable to the file: <br/><br />
<img src="https://i.imgur.com/dmZvO4u.png" height="90%" width="90%" alt="Keylogger Steps"/>
<br />
<br />
<br />
Finally, the catch block will detect when the user presses special characters. I wrote the code to write the special characters to the file automatically that were oddly formatted: <br/><br />
<img src="https://i.imgur.com/R8xMIBf.png" height="80%" width="80%" alt="Keylogger Steps"/>
<br />
<br />
<br />
The last part of the code is the main function. Once the code starts, it will listen to the keyboard and capture keystrokes. Once the code stops, it will send the email: <br/><br />
<img src="https://i.imgur.com/ApP4xrw.png" height="80%" width="80%" alt="Keylogger Steps"/>
<br />
<br />
<br />

 
<h2>Program demonstration:</h2>
<p align="center">
The attacker must create an app password with their email account outside the code. This password will be the smtp_pass value in the code. An app, like VSCode, can use the smtp_pass to send the email:   <br/><br />
<img src="https://i.imgur.com/xILsVBE.png" height="40%" width="40%" alt="Keylogger Steps"/>
<br />
<br />
<br />
Next, I will start the code, navigate to Facebook, and attempt to login with a fake password (for privacy reasons): <br/><br />
<img src="https://i.imgur.com/jEUu17C.png" height="40%" width="40%" alt="Keylogger Steps"/>
<br />
<br />
<br />
Once I do all of that, I can stop the code and I will receive the email: <br/><br />
<img src="https://i.imgur.com/kpiskOG.png" height="40%" width="40%" alt="Keylogger Steps"/>
<br />
<br />
<br />
Upon viewing the text file, I can see that everything I typed recorded: <br/><br />
<img src="https://i.imgur.com/7qCF8VC.png" height="80%" width="80%" alt="Keylogger Steps"/>
<br />
<br />
<br />
Thanks for reading this far! I enjoyed creating this Keylogger and hope you enjoyed learning about it!<br/><br />
