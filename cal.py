#!/usr/bin/env python3

"""A basic simple calculator developed using procedures perfoming
addition,subtraction,multiplication and division"""

import tkinter as tk

def addition():
   try:
     first=float(first_entry.get())
     second=float(second_entry.get())

     result=first+second

     now=datetime.now()
     result_label.config(text=f"Result is {result}")

   except ValueError:
    result_label.config(text="Please enter valid numbers")


def subtraction():
   try:
    first=float(first_entry.get())
    second=float(second_entry.get())

    result=first-second

    result_label.config(text=f"Result: {result}")

   except ValueError:
    result_label.config(text="Please enter valid numbers")


def multiplication():
   try:
    first=float(first_entry.get())
    second=float(second_entry.get())

    result=first * second
    result_label.config(text=f"Result:{result}")

   except ValueError:
    result_label.config(text="Please enter valid numbers")


def division():
  try:
    first=float(first_entry.get())
    second=float(second_entry.get())
    try:
     result=first/second
     result_label.config(text=f"Result :{result}")
    except ZeroDivisionError:
     result_label.config(text="Zero division Error")
  except ValueError:
   result_label.config(text="Please enter valid numbers")



#Main Window
window=tk.Tk()
window.title("Calculator")
window.geometry("500x500")

#Title
title_label=tk.Label(window,text="My calculator",font=("Algerian",26,"bold"))
title_label.pack(pady=5)

#First number

first_label=tk.Label(window,text="First number",font=("Algerian",12))
first_label.pack()

first_entry=tk.Entry(window,font=("Algerian",14),width=30)
first_entry.pack(pady=5)


#Second Number 
second_label=tk.Label(window,text="Second number",font=("Algerian",12))
second_label.pack()

second_entry=tk.Entry(window,font=("Algerian",14),width=30)
second_entry.pack(pady=5)



#Addition button
add_button=tk.Button(window,text="ADD",font=("Algerian",12,"bold"),width=15,command=addition)
add_button.pack(pady=5)

#Subtraction button

subtract_button=tk.Button(window,text="Subtract",font=("Algerian",12,"bold"),width=15,command=subtraction)
subtract_button.pack(pady=5)

#Divide button
divide_button=tk.Button(window,text="Divide",font=("Algerian",12,"bold"),width=15,command=division)
divide_button.pack(pady=5)

#Multiplication button
multiply_button=tk.Button(window,text="Multiply",font=("Algerian",12,"bold"),width=15,command=multiplication)
multiply_button.pack(pady=5)

#Result button
result_label=tk.Button(window,text="Result:",font=("Algerian",12,"bold"),width=15)
result_label.pack(pady=5)

window.mainloop()




