from tkinter import *
import requests



def get_quote():
    response = requests.get(url="https://zenquotes.io/api/random")
    print(response.status_code)
    print(response.text)
    response.raise_for_status()
    data = response.json()
    quote = data[0]["q"]
    author = data[0]["a"]
    canvas.itemconfig(quote_text, text=f'"{quote}"\n- {author}')

window = Tk()
window.title("Quote Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Tap the button for a quote", width=250, font=("Arial", 18, "bold"), fill="white")
canvas.grid(row=0, column=0)

button_img = PhotoImage(file="button.png")
button = Button(image=button_img, highlightthickness=0, command=get_quote)
button.grid(row=1, column=0)



window.mainloop()
