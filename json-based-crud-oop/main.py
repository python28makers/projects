from app.models import User
from app.mixins import CreateMixin, ReadMixin, DeleteMixin
from app.crud import CRUD


class Interface(CreateMixin, ReadMixin, DeleteMixin, CRUD):
    model = User

interface = Interface()
# interface.create()
# interface.read()
interface.delete()
