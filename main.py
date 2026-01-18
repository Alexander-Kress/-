import tkinter as tk
from emailSender import EmailSenderApp

def main():
    root = tk.Tk()
    EmailSenderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
