import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Your email credentials
sender_email = "a.mokrani20002@gmail.com"
password = "Flilsa14"

# Email server configuration
smtp_server = "smtp.gmail.com"
port = 587  # For starttls

# Create a secure SSL context
context = smtplib.ssl.create_default_context()

# Email content
receiver_email = "a.mokrani2000@gmail.com"
subject = "Automated Email from AI"
body = "This is an automated email sent by an AI script."

# Set up the MIME
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Add body to email
message.attach(MIMEText(body, "plain"))

try:
    # Connect to the server and send the email
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()  # Can be omitted
    server.starttls(context=context)  # Secure the connection
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()
