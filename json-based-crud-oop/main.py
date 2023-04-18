from app.models import User
from app.mixins import CreateMixin, ReadMixin
from app.crud import CRUD


class Interface(CreateMixin, ReadMixin, CRUD):
    model = User

interface = Interface()
# interface.create()
interface.read()
