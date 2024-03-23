# Beginner Python Projects
# Email Sender

from email.message import EmailMessage
import smtplib
import ssl

email_sender = 'wsdff345@otemdi.com'
email_password = '**** **** **** ****'
email_receiver = 'wepipat332@otemdi.com'

subject = 'Python Email Sender'
body = 'This is a test email sent from Python'

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context==context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    
    


# Word Replacement Program

def replace_word():
    text = 'This is a test sentence'
    word_to_replace = str(input('Enter the word to replace: '))
    if word_to_replace not in text:
        print('The word you want to replace is not in the text')
        return
    new_word = str(input('Enter the new word: '))
    new_text = text.replace(word_to_replace, new_word)
    print(new_text)
    
    
# replace_word()


# Basic Calculator
# define the functions needed: add, subtract, multiply, divide

def add(a,b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))
    
def sub(a,b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))
    
def mul(a,b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))
    
def div(a,b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))

while True:
    print('A. Additon')
    print('B. Subtraction')
    print('C. Multiplication')
    print('D. Division')
    print('E. Exit')

    choice = input('Enter your choice: ')
    if choice == 'A' or choice == 'a':    
        print('Addition')
        a = float(input('Enter the first number: '))
        b = float(input('Enter the second number: '))
        add(a,b)
    elif choice == 'B' or choice == 'b':    
        print('Subtraction')
        a = float(input('Enter the first number: '))
        b = float(input('Enter the second number: '))
        sub(a,b)
    elif choice == 'C' or choice == 'c':
        print('Multiplication')
        a = float(input('Enter the first number: '))
        b = float(input('Enter the second number: '))
        mul(a,b)
    elif choice == 'D' or choice == 'd':
        print('Division')
        a = float(input('Enter the first number: '))
        b = float(input('Enter the second number: '))
        div(a,b)
    elif choice == 'E' or choice == 'e':
        quit()
    else:
        print('Invalid choice')
    