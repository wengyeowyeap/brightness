from tkinter import *  
from tkinter import ttk

def donothing():
  filewin = Toplevel(root)
  button = Button(filewin, text="Do nothing button")
  button.pack()

class NewFormCode(Toplevel): 
  def __init__(self, master = None): 
    super().__init__(master = master) 
    self.title("New Formcode")
    self.geometry("280x450") 
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

    #New Formcode Button
    new_record = Button(self, text = 'New Formcode', command = self.destroy)
    new_record.grid(column = 0,  row = 0, padx = 10, pady = 10, ipadx = 5, ipady = 5)
    #Close Button
    close_new_record = Button(self, text = 'Close', command = self.destroy)
    close_new_record.grid(column = 1,  row = 0, padx = 10, pady = 10, ipadx = 5, ipady = 5)

    Label(self,  text ="Form Code: ").grid(column = 0,  row = 1, padx = (5,0), pady = (10,0))
    Label(self,  text ="VAR - New Form Code").grid(column = 1,  row = 1, pady = (10,0))
    Label(self,  text ="Date: ").grid(column = 0,  row = 2, padx = (15,0), pady = (10,0))
    Label(self,  text ="VAR - Current date").grid(column = 1,  row = 2, pady = (10,0))
    Label(self,  text ="Item Code: ").grid(column = 0,  row = 4, padx = (5,0), pady = (10,0))
    item_code = StringVar()
    item_code_entry = Entry(self, textvariable = item_code)
    item_code_entry.grid(column = 1,  row = 4)
    item_code_entry.bind('<Return>', focusweight)
    Label(self,  text ="Sample Weight (g): ").grid(column = 0,  row = 5, padx = (5,0), pady = 10)
    sample_weight = StringVar()
    sample_weight_entry = Entry(self, textvariable = sample_weight)
    sample_weight_entry.grid(column = 1,  row = 5)
    sample_weight_entry.bind('<Return>', submit) #trigger submit function when enter is pressed

    Label(self,  text ="Customer: ").grid(column = 0,  row = 3, padx = (15,0), pady = (10,0), sticky = N)
    # Combobox creation
    # create a frame 
    customer_input_frame = Frame(self)
    customer_input_frame.grid(column = 1,  row = 3, pady = (10,10))
    # If customer not in list, pop up add new customer fw_pct_frame
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

class EditRecord(Toplevel): 
  def __init__(self, master = None): 
    super().__init__(master = master) 
    self.title("Edit Record")
    self.geometry("280x450") 
    # Function for checking the key pressed and updating the listbox 

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

    #save Button
    save_record = Button(self, text = 'Save', command = self.destroy)
    save_record.grid(column = 0,  row = 6, padx = 10, pady = 10, ipadx = 5, ipady = 5)
    #Close Button
    close_new_record = Button(self, text = 'Close', command = self.destroy)
    close_new_record.grid(column = 1,  row = 6, padx = 10, pady = 10, ipadx = 5, ipady = 5)

    Label(self,  text ="Form Code: ").grid(column = 0,  row = 1, padx = (5,0), pady = (10,0))
    Label(self,  text ="VAR - Selected Form Code").grid(column = 1,  row = 1, pady = (10,0))
    Label(self,  text ="Date: ").grid(column = 0,  row = 2, padx = (15,0), pady = (10,0))
    Label(self,  text ="VAR - Current date").grid(column = 1,  row = 2, pady = (10,0))
    Label(self,  text ="Item Code: ").grid(column = 0,  row = 4, padx = (5,0), pady = (10,0))
    item_code = StringVar()
    item_code_entry = Entry(self, textvariable = item_code)
    item_code_entry.grid(column = 1,  row = 4)
    item_code_entry.bind('<Return>', focusweight)
    Label(self,  text ="Sample Weight (g): ").grid(column = 0,  row = 5, padx = (5,0), pady = 10)
    sample_weight = StringVar()
    sample_weight_entry = Entry(self, textvariable = sample_weight)
    sample_weight_entry.grid(column = 1,  row = 5)
    sample_weight_entry.bind('<Return>', submit) #trigger submit function when enter is pressed

class AddToFormcode(Toplevel): 
  def __init__(self, master = None): 
    super().__init__(master = master) 
    self.title("Edit Record")
    self.geometry("280x450")
    # Function for checking the key pressed and updating the listbox 

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

    #save Button
    save_record = Button(self, text = 'Add', command = self.destroy)
    save_record.grid(column = 0,  row = 6, padx = 10, pady = 10, ipadx = 5, ipady = 5)
    #Close Button
    close_new_record = Button(self, text = 'Close', command = self.destroy)
    close_new_record.grid(column = 1,  row = 6, padx = 10, pady = 10, ipadx = 5, ipady = 5)

    Label(self,  text ="Form Code: ").grid(column = 0,  row = 1, padx = (5,0), pady = (10,0))
    Label(self,  text ="VAR - Selected Form Code").grid(column = 1,  row = 1, pady = (10,0))
    Label(self,  text ="Date: ").grid(column = 0,  row = 2, padx = (15,0), pady = (10,0))
    Label(self,  text ="VAR - Current date").grid(column = 1,  row = 2, pady = (10,0))
    Label(self,  text ="Item Code: ").grid(column = 0,  row = 4, padx = (5,0), pady = (10,0))
    item_code = StringVar()
    item_code_entry = Entry(self, textvariable = item_code)
    item_code_entry.grid(column = 1,  row = 4)
    item_code_entry.bind('<Return>', focusweight)
    Label(self,  text ="Sample Weight (g): ").grid(column = 0,  row = 5, padx = (5,0), pady = 10)
    sample_weight = StringVar()
    sample_weight_entry = Entry(self, textvariable = sample_weight)
    sample_weight_entry.grid(column = 1,  row = 5)
    sample_weight_entry.bind('<Return>', submit) #trigger submit function when enter is pressed

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
ttk.Label(tab1,  text ="Clicked Form Code").grid(column = 1,  row = 0, pady = (10,0))
ttk.Label(tab1,  text ="Customer: ").grid(column = 2,  row = 0, padx = (15,0), pady = (10,0))
ttk.Label(tab1,  text ="Kedai Emas Sangat Panjang").grid(column = 3,  row = 0, pady = (10,0))
ttk.Label(tab1,  text ="Date: ").grid(column = 4,  row = 0, padx = (15,0), pady = (10,0))
ttk.Label(tab1,  text ="Clicked date").grid(column = 5,  row = 0, pady = (10,0))
ttk.Label(tab1,  text ="Item Code: ").grid(column = 0,  row = 1, padx = (5,0), pady = (10,0))
ttk.Label(tab1,  text ="Clicked item code").grid(column = 1,  row = 1, padx = (5,0), pady = (10,0))
ttk.Label(tab1,  text ="Sample Weight (g): ").grid(column = 2,  row = 1, padx = (5,0), pady = 10)
ttk.Label(tab1,  text ="0.0001").grid(column = 3,  row = 1, padx = (5,0), pady = 10)

# tab1 button #
new_record = Button(tab1, text = 'NEW')
new_record.grid(column = 6,  row = 0, padx = 10, pady = 10, ipadx = 10, ipady = 10)
new_record.bind("<Button>", lambda e: NewFormCode(root)) 
delete_record = Button(tab1, text = 'DELETE')
delete_record.grid(column = 7,  row = 0, padx = 10, pady = 10, ipadx = 10, ipady = 10)
edit_record = Button(tab1, text = 'EDIT')
edit_record.grid(column = 8,  row = 0, padx = 10, pady = 10, ipadx = 10, ipady = 10)
edit_record.bind("<Button>", lambda e: EditRecord(root)) 
add_to_formcode = Button(tab1, text = 'ADD')
add_to_formcode.grid(column = 9,  row = 0, padx = 10, pady = 10, ipadx = 10, ipady = 10)
add_to_formcode.bind("<Button>", lambda e: AddToFormcode(root)) 

# create a frame in tab 1 for left table
left_table_frame = ttk.Frame(tab1)
left_table_frame.grid(column = 0,  row = 2, columnspan = 4)
# Constructing vertical scrollbar 
left_table_scroll = ttk.Scrollbar(left_table_frame, orient ="vertical") 
left_table_scroll.pack(side ='right', fill='y')
# left table # 
left_table = ttk.Treeview(left_table_frame, selectmode ='browse', height = 20, yscrollcommand = left_table_scroll.set, columns = ("1", "2", "3", "4"), show = 'headings') 
left_table.pack(side ='left')
# Configuring scrollbar 
left_table_scroll.configure(command = left_table.yview) 
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
right_table = ttk.Treeview(right_table_frame, selectmode ='browse', height = 20, yscrollcommand = right_table_scroll.set, columns = ("1", "2", "3", "4"), show = 'headings') 
right_table.pack(side ='left')
# Configuring scrollbar 
right_table_scroll.configure(command = right_table.yview) 
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

# tab 2 #
# frame for info
fw_info_frame = ttk.Frame(tab2)
fw_info_frame.grid(column = 0,  row = 0)
ttk.Label(fw_info_frame,  text ="Customer").grid(column = 0,  row = 0, padx = (5,0), pady = (10,0), sticky=W)
ttk.Label(fw_info_frame,  text ="Kedai Emas Sangat Panjang").grid(column = 0, row = 1, padx = (5,0),pady = (10,0), sticky=W)
ttk.Label(fw_info_frame,  text ="Item Code").grid(column = 0,  row = 2, padx = (5,0), pady = (10,0), sticky=W)
ttk.Label(fw_info_frame,  text ="Clicked Item Code").grid(column = 0,  row = 3, padx = (5,0),pady = (10,0), sticky=W)
fw_entry_frame = ttk.Frame(tab2)
fw_entry_frame.grid(column = 1,  row = 0)
ttk.Label(fw_entry_frame,  text ="A").grid(column = 0,  row = 0, padx = 10)
ttk.Label(fw_entry_frame,  text ="B").grid(column = 0,  row = 1, padx = 10)
fwa = IntVar()
fwa_entry = Entry(fw_entry_frame, textvariable = fwa)
fwa_entry.grid(column = 1,  row = 0)
fwb = IntVar()
fwb_entry = Entry(fw_entry_frame, textvariable = fwb)
fwb_entry.grid(column = 1,  row = 1)
fw_pct_frame = ttk.Frame(tab2)
fw_pct_frame.grid(column = 2,  row = 0, padx = 20)
ttk.Label(fw_pct_frame, text = "Silver %", font = ("Times New Roman", 10)).grid(column = 0, row = 0) 
silver_pct = IntVar() 
pct_entry = ttk.Combobox(fw_pct_frame, width = 10, textvariable = silver_pct, values = [900, 750], state = 'readonly') 
pct_entry.grid(column = 0, row = 1) 
pct_entry.current()
#edit button
edit_fw = Button(tab2, text = 'EDIT')
edit_fw.grid(column = 3,  row = 0, padx = 10, ipadx = 10, ipady = 10, rowspan = 2)
fw_table_frame = ttk.Frame(tab2)
fw_table_frame.grid(column = 0,  row = 2, columnspan = 4)
# Constructing vertical scrollbar 
fw_table_scroll = ttk.Scrollbar(fw_table_frame, orient ="vertical") 
fw_table_scroll.pack(side ='right', fill='y')
# fw table # 
fw_table = ttk.Treeview(fw_table_frame, selectmode ='browse', height = 20, yscrollcommand = fw_table_scroll.set, columns = ("1", "2", "3", "4", "5"), show = 'headings') 
fw_table.pack(side ='left')
# Configuring scrollbar 
fw_table_scroll.configure(command = fw_table.yview) 
# Assigning the width and anchor to the respective columns 
fw_table.column("1", width = 100, anchor ='c') 
fw_table.column("2", width = 100, anchor ='c') 
fw_table.column("3", width = 100, anchor ='c') 
fw_table.column("4", width = 100, anchor ='c') 
fw_table.column("5", width = 100, anchor ='c') 
# Assigning the heading names to the respective columns 
fw_table.heading("1", text ="Customer") 
fw_table.heading("2", text ="Item Code") 
fw_table.heading("3", text ="A")
fw_table.heading("4", text ="B")
fw_table.heading("5", text ="%")


# tab 3 #
# frame for info
lw_info_frame = ttk.Frame(tab3)
lw_info_frame.grid(column = 0,  row = 0)
ttk.Label(lw_info_frame,  text ="Customer").grid(column = 0,  row = 0, padx = (5,0), pady = (10,0), sticky=W)
ttk.Label(lw_info_frame,  text ="Kedai Emas Sangat Panjang").grid(column = 0, row = 1, padx = (5,0),pady = (10,0), sticky=W)
ttk.Label(lw_info_frame,  text ="Item Code").grid(column = 0,  row = 2, padx = (5,0), pady = (10,0), sticky=W)
ttk.Label(lw_info_frame,  text ="Clicked Item Code").grid(column = 0,  row = 3, padx = (5,0),pady = (10,0), sticky=W)
# frame for entry and calculation
lw_entry_frame = ttk.Frame(tab3)
lw_entry_frame.grid(column = 1,  row = 0)
ttk.Label(lw_entry_frame,  text ="A").grid(column = 0,  row = 1, padx = 10)
ttk.Label(lw_entry_frame,  text ="B").grid(column = 0,  row = 2, padx = 10)
ttk.Label(lw_entry_frame,  text ="Last Weight").grid(column = 1,  row = 0)
lwa = IntVar()
lwa_entry = Entry(lw_entry_frame, textvariable = lwa)
lwa_entry.grid(column = 1,  row = 1)
lwb = IntVar()
lwb_entry = Entry(lw_entry_frame, textvariable = lwb)
lwb_entry.grid(column = 1,  row = 2)
ttk.Label(lw_entry_frame,  text ="/").grid(column = 2,  row = 1, padx = 5)
ttk.Label(lw_entry_frame,  text ="/").grid(column = 2,  row = 2, padx = 5)
ttk.Label(lw_entry_frame,  text ="First Weight").grid(column = 3,  row = 0)
lwfwa = IntVar()
lwfwa_entry = Entry(lw_entry_frame, textvariable = lwfwa, state = 'disabled')
lwfwa_entry.grid(column = 3,  row = 1)
lwfwb = IntVar()
lwfwb_entry = Entry(lw_entry_frame, textvariable = lwfwb, state = 'disabled')
lwfwb_entry.grid(column = 3,  row = 2)
ttk.Label(lw_entry_frame,  text ="=").grid(column = 4,  row = 1, padx = 5)
ttk.Label(lw_entry_frame,  text ="=").grid(column = 4,  row = 2, padx = 5)
ra = IntVar()
ra_entry = Entry(lw_entry_frame, textvariable = ra, state = 'disabled')
ra_entry.grid(column = 5,  row = 1)
rb = IntVar()
rb_entry = Entry(lw_entry_frame, textvariable = rb, state = 'disabled')
rb_entry.grid(column = 5,  row = 2)
ttk.Label(lw_entry_frame,  text ="/2").grid(column = 6,  row = 1, padx = 5, rowspan = 2)
avg_result = IntVar()
avg_result_entry = Entry(lw_entry_frame, textvariable = avg_result, state = 'disabled')
avg_result_entry.grid(column = 7,  row = 1, rowspan = 2)
ttk.Label(lw_entry_frame,  text ="Loss").grid(column = 8,  row = 0, padx = 5)
loss = IntVar()
loss_label = Label(lw_entry_frame, textvariable = loss)
loss_label.grid(column = 8,  row = 1, rowspan = 2)
ttk.Label(lw_entry_frame,  text ="=").grid(column = 9,  row = 1, rowspan = 2, padx = 5)
ttk.Label(lw_entry_frame,  text ="Result").grid(column = 11,  row = 0)
result = IntVar()
result_entry = Entry(lw_entry_frame, textvariable = result, state = 'disabled')
result_entry.grid(column = 11,  row = 1, rowspan = 2)
#edit button
lw_edit_frame = ttk.Frame(tab3)
lw_edit_frame.grid(column = 2,  row = 0)
edit_lw = Button(lw_edit_frame, text = 'EDIT')
edit_lw.grid(column = 0,  row = 0, padx = 10, ipadx = 10, ipady = 10, rowspan = 2)
# Last Weight Table
lw_table_frame = ttk.Frame(tab3)
lw_table_frame.grid(column = 0,  row = 1, columnspan = 11, pady = 20)
# Constructing vertical scrollbar 
lw_table_scroll = ttk.Scrollbar(lw_table_frame, orient ="vertical") 
lw_table_scroll.pack(side ='right', fill='y')
# lw table # 
lw_table = ttk.Treeview(lw_table_frame, selectmode ='browse', height = 20, yscrollcommand = lw_table_scroll.set, columns = ("1", "2", "3", "4", "5", "6", "7", "8"), show = 'headings') 
lw_table.pack(side ='left')
# Configuring scrollbar 
lw_table_scroll.configure(command = lw_table.yview) 
# Assigning the width and anchor to the respective columns 
lw_table.column("1", width = 100, anchor ='c') 
lw_table.column("2", width = 100, anchor ='c') 
lw_table.column("3", width = 100, anchor ='c') 
lw_table.column("4", width = 100, anchor ='c') 
lw_table.column("5", width = 100, anchor ='c') 
lw_table.column("6", width = 100, anchor ='c') 
lw_table.column("7", width = 100, anchor ='c') 
lw_table.column("8", width = 100, anchor ='c') 
# Assigning the heading names to the respective columns 
lw_table.heading("1", text ="Customer") 
lw_table.heading("2", text ="Item Code") 
lw_table.heading("3", text ="First A")
lw_table.heading("4", text ="First B")
lw_table.heading("5", text ="Last A")
lw_table.heading("6", text ="Last B")
lw_table.heading("7", text ="%")
lw_table.heading("8", text ="Result")

root.config(menu=menubar)
root.mainloop()  