# Introduction

This Python script allows you to delete all emails in a Gmail account that are older than one year. The script is designed to work with Gmail accounts that have two-factor authentication enabled.

# Requirements

In order to use this script, you will need:

- Python 3.x
- The `imaplib` and `datetime` modules (which are included in the Python Standard Library)

# Usage

1. Update the script with your Gmail login credentials.

Open the `gmail-deleter.py` file in a text editor and update the following lines with your own information:

Set the IMAP server and login credentials
imap_server = "imap.gmail.com"
username = "your_email_address@gmail.com" # Replace with your email address
password = "your password from Google-2FA"
2. Run the script.

Once you have updated the script with your Gmail login credentials, you can run the script by typing the following command in a terminal or command prompt window:

python gmail-deleter.py

The script will prompt you to enter your password (including the two-factor authentication code if required). After you have entered your password, the script will connect to the IMAP server, log in to your Gmail account, and delete all emails that are older than one year.

# Notes

- The script will not delete any emails that are less than one year old.
- The script does not currently support deleting emails from folders other than the inbox.
- The script does not currently support deleting emails that have been marked as important, starred, or in any other way labeled.


I hope this README.txt file provides enough information for you to use the script successfully. If you have any questions or comments, please feel free to let me know.