<h1>Keylogger Development in Python using VSCode</h1>

<h2>Overview</h2>
This project utilized Visual Studio Code to develop a Keylogger in Python. This lab is strictly educational and is not intended for malicious use. This project aimed to achieve the following goals:
<br><br>
<ul>
 <li>Understand how Python, or coding languages in general, can interact with our devices</li>
 <li>Learn more about the libraries and functions Python offers</li>
 <li>Gain insight on how a keylogger functions</li>
 <ul><li>Understanding how malware works can help professionals detect, prevent, and respond to threats</li></ul>
</ul>
<h2>Summary</h2>
This program records user keystrokes and writes them to a text file. Upon termination, the program emails the attacker with the keystrokes log file attached. I'd like to acknowledge that a keylogger has much more potential than I've coded. However, I don't feel entirely comfortable developing a fully-fledged keylogger for the entire internet to view. A normal keylogger, upon execution by an unknowing party, would establish persistence within a system. Persistence can be as simple as having the code hide itself in AppData and then creating a shortcut to itself in the Windows startup folder. This means it automatically starts at machine startup and automatically sends the email at system shutdown. 

<h2>Languages and Utilities Used</h2>

- <b>Python</b> 
- <b>Visual Studio Code</b>

<h2>Program walk-through:</h2>

<p align="center">
In this first section of the code, all of the import statements are established. Most of these are for crafting the email at shutdown: <br/><br />
<img src="https://i.imgur.com/wqtLnXg.png" height="50%" width="50%" alt="Keylogger Steps"/>
<br />
<br />
<br />
This next section of the code deals with email creation. In this first part, all of the variables are created that are needed to craft an email. You might notice the smtp_pass variable is blacked out, this is because it is tied to my email account. <br/><br />
<img src="https://i.imgur.com/VliSp0L.png" height="50%" width="50%" alt="Keylogger Steps"/>
<br />
<br />
<br />
This section creates the email. This is similar to clicking the create email button in Gmail and being greeted with an empty email that needs to be filled out: <br/><br />
<img src="https://i.imgur.com/v2cJfGt.png" height="30%" width="30%" alt="Keylogger Steps"/>
<br />
<br />
<br />
Next, this block of code opens keystrokes.txt, encodes it, and attaches it to the email: <br/><br />
<img src="https://i.imgur.com/hWlfxUM.png" height="80%" width="80%" alt="Keylogger Steps"/>
<br />
<br />
<br />
The final piece of the send_email function is to send the email that has just been crafted. In this part the Transport Layer Security (TLS) is started, the code logs into the SMTP server, and it sends the email: <br/><br />
<img src="https://i.imgur.com/WmuwQbx.png" height="70%" width="70%" alt="Keylogger Steps"/>
<br />
<br />
<br />
In this next part, the code defines what it should do if a key is pressed. First, it checks if keystrokes.txt exists and either creates the file or appends to it: <br/><br />
<img src="https://i.imgur.com/EA8yv76.png" height="60%" width="60%" alt="Keylogger Steps"/>
<br />
<br />
<br />
The try block retrieves each character pressed, stores them in the char variable, and then writes that char variable to the file: <br/><br />
<img src="https://i.imgur.com/dmZvO4u.png" height="90%" width="90%" alt="Keylogger Steps"/>
<br />
<br />
<br />
Finally, the catch block will detect when any special characters are pressed and will manually write them to the file. This is because the special characters when automatically written to the file were oddly formatted: <br/><br />
<img src="https://i.imgur.com/R8xMIBf.png" height="80%" width="80%" alt="Keylogger Steps"/>
<br />
<br />
<br />
The last part of the code is the main function. Once the code is started it will begin to listen to the keyboard and capture keystrokes. Once the code is stopped it will send the email: <br/><br />
<img src="https://i.imgur.com/ApP4xrw.png" height="80%" width="80%" alt="Keylogger Steps"/>
<br />
<br />
<br />

 
<h2>Program demonstration:</h2>
<p align="center">
Outside of the code, the attacker needs to create an app password with their email account. This password will be the smtp_pass value in the code. This allows an app, VSCode for example, to send the email: <br/><br />
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
Upon viewing the text file, I can see that everything I typed was recorded: <br/><br />
<img src="https://i.imgur.com/7qCF8VC.png" height="80%" width="80%" alt="Keylogger Steps"/>
<br />
<br />
<br />
And we're done <br/><br />
