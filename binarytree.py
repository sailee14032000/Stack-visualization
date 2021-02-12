import tkinter as tk
from tkinter.font import Font
import time



class canvas_node(object):
    def __init__(self,val):
        self.canvas_n = output.create_oval(10,10,40,40,tags="nodes_circle",outline='#76af72',fill='#E0E0E0')
        self.canvas_n_coords = output.coords(self.canvas_n)
        self.canvas_ntxt = output.create_text(25,25,text=val)
        self.canvas_ntxt_coords = output.coords(self.canvas_ntxt)



class node_(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self):
        self.root = None
        self.canvas_list = []

    def parentMove(self,x,y,node,dist):
            print(x,y)
            output.move(node.canvas_n,10+dist, 0)
            output.move(node.canvas_ntxt,10+dist, 0)
            node.canvas_n_coords = output.coords(node.canvas_n)
            print(node.canvas_n_coords)
            node.canvas_ntxt_coords = output.coords(node.canvas_ntxt)
            output.update()
            return node.canvas_n_coords


    def insertnode(self,val,start):
        temp = self.root
        list_ = self.canvas_list
        if not temp:
            self.root = node_(val)
            oval = canvas_node(val)
            x = output.winfo_width()//2
            time.sleep(0.5)
            output.move(oval.canvas_n,x,40)
            output.move(oval.canvas_ntxt, x, 40)
            oval.canvas_n_coords = output.coords(oval.canvas_n)
            oval.canvas_ntxt_coords = output.coords(oval.canvas_ntxt)
            list_.append(oval)
            output.update()
            return
        q = [temp]
        i = 0
        strt = start
        while len(q):
            temp = q.pop(0)
            t = list_[i]
            tx,ty= t.canvas_n_coords[0], t.canvas_n_coords[1]
            t = self.parentMove(tx,ty,t,strt)
            tx,ty=t[0],t[1]
            if not temp.left:
                new_node = node_(val)
                oval = canvas_node(val)
                time.sleep(0.5)
                output.move(oval.canvas_n, tx-40, ty+40)
                output.move(oval.canvas_ntxt, tx-40, ty+40)
                oval.canvas_n_coords = output.coords(oval.canvas_n)
                oval.canvas_ntxt_coords =  output.coords(oval.canvas_ntxt)
                list_.append(oval)

                output.update()
                temp.left = new_node
                return

            else:
                l = list_[i+1]
                lx, ly = l.canvas_n_coords[0], l.canvas_n_coords[1]
                l = self.parentMove(lx, ly, l,strt)

                q.append(temp.left)
            if not temp.right:
                new_node = node_(val)
                oval = canvas_node(val)
                time.sleep(0.5)
                output.move(oval.canvas_n, tx+40, ty + 40)
                output.move(oval.canvas_ntxt, tx+40, ty + 40)
                oval.canvas_n_coords = output.coords(oval.canvas_n)
                oval.canvas_ntxt_coords = output.coords(oval.canvas_ntxt)
                list_.append(oval)
                temp.right = new_node
                return
            else:
                i+=1
                strt-=1
                r = list_[i+2]
                rx, ry = r.canvas_n_coords[0], r.canvas_n_coords[1]
                r = self.parentMove(rx, ry, r, strt)

                q.append(temp.right)


    def inorder(self,node):
        if not node:
            return
        self.inorder(node.left)
        print(node.val)
        self.inorder(node.right)

btree = BinaryTree()
start = 1
def insert(event):
     global start
     val = int(node.get())
     btree.insertnode(val,start)
     start+=2

def delete(event):
    k = node.get()
    print(k)


window = tk.Tk(className="Binary Tree")
window.configure(bg='#ffffff')


primary_fonts = Font(family='Consolas',size=14,weight='normal')
secondary_fonts = Font(family='Consolas',size=12,weight='normal')
bold_fonts = Font(family='Consolas',size=12,weight='bold')

#setting_Size
window_w = window.winfo_screenwidth()//2
window_h = window.winfo_screenheight()*3//4
size = str(window_w) + "x" + str(window_h)
window.geometry(size)
window.resizable(0,0)

heading = tk.Label(text="Binary Tree")
heading.configure(font=primary_fonts,bg='#ffffff')
heading.pack(fill=tk.X)

definition = tk.Label(wraplength=window_w-10,justify='left',text="A binary tree is a tree in which every node has 2 children. Left node of a node is called as left child and right as right child")
definition.configure(font=secondary_fonts,bg='#d4ecd4')
definition.pack(fill=tk.X,ipadx=15,ipady=15)

set_of_operations = tk.Frame(bg="#76af72")
enter_no = tk.Label(master=set_of_operations,text="Enter node",bg="#76af72",fg="#ffffff")
node = tk.Entry(master=set_of_operations)
insert_b = tk.Button(master=set_of_operations,text="INSERT",bg="#76af72",fg="#ffffff")
delete_b = tk.Button(master=set_of_operations,text="DELETE",bg="#76af72",fg="#ffffff")

enter_no.pack(ipadx=5,ipady=5,pady=10,padx=5,side=tk.LEFT,anchor='nw')
node.pack(ipadx=5,ipady=5,pady=10,padx=5,side=tk.LEFT,anchor='nw')
insert_b.pack(pady=10,padx=5,side=tk.LEFT,anchor='nw')
delete_b.pack(pady=10,padx=5,side=tk.LEFT,anchor='nw')

insert_b.bind('<Button-1>',insert)
delete_b.bind('<Button-1>',delete)


enter_no.configure(font=bold_fonts)
node.configure(font=bold_fonts)
insert_b.configure(font=bold_fonts)
delete_b.configure(font=bold_fonts)

set_of_operations.pack(fill=tk.X)

output_frame = tk.Frame(bg='#ffffff')
output = tk.Canvas(master=output_frame,bg='#ffffff',width=window_w,bd=0,confine=False,scrollregion=(0,0,1000,1000))
output_y_scroll = tk.Scrollbar(master=output_frame,width=12,orient=tk.VERTICAL)
output_x_scroll = tk.Scrollbar(master=output_frame,width=12,orient=tk.HORIZONTAL)



output.config(yscrollcommand=output_y_scroll.set,xscrollcommand=output_x_scroll)
output_y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
output_x_scroll.pack(side=tk.BOTTOM,fill=tk.X)
output_y_scroll.config(command=output.yview)
output_x_scroll.config(command=output.xview)
output_frame.pack()
output.pack()

window.mainloop()