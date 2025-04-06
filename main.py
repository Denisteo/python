import tkinter as tk

def click(event):
    current = str(entry.get())
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

entry = tk.Entry(root, font="Arial 20", borderwidth=3, relief=tk.RIDGE, justify="right")
entry.pack(pady=20, padx=10, fill=tk.X)

button_texts = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

button_frame = tk.Frame(root)
button_frame.pack(padx=10, pady=10)

for row in button_texts:
    button_row = tk.Frame(button_frame)
    button_row.pack(fill=tk.X)
    for char in row:
        button = tk.Button(button_row, text=char, font="Arial 18", height=2, width=5)
        button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        button.bind("<Button-1>", click)

root.mainloop()
