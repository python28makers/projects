""" CRUD - Create Read/Retrieve(Detail) Update Delete """
from crud.funcs import create, retrieve, update, delete, read

db = []


def start():
    while True:
        action = input(
        """Что Вы хотите сделать? 
        1. create
        2. read
        3. retrieve
        4. update
        5. delete
        exit - чтобы выйти
        """)
        actions = {
            '1': create,
            '2': read,
            '3': retrieve,
            '4': update,
            '5': delete
        }
        if action == 'exit':
            print('До свидания!')
            break
        try:
            print(actions[action](db))
        except KeyError:
            print('Нет такой команды')


if __name__ == '__main__':
    start()

# TODO: дописать тесты на все функции