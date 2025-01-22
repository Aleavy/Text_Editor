import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfile

def save_as_file():
    content = text_wg.get(1.0, "end-1c")

    files = [("All files", "*"),
            ("Python files", ".py"),
            ("Text files", ".txt")] 
    file = asksaveasfile(filetypes=files, defaultextension=files)
    file.write(content)
    print(file.name)

def open_file():
    files = [("All files", "*"),
        ("Python files", ".py"),
        ("Text files", ".txt")] 
    file = askopenfile(filetypes=files, defaultextension=files)

    text_wg.replace(1.0, "end", file.read())

main_window = tk.Tk()
main_window.title("Amazing Text Editor")


tools = tk.Frame(main_window, bg="black", border=4, relief="raised",height=400,  width= 300)
text_frame = tk.Frame(main_window)

scrollbar = tk.Scrollbar(text_frame)
text_wg = tk.Text(text_frame, border=4, font=("Arial", 20), yscrollcommand=scrollbar.set)
scrollbar.config(command=text_wg.yview)
save_btn = tk.Button(tools, text="Save", relief="solid", font=("Arial", 10), command=save_as_file)
open_btn = tk.Button(tools, text="Open", relief="solid", font=("Arial", 10), command=open_file)


tools.grid_propagate(False)
tools.grid(column=0, row=0, sticky=("NSEW"))

save_btn.grid(column=0, row=0, sticky=("NEW"))
open_btn.grid(column=1, row=0, sticky=("NEW"))

text_frame.grid(column=1, row=0, sticky=("NSEW"))
text_wg.grid(column=0, row=0, sticky=("NSEW"))
scrollbar.grid(column=1, row=0, sticky=("NS"))

main_window.bind("<Control-d>", lambda x: main_window.destroy())


main_window.grid_columnconfigure(0, weight=1)
main_window.grid_columnconfigure(1, weight=2)
main_window.grid_rowconfigure(0, weight=1)

tools.grid_columnconfigure(0, weight=1)
tools.grid_columnconfigure(1, weight=1)
tools.grid_rowconfigure(0, weight=1)

text_frame.grid_columnconfigure(0, weight=3)
text_frame.grid_rowconfigure(0, weight=3)


main_window.mainloop()