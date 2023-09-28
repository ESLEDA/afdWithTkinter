import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

window = tk.Tk()
window.title("afd")
window.geometry("420x280")
window.config(bg="PaleGreen1")
window.resizable(0,0)
fontStyle = tkFont.Font(family="Lucida Grande", size=16)

title = tk.Label(window, text="   Inserte cadena:",  font=fontStyle)
title.pack()
title.place(x=120,y=60)
title.config(bg="PaleGreen1")
title.config(fg="grey30")

input_cadena = tk.Entry(window)
input_cadena.pack()
input_cadena.place(x=155,y=100)

class AFD:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14'}
        self.alphabet = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                         'A', 'B', 'C', 'D', 'E', 'F', 'G','H', 'I', 'J',
                         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
                         'U', 'V', 'W', 'X', 'Y', 'Z', '-'}
        
        self.transitions = {
            'q0':  {'D': 'q1', 'E': 'q2'},
            'q1':  {'D': 'q3', 'E': 'q3', 'F': 'q3', 'G': 'q3', 'H' : 'q3', 'I': 'q3', 'J': 'q3', 'K': 'q3', 'L': 'q3', 'M' : 'q3', 
                    'N': 'q3', 'O': 'q3', 'P': 'q3', 'Q': 'q3', 'R': 'q3', 'S': 'q3', 'T': 'q3', 'U': 'q3', 'V': 'q3','W': 'q3', 'X': 'q3',
                    'Y': 'q3', 'Z': 'q3'},
            'q2':  {'A': 'q4', 'B': 'q4', 'C': 'q4', 'D': 'q4', 'E': 'q4', 'F': 'q4', 'G': 'q4'},
            'q3':  {'-': 'q5' },
            'q4':  {'-': 'q5' },
            'q5':  {'0': 'q6' ,'1': 'q7', '2': 'q7', '3': 'q7', '4': 'q7', '5': 'q7', '6': 'q7', '7': 'q7', '8': 'q7', '9': 'q7'},
            'q6':  {'0': 'q8', '1': 'q9', '2': 'q9', '3': 'q9', '4': 'q9', '5': 'q9', '6': 'q9', '7': 'q9', '8': 'q9', '9': 'q9'},
            'q7':  {'0': 'q9', '1': 'q9', '2': 'q9', '3': 'q9', '4': 'q9', '5': 'q9', '6': 'q9', '7': 'q9', '8': 'q9', '9': 'q9'},
            'q8':  {'0': 'q10','1': 'q11','2': 'q11','3': 'q11','4': 'q11','5': 'q11','6': 'q11','7': 'q11','8': 'q11','9': 'q11'},
            'q9':  {'0': 'q11','1': 'q11','2': 'q11','3': 'q11','4': 'q11','5': 'q11','6': 'q11','7': 'q11','8': 'q11','9': 'q11'},
            'q10': {           '1': 'q12','2': 'q12','3': 'q12','4': 'q12','5': 'q12','6': 'q12','7': 'q12','8': 'q12','9' :'q12'},
            'q11': {'0': 'q12','1': 'q12', '2': 'q12', '3': 'q12', '4': 'q12', '5': 'q12', '6': 'q12', '7': 'q12', '8': 'q12', '9' : 'q12'},
            'q12': {'-': 'q13'},
            'q13': {'A': 'q14', 'B': 'q14', 'C': 'q14', 'D': 'q14', 'E' : 'q14', 'F': 'q14', 'G': 'q14', 'H': 'q14', 'I': 'q14', 'J': 'q14', 
                    'K': 'q14', 'L': 'q14', 'M': 'q14', 'N': 'q14', 'O': 'q14', 'P': 'q14', 'Q' : 'q14', 'R': 'q14', 'S': 'q14', 'T': 'q14', 
                    'U': 'q14', 'V': 'q14', 'W': 'q14', 'X': 'q14', 'Y' : 'q14', 'Z': 'q14'},
            'q14' : {}
        }
        self.initial_state = 'q0'
        self.accept_states = {'q14'}
        
    def validar(self, input_string):
        current_state = self.initial_state
        current_states = [current_state]  
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False 
            if current_state not in self.states:
                return False  
            current_state = self.transitions[current_state].get(symbol, None)
            current_states.append(current_state)  
            if current_state is None:
                return False  

        if current_state in self.accept_states:
            return current_states 

        return False

automata = AFD()

def verificarCadena():
    input_string = input_cadena.get()
    rout_state = automata.validar(input_string)
    if rout_state:
        valid_message.config(text=f"(◕‿◕)Cadena valida: {input_string}")
        show_route(rout_state)
    else:
        valid_message.config(text=f"(◕_◕)Cadena invalida: {input_string}")
        show_route([])  

def show_route(visited_states):
    recorrido_text = "\n".join(visited_states)
    write_route.config(text=f"\n{recorrido_text}")

fontStyle2 = tkFont.Font(family="Lucida Grande", size=12)
btn = tk.Button(window, text="enviar", command=verificarCadena, font=fontStyle2)
btn.pack()
btn.place(x=180,y=130)
btn.config(bg="tomato")
btn.config(bd="0")
btn.config(cursor="circle")
btn.config(foreground="grey30")
btn.config(width="8", height="1")

valid_message = tk.Label(window, text="")
valid_message.pack()
valid_message.place(x=140,y=180)
valid_message.config(bg="PaleGreen1")

write_route = tk.Label(window, text="")
write_route.pack()
write_route.place(x=330, y=65)
write_route.config(bg="PaleGreen1")

window.mainloop()