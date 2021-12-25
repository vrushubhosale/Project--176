from tkinter import *
import speedtest

root = Tk()
root.configure(bg="#FFFFFF")
root.title("Internet Speedtest")
root.geometry("500x300")

label = Label(root, text="INTERNET SPEED CHECK", font=("Lucida Sans Unicode"
 ,20 , "bold"))
label.place(relx=0.5,rely=0.1,anchor=CENTER)

label_download = Label(root, text="Download speed ↓	", font=("Sergoe Print", 20, "bold"), bg="#dee8f1")
label_download.place(relx=0.25, rely=0.5, anchor=CENTER)

label_upload = Label(root, text="Upload speed ↑	", font=("Sergoe Print", 20, "bold"), bg="#dee8f1")
label_upload.place(relx=0.75, rely=0.5, anchor=CENTER)

label_download_speed = Label(root, font=("Yu Gothic Light", 14, "bold" , "italic"))
label_download_speed.place(relx=0.25 , rely=0.6, anchor=CENTER)

label_upload_speed = Label(root, font=("Yu Gothic Light", 14, "bold" , "italic"))
label_upload_speed.place(relx=0.75 , rely=0.6, anchor=CENTER)

def Speedtest():
    st = speedtest.Speedtest()
    download_speed = round(st.download()/1000000,2)
    label_download_speed['text'] = str(download_speed) + "mbps"
    upload_speed = round(st.upload()/1000000,2)
    label_upload_speed['text'] = str(upload_speed) + "mbps"
    
btn_doctor = Button(root, text="CHECK NET SPEED", command=Speedtest(), bg="purple", fg="white",)
btn_doctor.place(relx=0.5, rely=0.3 , anchor=CENTER)

root.mainloop()