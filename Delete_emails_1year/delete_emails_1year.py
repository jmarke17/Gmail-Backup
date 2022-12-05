import imaplib
import datetime

# Set the IMAP server and login credentials
imap_server = "imap.gmail.com"
username = "your mail"
password = "password-to-interact-with-2FA"

# Connect to the IMAP server and login
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(username, password)

# Select the inbox folder
imap.select("inbox")

# Fetch a list of all email IDs in the inbox
status, data = imap.search(None, "ALL")
email_ids = data[0].split()

# Get the current date and time
now = datetime.datetime.now()

# Delete any emails that are older than one year
for email_id in email_ids:
    # Fetch the email date
    status, data = imap.fetch(email_id, "(BODY[HEADER.FIELDS (DATE)])")
    email_date = data[0][1]

    # Parse the email date
    email_date = email.utils.parsedate_tz(email_date.decode("utf-8"))
    email_timestamp = email.utils.mktime_tz(email_date)
    email_datetime = datetime.datetime.fromtimestamp(email_timestamp)

    # Check if the email is older than one year
    if (now - email_datetime).total_seconds() > (365 * 24 * 60 * 60):
        # Delete the email if it is older than one year
        imap.store(email_id, "+FLAGS", "\\Deleted")

# Expunge the deleted emails
imap.expunge()

# Close the connection to the IMAP server
imap.close()
imap.logout()