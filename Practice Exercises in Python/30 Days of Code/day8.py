phoneBook = {}


# taking in the number of data set we're receiving
n = int(input())

# here we take the input and save it to the dictionary phoneBook
for i in range(n):
    keyValue = input()
    entry = keyValue.split()
    phoneBook[entry[0]] = entry[1]
    # print(phoneBook)

    
while True:
    try:
        # taking in a particular query to compare in dict
        query = input()
    except EOFError as error:
        break
    if query not in phoneBook:
        print("Not found")
    else:
        print(query + "=" + phoneBook[query])
