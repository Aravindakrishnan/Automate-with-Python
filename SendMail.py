
# Send a Mail with HTML :)

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
def send_mail(SUBJECT, BODY, TO, FROM):
   
    # Create message container - the correct MIME type is multipart/alternative here!
    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = SUBJECT
    MESSAGE['To'] = TO
    MESSAGE['From'] = FROM
    MESSAGE.preamble = """
Your mail reader does not support the report format.
Please visit us <a href="http://www.mysite.com">online</a>!"""
 
    # Record the MIME type text/html.
    HTML_BODY = MIMEText(BODY, 'html')
 
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    MESSAGE.attach(HTML_BODY)
 
    # The actual sending of the e-mail
    server = smtplib.SMTP('smtp.gmail.com',587)
 
    # Print debugging output when testing
    if __name__ == "__main__":
        server.set_debuglevel(1)
 
    # Credentials (if needed) for sending the mail
    password = "your_email_password"
 
    server.starttls()
    server.login(FROM,password)
    server.sendmail(FROM, [TO], MESSAGE.as_string())
    server.quit()
 
if __name__ == "__main__":
    """Executes if the script is run as main script (for testing purposes)"""
 
    email_content = """
 
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>html title</title>
   <style type="text/css" media="screen">
    table{
        background-color: #AAD373;
        empty-cells:hide;
    }
    td.cell{
        background-color: white;
    }
  </style>
 
 <body>
               <div class="container">
                     <h1>Helloworld</h1>
               </div>
               
 </body>
 
 
"""
 
    TO = 'example@gmail.com'
    FROM ='example@gmail.com'
 
    send_mail("myname", email_content, TO, FROM)
