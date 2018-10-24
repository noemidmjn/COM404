# simple counting using while 

# asking in a number counting down from
countDown = int(input())

while (countDown >= 0):
    print(countDown)
    countDown = countDown - 1
    if countDown == 0:
        print("Action!")
        break

# without break the program displays 0
