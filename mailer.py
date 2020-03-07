import smtplib
from csv import reader
import csv
from email.mime.text import MIMEText
from time import sleep

#NOTE, Your data has to be in the format found in README.md
def send(sender, pwd, reci, subject, country):
    try:
        msg = country + " is the greatest country in the world!" #Write your message template here, using 'country' as a placeholder

        msg = MIMEText(msg)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = reci

        server = smtplib.SMTP("smtp.gmail.com", 587) #put whatever smtp server you'd like here, in this case it is gmail
        server.starttls()
        server.login(sender, pwd)

        server.sendmail(sender, reci, msg.as_string())
        server.close()

    except Exception as e:
        print(str(e))
        print("Message Failed")


f = open('data.csv')
csv_f = csv.reader(f)
sendConstraint = 0 #Limit I put in to avoid sending emails to the same embassy twice. #This way emails can be done in batches/sessions instead of all at once
counter = 0

for row in csv_f:
  counter += 1
  if(counter > sendConstraint):
      subject = "About getting " + row[0] + " into my flag collection" #write your subject here with 'row[0]' being the name of the country you wish to email
      send("example@example.com", "PASSWORD", row[1], subject, row[0]) #Sensitive Data
      print("Sent message to " + row[0] + " at email : " + row[1] + " Index is " + str(counter))
      sleep(2.34) #Delay number I found while testing with gmail. Anything less would mess up and start skipping
