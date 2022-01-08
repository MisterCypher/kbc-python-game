import tkinter
from tkinter import messagebox
from tkinter import *
from PIL import Image,ImageTk
import winsound


class KBC:
    def main(self):
        root=tkinter.Tk() 
        root.attributes('-fullscreen', True)
        frame=Frame(root)
        root["bg"]="black"
        frame.pack()

        def lose():
            messagebox.showinfo("ANSWER","You lose")
            frame=Frame(root)
            root["bg"]="black";
            frame.pack()
            C = tkinter.Canvas(root, bg="black", height=250, width=1348)
            C.pack()
            C.place(x=0,y=452)
            L1=Label(root, text=" THANKS FOR PLAYING ",width="70",height="3")
            L1.pack()
            L1.place(y=350,x=450)
 
            b3=Button(root,text="REPLAY",width="40",height="4",command=play)
            b3.pack()
            b3.place(x=275,y=500)
            b6=Button(root,text="EXIT",width="40",height="4",command=root.destroy)
            b6.pack()
            b6.place(x=750,y=500)
            winsound.PlaySound("C:\Windows\Media\lose.wav",winsound.SND_FILENAME)
            root.mainloop()
        
        def play():
           if e1.get().isalpha() and name != "":
             p1()
           else:
             messagebox.showinfo("Alert","Enter Name")
       
        




        def p1():
            start()
            frame=Frame(root)
            root["bg"]="black";
            frame.pack()
            C = tkinter.Canvas(root, bg="black", height=250, width=1348)
            C.pack()
            C.place(x=0,y=452)
            L1=Label(root, text=" 1.   Which is the smallest state in India ",width="70",height="3")
            L1.pack()
            L1.place(y=350,x=450)
            b3=Button(root,text="A. Goa",width="40",height="4",command=p2)
            b3.pack()
            b3.place(x=275,y=500)
            b4=Button(root,text="C. Maharashta",width="40",height="4",command=lose)
            b4.pack()
            b4.place(x=275,y=600)
            b5=Button(root,text="D. Tripura",width="40",height="4",command=lose)
            b5.pack()
            b5.place(x=750,y=600)
            b6=Button(root,text="B. Kerala",width="40",height="4",command=lose)
            b6.pack()
            b6.place(x=750,y=500)
            root.mainloop()
        def p2():
            messagebox.showinfo("ANSWER","You are right you win 5 thousand")
            winsound.PlaySound("C:\Windows\Media\clap.wav",winsound.SND_FILENAME)
            frame=Frame(root)
            root["bg"]="black";
            frame.pack()
            C = tkinter.Canvas(root, bg="black", height=250, width=1348)
            C.pack()
            C.place(x=0,y=452)
            L1=Label(root, text=" 2.   Who is the founder of facebook ",width="70",height="3")
            L1.pack()
            L1.place(y=350,x=450)
 
            b3=Button(root,text="A. Steve jobs",width="40",height="4",command=lose)
            b3.pack()
            b3.place(x=275,y=500)
            b4=Button(root,text="C. Bill gates",width="40",height="4",command=lose)
            b4.pack()
            b4.place(x=275,y=600)
            b5=Button(root,text="D. Mark Zuckerberg",width="40",height="4",command=p3)
            b5.pack()
            b5.place(x=750,y=600)
            b6=Button(root,text="B. Amin gray",width="40",height="4",command=lose) 
            b6.pack()
            b6.place(x=750,y=500)
            root.mainloop()    

        def p3():
            messagebox.showinfo("ANSWER","You are rigth,you win 10 thousand")
            winsound.PlaySound("C:\Windows\Media\clap.wav",winsound.SND_FILENAME)
            frame=Frame(root)
            root["bg"]="black";
            frame.pack()
            C = tkinter.Canvas(root, bg="black", height=250, width=1348)
            C.pack()
            C.place(x=0,y=452)
            L1=Label(root, text=" 3.Who is Narendra Nath Datta ",width="70",height="3")
            L1.pack()
            L1.place(y=350,x=450)
 
            b3=Button(root,text="A.SWAMI RAMKRISHNA    ",width="40",height="4",command=lose)
            b3.pack()
            b3.place(x=275,y=500)
            b4=Button(root,text="C.SWAMI SIVANANDA",width="40",height="4",command=lose)
            b4.pack()
            b4.place(x=275,y=600)
            b5=Button(root,text="D. SWAMI HARIDAS",width="40",height="4",command=lose)
            b5.pack()
            b5.place(x=750,y=600)
            b6=Button(root,text="B. SWAMI VIVEKANANDA ",width="40",height="4",command=audioquestion)
            b6.pack()
            b6.place(x=750,y=500)
            root.mainloop()

        def audioquestion():
            messagebox.showinfo("ANSWER","You are right,you win 20 thousand")
            winsound.PlaySound("C:\Windows\Media\clap.wav",winsound.SND_FILENAME)
            frame=Frame(root)
            root["bg"]="black";
            frame.pack()
            C = tkinter.Canvas(root, bg="black", height=250, width=1348)
            C.pack()
            C.place(x=0,y=452)
            L1=Label(root, text=" 4.Identify the poet of the poem from the audio?  ",width="70",height="3")
            L1.pack()
            L1.place(y=350,x=450)
            b3=Button(root,text="A.Listen Audio ",width="40",height="4",command=p4)
            b3.pack()
            b3.place(x=500,y=500)
            root.mainloop()

        def p4():
            winsound.PlaySound("C:\Windows\Media\poem.wav",winsound.SND_FILENAME)
            frame=Frame(root)
            root["bg"]="black";
            frame.pack()
            C = tkinter.Canvas(root, bg="black", height=250, width=1348)
            C.pack()
            C.place(x=0,y=452)
            L1=Label(root, text=" 4.Identify the poet of the poem from the audio?  ",width="70",height="3")
            L1.pack()
            L1.place(y=350,x=450)
            b3=Button(root,text="A.Harivansh rai bachchan ",width="40",height="4",command=p5)
            b3.pack()
            b3.place(x=275,y=500)
            b4=Button(root,text="C.Amitabh Bachchan",width="40",height="4",command=lose)
            b4.pack()
            b4.place(x=275,y=600)
            b5=Button(root,text="D. Premchand",width="40",height="4",command=lose)
            b5.pack()
            b5.place(x=750,y=600)
            b6=Button(root,text="B. Jaishankar Prasad",width="40",height="4",command=lose)
            b6.pack()
            b6.place(x=750,y=500)
            root.mainloop()

        def p5():
            messagebox.showinfo("ANSWER","You are right,you win 40 thousand")
            winsound.PlaySound("C:\Windows\Media\clap.wav",winsound.SND_FILENAME)
            frame=Frame(root)
            root["bg"]="black";
            frame.pack()
            C = tkinter.Canvas(root, bg="black", height=250, width=1348)
            C.pack()
            C.place(x=0,y=452)
            L1=Label(root, text=" 5.Which of these places is not located in Mumbai?  ",width="70",height="3")
            L1.pack()
            L1.place(y=350,x=450)
            b3=Button(root,text="A.The Gateway of India  ",width="40",height="4",command=lose)
            b3.pack()
            b3.place(x=275,y=500)
            b4=Button(root,text="C.The Kamala Nehru Park ",width="40",height="4",command=lose)
            b4.pack()
            b4.place(x=275,y=600)
            b5=Button(root,text="D. The Juhu Beach ",width="40",height="4",command=lose)
            b5.pack()
            b5.place(x=750,y=600)
            b6=Button(root,text="B. The Charminar",width="40",height="4",command=p6)
            b6.pack()
            b6.place(x=750,y=500)
            root.mainloop()

        def p6():
                 messagebox.showinfo("ANSWER","You are right,you win 80 thousand")
                 winsound.PlaySound("C:\Windows\Media\clap.wav",winsound.SND_FILENAME)
                 frame=Frame(root)
                 root["bg"]="black";
                 frame.pack()
                 C = tkinter.Canvas(root, bg="black", height=250, width=1348)
                 C.pack()
                 C.place(x=0,y=452)
                 L1=Label(root, text=" 6.Which is the world's tallest statue?  ",width="70",height="3")
                 L1.pack()
                 L1.place(y=350,x=450)
                 b3=Button(root,text="A.Statue of Liberty  ",width="40",height="4",command=lose)
                 b3.pack()
                 b3.place(x=275,y=500)
                 b4=Button(root,text="C.Statue of Unity ",width="40",height="4",command=p7)
                 b4.pack()
                 b4.place(x=275,y=600)
                 b5=Button(root,text="D. Statue of Diversity ",width="40",height="4",command=lose)
                 b5.pack()
                 b5.place(x=750,y=600)
                 b6=Button(root,text="B. Statue of Fraternity",width="40",height="4",command=lose)
                 b6.pack()
                 b6.place(x=750,y=500)
                 root.mainloop()

        def p7():
                 messagebox.showinfo("ANSWER","You are right,you win 1 lakh 60 thousand")
                 winsound.PlaySound("C:\Windows\Media\clap.wav",winsound.SND_FILENAME)
                 frame=Frame(root)
                 root["bg"]="black";
                 frame.pack()
                 C = tkinter.Canvas(root, bg="black", height=250, width=1348)
                 C.pack()
                 C.place(x=0,y=452)
                 L1=Label(root, text=" 7.Which of these married couples represents India  in the same sport   ?  ",width="70",height="3")
                 L1.pack()
                 L1.place(y=350,x=450)
                 b3=Button(root,text="A.Pratima Singh, Ishant Sharma",width="40",height="4",command=lose)
                 b3.pack()
                 b3.place(x=275,y=500)
                 b4=Button(root,text="C.Sania Mirza, Shoaib Malik ",width="40",height="4",command=lose)
                 b4.pack()
                 b4.place(x=275,y=600)
                 b5=Button(root,text="D. Dipika Pallikal, Dinesh Karthik ",width="40",height="4",command=lose)
                 b5.pack()
                 b5.place(x=750,y=600)
                 b6=Button(root,text="B. Saina Nehwal, P Kashyap",width="40",height="4",command=p8)
                 b6.pack()
                 b6.place(x=750,y=500)
                 root.mainloop()

        def p8():
                 messagebox.showinfo("ANSWER","You are right,you win 3 lakh 20 thousand")
                 winsound.PlaySound("C:\Windows\Media\clap.wav",winsound.SND_FILENAME)
                 frame=Frame(root)
                 root["bg"]="black";
                 frame.pack()
                 C = tkinter.Canvas(root, bg="black", height=250, width=1348)
                 C.pack()
                 C.place(x=0,y=452)
                 L1=Label(root, text=" 8.Which of the following is the shankh of Lord Shree Krishna ?  ",width="70",height="3")
                 L1.pack()
                 L1.place(y=350,x=450)
                 b3=Button(root,text="A.Anantavijaya",width="40",height="4",command=lose)
                 b3.pack()
                 b3.place(x=275,y=500)
                 b4=Button(root,text="C.Devdutt ",width="40",height="4",command=lose)
                 b4.pack()
                 b4.place(x=275,y=600)
                 b5=Button(root,text="D. Panchajanya ",width="40",height="4",command=p9)
                 b5.pack()
                 b5.place(x=750,y=600)
                 b6=Button(root,text="B. Paundr",width="40",height="4",command=lose)
                 b6.pack()
                 b6.place(x=750,y=500)
                 root.mainloop()

        def p9():
                 messagebox.showinfo("ANSWER","You are right,you win 6 lakh 40 thousand")
                 winsound.PlaySound("C:\Windows\Media\clap.wav",winsound.SND_FILENAME)
                 frame=Frame(root)
                 root["bg"]="black";
                 frame.pack()
                 C = tkinter.Canvas(root, bg="black", height=250, width=1348)
                 C.pack()
                 C.place(x=0,y=452)
                 L1=Label(root, text=" 9.Bimbisara was the founder of which one of the following dynasties?  ",width="70",height="3")
                 L1.pack()
                 L1.place(y=350,x=450)
                 b3=Button(root,text="A.Nanda",width="40",height="4",command=lose)
                 b3.pack()
                 b3.place(x=275,y=500)
                 b4=Button(root,text="C.Haryanka ",width="40",height="4",command=p10)
                 b4.pack()
                 b4.place(x=275,y=600)
                 b5=Button(root,text="D. Maurya ",width="40",height="4",command=lose)
                 b5.pack()
                 b5.place(x=750,y=600)
                 b6=Button(root,text="B. Shunga",width="40",height="4",command=lose)
                 b6.pack()
                 b6.place(x=750,y=500)
                 root.mainloop()

        def p10():
                 messagebox.showinfo("ANSWER","You are right,you win 12 lakh 80 thousand")
                 winsound.PlaySound("C:\Windows\Media\clap.wav",winsound.SND_FILENAME)
                 frame=Frame(root)
                 root["bg"]="black";
                 frame.pack()
                 C = tkinter.Canvas(root, bg="black", height=250, width=1348)
                 C.pack()
                 C.place(x=0,y=452)
                 L1=Label(root, text=" 10.What was the name of the first animal which was sent to space?  ",width="70",height="3")
                 L1.pack()
                 L1.place(y=350,x=450)
                 b3=Button(root,text="A.Laika",width="40",height="4",command=p11)
                 b3.pack()
                 b3.place(x=275,y=500)
                 b4=Button(root,text="C. Strelka ",width="40",height="4",command=lose)
                 b4.pack()
                 b4.place(x=275,y=600)
                 b5=Button(root,text="D.Belka ",width="40",height="4",command=lose)
                 b5.pack()
                 b5.place(x=750,y=600)
                 b6=Button(root,text="B. Gordo",width="40",height="4",command=lose)
                 b6.pack()
                 b6.place(x=750,y=500)
                 root.mainloop()
              
        def p11():
                 messagebox.showinfo("ANSWER","You are right,you win 50 lakh")
                 winsound.PlaySound("C:\Windows\Media\clap.wav",winsound.SND_FILENAME)
                 frame=Frame(root)
                 root["bg"]="black";
                 frame.pack()
                 C = tkinter.Canvas(root, bg="black", height=250, width=1348)
                 C.pack()
                 C.place(x=0,y=452)
                 L1=Label(root, text=" 11.Which of the following is not a pair of parent and child, who have both won Nobel Prizes?  ",width="70",height="3")
                 L1.pack()
                 L1.place(y=350,x=450)
                 b3=Button(root,text="A.Marie Curie, Irene Joliot Curie",width="40",height="4",command=lose)
                 b3.pack()
                 b3.place(x=275,y=500)
                 b4=Button(root,text="C.JJ Thomson, George Paget Thomson ",width="40",height="4",command=lose)
                 b4.pack()
                 b4.place(x=275,y=600)
                 b5=Button(root,text="D.Niels Bohr, Aage Bohr",width="40",height="4",command=lose)
                 b5.pack()
                 b5.place(x=750,y=600)
                 b6=Button(root,text="B. Herman Emil Fischer, Hans Fischer",width="40",height="4",command=winner)
                 b6.pack()
                 b6.place(x=750,y=500)
                 root.mainloop()
              
        def winner():
            messagebox.showinfo("ANSWER","You are right,you win 1 crore ")
            winsound.PlaySound("C:\Windows\Media\clap.wav",winsound.SND_FILENAME)
            frame=Frame(root)
            root["bg"]="black";
            frame.pack()
            C = tkinter.Canvas(root, bg="black", height=250, width=1348)
            C.pack()
            C.place(x=0,y=452)
            L1=Label(root, text=e1.get()+" You become crorepati  ",width="70",height="3")
            L1.pack()
            L1.place(y=350,x=450)
            b3=Button(root,text="REPLAY",width="40",height="4",command=play)
            b3.pack()
            b3.place(x=275,y=500)
            b6=Button(root,text="EXIT",width="40",height="4",command=root.destroy)
            b6.pack()
            b6.place(x=750,y=500)
            root.mainloop()   

        def start():
             messagebox.showinfo("Welcome","Hello "+e1.get()+" get ready to play")
             winsound.PlaySound("C:\Windows\Media\kbcopen",winsound.SND_FILENAME)
          
        C = tkinter.Canvas(root, bg="purple4", height=450, width=1362)
        C.pack()
        C.place(x=0,y=0)
        img = ImageTk.PhotoImage(Image.open("kbc.jpg"))
        panel = Label(root, image = img,width=500,height=282)
        panel.pack()
        panel.place(x=0,y=0)
        img1 = ImageTk.PhotoImage(Image.open("kbc.jpg"))
        panel1 = Label(root, image = img,width=500,height=282)
        panel1.pack()
        panel1.place(x=450,y=0)
        img2 = ImageTk.PhotoImage(Image.open("kbc.jpg"))
        panel2 = Label(root, image = img,width=500,height=282)
        panel2.pack()
        panel2.place(x=845,y=0)
        img3 = ImageTk.PhotoImage(Image.open("kbc.jpg"))
        panel3 = Label(root, image = img,width=300,height=50)
        panel3.pack()
        panel3.place(x=0,y=285)
        img4 = ImageTk.PhotoImage(Image.open("kbc.jpg"))
        panel4 = Label(root, image = img,width=300,height=50)
        panel4.pack()
        panel4.place(x=0,y=337)
        img5 = ImageTk.PhotoImage(Image.open("kbc.jpg"))
        panel5 = Label(root, image = img,width=300,height=60)
        panel5.pack()
        panel5.place(x=0,y=390)
        img6 = ImageTk.PhotoImage(Image.open("kbc.jpg"))
        panel6 = Label(root, image = img,width=300,height=50)
        panel6.pack()
        panel6.place(x=1050,y=285)
        img7 = ImageTk.PhotoImage(Image.open("kbc.jpg"))
        panel7 = Label(root, image = img,width=300,height=50)
        panel7.pack()
        panel7.place(x=1050,y=337)
        img8 = ImageTk.PhotoImage(Image.open("kbc.jpg"))
        panel8 = Label(root, image = img,width=300,height=60)
        panel8.pack()
        panel8.place(x=1050,y=390)
        b1=Button(root,text="PLAY",command=play,width=15,height=2)
        b1.pack()
        b1.place(x=500,y=350)
        b2=Button(root,text="QUIT",command=root.destroy,width=15,height=2)
        b2.pack()
        b2.place(x=700,y=350)
        scrolebar=Scrollbar(root,)
        scrolebar.pack(side=RIGHT,fill=Y)
        name = Label(root, text = "Enter your Name").place(x = 500,y = 500)
        e1 = Entry(root)
        e1.place(x = 600, y = 500)
        root.mainloop()
                         
k=KBC()
k.main()






































