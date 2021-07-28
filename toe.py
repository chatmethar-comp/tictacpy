from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('tic tac toe by zizzer')
#root.geometry("750x1000")
root.iconbitmap('tableIocn.png')

Clicked = True
count = 0


#dis all buttons
def disableAllButton():
	b1.config(state=DISABLED)
	b2.config(state=DISABLED)
	b3.config(state=DISABLED)
	b4.config(state=DISABLED)
	b5.config(state=DISABLED)
	b6.config(state=DISABLED)
	b7.config(state=DISABLED)
	b8.config(state=DISABLED)
	b9.config(state=DISABLED)


def checkifwon():
	global winner
	winner = False

	if b1["text"] == "X" and b2["text"] =="X" and b3["text"] =="X":
		b1.config(bg ="green")
		b2.config(bg ="green")
		b3.config(bg ="green")
		winner = True
		messagebox.showinfo('Tic tac toe','Cingratulation!  X Wins!')
		disableAllButton()
		
	elif b4["text"] == "X" and b5["text"] =="X" and b6["text"] =="X":
		b4.config(bg ="green")
		b5.config(bg ="green")
		b6.config(bg ="green")
		winner = True
		messagebox.showinfo('Tic tac toe','Cingratulation!  X Wins!')
		disableAllButton()
		
		
	elif b7["text"] == "X" and b8["text"] =="X" and b9["text"] =="X":
		b7.config(bg ="green")
		b8.config(bg ="green")
		b9.config(bg ="green")
		winner = True
		messagebox.showinfo('Tic tac toe','Cingratulation!  X Wins!')
		disableAllButton()

	elif b1["text"] == "X" and b4["text"] =="X" and b7["text"] =="X":
		b1.config(bg ="green")
		b4.config(bg ="green")
		b7.config(bg ="green")
		winner = True
		messagebox.showinfo('Tic tac toe','Cingratulation!  X Wins!')
		disableAllButton()
		

	elif b2["text"] == "X" and b5["text"] =="X" and b8["text"] =="X":
		b2.config(bg ="green")
		b5.config(bg ="green")
		b8.config(bg ="green")
		winner = True
		messagebox.showinfo('Tic tac toe','Cingratulation!  X Wins!')
		disableAllButton()

	elif b3["text"] == "X" and b6["text"] =="X" and b9["text"] =="X":
		b3.config(bg ="green")
		b6.config(bg ="green")
		b9.config(bg ="green")
		winner = True
		messagebox.showinfo('Tic tac toe','Cingratulation!  X Wins!')
		disableAllButton()

	elif b1["text"] == "X" and b5["text"] =="X" and b9["text"] =="X":
		b1.config(bg ="green")
		b5.config(bg ="green")
		b9.config(bg ="green")
		winner = True
		messagebox.showinfo('Tic tac toe','Cingratulation!  X Wins!')
		disableAllButton()

	elif b3["text"] == "X" and b5["text"] =="X" and b7["text"] =="X":
		b3.config(bg ="green")
		b5.config(bg ="green")
		b7.config(bg ="green")
		winner = True
		messagebox.showinfo('Tic tac toe','Cingratulation!  X Wins!')
		disableAllButton()




	if b1["text"] == "O" and b2["text"] =="O" and b3["text"] =="O":
		b1.config(bg ="green")
		b2.config(bg ="green")
		b3.config(bg ="green")
		winner = True
		messagebox.showinfo('Tic tac toe','Cingratulation!  O Wins!')
		disableAllButton()
		
	elif b4["text"] == "O" and b5["text"] =="O" and b6["text"] =="O":
		b4.config(bg ="green")
		b5.config(bg ="green")
		b6.config(bg ="green")
		winner = True
		messagebox.showinfo('Tic tac toe','Cingratulation!  O Wins!')
		disableAllButton()
		
	elif b7["text"] == "O" and b8["text"] =="O" and b9["text"] =="O":
		b7.config(bg ="green")
		b8.config(bg ="green")
		b9.config(bg ="green")
		winner = True
		messagebox.showinfo('Tic tac toe','Cingratulation!  O Wins!')
		disableAllButton()

	elif b1["text"] == "O" and b4["text"] =="O" and b7["text"] =="O":
		b1.config(bg ="green")
		b4.config(bg ="green")
		b7.config(bg ="green")
		winner = True
		messagebox.showinfo('Tic tac toe','Cingratulation!  O Wins!')
		disableAllButton()

	elif b2["text"] == "O" and b5["text"] =="O" and b8["text"] =="O":
		b2.config(bg ="green")
		b5.config(bg ="green")
		b8.config(bg ="green")
		winner = True
		messagebox.showinfo('Tic tac toe','Cingratulation!  O Wins!')
		disableAllButton()

	elif b3["text"] == "O" and b6["text"] =="O" and b9["text"] =="O":
		b3.config(bg ="green")
		b6.config(bg ="green")
		b9.config(bg ="green")
		winner = True
		messagebox.showinfo('Tic tac toe','Cingratulation!  O Wins!')
		disableAllButton()

	elif b1["text"] == "O" and b5["text"] =="O" and b9["text"] =="O":
		b1.config(bg ="green")
		b5.config(bg ="green")
		b9.config(bg ="green")
		winner = True
		messagebox.showinfo('Tic tac toe','Cingratulation!  O Wins!')
		disableAllButton()


	elif b3["text"] == "O" and b5["text"] =="O" and b7["text"] =="O":
		b3.config(bg ="green")
		b5.config(bg ="green")
		b7.config(bg ="green")
		winner = True
		messagebox.showinfo('Tic tac toe','Cingratulation!  O Wins!')
		disableAllButton()

	if count == 9 and winner == False :
		messagebox.showinfo('Tic tac toe','Tie! no one Win!')

#start
def b_click(b):
	global Clicked, count
	
	if b["text"] == " " and Clicked == True:
		b.config(text = 'X')
		b["text"] == "X"
		Clicked = False
		count += 1
		print('X turn')
		checkifwon()
	elif b["text"] == " " and Clicked == False:
		b.config(text = 'O')
		b["text"] == "O"
		Clicked = True
		count += 1
		print('O turn')
		checkifwon()
	else:
		messagebox.showerror('Tic tac toe','that box have already been Clicked')
	print(count)
	
def reset():
	global b1, b2, b3, b4, b5, b6, b7, b8, b9
	global Clicked,count
	Clicked = True
	count = 0
	b1 = Button(root,text = ' ',font=(None,20),height = 3, width = 6,bg="SystemButtonFace",command=lambda: b_click(b1))
	b2 = Button(root,text = ' ',font=(None,20),height = 3, width = 6,bg="SystemButtonFace",command=lambda: b_click(b2))
	b3 = Button(root,text = ' ',font=(None,20),height = 3, width = 6,bg="SystemButtonFace",command=lambda: b_click(b3))

	b4 = Button(root,text = ' ',font=(None,20),height = 3, width = 6,bg="SystemButtonFace",command=lambda: b_click(b4))
	b5 = Button(root,text = ' ',font=(None,20),height = 3, width = 6,bg="SystemButtonFace",command=lambda: b_click(b5))
	b6 = Button(root,text = ' ',font=(None,20),height = 3, width = 6,bg="SystemButtonFace",command=lambda: b_click(b6))

	b7 = Button(root,text = ' ',font=(None,20),height = 3, width = 6,bg="SystemButtonFace",command=lambda: b_click(b7))
	b8 = Button(root,text = ' ',font=(None,20),height = 3, width = 6,bg="SystemButtonFace",command=lambda: b_click(b8))
	b9 = Button(root,text = ' ',font=(None,20),height = 3, width = 6,bg="SystemButtonFace",command=lambda: b_click(b9))

	b1.grid(row=0,column=0)
	b2.grid(row=0,column=1)
	b3.grid(row=0,column=2)

	b4.grid(row=1,column=0)
	b5.grid(row=1,column=1)
	b6.grid(row=1,column=2)

	b7.grid(row=2,column=0)
	b8.grid(row=2,column=1)
	b9.grid(row=2,column=2)

myMenu = Menu(root)
root.config(menu = myMenu)

optionsMenu = Menu(myMenu, tearoff = False)
myMenu.add_cascade(label="options",menu=optionsMenu)
optionsMenu.add_command(label='Reset Game',command=reset)


reset()
root.mainloop()