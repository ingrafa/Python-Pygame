import tkinter as tk
import time
from playsound import playsound

def start_timer():
    global running
    running = True
    start_time = time.time()
    while running:
        elapsed_time = time.time() - start_time
        timer_label.config(text=str(int(elapsed_time)))
        root.update()

def stop_timer():
    global running
    running = False

def set_alarm():
    alarm_time = int(alarm_entry.get())
    time.sleep(alarm_time)
    playsound('alarma.wav')

root = tk.Tk()
root.title('Cronómetro y Alarma')

timer_label = tk.Label(root, text="0", font=("Arial", 24), width=10)
timer_label.pack(padx=50, pady=20)

start_button = tk.Button(root, text="Iniciar Cronómetro", command=start_timer)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Detener Cronómetro", command=stop_timer)
stop_button.pack(pady=10)

alarm_entry_label = tk.Label(root, text="Ingrese el tiempo para la alarma (segundos):")
alarm_entry_label.pack(pady=10)

alarm_entry = tk.Entry(root)
alarm_entry.pack(pady=10)

set_alarm_button = tk.Button(root, text="Configurar Alarma", command=set_alarm)
set_alarm_button.pack(pady=10)

root.mainloop()