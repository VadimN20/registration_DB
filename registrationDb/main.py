from datetime import datetime
import tkinter as tk
from regUser import writeIn, logIn


class Registration(tk.Tk):
    def __init__(self):
        super().__init__()
        self.groupReg = tk.LabelFrame(self, padx=15, pady=10, text='Registration')
        self.groupReg.pack(padx=10, pady=5)

        self.lblLog = tk.Label(self.groupReg, text='Login')
        self.lblLog.grid(row=0, column=0)
        self.lblPas = tk.Label(self.groupReg, text='Password')
        self.lblPas.grid(row=1, column=0)
        self.entryLog = tk.Entry(self.groupReg, bd=1)
        self.entryLog.grid(row=0, column=1, columnspan=5, sticky=tk.W)
        self.entryPas = tk.Entry(self.groupReg, bd=1, show='*')
        self.entryPas.grid(row=1, column=1, columnspan=5, sticky=tk.W)

        self.btnReg = tk.Button(self.groupReg, text='Register', command=self.reg)
        self.btnReg.grid(row=2, column=2, sticky=tk.E)

        self.btnLogIn = tk.Button(self.groupReg, text='Login', command=self.log_in)
        self.btnLogIn.grid(row=2, column=4, sticky=tk.E)

    def reg(self):
        s = self.entryLog.get()
        d = self.entryPas.get()
        regTime = datetime.now()

        self.lblinfo = tk.Label(self.groupReg, text = writeIn(s, d, regTime))
        self.lblinfo.grid(row=3, column=0, columnspan=5)


    def log_in(self):
        l = self.entryLog.get()
        p = self.entryPas.get()
        lastTime = datetime.now()

        self.lblinfo = tk.Label(self.groupReg, text=logIn(l, p, lastTime))
        self.lblinfo.grid(row=3, column=0, columnspan=5)


if __name__ == "__main__":
    registr = Registration()
    registr.geometry('500x300')
    registr.title('Окно регистрации')
    registr.resizable()
    registr.mainloop()
