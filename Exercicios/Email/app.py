import os
import smtplib
from email.message import EmailMessage
from segredos import senha

# Configurar email, senha
EMAIL_ADDRESS = 'testeemaildedisparo@gmail.com'
EMAIL_PASSWORD = senha
# Criar um email
msg = EmailMessage()
msg['Subject'] = 'Teste de disparo'
msg['From'] = 'testeemaildedisparo@gmail.com'
msg['To'] = 'testeemaildedisparo@gmail.com'
msg.set_content('Fazendo um teste de disparo')
# Enviar um email
for c in range(5000):
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        smtp.send_message(msg)