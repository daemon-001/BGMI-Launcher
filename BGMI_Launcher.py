
import customtkinter
import subprocess
import threading
import sys
import os


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')
app = customtkinter.CTk()
app.geometry('400x400')
app.title('BGMI Launcher')
app.iconbitmap(resource_path('icon.ico'))
app.resizable(0, 0)
text_1 = customtkinter.CTkTextbox(master=app, width=350, height=180)
switch_var = customtkinter.StringVar(value='off')

def scripts(x):
    y = x
    if y == 11:
        file = 'scripts\\connect_emulator.bat'
    elif y == 12:
        file = 'scripts\\lounch_bgmi.bat'
    elif y == 13:
        file = 'scripts\\reconnect_server.bat'
    elif y == 14:
        file = 'scripts\\clear_logs.bat'
    elif y == 15:
        switch = switch_var.get()
        if switch == 'on':
            file = "scripts\\on.bat"
        if switch == 'off':
            file = "scripts\\off.bat"
    proc = subprocess.Popen(file, stdout=subprocess.PIPE)
    text_1.delete('0.0', 'end')
    while not proc.poll():
        data = proc.stdout.readline()
        if data:
            text_1.insert('end', data)
            text_1.see('end')
            text_1.update_idletasks()
        else:
            break
frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=20, fill='both', expand=False)
frame_1.columnconfigure(0, weight=1)
frame_1.columnconfigure(1, weight=1)
frame_1.rowconfigure(0, weight=1)
frame_1.rowconfigure(1, weight=1)
frame_1.rowconfigure(2, weight=1)
button_0 = customtkinter.CTkButton(master=frame_1, text='Connect Emulator', command=lambda: threading.Thread(target=scripts(11)).start())
button_0.grid(row=0, column=0, padx=10, pady=10)
button_1 = customtkinter.CTkButton(master=frame_1, text='Lounch BGMI', command=lambda: threading.Thread(target=scripts(12)).start())
button_1.grid(row=0, column=1, padx=10, pady=10)
button_2 = customtkinter.CTkButton(master=frame_1, text='Reconnect Server', command=lambda: threading.Thread(target=scripts(13)).start())
button_2.grid(row=1, column=0, padx=10, pady=10)
button_3 = customtkinter.CTkButton(master=frame_1, text='Clear Logs', command=lambda: threading.Thread(target=scripts(14)).start())
button_3.grid(row=1, column=1, padx=10, pady=10)
switch_1 = customtkinter.CTkSwitch(master=app, text='Port Block', command=lambda: threading.Thread(target=scripts(15)).start(), variable=switch_var, onvalue='on', offvalue='off')
switch_1.pack(padx=10, pady=10)
text_1.pack(pady=10, padx=10)

app.mainloop()