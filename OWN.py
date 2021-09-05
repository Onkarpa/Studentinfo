import tkinter as tk
import os

root=tk.Tk()
root.title('owngui')
root.geometry('1300x700')
root.configure(bg='pink')

tp_frame=tk.Frame(root,bg='black')
tp_frame.place(x=5,y=5,width=1355,height=50)

tp_lb=tk.Label(tp_frame,text='~ Result ~',font=('Times New Roman',20,'bold'),bg='black',fg='white')
tp_lb.pack(pady=5)

l_frame=tk.Frame(root,bg='black')
l_frame.place(x=5,y=60,width=670,height=500)

r_frame=tk.Frame(root,bg='black')
r_frame.place(x=680,y=60,width=676,height=500)

b_frame=tk.Frame(root,bg='black')
b_frame.place(x=5,y=570,width=1355,height=100)


#creating a variable

sid=tk.StringVar()
fname=tk.StringVar()
lname=tk.StringVar()
clas=tk.StringVar()
strm=tk.StringVar()
mail=tk.StringVar()
py=tk.IntVar()
ml=tk.IntVar()
sql=tk.IntVar()
tot=tk.StringVar()
per=tk.StringVar()
gr=tk.StringVar()

def logout():
    ask=tk.messagebox.askyesno('confermation','Do you really want to closed')
    if ask>0:
        root.destroy()

def clear():
    sid.set('')
    fname.set('')
    lname.set('')
    clas.set('')
    strm.set('')
    mail.set('')
    py.set(0)
    ml.set(0)
    sql.set(0)
    tot.set('')
    per.set('')
    gr.set('')


def calculate():
    total=py.get()+ml.get()+sql.get()
    tot.set(total)
    
    perc=total/3
    per.set(perc)
    
    if perc>85:
        gr.set('OO')
    elif perc<84 and perc>54:
        gr.set('A')
    elif perc<55 and perc>35:
        gr.get('B')
    elif perc<36:
        gr.set('C')
    else:
        gr.set('Fail')

def save_file():
    calculate()
    with open('data/' + str(sid.get()) + '.txt','w') as f:
        f.write(
                str(sid.get()) + ',' +
                str(fname.get()) + ',' +
                str(lname.get()) + ',' +
                str(clas.get()) + ',' +
                str(strm.get()) + ',' +
                str(mail.get()) + ',' +
                str(py.get()) + ',' +
                str(ml.get()) + ',' +
                str(sql.get()) + ',' +
                str(tot.get()) + ',' +
                str(per.get()) + ',' +
                str(gr.get()) 
                )
def save():
    present='no'
    if sid.get()==" ":
        tk.messagebox.showerror('Warning','ID is mandatory')
    else:
        f=os.listdir('data/')
        for file in f:
            if file.split('.')[0] == sid.get():
                present ='yes'
        if present =='yes':
            ask=tk.messagebox.askyesno('Update','DO you really want to update the file')
            if ask > 0:
                calculate()
                save_file()
                tk.messagebox.showinfo('Success',' File Update Successfulluy')
        else:
                calculate()
                save_file()
                tk.messagebox.showinfo('Success',' File Saved Successfulluy')
                
def search():
    present='no'
    if sid.get()=='':
        tk.messagebox.showerror('Warning','ID is mandatory')
    else:
        f=os.listdir('data/')
        for file in f:
            file_txt=file.split('.')
            if sid.get()==file_txt[0]:
                present='yes'
    if present=='yes':
        with open('data/' + str(sid.get()) + '.txt','r') as f1:
            sid_info=f1.read()
            sid_info_lst=sid_info.split(',')
            
            sid.set(sid_info_lst[0])
            fname.set(sid_info_lst[1])
            lname.set(sid_info_lst[2])
            clas.set(sid_info_lst[3])
            strm.set(sid_info_lst[4])
            mail.set(sid_info_lst[5])
            py.set(sid_info_lst[6])
            ml.set(sid_info_lst[7])
            sql.set(sid_info_lst[8])
            tot.set(sid_info_lst[9])
            per.set(sid_info_lst[10])
            gr.set(sid_info_lst[11])
            
    else:
            tk.messagebox.showerror('warning','ID does not exist')          
                

#left part

sid_id=tk.Label(l_frame,text='ID',font=('Times New Roman',20,'bold'),bg='black',fg='white')
sid_id.grid(row=0,column=0,padx=10,pady=10)

sid_e=tk.Entry(l_frame,textvariable=sid,font=('Times New Roman',20,'bold'),bg='black',fg='white')
sid_e.grid(row=0,column=1,padx=10,pady=10)

fname_l=tk.Label(l_frame,text='Fnmae',font=('Times New Roman',20,'bold'),bg='black',fg='white')
fname_l.grid(row=3,column=0,padx=10,pady=10)

fname_e=tk.Entry(l_frame,textvariable = fname,font=('Times New Roman',20,'bold'),bg='black',fg='white')
fname_e.grid(row=3,column=1,padx=10,pady=10)

lname_l=tk.Label(l_frame,text='Lnmae',font=('Times New Roman',20,'bold'),bg='black',fg='white')
lname_l.grid(row=6,column=0,padx=10,pady=10)

lname_e=tk.Entry(l_frame,textvariable=lname,font=('Times New Roman',20,'bold'),bg='black',fg='white')
lname_e.grid(row=6,column=1,padx=10,pady=10)

clas_l=tk.Label(l_frame,text='Class',font=('Times New Roman',20,'bold'),bg='black',fg='white')
clas_l.grid(row=9,column=0,padx=10,pady=10)

clas_e=tk.Entry(l_frame,textvariable =clas,font=('Times New Roman',20,'bold'),bg='black',fg='white')
clas_e.grid(row=9,column=1,padx=10,pady=10)

strm_l=tk.Label(l_frame,text='Stream',font=('Times New Roman',20,'bold'),bg='black',fg='white')
strm_l.grid(row=12,column=0,padx=10,pady=10)

strm_e=tk.Entry(l_frame,textvariable = strm,font=('Times New Roman',20,'bold'),bg='black',fg='white')
strm_e.grid(row=12,column=1,padx=10,pady=10)

mail_l=tk.Label(l_frame,text='Mail_ID',font=('Times New Roman',20,'bold'),bg='black',fg='white')
mail_l.grid(row=15,column=0,padx=10,pady=10)

mail_e=tk.Entry(l_frame,textvariable = mail,font=('Times New Roman',20,'bold'),bg='black',fg='white')
mail_e.grid(row=15,column=1,padx=10,pady=10)

#Right part


py_l=tk.Label(r_frame,text='Python',font=('Times New Roman',20,'bold'),bg='black',fg='white')
py_l.grid(row=0,column=0,padx=10,pady=10)

py_e=tk.Entry(r_frame,textvariable = py,font=('Times New Roman',20,'bold'),bg='black',fg='white')
py_e.grid(row=0,column=1,padx=10,pady=10)

ml_l=tk.Label(r_frame,text='ML',font=('Times New Roman',20,'bold'),bg='black',fg='white')
ml_l.grid(row=1,column=0,padx=10,pady=10)

ml_e=tk.Entry(r_frame,textvariable = ml,font=('Times New Roman',20,'bold'),bg='black',fg='white')
ml_e.grid(row=1,column=1,padx=10,pady=10)

sql_l=tk.Label(r_frame,text='SQL',font=('Times New Roman',20,'bold'),bg='black',fg='white')
sql_l.grid(row=3,column=0,padx=10,pady=10)

sql_e=tk.Entry(r_frame,textvariable = sql,font=('Times New Roman',20,'bold'),bg='black',fg='white')
sql_e.grid(row=3,column=1,padx=10,pady=10)

tot_l=tk.Label(r_frame,text='Total',font=('Times New Roman',20,'bold'),bg='black',fg='white')
tot_l.grid(row=6,column=0,padx=10,pady=10)

tot_e=tk.Entry(r_frame,textvariable = tot,font=('Times New Roman',20,'bold'),bg='black',fg='white')
tot_e.grid(row=6,column=1,padx=10,pady=10)

per_l=tk.Label(r_frame,text='Per',font=('Times New Roman',20,'bold'),bg='black',fg='white')
per_l.grid(row=9,column=0,padx=10,pady=10)

per_e=tk.Entry(r_frame,textvariable = per,font=('Times New Roman',20,'bold'),bg='black',fg='white')
per_e.grid(row=9,column=1,padx=10,pady=10)

gr_l=tk.Label(r_frame,text='Grade',font=('Times New Roman',20,'bold'),bg='black',fg='white')
gr_l.grid(row=12,column=0,padx=10,pady=10)

gr_e=tk.Entry(r_frame,textvariable = gr,font=('Times New Roman',20,'bold'),bg='black',fg='white')
gr_e.grid(row=12,column=1,padx=10,pady=10)


#buttons

log_b=tk.Button(b_frame,text='Lgout',font=('Times New Roman',20,'bold'),bg='black',fg='white',command=logout)
log_b.pack(padx=5,pady=5,side=tk.RIGHT)

clr_b=tk.Button(b_frame,text='clear',font=('Times New Roman',20,'bold'),bg='black',fg='white',command=clear)
clr_b.pack(padx=5,pady=5,side=tk.RIGHT)

cal_b=tk.Button(b_frame,text='Calculate',font=('Times New Roman',20,'bold'),bg='black',fg='white',command=calculate)
cal_b.pack(padx=5,pady=5,side=tk.RIGHT)

save_b=tk.Button(b_frame,text='Save',font=('Times New Roman',20,'bold'),bg='black',fg='white',command=save)
save_b.pack(padx=5,pady=5,side=tk.RIGHT)

search_b=tk.Button(b_frame,text='Search',font=('Times New Roman',20,'bold'),bg='black',fg='white',command=search)
search_b.pack(padx=5,pady=5,side=tk.RIGHT)




root.mainloop()
