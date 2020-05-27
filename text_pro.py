import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os
from tkinter.tix import tixCommand

main_app = tk.Tk()
main_app.geometry('1200x650')
main_app.title('text_pro')
# ----------- main menu -----------
main_menu = tk.Menu()
# Icons
new_icon = tk.PhotoImage(file="C:\\Users\\kunal\\Downloads\\text_pro icon\\icons2\\icons2\\new.png")
open_icon = tk.PhotoImage(file="C:\\Users\\kunal\\Downloads\\text_pro icon\\icons2\\icons2\\open.png")
save_icon = tk.PhotoImage(file="C:\\Users\\kunal\\Downloads\\text_pro icon\\icons2\\icons2\\save.png")
save_as_icon = tk.PhotoImage(file="C:\\Users\\kunal\\Downloads\\text_pro icon\\icons2\\icons2\\save_as.png")
exit_icon = tk.PhotoImage(file="C:\\Users\\kunal\\Downloads\\text_pro icon\\icons2\\icons2\\exit.png")

file = tk.Menu(main_menu, tearoff=False)


# -- EDIT ---
edit = tk.Menu(main_menu, tearoff=False)
# ---- Edit ICONS -----
copy_icon = tk.PhotoImage(file="C:\\Users\\kunal\\Downloads\\text_pro icon\\icons2\\icons2\\copy.png")

paste_icon = tk.PhotoImage(file="C:\\Users\\kunal\\Downloads\\text_pro icon\\icons2\\icons2\\paste.png")

cut_icon = tk.PhotoImage(file="C:\\Users\\kunal\\Downloads\\text_pro icon\\icons2\\icons2\\cut.png")

clear_all_icon = tk.PhotoImage(file="C:\\Users\\kunal\\Downloads\\text_pro icon\\icons2\\icons2\\clear_all.png")

find_icon = tk.PhotoImage(file="C:\\Users\\kunal\\Downloads\\text_pro icon\\icons2\\icons2\\find.png")

# --- view ----
view = tk.Menu(main_menu, tearoff=False)
tool_bar_icon = tk.PhotoImage(file="C:\\Users\\kunal\\Downloads\\text_pro icon\\icons2\\icons2\\tool_bar.png")

status_bar_icon = tk.PhotoImage(file="C:\\Users\\kunal\\Downloads\\text_pro icon\\icons2\\icons2\\status_bar.png")


color_theme = tk.Menu(main_menu, tearoff=False)
light_default_icon = tk.PhotoImage(file="C:\\Users\\kunal\\Downloads\\text_pro icon\\icons2\\icons2\\light_default.png")
#color_theme.add_command(label="light default", image=light_default_icon, compound=tk.LEFT)
dark_icon = tk.PhotoImage(file="C:\\Users\\kunal\\Downloads\\text_pro icon\\icons2\\icons2\\dark.png")
#color_theme.add_command(label="Dark", image=dark_icon, compound=tk.LEFT)
light_plus_icon = tk.PhotoImage(file="C:\\Users\\kunal\\Downloads\\text_pro icon\\icons2\\icons2\\light_plus.png")
#color_theme.add_command(label="light plus", image=light_plus_icon, compound=tk.LEFT)
night_blue_icon = tk.PhotoImage(file="C:\\Users\\kunal\\Downloads\\text_pro icon\\icons2\\icons2\\night_blue.png")
#color_theme.add_command(label="Night blue", image=night_blue_icon, compound=tk.LEFT)
red_icon = tk.PhotoImage(file="C:\\Users\\kunal\\Downloads\\text_pro icon\\icons2\\icons2\\red.png")
#color_theme.add_command(label="Red", image=red_icon, compound=tk.LEFT)
monokai_icon = tk.PhotoImage(file="C:\\Users\\kunal\\Downloads\\text_pro icon\\icons2\\icons2\\monokai.png")
#color_theme.add_command(label="Monokia", image=monokai_icon, compound=tk.LEFT)
theme_choice = tk.StringVar()
color_icon = (light_default_icon, light_plus_icon, dark_icon, red_icon,monokai_icon, night_blue_icon)

color_dict = {
    "light default" : ('#000000','#ffffff'),
    "Light plus" : ('#474747','#e0e0e0'),
    "Dark" : ('#c4c4c4', '#2d2d2d'),
    "Red" : ('#2d2d2d', '#ffeBeB'),
    "Monakai" : ('#d3b774','#474747'),
    'Night Blue': ('#ededed','#6b9dc2')
}


# cascade
main_menu.add_cascade(label="File", menu=file)
main_menu.add_cascade(label="Edit", menu=edit)
main_menu.add_cascade(label="View", menu=view)
main_menu.add_cascade(label="Color_theme", menu=color_theme)

# ----------- end menu ------------
# ----------- toolbar -----------
tool_bar = ttk.Label(main_app)
tool_bar.pack(side=tk.TOP, fill=tk.X)
# font box
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30,textvariable=font_family, state="readonly")
font_box["values"] = font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0, column=0,padx=5)
# size box
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=34, textvariable=size_var, state="readonly")
font_size["values"] = tuple(range(6,90,2))
font_size.current(4)
font_size.grid(row=0, column=1,padx=5)
# Bold button
bold_icon = tk.PhotoImage(file="C:\\Users\\kunal\\Downloads\\text_pro icon\\icons2\icons2\\bold.png")
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2,padx=5)
# italic buttonh
italic_icon = tk.PhotoImage(file="C:\\Users\\kunal\\Downloads\\text_pro icon\\icons2\icons2\\italic.png")
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=3,padx=5)
# underline
underline_icon = tk.PhotoImage(file="C:\\Users\\kunal\\Downloads\\text_pro icon\\icons2\icons2\\underline.png")
underline_btn = ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0, column=4,padx=5)
# align_center
align_center_icon = tk.PhotoImage(file="C:\\Users\\kunal\Downloads\\text_pro icon\\icons2\\icons2\\align_center.png")
align_center_btn = ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=5,padx=5)
# align_left
align_left_icon = tk.PhotoImage(file="C:\\Users\\kunal\Downloads\\text_pro icon\\icons2\\icons2\\align_left.png")
align_left_btn = ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=4,padx=5)
# align_right
align_right_icon = tk.PhotoImage(file="C:\\Users\\kunal\Downloads\\text_pro icon\\icons2\\icons2\\align_right.png")
align_right_btn = ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=6,padx=5)
# font color button
font_color_icon = tk.PhotoImage(file="C:\\Users\\kunal\\Downloads\\text_pro icon\\icons2\\icons2\\font_color.png")
font_color_btn = ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=7,padx=5)

# ----------- end toolbar ------------
# ----------- text editor -----------
text_editor = tk.Text(main_app)
text_editor.config(wrap='word', relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_app)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# font family and font size functionality
current_font_family = "Arial"
current_font_size = 12

def change_font(main_app):
    global  current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))
def change_font_size(main_app):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))

font_size.bind("<<ComboboxSelected>>",change_font_size)
font_box.bind("<<ComboboxSelected>>",change_font)
# ----------- Button functionality----
# Bold button functionality
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()["weight"] == 'normal':
        '''if its not already bold so we can convert into bold font'''
        text_editor.configure(font=(current_font_family, current_font_size, 'bold' ))

    if text_property.actual()["weight"] == 'bold':
        '''if its already bold so we can convert into normal font'''
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))
bold_btn.configure(command=change_bold)

# italic button functionality
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()["slant"] == 'roman':
        '''if its not italic so we can convert into italic font'''
        text_editor.configure(font=(current_font_family, current_font_size, 'italic' ))

    if text_property.actual()["slant"] == 'italic':
        '''if its already italic so we can convert into normal(roman) font'''
        text_editor.configure(font=(current_font_family, current_font_size, 'roman'))

italic_btn.configure(command=change_italic)

# underline button functionality
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()["underline"] == 0:
        '''if its not underlined so we can convert into underlined font'''
        text_editor.configure(font=(current_font_family, current_font_size, 'underline' ))

    if text_property.actual()["underline"] == 1:
        '''if its already underlined so we can convert into not underline font'''
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

underline_btn.configure(command=change_underline)
## font color configuration
def change_font_color():
    '''change color of font '''
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
font_color_btn.configure(command=change_font_color)

text_editor.configure(font=("Arial", 12))
# ----- Align functionality --
def align_left():
    '''align text in left side'''
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')
align_left_btn.configure(command=align_left)

def align_center():
    '''align text in center side'''
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')
align_center_btn.configure(command=align_center)

def align_right():
    '''align text in right side'''
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')
align_right_btn.configure(command=align_right)

# ----------- end editor ------------

# ----------- main status bar -----------
status_bar = ttk.Label(main_app,text="Status Bar")
status_bar.pack(side=tk.BOTTOM)
text_changed = False
def count_char(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        word = len(text_editor.get(1.0, 'end-1c').split())
        character = len(text_editor.get(1.0, 'end-1c').replace(" ", ''))
        status_bar.config(text=f'Characters : {character} | Words : {word}')
    text_editor.edit_modified(False)
text_editor.bind('<<Modified>>', count_char)
# ----------- end status bar ------------

# ----------- main menu functionality  -----------

url = "" # variable

# --------------- file command ------------
# New command
def New_file(event=None):
    global url
    url = ""
    text_editor.delete(1.0, tk.END)
file.add_command(label="New", image=new_icon, compound=tk.LEFT, accelerator="CTRL+N", command=New_file)

# Open command
def Open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File", filetypes=(('Text File',"*.txt"), ("All files", "*.*")))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except "FileNotFoundError":
        return
    except:
        return
    main_app.title(os.path.basename(url))

file.add_command(label="Open", image=open_icon, compound=tk.LEFT, accelerator="CTRL+O",command=Open_file)
# ---- save command
def Save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File','*.txt'), ('All files','*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return

file.add_command(label="Save", image=save_icon, compound=tk.LEFT, accelerator="CTRL+S",command=Save_file)
# -------- Save as file
def Save_as(event=None):
    global url
    try:
        content = text_editor.get(1.0,tk.END)
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
        url.write(content2)
        url.close()
    except:
        return

file.add_command(label="Save As", image=save_as_icon, compound=tk.LEFT, accelerator="CTRL+ALT+S",command=Save_as)
# --------- EXit
def Exit(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel("Warning", "Do you want to save the file")
            if mbox == True:
                if url:
                    content = str(text_editor.get(1.0, tk.END))
                    with open (url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                        main_app.destroy()
                else:
                    content = text_editor.get(1.0, tk.END)
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',filetypes=(('Text File', '*.txt'),('All files', " *.*")))
                    url.write(content)
                    url.close()
                    main_app.destroy()
            elif mbox is False:
                main_app.destroy()
        else:
            main_app.destroy()
    except:
        return

file.add_command(label="Exit", image=exit_icon, compound=tk.LEFT, accelerator="CTRL+Q",command=Exit)


# Edit command
edit.add_command(label="Copy", image=copy_icon, compound=tk.LEFT, accelerator="CTRL+C",command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label="Paste", image=paste_icon, compound=tk.LEFT, accelerator="CTRL+V",command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label="Cut", image=cut_icon, compound=tk.LEFT, accelerator="CTRL+X",command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label="Clear_all", image=clear_all_icon, compound=tk.LEFT,command=text_editor.delete(1.0, tk.END))
# ---------- find functionality
def find_func(event=None):

    def find(event=None):
        word = find_input.get()
        text_editor.tag_remove("match", '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos} + {len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='#ff0000', backgroud='#0000ff')


    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)


    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

    ## Frame
    find_frame = ttk.LabelFrame(find_dialogue, text = 'Find/Replace')
    find_frame.pack(pady=20)
    ## Lables
    text_find_lable = ttk.Label(find_frame,text="Find : ")
    text_replace_lable = ttk.Label(find_frame,text="Replace ")
    ## Entry
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame,width=30)
    ## Button
    find_button = ttk.Button(find_frame,text="Find", command=find)
    replace_button = ttk.Button(find_frame, text='Replace', command=replace)

    ## label Grid
    text_find_lable.grid(row=0, column=0, padx=4, pady=4)
    text_replace_lable.grid(row=1, column=0, padx=4, pady=4)

    ## Entry grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    ## button grid
    find_button.grid(row=2, column=0, padx=8, pady= 4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()

edit.add_command(label="Find", image=find_icon, compound=tk.LEFT, accelerator="CTRL+F",command=find_func)

# View check button
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True

view.add_checkbutton(label="Tool bar",onvalue=True, offvalue=0,variable=show_toolbar,image=tool_bar_icon, compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label="Status bar",onvalue=1, offvalue=False,variable=show_statusbar,image=status_bar_icon, compound=tk.LEFT, command=hide_statusbar)
status_bar.config()
# color Theme
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg = fg_color)

count = 0
for i in color_dict:
    color_theme.add_radiobutton(label=i, image=color_icon[count], variable=theme_choice, compound=tk.LEFT,command= change_theme)
    if count < len(color_icon):
        count+=1
# ----------- main menu functionality end ------------
main_app.config(menu=main_menu)
# --------- bind shortcut keys
main_app.bind('<Control-n>',New_file)
main_app.bind('<Control-o>',Open_file)
main_app.bind('<Control-s>',Save_file)
main_app.bind('<Control-Alt-s>',Save_as)
main_app.bind('<Control-q>',Exit)
main_app.bind('<Control-f>',find_func)
main_app.mainloop()
