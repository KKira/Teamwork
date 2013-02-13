"""
Welcome Team

A resource: http://effbot.org/tkinterbook/
A better resource: http://pypi.python.org/pypi/PySide
"""
import Tkinter as tk

app = tk.Tk()

frame = tk.Frame(app)
frame.pack()

label = tk.Label(frame, text="""
Add your name to this list.
If you're feeling adventurous, add a widget.
Or something else?
---------------------------------------------------------------------------
Harold
Alberto

""", borderwidth=5)
label.pack(expand=1)

tk.mainloop()
