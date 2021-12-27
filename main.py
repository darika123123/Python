from utils.delivery import *
from utils.provider import *
from utils.saleman import *

account = str(
    input('Please type your type of account: >>> '))

def typeOfAccount(arg):

    if arg.lower() == 'saleman':
        saleman_enter(arg)
    elif arg.lower() == 'delivery':
        delivery_enter(arg)
    elif arg.lower() == 'provider':
        provider_enter(arg)
    else:
        return print("Sorry,I didn't find this type of account, type one more time.")


typeOfAccount(account)
