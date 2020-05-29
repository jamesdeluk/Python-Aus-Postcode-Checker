"""checks postcode against aus regional postcodes"""

from tkinter import *
from tkinter import ttk
import json

specific_postcodes_file = 'Resources/postcodes.txt'
with open(specific_postcodes_file, 'r') as f:
    specific_postcodes = f.read()[1:-1].split(', ')
    specific_postcodes = [int(x) for x in specific_postcodes]

postcodes_lookup_file = 'Resources/au_postcodes.json'
with open(postcodes_lookup_file) as f:
    postcodes_lookup = json.load(f)


def get_regions(postcode):
    # print('called')
    try:
        postcode = int(postcode)
        # region_str = ''
        region_list = []
        # print(postcode)
        # print(type(postcode))
        for region in postcodes_lookup:
            if region['postcode'] == postcode:
                # print(region['postcode'])
                # print(type(region['postcode']))
                # region_str += region['place_name']
                # print(region_str)
                region_list.append(region['place_name'])
        return region_list
    except:
        return
    # print('return')

regionals = []
not_regionals = []
# output = ''

def check(*args):
    """checking code"""
    # global output
    postcode_input = postcode.get()
    regions = get_regions(postcode_input)
    s = ''
    if len(postcode_input) == 0:
        s += f'Enter something...\n'
    elif len(postcode_input) != 4:
        s += f'{postcode_input}: Invalid postcode\n'
    elif len(regions) == 0:
        s += f'{postcode_input}: Invalid postcode\n'
    elif int(postcode_input) in specific_postcodes:
        for region in regions:
            s += f'{postcode_input} {region}: ^_^ Regional\n'
            regionals.append(postcode_input)
            p2t.insert(END, f'{postcode_input} ')
    else:
        for region in regions:
            s += f'{postcode_input} {region}: ㅠ_ㅠ Not regional\n'
            not_regionals.append(postcode_input)
            p3t.insert(END, f'{postcode_input} ')
    # output = s + output
    result.set(s.strip())
    p1t.insert('1.0', s)
    e1.delete(0, END)

root = Tk()

root.title('Postcode Checker')
root.geometry('400x400')
# mainframe = Frame(root)
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

s = ttk.Style()
s.theme_use('clam')
# ('aqua', 'clam', 'alt', 'default', 'classic')

postcode = StringVar()
result = StringVar()
option = StringVar()
result.set('Please enter a postcode')

e1 = ttk.Entry(mainframe, textvariable=postcode)
e1.grid(row=0, column=0, sticky=NSEW)

b1 = ttk.Button(mainframe, text="Check", command=check, default=ACTIVE)
b1.grid(row=1, column=0, sticky=NSEW)

l1 = ttk.Label(mainframe, textvariable=result)
l1.grid(row=2, column=0, sticky=NSEW)

nb = ttk.Notebook(mainframe)
nb.grid(row=3, column=0, sticky=NSEW)
p1 = ttk.Frame(nb)
p1t = Text(p1, height=15)
p2 = ttk.Frame(nb)
p2t = Text(p2, height=15)
p3 = ttk.Frame(nb)
p3t = Text(p3, height=15)
for widget in [p1t, p2t, p3t]:
    widget.grid(row=0, column=0, sticky=NSEW)
nb.add(p1, text='Output')
nb.add(p2, text='Regional')
nb.add(p3, text='Not Regional')

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

e1.focus()

mainframe.grid_columnconfigure(0,weight=1)
# # self.grid_columnconfigure(1,weight=1)
# # self.grid_columnconfigure(2,weight=1)
# mainframe.grid_rowconfigure(0,weight=1)
# mainframe.grid_rowconfigure(1,weight=1)
# mainframe.grid_rowconfigure(2,weight=1)
# mainframe.grid_rowconfigure(3,weight=1)

root.bind('<Return>', check)
# b1.bind('<Enter>', lambda e: b1.configure(bg="blue"))
# b1.bind('<Leave>', lambda e: b1.configure(text='Moved mouse outside'))

root.mainloop()
