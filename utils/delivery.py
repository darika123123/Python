from os import read


def read_file(file):
    f = open(file)
    for line in f:
        print(line[:-1])
        
def delivery_enter(arg):
    login = str(input('Enter the login '))
    password = str(input('Enter the password '))
    validate = False
    f = open('./accounts/delivery.txt')
    for line in f:
        val1, val2 = line.split(' ')
        if val1 == login and val2[:-1] == password:
            validate = True
            while True:
                menu = str(input(
                    'Greetings, dear Deliveryman! Please type the menu number to work with the program, if finished, then type 7: '))
                if menu == '1':
                    read_file('solt.txt')
                elif menu == '2':
                    read_file('./data/delivered.txt')
                elif menu == '3':
                    array = []
                    f = open('./data/delivered.txt')
                    for line in f:
                        array.append(line)
                    for i in range(len(array)):
                        print(str(i+1)+'.'+array[i])
                    deleteOne = int(input(
                        'Which order would you like to delete (Select a number)?>>> '))
                    for i in range(len(array)):
                        if i == deleteOne-1:
                            deleted=array.pop(i)
                            with open ("report.txt","a+")as f:
                                f.write(str(deleted))
                    with open('./data/delivered.txt', "w") as file:
                        for line in array:
                            file.write(line)
                    print('You have left:')
                    read_file('./data/delivered.txt')
                elif menu == '4':
                    f = open('./data/delivered.txt')
                    count = 0
                    for line in f:
                        count += 1
                    print('Quantity of delivered items', count)
                elif menu == '5':
                    f = open('solt.txt')
                    count = 0
                    for line in f:
                        count += 1
                    print('Number of items ordered', count)
                elif menu == '6':
                    f = open('./data/delivered.txt')
                    count = 0
                    for line in f:
                        val1, val2 = line.split(' ')
                        count += int(val2)
                    print(count)
                elif menu == '7':
                    return print('The program is completed, we will be glad to see you back!')
                else:
                    print('Type an item from the menu')
                continue
    if validate == False:
        print("I don't understand you")
