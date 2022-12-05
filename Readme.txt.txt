# Introduction

This Python script allows you to download all of the emails in a Gmail account that has two-factor authentication enabled. The emails will be saved as `.eml` files in a folder on your Windows desktop.

# Requirements

In order to use this script, you will need:

- Python 3.x
- The `imaplib` module (which is included in the Python Standard Library)
- An app-specific password for your Gmail account (see below for instructions on how to generate one)

# Usage

1. Generate an app-specific password for your Gmail account.

To do this, follow these steps:

- Go to the Google Account security page (https://myaccount.google.com/security).
- Scroll down to the "Signing in to Google" section and click on the "App passwords" option.
- Click on the "Select app" dropdown menu and select the app that you are using to access Gmail (e.g. "Other (Custom Name)").
- Enter a name for the app (e.g. "Python Script") and click on the "Generate" button.
- Google will generate an app-specific password for you. Make a note of this password, as you will need it to log in to your Gmail account using the Python script.

2. Update the script with your Gmail login credentials and app-specific password.

Open the `gmail-downloader.py` file in a text editor and update the following lines with your own information:

Set the IMAP server and login credentials
imap_server = "imap.gmail.com"
username = "your_email_address@gmail.com" # Replace with your email address
password = "your_app_specific_password" # Replace with your app-specific password

Copy code

3. Run the script.

Once you have updated the script with your Gmail login credentials and app-specific password, you can run the script by typing the following command in a terminal or command prompt window:

python gmail-downloader.py

Copy code

The script will connect to the IMAP server, log in to your Gmail account, and download all of the emails in your inbox. It will save each email as an `.eml` file in a folder named `Emails_Downloaded` on your Windows desktop.

# Notes

- The script will create the `Emails_Downloaded` folder on your desktop if it does not already exist.
- The script will not download any attachments that may be included in the emails.
- The script does not currently support downloading emails from folders other than the inbox.
I hope this README.txt file provides enough information for you to use the script successfully. If you have any questions or comments, please feel free to let me know.