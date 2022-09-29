import tkinter
import tkinter.messagebox

class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("500x300")
        self.main_window.title("Yoooooo")

        self.top_frame = tkinter.Frame(self.main_window)
        self.botton_frame = tkinter.Frame(self.main_window)

        self.HelloLabel = tkinter.Label(self.top_frame, text="Tim")
        self.ByeLabel = tkinter.Label(self.top_frame, text="Jerry")
        self.label3 = tkinter.Label(self.top_frame, text="Billy")

        self.top_frame.pack()
        self.botton_frame.pack()

        self.HelloLabel.pack(side='left')
        self.ByeLabel.pack(side='left')
        self.label3.pack(side='left')
        self.promptLabel = tkinter.Label(self.top_frame, text="Enter kilometer #: ")
        self.promptInput = tkinter.Entry(self.botton_frame, width=10)

        def convert():
            kilo = float(self.promptInput.get())
            miles = kilo * 0.6214
            tkinter.messagebox.showinfo('Result', f'{str(kilo)} to miles = {miles}')

        self.promptLabel.pack()
        self.promptInput.pack()

        def close_application():
            self.main_window.destroy()

        def do_something():
            tkinter.messagebox.showinfo('Response', "Hi")

        self.click_me = tkinter.Button(self.botton_frame, text="Click me", command=convert)
        self.click_me.pack(side='right')

        self.quit_button = tkinter.Button(self.botton_frame, text="Quit", command=close_application)
        self.quit_button.pack(side='left')


        tkinter.mainloop()

my_gui = myGUI()