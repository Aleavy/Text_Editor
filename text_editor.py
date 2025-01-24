import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfile

def save_as_file():
    try:
        content = text_wg.dump(1.0, "end")
        print(content)
        content_formatted = ", ".join(map(str, content))
        files = [("All files", "*"),
                ("Python files", ".py"),
                ("Text files", ".txt")] 
        file = asksaveasfile(filetypes=files, defaultextension=files)
        file.write(content_formatted)
        print(file.name)
    except AttributeError:
        pass

def convert_to_tupple(iterable_list= ['text', 'asdsa', '1.0', 'tagon', 'red', '1.5', 'text', 'dsa', '1.5']):
    list_with_tuples = []
    for item in range(0, len(iterable_list), 3):
        list_with_tuples.append((iterable_list[item], iterable_list[item + 1], iterable_list[item + 2]))
    return list_with_tuples

def adding_lenght(iterable : list, num):
    while len(iterable) % num != 0:
        iterable.append((None, None, None))
    return iterable

def text_parser(list_with_tuples, target):
    try:
        for i in range(0, len(list_with_tuples)):
            key, value, index = list_with_tuples[i][0], list_with_tuples[i][1], list_with_tuples[i][2]
            print(f"Tuple: {key}, {value}, {index}")
            if key == "text":
                if value == "\n":
                    target.insert(index, "")
                else:
                    target.insert(index, value)
            elif key == "tagon":
                text, ind = list_with_tuples[i+1][1], list_with_tuples[i+1][2]
                target.insert(ind, text)
                del list_with_tuples[i+1]
                tag_end = list_with_tuples[i+2][2]
                target.tag_add(f"{value}", index, tag_end)
            elif key == "mark":
                target.mark_set(value, index)
    except IndexError:
        pass


def open_file():
    try:
        files = [("All files", "*"),
            ("Python files", ".py"),
            ("Text files", ".txt")] 
        file = askopenfile(filetypes=files, defaultextension=files)
        text_with_tags = file.read().split(", ")
        text_with_tags_format = [i.replace("(", "").replace(")", "").replace("'", "") for i in text_with_tags]
        final_text = convert_to_tupple(text_with_tags_format)
        text_wg.delete("1.0", "end")
        text_parser(final_text, text_wg)

        
        
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
                print(tag)
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
text_wg = tk.Text(text_frame, border=4, font=("Arial", 20), yscrollcommand=scrollbar.set, undo = True)
scrollbar.config(command=text_wg.yview)
save_btn = tk.Button(tools, text="Save", relief="solid", font=("Arial", 10), command=save_as_file)
open_btn = tk.Button(tools, text="Open", relief="solid", font=("Arial", 10), command=open_file)
header_btn = tk.Button(tools, text="Header", relief="solid", command=increase_font)
body_btn = tk.Button(tools, text="Body", relief="solid", command=decrease_font)

tools.grid_propagate(False)
tools.grid(column=0, row=0, sticky=("NSEW"))

save_btn.grid(column=0, row=0, sticky=("EW"))
open_btn.grid(column=1, row=0, sticky=("EW"))
header_btn.grid(column=0, row=1, columnspan=1, sticky=("NEW"))
body_btn.grid(column=1, row=1, columnspan=1, sticky=("NEW"))

text_frame.grid(column=1, row=0, sticky=("NSEW"))
text_wg.grid(column=0, row=0, sticky=("NSEW"))

scrollbar.grid(column=1, row=0, sticky=("NS"))

text_wg.tag_configure("red", background="red", foreground="white") 
text_wg.tag_configure("blue", background="blue", foreground="white") 
text_wg.tag_configure("yellow", background="yellow", foreground="black") 
font_size = text_wg.config("font")[-1].split(" ")
print(font_size)
text_wg.tag_configure("more", font= (font_size[0], int(font_size[1]) + 10)) 

main_window.bind("<Control-d>", lambda x: main_window.destroy())
main_window.bind("<Control-r>", lambda x: highlight_text("red"))
main_window.bind("<Control-q>", lambda x: highlight_text("yellow"))
main_window.bind("<Control-f>", lambda x: highlight_text("blue"))


main_window.grid_columnconfigure(0, weight=1)
main_window.grid_columnconfigure(1, weight=2)
main_window.grid_rowconfigure(0, weight=1)

tools.grid_columnconfigure(0, weight=1)
tools.grid_columnconfigure(1, weight=1)
tools.grid_rowconfigure(0, weight=0)



text_frame.grid_columnconfigure(0, weight=3)
text_frame.grid_rowconfigure(0, weight=3)


main_window.mainloop()