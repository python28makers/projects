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
        return model


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
                data.pop(data.index(user))
                self.write_to_db(data)
                break
        else:
            print('Нет такого пользователя')


class UpdateMixin:
    def update(self):
        data = self.read_db()
        uid = input('Введите id пользователя ')
        user = self.get_object(uid)
        if user is not None:
            data.remove(user)
            new_username = input('Введите новое имя ') or user['username']
            new_age = input('Введите новый возраст ') or user['age']
            new_email = input('Введите новую почту ') or user['email']
            uid = user['uid']
            model = self.model(uid, new_username, new_age, new_email)
            data.append(model.dict())
            self.write_to_db(data)
        else:
            print('Пользователь не найден')
            




# TODO: Дописать остальные миксины
