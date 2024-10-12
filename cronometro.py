import time
import tkinter as tk

def start_timer():
    try:
        total_time = int(entry.get())
        countdown(total_time)
    except ValueError:
        time_display.set("Entrada Inválida")

def countdown(t):
    if t > 0:
        minutes, seconds = divmod(t, 60)
        time_display.set(f"{minutes:02d}:{seconds:02d}")
        root.after(1000, countdown, t - 1)
    else:
        time_display.set("00:00")
        root.destroy()

root = tk.Tk()
root.title("Cronômetro Simples")
root.geometry("250x150")
root.configure(bg="lightgray")

time_display = tk.StringVar()
time_display.set("00:00")

entry = tk.Entry(root, width=10, font=("Helvetica", 14))
entry.pack(pady=10)

button = tk.Button(root, text="Iniciar", command=start_timer, font=("Helvetica", 12), bg="blue", fg="white")
button.pack(pady=5)

timer_label = tk.Label(root, textvariable=time_display, font=("Helvetica", 24), bg="lightgray")
timer_label.pack(pady=10)

root.mainloop()
