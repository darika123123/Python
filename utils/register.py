import hashlib

def register(arg):

    account_types = ["saleman", "deliveryman", "provider"]
    account_type = input("Enter your type of account: ")

    if not(account_type.lower() in account_types): # Если не правильно велл тип аккаунта
        print("Sorry,I didn't find this type of account, type one more time.")
        return
        
    login = input("Enter your login:")
    password = input("Enter your password:")

    if account_type == "saleman":
        with open("./accounts/saleman.txt", "a", encoding='utf-8') as file:
            file.write(f"{login} {password}\n")

    if account_type == "deliveryman":
        with open("./accounts/delivery.txt", "a", encoding='utf-8') as file:
            file.write(f"{login} {password}\n")

    if account_type == "provider":
        with open("./accounts/provider.txt", "a", encoding='utf-8') as file:
            file.write(f"{login} {password}\n")


if (__name__ == "main"):
    register()
    