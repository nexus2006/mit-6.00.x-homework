intro = "Please think of a number between 0 and 100!"
guess = "Is your secret number "
prompt = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."
done = "Game over. Your secret number was: "
input_err = "Sorry, I did not understand your input."

low = 0
high = 100
guess_success = False
print intro
while not guess_success:
    #guess logic
    ans = abs((high+low)/2)
    print guess + str(ans) + "?"
    #handle input
    ins = raw_input(prompt)
    if ins == 'h':
        high = ans
    elif ins == 'l':
        low = ans
    elif ins == 'c':
        guess_success = True
    else:
        print input_err
print done + str(ans)
