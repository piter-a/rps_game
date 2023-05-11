from tkinter import *
import random

class RockPaperScissorsGame:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('400x400')
        self.root.resizable(0, 0)
        self.root.title("Rock-Paper-Scissors game")
        self.root.config(bg='lightblue')
        
        self.result = StringVar()
        self.current_score = StringVar()
        self.pwins = IntVar()
        self.cwins = IntVar()
        self.user_input = StringVar()
        
        Label(self.root, text='Rock-Paper-Scissors',
              font='arial 20 bold', bg='lightblue').pack()
        
        Label(self.root, text='Choose one: --Rock,Paper,Scissors--',
              font='arial 15 bold', bg='lightblue').place(x=20, y=70)
        
        Entry(self.root, font='arial 15', textvariable=self.user_input,
              bg='green').place(x=90, y=130)
        
        Entry(self.root, font='arial 10 bold', textvariable=self.result,
              bg='green', width=50).place(x=25, y=250)
        
        Entry(self.root, font='arial 10 bold', textvariable=self.current_score,
              bg='green', width=50).place(x=25, y=280)
        
        Button(self.root, font='arial 13 bold', text='PLAY', padx=5, bg='lightblue',
               command=self.play).place(x=150, y=190)
        
        Button(self.root, font='arial 13 bold', text='RESET', padx=5,
               bg='lightblue', command=self.full_reset).place(x=70, y=310)
        
        Button(self.root, font='arial 13 bold', text='EXIT', padx=5,
               bg='lightblue', command=self.exit).place(x=230, y=310)
        
        self.full_reset()
        
    def play(self):
        options = ['rock', 'paper', 'scissors']
        comp_choice = random.choice(options)
        user = self.user_input.get().lower()

        if user != 'rock' and user != 'paper' and user != 'scissors':
            self.result.set('Invalid input, select rock, paper, or scissors.')

        elif user == comp_choice:
            self.result.set(
                f"It's a tie, computer also selected {comp_choice}. Play again.")

        elif (user == 'rock' and comp_choice == 'scissors') or \
             (user == 'paper' and comp_choice == 'rock') or \
             (user == 'scissors' and comp_choice == 'paper'):
            self.pwins.set(self.pwins.get() + 1)
            self.result.set(
                f'You win this round, computer selected {comp_choice}. Play again.')

        else:
            self.cwins.set(self.cwins.get() + 1)
            self.result.set(
                f'Computer wins this round, computer selected {comp_choice}. Play again')

        self.print_score()
        self.clear_text()

    def end_message(self):
        self.user_input.set("")
        self.current_score.set(f"Final Score --> Player: {self.pwins.get()} Computer: {self.cwins.get()}")

    def full_reset(self):
        self.result.set('')
        self.user_input.set("")
        self.current_score.set("")
        self.pwins.set(0)
        self.cwins.set(0)

    def exit(self):
        self.root.destroy()

    def clear_text(self):
        self.user_input.set("")

    def print_score(self):
        self.current_score.set(
            f"Current Score --- Player Score: {self.pwins.get()}, Computer Score {self.cwins.get()}")

        if self.pwins.get() == 3:
            self.result.set('Congrats, you won! Reset to play again or exit.')
            self.end_message()

        elif self.cwins.get() == 3:
            self.result.set('Sorry, you lost. Reset to play again or exit.')
            self.end_message()

game = RockPaperScissorsGame()
game.root.mainloop()