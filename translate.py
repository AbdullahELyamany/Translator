
"""
 Translator App with a GUI
 
 Created By *Abdullah EL-Yamany*

 YouTube Channel => Codezilla
 Video Link => https://youtu.be/ksV4sJ41H_c?si=yWwxMn7SfXJC6ezX
"""

import tkinter as tk
from tkinter import ttk
from libretranslatepy import LibreTranslateAPI


lt = LibreTranslateAPI("https://translate.argosopentech.com/")

lang_data = lt.languages()
lang_name = [lang['name'] for lang in lang_data]
lang_codes = {lang['name']: lang['code'] for lang in lang_data}

#------------- Translate Function ------------#
def translate():
    try:
        translated_text = lt.translate(input_text.get("1.0", tk.END), lang_codes[input_lang.get()], lang_codes[output_lang.get()])
        output_text.delete("1.0", tk.END)
        output_text.insert("1.0", translated_text)
    except KeyError as err:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, err)

#------------- Clear/Delete Function ------------#
def delete():
    
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)


#------------- GUI App ------------#
root = tk.Tk()
root.geometry('700x400')
root.title("Translator")
root.config(bg='whitesmoke')

title_label = tk.Label(root, text="[+] AE  Translator", font=("arial 20 bold"))
title_label.pack(fill='x')

#------------- input section ------------#
input_label = tk.Label(root, text="Enter Text", font=("arial 15 bold"), bg='whitesmoke')
input_label.place(x=240, y=100)

input_text = tk.Text(root, font="arial 13", height=11, width=30)
input_text.place(x=20 , y=240)

input_lang = ttk.Combobox(root, width=20, values=lang_name)
input_lang.place(x=210, y=170)
input_lang.set("Choose Input Language")

#------------- output section ------------#
output_label = tk.Label(root, text="Output", font=("arial 15 bold"), bg='whitesmoke')
output_label.place(x=1370, y=100)

output_text = tk.Text(root, font="arial 13", height=11, width=30)
output_text.place(x=1100 , y=240)

output_lang = ttk.Combobox(root, width=22, values=lang_name)
output_lang.place(x=1300, y=170)
output_lang.set("Choose Output Language")

#------------- Translate Button ------------#
trans_bt = tk.Button(root, text="Translate", font="arial 15 bold", command=translate)
trans_bt.place(x=780, y=830)

#------------- Clear/Delete Button ------------#
delete_bt = tk.Button(root, text="Clear", font="arial 13 bold", command=delete)
delete_bt.place(x=835, y=930)

root.mainloop()
