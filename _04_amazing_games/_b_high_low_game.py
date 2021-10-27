from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    ran = random.randint(1, 100)

    # 2. Print out the random variable that you made in step #1
    print(ran)
    # 3. Code a for loop to run steps 4-10, 10 times
    for i in range(10):
        # 4. Ask the user for a guess using a pop-up window, and save their response
        resp=simpledialog.askinteger(title='Guess the Number!', prompt="Guess a number between 1 and 100!")
        # 5. If the guess is correct
        if resp== ran:
            messagebox.showinfo(title='You did it!', message='Congratulations! You guessed the number!')
            sys.exit(0)
        if resp > ran:
            messagebox.showinfo(title='Too High', message='Oops! A bit too high. Try again!')
        else:
            messagebox.showinfo(title='Too low!', message='That was a bit too low! Try again!')
            # 6. Win. Use 'sys.exit(0)' to end the program
    messagebox.showinfo(title='You were so close!', message='You were so close to getting the number! It was ' + str(ran) +'! You will get it next time!')
        # 7. if the guess is high
            # 8. Tell them it's too high
        # 9. Else if the guess is low
            # 10. Tell them it's too low

    #11. Outside of the loop, tell the user they lost

    window.mainloop()
