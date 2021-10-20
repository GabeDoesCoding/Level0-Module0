from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    ran = random.randint(0,3)
    # 2. Print your variable to the console
    print()
    # 3. Get the user to enter something that they think is awesome
    simpledialog.askstring(title='Awesome', prompt="What is something you think is awesome?")
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
    if ran == 0:
            messagebox.showinfo(title='Awesome!', message="What you entered is awesome!")
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    if ran == 1:
            messagebox.showinfo(title='Okay', message="What you entered is okay.")
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    if ran == 2:
            messagebox.showinfo(title='Boring', message="What you entered is boring...")
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
    if ran == 3:
            messagebox.showinfo(title='Incredible!' , message= "What you entered is really incredible!")
    # Run the window's .mainloop() method
    window.mainloop()