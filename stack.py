import time
import tkinter as tk
from tkinter import Toplevel
from tkinter.font import Font
import tkinter.messagebox as msg
def binary_tree():
    pass
l = []
canvas_w = 50
canvas_h = 100
last = []
last_text = []

def push(event):
    global canvas_w
    global canvas_h
    input_ = node.get()
    if input_=="":
        msg.showwarning(title="No input",message="Please enter input")
        return
    l.append(input_)
    last_rect = output.create_rectangle(canvas_w,canvas_h,canvas_w+40,canvas_h+40,outline='#66a1ba',fill='#e6edf0')
    last.append(last_rect)

    last_rect_text = output.create_text(canvas_w+20,canvas_h+20,text=l[-1],font=bold_fonts)
    last_text.append(last_rect_text)

    canvas_w +=40

def pop(event):
    global canvas_w
    global canvas_h
    if len(l)==0:
        msg.showwarning(title="Empty List", message="List is empty")
        return
    last_element = "{} is popped ".format(l.pop(-1))

    to_be_deleted_rect = last.pop()
    to_be_deleted_rect_text = last_text.pop()
    text_popped = output.create_text(80,output.winfo_height()-16, text=last_element)
    output.move(to_be_deleted_rect,canvas_w-60,canvas_h-60)
    output.move(to_be_deleted_rect_text, canvas_w-60, canvas_h-60)
    x1,y1,x2,y2 = output.coords(to_be_deleted_rect)
    if len(l)>0:
        line = output.create_line(canvas_w-40,canvas_h+15,x1,y1,arrow=tk.LAST,capstyle=tk.BUTT,fill='#66a1ba')
    window.update()
    time.sleep(0.3)
    output.delete(to_be_deleted_rect)
    output.delete(text_popped)

    output.delete(to_be_deleted_rect_text)
    try:
        output.delete(line)
    except:
        pass
    canvas_w -= 40


def top(event):
    if len(l) == 0:
        msg.showwarning(title="Empty List", message="List is empty")
        return
    top = "Top element is " + str(l[-1])

    msg.showinfo(title="Top",message=top)
def size_(event):
    length =  "Length is {}".format(len(l))
    msg.showinfo(title="Length", message=length)


window = tk.Tk(className="Stack")
window.configure(bg='#ffffff')

primary_fonts = Font(family='Consolas',size=14,weight='normal')
secondary_fonts = Font(family='Consolas',size=12,weight='normal')
bold_fonts = Font(family='Consolas',size=12,weight='bold')


#setting size
window_w = window.winfo_screenwidth()//2
window_h = window.winfo_screenheight()*3//4
size = str(window_w) + "x" + str(window_h)
window.geometry(size)
window.resizable(0,0)

heading = tk.Label(text="Stack")
heading.configure(font=primary_fonts,bg='#ffffff')
heading.pack(fill=tk.X)

definition = tk.Label(wraplength=window_w-10,justify='left',text="A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. In stack, a new element is added at one end and an element is removed from that end only. The insert and delete operations are often called push and pop.")
definition.configure(font=secondary_fonts,bg='#e6edf0')
definition.pack(fill=tk.X,ipadx=15,ipady=15)

set_of_operations = tk.Frame(bg='#66a1ba')
enter_no = tk.Label(master=set_of_operations,text="ENTER NUMBER",bg="#66a1ba",fg="#ffffff")
node = tk.Entry(master=set_of_operations)
push_b = tk.Button(master=set_of_operations,text="PUSH",bg="#66a1ba",fg="#ffffff")
pop_b = tk.Button(master=set_of_operations,text="POP",bg="#66a1ba",fg="#ffffff")

top_b = tk.Button(master=set_of_operations,text="TOP",bg="#66a1ba",fg="#ffffff")
size_b = tk.Button(master=set_of_operations,text="SIZE",bg="#66a1ba",fg="#ffffff")


push_b.bind('<Button-1>',push)

pop_b.bind('<Button-1>',pop)

top_b.bind('<Button-1>',top)
size_b.bind('<Button-1>',size_)
enter_no.pack(ipadx=5,ipady=5,pady=10,padx=5,side=tk.LEFT,anchor='nw')
node.pack(ipadx=5,ipady=5,pady=10,padx=10,side=tk.LEFT,anchor='nw')
push_b.pack(pady=10,padx=10,side=tk.LEFT,anchor='nw')
pop_b.pack(pady=10,padx=10,side=tk.LEFT,anchor='nw')
size_b.pack(pady=10,padx=10,side=tk.LEFT,anchor='nw')
top_b.pack(pady=10,padx=10,side=tk.LEFT,anchor='nw')

enter_no.configure(font=bold_fonts)
push_b.configure(font=bold_fonts)
pop_b.configure(font=bold_fonts)
top_b.configure(font=bold_fonts)
size_b.configure(font=bold_fonts)
set_of_operations.pack(fill=tk.X)

output_frame = tk.Frame(bg='#ffffff')
output = tk.Canvas(master=output_frame,bg='#ffffff',width=window_w,bd=0,confine=False)
output.pack()
output_frame.pack()

binary_tree = tk.Button(text="Binary Tree",bg="#66a1ba",fg="#ffffff",font=bold_fonts,command=binary_tree)
binary_tree.pack(ipadx=5,ipady=5,pady=10,padx=10,side=tk.LEFT,anchor='nw')

window.mainloop()
