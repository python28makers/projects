import uuid

class ReadMixin:
    def read(self):
        print(self.read_db())

class CreateMixin:
    def create(self):
        data = self.read_db()
        username = input('Введите имя ')
        age = input('Введите возраст ')
        email = input('Введите почту ')
        uid = str(uuid.uuid4())[:8]
        model = self.model(uid, username, age, email)
        data.append(model.dict())
        self.write_to_db(data)

class UpdateMixin:
    ...

class DeleteMixin:
    ...

class DetailMixin:
    ...

# TODO: Дописать остальные миксины
