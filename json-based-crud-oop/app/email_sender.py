import smtplib

class EmailSender:
    __sender = smtplib.SMTP('smtp.gmail.com', 587)
    __host_email = 'почта отправителя'

    def send_mail(self, email):
        self.__sender.starttls()
        self.__sender.login(self.__host_email, 'пароль приложений')
        self.__sender.sendmail(self.__host_email, email, 'Thanks for registration!')
        self.__sender.quit()


# email_sender = EmailSender()
# email_sender.send_mail('xaces14925@momoshe.com')
