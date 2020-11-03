# 8.5 Open the file mbox-short.txt and read it line by line.
# When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split()
# and print out the second word in the line
# (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with
# 'From:'. Also look at the last line of the sample output to see how to print the count.


def my_function(filePath):
    f = open(filePath)
    line = f.readline()

    i = 0
    while line:
        if 'From: ' in line:
            arr = line.split('From: ')
            print(arr[1])
            i += 1
        line = f.readline()
    f.close()

    return i

res = my_function("mbox-short.txt")
print(res)


def my_function2(filePath):
    f = open(filePath)
    line = f.readline()

    i = 0
    while line:
        if 'From: ' in line:
            arr = line.split('From: ')

            for item in arr:
                if '@' in item:
                    i += 1
                    print(item)

        line = f.readline()
    f.close()

    return i


res = my_function2("mbox-short.txt")
print(res)