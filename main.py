from tkinter import *

root = Tk()
root.title("Zekat Hesaplayıcı")
root.geometry("1024x724")

def zekathesapla():
    print("zekat hesaplanıyor")
    zekatsiz = float(para.get())
    zekat = zekatsiz / 4
    zekatgoster(zekat)

def zekatgoster(zekat):
    global degisken
    global degisken2
    degisken = Label(root, text="Ödemeniz Gereken Zekat: ")
    degisken.pack()
    degisken2 = Label(root, text=zekat)
    degisken2.pack()

text = Label(root, text="Zekatını Hesaplayacağımız Para Miktarı")
text.pack()

para = Entry(root)
para.pack()

button = Button(root, text="ZEKATI HESAPLA", command=zekathesapla)
button.pack()

root.mainloop()
