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


class DetailMixin:
    def retrieve(self):
        uid = input("Введите id пользователя ")
        user = self.get_object(uid)
        if user:
            print(user)
        else:
            print('Нет такого пользователя')


class DeleteMixin:
    def delete(self):
        data = self.read_db()
        uid = input('Введите id пользователя ')
        for user in data:
            if user['uid'] == uid:
                data.remove(data.index(user))
                self.write_to_db(data)
                break
        else:
            print('Нет такого пользователя')


class UpdateMixin:
    ...



# TODO: Дописать остальные миксины
