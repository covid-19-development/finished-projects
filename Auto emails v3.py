import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to send an email
def send_email(sender_email, password, smtp_server, port, receiver_email, subject, body):
    try:
        # Connect to the server and send the email
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  # Secure the connection
        server.login(sender_email, password)

        # Set up the MIME
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        if 'server' in locals():
            server.quit()

# Main function to handle the email sending process
def main():
    sender_email = input("Enter your email address: ")
    password = input("Enter your email password: ")  # Note: Handle passwords securely
    smtp_server = input("Enter your SMTP server (e.g., smtp.gmail.com): ")
    port = int(input("Enter the port (e.g., 587 for TLS): "))

    receiver_email = input("Enter the recipient's email address: ")
    subject = input("Enter the subject of the email: ")
    body = input("Enter the body of the email: ")

    # Send the email
    send_email(sender_email, password, smtp_server, port, receiver_email, subject, body)

    # Ask the user if they want to send another email
    restart = input("Would you like to send another email? (yes/no): ").lower()
    if restart == "yes" or restart == "y":
        main()

# Call the main function
main()
