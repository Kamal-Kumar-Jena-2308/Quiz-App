from tkinter import *
import tkinter.font as fnt
import requests
import json
from PIL import Image, ImageTk
import random
from tkinter import messagebox
api_url = 'https://the-trivia-api.com/api/questions?categories=science,general_knowledge&limit=5&difficulty=easy'
response = requests.get(api_url)
responsetext=response.text
rtext=json.loads(responsetext)
marks=0
if __name__ == '__main__':
    def sumup():
        root=Tk()
        root.title('Trivia - By Kamal Kumar Jena')
        root.config(bg="#FF6700")
        root.geometry("450x100")
        root.resizable(False,False)
        labelk=Label(text=f"Your score is {marks}/25",font=fnt.Font(size=20),bg="#FF6700")
        labelk1=Label(text=f"For each correct answer +5\nFor each incorrent answer -3",font=fnt.Font(size=11),bg="#FF6700").place(x=125,y=60)        
        labelk.pack()
        img=Image.open('img.jpg')
        img=img.resize((80,80), Image.ANTIALIAS)
        img=ImageTk.PhotoImage(img)
        z=Label(image=img).place(x=370,y=18)
        root.mainloop()
    for i in range(5):
        tk=Tk()
        tk.config(bg="#FFD700")
        question=f'Q{i+1}.'+rtext[i].get('question')
        answer=rtext[i].get('correctAnswer')
        choice=rtext[i].get('incorrectAnswers')
        choice.append(answer)
        random.shuffle(choice)
        choice1=choice[0]
        choice2=choice[1]
        choice3=choice[2]
        choice4=choice[3]
        def check():
            global marks
            if a1.cget('text') == answer:
                tk.config(bg="green")
                label.config(bg="green")
                messagebox.showinfo("Correct", "Well Done! Your answer is correct!")
                marks+=5
                tk.destroy()
            else:
                label.config(bg="red")
                tk.config(bg="red")
                messagebox.showinfo("Wrong", f"Your answer is Wrong.\nThe Correct answer is {answer}")
                marks-=3
                tk.destroy()
        def check1():
            global marks
            if b1.cget('text') == answer:
                tk.config(bg="green")
                label.config(bg="green")
                messagebox.showinfo("Correct", "Well Done! Your answer is correct!")
                marks+=5
                tk.destroy()
            else:
                label.config(bg="red")
                tk.config(bg="red")
                messagebox.showinfo("Wrong", f"Your answer is Wrong.\nThe Correct answer is {answer}")    
                marks-=3
                tk.destroy()
        def check2():
            global marks
            if c1.cget('text') == answer:
                label.config(bg="green")                
                tk.config(bg="green")
                messagebox.showinfo("Correct", "Well Done! Your answer is correct!")
                marks+=5
                tk.destroy()
            else:
                label.config(bg="red")
                tk.config(bg="red")
                messagebox.showinfo("Wrong", f"Your answer is Wrong.\nThe Correct answer is {answer}")
                marks-=3
                tk.destroy()
        def check3():
            global marks
            if d1.cget('text') == answer:
                label.config(bg="green")                
                tk.config(bg="green")
                messagebox.showinfo("Correct", "Well Done! Your answer is correct!")
                marks+=5
                tk.destroy()
            else:
                label.config(bg="red")
                tk.config(bg="red")
                messagebox.showinfo("Wrong", f"Your answer is Wrong.\nThe Correct answer is {answer}")
                marks-=3
                tk.destroy()
        def bye():
            exit()
        label=Label(text=question,font=fnt.Font(size=14),bg="#FFD700")
        label.pack(pady=30,padx=15)
        a1=Button(text=choice1,command=lambda: check(),font=fnt.Font(size=14),borderwidth=2,relief=RAISED,bg="cyan")
        a1.pack(pady=10,padx=15)
        b1=Button(text=choice2,command=lambda: check1(),font=fnt.Font(size=14),borderwidth=2,relief=RAISED,bg="cyan")
        b1.pack(pady=10,padx=15)
        c1=Button(text=choice3,command=lambda: check2(),font=fnt.Font(size=14),borderwidth=2,relief=RAISED,bg="cyan")
        c1.pack(pady=10,padx=15)
        d1=Button(text=choice4,command=lambda: check3(),font=fnt.Font(size=14),borderwidth=2,relief=RAISED,bg="cyan")
        d1.pack(pady=10,padx=15)
        exitb=Button(text="Exit",command=bye,font=fnt.Font(size=14),borderwidth=2,relief=GROOVE)
        exitb.pack(anchor="ne",pady=30,padx=30)
        tk.resizable(False,False)
        tk.title("Trivia - By Kamal Kumar Jena")
        def db():
            pass
        tk.protocol("WM_DELETE_WINDOW",db)
        tk.mainloop()
    sumup()
