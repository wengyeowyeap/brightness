from ttkwidgets.autocomplete import AutocompleteCombobox
from tkinter import *  
from tkinter import ttk

def donothing():
  filewin = Toplevel(root)
  button = Button(filewin, text="Do nothing button")
  button.pack()

# Function for checking the key pressed and updating the listbox 
def checkkey(event): 
  if event.keysym=='Down':
    lb.focus_set()
    lb.select_set(0) #This only sets focus on the first item.
    lb.event_generate("<<ListboxSelect>>")
  elif event.keysym=='Return':
    item_code_entry.focus_set()
  else:
    value = event.widget.get() 
    print(value)     
    # get data from l 
    if value == '': 
        data = l
        update(data)
        lb.pack_forget()
    else: 
        data = [] 
        for item in l: 
            if value.lower() in item.lower(): 
                data.append(item)
                update(data)
                lb.pack()
   
def update(data): 
  # clear previous data 
  lb.delete(0, 'end') 
  
  # put new data 
  for item in data: 
      lb.insert('end', item) 

def selectcustomer(event):
  selection = event.widget.curselection()
  lb.pack_forget()
  if selection:
      index = selection[0]
      customer.set(event.widget.get(index))
      customer_entry.focus_set()

# Driver code 
l = ['C','C++','Java', 
     'Python','Perl', 
     'PHP','ASP','JS',
     "apple", "banana", "cherry", 
     "orange", "kiwi", "melon", "mango",
    "Rice", "Chickpeas", "Pulses", "bread", "meat",
    "Milk", "Bacon", "Eggs", "Rice Cooker", "Sauce",
    "Chicken Pie", "Apple Pie", "Pudding" ]

def focusweight(event):
  sample_weight_entry.focus_set() 

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
ttk.Label(tab1,  text ="Form Code: ").grid(column = 0,  row = 0, padx = (5,0), pady = (10,0))
ttk.Label(tab1,  text ="VAR - Clicked Form Code").grid(column = 1,  row = 0, pady = (10,0))
ttk.Label(tab1,  text ="Customer: ").grid(column = 2,  row = 0, padx = (15,0), pady = (10,0))
ttk.Label(tab1,  text ="Date: ").grid(column = 4,  row = 0, padx = (15,0), pady = (10,0))
ttk.Label(tab1,  text ="VAR - Clicked date").grid(column = 5,  row = 0, pady = (10,0))
ttk.Label(tab1,  text ="Item Code: ").grid(column = 0,  row = 1, padx = (5,0), pady = (10,0))
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
# create a frame 
customer_input_frame = ttk.Frame(tab1)
customer_input_frame.grid(column =3,  row = 0)
# If customer not in list, pop up add new customer window
customer = StringVar() 
customer_entry = Entry(customer_input_frame, textvariable=customer) 
customer_entry.pack() 
customer_entry.bind('<KeyRelease>', checkkey) 
#creating list box 
lb = Listbox(customer_input_frame)
lb.pack()
lb.pack_forget()
update(l) 
lb.bind("<KeyRelease-Return>", selectcustomer)
lb.bind("<ButtonRelease-1>", selectcustomer)
lb.bind("<Double-Button-1>", selectcustomer)

# tab1 button #
new_record = Button(tab1, text = 'NEW', command = root.destroy)
new_record.grid(column = 6,  row = 0, padx = 10, pady = 10, ipadx = 10, ipady = 10)
delete_record = Button(tab1, text = 'DELETE', command = root.destroy)
delete_record.grid(column = 7,  row = 0, padx = 10, pady = 10, ipadx = 10, ipady = 10)
edit_record = Button(tab1, text = 'EDIT', command = root.destroy)
edit_record.grid(column = 8,  row = 0, padx = 10, pady = 10, ipadx = 10, ipady = 10)
add_record = Button(tab1, text = 'ADD', command = root.destroy)
add_record.grid(column = 9,  row = 0, padx = 10, pady = 10, ipadx = 10, ipady = 10)

# create a frame in tab 1 for left table
left_table_frame = ttk.Frame(tab1)
left_table_frame.grid(column = 0,  row = 2, columnspan = 4)
# Constructing vertical scrollbar 
left_table_scroll = ttk.Scrollbar(left_table_frame, orient ="vertical") 
left_table_scroll.pack(side ='right', fill='y')
# left table # 
left_table = ttk.Treeview(left_table_frame, selectmode ='browse', height = 20, yscrollcommand = left_table_scroll.set) 
left_table.pack(side ='left')
# Configuring scrollbar 
left_table_scroll.configure(command = left_table.yview) 
# Defining number of columns 
left_table["columns"] = ("1", "2", "3", "4") 
# Defining heading 
left_table['show'] = 'headings'
# Assigning the width and anchor to the respective columns 
left_table.column("1", width = 100, anchor ='c') 
left_table.column("2", width = 100, anchor ='c') 
left_table.column("3", width = 100, anchor ='c') 
left_table.column("4", width = 100, anchor ='c') 
# Assigning the heading names to the respective columns 
left_table.heading("1", text ="Form Code") 
left_table.heading("2", text ="Item") 
left_table.heading("3", text ="Date")
left_table.heading("4", text ="Customer")
# Inserting the items and their features to the columns built 
left_table.insert("", 'end', text ="L1", values =("Nidhi", "F", "25")) 
left_table.insert("", 'end', text ="L2", values =("Nisha", "F", "23")) 
left_table.insert("", 'end', text ="L3", values =("Preeti", "F", "27")) 
left_table.insert("", 'end', text ="L4", values =("Rahul", "M", "20")) 
left_table.insert("", 'end', text ="L5", values =("Sonu", "F", "18")) 
left_table.insert("", 'end', text ="L6", values =("Rohit", "M", "19")) 
left_table.insert("", 'end', text ="L7", values =("Geeta", "F", "25")) 
left_table.insert("", 'end', text ="L8", values =("Ankit", "M", "22")) 
left_table.insert("", 'end', text ="L10", values =("Mukul", "F", "25")) 
left_table.insert("", 'end', text ="L11", values =("Mohit", "M", "16")) 
left_table.insert("", 'end', text ="L12", values =("Vivek", "M", "22")) 
left_table.insert("", 'end', text ="L13", values =("Suman", "F", "30")) 
left_table.insert("", 'end', text ="L1", values =("Nidhi", "F", "25")) 
left_table.insert("", 'end', text ="L2", values =("Nisha", "F", "23")) 
left_table.insert("", 'end', text ="L3", values =("Preeti", "F", "27")) 
left_table.insert("", 'end', text ="L4", values =("Rahul", "M", "20")) 
left_table.insert("", 'end', text ="L5", values =("Sonu", "F", "18")) 
left_table.insert("", 'end', text ="L6", values =("Rohit", "M", "19")) 
left_table.insert("", 'end', text ="L7", values =("Geeta", "F", "25")) 
left_table.insert("", 'end', text ="L8", values =("Ankit", "M", "22")) 
left_table.insert("", 'end', text ="L10", values =("Mukul", "F", "25")) 
left_table.insert("", 'end', text ="L11", values =("Mohit", "M", "16")) 
left_table.insert("", 'end', text ="L12", values =("Vivek", "M", "22")) 
left_table.insert("", 'end', text ="L13", values =("Suman", "F", "30")) 

# create a frame in tab 1 for right table
right_table_frame = ttk.Frame(tab1)
right_table_frame.grid(column = 4,  row = 2, columnspan = 4)
# Constructing vertical scrollbar 
right_table_scroll = ttk.Scrollbar(right_table_frame, orient ="vertical") 
right_table_scroll.pack(side ='right', fill='y')
# right table # 
right_table = ttk.Treeview(right_table_frame, selectmode ='browse', height = 20, yscrollcommand = right_table_scroll.set) 
right_table.pack(side ='left')
# Configuring scrollbar 
right_table_scroll.configure(command = right_table.yview) 
# Defining number of columns 
right_table["columns"] = ("1", "2", "3", "4") 
# Defining heading 
right_table['show'] = 'headings'
# Assigning the width and anchor to the respective columns 
right_table.column("1", width = 100, anchor ='c') 
right_table.column("2", width = 100, anchor ='c') 
right_table.column("3", width = 100, anchor ='c') 
right_table.column("4", width = 100, anchor ='c') 
# Assigning the heading names to the respective columns 
right_table.heading("1", text ="Form Code") 
right_table.heading("2", text ="Item") 
right_table.heading("3", text ="Sample Weight")
right_table.heading("4", text ="Sample Return")
# Inserting the items and their features to the columns built 
right_table.insert("", 'end', text ="L1", values =("Nidhi", "F", "25")) 
right_table.insert("", 'end', text ="L2", values =("Nisha", "F", "23")) 
right_table.insert("", 'end', text ="L3", values =("Preeti", "F", "27")) 
right_table.insert("", 'end', text ="L4", values =("Rahul", "M", "20")) 
right_table.insert("", 'end', text ="L5", values =("Sonu", "F", "18")) 
right_table.insert("", 'end', text ="L6", values =("Rohit", "M", "19")) 
right_table.insert("", 'end', text ="L7", values =("Geeta", "F", "25")) 
right_table.insert("", 'end', text ="L8", values =("Ankit", "M", "22")) 
right_table.insert("", 'end', text ="L10", values =("Mukul", "F", "25")) 
right_table.insert("", 'end', text ="L11", values =("Mohit", "M", "16")) 
right_table.insert("", 'end', text ="L12", values =("Vivek", "M", "22")) 
right_table.insert("", 'end', text ="L13", values =("Suman", "F", "30")) 
right_table.insert("", 'end', text ="L1", values =("Nidhi", "F", "25")) 
right_table.insert("", 'end', text ="L2", values =("Nisha", "F", "23")) 
right_table.insert("", 'end', text ="L3", values =("Preeti", "F", "27")) 
right_table.insert("", 'end', text ="L4", values =("Rahul", "M", "20")) 
right_table.insert("", 'end', text ="L5", values =("Sonu", "F", "18")) 
right_table.insert("", 'end', text ="L6", values =("Rohit", "M", "19")) 
right_table.insert("", 'end', text ="L7", values =("Geeta", "F", "25")) 
right_table.insert("", 'end', text ="L8", values =("Ankit", "M", "22")) 
right_table.insert("", 'end', text ="L10", values =("Mukul", "F", "25")) 
right_table.insert("", 'end', text ="L11", values =("Mohit", "M", "16")) 
right_table.insert("", 'end', text ="L12", values =("Vivek", "M", "22")) 
right_table.insert("", 'end', text ="L13", values =("Suman", "F", "30")) 
root.config(menu=menubar)
root.mainloop()  