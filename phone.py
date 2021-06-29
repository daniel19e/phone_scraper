import re
import pyperclip
# Create a regex for phone numbers
phoneRegex = re.compile(r'''
(
((\d\d\d)|(\(\d\d\d\)))?            #area code
(\s|-)              #first separator
\d\d\d              #first 3 digits
-                   #separator
\d\d\d\d            #last four digits
(((ext(\.)?\s)|x)   #extensions(optional)
(\d{2,5}))?         #extension number(optional)
)
''', re.VERBOSE)
# Create regex for email addresses
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+      #name part
@                    # @ symbol
[a-zA-Z0-9_.+]+      #domain name part   
''', re.VERBOSE)

# Get text off clipboard
text = pyperclip.paste()

# Extract email/phone from text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])


# Copy extracted phone numbers and emails from clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
