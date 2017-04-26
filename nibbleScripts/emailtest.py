import smtplib

smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtpObj.ehlo()
smtpObj.sendmail('pardipchagar@gmail.com', 'pardipchagar@gmail.com',
'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely,Bob')