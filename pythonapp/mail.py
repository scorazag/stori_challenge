import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def send_email(credit,debit,balance,month):
  sender_email = 'Stori@gmail.com'
  receiver_email = 'your@gmail.com'

  message = MIMEMultipart('alternative')
  message['Subject'] = 'multipart test'
  message['From'] = sender_email
  message['To'] = receiver_email


  html = """\
  <html>
    <body>
      <h2>Hola te comparitimos el resument de tu cuenta</h2>
      <table >
        <tr>
          <td>Credit</td>
          <td>%s</td>
        </tr>
        <tr>
          <td>Debit</td>
          <td>%s</td>
        </tr>
        <tr>
          <td>Balance</td>
          <td>%s</td>
        </tr>
        <tr>
          <td>Resumen por Mes</td>
          <td>%s</td>
        </tr>
      </table>
      <br>

      <table >
        <tr>
          <td><td><img src="cid:image1" alt="logo" width="100" height="100"></td></td>
          <td>Gracias por tu preferencia cualquier duda no <br>
            dudes en llamarnos 555555 o por correo electonico
          </td>
        </tr>
      </table>
    </body>
  </html>
  """%(credit,debit,balance,month)

  msj = MIMEText(html, 'html')
  message.attach(msj)

  #Attach Image 
  stori_logo = open('logo.jpg', 'rb')
  msgImage = MIMEImage(stori_logo.read())
  stori_logo.close()

  msgImage.add_header('Content-ID', '<image1>')
  message.attach(msgImage)

  with smtplib.SMTP(host='smtp.ethereal.email', port='587') as server:
      server.starttls()
      server.login('frederick.rippin@ethereal.email', 'm1p95QGh7Zu95xqjFQ')
      server.sendmail(
          'frederick.rippin@ethereal.email', receiver_email, message.as_string()
      )
  
  print('Email sent')
