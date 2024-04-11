import tkinter as tk

# tkinter package helps in building GUI

window = tk.Tk()
window.title("my title")
window.minsize(width=1320, height=800)

# Label
my_label = tk.Label(text="my label", font=("Arial", 24))
my_label.pack(expand=True)


tk.mainloop()