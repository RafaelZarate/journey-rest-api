
from django.core.mail import send_mail, send_mass_mail, get_connection

from journey import settings


class DjangoMailSvc(object):
    def __init__(self):
        self.from_email = 'rafazrte@gmail.com'
        self.fail_silently = False
        # self.connection = get_connection()

    def send_mail(
        self,
        recipient_list: list,
        subject: str=None,
        message: str=None,
        html_message: str=None
    ):
        if not message and not html_message:
            raise Exception('A message or html_message needs to be given')
        if any(not isinstance(recipient, str) for recipient in recipient_list):
            raise Exception('All recipients need strings')
        subject = subject or 'Message from Journey!'

        sent_emails = send_mail(
            subject=subject,
            message=message,
            from_email=self.from_email,
            recipient_list=recipient_list,
            fail_silently=self.fail_silently,
            html_message=html_message,
            # connection=self.connection
        )
        return_dict = dict(
            status='succces' if sent_emails != 0 else 'error',
            message='Email sent succesfully.' if sent_emails != 0 else 'An error ocurred.'
        )
        return return_dict


    def send_mass_mail(
        self,
        recipient_list: list,
        subject: str=None,
        message: str=None,
        html_message: str=None
    ):
        if not message and not html_message:
            raise Exception('A message or html_message needs to be given')
        # if any(not isinstance(recipient, str) for recipient in recipient_list):
        #     raise Exception('All recipients need')
        subject = subject or 'Message from Journey!'
        datatuple = (subject, message, self.from_email, recipient_list)

        sent_emails = send_mass_mail(datatuple)
        return_status = 'sucecss'
        return_message = 'All emails were sent properly'
        if sent_emails == 0:
            return_status = 'error'
            return_message = 'No emails sent.'
        elif sent_emails != len(recipient_list):
            return_message = 'Some emails were sent but not all of them'
        return_dict = dict(
            status=return_status,
            sent_emails=sent_emails,
            message=return_message
        )
        return return_dict
