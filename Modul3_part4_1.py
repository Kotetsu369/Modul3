import json


# with open('login_pas.json', 'w') as f:  # Создаем файл
#    json.dump(log_pas, f)

def registration(log, password):
    with open('login_pas.json', 'r') as f:
        log_pas = json.load(f)
        if log not in log_pas.keys():
            log_pas[log] = password
            with open('login_pas.json', 'w') as f:
                json.dump(log_pas, f)
            print('You are registrated')
        else:
            print("Chose other login")


while True:
    secret = ('Fire!!!!!')
    log_pas = {'test': 'testpassword'}

    start = input("Вход или регистрация?")
    if start == 'вход':
        with open('login_pas.json', 'r') as f:
            log_pas = json.load(f)
            log = input("Введите свой логин")
            password = input("Введите свой пароль")
            if log in log_pas.keys():
                if log_pas[log] == password:
                    print("Ура")
                    print(secret)
            else:
                print("not right, try again")
    else:
        registration(input("login"), input("password"))
