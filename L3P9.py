rightAnswer = False

print "Please think of a number between 0 and 100!"

low = 0
high = 100

ans = (high + low) / 2

while rightAnswer != True:
    print "Is your secret number " + str(ans) + "?"
    result = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if result == 'h':
        high = ans
    elif result == 'l':
        low = ans
    elif result == 'c':
        rightAnswer = True
        print "Game over. Your secret number was: " + str(ans)
        break
    else:
        print "Sorry, I did not understand your input."
    ans = (high + low) / 2
