import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sent_from = 'gossip.rosabellegarde@gmail.com'
subject = 'Code de validation - Gossip Rosa Parks & Bellegarde'


def envoyer_email_verification(destinataires, code_a_envoyer):
    corps = f"""Bonjour,\nVoici votre code de validation pour Gossip Rosa Parks et Bellegarde ! \n {code_a_envoyer} \n 
    Bonne fin de journée !"""

    # Crée un objet MIMEText pour gérer le contenu de l'e-mail
    msg = MIMEMultipart()
    msg['From'] = sent_from
    msg['To'] = ", ".join(destinataires)
    msg['Subject'] = subject

    texte = MIMEText(corps.encode('utf-8'), 'plain', 'utf-8')
    msg.attach(texte)

    serveur = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    serveur.ehlo()
    serveur.login(sent_from, 'lurm fhoe kowk karp')

    serveur.sendmail(sent_from, destinataires, msg.as_string())
    serveur.close()