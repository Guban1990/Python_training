from model.group import Contact


testdata = [
    Contact(firstname="firstname1", lastname="lastname1", address="address1", homephone="1234", email="mail@yandex.ru")
]

"""def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", address="", homephone="", email="")] + [
    Contact(firstname=random_string("firstname", 5), lastname=random_string("lastname", 10),
            address=random_string("address", 20), homephone=(random_string("homephone", 10)),
            email=(random_string("email", 7)))
    for i in range(5)
]"""
