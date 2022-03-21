import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import hashtagGenerator as htg
import pyperclip
#hashtag Gen Function

# root window
root = tk.Tk()
root.geometry("300x150")
root.resizable(False, False)
root.title('Hashtag Generator')

# store hashtag and number of hashtag
hashtagInput = tk.StringVar()
numberOfHash = tk.StringVar()

def generateClick():
    gen   = htg.HashtagGenerator()
    input = hashtagInput.get() ; ammount = int(numberOfHash.get())
    tags  = gen.GenerateTags([input],ammount) ; msg = ""
    for t in tags : msg = msg + str(t) + "\n"
    # callback when the generate button clicked
    pyperclip.copy(msg)
    showinfo( title='Hashtags Generated', message = msg +"Success! The hashtags have been copied to your clipboard \n")        


# Sign in frame
box = ttk.Frame(root) ; box.pack(padx=10, pady=10, fill='x', expand=True)

# hashtag
hashtagInput_label = ttk.Label( box, text="Enter Hashtag:" )
hashtagInput_label.pack( fill='x', expand=True )

hashtagInput_entry = ttk.Entry( box, textvariable=hashtagInput )
hashtagInput_entry.pack( fill='x', expand=True ) ; hashtagInput_entry.focus()

# number of hashtags
numberOfHash_label = ttk.Label( box, text="Enter amount of Hashtags:" )
numberOfHash_label.pack( fill='x',expand=True )

numberOfHash_entry = ttk.Entry( box, textvariable=numberOfHash )
numberOfHash_entry.pack(fill='x', expand=True)

# generate button
generate_button = ttk.Button( box, text="Generate", command=generateClick )
generate_button.pack( fill='x', expand=True, pady=10 )

root.mainloop()