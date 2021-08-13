# send automated gmail messages account By Deepak-glitch
import os 
import smtplib
import imghdr #Used To Send Images 

Sender_Email = "#Your Email Address"
Reciver_Email = []
Password = "Your Password"
Message = "Your Message"

Server = smtplib.SMTP('smtp.gmail.com', 587)
Server.starttls()
Server.login(Sender_Email, Password)
print("Login Success")
Server.sendmail(Sender_Email, Reciver_Email, Message)
print("Email has been sent",Reciver_Email)