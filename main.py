import tkinter as tk
import time

def start():
    global running
    running = True
    start_time = time.time()
    while running:
        elapsed_time = time.time() - start_time
        label.config(text=str(round(elapsed_time, 2)))
        root.update()

def stop():
    global running
    running = False

root = tk.Tk()
root.title("Cronómetro")

label = tk.Label(root, text="0", font=("Arial", 24), width=10)
label.pack(padx=50, pady=50)

start_button = tk.Button(root, text="Start", command=start)
start_button.pack(padx=10, pady=10, side=tk.LEFT)

stop_button = tk.Button(root, text="Stop", command=stop)
stop_button.pack(padx=10, pady=10, side=tk.RIGHT)

root.mainloop()
