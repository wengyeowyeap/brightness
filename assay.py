from tkinter import *  
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from ttkthemes import ThemedTk
import datetime
import mysql.connector
from decouple import config

today = datetime.date.today()
now = datetime.datetime.now()
colorset = True
formcode = 0
mainselected = []

def printersetting():
  printersetting = Toplevel(root)
  printersetting.grab_set()
  button = Button(printersetting, text="CL")
  button.pack()

def assaysetting():
  assaysetting = Toplevel(root)
  assaysetting.grab_set()
  # Tab #
  tabControl = ttk.Notebook(assaysetting) 
  tab1 = ttk.Frame(tabControl) 
  tab2 = ttk.Frame(tabControl) 
  tab3 = ttk.Frame(tabControl) 
  tab4 = ttk.Frame(tabControl) 
  tabControl.add(tab1, text ='User') 
  tabControl.add(tab2, text ='Company Info')
  tabControl.add(tab3, text ='Loss') 
  tabControl.pack(expand = 1, fill ="both")

  #tab 1 - User
  ttk.Label(tab1,  text ="Username").grid(column = 0,  row = 0, padx = 10)
  username = StringVar()
  ttk.Label(tab1,  textvariable = username).grid(column = 1,  row = 0, padx = 10)
  ttk.Label(tab1,  text ="Change Password").grid(column = 0,  row = 1, padx = 10)
  ttk.Label(tab1,  text ="Current Password").grid(column = 0,  row = 2, padx = 10)
  current_password = StringVar()
  current_password_entry = Entry(tab1, textvariable = current_password, show='*').grid(column = 1,  row = 2)
  ttk.Label(tab1,  text ="New Password").grid(column = 0,  row = 3, padx = 10)
  new_password = StringVar()
  new_password_entry = Entry(tab1, textvariable = new_password, show='*').grid(column = 1,  row = 3)
  ttk.Label(tab1,  text ="Confirm New Password").grid(column = 0,  row = 4, padx = 10)
  confirm_new_password = StringVar()
  confirm_new_password_entry = Entry(tab1, textvariable = confirm_new_password, show='*').grid(column = 1,  row = 4)
  submit_password = ttk.Button(tab1, text = 'Submit')
  submit_password.grid(column = 0,  row = 5, ipadx = 10, ipady = 10, columnspan = 2)  

  #tab 2 - Company Info
  ttk.Label(tab2,  text ="Company Name").grid(column = 0,  row = 0, padx = 10)
  company_name = StringVar()
  company_name_entry = Entry(tab2, textvariable = company_name).grid(column = 1,  row = 0)
  ttk.Label(tab2,  text ="Address").grid(column = 0,  row = 1, padx = 10)
  address = StringVar()
  address_entry = Entry(tab2, textvariable = address).grid(column = 1,  row = 1)
  ttk.Label(tab2,  text ="Contact").grid(column = 0,  row = 2, padx = 10)
  contact = StringVar()
  contact_entry = Entry(tab2, textvariable = contact).grid(column = 1,  row = 2)
  ttk.Label(tab2,  text ="Terms & Condition").grid(column = 0,  row = 3, padx = 10)
  tandc1 = StringVar()
  tandc1_entry = Entry(tab2, textvariable = tandc1).grid(column = 1,  row = 3)
  tandc2 = StringVar()
  tandc2_entry = Entry(tab2, textvariable = tandc2).grid(column = 1,  row = 4)
  tandc3 = StringVar()
  tandc3_entry = Entry(tab2, textvariable = tandc3).grid(column = 1,  row = 5)

  ttk.Label(tab2,  text ="Email").grid(column = 0,  row = 6, padx = 10)
  email = StringVar()
  email_entry = Entry(tab2, textvariable = email).grid(column = 1,  row = 6)
  ttk.Label(tab2,  text ="Email Password").grid(column = 0,  row = 7, padx = 10)
  password = StringVar()
  password_entry = Entry(tab2, textvariable = password, show='*').grid(column = 1,  row = 7)

  submit_company_profile = ttk.Button(tab2, text = 'Submit')
  submit_company_profile.grid(column = 0,  row = 8, padx = 10, pady = 10, ipadx = 10, ipady = 10, columnspan = 2) 

  #tab3 - Loss
  # create frame for input (add/edit)
  loss_input_frame = Frame(tab3)
  loss_input_frame.grid(column = 0,  row = 0)
  low = StringVar()
  low_entry = Entry(loss_input_frame, textvariable = low).grid(column = 0,  row = 0)
  ttk.Label(loss_input_frame,  text ="≥ Result ≥").grid(column = 1,  row = 0, padx = 10)
  high = StringVar()
  high_entry = Entry(loss_input_frame, textvariable = high).grid(column = 2,  row = 0)
  ttk.Label(loss_input_frame,  text ="Loss %").grid(column = 0,  row = 2, padx = 10)
  contact = StringVar()
  contact_entry = Entry(loss_input_frame, textvariable = contact).grid(column = 1,  row = 2, columnspan = 3)
  new_loss = ttk.Button(loss_input_frame, text = 'NEW')
  new_loss.grid(column = 0,  row = 3, padx = 10, pady = 10, ipadx = 10, ipady = 10, columnspan = 3) 
  edit_loss = ttk.Button(loss_input_frame, text = 'EDIT')
  edit_loss.grid(column = 0,  row = 4, padx = 10, pady = 10, ipadx = 10, ipady = 10, columnspan = 3) 
  delete_loss = ttk.Button(loss_input_frame, text = 'DELETE')
  delete_loss.grid(column = 0,  row = 5, padx = 10, pady = 10, ipadx = 10, ipady = 10, columnspan = 3)

  # create frame for loss table
  loss_table_frame = Frame(tab3)
  loss_table_frame.grid(column = 1,  row = 0)
  # Constructing vertical scrollbar 
  loss_table_scroll = ttk.Scrollbar(loss_table_frame, orient ="vertical") 
  loss_table_scroll.pack(side ='right', fill='y')
  # loss table # 
  loss_table = ttk.Treeview(loss_table_frame, selectmode ='browse', height = 20, yscrollcommand = loss_table_scroll.set, columns = ("1", "2", "3"), show = 'headings') 
  loss_table.pack(side ='left')
  # Configuring scrollbar 
  loss_table_scroll.configure(command = loss_table.yview) 
  # Assigning the width and anchor to the respective columns 
  loss_table.column("1", width = 100, anchor ='c') 
  loss_table.column("2", width = 100, anchor ='c') 
  loss_table.column("3", width = 100, anchor ='c') 
  # Assigning the heading names to the respective columns 
  loss_table.heading("1", text ="Minimum") 
  loss_table.heading("2", text ="Maximum") 
  loss_table.heading("3", text ="Loss %")

class NewFormCode(Toplevel): 
  def __init__(self, master = None): 
    super().__init__(master = master) 
    self.title("New Formcode")
    self.geometry("280x450") 
    self.grab_set()
    def setformcode():
      global formcode
      mycursor = assaydb.cursor()
      mycursor.execute("SELECT * FROM assayresult ORDER BY formcode DESC LIMIT 1")
      myresult = mycursor.fetchall()
      if myresult:
        for x in myresult:
          formcode = x[17] + 1
          showformcode.set(formcode)
      else:
        formcode = 1

    def nextformcode():
      setformcode()
      #clear boxes and refocus
      item_code.set("") 
      sample_weight.set("")
      customer.set("")
      customer_entry.focus_set()

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
            data = cl
            update(data)
            lb.pack_forget()
        else: 
            data = [] 
            for item in cl: 
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

    def focusweight(event):
      sample_weight_entry.focus_set() 

    def submit(event): 
      code=item_code_entry.get()
      weight=sample_weight_entry.get()
      customer=customer_entry.get()
      print("The code is : " + code)
      print("The weight is : " + weight)
      print(customer)
      # search customer id
      sql = f"SELECT * FROM user WHERE name ='{customer}'"      
      mycursor.execute(sql)
      customerselected = mycursor.fetchone()
      #insert record
      sql = "INSERT INTO assayresult (created, modified, itemcode, sampleweight, color, customer, formcode) VALUES (%s, %s, %s, %s, %s, %s, %s)"
      val = (now, now, code, weight, colorset, customerselected[0], formcode)
      mycursor.execute(sql, val)
      assaydb.commit()
      for i in left_table.get_children():
        left_table.delete(i)
      loadmainlefttable()
      for i in right_table.get_children():
        right_table.delete(i)
      loadmainrighttable()
      #clear boxes
      item_code.set("") 
      sample_weight.set("")
      item_code_entry.focus_set()

    # get customer from db
    mycursor.execute("SELECT * FROM user WHERE role ='customer'")
    myresult = mycursor.fetchall()
    cl = []
    if myresult:
      for x in myresult:
        cl.append(x[9])
    
    showformcode = StringVar()
    setformcode()    
    #New Formcode Button
    new_formcode = Button(self, text = 'New Formcode', command = nextformcode)
    new_formcode.grid(column = 0,  row = 0, padx = 10, pady = 10, ipadx = 5, ipady = 5)
    #Close Button
    close_new_record = Button(self, text = 'Close', command = self.destroy)
    close_new_record.grid(column = 1,  row = 0, padx = 10, pady = 10, ipadx = 5, ipady = 5)

    Label(self,  text ="Form Code: ").grid(column = 0,  row = 1, padx = (5,0), pady = (10,0))
    Label(self,  textvariable = showformcode).grid(column = 1,  row = 1, pady = (10,0))
    Label(self,  text ="Date: ").grid(column = 0,  row = 2, padx = (15,0), pady = (10,0))
    showdate = StringVar()
    showdate.set(today.strftime("%d/%m/%Y"))
    Label(self,  textvariable = showdate).grid(column = 1,  row = 2, pady = (10,0))
    Label(self,  text ="Item Code: ").grid(column = 0,  row = 4, padx = (5,0), pady = (10,0))
    item_code = StringVar()
    item_code_entry = Entry(self, textvariable = item_code)
    item_code_entry.grid(column = 1,  row = 4)
    item_code_entry.bind('<Return>', focusweight)
    Label(self,  text ="Sample Weight (g): ").grid(column = 0,  row = 5, padx = (5,0), pady = 10)
    sample_weight = DoubleVar()
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
    update(cl) 
    lb.bind("<KeyRelease-Return>", selectcustomer)
    lb.bind("<ButtonRelease-1>", selectcustomer)
    lb.bind("<Double-Button-1>", selectcustomer)

class NewRound(Toplevel): 
  def __init__(self, master = None): 
    super().__init__(master = master) 
    self.title("New Formcode")
    self.geometry("280x450") 
    self.grab_set()
    def setformcode():
      global formcode
      mycursor = assaydb.cursor()
      mycursor.execute("SELECT * FROM assayresult ORDER BY formcode DESC LIMIT 1")
      myresult = mycursor.fetchall()
      if myresult:
        for x in myresult:
          formcode = x[17] + 1
          showformcode.set(formcode)
      else:
        formcode = 1
    def nextformcode():
      setformcode()
      #clear boxes and refocus
      item_code.set("") 
      sample_weight.set("")
      customer.set("")
      customer_entry.focus_set()
    def changecolor():
      global colorset
      if colorset == True:
        colorset = False
      else:
        colorset = True
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
            data = cl
            update(data)
            lb.pack_forget()
        else: 
            data = [] 
            for item in cl: 
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
    def focusweight(event):
      sample_weight_entry.focus_set() 
    def submit(event): 
      code=item_code_entry.get()
      weight=sample_weight_entry.get()
      customer=customer_entry.get()
      print("The code is : " + code)
      print("The weight is : " + weight)
      print(customer)
      # search customer id
      sql = f"SELECT * FROM user WHERE name ='{customer}'"      
      mycursor.execute(sql)
      customerselected = mycursor.fetchone()
      #insert record
      sql = "INSERT INTO assayresult (created, modified, itemcode, sampleweight, color, customer, formcode) VALUES (%s, %s, %s, %s, %s, %s, %s)"
      val = (now, now, code, weight, colorset, customerselected[0], formcode)
      mycursor.execute(sql, val)
      assaydb.commit()
      for i in left_table.get_children():
        left_table.delete(i)
      loadmainlefttable()
      for i in right_table.get_children():
        right_table.delete(i)
      loadmainrighttable()
      #clear boxes
      item_code.set("") 
      sample_weight.set("")
      item_code_entry.focus_set()
    # get customer from db
    mycursor.execute("SELECT * FROM user WHERE role ='customer'")
    myresult = mycursor.fetchall()
    cl = []
    if myresult:
      for x in myresult:
        cl.append(x[9])
    
    showformcode = StringVar()
    setformcode()
    changecolor()
    #New Formcode Button
    new_formcode = Button(self, text = 'New Formcode', command = nextformcode)
    new_formcode.grid(column = 0,  row = 0, padx = 10, pady = 10, ipadx = 5, ipady = 5)
    #Close Button
    close_new_record = Button(self, text = 'Close', command = self.destroy)
    close_new_record.grid(column = 1,  row = 0, padx = 10, pady = 10, ipadx = 5, ipady = 5)

    Label(self,  text ="Form Code: ").grid(column = 0,  row = 1, padx = (5,0), pady = (10,0))
    Label(self,  textvariable = showformcode).grid(column = 1,  row = 1, pady = (10,0))
    Label(self,  text ="Date: ").grid(column = 0,  row = 2, padx = (15,0), pady = (10,0))
    showdate = StringVar()
    showdate.set(today.strftime("%d/%m/%Y"))
    Label(self,  textvariable = showdate).grid(column = 1,  row = 2, pady = (10,0))
    Label(self,  text ="Item Code: ").grid(column = 0,  row = 4, padx = (5,0), pady = (10,0))
    item_code = StringVar()
    item_code_entry = Entry(self, textvariable = item_code)
    item_code_entry.grid(column = 1,  row = 4)
    item_code_entry.bind('<Return>', focusweight)
    Label(self,  text ="Sample Weight (g): ").grid(column = 0,  row = 5, padx = (5,0), pady = 10)
    sample_weight = DoubleVar()
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
    update(cl) 
    lb.bind("<KeyRelease-Return>", selectcustomer)
    lb.bind("<ButtonRelease-1>", selectcustomer)
    lb.bind("<Double-Button-1>", selectcustomer)

class EditRecord(Toplevel): 
  def __init__(self, master = None): 
    super().__init__(master = master) 
    self.title("Edit Record")
    self.geometry("280x450") 
    # Function for checking the key pressed and updating the listbox 

    def focusweight(event):
      print(sample_weight_entry)
      sample_weight_entry.focus_set() 

    def focusok(event):
      print(editok)
      editok.focus_set() 

    def editassay(): 
      code=item_code_entry.get()
      weight=sample_weight_entry.get()
      print("The code is : " + code)
      print("The weight is : " + weight)
      global mainselected
      id = mainselected[8]
      global now
      #update record using id
      sql = "UPDATE assayresult SET itemcode = %s, sampleweight = %s, modified = %s WHERE id = %s"
      val = (code, weight, now, id)
      mycursor.execute(sql, val)
      assaydb.commit()
      for i in left_table.get_children():
        left_table.delete(i)
      loadmainlefttable()
      for i in right_table.get_children():
        right_table.delete(i)
      loadmainrighttable()
      self.destroy()

    global mainselected
    formcodee = StringVar()
    dateee = StringVar()
    customere = StringVar()
    formcodee.set(mainselected[0])
    dateee.set(mainselected[6])
    customere.set(mainselected[7])
    Label(self,  text ="Customer: ").grid(column = 0,  row = 1, padx = (5,0), pady = (10,0))
    Label(self,  textvariable = customere).grid(column = 1,  row = 1, pady = (10,0))
    Label(self,  text ="Date: ").grid(column = 0,  row = 2, padx = (15,0), pady = (10,0))
    Label(self,  textvariable =dateee).grid(column = 1,  row = 2, pady = (10,0))
    Label(self,  text ="Form Code: ").grid(column = 0,  row = 3, padx = (5,0), pady = (10,0))
    Label(self,  textvariable = formcodee).grid(column = 1,  row = 3, pady = (10,0))
    Label(self,  text ="Item Code: ").grid(column = 0,  row = 4, padx = (5,0), pady = (10,0))
    item_code = StringVar()
    item_code.set(mainselected[1])
    item_code_entry = Entry(self, textvariable = item_code)
    item_code_entry.grid(column = 1,  row = 4)
    item_code_entry.bind('<Return>', focusweight)
    Label(self,  text ="Sample Weight (g): ").grid(column = 0,  row = 5, padx = (5,0), pady = 10)
    sample_weight = DoubleVar()
    sample_weight.set(mainselected[2])
    sample_weight_entry = Entry(self, textvariable = sample_weight)
    sample_weight_entry.grid(column = 1,  row = 5)
    sample_weight_entry.bind('<Return>', focusok)
    editok = Button(self, text = 'Save', command = editassay)
    editok.grid(column = 0,  row = 6, ipadx = 5, ipady = 5)
    editcancel = Button(self, text = 'Cancel', command = self.destroy).grid(column = 1,  row = 6, ipadx = 5, ipady = 5)

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
    sample_weight = DoubleVar()
    sample_weight_entry = Entry(self, textvariable = sample_weight)
    sample_weight_entry.grid(column = 1,  row = 5)
    sample_weight_entry.bind('<Return>', submit) #trigger submit function when enter is pressed

def loadmainlefttable():
  mycursor.execute("SELECT assayresult.formcode AS formcode, assayresult.created AS created, user.name AS customer, assayresult.color AS color, assayresult.itemcode AS itemcode, assayresult.sampleweight AS sampleweight, assayresult.id AS id FROM assayresult INNER JOIN user ON assayresult.customer = user.id ORDER BY assayresult.formcode")
  dbresult = mycursor.fetchall()
  loadlefttable = []
  for x in dbresult:
    newx = list(x)
    if newx[3] == 1:
      newx[3] = True
    else:
      newx[3] = False
    if loadlefttable:
      if newx[0] == loadlefttable[-1][0]:
        loadlefttable[-1][1] += 1
      else:
        newx.insert(1,int(1))
        newx[2] = newx[2].strftime("%d/%m/%Y")
        loadlefttable.append(newx)
    else:
      newx.insert(1,int(1))
      newx[2] = newx[2].strftime("%d/%m/%Y")
      loadlefttable.append(newx)
  for record in loadlefttable:
    if record[4]:
      left_table.insert("", 'end', text ="L1", values =record, tags = ("true"))
    else:
      left_table.insert("", 'end', text ="L1", values =record, tags = ("false"))
  left_table.tag_configure('true', background='lightcyan')
  left_table.tag_configure('false', background='plum')

def loadmainrighttable():
  mycursor.execute("SELECT assayresult.formcode AS formcode, assayresult.itemcode AS itemcode, assayresult.sampleweight AS sampleweight, assayresult.samplereturn AS samplereturn, assayresult.finalresult AS finalresult, assayresult.color AS color, assayresult.created AS created, user.name AS customer, assayresult.id AS id FROM assayresult INNER JOIN user ON assayresult.customer = user.id ORDER BY assayresult.formcode")
  dbresult = mycursor.fetchall()
  loadrighttable = []
  for x in dbresult:
    newx = list(x)
    newx[6] = newx[6].strftime("%d/%m/%Y")
    if newx[5] == 1:
      newx[5] = True
    else:
      newx[5] = False
    loadrighttable.append(newx)
  for record in loadrighttable:
    if record[5]:
      right_table.insert("", 'end', text ="L1", values =record, tags = ("true"))
    else:
      right_table.insert("", 'end', text ="L1", values =record, tags = ("false"))
  right_table.tag_configure('true', background='lightcyan')
  right_table.tag_configure('false', background='plum')

def displaymainfromleft(a):
  curItem = left_table.focus()
  print(left_table.item(curItem).get('values'))
  global mainselected
  mainselected = left_table.item(curItem).get('values')
  selectedfc.set(mainselected[0])
  selectedc.set(mainselected[3])
  selectedd.set(mainselected[2])
  selectedic.set(mainselected[5])
  selectedsw.set(mainselected[6])

def displaymainfromright(a):
  curItem = right_table.focus()
  print(right_table.item(curItem).get('values'))
  global mainselected
  mainselected = right_table.item(curItem).get('values')
  selectedfc.set(mainselected[0])
  selectedc.set(mainselected[7])
  selectedd.set(mainselected[6])
  selectedic.set(mainselected[1])
  selectedsw.set(mainselected[2])

class DeleteRecord(Toplevel): 
  def __init__(self, master = None): 
    super().__init__(master = master) 
    self.title("Delete Item")
    self.grab_set()

    def deleteassay():
      global mainselected
      if len(mainselected) <= 8:
        sql = f"DELETE FROM assayresult WHERE formcode = '{mainselected[0]}'"
        mycursor.execute(sql)
        assaydb.commit()
        for i in left_table.get_children():
          left_table.delete(i)
          loadmainlefttable()
        for i in right_table.get_children():
          right_table.delete(i)
        loadmainrighttable()
        self.destroy()
      else:
        sql = f"DELETE FROM assayresult WHERE id = '{mainselected[8]}'"
        mycursor.execute(sql)
        assaydb.commit()
        for i in left_table.get_children():
          left_table.delete(i)
          loadmainlefttable()
        for i in right_table.get_children():
          right_table.delete(i)
        loadmainrighttable()
        self.destroy()

    deleteq = StringVar()
    deleteitemverify = StringVar()
    global mainselected
    if len(mainselected) <= 8:
      deleteq.set(f"Delete all item under this formcode?")
      deleteitemverify.set(f"Customer: {mainselected[3]}\nFormcode: {mainselected[0]}\nTotal Item: {mainselected[1]}")
    else:
      deleteq.set(f"Are you sure you want to delete this item?")
      deleteitemverify.set(f"Customer: {mainselected[7]}\nFormcode: {mainselected[0]}\nItemcode: {mainselected[1]}\n")
    
    Label(self,  textvariable = deleteq).grid(column = 0,  row = 0, padx=10, columnspan = 2)
    Label(self,  textvariable = deleteitemverify).grid(column = 0,  row = 1, padx=10, columnspan = 2)

    deleteok = Button(self, text = 'Ok', command = deleteassay).grid(column = 0,  row = 2, ipadx = 5, ipady = 5)
    deletecancel = Button(self, text = 'Cancel', command = self.destroy).grid(column = 1,  row = 2, ipadx = 5, ipady = 5)

root = ThemedTk(theme="clearlooks")
root.title("Brightness Assay")

assaydb = mysql.connector.connect(
          host = config('MYSQLHOST'),
          user = config('MYSQLUSER'),
          passwd = config('MYSQLPW'),
          database="assay"
        )

print(assaydb)
mycursor = assaydb.cursor()
# Menu #
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Menu", menu=filemenu)
filemenu.add_command(label="Printer Setting", command=printersetting)
filemenu.add_command(label="Assay Setting", command=assaysetting)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

# Tab #
tabControl = ttk.Notebook(root) 
tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl) 
tab3 = ttk.Frame(tabControl) 
tab4 = ttk.Frame(tabControl) 
tab5 = ttk.Frame(tabControl) 
tab6 = ttk.Frame(tabControl) 
tabControl.add(tab1, text ='Main') 
tabControl.add(tab2, text ='First Weight')
tabControl.add(tab3, text ='Last Weight') 
tabControl.add(tab4, text ='Sample Return') 
tabControl.add(tab5, text ='History') 
tabControl.add(tab6, text ='Customer') 
tabControl.pack(expand = 1, fill ="both") 

#tab 1#
ttk.Label(tab1,  text ="Form Code: ").grid(column = 0,  row = 0, padx = (5,0), pady = (10,0))
selectedfc = StringVar()
ttk.Label(tab1,  textvariable = selectedfc).grid(column = 1,  row = 0, pady = (10,0))
ttk.Label(tab1,  text ="Customer: ").grid(column = 2,  row = 0, padx = (15,0), pady = (10,0))
selectedc = StringVar()
ttk.Label(tab1,  textvariable = selectedc).grid(column = 3,  row = 0, pady = (10,0))
ttk.Label(tab1,  text ="Date: ").grid(column = 4,  row = 0, padx = (15,0), pady = (10,0))
selectedd = StringVar()
ttk.Label(tab1,  textvariable = selectedd).grid(column = 5,  row = 0, pady = (10,0))
ttk.Label(tab1,  text ="Item Code: ").grid(column = 0,  row = 1, padx = (5,0), pady = (10,0))
selectedic = StringVar()
ttk.Label(tab1,  textvariable = selectedic).grid(column = 1,  row = 1, padx = (5,0), pady = (10,0))
ttk.Label(tab1,  text ="Sample Weight (g): ").grid(column = 2,  row = 1, padx = (5,0), pady = 10)
selectedsw = StringVar()
ttk.Label(tab1,  textvariable = selectedsw).grid(column = 3,  row = 1, padx = (5,0), pady = 10)

# tab1 button #
new_record = ttk.Button(tab1, text = 'NEW')
new_record.grid(column = 6,  row = 0, padx = 10, pady = 10)
new_record.bind("<Button>", lambda e: NewFormCode(root))
new_round = ttk.Button(tab1, text = 'NEW ROUND')
new_round.grid(column = 6,  row = 1, padx = 10, pady = 10)
new_round.bind("<Button>", lambda e: NewRound(root))
delete_record = ttk.Button(tab1, text = 'DELETE')
delete_record.grid(column = 7,  row = 0, padx = 10, pady = 10)
delete_record.bind("<Button>", lambda e: DeleteRecord(root))
edit_record = ttk.Button(tab1, text = 'EDIT')
edit_record.grid(column = 8,  row = 0, padx = 10, pady = 10)
edit_record.bind("<Button>", lambda e: EditRecord(root)) 
add_to_formcode = ttk.Button(tab1, text = 'ADD')
add_to_formcode.grid(column = 9,  row = 0, padx = 10, pady = 10)
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
loadmainlefttable()
left_table.bind('<<TreeviewSelect>>', displaymainfromleft)
# create a frame in tab 1 for right table
right_table_frame = ttk.Frame(tab1)
right_table_frame.grid(column = 4,  row = 2, columnspan = 4)
# Constructing vertical scrollbar 
right_table_scroll = ttk.Scrollbar(right_table_frame, orient ="vertical") 
right_table_scroll.pack(side ='right', fill='y')
# right table # 
right_table = ttk.Treeview(right_table_frame, selectmode ='browse', height = 20, yscrollcommand = right_table_scroll.set, columns = ("1", "2", "3", "4","5"), show = 'headings') 
right_table.pack(side ='left')
# Configuring scrollbar 
right_table_scroll.configure(command = right_table.yview)
# Assigning the width and anchor to the respective columns 
right_table.column("1", width = 100, anchor ='c') 
right_table.column("2", width = 100, anchor ='c') 
right_table.column("3", width = 100, anchor ='c') 
right_table.column("4", width = 100, anchor ='c') 
right_table.column("5", width = 100, anchor ='c')
# Assigning the heading names to the respective columns 
right_table.heading("1", text ="Form Code") 
right_table.heading("2", text ="Item") 
right_table.heading("3", text ="Sample Weight")
right_table.heading("4", text ="Sample Return")
right_table.heading("5", text ="Result")
# Inserting the items and their features to the columns built 
loadmainrighttable()
right_table.bind('<<TreeviewSelect>>', displaymainfromright)
# tab 2 first weight #
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
edit_fw = ttk.Button(tab2, text = 'EDIT')
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


# tab 3 - first weight #
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
ttk.Label(lw_entry_frame,  text ="-").grid(column = 8,  row = 1, padx = 5, rowspan = 2)
ttk.Label(lw_entry_frame,  text ="Loss").grid(column = 9,  row = 0, padx = 5)
loss = IntVar()
loss_label = Label(lw_entry_frame, textvariable = loss)
loss_label.grid(column = 9,  row = 1, rowspan = 2)
ttk.Label(lw_entry_frame,  text ="=").grid(column = 10,  row = 1, rowspan = 2, padx = 5)
ttk.Label(lw_entry_frame,  text ="Result").grid(column = 11,  row = 0)
result = IntVar()
result_entry = Entry(lw_entry_frame, textvariable = result, state = 'disabled')
result_entry.grid(column = 11,  row = 1, rowspan = 2)
#edit button
lw_edit_frame = ttk.Frame(tab3)
lw_edit_frame.grid(column = 2,  row = 0)
edit_lw = ttk.Button(lw_edit_frame, text = 'EDIT')
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

# tab 4 - sample return#
# frame for info
sr_info_frame = ttk.Frame(tab4)
sr_info_frame.grid(column = 0,  row = 0)
ttk.Label(sr_info_frame,  text ="Customer").grid(column = 0,  row = 0, padx = (5,0), pady = (10,0), sticky=W)
ttk.Label(sr_info_frame,  text ="Kedai Emas Sangat Panjang").grid(column = 0, row = 1, padx = (5,0),pady = (10,0), sticky=W)
ttk.Label(sr_info_frame,  text ="Item Code").grid(column = 1,  row = 0, padx = (5,0), pady = (10,0), sticky=W)
ttk.Label(sr_info_frame,  text ="Clicked Item Code").grid(column = 1,  row = 1, padx = (5,0),pady = (10,0), sticky=W)
ttk.Label(sr_info_frame,  text ="Sample Weight (g)").grid(column = 2,  row = 0, padx = (5,0), pady = (10,0), sticky=W)
ttk.Label(sr_info_frame,  text ="1.36").grid(column = 2,  row = 1, padx = (5,0),pady = (10,0), sticky=W)
ttk.Label(sr_info_frame,  text ="Sample Return (g)").grid(column = 3,  row = 0, padx = (5,0), pady = (10,0), sticky=W)
sr = DoubleVar()
sr_entry = Entry(sr_info_frame, textvariable = sr)
sr_entry.grid(column = 3,  row = 1)
# Sample Return Table
sr_table_frame = ttk.Frame(tab4)
sr_table_frame.grid(column = 0,  row = 1, columnspan = 3, pady = 20)
# Constructing vertical scrollbar 
sr_table_scroll = ttk.Scrollbar(sr_table_frame, orient ="vertical") 
sr_table_scroll.pack(side ='right', fill='y')
# sr table # 
sr_table = ttk.Treeview(sr_table_frame, selectmode ='browse', height = 20, yscrollcommand = sr_table_scroll.set, columns = ("1", "2", "3", "4", "5", "6"), show = 'headings') 
sr_table.pack(side ='left')
# Configuring scrollbar 
sr_table_scroll.configure(command = sr_table.yview) 
# Assigning the width and anchor to the respective columns 
sr_table.column("1", width = 100, anchor ='c') 
sr_table.column("2", width = 100, anchor ='c') 
sr_table.column("3", width = 100, anchor ='c') 
sr_table.column("4", width = 100, anchor ='c') 
sr_table.column("5", width = 100, anchor ='c') 
sr_table.column("6", width = 100, anchor ='c') 
# Assigning the heading names to the respective columns 
sr_table.heading("1", text ="Customer") 
sr_table.heading("2", text ="Form Code")
sr_table.heading("3", text ="Item Code") 
sr_table.heading("4", text ="Result")
sr_table.heading("5", text ="Sample Weight")
sr_table.heading("6", text ="Sample Return")

# tab 5 - search history
# frame for info
filter_frame = ttk.Frame(tab5)
filter_frame.grid(column = 0,  row = 0, sticky = N)
ttk.Label(filter_frame,  text ="Customer").grid(column = 0,  row = 0, padx = (5,0), pady = (10,0), sticky=W)
# Function for checking the key pressed and updating the listbox 
def checkkeytab5(event): 
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
        updatetab5(data)
        lb.pack_forget()
    else: 
        data = [] 
        for item in l: 
            if value.lower() in item.lower(): 
                data.append(item)
                updatetab5(data)
                lb.pack()
def updatetab5(data): 
  # clear previous data 
  lb.delete(0, 'end') 
  # put new data 
  for item in data: 
      lb.insert('end', item) 
def selectcustomertab5(event):
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
# Combobox creation
# create a frame 
customer_input_frame = Frame(filter_frame)
customer_input_frame.grid(column = 0,  row = 1)
# If customer not in list, pop up add new customer fw_pct_frame
customer = StringVar() 
customer_entry = Entry(customer_input_frame, textvariable=customer) 
customer_entry.pack() 
customer_entry.bind('<KeyRelease>', checkkeytab5) 
#creating list box 
lb = Listbox(customer_input_frame)
lb.pack()
lb.pack_forget()
updatetab5(l) 
lb.bind("<KeyRelease-Return>", selectcustomertab5)
lb.bind("<ButtonRelease-1>", selectcustomertab5)
lb.bind("<Double-Button-1>", selectcustomertab5)
ttk.Label(filter_frame,  text ="Item Code").grid(column = 0,  row = 2, padx = (5,0), pady = (10,0), sticky=W)
search_code = StringVar() 
search_code_entry = Entry(filter_frame, textvariable=search_code).grid(column = 0,  row = 3, padx = (5,0), pady = (10,0), sticky=W)
# frame for date
date_frame = Frame(filter_frame)
date_frame.grid(column = 0,  row = 4)
def print_sel():
    print(start_cal.get_date())
    print(end_cal.get_date())
ttk.Label(date_frame, text='Start date').pack()
start_cal = DateEntry(date_frame, width=12, background='darkblue', foreground='white', date_pattern = 'dd-mm-y', maxdate= today, showothermonthdays = False, showweeknumbers = False, weekendbackground = '#DCDCDC')
start_cal.pack(padx=5, pady=5)
ttk.Label(date_frame, text='End date').pack()
end_cal = DateEntry(date_frame, width=12, background='darkblue', foreground='white', date_pattern = 'dd-mm-y', maxdate= today, showothermonthdays = False, showweeknumbers = False, weekendbackground = '#DCDCDC')
end_cal.pack(padx=5, pady=5)
ttk.Button(filter_frame, text="Search", command=print_sel).grid(column = 0,  row = 5)
# Search History Table
sh_table_frame = ttk.Frame(tab5)
sh_table_frame.grid(column = 1,  row = 0, pady = 20)
# Constructing vertical scrollbar 
sh_table_scroll = ttk.Scrollbar(sh_table_frame, orient ="vertical") 
sh_table_scroll.pack(side ='right', fill='y')
# sh table # 
sh_table = ttk.Treeview(sh_table_frame, selectmode ='browse', height = 20, yscrollcommand = sh_table_scroll.set, columns = ("1", "2", "3", "4", "5", "6"), show = 'headings') 
sh_table.pack(side ='left')
# Configuring scrollbar 
sh_table_scroll.configure(command = sh_table.yview) 
# Assigning the width and anchor to the respective columns 
sh_table.column("1", width = 100, anchor ='c') 
sh_table.column("2", width = 100, anchor ='c') 
sh_table.column("3", width = 100, anchor ='c') 
sh_table.column("4", width = 100, anchor ='c') 
sh_table.column("5", width = 100, anchor ='c') 
sh_table.column("6", width = 100, anchor ='c') 
# Assigning the heading names to the respective columns 
sh_table.heading("1", text ="Customer") 
sh_table.heading("2", text ="Form Code")
sh_table.heading("3", text ="Item Code") 
sh_table.heading("4", text ="Result")
sh_table.heading("5", text ="Sample Weight")
sh_table.heading("6", text ="Sample Return")


# tab 6 - customer list
# frame for info
customer_filter_frame = ttk.Frame(tab6)
customer_filter_frame.grid(column = 0,  row = 0, sticky = N)
ttk.Button(customer_filter_frame, text="NEW", command=print_sel).grid(column = 0,  row = 0)
ttk.Button(customer_filter_frame, text="EDIT", command=print_sel).grid(column = 0,  row = 1)
ttk.Button(customer_filter_frame, text="DELETE", command=print_sel).grid(column = 0,  row = 2)
ttk.Label(customer_filter_frame,  text ="Customer").grid(column = 0,  row = 3, padx = (5,0), pady = (10,0), sticky=W)
# Function for checking the key pressed and updating the listbox 
def checkkeytab6(event): 
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
        updatetab6(data)
        lb.pack_forget()
    else: 
        data = [] 
        for item in l: 
            if value.lower() in item.lower(): 
                data.append(item)
                updatetab6(data)
                lb.pack()
def updatetab6(data): 
  # clear previous data 
  lb.delete(0, 'end') 
  # put new data 
  for item in data: 
      lb.insert('end', item) 
def selectcustomertab6(event):
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
# Combobox creation
# create a frame 
customer_input_frame = Frame(customer_filter_frame)
customer_input_frame.grid(column = 0,  row = 4)
# If customer not in list, pop up add new customer fw_pct_frame
customer = StringVar() 
customer_entry = Entry(customer_input_frame, textvariable=customer) 
customer_entry.pack() 
customer_entry.bind('<KeyRelease>', checkkeytab6) 
#creating list box 
lb = Listbox(customer_input_frame)
lb.pack()
lb.pack_forget()
updatetab6(l) 
lb.bind("<KeyRelease-Return>", selectcustomertab6)
lb.bind("<ButtonRelease-1>", selectcustomertab6)
lb.bind("<Double-Button-1>", selectcustomertab6)
ttk.Button(customer_filter_frame, text="Search", command=print_sel).grid(column = 0,  row = 5)
# Customer Table
cl_table_frame = ttk.Frame(tab6)
cl_table_frame.grid(column = 1,  row = 0, pady = 20)
# Constructing vertical scrollbar 
cl_table_scroll = ttk.Scrollbar(cl_table_frame, orient ="vertical") 
cl_table_scroll.pack(side ='right', fill='y')
# cl table # 
cl_table = ttk.Treeview(cl_table_frame, selectmode ='browse', height = 20, yscrollcommand = cl_table_scroll.set, columns = ("1", "2", "3", "4"), show = 'headings') 
cl_table.pack(side ='left')
# Configuring scrollbar 
cl_table_scroll.configure(command = cl_table.yview) 
# Assigning the width and anchor to the respective columns 
cl_table.column("1", width = 100, anchor ='c') 
cl_table.column("2", width = 100, anchor ='c') 
cl_table.column("3", width = 100, anchor ='c') 
cl_table.column("4", width = 100, anchor ='c') 
# Assigning the heading names to the respective columns 
cl_table.heading("1", text ="Customer") 
cl_table.heading("2", text ="Phone")
cl_table.heading("3", text ="Email") 
cl_table.heading("4", text ="Fax")
root.config(menu=menubar)
root.mainloop()  