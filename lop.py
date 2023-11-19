from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Ryunar')
root.geometry('1248x748')

def login():
    user_name = text_root1.get(1.0,'end-1c')
    pass_name = text_root2.get(1.0,'end-1c')

    user_name_def = 'admin'
    pass_name_def = '123abc'

    if user_name == user_name_def and pass_name == pass_name_def:
        print('Bạn đã nhập đúng')
    else:
        print('Bạn nhập sai hãy nhập lại!')

logo = PhotoImage(file = "C:/Users/OSC/Documents/code/Logo Ryunar/hi.png")
root.iconphoto(True,logo)

img = Image.open("C:/Users/OSC/Documents/code/Logo Ryunar/hi.png")
img = img.resize((160,160))
image = ImageTk.PhotoImage(img)
l = Label(root,image=image).place(x=942,y=70)

img1 = Image.open("C:/Users/OSC/Documents/code/Logo Ryunar/i.png")
img1 = img1.resize((707,765))
image1 = ImageTk.PhotoImage(img1)
l1 = Label(root,image=image1).place(x=0)



main=Label(root,text = "Đăng nhập",fg= 'blue',font =('Inter',30))
main.place(x=934,y=210 )

main1=Label(root,text = "Tài khoản",fg= 'blue',font =('Inter',12))
main1.place(x=934,y=290 )

main2=Label(root,text = "Email",fg='gray',font =('Inter',12))
main2.place(x=1080,y=290 )

main3=Label(root,text="Quên mật khẩu ?",fg='blue',font =('Inter',12))
main3.place(x=969,y=520)

main4=Label(root,text='Bằng cách vào các nút trên, bạn đã đồng ý Thông tin \n điều khoản và Chính sách bảo mật',fg='gray',font=('Inter',10))
main4.place(x=880,y=552)

main5=Label(root,text='Bạn chưa có tài khoản?',fg='gray',font=('Inter',11))
main5.place(x=955,y=602)

main6=Label(root,text='Đăng ký',fg='blue',font=('Inter',11)) 
main6.place(x=999,y=625)


pos_x=870

text_root1 = Text(root,width =40,height=2)
text_root1.place(x=pos_x,y=320)


text_root2 = Text(root,width =40,height=2)
text_root2.place(x=pos_x,y=390)

my_Button = Button (root,text='Đăng Nhập',bg='blue',width=35,height=2,font=('Inter') ,command=login)
my_Button.place(x=pos_x,y=460)


root.mainloop()