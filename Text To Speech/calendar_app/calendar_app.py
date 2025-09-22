import calendar
import tkinter as tk
from tkinter import messagebox

def show_calendar():
    year = year_entry.get()
    if not year.isdigit():
        messagebox.showerror("Invalid Input", "Please enter a valid year (numbers only).")
        return
    
    year = int(year)
    cal_text = calendar.TextCalendar().formatyear(year)

    top = tk.Toplevel(root)
    top.title(f"Calendar for {year}")
    text_widget = tk.Text(top, wrap='none')
    text_widget.insert(tk.END, cal_text)
    text_widget.pack(expand=True, fill='both')

root = tk.Tk()
root.title("Calendar Application")
root.geometry("300x150")
root.configure(bg="white")

label = tk.Label(root, text="Enter Year:", bg="white")
label.pack(pady=10)

year_entry = tk.Entry(root)
year_entry.pack()

show_button = tk.Button(root, text="Show Calendar", command=show_calendar)
show_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack()

root.mainloop()
