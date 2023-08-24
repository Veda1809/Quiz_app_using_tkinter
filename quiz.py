#import modules
from tkinter import messagebox
from tkinter import*

root = Tk()
root.config(background="Black")
root.title("Quiz")



def correct_answer_q1():
	messagebox.showinfo("Correct answer",
						"You have selected the correct answer!! ")
	q1_scr.destroy()

def wrong_answer_q1():
	messagebox.showerror("Wrong answer",
						"You have selected a wrong answer. \nPlease reattempt the question")
	
    
    
def question_1():
	global q1_scr
	q1_scr = Toplevel(root)
	q1_scr.config(background="Black")
	q1_scr.title("Question 1")
	   
	# Lable
	Label(q1_scr, text="Question 1", fg="Green", bg="Black", font=("Times new roman", 20)).grid(row=0,sticky=N,pady=5)
	Label(q1_scr, text="What's the world's most ancient game?", fg="Green", bg="Black", font=("Times new roman", 20)).grid(row=1,sticky=N,pady=5)
	Label(q1_scr, text="Hockey", fg="red", bg="Black", font=("Times new roman", 15)).grid(row=2,sticky=W, pady=5)  
	Label(q1_scr, text="Wrestling", fg="red", bg="Black", font=("Times new roman", 15)).grid(row=3,sticky=W, pady=5)  
	Label(q1_scr, text="Chess", fg="red", bg="Black", font=("Times new roman", 15)).grid(row=4,sticky=W, pady=5)
	Label(q1_scr, text="Cricket", fg="red", bg="Black", font=("Times new roman", 15)).grid(row=5,sticky=W, pady=5)

	# Buttons
	Button(q1_scr, text="A", fg="Blue", bg="red", font=("Times new roman", 15), command=wrong_answer_q1).grid(row=2, sticky=W, pady=5, padx=250)  
	Button(q1_scr, text="B", fg="Blue", bg="red", font=("Times new roman", 15), command=correct_answer_q1).grid(row=3, sticky=W, pady=5, padx=250)  
	Button(q1_scr, text="C", fg="Blue", bg="red", font=("Times new roman", 15), command=wrong_answer_q1).grid(row=4, sticky=W, pady=5, padx=250)  
	Button(q1_scr, text="D", fg="Blue", bg="red", font=("Times new roman", 15), command=wrong_answer_q1).grid(row=5, sticky=W, pady=5, padx=250)  




def correct_answer_q2():
	messagebox.showinfo("Correct answer",
						"You have selected the correct answer!! ")
	q2_scr.destroy()

def wrong_answer_q2():
	messagebox.showerror("Wrong answer",
						"You have selected a wrong answer. \nPlease reattempt the question")
						


def question_2():
	global q2_scr
	q2_scr = Toplevel(root)
	q2_scr.config(background="Black")
	q2_scr.title("Question 2")
	  
	# Lable
	Label(q2_scr, text="Question 1", fg="Green", bg="Black", font=("Times new roman", 20)).grid(row=0,sticky=N,pady=5)
	Label(q2_scr, text="Name the Largest organ in the human body.", fg="Green", bg="Black", font=("Times new roman", 20)).grid(row=1,sticky=N,pady=5)
	Label(q2_scr, text="brain", fg="red", bg="Black", font=("Times new roman", 15)).grid(row=2,sticky=W, pady=5)  
	Label(q2_scr, text="lungs", fg="red", bg="Black", font=("Times new roman", 15)).grid(row=3,sticky=W, pady=5)  
	Label(q2_scr, text="skin", fg="red", bg="Black", font=("Times new roman", 15)).grid(row=4,sticky=W, pady=5)
	Label(q2_scr, text="small intestine", fg="red", bg="Black", font=("Times new roman", 15)).grid(row=5,sticky=W, pady=5)

	# Buttons
	Button(q2_scr, text="A", fg="Blue", bg="red", font=("Times new roman", 15), command=wrong_answer_q2).grid(row=2, sticky=W, pady=5, padx=250)  
	Button(q2_scr, text="B", fg="Blue", bg="red", font=("Times new roman", 15), command=wrong_answer_q2).grid(row=3, sticky=W, pady=5, padx=250)  
	Button(q2_scr, text="C", fg="Blue", bg="red", font=("Times new roman", 15), command=correct_answer_q2).grid(row=4, sticky=W, pady=5, padx=250)  
	Button(q2_scr, text="D", fg="Blue", bg="red", font=("Times new roman", 15), command=wrong_answer_q2).grid(row=5, sticky=W, pady=5, padx=250)  




def correct_answer_q3():
	messagebox.showinfo("Correct answer",
						"You have selected the correct answer!! ")
	q3_scr.destroy()

def wrong_answer_q3():
	messagebox.showerror("Wrong answer",
						"You have selected a wrong answer. \nPlease reattempt the question")
						


def question_3():
	global q3_scr
	q3_scr = Toplevel(root)
	q3_scr.config(background="Black")
	q3_scr.title("Question 3")
	  
	# Lable
	Label(q3_scr, text="Question 3", fg="Green", bg="Black", font=("Times new roman", 20)).grid(row=0,sticky=N,pady=5)
	Label(q3_scr, text="Which city is known as 'The Holy Land'.", fg="Green", bg="Black", font=("Times new roman", 20)).grid(row=1,sticky=N,pady=5)
	Label(q3_scr, text="Vatican", fg="red", bg="Black", font=("Times new roman", 15)).grid(row=2,sticky=W, pady=5)  
	Label(q3_scr, text="Beirut", fg="red", bg="Black", font=("Times new roman", 15)).grid(row=3,sticky=W, pady=5)  
	Label(q3_scr, text="Barcelona", fg="red", bg="Black", font=("Times new roman", 15)).grid(row=4,sticky=W, pady=5)
	Label(q3_scr, text="Palestine", fg="red", bg="Black", font=("Times new roman", 15)).grid(row=5,sticky=W, pady=5)

	# Buttons
	Button(q3_scr, text="A", fg="Blue", bg="red", font=("Times new roman", 15), command=wrong_answer_q3).grid(row=2, sticky=W, pady=5, padx=250)  
	Button(q3_scr, text="B", fg="Blue", bg="red", font=("Times new roman", 15), command=wrong_answer_q3).grid(row=3, sticky=W, pady=5, padx=250)  
	Button(q3_scr, text="C", fg="Blue", bg="red", font=("Times new roman", 15), command=wrong_answer_q3).grid(row=4, sticky=W, pady=5, padx=250)  
	Button(q3_scr, text="D", fg="Blue", bg="red", font=("Times new roman", 15), command=correct_answer_q3).grid(row=5, sticky=W, pady=5, padx=250)  


def correct_answer_q4():
	messagebox.showinfo("Correct answer",
						"You have selected the correct answer!! ")
	q4_scr.destroy()

def wrong_answer_q4():
	messagebox.showerror("Wrong answer",
						"You have selected a wrong answer. \nPlease reattempt the question")
						


def question_4():
	global q4_scr
	q4_scr = Toplevel(root)
	q4_scr.config(background="Black")
	q4_scr.title("Question 4")
	  
	# Lable
	Label(q4_scr, text="Question 4", fg="Green", bg="Black", font=("Times new roman", 20)).grid(row=0,sticky=N,pady=5)
	Label(q4_scr, text="Which city is known as 'Silicon city'.", fg="Green", bg="Black", font=("Times new roman", 20)).grid(row=1,sticky=N,pady=5)
	Label(q4_scr, text="Mumbai", fg="red", bg="Black", font=("Times new roman", 15)).grid(row=2,sticky=W, pady=5)  
	Label(q4_scr, text="Jaipur", fg="red", bg="Black", font=("Times new roman", 15)).grid(row=3,sticky=W, pady=5)  
	Label(q4_scr, text="Manglore", fg="red", bg="Black", font=("Times new roman", 15)).grid(row=4,sticky=W, pady=5)
	Label(q4_scr, text="Banglore", fg="red", bg="Black", font=("Times new roman", 15)).grid(row=5,sticky=W, pady=5)

	# Buttons
	Button(q4_scr, text="A", fg="Blue", bg="red", font=("Times new roman", 15), command=wrong_answer_q3).grid(row=2, sticky=W, pady=5, padx=250)  
	Button(q4_scr, text="B", fg="Blue", bg="red", font=("Times new roman", 15), command=wrong_answer_q3).grid(row=3, sticky=W, pady=5, padx=250)  
	Button(q4_scr, text="C", fg="Blue", bg="red", font=("Times new roman", 15), command=wrong_answer_q3).grid(row=4, sticky=W, pady=5, padx=250)  
	Button(q4_scr, text="D", fg="Blue", bg="red", font=("Times new roman", 15), command=correct_answer_q3).grid(row=5, sticky=W, pady=5, padx=250)  



#Labels
Label(root,text="Quiz", fg="Red", bg="Black", font=("Algerian",20)).grid(row=0,column=2,sticky=N,pady=5)
Label(root,text="Questions", fg="green", bg="Black", font=("Times new Roman",18)).grid(row=1,column=2,sticky=N,pady=5)

#Buttons
Button(root,text="Question 1",fg="red", bg="Orange", font=("calibri",15), command=question_1 ).grid(row=3, sticky=W, column=1, pady=5, padx=10)
Button(root,text="Question 2",fg="red", bg="Orange", font=("calibri",15), command=question_2 ).grid(row=3, sticky=W, column=2, pady=5, padx=10)
Button(root,text="Question 3",fg="red", bg="Orange", font=("calibri",15), command=question_3 ).grid(row=3, sticky=W, column=6, pady=5, padx=10)
Button(root,text="Question 4",fg="red", bg="Orange", font=("calibri",15), command=question_4 ).grid(row=3, sticky=W, column=9, pady=5, padx=10)

root.mainloop()
