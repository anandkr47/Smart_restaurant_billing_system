import sqlite3
from tkinter import messagebox


def check_empty(a, b, c):
    if a == b == '' and c != '':
        messagebox.showwarning("Warning", "Please enter 'Name' and 'Phone number'...!")
        return False
    elif a == c == '' and b != '':
        messagebox.showwarning("Warning", "Please enter 'Name' and 'Address'...!")
        return False
    elif b == c == '' and a != '':
        messagebox.showwarning("Warning", "Please enter 'Phone number' and 'Address'...!")
        return False
    elif a == '' and b != c != '':
        messagebox.showwarning("Warning", "Please enter 'Name'...!")
        return False
    elif b == '' and a != c != '':
        messagebox.showwarning("Warning", "Please enter 'Phone number'...!")
        return False
    elif c == '' and b != a != '':
        messagebox.showwarning("Warning", "Please enter 'Address'...!")
        return False
    else:
        return True


def check_for_items(a, b, c):
    chk = 0
    if chk == 0:
        l = len(a)
        if l >= 3:
            w = a.split(" ")
            for word in w:
                if word.isalpha():
                    chk = 1
                elif word.isalnum():
                    chk = 0
                    messagebox.showerror("Error", "Your 'NAME' contains numbers...!")
                    break
                else:
                    messagebox.showerror("Error", "Your 'NAME' contains wild characters...!")
                    break
        elif 0 < l < 3:
            chk = 0
            messagebox.showerror("Error", "Please enter appropriate name...!")
    if chk == 1:
        l = len(b)
        if l == 10:
            if b.isdigit():
                chk = 1
            elif b.isalnum():
                chk = 0
                messagebox.showerror("Error", "Your 'Phone Number' contains alphabets...!")
            else:
                chk = 0
                messagebox.showerror("Error", "Your 'Phone Number' contains wild characters...!")
        elif l != 10:
            chk = 0
            messagebox.showerror("Error", "Please enter valid Phone number...!")
    if chk == 1:
        l = len(c)
        if l >= 6:
            chk = 1
        elif 0 < l < 6:
            chk = 0
            messagebox.showerror("Error", "Please enter a valid Address...!")
        else:
            pass
    if chk == 1:
        return True
    else:
        return False


def getOptions():
    conn = sqlite3.connect("food.db")
    c = conn.cursor()
    options = []
    foodrate = {}
    foodplace = {}
    q = "select food,rate,place from food_base"
    c.execute(q)
    data = c.fetchall()
    foodlst = list(data)
    l = len(foodlst)
    for i in range(l):
        a = list(foodlst[i])
        options.append(a[0])
        foodrate[a[0]] = a[1]
        foodplace[a[0]] = a[2]
    return options, foodrate, foodplace


def checkslpno(a):
    conn = sqlite3.connect('records.db')
    c = conn.cursor()
    q = 'Select Slip_No from customers'
    c.execute(q)
    data = c.fetchall()
    for i in data:
        if a in i:
            c.close()
            return 1
        else:
            continue


def showtime(event):
    button = event.widget
    button.config(bg='gray60')


def showtimeends(event):
    button = event.widget
    button.config(bg='White')


def E_srchcusto(event):
    button = event.widget
    button.config(bg='brown1')


def L_srchcusto(event):
    button = event.widget
    button.config(bg='DarkOliveGreen3')


def E_addbtn(event):
    button = event.widget
    button.config(bg='cyan4')


def L_addbtn(event):
    button = event.widget
    button.config(bg='medium aquamarine')


def E_totbtn(event):
    button = event.widget
    button.config(bg='tan4')


def L_totbtn(event):
    button = event.widget
    button.config(bg='medium aquamarine')


def E_billbtn(event):
    button = event.widget
    button.config(bg='green4')


def L_billbtn(event):
    button = event.widget
    button.config(bg='medium aquamarine')


def E_exitbtn(event):
    button = event.widget
    button.config(bg='red2')


def L_lgextbtn(event):
    button = event.widget
    button.config(bg='gray64')


def L_exitbtn(event):
    button = event.widget
    button.config(bg='medium aquamarine')


def E_widgets(event):
    button = event.widget
    button.config(bg='deep sky blue')


def L_widgets(event):
    button = event.widget
    button.config(bg='cyan')


def E_SDG(event):
    button = event.widget
    button.config(bg='gray50')


def L_SDG(event):
    button = event.widget
    button.config(bg='gray30')


def E_prntbtn(event):
    button = event.widget
    button.config(bg='SlateBlue1')


def L_prntbtn(event):
    button = event.widget
    button.config(bg='medium aquamarine')


def E_resetbtn(event):
    button = event.widget
    button.config(bg='VioletRed4', fg='gray60')


def L_resetbtn(event):
    button = event.widget
    button.config(bg='medium orchid', fg='black')


def E_rcptfem(event):
    button = event.widget
    button.config(bg='deep sky blue')


def L_recptfrm(event):
    button = event.widget
    button.config(bg='khaki3')


def E_lgtit(event):
    button = event.widget
    button.config(bg='black')


def L_lgtit(event):
    button = event.widget
    button.config(bg='Powder Blue')


def E_lg_login_btn(event):
    button = event.widget
    button.config(bg='purple1')


def L_lg_login_btn(event):
    button = event.widget
    button.config(bg='SpringGreen2')


def check_name():
    conn = sqlite3.connect('records.db')
    c = conn.cursor()
    q = 'Select Name, from user_ids'


def exit_btn(a):
    ans = messagebox.askyesno("Exit Program", "Do you want to exit the Program...?")
    if ans > 0:
        a.destroy()
    else:
        return


def E_crete_n_usr(event):
    button = event.widget
    button.config(bg='cyan2')


def L_crete_n_usr(event):
    button = event.widget
    button.config(bg='gray30')


def E_cr_usr_btn(event):
    button = event.widget
    button.config(bg='gold2')


def L_cr_usr_btn(event):
    button = event.widget
    button.config(bg='plum2')


def E_cl_usr_btn(event):
    button = event.widget
    button.config(bg='red')


def L_cl_usr_btn(event):
    button = event.widget
    button.config(bg='forest green')


def check_creat_details(a, b, c, d, e, f, g, h):
    chk = 0
    if chk == 0:
        l = len(a)
        if l >= 3:
            if a.isalpha():
                chk = 1
            elif a.isalnum():
                messagebox.showerror("Error", "Your First Name contains numbers...!")
                e.focus_set()
            else:
                messagebox.showerror("Error", "Your First Name contains wild characters...!")
                e.focus_set()
        elif 0 < l < 3:
            messagebox.showerror("Error", "Please enter appropriate name...!")
            e.focus_set()
    if chk == 1:
        l = len(b)
        if l >= 3:
            if b.isalpha():
                chk = 1
            elif b.isalnum():
                chk = 0
                messagebox.showerror("Error", "Your Second Name contains numbers...!")
                f.focus_set()
            else:
                chk = 0
                messagebox.showerror("Error", "Your Second Name contains wild characters...!")
                f.focus_set()
        elif 0 < l < 3:
            chk = 0
            messagebox.showerror("Error", "Please enter appropriate Second name...!")
            f.focus_set()
    if chk == 1:
        l = len(c)
        if l == 10:
            if c.isdigit():
                chk = 1
            elif c.isalnum():
                chk = 0
                messagebox.showerror("Error", "Entered 'Phone Number' contains alphabets...!")
                g.focus_set()
            else:
                chk = 0
                messagebox.showerror("Error", "Entered 'Phone Number' contains wild characters...!")
                g.focus_set()
        elif l != 10:
            chk = 0
            messagebox.showerror("Error", "Please enter valid Phone number...!")
            g.focus_set()
    if chk == 1:
        l = len(d)
        ans = ''
        for i in range(l):
            if d[i] == '@':
                ans += d[i:]
                break
            else:
                pass
        if ans != '@gmail.com' and ans != '@hotmail.com' and ans != '@outlook.com' and ans != '@yahoo.com':
            messagebox.showerror("Error", "Your gmail doesn't have '@gmail.com' or\
 '@hotmail.com' or '@outlook.com' or @yahoo.com mail address...!")
            messagebox.showinfo("Information", "Try re-entering your E-Mail address..")
            h.focus_set()
            chk = 0
        else:
            chk = 1
    if chk == 1:
        return True
    else:
        return False


def check_create_password(a, b):
    l1 = len(a)
    l2 = len(b)
    if l1 == l2 < 4:
        messagebox.showinfo("Information", "Your password should contains 4 or more than 4 characters")
        return False
    elif a != b:
        messagebox.showerror("Error", "Failed to Create New User...!")
        messagebox.showinfo("Information", "Your password didn't match...!")
        return False
    else:
        return True


def detail_blank(a, b, c, d, e, f, g):
    if a == '' or b == '' or c == '' or d == '' or e == '' or f == '':
        messagebox.showerror("Error", "Please fill up the needed details to proceed..!")
        g.focus_set()
        return False
    else:
        return True


def creating_new_user(a, b, c, d, e, write):
    nam = a+' '+b
    phone = c
    mail = d
    pswd = e
    if write == 1:
        try:
            conn = sqlite3.connect('records.db')
            c = conn.cursor()
            q = "INSERT into user_ids VALUES('{}', '{}', '{}', '{}')".format(nam, phone, mail, pswd)
            c.execute(q)
            conn.commit()
            conn.close()
            return True
        except WindowsError:
            messagebox.showerror("Error", "Failed to create your account...!")
            return False
    else:
        return False


def check_login_blanks(a, b):
    if a == '' and b == '':
        messagebox.showwarning("Warning", "Please enter your E-Mail and Password to login..!")
    elif a != '' and b == '':
        messagebox.showwarning("Warning", "Please enter your Password to login..!")
    elif a == '' and b != '':
        messagebox.showwarning("Warning", "Please enter your Email...!")
    else:
        return True


def check_login_details(a, b):
    mail = a
    pswd = b
    conn = sqlite3.connect('records.db')
    c = conn.cursor()
    q = "select * from user_ids where gmail='{}' and password='{}'".format(mail, pswd)
    c.execute(q)
    data = c.fetchall()
    conn.commit()
    conn.close()
    for value in data:
        messagebox.showinfo('', "WELCOME '"+data[0][0].upper()+"'")
        return True
    else:
        return False


def enter_customer_details(a, b, c, d, e, f):
    conn = sqlite3.connect('records.db')
    cn = conn.cursor()
    q = "INSERT into customers VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(a, b, c, d, e, f)
    cn.execute(q)
    conn.commit()
    conn.close()
    messagebox.showinfo("Information", "Successfully Done...!")
    return True


def E_reciept(event):
    button = event.widget
    button.config(bg='LightGray', state='disable')


def L_reciept(event):
    button = event.widget
    button.config(bg='White', state='normal')


def E_fooddb(event):
    button = event.widget
    button.config(bg='navy', fg='gray62')


def L_fooddb(event):
    button = event.widget
    button.config(bg='deep pink', fg='black')


def E_custodb(event):
    button = event.widget
    button.config(bg='DeepSkyBlue2', fg='black')


def L_custodb(event):
    button = event.widget
    button.config(bg='brown4', fg='gray60')


def E_usrdb(event):
    button = event.widget
    button.config(bg='aquamarine', fg='black')


def L_usrdb(event):
    button = event.widget
    button.config(bg='purple4', fg='gray60')


def E_srch_db_btn(event):
    button = event.widget
    button.config(bg='DarkOrchid1', fg='black')


def L_srch_db_btn(event):
    button = event.widget
    button.config(bg='gray10', fg='gray60')


def E_exit_db(event):
    button = event.widget
    button.config(bg='red2')


def L_exit_db(event):
    button = event.widget
    button.config(bg='dark orange')


def delete_food_frm_db(v, d):
    if d:
        conn = sqlite3.connect('food.db')
        c = conn.cursor()
        ans = messagebox.askyesno("Conformation", f"Do you really want to delete the food item '{v[0]}'\
 from database...?")
        if ans:
            c.execute(f"DELETE FROM food_base WHERE Food='{v[0]}'")
            conn.commit()
            messagebox.showinfo("Information", f"Successfully deleted the food item '{v[0]}' from database.")
            messagebox.showinfo("Information", "Go Back and Once again Select Food DataBase to see the updated\
 database")
        else:
            messagebox.showinfo("Information", f"The selected food item '{v[0]}' is not deleted.")
        conn.close()
    else:
        pass


def update_food_db(a, b, c, k):
    try:
        conn = sqlite3.connect('food.db')
        cr = conn.cursor()
        q1 = f"UPDATE food_base SET Rate={b} WHERE Food='{k}'"
        q2 = f"UPDATE food_base SET Place='{c}' WHERE Food='{k}'"
        q3 = f"UPDATE food_base SET Food='{a}' WHERE Food='{k}'"
        cr.execute(q1)
        cr.execute(q2)
        cr.execute(q3)
        conn.commit()
        conn.close()
        return True
    except sqlite3.OperationalError:
        return False


def add_food_in_db(v):
    try:
        conn = sqlite3.connect('food.db')
        cr = conn.cursor()
        q = f"INSERT INTO food_base(Food, Rate, Place) VALUES('{v[0]}', {v[1]}, '{v[2]}')"
        cr.execute(q)
        conn.commit()
        conn.close()
        return True
    except sqlite3.OperationalError:
        return False


def E_lst(event):
    button = event.widget
    button.config(bg='thistle')


def L_lst(event):
    button = event.widget
    button.config(bg='misty rose')
