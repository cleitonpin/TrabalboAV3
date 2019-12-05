import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random



    
sender_email = "riftpopo@gmail.com"
receiver_email = "cleiton.biou@gmail.com"
password = "cleiton142"

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email
codigo = random.randint(1000,9999)
# Create the plain-text and HTML version of your message
text = "Oi"
html = f"""\
<html>
  <head>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  </head>
  <body>
      <div style=''>
        <h2 align='center' style='font-family:Arial; color:#e6e6e6; background:#a22222; padding:10px 0 10px 0;'>RiftsPoPo</h2>
        <div> 
          <h5 style='color:#565656; font-size:24px;'>CÓDIGO DE CORFIRMAÇÃO: {codigo}</h5>
        </div>
        <div>
          <img style='position:relative; left:340px;' src='https://vignette.wikia.nocookie.net/leagueoflegends/images/7/78/Rengar_Render.png/revision/latest?cb=20131020145558&path-prefix=pt-br' width='256px' alt='sandney mito ahuahuah'>
        </div>
      </div>
      
  </body>

</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )

