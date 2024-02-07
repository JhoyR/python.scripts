import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Configuration
config = {
    "smtp_server": "smtp.example.com",
    "smtp_port": 587,
    "smtp_user": "seu_email@example.com",
    "smtp_password": "sua_senha",
    "from_email": "seu_email@example.com",
    "to_email": "destinatario@example.com",
    "subject": "Exemplo de E-mail Automatizado",
    "attachments": ["path/to/file1.txt", "path/to/file2.pdf"],
    "body": """,
Olá,

Este é um exemplo de e-mail automatizado enviado via Python.

Atenciosamente,
Seu Nome
""",
}

def send_email(config):
    # Check if required configuration values are present
    required_config = ["smtp_server", "smtp_port", "smtp_user", "smtp_password", "from_email", "to_email"]
    missing_config = [key for key in required_config if key not in config]
    if missing_config:
        raise ValueError(f"Missing configuration values: {', '.join(missing_config)}")

    # Connect to the SMTP server
    try:
        server = smtplib.TLS(config["smtp_server"], config["smtp_port"])
        server.login(config["smtp_user"], config["smtp_password"])
    except Exception as e:
        raise ValueError(f"Failed to connect to SMTP server: {str(e)}")

    # Create the email
    msg = MIMEMultipart()
    msg["From"] = config["from_email"]
    msg["To"] = config["to_email"]
    msg["Subject"] = config["subject"]
    msg.attach(MIMEText(config["body"], "plain"))

    # Attach files if provided
    if "attachments" in config:
        for attachment in config["attachments"]:
            with open(attachment, "rb") as f:
                part = MIMEApplication(f.read(), _subtype="octet-stream")
                part.add_header("Content-Disposition", 'attachment', filename=attachment)
                msg.attach(part)

    # Send the email
    try:
        server.sendmail(config["from_email"], config["to_email"], msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        raise ValueError(f"Failed to send email: {str(e)}")

# Send the email
send_email(config)