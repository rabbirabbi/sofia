import smtplib
import getpass

myemail=input("mail id:")
pwd=getpass.getpass()
remail=input("recever mail id:")

#craete smpt session 
s=smtplib.SMTP('smpt.gmail.com',587)

#start TLS for security
s.starttls()

#authentication
s.login(myemail,pwd)

#msg to be sent
msg="hi hw r u"

#sending the mail
s.sendmail(myemail,remail,msg)

#terminating the session
s.quit() 