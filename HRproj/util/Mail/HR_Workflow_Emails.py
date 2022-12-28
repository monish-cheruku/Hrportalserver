from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage

class EmailUtils():

    def getEmailBody(template, context):
        body = render_to_string(template, context)    
        return body

    
    def sendEmail(subject, body, to, cc):
        try:
            if settings.SEND_EMAIL:    
                email = EmailMessage(
                    subject=subject,
                    body=body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=to,            
                    cc=cc
                )

                email.content_subtype = "html"  # set the content subtype to html
                email.send()   
        except Exception as ex:
            raise Exception("Exception while sending emails- "+str(ex))            