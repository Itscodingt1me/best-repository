def encode(data):
    data_f = ''
    for i in range(0, len(data)):
        if int(data[i]) == 7:
            data_f += 'a'
        elif int(data[i]) == 8:
            data_f += 'b'
        elif int(data[i]) == 9:
            data_f += 'c'
        else:
            data_f += str(int(data[i]) + 3)
    return data_f


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

        #elif menu == '2':
            #print('The encoded password is,', data, ',and the original password is', decode(data), '.')

        elif menu == '3':
            break


if __name__ == '__main__':
    main()
