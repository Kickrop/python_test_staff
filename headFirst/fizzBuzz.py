for i in range(1,103):
    line = ""
    if i%3 == 0:
        line = line + "Fizz"
    if i%5 == 0:
        line = line + "Buzz"
    if line:
        print(line)
    else:
        print(i)
