from tkinter import *
from tkinter import  messagebox
import random

Select = False
def Game():
    # from goto import goto, label

    order = ['0'] * 9
    fileplay = ['0'] * 9
    root = Tk()
    root.title("Tic Tac toe")

    # Global Variables
    global turn
    turn = True  # if turn is true X goes
    global m_count
    m_count = 0  # to count total number of moves
    global winner
    winner = False
    # Game Functions

    # Buttons

    b1 = Button(root, text=" ", font=("Arial", 26), height=4, width=10, bg="#C0C0C0", command=lambda: click(b1))
    b2 = Button(root, text=" ", font=("Arial", 26), height=4, width=10, bg="#C0C0C0", command=lambda: click(b2))
    b3 = Button(root, text=" ", font=("Arial", 26), height=4, width=10, bg="#C0C0C0", command=lambda: click(b3))

    b4 = Button(root, text=" ", font=("Arial", 26), height=4, width=10, bg="#C0C0C0", command=lambda: click(b4))
    b5 = Button(root, text=" ", font=("Arial", 26), height=4, width=10, bg="#C0C0C0", command=lambda: click(b5))
    b6 = Button(root, text=" ", font=("Arial", 26), height=4, width=10, bg="#C0C0C0", command=lambda: click(b6))

    b7 = Button(root, text=" ", font=("Arial", 26), height=4, width=10, bg="#C0C0C0", command=lambda: click(b7))
    b8 = Button(root, text=" ", font=("Arial", 26), height=4, width=10, bg="#C0C0C0", command=lambda: click(b8))
    b9 = Button(root, text=" ", font=("Arial", 26), height=4, width=10, bg="#C0C0C0", command=lambda: click(b9))

    # Adding buttons

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

    # Button b_list and b_dict
    global b_list
    global b_dict
    b_list = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    b_dict = {1: b1, 2: b2, 3: b3, 4: b4, 5: b5, 6: b6, 7: b7, 8: b8, 9: b9}

    # click

    def click(b):
        global turn, m_count,Select,b_dict,b_list
        if b["text"] == " " and turn == True:
            b["text"] = "X"
            turn = False
            m_count += 1
            order[b_list.index(b)] = str(m_count)
            b.config(state="disabled")
            # Added cpuplay here so cpu will play immediately after we click. Also cause the main function thing wasn't working
            if Select == False :
                cpuplay()
        elif b["text"] == " " and turn == False:
            b["text"] = "O"
            turn = True
            m_count += 1
            order[b_list.index(b)] = str(m_count)
            b.config(state="disabled")
        checkwin()

    # Random play
    def playrandom():
        global b_list
        global b_dict
        global turn, winner
        global m_count
        o = b_dict[random.randint(1, 9)]
        if str(o['state']) == "disabled":
            playrandom()
        else:
            click(o)

    # CPU play
    def cpuplay():
        global b_list
        global b_dict
        global turn, winner
        global m_count
        global fileplay
        f = open("D:/desktop/programs/Python/Win.txt", "r")
        flag = 1
        if turn == False and m_count < 9:
            while (flag != 0):
                flag = 0
                fileplay = ['0'] * 9
                fileplay = f.readline()
                if (fileplay == ""):
                    fileplay = ['0'] * 9
                    break
                for x in range(m_count):
                    if (fileplay.index(str(x + 1)) != order.index(str(x + 1))):
                        flag += 1
                        break
            if (fileplay == ['0', '0', '0', '0', '0', '0', '0', '0', '0']):
                playrandom()
            else:
                x = fileplay.index(str(m_count + 1))
                o = b_dict[x + 1]
                click(o)

    # To check for win
    def checkwin():
        global b_list, winner, m_count,b_dict
        i = 0
        j = 0
        # horzontal check
        while (i < 9):
            if b_list[i]["text"] == b_list[i + 1]["text"] and b_list[i + 1]["text"] == b_list[i + 2]["text"] and \
                    b_list[i + 2]["text"] == b_list[i]["text"] and b_list[i]["text"] != " ":
                winner = True
                win_ani(b_list[i], b_list[i + 1], b_list[i + 2])
                break
            i = i + 3

        # verticle check
        while (j < 3):
            if b_list[j]["text"] == b_list[j + 3]["text"] and b_list[j + 3]["text"] == b_list[j + 6]["text"] and \
                    b_list[j + 6]["text"] == b_list[j]["text"] and b_list[j]["text"] != " ":
                winner = True
                win_ani(b_list[j], b_list[j + 3], b_list[j + 6])
                break
            j = j + 1

        # diagonal check
        if (b_list[0]["text"] == b_list[4]["text"] and b_list[4]["text"] == b_list[8]["text"] and b_list[8]["text"] ==
                b_list[0]["text"] and b_list[0]["text"] != " "):
            winner = True
            win_ani(b_list[0], b_list[4], b_list[8])
        if b_list[2]["text"] == b_list[4]["text"] and b_list[4]["text"] == b_list[6]["text"] and b_list[6]["text"] == \
                b_list[2]["text"] and b_list[2]["text"] != " ":
            winner = True
            win_ani(b_list[2], b_list[4], b_list[6])

        # Draw
        if winner == False and m_count == 9:
            messagebox.showinfo("Tic-Tac-Toe", "Its a TIE!")
            root.destroy()
            Menu()

    # End game animation

    def win_ani(a, b, c):
        m_count, order
        fileplay
        a.config(bg="#31FC0F")
        b.config(bg="#31FC0F")
        c.config(bg="#31FC0F")

        for element in b_list:
            element.config(state="disabled")

        messagebox.showinfo("Tic-Tac-Toe", "CONGRATULATIONS! " + a["text"] + "  WINS! Total moves: " + str(m_count))
        if (a["text"] == 'O'):
            f = open("D:/desktop/programs/Python/Win.txt", "a")
            f.write("\n")
            for x in order:
                f.write("%s" % x)
            f.close()
        root.destroy()
        Menu()
        exit(1)

    root.mainloop()

def Menu():
    menu = Tk()
    menu.title("Tic-Tac-Toe")
    menu.geometry("500x450")
    menu.configure(bg = "#5B92A2")
    Label(menu, text ="TIC-TAC-TOE" , font = ('Helvetica', 40),bg = "#5B92A2").pack()
    Label(menu, text = "", font=("Arial", 6),bg = "#5B92A2").pack() 
    Button(menu , text = "Single-Player", font = ('Helvetica', 16) , command =lambda : [menu.destroy(),Single_player()], bg ="#AFAEAD" , padx =10 , pady=10).pack()
    Label(menu, text = "", font=("Arial", 6),bg = "#5B92A2").pack() 
    Button(menu , text = "Multi-Player", font = ('Helvetica', 16) , command = lambda : [menu.destroy(), Multi_player()], bg ="#AFAEAD" , padx =17 , pady=10).pack()
    Label(menu, text = "", font=("Arial", 6),bg = "#5B92A2").pack() 
    Button(menu , text = "Instructions", font = ('Helvetica', 16) , command = lambda : [menu.destroy(), Game_info()], bg ="#AFAEAD" , padx =17 , pady=10).pack()
    Label(menu, text = "", font=("Arial", 6),bg = "#5B92A2").pack() 
    Button(menu , text = "Exit", font = ('Helvetica', 16) , command = lambda : exit(1), bg ="#AFAEAD" , padx =53 , pady=10).pack()
    Label(menu, text = "", font=("Arial", 6),bg = "#5B92A2").pack() 
    menu.mainloop()

def Single_player():
    Game()

def Multi_player():
    global Select
    Select = True
    Game()

def Game_info():

    info =  Tk()
    info.configure(bg = "#5B92A2")
    Label(info, text = "RULES FOR TIC-TAC-TOE", font=("Arial", 38),bg = "#5B92A2").pack() 
    Label(info, text = "", font=("Arial", 18),bg = "#5B92A2").pack() 
    Label(info, text = "1. The game is played on a grid that's 3 squares by 3 squares.                                                                                    ", font=("Arial", 18),bg = "#5B92A2").pack()
    Label(info, text = "2. You are X, your friend (or the computer in this case) is O. Players take turns putting their marks in empty squares. ", font=("Arial", 18),bg = "#5B92A2").pack()
    Label(info, text = "3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.                                  ", font=("Arial", 18),bg = "#5B92A2").pack()
    Label(info, text = "4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie                   ", font=("Arial", 18),bg = "#5B92A2").pack()
    back = Button(info, text = "BACK", command = lambda : [info.destroy(), Menu()] , bg ="#AFAEAD" ,padx =20 , pady=10)
    Label(info, text = "", font=("Arial", 18),bg = "#5B92A2").pack() 
    back.pack()
    Label(info, text = "", font=("Arial", 18),bg = "#5B92A2").pack() 
    info.mainloop()

def main():
    Menu()

if __name__ == '__main__':
    main()



