import smtplib
from email.message import EmailMessage

Asunto = ""
Correo = ""
Mensaje = ""
Correo = ""

Datos = input("")
Array = Datos.split(",")

for i in Array: 
    if i.find("C:") != -1:
        Correo = i.split(":")[1]
    if i.find("A:") != -1:
        Asunto = i.split(":")[1]
    if i.find("M:") != -1:
        Mensaje = i.split(":")[1]
    


Sender_Email = "yedayure@gmail.com"
Password = "Mayo2021."
Reciever_Email = Correo


newMessage = EmailMessage()                         
newMessage['Subject'] = Asunto
newMessage['From'] = Sender_Email                   
newMessage['To'] = Reciever_Email    
content=Mensaje               
newMessage.set_content(content)

files = ['docker codigos.txt']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Sender_Email, Password)              
    smtp.send_message(newMessage)  
