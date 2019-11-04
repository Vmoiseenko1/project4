# Project #4
# The developer : Moiseenko Victoria
# The idea: to translate the entered number into binary, octal and hexadecimal notation

number = int(input('Enter your number: '))
a = ''
while number > 0:  # Translating the number into binary notation
    a = str(number % 2) + a
    number = number // 2
print('Binary notation:', a)

length = len(a)

if length % 3 == 0: # Translating the number into octal system
    n = 0
    s = ' '
    n_2 = ''
    while n + 3 <= length:
        n2 = a[n] + a[n + 1] + a[n + 2] + s
        n += 3
        n_2 += n2

    n_2_replaced = n_2.replace('000', '0')
    n_2_replaced = n_2_replaced.replace('001', '1')
    n_2_replaced = n_2_replaced.replace('010', '2')
    n_2_replaced = n_2_replaced.replace('011', '3')
    n_2_replaced = n_2_replaced.replace('100', '4')
    n_2_replaced = n_2_replaced.replace('101', '5')
    n_2_replaced = n_2_replaced.replace('110', '6')
    n_2_replaced = n_2_replaced.replace('111', '7')
    n_2_replaced = n_2_replaced.replace(' ', '')
    print('Octal system:', n_2_replaced)
elif length % 3 != 0:
    l = 0
    while length % 3 != 0:
        l += 1
        numb = '0' * l + a
        length += 1

    length_numb = len(numb)
    n = 0
    s = ' '
    n_2 = ''
    while n + 3 <= length_numb:
        n2 = numb[n] + numb[n + 1] + numb[n + 2] + s
        n += 3
        n_2 += n2

    n_2_replaced = n_2.replace('000', '0')
    n_2_replaced = n_2_replaced.replace('001', '1')
    n_2_replaced = n_2_replaced.replace('010', '2')
    n_2_replaced = n_2_replaced.replace('011', '3')
    n_2_replaced = n_2_replaced.replace('100', '4')
    n_2_replaced = n_2_replaced.replace('101', '5')
    n_2_replaced = n_2_replaced.replace('110', '6')
    n_2_replaced = n_2_replaced.replace('111', '7')
    n_2_replaced = n_2_replaced.replace(' ', '')
    if n_2_replaced[0] == '0':
        n_2_replaced = n_2_replaced.replace('0', '')
    print('Octal system:', n_2_replaced)

if length % 4 == 0: # Translating the number into hexademical system
    n = 0
    s = ''
    n_2 = ''
    while n + 4 <= length:
        n2 = a[n] + a[n + 1] + a[n + 2] + a[n+3] + s
        n += 4
        n_2 += n2

    n_2_replaced = n_2.replace('0000', '0')
    n_2_replaced = n_2_replaced.replace('0001', '1')
    n_2_replaced = n_2_replaced.replace('0010', '2')
    n_2_replaced = n_2_replaced.replace('0011', '3')
    n_2_replaced = n_2_replaced.replace('0100', '4')
    n_2_replaced = n_2_replaced.replace('0101', '5')
    n_2_replaced = n_2_replaced.replace('0110', '6')
    n_2_replaced = n_2_replaced.replace('0111', '7')
    n_2_replaced = n_2_replaced.replace('1000', '8')
    n_2_replaced = n_2_replaced.replace('1001', '9')
    n_2_replaced = n_2_replaced.replace('1010', 'A')
    n_2_replaced = n_2_replaced.replace('1011', 'B')
    n_2_replaced = n_2_replaced.replace('1100', 'C')
    n_2_replaced = n_2_replaced.replace('1101', 'D')
    n_2_replaced = n_2_replaced.replace('1110', 'E')
    n_2_replaced = n_2_replaced.replace('1111', 'F')
    n_2_replaced = n_2_replaced.replace(' ', '')
    print('Hexademical system:', n_2_replaced)
elif length % 4 != 0:
    l = 0
    while length % 4 != 0:
        l += 1
        numb = '0' * l + a
        length += 1

    length_numb = len(numb)
    n = 0
    s = ' '
    n_2 = ''
    n_3 = ''
    while n + 4 <= length_numb:
        n2 = numb[n] + numb[n + 1] + numb[n + 2] + numb[n + 3] + s
        n += 4
        n_2 += n2

    n_2_replaced = n_2.replace('0000', '0')
    n_2_replaced = n_2_replaced.replace('0001', '1')
    n_2_replaced = n_2_replaced.replace('0010', '2')
    n_2_replaced = n_2_replaced.replace('0011', '3')
    n_2_replaced = n_2_replaced.replace('0100', '4')
    n_2_replaced = n_2_replaced.replace('0101', '5')
    n_2_replaced = n_2_replaced.replace('0110', '6')
    n_2_replaced = n_2_replaced.replace('0111', '7')
    n_2_replaced = n_2_replaced.replace('1000', '8')
    n_2_replaced = n_2_replaced.replace('1001', '9')
    n_2_replaced = n_2_replaced.replace('1010', 'A')
    n_2_replaced = n_2_replaced.replace('1011', 'B')
    n_2_replaced = n_2_replaced.replace('1100', 'C')
    n_2_replaced = n_2_replaced.replace('1101', 'D')
    n_2_replaced = n_2_replaced.replace('1110', 'E')
    n_2_replaced = n_2_replaced.replace('1111', 'F')
    n_2_replaced = n_2_replaced.replace(' ', '')
    if n_2_replaced[0] == '0':
        n_2_replaced = n_2_replaced.replace('0', '')
        print('Hexademical system:', n_2_replaced)






