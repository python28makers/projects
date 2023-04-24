from app.models import User
from app.email_sender import EmailSender
from app.mixins import (
    CreateMixin, ReadMixin, 
    DeleteMixin, DetailMixin, 
    UpdateMixin
    )
from app.crud import CRUD


class Interface(CreateMixin, ReadMixin, DeleteMixin, DetailMixin, UpdateMixin, CRUD):
    model = User

interface = Interface()
email_sender = EmailSender()
user = interface.create()
# user = User('aigsdfhk', 'asdfasdf', 12, 'some@mail.com')
email_sender.send_mail(user.email)
# interface.create()
# interface.read()
# interface.delete()
# interface.read()
# interface.update()
# interface.retrieve()

'qfxliqhcnvhokszw'