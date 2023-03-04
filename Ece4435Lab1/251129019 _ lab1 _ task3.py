from socket import *
import time
import base64
import ssl

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
#Fill in start

mailserver = ("smtp.gmail.com", 587)

#Fill in end


# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

#Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')


# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print("HELO" + recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Utilizing the TLS command and printing out the server response
ttls = "STARTTLS\r\n"
clientSocket.send(ttls.encode())
recv2 = clientSocket.recv(1024)
recv2 = recv2.decode()
print("STARTTLS command: " + recv2)

# Credentials for the email, username and password
username = "kevinnumba10@gmail.com"
password = "Ballislife4585"

userEncoding = (username).encode()
passwordEncoding = (password).encode()

# Wrapping the client socket in SSl and attempting to establish connection
SSLClientSocket = ssl.wrap_socket(clientSocket)
SSLClientSocket.send(heloCommand.encode())
recv1 = SSLClientSocket.recv(1024)
recv1 = recv1.decode()
print("HELO: " + recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Creating The Authentication Messages
authenticationMessage = "AUTH LOGIN\r\n".encode()
SSLClientSocket.send(authenticationMessage)
receivedAuthentication = SSLClientSocket.recv(1024).decode()
print("Authentication LOGIN: " + receivedAuthentication)

# Retrieving Username Authentication
base64Encoding = base64.b64encode(userEncoding)
SSLClientSocket.send(base64Encoding + "\r\n".encode())
receivedAuthentication = SSLClientSocket.recv(1024).decode()
print("Authentication USERNAME: " + receivedAuthentication)

# PASSWORD AUTHENTICATION
base64Encoding = base64.b64encode(passwordEncoding)
SSLClientSocket.send(base64Encoding+"\r\n".encode())
receivedAuthentication = SSLClientSocket.recv(1024).decode()
print("Authentication PASSWORD: " + receivedAuthentication)

# Send MAIL FROM command and print server response.
# Fill in start

mailFrom = "MAIL FROM: <kevinnumba10@gmail.com>\r\n"
SSLClientSocket.send(mailFrom.encode())
recv3 = SSLClientSocket.recv(1024)
recv3 = recv3.decode()
print("MAIL FROM command: "+recv3)

# Fill in end

# Sending the RCPT TO command and print theserver response.
# Fill in start

rcptTo = "RCPT TO: <kenny.aidoo02@gmail.com>\r\n"
SSLClientSocket.send(rcptTo.encode())
recv4 = SSLClientSocket.recv(1024)
recv4 = recv4.decode()
print("RCPT TO command: "+recv4)

# Fill in end

# Send DATA command and print server response.
# Fill in start
data = "DATA\r\n"
SSLClientSocket.send(data.encode())
recv5 = SSLClientSocket.recv(1024)
recv5 = recv5.decode()
print("DATA command: "+recv5)
# Fill in end

# Send message data.
# Fill in start

subject = "SUBJECT: totally not spam\r\n"
SSLClientSocket.send(subject.encode())
date = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
date = date + "\r\n\r\n"
SSLClientSocket.send(date.encode())
SSLClientSocket.send(msg.encode())
SSLClientSocket.send(endmsg.encode())
recv_msg = SSLClientSocket.recv(1024)
print("Response after sending message body:"+recv_msg.decode())

# Fill in end


# Send QUIT command and get server response.
# Fill in start

quit = "QUIT\r\n"
SSLClientSocket.send(quit.encode())

# Fill in end
