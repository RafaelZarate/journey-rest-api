
from core.services.external import DjangoMailSvc

class MailSvc(object):
    def __init__(self, mail_service: str='Django'):
        if mail_service == 'Django':
            self.mail_service = DjangoMailSvc()
        else:
            raise Exception('Invalid email service provider selected')
    
    def send_mail(
        self,
        recipient_list: list,
        subject: str=None,
        message: str=None,
        html_message: str=None
    ):
        return self.mail_service.send_mail(
            recipient_list=recipient_list,
            subject=subject,
            message=message,
            html_message=html_message
    )
    
    def send_mass_mail(
        self,
        recipient_list: list,
        subject: str=None,
        message: str=None,
        html_message: str=None
    ):
        return self.mail_service.send_mass_mail(
            recipient_list=recipient_list,
            subject=subject,
            message=message,
            html_message=html_message
    )
