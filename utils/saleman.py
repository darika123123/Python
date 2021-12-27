def read_file(file):
    f = open(file)
    for line in f:
        print(line[:-1])

def saleman_enter(arg):
    login = str(input('Enter the login '))
    password = str(input('Enter the password '))
    validate = False
    f = open('./accounts/saleman.txt')
    for line in f:
        val1, val2 = line.split(' ')
        if val1 == login and val2[:-1] == password:
            validate = True
            while True:
                menu = str(input(
                    'Greetings, dear Saleman! Please type the menu number to work with the program, if finished, then type 6: '))
                if menu == '1':
                    read_file('./data/sale.txt')
                elif menu == '2':
                    print('1-Search by name')
                    print('2-Search by date')
                    print('3-Exit')
                    while True:
                        Number = input('')
                        if Number == '1':
                            Name = str(input('Search an item by name:>>'))
                            f = open('./data/sale.txt')
                            result = False
                            for line in f:
                                val1, val2 = line.split(' ')
                                if Name.lower() == val1.lower():
                                    result = True
                                    print(line)
                            if result == False:
                                print('There is no such item')
                        elif Number == '2':
                            Date = str(input('Search an item by name:>>'))
                            f = open('./data/sale.txt')
                            result = False
                            for line in f:
                                val1, val2 = line.split(' ')
                                if Date.lower() == val2[:-1].lower():
                                    result = True
                                    print(line)
                            if result == False:
                                print('There is no item on this date')
                        elif Number == '3':
                            break
                        else:
                            print('There is no command')
                elif menu == '3':
                    read_file('solt.txt')
                elif menu == '4':
                    read_file('order.txt')
                    Name = str(input('Name of the product to order-> '))
                    Quantity = str(input('The quantity-> '))
                    with open('order.txt', "a+") as file:
                        file.write(Name+" "+Quantity+"\n")
                elif menu == '5':
                    array = []
                    f = open('solt.txt')
                    for line in f:
                        array.append(line)
                    for i in range(len(array)):
                        print(str(i+1)+'.'+array[i])
                    deleteOne = int(
                        input('Which order would you like to delete (Select a number)?>>> '))
                    for i in range(len(array)):
                        if i == deleteOne-1:
                            array.remove(array[i])
                    with open('solt.txt', "w") as file:
                        for line in array:
                            file.write(line)
                    print('You have left:')
                    read_file('solt.txt')
                elif menu == '6':
                    return print('The program is completed, we will be glad to see you back! ')

    if validate == False:
        print("I don't understand you")

