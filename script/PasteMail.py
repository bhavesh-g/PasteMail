
import time
import smtplib
import pyautogui
import os
from email.mime.text import MIMEText
   
time_now=time.time()

#just to print time on
#screen and maintain logs
time_it= str(time.localtime(time_now).tm_hour)+":"+str(time.localtime(time_now).tm_min)+":"+str(time.localtime(time_now).tm_sec)+"  "+str(time.localtime(time_now).tm_mday)+"/"+str(time.localtime(time_now).tm_mon)+"/"+str(time.localtime(time_now).tm_year)+"\n"
print(time_it)

# make empty file
f = open('doc.txt','w')
f.close()

# open the empty file window
fd=os.popen('doc.txt','w')

# wait for action to get complete
time.sleep(1)

# three steps
pyautogui.hotkey('ctrl','v') # Paste the copied content
pyautogui.hotkey('ctrl','s') # Save the file
pyautogui.hotkey('alt','f4') # Close the file window

#close the file
fd.close()

# open the saved file
f=open('doc.txt','r')

# read its content
p=f.read()

# close the file
f.close()

#check whether its empty or not
if(len(p)==0):
    print('Nothing copied!!')
    print('aborting...')
    time.sleep(1)

# not empty
else:
    print('sending..')

    # open the logs file
    f=open('logs.txt','a')

    # write logs to it
    f.write(time_it+str(p)+"\n")

    # close the logs file
    f.close()

    #the email part,
    #setting up smtp configs
    #and attaching the html
    #template with content
    #from above file at pre
    #tags i.e. body1

    
    sender = "Sender's email address"
    subject = "You have pasted with PasteMail"
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender,'Password of sender email id here')


    #html
    body0='''<!DOCTYPE html><html><head><title></title>

	<style>
		.text-center{text-align:center!important}@media (min-width:576px){.text-sm-left{text-align:left!important}.text-sm-right{text-align:right!important}.text-sm-center{text-align:center!important}}@media (min-width:768px){.text-md-left{text-align:left!important}.text-md-right{text-align:right!important}.text-md-center{text-align:center!important}}@media (min-width:992px){.text-lg-left{text-align:left!important}.text-lg-right{text-align:right!important}.text-lg-center{text-align:center!important}}@media (min-width:1200px){.text-xl-left{text-align:left!important}.text-xl-right{text-align:right!important}.text-xl-center{text-align:center!important}}
		.display-4{font-size:3.5rem;font-weight:300;line-height:1.2}
		.lead{font-size:1.25rem;font-weight:300}
	</style>
	<link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=yes, user-scalable=no"><link href="https://fonts.googleapis.com/css?family=Crafty+Girls" rel="stylesheet"></head><body ">

		<div class="row" style="margin:0px auto;padding-bottom: 5px; ">
			<div style="min-height: 10px;background-color: #ffe392;" class="col-sm-12">
				<p class="text-center display-4" style="font-family: 'Crafty Girls', cursive;align:center;margin:0px auto;">PasteMail</p><p class="text-center lead">Here is your recent paste</p>
			</div>
		</div>
<div class="container" style="border:30px solid #ffe3928c;border-radius:10px;">	
<pre style="min-height: 400px;padding:0px 0px 0px 5px;font-size: large;margin: 0px;">'''

    # content 
    body1=p

    #html
    body2='''</pre></div><div class="row" style="margin:0px auto;"><div style="min-height: 10px;background-color: #ffe392;" class="col-sm-12"><p class="text-center" style="font-size:small;margin:0px auto;">a free service by: <a href="https://www.linkedin.com/in/mebhaveshg/">Bhavesh</a></p></div></body></html>'''

    #email html with content
    body=body0+body1+body2
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = 'Email on which you want to receive copied content'
    msg.set_type('text/html; charset=UTF-8')
    send_it = session.sendmail(sender, 'Email on which you want to receive copied content', msg.as_string())
    print("Check your mail, Thanks for pasting with us.")
    time.sleep(2)




