S = int(input())

for i in range(S):
    string = input()
    odd = ''
    even = ''

    for j in range(len(string)):
        if (j % 2 == 0):
            even += string[j]
        else:
            odd += string[j]

    print('{} {}'.format(even, odd))
