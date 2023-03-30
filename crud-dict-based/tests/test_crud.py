from crud.funcs import *

test_db = []

def test_create():
    user = create(test_db)
    assert user['age'] == 20