def decode(string):
    data_f = ''
    for i in range(0, len(string)):
        data_f += str(int(string[i]) - 3)
    return data_f


#Tianhao Zhang
def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(string):
    encoded = ""
    for i in string:
        i= int(i)+3
        if i > 10:
            i=i-10
        #decode process; add 3 to each of digits.
        encoded += str(i)
        #gather up the digits