import customtkinter as ctk  # pyright: ignore[reportMissingImports]

ctk.set_appearance_mode("light")  # light mode set karna

app = ctk.CTk()  # app window create karna
app.title("Simple Calculator")  # window ka title set karna
app.geometry("300x330")  # window size set karna

entry = ctk.CTkEntry(   #jahan numbers display honge button click karne k baad
    app,
    width=250,
    height=50,
    justify="right",  # text right align karna
    font=("Arial", 20,"bold"),
    fg_color="#EBEFF0",  # entry ka background color
    text_color="#050505",  # entry ka text color
    border_color="#5e0606",  # entry ka border color
    border_width=2  # border ki width
)
entry.pack(pady=20)  # entry ko window mein add (pack) kar do aur vertical padding (upar aur neeche) se 20 pixels ka space do

def button_click(text):  # jab button click ho
    if text == "=":  # agar equal sign hai
        try:
            result = eval(entry.get())  # expression evaluate karna
            entry.delete(0, ctk.END)  # pehle text delete karna
            entry.insert(0, str(result))  # result show karna
        except:
            entry.delete(0, ctk.END)  # error case mai clear karna
            entry.insert(0, "Error")  # "Error" show karna
    elif text == "C":  # agar C dabaya
        entry.delete(0, ctk.END)  # entry clear karna
    else:
        entry.insert(ctk.END, text)  # button ka text add karna

buttons = [  # button layout
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

for row in buttons:  # har row ke liye
    frame = ctk.CTkFrame(app)  # har row of button k liye ek naya frame banaya
    frame.pack(pady=5)  # row ko window main add karna aur upar-neeche 5 pixels ka gap dena
    for item in row:  # har ek no. k liye button banao
        btn = ctk.CTkButton(
            frame,
            text=item,
            width=50,
            height=40,
            command=lambda t=item: button_click(t),  # button click handle karna
            fg_color="#000000",  # button ka color
            hover_color="#f0bd45",  # hover color
            text_color="#FFFFFF",  # text ka color
            font=("Arial", 14, "bold"),  # bold font
            border_color="#f0bd45",  # entry ka border color
            border_width=2
        )
        btn.pack(side='left', padx=5)  # button ko left side par lagana with spacing

app.mainloop()  # app run karna
