


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def create_phishing_email(sender, recipient, fake_url):
    """Generate a phishing email mimicking a legitimate service."""
    # Email headers
    subject = "Urgent: Account Verification Required"
    
    # HTML body with phishing link
    html_body = f"""
    <html>
      <body>
        <p>Dear User,</p>
        <p>We detected unusual activity on your account. Verify your identity now:</p>
        <a href="{fake_url}">Click here to secure your account</a>
        <p>If you did not request this, contact support immediately.</p>
        <p><em>© Legitimate Service 2023</em></p>
      </body>
    </html>
    """
    
    # Create MIME message
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(html_body, 'html'))
    
    return msg.as_string()

def main():
    # Example configuration (use dummy data)
    sender = "noreply@legit-service.com"  # Spoofed sender
    recipient = "user@example.com"         # Target email
    phishing_url = "http://malicious-site.com/login"  # Fake link
    
    # Generate the phishing email
    email_content = create_phishing_email(sender, recipient, phishing_url)
    
    # Save to a file instead of sending (for analysis)
    with open("phishing_email_sample.txt", "w") as f:
        f.write(email_content)
    print("Phishing email sample saved to phishing_email_sample.txt")

if __name__ == "__main__":
    main()