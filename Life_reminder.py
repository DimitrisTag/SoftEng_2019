import tkinter as tk
from tkinter import *
from tkinter import font as tkfont
import PIL
from tkinter.ttk import *
import time
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter.messagebox import showinfo

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Life reminder")
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Menu, IatrikaRantevou, Epiloges, Farmako, Eidopoihsh, Message, Notes, Thermides,MetritisThermidon, PosotitaNerou, Geuma,
                                            SomatikiAsk, NotConf, Xompi, Diafora, Ruthmiseis):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class Xrhsths():
    def __init__(self,genos, ipsos, kila, stoxos, *args, **kwargs):
        self.genos=genos
        self.ipsos-ipsos
        self.kila=kila
        self.stoxos=stoxos





class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        RELAXING_TIME = 3000


        self.controller = controller
        self.configure(background='white')

        basewidth = 500
        img = Image.open('logo.jpg')
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        img.save('resized_image.jpg')

        path = "resized_image.jpg"
        # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        img2 = ImageTk.PhotoImage(Image.open(path))


        # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        self.panel = tk.Label(self, image=img2)
        self.display = img2

        # The Pack geometry manager packs widgets in rows or columns.
        self.panel.pack(side="bottom", fill="both", expand="yes" )
        self.after(RELAXING_TIME, lambda: controller.show_frame("Menu"))

class Menu(tk.Frame):
    #Η κυρια οθονη που περιεχει ολες τις υποκατηγοριες
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        helv36 = tkfont.Font(family='Helvetica', size=13)
        label = tk.Label(self, text="Επιλέξτε μία κατηγορία από τις παρακάτω",
                         font=controller.title_font, background='white')
        label.pack(side="top", fill="x", pady=10)
        #οι εικονες που χρησιμοποιηθηκαν σε αυτη τη σελιδα
        self.kardia = tk.PhotoImage(file="rkardia.png")
        self.milo = tk.PhotoImage(file="rmilo.png")
        self.man = tk.PhotoImage(file="rman.png")
        self.gear = tk.PhotoImage(file="rgear.png")
        label = tk.Label(self, text="Υγεία", font=controller.title_font,background='white',
                         image=self.kardia, compound="left")
        label.pack(side="top", fill="x", pady=10)
        #hover functions
        def on_enter(e):
            rantevou['background'] = 'red'


        def on_leave(e):
            rantevou['background'] = 'SystemButtonFace'

        #καθε κουμπι κανει redirect σε αντιστοιχη σελιδα
        rantevou = tk.Button(self, text="Ιατρικά Ραντεβού",font = helv36, background='white',
                                            command=lambda: controller.show_frame("IatrikaRantevou"))
        rantevou.pack(fill='both')
        #in and out hover options
        rantevou.bind("<Enter>", on_enter)
        rantevou.bind("<Leave>", on_leave)

        def on_enter(e):
            farmaka['background'] = 'red'

        def on_leave(e):
            farmaka['background'] = 'SystemButtonFace'

        farmaka = tk.Button(self, text="Υπενθύμιση φαρμακευτικής αγωγής",font=helv36,background='white',
                                        command=lambda: controller.show_frame("Farmako"))
        farmaka.pack(fill='both')
        farmaka.bind("<Enter>", on_enter)
        farmaka.bind("<Leave>", on_leave)
        def on_enter(e):
            simeiwseis['background'] = 'red'

        def on_leave(e):
            simeiwseis['background'] = 'SystemButtonFace'
        simeiwseis = tk.Button(self, text="Σημειώσεις",font=helv36,background='white',
                                        command=lambda: controller.show_frame("Notes"))
        simeiwseis.pack(fill='both')
        simeiwseis.bind("<Enter>", on_enter)
        simeiwseis.bind("<Leave>", on_leave)

        label = tk.Label(self, text=" Διατροφή", font=controller.title_font, background='white',
                         image=self.milo, compound="left")
        label.pack(side="top", fill="x", pady=10)

        def on_enter(e):
            calcal['background'] = 'red'

        def on_leave(e):
            calcal['background'] = 'SystemButtonFace'

        calcal = tk.Button(self, text="Θερμιδομετρητής", font = helv36,background='white',
                        command=lambda: controller.show_frame("Thermides"))
        calcal.pack(fill='both')
        calcal.bind("<Enter>", on_enter)
        calcal.bind("<Leave>", on_leave)
        def on_enter(e):
            watercon['background'] = 'red'

        def on_leave(e):
            watercon['background'] = 'SystemButtonFace'
        watercon = tk.Button(self, text="Κατανάλωση Νερού", font=helv36,background='white',
                                    command=lambda: controller.show_frame("PosotitaNerou"))
        watercon.pack(fill='both')
        watercon.bind("<Enter>", on_enter)
        watercon.bind("<Leave>", on_leave)
        def on_enter(e):
            foodp['background'] = 'red'

        def on_leave(e):
            foodp['background'] = 'SystemButtonFace'
        foodp = tk.Button(self, text="Πρόγραμμα φαγητού", font=helv36,background='white',
                            command=lambda: controller.show_frame("Geuma"))
        foodp.pack(fill='both')
        foodp.bind("<Enter>", on_enter)
        foodp.bind("<Leave>", on_leave)

        label = tk.Label(self, text="Δραστηριότητες", font=controller.title_font, background='white',
                         image=self.man, compound="left")
        label.pack(side="top", fill="x", pady=10)

        def on_enter(e):
            gym['background'] = 'red'

        def on_leave(e):
            gym['background'] = 'SystemButtonFace'

        gym = tk.Button(self, text="Γυμναστική", font = helv36,background='white',
                                    command=lambda: controller.show_frame("SomatikiAsk"))
        gym.pack(fill='both')
        gym.bind("<Enter>", on_enter)
        gym.bind("<Leave>", on_leave)
        def on_enter(e):
            hob['background'] = 'red'

        def on_leave(e):
            hob['background'] = 'SystemButtonFace'
        hob = tk.Button(self, text="Χόμπι", font=helv36,background='white',
                                command=lambda: controller.show_frame("Xompi"))
        hob.pack(fill='both')
        hob.bind("<Enter>", on_enter)
        hob.bind("<Leave>", on_leave)
        def on_enter(e):
            other['background'] = 'red'

        def on_leave(e):
            other['background'] = 'SystemButtonFace'
        other = tk.Button(self, text="Διάφορες", font=helv36,background='white',
                            command=lambda: controller.show_frame("Diafora"))
        other.pack(fill='both')
        other.bind("<Enter>", on_enter)
        other.bind("<Leave>", on_leave)
        settings = tk.Button(self, image=self.gear, command=lambda: controller.show_frame("Ruthmiseis"))
        settings.pack(side="bottom", anchor = "se", pady=15, padx=15)
#ακολουθουν ολες οι σελιδες των αντιστοιχων use case. Βρειτε ποιες σας αντιστοιχουν
#και δουλεψτε μεσα σε αυτες τις κλασεις
#τα ονοματα των κλασεων ειναι παρομοια με αυτα των κλασεων στο domain model για αποφυγη παρεξηγησεων

class IatrikaRantevou(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Επιλέξτε μήνα: ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mhnas = ["Ιανουάριος", "Φεβρουάριος", "Μάρτιος", "Απρίλιος", "Μάϊος", "Ιούνιος", "Ιούλιος", "Αύγουστος",
                 "Σεπτέμβριος", "Οκτώμβριος", "Νοέμβριος", "Δεκέμβριος"]
        global mhn
        mhn = StringVar(self)
        mhn.set(mhnas[0])
        w = OptionMenu(self, mhn, *mhnas)
        w.pack()

        label = tk.Label(self, text="Επιλέξτε ημέρα: ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        meres = list(range(1, 32))
        global mera
        mera = IntVar(self)
        mera.set(meres[0])
        w = OptionMenu(self, mera, *meres)
        w.pack()
        button = tk.Button(self, text="Next",
                            command=lambda: controller.show_frame("Epiloges"))
        button.pack()
        backb = tk.Button(self, text='Πίσω', command=lambda: controller.show_frame("Menu"))
        backb.pack(side="bottom", anchor="se", pady=15, padx=15)

class Epiloges(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label2 = tk.Label(self, text="Επιλέξτε ώρα: ", font=controller.title_font)
        label2.pack(fill="x", pady=10)

        ora = [
            "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00",
            "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "00:00"
        ]

        global timee
        timee = StringVar(self)
        timee.set(ora[0])  # default value
        w = OptionMenu(self, timee, *ora)
        w.pack()

        label3 = tk.Label(self, text="Τίτλος Ιατρικού Ραντεβού: ", font=controller.title_font).place(x=10, y=150)
        rantevou = StringVar(self, value='Τίτλος')
        E1 = Entry(self, textvariable=rantevou).place(x=10, y=200)


        label4 = tk.Label(self, text="Σημειώσεις: ", font=controller.title_font).place(x=10, y=250)
        shmeiwseis = StringVar(self, value='Σημείωση')
        E2 = Entry(self, textvariable=shmeiwseis).place(x=10, y=300)

        label5 = tk.Label(self, text="Ειδοποιήσεις: ", font=controller.title_font).place(x=10, y=350)

        eidop = [
            "1 ημέρα πριν", "6 ώρες πριν", "3 ώρες πριν", "1 ώρες πριν", "Ποτέ"
        ]
        eidopp = StringVar(self)
        eidopp.set(ora[0])  # default value
        w = OptionMenu(self, eidopp, *eidop).place(x=10, y=400)
        backb = tk.Button(self, text='Πίσω', command=lambda: controller.show_frame("IatrikaRantevou"))
        backb.pack(side="bottom", anchor="se", pady=15, padx=15)

        a=[]
        self.count = 0

        def confirmation():

            if self.count>0:

                for i in range(0, len(a), 6):
                    if mhn.get()==a[i] and mera.get()==a[i+1]:
                        if timee.get()== a[i+3]:
                            messagebox.showerror('Σφάλμα!', 'Η ώρα χρησιμοποιείται ήδη.')

                        else:
                            a.append(mhn.get())
                            a.append(mera.get())
                            a.append(rantevou.get())
                            a.append(timee.get())
                            a.append(eidopp.get())
                            a.append(shmeiwseis.get())
                            self.count += 1
            elif self.count==0:
                a.append(mhn.get())
                a.append(mera.get())
                a.append(rantevou.get())
                a.append(timee.get())
                a.append(eidopp.get())
                a.append(shmeiwseis.get())
                self.count += 1

        finalbutton = tk.Button(self, text='Αποθήκευση Καταχώρησης', command=lambda: confirmation()).place(x=250,
                                                                                                           y=300)



        def diagrafh():
            if self.count > 0:
                for x in range(0, len(a), 6):
                    print(int(x/5),'.',a[x], a[x + 1], a[x + 2], a[x + 3], a[x + 4], a[x + 5])
                d = input('Πληκτρολογίστε τον αριθμό της καταχώρησης που θα θέλατε να διαγράψετε: ')

                d = int(d)*6
                del a[d]
                del a[d]
                del a[d]
                del a[d]
                del a[d]
                del a[d]
                for x in range(0, len(a), 6):
                    print(int(x/5),'.',a[x], a[x + 1], a[x + 2], a[x + 3], a[x + 4], a[x + 5])
            else:
                messagebox.showinfo('oups', 'Δεν υπάρχουν καταχωρήσεις.')
        deleting = Button(self, text="Διαγραφή υπάρχουσας καταχώρησης", command=diagrafh).place(x=250, y=350)

        def uparxouses():
            for x in range(0, len(a), 6):
                print(a[x], a[x + 1], a[x + 2], a[x + 3], a[x + 4], a[x + 5])

        katButton = tk.Button(self, text='Καταχωρήσεις', command=lambda: uparxouses()).place(x=250, y=400)


class Farmako(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Φαρμακευτική Αγωγή", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        backb = tk.Button(self, text='Πίσω', command=lambda: controller.show_frame("Menu"))
        backb.pack(side="bottom", anchor="se", pady=15, padx=15)

        label2 = tk.Label(self, text="Επιλέξτε ώρα: ", font=controller.title_font)
        label2.pack(fill="x", pady=5)

        ora = [
            "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00",
            "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "00:00"
        ]

        global timee
        timee = StringVar(self)
        timee.set(ora[0])  # default value
        w = OptionMenu(self, timee, *ora)
        w.pack()

        label = tk.Label(self, text="Επιλέξτε μονάδα: ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        monada = ["Χάπι", "Σιρόπι", "Γραμμάρια", "Αμπούλα", "Εισπνεόμενο"]
        global mon
        mon = StringVar(self)
        mon.set(monada[0])
        w = OptionMenu(self, mon, *monada)
        w.pack()

        label1 = tk.Label(self, text="Συμπληρώστε ένα όνομα για το φάρμακο: ", font=controller.title_font).place(x=10, y=200)
        global name
        name = StringVar(self, value='Όνομα')
        E1 = Entry(self, textvariable=name).place(x=10, y=250)

        label2 = tk.Label(self, text="Συμπληρώστε την διαθέσιμη ποσότητα: ", font=controller.title_font).place(x=10, y=300)
        global posothta
        posothta = IntVar(self, value=0)
        E2 = Entry(self, textvariable=posothta).place(x=10, y=350)

        label1 = tk.Label(self, text="Ορίστε τη δοσολογία: ", font=controller.title_font).place(x=10, y=400)
        global dosologia
        dosologia = IntVar(self, value=0)
        E1 = Entry(self, textvariable=dosologia).place(x=10, y=450)



        def mnm():
                    global MsgBox
                    MsgBox = tk.messagebox.askquestion('Επισήμανση!', 'Θέλετε να επιλέξετε συγκεκριμένες ημέρες;')
                    if MsgBox == 'yes':
                        controller.show_frame("Message")
                    else:
                        showinfo("Ok!",
                                 "Ειδοποιήσεις για την συγκεκριμένη αγωγή θα έρχονται καθημερινά.")

        neeext = Button(self, text='Eπόμενο', command=lambda: mnm()).place(x=200, y=500)


class Message(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        label = tk.Label(self, text="Eπιλέξτε ημέρες:", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        #μια μεταβλητη για την καθε μερα
        var1 = IntVar()
        Checkbutton(self, text="Δευτέρα", variable=var1).pack()
        var2 = IntVar()
        Checkbutton(self, text="Τρίτη", variable=var2).pack()
        var3 = IntVar()
        Checkbutton(self, text="Τετάρτη", variable=var3).pack()
        var4 = IntVar()
        Checkbutton(self, text="Πέμπτη", variable=var4).pack()
        var5 = IntVar()
        Checkbutton(self, text="Παρασκευή", variable=var5).pack()
        var6 = IntVar()
        Checkbutton(self, text="Σάββατο", variable=var6).pack()
        var7 = IntVar()
        Checkbutton(self, text="Κυριακή", variable=var7).pack()

        chosen_days = []
        def var_states(chosen_days):
            if var1.get() == 1:
                chosen_days.append("Δευτέρα")
            if var2.get() == 1:
                chosen_days.append("Τρίτη")
            if var3.get() == 1:
                chosen_days.append("Τετάρτη")
            if var4.get() == 1:
                chosen_days.append("Πέμπτη")
            if var5.get() == 1:
                chosen_days.append("Παρασκευή")
            if var6.get() == 1:
                chosen_days.append("Σάββατο")
            if var7.get() == 1:
                chosen_days.append("Κυριακή")
            #for x in range(len(chosen_days)):
            return(chosen_days)


        button1 = tk.Button(self, text="Επόμενο",
                        command=lambda: controller.show_frame("Eidopoihsh"))
        button1.pack()


class Eidopoihsh(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label2 = tk.Label(self, text="Ειδοποιήσεις: ", font=controller.title_font).place(x=10, y=100)

        epiloges_eid = [
            "Στην αρχή κάθε επιλεγμένης μέρας", "1 ώρα πριν", "2 ώρες πριν", "3 ώρες πριν", "Ποτέ"
        ]

        eidop = StringVar(self)
        eidop.set(epiloges_eid[0])  # default value

        om = OptionMenu(self, eidop, *epiloges_eid).place(x=10, y=150)
        self.flag = 0
        b = []
        def confirmation():
            b.append(name.get())
            b.append(timee.get())
            b.append(mon.get())
            b.append(posothta.get())
            b.append(dosologia.get())
            b.append(eidop.get())
            self.flag += 1



        def kataxvrhsh():
            if self.flag>0:
                for x in range(0, len(b), 6):
                    print(b[x], b[x + 1], b[x + 2], b[x + 3], b[x + 4], b[x + 5])
            elif self.flag==0:
                messagebox.showinfo('oups', 'Δεν υπάρχουν καταχωρήσεις.')




        finalbutton = tk.Button(self, text='Αποθήκευση Καταχώρησης', command=confirmation).place(x=160, y=260)
        finalkat = tk.Button(self, text='Καταχώρηση', command=kataxvrhsh).place(x=160, y=310)

        def diagrafh():

            for x in range(0, len(b), 6):
                print(int(x / 5), '.', b[x], b[x + 1], b[x + 2], b[x + 3], b[x + 4], b[x + 5])
            d = input('Πληκτρολογίστε τον αριθμό της καταχώρησης που θα θέλατε να διαγράψετε: ')

            d = int(d) * 6
            del b[d]
            del b[d]
            del b[d]
            del b[d]
            del b[d]
            del b[d]
            for x in range(0, len(b), 6):
                print(int(x / 5), '.', b[x], b[x + 1], b[x + 2], b[x + 3], b[x + 4], b[x + 5])


        deleting = Button(self, text="Διαγραφή υπάρχουσας καταχώρησης", command=diagrafh).place(x=160, y=360)

        backb = tk.Button(self, text='Πίσω', command=lambda: controller.show_frame("Farmako"))
        backb.pack(side="bottom", anchor="se", pady=15, padx=15)

class Notes(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Εισάγετε μια σημείωση", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        note_catalog = []
        simeiwseis = StringVar()
        E1 = Entry(self, textvariable=simeiwseis).place(x=20, y=50)

        def submission():
            temp = simeiwseis.get()
            showinfo("Ok!", "Σημείωση καταχωρήθηκε.")
            note_catalog.append(temp)

        submit = Button(self, text='+', command=lambda: submission()).place(x=150, y=48)
        def show_it():
            for x in range(len(note_catalog)):
                print("Σημειωση", x,':', note_catalog[x], '\n')
        show = Button(self, text='Εμφάνιση σημειώσεων', command=lambda: show_it()).place(x=340, y=80)
        backb = tk.Button(self, text='Πίσω', command=lambda: controller.show_frame("Menu"))
        backb.pack(side="bottom", anchor="se", pady=15, padx=15)
class Thermides(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Πληροφορίες του χρήστη
        label = tk.Label(self, text="Εισάγετε τα στοιχεία σας", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        label1 = tk.Label(self, text="Γένος:", font=controller.title_font).place(x=30, y=50)

        genos = StringVar()
        E2 = Entry(self, textvariable=genos).place(x=110, y=60)

        label2 = tk.Label(self, text="'Υψος:", font=controller.title_font).place(x=30, y=80)
        ypsos = IntVar()
        E3 = Entry(self, textvariable=ypsos).place(x=110, y=90)

        label3 = tk.Label(self, text="Βάρος:", font=controller.title_font).place(x=20, y=110)
        varos = IntVar()
        E4 = Entry(self, textvariable=varos).place(x=110, y=120)

        label3 = tk.Label(self, text="Στόχος:", font=controller.title_font).place(x=20, y=150)


        stoxos = [
            "Απώλεια Βάρους",
            "Διατήρηση Βάρους",
            "Αύξηση Βάρους"
        ]

        st = StringVar(self)
        st.set(stoxos[0])  # default value

        w = OptionMenu(self, st, *stoxos).place(x=110, y=160)

        def meals():
            txt ='''        Μία φέτα ψωμί έχει 80 θερμίδες.
        Μία φέτα ψωμί ολικής αλέσεως έχει 31 θερμίδες.
        Ένα μήλο έχει 133 θερμίδες.
        Ένα πορτοκάλι έχει 70 θερμίδες.
        Μία μπανάνα έχει 120 θερμίδες.
        Ένα κοτόπουλο βραστό έχει 300 θερμίδες.
        Μία μερίδα μακαρόνια νερόβραστα έχει 333 θερμίδες.
        Μία τσιπούρα ψητή των 100gr έχει 118 θερμίδες.
        Τα δημητριακά ολικής άλεσης (40gr) έχουν 110 θερμίδες.
        '''

            showinfo("Προτεινόμενα γεύματα", txt)
            controller.show_frame("MetritisThermidon")
        next = tk.Button(self, text='Επόμενο', command=lambda:meals()).place(x=150, y=200)
        backb = tk.Button(self, text='Πίσω', command=lambda: controller.show_frame("Menu"))
        backb.pack(side="bottom", anchor="se", pady=15, padx=15)

class MetritisThermidon(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Ημερολόγιο", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        label2 = tk.Label(self, text="Επιλέξτε ημέρα: ", font=controller.title_font).place(x=30, y=50)

        imera = [
            "Δευτέρα",
            "Τρίτη",
            "Τετάρτη",
            "Πέμπτη",
            "Παρασκευή",
            "Σάββατο",
            "Κυριακή"
            ]

        mera = StringVar(self)
        mera.set(imera[0])  # default value

        w = OptionMenu(self, mera, *imera).place(x=230, y=60)

        label2 = tk.Label(self, text="Όριο θερμίδων: ", font=controller.title_font).place(x=30, y=80)
        orio = IntVar()
        E1 = Entry(self, textvariable=orio).place(x=220, y=90)

        label3 = tk.Label(self, text="Θερμίδες γεύματος: ", font=controller.title_font).place(x=30, y=120)
        therm = IntVar()
        E2 = Entry(self, textvariable=therm).place(x=260, y=130)

        self.sunolo_thermidon = 0

        def elegxos_therm():
           orio_thermidon=orio.get()
           thermides_geumatos=therm.get()
           self.sunolo_thermidon=self.sunolo_thermidon+thermides_geumatos
           ypol=orio_thermidon-self.sunolo_thermidon
           a="Σας έχουν απομείνει "
           b=" θερμίδες για να συμπληρώσετε το όριο"
           c= a + str(ypol) + b
           if self.sunolo_thermidon>orio_thermidon:
            showinfo("Μήνυμα", "Έχετε ξεπεράσει το όριο θερμίδων")
           elif self.sunolo_thermidon<orio_thermidon:
            showinfo("Μήνυμα", c)
           else:
               showinfo("Μήνυμα","Συγχαρητήρια, πετύχατε το στόχο σας")

        bb = tk.Button(self, text='+', command=lambda:elegxos_therm()).place(x=220, y=170)

        backb = tk.Button(self, text='Πίσω', command=lambda: controller.show_frame("Menu"))
        backb.pack(side="bottom", anchor="se", pady=15, padx=15)

class PosotitaNerou(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #Πόσα ποτήρια θέλει να καταναλώσει
        label = tk.Label(self, text="Στόχος ποτηριών νερού/ημέρα", font=controller.title_font).place(x=10, y=50)
        potiria = IntVar()
        E1 = Entry(self, textvariable=potiria).place(x=10, y=90)


        #Ειδοποιήσεις
        label2 = tk.Label(self, text="Ειδοποιήσεις: ", font=controller.title_font).place(x=10, y=120)


        eidop = [
            "Κάθε 1 ώρα", "Κάθε 2 ώρες", "Κάθε 3 ώρες"
        ]

        ora = [
            "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00",
            "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "00:00"
        ]

        eidopp = StringVar(self)
        eidopp.set(ora[0])  # default value

        w = OptionMenu(self, eidopp, *eidop).place(x=180, y=130)


        backb = tk.Button(self, text='Πίσω', command=lambda: controller.show_frame("Menu"))
        backb.pack(side="bottom", anchor="se", pady=15, padx=15)

        self.potiria2 = 0


        def checkk():
            self.potiria2 = self.potiria2 + 1
            showinfo("Μήνυμα", "Συγχαρητήρια, καταναλώσατε ένα ποτήρι νερό")
            elegxos_potirion()

        def denyy():
            showinfo("Μήνυμα", "Δεν καταναλώσατε ένα ποτήρι νερό")
            elegxos_potirion()

        label3 = tk.Label(self, text="Κατανάλωση ποτηριού:", font=controller.title_font).place(x=10, y=170)
        check = tk.Button(self, text='✔', command=checkk).place(x=310, y=175)
        deny = tk.Button(self, text='✘', command=denyy).place(x=340, y=175)

        def elegxos_potirion():
            stoxos_potirion = potiria.get()
            ypol2 = stoxos_potirion - self.potiria2
            a = "Σας έχουν απομείνει "
            b = " ποτήρια για να συμπληρώσετε το όριο"
            c = a + str(ypol2) + b
            if self.potiria2 > stoxos_potirion:
                showinfo("Μήνυμα", "Έχετε ξεπεράσει το όριο των ποτηριών νερού")
            elif self.potiria2 < stoxos_potirion:
                showinfo("Μήνυμα", c)
            else:
                showinfo("Μήνυμα", "Συγχαρητήρια, πετύχατε το στόχο σας")




class Geuma(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Επιλέξτε ημέρα: ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)



        imera = [
            "Δευτέρα",
            "Τρίτη",
            "Τετάρτη",
            "Πέμπτη",
            "Παρασκευή",
            "Σάββατο",
            "Κυριακή"
        ]

        mera = StringVar(self)
        mera.set(imera[0])  # default value

        w = OptionMenu(self, mera, *imera)
        w.pack()

        label2 = tk.Label(self, text="Επιλέξτε ώρα: ", font=controller.title_font)
        label2.pack(fill="x", pady=10)

        ora = [
            "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00",
            "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "00:00"
        ]

        timee = StringVar(self)
        timee.set(ora[0])  # default value

        w = OptionMenu(self, timee, *ora)
        w.pack()

        label3 = tk.Label(self, text="Τίτλος γεύματος: ", font=controller.title_font).place(x=10, y=200)

        fai=StringVar()

        E1 = Entry(self, textvariable=fai).place(x=210, y=210)


        deutera=[]
        triti=[]
        tetarti=[]
        pempti=[]
        paraskeui=[]
        savvato=[]
        kuriaki=[]

        def do_it():
            #print(str(mera.get())+ " \n" + str(timee.get()) + " " + str(fai.get()) )


            if mera.get() == imera[0]:
                deutera.append(timee.get())
                if fai.get()=='':
                    deutera.append('<Χωρίς τίτλο>')
                else:
                    deutera.append(fai.get())
            if mera.get() == imera[1]:
                triti.append(timee.get())
                if fai.get()=='':
                    triti.append('<Χωρίς τίτλο>')
                else:
                    triti.append(fai.get())
            if mera.get() == imera[2]:
                tetarti.append(timee.get())
                if fai.get()=='':
                    tetarti.append('<Χωρίς τίτλο>')
                else:
                    tetarti.append(fai.get())
            if mera.get() == imera[3]:
                pempti.append(timee.get())
                if fai.get()=='':
                    pempti.append('<Χωρίς τίτλο>')
                else:
                    pempti.append(fai.get())
            if mera.get() == imera[4]:
                paraskeui.append(timee.get())
                if fai.get()=='':
                    paraskeui.append('<Χωρίς τίτλο>')
                else:
                    paraskeui.append(fai.get())
            if mera.get() == imera[5]:
                savvato.append(timee.get())
                if fai.get()=='':
                    savvato.append('<Χωρίς τίτλο>')
                else:
                    savvato.append(fai.get())
            if mera.get() == imera[6]:
                kuriaki.append(timee.get())
                if fai.get()=='':
                    kuriaki.append('<Χωρίς τίτλο>')
                else:
                    kuriaki.append(fai.get())
            messagebox.showinfo("Μήνυμα", "Συγχαρητήρια, προσθέσατε μία καταχώρηση!\nΠατήστε οκ για να συνεχίσετε.")

        plus = Button(self, text='+', command=do_it).place(x=315, y=208)

        label3 = tk.Label(self, text="Ειδοποιήσεις: ", font=controller.title_font).place(x=45, y=300)


        eidop = [
            "1 ώρα πριν", "3 ώρες πριν", "Ποτέ"
        ]

        eidopp = StringVar(self)
        eidopp.set(ora[0])  # default value

        w = OptionMenu(self, eidopp, *eidop).place(x=210, y=310)

        def save_it():
            print("Δευτέρα: ")
            for x in range(0, len(deutera), 2):
                print("\t", deutera[x], deutera[x+1])
            print("\nΤρίτη: ")
            for x in range(0, len(triti), 2):
                print("\t", triti[x], triti[x+1])
            print("\nΤετάρτη: ")
            for x in range(0, len(tetarti), 2):
                print("\t", tetarti[x], tetarti[x+1])
            print("\nΠέμπτη: ")
            for x in range(0, len(pempti), 2):
                print("\t", pempti[x], pempti[x+1])
            print("\nΠαρασκευή: ")
            for x in range(0, len(paraskeui), 2):
                print("\t", paraskeui[x], paraskeui[x+1])
            print("\nΣάββατο: ")
            for x in range(0, len(savvato), 2):
                print("\t", savvato[x], savvato[x+1])
            print("\nΚυριακή: ")
            for x in range(0, len(kuriaki), 2):
                print("\t", kuriaki[x], kuriaki[x+1])

        save = Button(self, text='Αποθήκευση', command=save_it).place(x=215, y=458)

        def delete_it():

            print(mera.get())
            if mera.get() == imera[0]:
                for x in range(0, len(deutera), 2):
                    print(int(x/2),".", deutera[x], deutera[x+1])
                toDel = input("Πληκτρολογίστε το νούμερο της καταχώρησης που θα θέλατε να διαγράψετε: ")
                toDel = 2*int(toDel)

                del deutera[toDel]
                del deutera[toDel]
                for x in range(0, len(deutera), 2):
                    print(int(x/2),".", deutera[x], deutera[x+1])
            if mera.get() == imera[1]:
                for x in range(0, len(triti), 2):
                    print(int(x/2), ".", triti[x], triti[x+1])
                toDel = input("Πληκτρολογίστε το νούμερο της καταχώρησης που θα θέλατε να διαγράψετε: ")
                toDel = 2 * int(toDel)

                del triti[toDel]
                del triti[toDel]
                for x in range(0, len(triti), 2):
                    print(int(x / 2), ".", triti[x], triti[x + 1])
            if mera.get() == imera[2]:
                for x in range(0, len(tetarti), 2):
                    print(int(x/2), ".", tetarti[x], tetarti[x+1])
                toDel = input("Πληκτρολογίστε το νούμερο της καταχώρησης που θα θέλατε να διαγράψετε: ")
                toDel = 2 * int(toDel)

                del tetarti[toDel]
                del tetarti[toDel]
                for x in range(0, len(tetarti), 2):
                    print(int(x / 2), ".", tetarti[x], tetarti[x + 1])
            if mera.get() == imera[3]:
                for x in range(0, len(pempti), 2):
                    print(int(x/2), ".", pempti[x], pempti[x+1])
                toDel = input("Πληκτρολογίστε το νούμερο της καταχώρησης που θα θέλατε να διαγράψετε: ")
                toDel = 2 * int(toDel)

                del pempti[toDel]
                del pempti[toDel]
                for x in range(0, len(pempti), 2):
                    print(int(x / 2), ".", pempti[x], pempti[x + 1])
            if mera.get() == imera[4]:
                for x in range(0, len(paraskeui), 2):
                    print(int(x/2), ".", paraskeui[x], paraskeui[x+1])
                toDel = input("Πληκτρολογίστε το νούμερο της καταχώρησης που θα θέλατε να διαγράψετε: ")
                toDel = 2 * int(toDel)

                del paraskeui[toDel]
                del paraskeui[toDel]
                for x in range(0, len(paraskeui), 2):
                    print(int(x / 2), ".", paraskeui[x], paraskeui[x + 1])
            if mera.get() == imera[5]:
                for x in range(0, len(savvato), 2):
                    print(int(x/2), ".", savvato[x], savvato[x+1])
                toDel = input("Πληκτρολογίστε το νούμερο της καταχώρησης που θα θέλατε να διαγράψετε: ")
                toDel = 2 * int(toDel)

                del savvato[toDel]
                del savvato[toDel]
                for x in range(0, len(savvato), 2):
                    print(int(x / 2), ".", savvato[x], savvato[x + 1])
            if mera.get() == imera[6]:
                for x in range(0, len(kuriaki), 2):
                    print(int(x/2),".", kuriaki[x], kuriaki[x+1])
                toDel = input("Πληκτρολογίστε το νούμερο της καταχώρησης που θα θέλατε να διαγράψετε: ")
                toDel = 2 * int(toDel)

                del kuriaki[toDel]
                del kuriaki[toDel]
                for x in range(0, len(kuriaki), 2):
                    print(int(x / 2), ".", kuriaki[x], kuriaki[x + 1])


        delete = Button(self, text='Διαγραφή', command=delete_it).place(x=215, y=558)

        backb = tk.Button(self, text='Πίσω', command=lambda: controller.show_frame("Menu"))
        backb.pack(side="bottom", anchor="se", pady=15, padx=15)


class SomatikiAsk(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.flager = "false"  # true= οι κανονες εγκυροτητας ισχυουν
        label1 = tk.Label(self, text="Τίτλος σωματικής άσκησης: ", font=controller.title_font).place(x=10, y=10)
        global titlos
        titlos = StringVar()
        title_holder = Entry(self, textvariable=titlos).place(x=340, y=20)
        label2 = tk.Label(self, text="Διάρκεια(σε ώρες): ", font=controller.title_font).place(x=10, y=60)
        global dur
        dur = StringVar()
        dur_holder = Entry(self, textvariable=dur).place(x=240, y=70)
        label3 = tk.Label(self, text="Πλήθος ημερών: ", font=controller.title_font).place(x=10, y=100)
        global mera_count
        mera_count = StringVar()
        mera_holder = Entry(self, textvariable=mera_count).place(x=215, y=110)
        global kataxwrisi
        kataxwrisi = []

        def elegxos(kataxwrisi):
            temp1 = int(str(eval(dur.get())))  # elegxos egkirotitas wrwn
            temp2 = int(str(eval(mera_count.get())))  # elegxos egkirotitas hmerwn ana vdomada
            if temp1 > 24 or temp1 <= 0:
                showinfo("Error", "Λάθος Στοιχεία στο πεδίο Διάρκεια(σε ώρες). Επιτρεπτά Δεδομένα 0-24")

            else:
                if temp2 > 7 or temp2 < 1:
                    showinfo("Error", "Λάθος Στοιχεία στο πεδίο Πλήθος ημερών. Επιτρεπτά Δεδομένα 0-7")
                else:
                    self.flager = "true"
            if self.flager == "true":
                global MsgBox
                MsgBox = tk.messagebox.askquestion('Επισήμανση!', 'Θέλετε να επιλέξετε συγκεκριμένες ημέρες;')
                if MsgBox == 'yes':
                    kataxwrisi.append(titlos.get())
                    kataxwrisi.append(dur.get())
                    kataxwrisi.append(mera_count.get())
                    controller.show_frame("NotConf")
                else:
                    kataxwrisi.append(titlos.get())
                    kataxwrisi.append(dur.get())
                    kataxwrisi.append(mera_count.get())
                    showinfo("Ok!",
                             "Ειδοποιήσεις για την συγκεκριμένη δραστηριότητα θα έρχονται στην αρχή κάθε βδόμαδας.")

        neeext = Button(self, text='Eπόμενο', command=lambda: elegxos(kataxwrisi)).place(x=200, y=160)
        def diagrafi_kataxwrisis(kataxwrisi):
            toDel = input("Πληκτρολογίστε τον τίτλο της καταχώρησης την οποία θα θέλατε να διαγράψετε: ")
            flag = 0  # Οριζει αν βρεθηκε καταχωρηση με το ονομα που δωθηκε
            for x in range(len(kataxwrisi)):
                if toDel == kataxwrisi[x]:
                    flag = 1
                    del kataxwrisi[x + 2]
                    del kataxwrisi[x + 1]
                    del kataxwrisi[x]
                    showinfo("OK!", "Η διαγραφή της καταχώρησης ήταν επιτυχής.")
                    return

                x = +2
            if flag == 0:
                showinfo("Error", "Δεν βρέθηκε καταχώρηση με αυτό το όνομα. \n \tΔοκιμάστε ξανά.")

        deleting = Button(self, text="Διαγραφή υπάρχουσας καταχώρησης", command=lambda : diagrafi_kataxwrisis(kataxwrisi)).place(x=120, y=220)
        backb = tk.Button(self, text='Πίσω', command=lambda: controller.show_frame("Menu"))
        backb.pack(side="bottom", anchor="se", pady=15, padx=15)

class NotConf(tk.Frame) :

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        self.controller = controller
        label = tk.Label(self, text="Eπιλέξτε ημέρες:", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        #μια μεταβλητη για την καθε μερα
        var1 = IntVar()
        Checkbutton(self, text="Δευτέρα", variable=var1).pack()
        var2 = IntVar()
        Checkbutton(self, text="Τρίτη", variable=var2).pack()
        var3 = IntVar()
        Checkbutton(self, text="Τετάρτη", variable=var3).pack()
        var4 = IntVar()
        Checkbutton(self, text="Πέμπτη", variable=var4).pack()
        var5 = IntVar()
        Checkbutton(self, text="Παρασκευή", variable=var5).pack()
        var6 = IntVar()
        Checkbutton(self, text="Σάββατο", variable=var6).pack()
        var7 = IntVar()
        Checkbutton(self, text="Κυριακή", variable=var7).pack()
        chosen_days = []
        def var_states(chosen_days):
            if var1.get() == 1:
                chosen_days.append("Δευτέρα")
            if var2.get() == 1:
                chosen_days.append("Τρίτη")
            if var3.get() == 1:
                chosen_days.append("Τετάρτη")
            if var4.get() == 1:
                chosen_days.append("Πέμπτη")
            if var5.get() == 1:
                chosen_days.append("Παρασκευή")
            if var6.get() == 1:
                chosen_days.append("Σάββατο")
            if var7.get() == 1:
                chosen_days.append("Κυριακή")
            #for x in range(len(chosen_days)):
            return(chosen_days)
        label4 = tk.Label(self, text="Ειδοποιήσεις: ", font=controller.title_font).place(x=45, y=215)

        epiloges_eid = [
            "Στην αρχή κάθε επιλεγμένης μέρας", "Στην αρχή της εβδομάδας", "1 ημέρα πριν", "Ποτέ"
        ]

        eidop = StringVar(self)
        eidop.set(epiloges_eid[0])  # default value

        om = OptionMenu(self, eidop, *epiloges_eid).place(x=210, y=220)

        def confirmation():
            print(" Τίτλος:", titlos.get(),"\n","Διάρκεια(σε ώρες):",dur.get(),"\n",
                  "Πλήθος ημερών:",mera_count.get(),"\n","Συγκεκριμένες μέρες:",MsgBox,"\n",
                  "Ημέρες που επιλέχθηκαν:",var_states(chosen_days),"\n", "Eiδοποιήσεις:",eidop.get())

        finalbutton = tk.Button(self, text='Αποθήκευση Καταχώρησης', command=lambda: confirmation()).place(x=160, y=260)


        backb = tk.Button(self, text='Πίσω', command=lambda: controller.show_frame("SomatikiAsk"))
        backb.pack(side="bottom", anchor="se", pady=15, padx=15)

class Xompi(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label1 = tk.Label(self, text="Επιλέξτε ημέρα: ", font=controller.title_font).place(x=10, y=10)
        imera = [
            "Δευτέρα",
            "Τρίτη",
            "Τετάρτη",
            "Πέμπτη",
            "Παρασκευή",
            "Σάββατο",
            "Κυριακή"
        ]
        mera = StringVar(self)
        mera.set(imera[0])  # default value

        w = OptionMenu(self, mera, *imera).place(x=200, y=15)
        label2 = tk.Label(self, text="Tίτλος Χόμπι: ", font=controller.title_font).place(x=10, y=60)
        titlos = StringVar()
        titlos_holder = Entry(self, textvariable=titlos).place(x=170, y=70)
        label3 = tk.Label(self, text="Ώρα ενασχόλησης: ", font=controller.title_font).place(x=10, y=110)
        ora = [
            "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00",
            "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "00:00"
        ]

        timee = StringVar(self)
        timee.set(ora[0])  # default value
        w = OptionMenu(self, timee, *ora).place(x=240, y=118)
        label4 = tk.Label(self, text="Ειδοποιήσεις: ", font=controller.title_font).place(x=10, y=160)

        epiloges_eid = [
            "1 ώρα πριν", "3 ώρες πριν", "Ποτέ"
        ]

        eidop = StringVar(self)
        eidop.set(epiloges_eid[0])  # default value

        om = OptionMenu(self, eidop, *epiloges_eid).place(x=195, y=165)
        global used_hours
        used_hours = [] #πρωτο στοιχειο ωρα, δευτερο η μερα για την αντιστοιχη ωρα
        global kataxwrisi #4 στοιχεια ανα καταχωρηση, με 1)τιτλος,2)μερα,3)ωρα,4)ειδοποιησεις
        kataxwrisi = []

        def elegxos_kai_apo8ikeusi(used_hours, kataxwrisi):
            for x in range(len(used_hours)):
                if timee.get() == used_hours[x] and mera.get() == used_hours[x+1]:
                    showinfo("error","H ωρα που επιλέξατε για την συγκεκριμένη μέρα χρησιμοποιείται ήδη.\n \tΔοκιμάστε ξανά")
                    return
                x=+1
            used_hours.append(timee.get())
            used_hours.append(mera.get())
            showinfo("OK!", "Καταχώρηση αποθηκεύτηκε.")
            kataxwrisi.append(titlos.get())
            kataxwrisi.append(mera.get())
            kataxwrisi.append(timee.get())
            kataxwrisi.append(eidop.get())
            print(" Τιτλος:",titlos.get(),"\n", "Mέρα:", mera.get(), "\n", "Ώρα:", timee.get(),"\n", "Ειδοποιήσεις:", eidop.get())

        save_b = Button(self, text="Αποθήκευση Καταχώρησης", command=lambda: elegxos_kai_apo8ikeusi(used_hours, kataxwrisi)).place(x=170,y=220)
        def diagrafi_kataxwrisis(kataxwrisi):
            toDel = input("Πληκτρολογίστε τον τίτλο της καταχώρησης την οποία θα θέλατε να διαγράψετε: ")
            flag = 0 #Οριζει αν βρεθηκε καταχωρηση με το ονομα που δωθηκε
            for x in range(len(kataxwrisi)):
                if toDel == kataxwrisi[x]:
                    flag=1
                    del kataxwrisi[x+3]
                    del kataxwrisi[x+2]
                    del kataxwrisi[x+1]
                    del kataxwrisi[x]
                    showinfo("OK!", "Η διαγραφή της καταχώρησης ήταν επιτυχής.")
                    return

                x=+3
            if flag == 0:
                showinfo("Error", "Δεν βρέθηκε καταχώρηση με αυτό το όνομα. \n Δοκιμάστε ξανά.")

        deleting = Button(self, text="Διαγραφή Καταχώρησης", command=lambda: diagrafi_kataxwrisis(kataxwrisi)).place(x=175,y=350)

        backb = tk.Button(self, text='Πίσω', command=lambda: controller.show_frame("Menu"))
        backb.pack(side="bottom", anchor="se", pady=15, padx=15)
class Diafora(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page diafores drasthriothtes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        backb = tk.Button(self, text='Πίσω', command=lambda: controller.show_frame("Menu"))
        backb.pack(side="bottom", anchor="se", pady=15, padx=15)

class Ruthmiseis(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Ρυθμίσεις", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)




        self.gears = tk.PhotoImage(file="gears.png")
        labelg = Label(self, image=self.gears)
        labelg.pack()

        labell = tk.Label(self, text="Γλώσσα/Language", font=controller.title_font).place(x=150, y=180)

        self.uk = tk.PhotoImage(file="uk.png")
        self.gr = tk.PhotoImage(file="gr.png")

        self.glossa = "gr"

        def lang_switch1():
            if self.glossa == "gr":
                self.glossa ="uk"
                messagebox.showinfo('',"Language changed to english.")
            else:
                messagebox.showinfo('', "The language is already set to english.")

        def lang_switch2():
            if self.glossa == "uk":
                self.glossa ="gr"
                messagebox.showinfo('',"Η γλώσσα άλλαγε σε Ελληνικά.")

            else:
                messagebox.showinfo('', "H γλώσσα είναι ήδη ελληνική.")

        luk = tk.Button(self, image=self.uk, command=lang_switch1).place(x=260, y=230)
        lgr = tk.Button(self, image=self.gr, command=lang_switch2).place(x=200, y=230)

        labelS = tk.Label(self, text="Ειδοποιήσεις", font=controller.title_font).place(x=180, y=300)

        snd = [
            "Ήχος",
            "Δόνηση",
            "Αθόρυβο"]

        sound = StringVar(self)
        sound.set(snd[0])  # default value
        w = OptionMenu(self, sound, *snd).place(x=230 ,y=330)

        self.theme = "light_theme"
        def dark():
            if self.theme == "light_theme":
                self.theme = "dark_theme"
                self.configure(background="black")

            else:
                self.theme = "light_theme"
                mycolor = '#%02x%02x%02x' % (240, 240, 237)
                self.configure(bg=mycolor)
        labeldm = tk.Label(self, text="Dark Mode:", font=controller.title_font).place(x=140, y=360)
        dmb = tk.Button(self, text='On/Off', command=dark).place(x=300, y=365)

        labeldm = tk.Label(self, text="Εισαγωγή/εξαγωγή δεδομένων", font=controller.title_font).place(x=80, y=420)

        def imp_em():
            print("imported")
        def exp_em():
            print("exported")

        impb = tk.Button(self, text='Εισαγωγή', command=imp_em).place(x=250, y=460)
        expb = tk.Button(self, text='Εξαγωγή', command=exp_em).place(x=190, y=460)

        backb = tk.Button(self, text='Πίσω', command=lambda: controller.show_frame("Menu"))
        backb.pack(side="bottom", anchor="se", pady=15, padx=15)


class Eidopoihseis(IatrikaRantevou,Farmako,PosotitaNerou,Geuma,Thermides,SomatikiAsk,Xompi):
    def __init__(self):
        #Σε αυτη την κλαση περιεχονται ολες οι λειτουργιες σχετικα με τις ρυθμισεις
        #πχ. Internal Clock, System sound, android sync
        #Λειτουργιες σαν και αυτες δεν μπορουμε να τις υλοποιησουμε, διοτι ειναι αρμοδιοτητα της Android αλλά και του software του εκαστοτε κινητου
        #Θα προσπαθησουμε να τις εξομοιωσουμε μεσα σε αυτη την κλαση
        sound_vol=IntVar() #Η ενταση του ηχου της εκαστοτε ειδοποιησης
        internal_clock = time
        vibration=bool
        id=IntVar() #Καθε ειδοποιηση θα εχει μοναδικο id για την ευκολία εφαρμογής
        lista_eidopoihsewn = [] #Εδω θα μπαινουν ολες οι ειδοποιησεις που θα εχουν επιλεχθει απτον χρηστη
        def notify_me(sound_vol, lista_eidopoihsewn, id):
            if lista_eidopoihsewn[id] == internal_clock:
                sound_vol = 10
                #Το software του κινητου στελνει push notification με συνοδεια ηχου


class Kataxwrhsh(IatrikaRantevou,Farmako,PosotitaNerou,Geuma,Thermides,SomatikiAsk,Xompi):
    def __init__(self):
        lista_kataxwrhsewn = []
        id = IntVar() #Καθε καταχωρηση εχει το δικο της μοναδικο id
        def export():
            # H συναρτηση αυτη θα παιρνει ολα τα στοιχεια απο τις καταχωρησεις και θα δημιουργει ενα csv file
            return file

        def imported(file):
            #H συναρτηση αυτη θα δεχεται ενα csv file το οποιο θα αποκρυπτογραφει και θα ενημερωνει με τις νεες καταχωρησεις
            return lista_kataxwrhsewn


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()