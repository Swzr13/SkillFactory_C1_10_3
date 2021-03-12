from ClassHousePet import Cat, Client
def print_client_balans(clients):
    for elem in clients:
        elem.print_balans()

cats = [Cat(name='Барон', sex='мальчик', age='2 года'), \
        Cat(name='Сэм', sex='мальчик', age='2 года')]

for pet in cats:
    pet.print_cat()

client_1 = Client(name='Ivanov', balans=0)
client_2 = Client(name='Tekstarov', balans=0)

clients = [client_1, client_2]
print_client_balans(clients)

client_1.add_coming(100)
client_2.add_coming(500)
print_client_balans(clients)

client_1.add_consumption(30)
client_2.add_consumption(120)
print_client_balans(clients)