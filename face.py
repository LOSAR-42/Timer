from tkinter import *
from tkinter import messagebox
import Math
import os
import subprocess
from sys import platform
import threading
import tkinter as tk
from time import sleep



class Interface(Frame):
    def __init__(self):
        super().__init__()
        self.interface()

    def interface(self):

        def Puk():# Проверят, является ли полученное значение=Int, если нет, то цикл вырубается.
            while True:
                puk_sum = entry.get()  # Получение введенного текста
                try:
                    tmp = int(puk_sum)
                    print('Status: Puk Good Work')
                    return math(tmp)
                except:
                    print('Status: Puk don"t work')
                    messagebox.showinfo('Message', 'Something is Wrong')
                    exit()

        def math(sum): # Перекидывает значение в math.py, где ведется отсчет таймера
            sum_min = (sum * 60) - 60
            Math.countdown(sum_min)
            aloxa_alg_process = threading.Thread(target=Aloxa)
            aloxa_alg_process.start() # Запускаем процесс
            #messagebox.showinfo('Message', 'Aloxa after 60 second (Press "Ok)')  # Выскакивает окно после окончания цикла

        def Aloxa(): # Визуальный таймер обратного отчета.
            aloxa_alg_process = threading.Thread(target=Aloxa_algorithm)
            aloxa_alg_process.start()
            i = 60
            print('Status: Aloxa start process')
            while 0 <= i <= 60:
                lbl_time['text'] -= 1
                sleep(1)
                i = int(lbl_time['text'])
                print(i)
            print("Aloxa_END")


        def Aloxa_algorithm ():
            aloxa_i = 60
            print('Status: Aloxa_algorithm start process')
            while aloxa_i:
                sleep(1)
                aloxa_i -= 1
                print(aloxa_i)
            print('Status: Aloxa_algoritm Good Work')
            chek_os()

        def chek_os (): # Chek OS and clouse ее так сказать.
            if platform == "linux" or platform == "linux2":
                os.system("shutdown now -h")
                print("Status: chek_os - Linux GoodWork")
            elif platform == "darwin":
                subprocess.call(['osascript', '-e','tell app "System Events" to shut down'])
                print("Status: chek_os - MacOS GoodWork")
            elif platform == "win32":
                os.system('shutdown -s')
                print("Status: chek_os - Windows GoodWork")

        time = 60
        lbl_time = tk.Label(text=time)  # Создает надпись для обратного отсчет в def "Aloxa"
        lbl_time.pack(padx=6, pady=6)


        label = Label()
        label.pack(anchor=NW, padx=6, pady=6)

        entry = Entry()
        entry.pack(anchor=NW, padx=6, pady=6)

        display_button = Button(text="Start", command=Puk)
        display_button.pack(side=LEFT, anchor=N, padx=6, pady=6)


def main():
    root = Tk()
    root.geometry("250x200")
    root.resizable(width=False, height=False)
    app = Interface()
    root.mainloop()

if __name__ == '__main__':
    main()