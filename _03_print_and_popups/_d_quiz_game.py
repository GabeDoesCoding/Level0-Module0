from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER
    messagebox.showinfo(title='Quiz Game', message="Welcome to the quiz game! You will be asked a series of questions which will add points to your score if answered correctly. However, if you answer incorrectly, points will be taken from your score. Good luck!")
    #      // 2.  Ask the user a question
    Q1 = simpledialog.askinteger(title='Quiz Game', prompt="What is 2x(-3)x Y = 36, what does Y equal?")
    #      // 3.  Use an if statement to check if their answer is correct
    if Q1 ==-6:
    #      // 4.  if the user's answer was correct, add one to their score 
        score +=1
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    else:
        score+=-1
    Q2 = simpledialog.askinteger(title='Quiz Game', prompt="What is (-64 ÷ 4) + (-5)?")
    if Q2==-21:
        score +=1
    else:
        score +=-1
    Q3 = simpledialog.askinteger(title='Quiz Game', prompt="What is 5+(-7)+15+(-13)?")
    if Q3 ==0:
        score+=1
    else:
        score+=-1
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    messagebox.showinfo(title='You finished!', message="Congratulations on completing the quiz! Your final score is...")
    messagebox.showinfo(title='You finished!', message= str(score) + "!")
    # Run the window's .mainloop() method
    window.mainloop()