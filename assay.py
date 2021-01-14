from ttkwidgets.autocomplete import AutocompleteCombobox
from tkinter import *  
from tkinter import ttk

def donothing():
  filewin = Toplevel(root)
  button = Button(filewin, text="Do nothing button")
  button.pack()

def focusweight(event):
 sample_weight_entry.focus_set()

def focusitemcode(event):
 item_code_entry.focus_set() 

def submit(event): 
  code=item_code_entry.get() 
  weight=sample_weight_entry.get()
    
  print("The code is : " + code) 
  print("The weight is : " + weight) 
    
  item_code.set("") 
  sample_weight.set("") 

root = Tk() 
root.title("Brightness Assay")

# Menu #
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Setting", command=donothing)

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# Tab #
tabControl = ttk.Notebook(root) 
  
tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl) 
tab3 = ttk.Frame(tabControl) 
tab4 = ttk.Frame(tabControl) 
tab5 = ttk.Frame(tabControl) 
  
tabControl.add(tab1, text ='Main') 
tabControl.add(tab2, text ='First Weight')
tabControl.add(tab3, text ='Last Weight') 
tabControl.add(tab4, text ='Sample Return') 
tabControl.add(tab5, text ='Report') 
tabControl.pack(expand = 1, fill ="both") 

#tab 1#
ttk.Label(tab1,  text ="Form Code: ").grid(column = 0,  row = 0, padx = (5,0), pady = 10)
ttk.Label(tab1,  text ="VAR - Clicked Form Code").grid(column = 1,  row = 0, pady = 10)
ttk.Label(tab1,  text ="Customer: ").grid(column = 2,  row = 0, padx = (15,0), pady = 10)
ttk.Label(tab1,  text ="Date: ").grid(column = 4,  row = 0, padx = (15,0), pady = 10)
ttk.Label(tab1,  text ="VAR - Clicked date").grid(column = 5,  row = 0, pady = 10)
ttk.Label(tab1,  text ="Item Code: ").grid(column = 0,  row = 1, padx = (5,0), pady = 10)
item_code = StringVar()
item_code_entry = Entry(tab1, textvariable = item_code)
item_code_entry.grid(column = 1,  row = 1)
item_code_entry.bind('<Return>', focusweight)
ttk.Label(tab1,  text ="Sample Weight (g): ").grid(column = 2,  row = 1, padx = (5,0), pady = 10)
sample_weight = StringVar()
sample_weight_entry = Entry(tab1, textvariable = sample_weight)
sample_weight_entry.grid(column = 3,  row = 1)
sample_weight_entry.bind('<Return>', submit) #trigger submit function when enter is pressed

# Combobox creation
# If customer not in list, pop up add new customer window
customer = StringVar() 
customerentry = AutocompleteCombobox(tab1, width=20, completevalues=["Sam", "Felicia", "Alan", "Brodie"], textvariable = customer)
customerentry.grid(column = 3, row = 0) 
customerentry.current()
customerentry.bind('<Return>', focusitemcode)

root.config(menu=menubar)
root.mainloop()  