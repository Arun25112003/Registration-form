import tkinter as tk 
from tkinter import messagebox
root=tk.Tk()
root.geometry("450x200")
root.configure(background="lightgreen")
root.title(‘SRMJEEE REGISTRARTION FORM’)
a=tk.Label(root, text='Form',background="lightgreen").grid(row=0,column=1)
l1 = tk.Label(root,text = "Name ", background="lightgreen").grid(row = 1, column = 0) t=tk.Entry(root,width=40).grid(row=1,column=1)
l2=tk.Label(root,text="Course ", background="lightgreen").grid(row = 2, column = 0) t=tk.Entry(root,width=40).grid(row=2,column=1)
l3=tk.Label(root,text="Semester ", background="lightgreen").grid(row = 3, column = 0) t=tk.Entry(root, width=40).grid(row=3,column=1)
l4 = tk.Label(root,text ="Form No. ",background="lightgreen").grid(row = 4, column = 0) t=tk.Entry(root, width=40).grid(row=4,column=1)
l5=tk.Label(root,text="Contact No. ",background="lightgreen").grid(row = 5, column = 0) t=tk.Entry(root, width=40).grid(row=5,column=1)
l6=tk.Label(root,text="Email id ",background="lightgreen").grid(row = 6, column = 0) t=tk.Entry(root,width=40).grid(row=6,column=1)
l6=tk.Label(root,text="Address ",background="lightgreen").grid(row = 7, column = 0) t=tk.Entry(root,width=40).grid(row=7,column=1)
button=tk.Button(root, text='Submit', width=6, background="red").grid(row=8,column=1)
root.mainloop()
