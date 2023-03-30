def create(db: list):
    user = {
        "id": input('Введите id '),
        "name": input('Введите имя '),
        "password": input('Введите пароль '),
        "age": int(input('Введите возраст ')),
    }
    db.append(user)
    return user


def read(db: list) -> list:
    return db


def retrieve(db: list):
    id_ = input('Введите id ')
    for user in db:
        if id_ == user['id']:
            return user
    else:
        return None
    

def update(db: list):
    user = retrieve(db)
    if user is not None:
        db.remove(user)
        user['id'] = user['id']
        user['name'] = input('Введите новое имя ')
        user['password'] = input('Введите новый пароль ')
        user['age'] = int(input('Введите новый возраст '))
        db.append(user)
        return user
    else:
        return None
    

def delete(db: list):
    user = retrieve(db)
    if user is not None:
        db.remove(user)
        return user
    else:
        return None

    

