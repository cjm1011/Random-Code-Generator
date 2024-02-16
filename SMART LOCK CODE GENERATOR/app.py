import random
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def generate_access_code(length=4):
    """Generate a random numeric access code."""
    characters = string.digits  # Only digits (0-9)
    access_code = ''.join(random.choice(characters) for _ in range(length))
    return access_code

def send_message(access_code):
    """Send an email with the access code to your personal email."""
    sender_email = "cesar.marty11@gmail.com"  # Your email address
    receiver_email = "adventuregardenstay@gmail.com"  # Your email address
    password = "fduq reqq unsn jbgo"  # Your email password

    message_template = """
    Hi There!

    Your Tampa trip is here!

    For check-in, we have a smart lock. Just enter code {} and you’re all set.

    When you are leaving the place during your stay, ensure the door is properly closed and then key-in the lock icon on the smart lock to lock the door. Then at checkout just do the same after you have gathered all your belongings. Before checking out, please take out the trash and place it in the blue trash bin located on the right hand side of the driveway.

    The address is 10207 N Ninevah Rd. Tampa, FL 33617. For parking, please park in the driveway right in front of the white vinyl fence where the container is located which the entrance will also be past that white plastic fence.

    Free WiFi is also provided during your stay:

    – Username: Its Cesar & Leo
    – Password: Welcome123

    •Bathroom:

    Please, do not flush feminine products, paper towels, baby wipes, etc.

    Hot Tub:

    To turn on the hot tub, please hold the center power/ON button for 3 seconds until you hear a beep sound. After that you can press the jet button and relax and enjoy the SPA. For a better and effective use, when not in use please place the tub cover to preserve the hot water. Once the tub is running it will auto-lock after 5 minutes to unlock it and select other features, hold the lock/unlock button for 3 seconds until you hear a beep sound then select whether you want to turn on/off the jets or heat up the tub. Also, after use ensure the hot tub water filtering feature stays ON to keep the water clean and sanitize. PLEASE NOTE: If you leave the tub uncovered the water will cool down and it takes several hours to heat up again.

    If there is anything else you need, like recommendations or directions or anything for the house, just let me know. We will be happy to help and want you to have a 5-star experience.
    """.format(access_code)
    
    # Create a MIMEText object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Test Access Code for Airbnb Guest"
    msg.attach(MIMEText(message_template, 'plain'))

    # Connect to the SMTP server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

    print("Email sent successfully.")

def main():
    # Generate a new numeric access code
    new_access_code = generate_access_code()
    
    # Send the email with the access code
    send_message(new_access_code)

if __name__ == "__main__":
    main()

# fduq reqq unsn jbgo