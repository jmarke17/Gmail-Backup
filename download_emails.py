import imaplib

# Set the IMAP server and login credentials
imap_server = "imap.gmail.com"
username = "your-email"
password = "password-to-interact-with-2FA"

# Connect to the IMAP server and login
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(username, password)

# Select the inbox folder
imap.select("inbox")

# Create a folder on the desktop to store the downloaded emails
import os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
folder = os.path.join(desktop, "Emails_Downloaded")
if not os.path.exists(folder):
    os.makedirs(folder)

# Fetch a list of all email IDs in the inbox
status, data = imap.search(None, "ALL")
email_ids = data[0].split()

# Download and save each email
for email_id in email_ids:
    # Fetch the email
    status, data = imap.fetch(email_id, "(RFC822)")
    email = data[0][1]

    # Save the email to a file in the Emails_Downloaded folder
    filename = "email_{}.eml".format(email_id)
    filepath = os.path.join(folder, filename)
    with open(filepath, "wb") as f:
        f.write(email)

# Close the connection to the IMAP server
imap.close()
imap.logout()