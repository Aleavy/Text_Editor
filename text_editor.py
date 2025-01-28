import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter import font






def save_as_file():
    try:
        content = text_wg.dump(1.0, "end-1c")
        content_formatted = ", ".join(map(str, content))
        files = [("All files", "*"),
                ("Python files", ".py"),
                ("Text files", ".txt")] 
        file = asksaveasfile(filetypes=files, defaultextension=".txt", initialdir="private")
        for item in content:
            key, value, index = item[0], item[1], item[2]
            if key == "text":
                file.write(value)

        filename = file.name.split(".")
        filename = filename[0].replace("/private", "/private/tags") +"_tags" + ".txt"
        print(filename)
        with open(filename, "w+") as j:
            j.writelines(content_formatted)
    except AttributeError:
        pass


def open_file():
    try:
        files = [("All files", "*"),
            ("Python files", ".py"),
            ("Text files", ".txt")] 
        file = askopenfile(filetypes=files, defaultextension=".txt", initialdir="private")

        filename = file.name.split(".")
        filename = filename[0].replace("/private", "/private/tags") +"_tags" + ".txt"
        print(filename)
        text_wg.delete("1.0", "end")
        text_wg.replace(1.0, "end-1c", file.read())
        with open(filename, "r+") as j:
            content = j.read().replace("),", ")-")
            content = content.split("-")
            content = [eval(item.strip()) for item in content]

            for ind, item in enumerate(content):
                key, value, index = item[0], item[1], item[2]
                if key == "tagon":
                    try:
                        end_tag = content[ind+2][2]                            
                        text_wg.tag_add(value, index, end_tag)
                    except IndexError:
                        text_wg.tag_add(value, index, "end-1c")
    except AttributeError:
        pass

def highlight_text(color:str): 
        
    # if no text is selected then tk.TclError exception occurs 
    try: 
        start, finish = text_wg.index("sel.first"), text_wg.index("sel.last")
        tags = text_wg.tag_names(start)
        if len(tags) > 1:
            if f"{color}" in tags:
                text_wg.tag_remove(f"{color}", start, finish)
                return
            for tag in tags:
                if tag == "sel" or tag == "more":
                    continue
                text_wg.tag_remove(tag, start, finish)
            text_wg.tag_add(f"{color}", "sel.first", "sel.last")      
        else:
            text_wg.tag_add(f"{color}", "sel.first", "sel.last")         
    except tk.TclError: 
        pass


def increase_font():
    try:
        text_wg.tag_add("more", "sel.first", "sel.last")
    except tk.TclError:
        pass


def _bold():
    try:
        text_wg.tag_add("bold", "sel.first", "sel.last")
    except tk.TclError:
        pass

def _bold_remove():
    try:
        text_wg.tag_remove("bold", "sel.first", "sel.last")
    except tk.TclError:
        pass


def decrease_font():
    try:
        text_wg.tag_remove("more", "sel.first", "sel.last")
    except tk.TclError:
        pass

main_window = tk.Tk()
main_window.title("Amazing Text Editor")


tools = tk.Frame(main_window, bg="black", border=4, relief="raised",height=400,  width= 300)
text_frame = tk.Frame(main_window)

scrollbar = tk.Scrollbar(text_frame)

size_font = 20
normal_font = font.Font(main_window ,family="Arial", size=size_font, weight="normal", name="NormalFont")

text_wg = tk.Text(text_frame, border=4, font=normal_font, yscrollcommand=scrollbar.set, undo = True)
scrollbar.config(command=text_wg.yview)
save_btn = tk.Button(tools, text="Save", relief="solid", font=("Arial", 10), command=save_as_file)
open_btn = tk.Button(tools, text="Open", relief="solid", font=("Arial", 10), command=open_file)
header_btn = tk.Button(tools, text="Header", relief="solid", command=increase_font)
body_btn = tk.Button(tools, text="Body", relief="solid", command=decrease_font)
bold_bnt = tk.Button(tools, text="Bold", relief="solid", command=_bold)
rm_bold_bnt = tk.Button(tools, text="Remove Bold", relief="solid", command=_bold_remove)

tools.grid_propagate(False)
tools.grid(column=0, row=0, sticky=("NSEW"))


bold_font = font.Font(text_wg, family="Arial", size=size_font, weight="bold", name="BoldFont")

save_btn.grid(column=0, row=0, sticky=("EW"))
open_btn.grid(column=1, row=0, sticky=("EW"))
header_btn.grid(column=0, row=1, columnspan=1, sticky=("NEW"))
body_btn.grid(column=1, row=1, columnspan=1, sticky=("NEW"))
bold_bnt.grid(column=0, row=3, columnspan=1, sticky=("NEW"))
rm_bold_bnt.grid(column=1, row=3, columnspan=1, sticky=("NEW"))

text_frame.grid(column=1, row=0, sticky=("NSEW"))
text_wg.grid(column=0, row=0, sticky=("NSEW"))

scrollbar.grid(column=1, row=0, sticky=("NS"))

text_wg.tag_configure("red", background="red", foreground="white") 
text_wg.tag_configure("blue", background="blue", foreground="white") 
text_wg.tag_configure("yellow", background="yellow", foreground="black") 
font_size = text_wg.config("font")[-1].split(" ")

text_wg.tag_configure("more", font= (font_size[0], size_font + 10) )
text_wg.tag_configure("bold", font=bold_font) 

main_window.bind("<Control-d>", lambda x: main_window.destroy())
main_window.bind("<Control-r>", lambda x: highlight_text("red"))
main_window.bind("<Control-q>", lambda x: highlight_text("yellow"))
main_window.bind("<Control-f>", lambda x: highlight_text("blue"))
main_window.bind("<Control-s>", lambda x: save_as_file())
main_window.bind("<Control-b>", lambda x: _bold())


main_window.grid_columnconfigure(0, weight=1)
main_window.grid_columnconfigure(1, weight=2)
main_window.grid_rowconfigure(0, weight=1)

tools.grid_columnconfigure(0, weight=1)
tools.grid_columnconfigure(1, weight=1)
tools.grid_rowconfigure(3, weight=0)
tools.grid_rowconfigure(0, weight=0)



text_frame.grid_columnconfigure(0, weight=3)
text_frame.grid_rowconfigure(0, weight=3)


main_window.mainloop()