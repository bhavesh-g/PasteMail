# PasteMail

## Idea:
There had been a number of occasions when i had copied something on my laptop and wanted use the same text on my mobile phone. Before the idea, i use to copy the text, open my already logged in Google drive account and paste the text on a file named Air_notepad. Then open that same file from my logged in account on phone, then copy the last pasted text in it, so that i can use it on phone too. ahhhhhh! yes it was pain.

## What PasteMail does:
- It creates an empty text file, 
- then it invokes ctrl+v key combination on keyboard to paste last copied text from clipboard on file,
- then invokes the ctrl+s key combination to save the changes
- and then alt+f4.
- then it again opens that file with content saved above
- save all it's content in a variable and closes it.
- then simply with the use of smtp library of python and some html+css, it adds that content to message body and email.
- it also maintains a logs.txt file with timestamp and pasted content.
- then one can simply check his/her mails to get the copied content from laptop to phone.

### The whole process completes under 7 seconds(depending on your internet connection)

## Note:
- You must be logged in with the same email id on laptop, which is being used to setup smtp server in script.
For now works fine on Windows, soon will be adding support for Linux/Mac too with necessary changes.
- Write sender' email and password in script, wherever mentioned and receiving email address also.
