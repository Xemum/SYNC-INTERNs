import smtplib
from random import randint
from email.message import EmailMessage
import ssl

# Function to generate OTP
def generate_otp():
    otp = []
    for _ in range(6):
        otp.append(str(randint(0, 9)))
    return ''.join(otp)

flag = True
while flag:
    otp = generate_otp()

    # SMTP server details
    smtp_server = "smtp.gmail.com"
    smtp_port = 465

    # Email credentials
    sender_email = "exemple@gmail.com"
    receiver_email = input("Enter your email here: ")
    password = "your password here " #you should get it from apppasswords 

    # Email subject and body
    subject = "Email verification code"
    body = "Your OTP is " + otp

    # Create the EmailMessage object
    em = EmailMessage()
    em['From'] = sender_email
    em['To'] = receiver_email
    em['Subject'] = subject
    em.set_content(body)

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Disable SSL certificate verification
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as smtp:
            smtp.login(sender_email, password)
            smtp.send_message(em)
    except Exception as e:
        print("An error occurred while sending the email:", e)
        continue

    other = input("Enter your OTP here: ")
    if other == otp:
        print("Welcome to the platform!")
        flag = False
    else:
        print("Your information is incorrect.")
        flag = True
