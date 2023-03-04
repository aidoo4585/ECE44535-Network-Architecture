from socket import *
import base64
import ssl
import smtplib
import time

msg = "\r\n I love computer networks! (using smtplib)"

# Choose a mail server (e.g. Google mail server) and call it mailserver
#Fill in start
mailserver = smtplib.SMTP('smtp.gmail.com:587')

username = "kevinnumba10@gmail.com"
password = "Ballislife4585"
recipient = "kenny.aidoo02@gmail.com"

# The Array of header also combining the array into a single header
messageHeader = ["From: " + username, "Subject: Testing using smtplib",
                 "To: " + recipient, "MIME-Version:1.0", "Content-Type: text"]
messageHeader = "\r\n".join(messageHeader)
# Notify when email is sending
print('Sending email...')

# Using the Protocol in order to establish the connection with the server
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login(username, password)

# Sending email
mailserver.sendmail(username, recipient, messageHeader+"\r\n\r\n"+msg)
mailserver.quit()
endmsg = "Email Delivered!"
print(endmsg)
