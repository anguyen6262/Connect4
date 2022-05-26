import tkinter as tk
from functools import partial

class connect4():

    def __init__(self):
        self.player1Turn = True
        self.gameNotOver = True
        self.mainWin = tk.Tk()
        self.mainWin.title("Connect4")
        self.f1 = tk.Frame(self.mainWin, bd=20,
                           relief=tk.RIDGE,
                           padx=20,
                           pady=30,
                           )
        self.f1.grid(row=0, column=0)
        self.l1 = tk.Label(self.f1, text="Player 1",
                           font="{Edwardian Script ITC} 18")
        self.l1.grid(row=2, column=1)
        self.l2 = tk.Label(self.f1, text="Player 2",
                           font="{Edwardian Script ITC} 18")
        self.l2.grid(row=2, column=3)
        self.l3 = tk.Label(self.f1, text="Connect 4",
                           font="{Edwardian Script ITC} 30",
                           justify="right",
                           bd=5,
                           )
        self.l3.grid(row=0, column=2)
        self.e1 = tk.Entry(self.f1, text="")
        self.e1.grid(row=3, column=1)
        self.e2 = tk.Entry(self.f1, text="")
        self.e2.grid(row=3, column=3)
        self.m1 = tk.Menubutton(self.f1, text="Color",
                                font="{Edwardian Script ITC} 18")
        self.m1.grid(row=5, column=1)
        self.menu1 = tk.Menu(self.m1)
        self.m1['menu'] = self.menu1
        self.select = tk.StringVar()
        self.m2 = tk.Menubutton(self.f1, text="Color",
                                font="{Edwardian Script ITC} 18")
        self.m2.grid(row=5, column=3)
        self.menu2 = tk.Menu(self.m2)
        self.m2['menu'] = self.menu2
        self.select = tk.StringVar()
        for opt in ['Blue', 'Green', 'Purple', 'Grey']:
            self.menu1.add_radiobutton(label=opt, variable=self.select, value=opt, command=partial(self.setColor, opt, True))
        for option in ['Red', 'Yellow', 'Orange', 'Pink']:
            self.menu2.add_radiobutton(label=option, variable=self.select, value=option, command=partial(self.setColor, option, False))
        self.play = tk.Button(self.f1, text="Play",
                              font="{Edwardian Script ITC} 18",
                              command=self.playCallBack)
        self.play.grid(row=7, column=2)
        self.quit = tk.Button(self.f1, text="Quit",
                              font="{Edwardian Script ITC} 18",
                              command=self.quitCallBack)
        self.quit.grid(row=8, column=2)

        self.player1color = "blue"
        self.player2color = "red"

        self.player1name = "player1"
        self.player2name = "player2"

    def quitCallBack(self):
        self.mainWin.destroy()

    def setColor(self, color, player1):
        if player1:
            self.player1color = color
        else:
            self.player2color = color

    def playCallBack(self):
        self.otherWin = tk.Toplevel(self.mainWin)
        self.c1 = tk.Canvas(self.otherWin,
                            height=768,
                            width=1366)
        self.c1.grid(row=1, column=1)

        self.c1.bind("<Button-1>", self.placePiece)
        self.r1 = self.c1.create_rectangle(333, 84, 1033, 684, fill="black")
        self.myBoard = []
        x0 = 343
        y0 = 94
        for row in range(7):
            myRow = []
            for column in range(6):
                myID = self.c1.create_oval(x0, y0, x0 + 80, y0 + 80, fill="white")
                myRow.append(myID)
                y0 += 100
            self.myBoard.append(myRow)
            y0 = 94
            x0 += 100

        self.player1name=self.e1.get()
        self.player2name=self.e2.get()

    def winScreen(self, name):
        self.c1.bind("<Button-1>", self.h)
        self.winWindow = tk.Toplevel(self.otherWin)
        self.f2 = tk.Frame(self.winWindow, bd=20,
                           relief=tk.RIDGE,
                           padx=20,
                           pady=30,
                           )
        self.f2.grid(row=0, column=0)
        self.l4 = tk.Label(self.f2, text=(name, "wins"),
                           font="{Edwardian Script ITC} 30",
                           justify="right",
                           bd=5,
                           )
        self.l4.grid(row=0, column=2)
        self.winWindow.protocol("WM_DELETE_WINDOW", self.destroy)

    def h(self, event):
        pass

    def destroy(self):
        self.winWindow.destroy()
        self.otherWin.destroy()

    def openSpot(self, column):
        if self.player1Turn == True:
            Fcol = self.player1color
            self.player1Turn = False
        else:
            Fcol = self.player2color
            self.player1Turn = True
        color = []
        for i in range(6):
            col = self.c1.itemcget(self.myBoard[column][5 - i], "fill")
            color.append(col)
        if color[0] == "white":
            self.c1.itemconfig(self.myBoard[column][5], fill=Fcol)
        elif color[1] == "white":
            self.c1.itemconfig(self.myBoard[column][4], fill=Fcol)
        elif color[2] == "white":
            self.c1.itemconfig(self.myBoard[column][3], fill=Fcol)
        elif color[3] == "white":
            self.c1.itemconfig(self.myBoard[column][2], fill=Fcol)
        elif color[4] == "white":
            self.c1.itemconfig(self.myBoard[column][1], fill=Fcol)
        elif color[5] == "white":
            self.c1.itemconfig(self.myBoard[column][0], fill=Fcol)
        else:
            print("choose a different column")
        self.checkForWin(self.player1color, self.player1name)
        self.checkForWin(self.player2color, self.player2name)

    def checkForWin(self, FCol, name):
        # Horizontal win condition
            for row in range(6):
                for col in range(4):
                    if self.c1.itemcget(self.myBoard[col][row], "fill") == FCol and self.c1.itemcget(
                            self.myBoard[col + 1][row], "fill") == FCol and self.c1.itemcget(self.myBoard[col + 2][row],
                                                                                         "fill") == FCol and self.c1.itemcget(
                            self.myBoard[col + 3][row], "fill") == FCol:
                        self.winScreen(name)



        # Vertical win condition
            for row in range(3):
                for col in range(7):
                    if self.c1.itemcget(self.myBoard[col][row], "fill") == FCol and self.c1.itemcget(
                            self.myBoard[col][row + 1], "fill") == FCol and self.c1.itemcget(self.myBoard[col][row + 2],
                                                                                         "fill") == FCol and self.c1.itemcget(
                            self.myBoard[col][row + 3], "fill") == FCol:
                        self.winScreen(name)

        # Positive slope diagonal win condition
            for row in range(3):
                for col in range(4):
                    if self.c1.itemcget(self.myBoard[col][row], "fill") == FCol and self.c1.itemcget(
                            self.myBoard[col + 1][row + 1], "fill") == FCol and self.c1.itemcget(
                            self.myBoard[col + 2][row + 2], "fill") == FCol and self.c1.itemcget(
                            self.myBoard[col + 3][row + 3], "fill") == FCol:
                        self.winScreen(name)

        # Negative slope diagonal win condition
            for row in range(4, 6):
                for col in range(4):
                    if self.c1.itemcget(self.myBoard[col][row], "fill") == FCol and self.c1.itemcget(
                            self.myBoard[col + 1][row - 1], "fill") == FCol and self.c1.itemcget(
                            self.myBoard[col + 2][row - 2], "fill") == FCol and self.c1.itemcget(
                            self.myBoard[col + 3][row - 3], "fill") == FCol:
                        self.winScreen(name)

    def placePiece(self, event):
        x = event.x
        y = event.y
        if x > 333 and x < 433 and y > 84 and y < 684:
            self.openSpot(0)
        elif x > 434 and x < 533 and y > 84 and y < 684:
            self.openSpot(1)
        elif x > 534 and x < 633 and y > 84 and y < 684:
            self.openSpot(2)
        elif x > 644 and x < 733 and y > 84 and y < 684:
            self.openSpot(3)
        elif x > 744 and x < 833 and y > 84 and y < 684:
            self.openSpot(4)
        elif x > 844 and x < 933 and y > 84 and y < 684:
            self.openSpot(5)
        elif x > 944 and x < 1033 and y > 84 and y < 684:
            self.openSpot(6)

    def run(self):
        self.mainWin.mainloop()


myGui = connect4()
myGui.run()
