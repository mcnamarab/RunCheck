import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import results, setup

def send_email():
  
    fromaddr = setup.sender_email
    toaddr = setup.reciever_email
     
    msg = MIMEMultipart()
     
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Run Pool Results"
    

    if setup.number_of_days == 0:
        body = ("You requested the results for zero games...  Check to make sure you changed the setup.py file to request 1 or more days of games" + '\n')
        
    else:  
        body = ("Here are the results of your run pool!" + '\n')

        msg.attach(MIMEText(body, 'plain'))
        
        filename = "results.txt"
        attachment = open("results.txt", "rb")
         
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
         
        msg.attach(part)
     
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, setup.sender_password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    