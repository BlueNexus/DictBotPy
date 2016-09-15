import socket
import sys
import time

server = "irc.sorcery.net"       #settings
channel = b"#bs12"
botnick = b"Kathyrine"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the socket
print("connecting to:"+server)
irc.connect((server, 6667))                                                         #connects to the server
irc.send(b"USER "+ botnick + b" " + botnick + b" " + botnick + b" :This is a fun bot!\n") #user authentication
irc.send(b"NICK "+ botnick + b"\n")                            #sets nick
irc.send(b"PRIVMSG nickserv :iNOOPE\r\n")    #auth
time.sleep(1)
irc.send(b"JOIN " + channel + b"\n")        #join the chan

while 1:    #puts it in a loop
   text=irc.recv(2040)  #receive the text
   print(text)   #print text to console

   if text.find(b'PING') != -1:                          #check if 'PING' is found
      irc.send(b'PONG ' + (text.decode().split()[1]).encode()  + b'\r\n') #returnes 'PONG' back to the server (prevents pinging out!)

   if text.find(b':~hi') !=-1: #you can change !hi to whatever you want
      t = text.split(b':~hi') #you can change t and to :)
      to = t[1].strip() #this code is for getting the first word after !hi
      irc.send(b'PRIVMSG '+channel+' :Hello '+str(to)+'! \r\n')
