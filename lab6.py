def encode(data):
    data_f = ''
    for i in range(0, len(data)):
        if int(data[i]) <= 7:
            data_f += str(int(data[i]) + 3)
        else:
            data_f += str(int(data[i]) - 7)
    return data_f
def decode(data):
    decoded_data = ""
    for i in data:
        if int(i) <3:
            decoded_data += str(int(i)+7)
        else:
            decoded_data += i
        #this should work. however, I didn't test it because abc gives me an error.

    return decoded_data
def main():
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        menu = input('Please enter an option:')
        if menu == '1':
            data = input('Please enter your password to encode:')
            data = encode(data)
            print('Your password has been encoded and stored!')

        elif menu == '2':
            print('The encoded password is,', data, ',and the original password is', decode(data), '.')

        elif menu == '3':
            break


if __name__ == '__main__':
    main()
