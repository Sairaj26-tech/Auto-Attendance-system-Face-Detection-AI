from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2,os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time
     

############################################# FUNCTIONS ################################################

def gui():
    pass

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

    


##################################################################################

def tick():
    time_string = time.strftime('%H:%M:%S')
    gui.clock.config(text=time_string)
    gui.clock.after(200,tick)
 
    
def tick1():
    time_string = time.strftime('%H:%M:%S')
    next8.clock1.config(text=time_string)
    next8.clock1.after(200,tick1)

###################################################################################

def contact():
    mess._show(title='Contact us', message="Please contact us on : 'sairajsmart369@gmail.com' ")

###################################################################################

def check_haarcascadefile():
    exists = os.path.isfile("haarcascade_frontalface_default.xml")
    if exists:
        pass
    else:
        mess._show(title='Some file missing', message='Please contact us for help')
        gui.window.destroy()

###################################################################################

def save_pass():
    assure_path_exists("imagelabel/")
    exists1 = os.path.isfile("imagelabel\psd.txt")
    if exists1:
        tf = open("imagelabel\psd.txt", "r")
        key = tf.read()
    else:
        master.destroy()
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas == None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        else:
            tf = open("imagelabel\psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registered', message='New password was registered successfully!!')
            return
    op = (old.get())
    newp= (new.get())
    nnewp = (nnew.get())
    if (op == key):
        if(newp == nnewp):
            txf = open("imagelabel\psd.txt", "w")
            txf.write(newp)
        else:
            mess._show(title='Error', message='Confirm new password again!!!')
            return
    else:
        mess._show(title='Wrong Password', message='Please enter correct old password.')
        return
    mess._show(title='Password Changed', message='Password changed successfully!!')
    master.destroy()

###################################################################################

def change_pass():
    global master 
    master = tk.Tk()
    master.geometry("400x160")
    master.resizable(False,False)
    master.title("Change Password")
    master.configure(background="white")
    lbl4 = tk.Label(master,text='    Enter Old Password',bg='white',font=('times', 12, ' bold '))
    lbl4.place(x=10,y=10)
    global old
    old=tk.Entry(master,width=25 ,fg="black",relief='solid',font=('times', 12, ' bold '),show='*')
    old.place(x=180,y=10)
    lbl5 = tk.Label(master, text='   Enter New Password', bg='white', font=('times', 12, ' bold '))
    lbl5.place(x=10, y=45)
    global new
    new = tk.Entry(master, width=25, fg="black",relief='solid', font=('times', 12, ' bold '),show='*')
    new.place(x=180, y=45)
    lbl6 = tk.Label(master, text='Confirm New Password', bg='white', font=('times', 12, ' bold '))
    lbl6.place(x=10, y=80)
    global nnew
    nnew = tk.Entry(master, width=25, fg="black", relief='solid',font=('times', 12, ' bold '),show='*')
    nnew.place(x=180, y=80)
    cancel=tk.Button(master,text="Cancel", command=master.destroy ,fg="black"  ,bg="red" ,height=1,width=25 , activebackground = "white" ,font=('times', 10, ' bold '))
    cancel.place(x=200, y=120)
    save1 = tk.Button(master, text="Save", command=save_pass, fg="black", bg="#3ece48", height = 1,width=25, activebackground="white", font=('times', 10, ' bold '))
    save1.place(x=10, y=120)
    master.mainloop()

#####################################################################################

def psw():
    assure_path_exists("imagelabel/")
    exists1 = os.path.isfile("imagelabel\psd.txt")
    if exists1:
        tf = open("imagelabel\psd.txt", "r")
        key = tf.read()
    else:
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas == None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        else:
            tf = open("imagelabel\psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registered', message='New password was registered successfully!!')
            return
    password = tsd.askstring('Password', 'Enter Password', show='*')
    if (password == key):
        TrainImages()
    elif (password == None):
        pass
    else:
        mess._show(title='Wrong Password', message='You have entered wrong password')

######################################################################################

def gclear():
    gui.txt.delete(0, 'end')
    res = " "
    gui.message1.configure(text=res)


def clear2():
    gui.txt2.delete(0, 'end')
    res = " "
    gui.message1.configure(text=res)
    
    
def clear8():
    gui.txt8.delete(0, 'end')
    res = " "
    gui.message1.configure(text=res)

#######################################################################################

def CaptureImages():
    check_haarcascadefile()
    columns = ['SERIAL NO.', '', 'USN', '', 'NAME', '', 'EMAIL']
    assure_path_exists("studet/")
    assure_path_exists("dataset/")
    serial = 0
    exists = os.path.isfile("studet\StudentDetails.csv")
    if exists:
        with open("studet\StudentDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
                serial = serial + 1
        serial = (serial // 2)
        csvFile1.close()
    else:
        with open("studet\StudentDetails.csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(columns)
            serial = 1
        csvFile1.close()
    Id = (gui.txt.get())
    name = (gui.txt2.get())
    emID = (gui.txt8.get())
    if ((name.isalpha()) or (' ' in name)):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # incrementing sample number
                sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("dataset\ " + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                            gray[y:y + h, x:x + w])
                # display the frame
                cv2.imshow('Taking Images', img)
            # wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum > 100:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Taken for ID : " + Id
        row = [serial, '', Id, '', name, '', emID]
        with open('studet\StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        gui.message1.configure(text=res)
    else:
        if (name.isalpha() == False):
            res = "Enter Correct name"
            gui.message.configure(text=res)

########################################################################################

def TrainImages():
    check_haarcascadefile()
    assure_path_exists("imagelabel/")
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, ID = getImagesAndLabels("dataset")
    try:
        recognizer.train(faces, np.array(ID))
    except:
        mess._show(title='No Registrations', message='Please Register someone first!!!')
        return
    recognizer.save("imagelabel\Trainner.yml")
    res = "Profile Saved Successfully"
    gui.message1.configure(text=res)
    gui.message.configure(text='Total Registrations till now  : ' + str(ID[0]))

############################################################################################3

def getImagesAndLabels(path):
    from PIL import Image
    # get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # create empth face list
    faces = []
    # create empty ID list
    Ids = []
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(ID)
    return faces, Ids

###########################################################################################

def DetectImages():
    subname = next8.combo.get()
    check_haarcascadefile()
    assure_path_exists("Attendance"+" "+subname+"/")
    assure_path_exists("studet/")
    for k in next8.tv.get_children():
        next8.tv.delete(k)
    msg = ''
    i = 0
    j = 0
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    exists3 = os.path.isfile("imagelabel\Trainner.yml")
    if exists3:
        recognizer.read("imagelabel\Trainner.yml")
    else:
        mess._show(title='Data Missing', message='Please click on Save Profile to reset data!!')
        return
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);

    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['USN', '', 'Name', '', 'Date', '', 'Time']
    exists1 = os.path.isfile("studet\StudentDetails.csv")
    if exists1:
        df = pd.read_csv("studet\StudentDetails.csv")
    else:
        mess._show(title='Details Missing', message='Students details are missing, please check!')
        cam.release()
        cv2.destroyAllWindows()
        gui.window.destroy()
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    exists = os.path.isfile("Attendance"+" "+subname+"\Attendance_" +subname+ date + ".csv")
    if exists:
        print("file already exists")
    else:
        with open("Attendance"+" "+subname+"\Attendance_" +subname+ date + ".csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(col_names)
        csvFile1.close()
                
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                ID = df.loc[df['SERIAL NO.'] == serial]['USN'].values
                ID = str(ID)
                ID = ID[1:-1]
                bb = str(aa)
                bb = bb[2:-2]
                attendance = [str(ID), '', bb, '', str(date), '', str(timeStamp)]
                global var
                var = bb
                df1 = pd.read_csv("Attendance"+" "+subname+"\Attendance_" +subname+ date + ".csv")
                if var not in df1.values:
                    with open("Attendance"+" "+subname+"\Attendance_" +subname+ date + ".csv", 'a+') as csvFile1:
                            writer = csv.writer(csvFile1)
                            writer.writerow(attendance)
                    csvFile1.close()
                    print("ATTENDANCE MARKED")
               

            else:
                Id = 'Unknown'
                bb = str(Id)
            cv2.putText(im, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
        cv2.imshow('Taking Attendance', im)


            
        if (cv2.waitKey(1) == ord('q')):
            break
    with open("Attendance"+" "+subname+"\Attendance_" +subname+ date + ".csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for lines in reader1:
            i = i + 1
            if (i > 1):
                if (i % 2 != 0):
                    iidd = str(lines[0]) + '   '
                    next8.tv.insert('', 0, text=iidd, values=(str(lines[2]), str(lines[4]), str(lines[6])))
    csvFile1.close()

    cam.release()
    cv2.destroyAllWindows()
######################################## USED STUFFS ############################################
    
global key
key = ''

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day,month,year=date.split("-")

mont={'01':'January',
      '02':'February',
      '03':'March',
      '04':'April',
      '05':'May',
      '06':'June',
      '07':'July',
      '08':'August',
      '09':'September',
      '10':'October',
      '11':'November',
      '12':'December'
      }

######################################## GUI FRONT-END ###########################################

global clock,window,tv,message,message1,txt,txt1

def nxt2():
    next8.window.destroy()
    gui()


def next8():
    from PIL import ImageTk,Image
    import PIL.ImageTk
    next8.window = tk.Tk()
    next8.window.geometry("1280x720")
    next8.window.resizable(True,False)
    next8.window.title("Attendance System")
    next8.window = tk.Toplevel()
    img_bg1 = ImageTk.PhotoImage(file = 'D:/phase 2/phase 2/lib.jpg') 
    ttk.Label( next8.window,image = img_bg1).pack()
    
    next8.frame1 = tk.Frame(next8.window, bg="honeydew3")
    next8.frame1.place(relx=0.28, rely=0.17, relwidth=0.38, relheight=0.80)
    
    next8.head1 = tk.Label(next8.frame1, text="                       For Already Registered                       ", fg="black",bg="honeydew4" ,font=('times', 17, ' bold ') )
    next8.head1.place(x=0,y=0)
    
    
    next8.frame4 = tk.Frame(next8.window, bg="#c4c6ce")
    next8.frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)
    
    next8.datef = tk.Label(next8.frame4, text = day+"-"+mont[month]+"-"+year+"  |  ", fg="orange",bg="#262523" ,width=55 ,height=1,font=('times', 22, ' bold '))
    next8.datef.pack(fill='both',expand=1)
    
    next8.message3 = tk.Label(next8.window, text="JNNCE Attendance System" ,fg="white",bg="#262523" ,width=55 ,height=1,font=('times', 29, ' bold '))
    next8.message3.place(x=10, y=10)
#   
    next8.frame3 = tk.Frame(next8.window, bg="#c4c6ce")
    next8.frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)
    
    next8.clock1 = tk.Label(next8.frame3,fg="orange",bg="#262523" ,width=55 ,height=1,font=('times', 22, ' bold '))
    next8.clock1.pack(fill='both',expand=1)
    tick1()
    
    
    
    email_btn = ImageTk.PhotoImage(file = 'D:/phase 2/phase 2/png button/email8.png')
    email_label=ttk.Label(next8.window,image = email_btn)
    
    detect_btn = ImageTk.PhotoImage(file = 'D:/phase 2/phase 2/png button/detect8.png')
    detect_label=ttk.Label(next8.window,image = detect_btn)
    
    exit_btn1 = ImageTk.PhotoImage(file = 'D:/phase 2/phase 2/png button/exit8.png')
    exit_label=ttk.Label(next8.window,image = exit_btn1)
    home_btn = ImageTk.PhotoImage(file = 'D:/phase 2/phase 2/png button/home8.png')
    home_label=ttk.Label(next8.window,image = home_btn)
    
    
    next8.me1 = tk.Label(next8.frame1, text="Select the subject",width=20  ,height=1  ,fg="black"  ,bg="honeydew3" ,font=('times', 17, ' bold ') )
    next8.me1.place(x=80, y=55)
    next8.combo=ttk.Combobox(next8.frame1)
    next8.combo['values']=("4G LTE","NCS","FON")
    next8.combo.place(x=150, y=88)
    
    next8.lbl3 = tk.Label(next8.frame1, text="Attendance",width=20  ,fg="black"  ,bg="honeydew3"  ,height=1 ,font=('times', 17, ' bold '))
    next8.lbl3.place(x=100, y=200)
    
    noty = tk.Button(next8.frame1,image = email_btn, command=psw ,borderwidth = 0)
    noty.place(x=330, y=140)
    trackImg = tk.Button(next8.frame1, image = detect_btn, command=DetectImages  ,borderwidth = 0)
    trackImg.place(x=30, y=130)
    
    
    

    
    next8.tv= ttk.Treeview(next8.frame1,height =12,columns = ('name','date','time'),)
    next8.tv.column('#0',width=82)
    next8.tv.column('name',width=130)
    next8.tv.column('date',width=133)
    next8.tv.column('time',width=133)
    next8.tv.grid(row=2,column=0,padx=(0,0),pady=(240,0),columnspan=4)
    next8.tv.heading('#0',text ='ID')
    next8.tv.heading('name',text ='NAME')
    next8.tv.heading('date',text ='DATE')
    next8.tv.heading('time',text ='TIME')
    
    scroll=ttk.Scrollbar(next8.frame1,orient='vertical',command=next8.tv.yview)
    scroll.grid(row=2,column=4,padx=(0,100),pady=(240,0),sticky='ns')
    next8.tv.configure(yscrollcommand=scroll.set)
    
    quitWindow = tk.Button(next8.frame1, image = exit_btn1, command=next8.window.destroy  ,borderwidth = 0)
    quitWindow.place(x=30, y=520)
    
    nxtWindow = tk.Button(next8.frame1, image = home_btn, command=nxt2 ,borderwidth = 0)
    nxtWindow.place(x=335, y=520)
    
    next8.window.mainloop()
    
    
    
    
def nxt1():
    gui.window.destroy() 
    next8()
    
    
def gui():
    from PIL import ImageTk,Image
    import PIL.ImageTk
    gui.window = tk.Toplevel()
    gui.window.geometry("1280x720")

    gui.window.resizable(True,False)
    gui.window.title("Attendance System")
    img_bg = ImageTk.PhotoImage(file = 'D:/phase 2/phase 2/image1.jpg') 
    ttk.Label(gui.window,image = img_bg).pack()
  
    
    gui.frame2 = tk.Frame(gui.window, bg="honeydew3")
    gui.frame2.place(relx=0.28, rely=0.17, relwidth=0.38, relheight=0.80)
    
    gui.message3 = tk.Label(gui.window, text="JNNCE Attendance System" ,fg="white",bg="#262523" ,width=55 ,height=1,font=('times', 29, ' bold '))
    gui.message3.place(x=10, y=10)
    
    gui.frame3 = tk.Frame(gui.window, bg="#c4c6ce")
    gui.frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)
    
    gui.frame4 = tk.Frame(gui.window, bg="#c4c6ce")
    gui.frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)
    
    gui.datef = tk.Label(gui.frame4, text = day+"-"+mont[month]+"-"+year+"  |  ", fg="orange",bg="#262523" ,width=55 ,height=1,font=('times', 22, ' bold '))
    gui.datef.pack(fill='both',expand=1)
    
    gui.clock = tk.Label(gui.frame3,fg="orange",bg="#262523" ,width=55 ,height=1,font=('times', 22, ' bold '))
    gui.clock.pack(fill='both',expand=1)
    tick()
    
    gui.head2 = tk.Label(gui.frame2, text="                       For New Registrations                       ", fg="black",bg="honeydew4" ,font=('times', 17, ' bold ') )
    gui.head2.grid(row=0,column=0)
    

    
    gui.lbl = tk.Label(gui.frame2, text="Enter USN",width=20  ,height=1  ,fg="black"  ,bg="honeydew3" ,font=('times', 17, ' bold ') )
    gui.lbl.place(x=80, y=55)
    
    
    gui.txt = tk.Entry(gui.frame2,width=32 ,fg="black",font=('times', 15, ' bold '))
    gui.txt.place(x=30, y=88)
    
    gui.lbl2 = tk.Label(gui.frame2, text="Enter Name",width=20  ,fg="black"  ,bg="honeydew3",font=('times', 17, ' bold '))
    gui.lbl2.place(x=80, y=140)
    
    gui.txt2 = tk.Entry(gui.frame2,width=32 ,fg="black",font=('times', 15, ' bold ')  )
    gui.txt2.place(x=30, y=173)
    
    gui.lb8 = tk.Label(gui.frame2, text="Enter  Email ID",width=20  ,height=1  ,fg="black"  ,bg="honeydew3" ,font=('times', 17, ' bold ') )
    gui.lb8.place(x=80, y=217)
    
    
    gui.txt8 = tk.Entry(gui.frame2,width=32 ,fg="black",font=('times', 15, ' bold '))
    gui.txt8.place(x=30, y=250)
    
    gui.message1 = tk.Label(gui.frame2, text="  " ,bg="honeydew3" ,fg="black"  ,width=39 ,height=1, activebackground = "yellow" ,font=('times', 15, ' bold '))
    gui.message1.place(x=7, y=290)
    
    gui.message = tk.Label(gui.frame2, text="" ,bg="honeydew3" ,fg="black"  ,width=39,height=1, activebackground = "yellow" ,font=('times', 16, ' bold '))
    gui.message.place(x=7, y=490)
    
    gui.lbl21 = tk.Label(gui.frame2, text="Capture Image",width=20  ,height=1  ,fg="black"  ,bg="honeydew3" ,font=('times', 15, ' bold ') )
    gui.lbl21.place(x=3, y=350)
    
      
    gui.lbl22 = tk.Label(gui.frame2, text="Save",width=20  ,height=1  ,fg="black"  ,bg="honeydew3" ,font=('times', 15, ' bold ') )
    gui.lbl22.place(x=280, y=350)
    
    
    res=0
    exists = os.path.isfile("studet\StudentDetails.csv")
    if exists:
        with open("studet\StudentDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
                res = res + 1
        res = (res // 2) - 1
        csvFile1.close()
    else:
        res = 0
    gui.message.configure(text='Total Registrations till now  : '+str(res))
    
    ##################### MENUBAR #################################
    
    gui.menubar = tk.Menu(gui.window,relief='ridge')
    filemenu = tk.Menu(gui.menubar,tearoff=0)
    filemenu.add_command(label='Change Password', command = change_pass)
    filemenu.add_command(label='Contact Us', command = contact)
    filemenu.add_command(label='Exit',command = gui.window.destroy)
    gui.menubar.add_cascade(label='Help',font=('times', 29, ' bold '),menu=filemenu)
    
################################ button image ####################################################    
    delete_btn = ImageTk.PhotoImage(file = 'D:/phase 2/phase 2/png button/del8.png')
    del_label=ttk.Label(gui.window,image = delete_btn)
    exit_btn = ImageTk.PhotoImage(file = 'D:/phase 2/phase 2/png button/exit8.png')
    exit_label=ttk.Label(gui.window,image = exit_btn)
    nxt_btn = ImageTk.PhotoImage(file = 'D:/phase 2/phase 2/png button/nextb8.png')
    nxt_label=ttk.Label(gui.window,image = nxt_btn)
    camera_btn = ImageTk.PhotoImage(file = 'D:/phase 2/phase 2/png button/cam8.png')
    camera_label=ttk.Label(gui.window,image =camera_btn)
    save_btn  = ImageTk.PhotoImage(file ='D:/phase 2/phase 2/png button/save-icon8.png')
    save_label=ttk.Label(gui.window,image = save_btn)
        
####################### ######################### BUTTONS ##################################
    
    clearButton = tk.Button(gui.frame2, image = delete_btn, command=gclear  ,borderwidth = 0)
    clearButton.place(x=360, y=83)
    clearButton2 = tk.Button(gui.frame2, image = delete_btn,command=clear2  ,borderwidth = 0)
    clearButton2.place(x=360, y=170)  
    clearButton8 = tk.Button(gui.frame2, image = delete_btn, command=clear8  ,borderwidth = 0)
    clearButton8.place(x=360, y=248) 
    takeImg = tk.Button(gui.frame2, image = camera_btn, command=CaptureImages  ,borderwidth = 0)
    takeImg.place(x=80, y=395)
    trainImg = tk.Button(gui.frame2,image = save_btn, command=psw ,borderwidth = 0)
    trainImg.place(x=350, y=395)
  
    quitWindow = tk.Button(gui.frame2, image = exit_btn, command=gui.window.destroy  ,borderwidth = 0)
    quitWindow.place(x=30, y=525)
    
    nxtWindow = tk.Button(gui.frame2,image = nxt_btn, command=nxt1  ,borderwidth = 0)
    nxtWindow.place(x=335, y=525)
    
    
    
    
########### ##################### END ######################################
    
    gui.window.configure(menu=gui.menubar)
    gui.window.mainloop()

####################################################################################################
gui()

    
    