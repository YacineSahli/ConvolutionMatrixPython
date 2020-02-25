#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.19
#  in conjunction with Tcl version 8.6
#    Dec 02, 2018 02:19:27 PM CST  platform: Windows NT

import sys

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import MainWindow_support
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    MainWindow_support.set_Tk_var()
    top = Toplevel1 (root)
    MainWindow_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    MainWindow_support.set_Tk_var()
    top = Toplevel1 (w)
    MainWindow_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font11 = "-family {Segoe UI} -size 9 -weight bold -slant roman"  \
                 " -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("615x313+629+87")
        top.title("Convolution Matrix")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")


        self.Frame_Matrix = tk.LabelFrame(top)
        self.Frame_Matrix.place(relx=0.016, rely=0.0, relheight=0.783 , relwidth=0.455)
        self.Frame_Matrix.configure(relief='groove')
        self.Frame_Matrix.configure(font=font11)
        self.Frame_Matrix.configure(foreground="black")
        self.Frame_Matrix.configure(text='''MATRIX''')
        self.Frame_Matrix.configure(background="#d9d9d9")
        self.Frame_Matrix.configure(highlightbackground="#d9d9d9")
        self.Frame_Matrix.configure(highlightcolor="black")
        self.Frame_Matrix.configure(width=280)

        self.TEntry00 = ttk.Entry(self.Frame_Matrix)
        self.TEntry00.place(relx=0.071, rely=0.163, relheight=0.127
                , relwidth=0.143, bordermode='ignore')
        self.TEntry00.configure(textvariable=MainWindow_support.matrix00)
        self.TEntry00.configure(width=40)
        self.TEntry00.configure(takefocus="")
        #self.TEntry00.configure(cursor="ibeam")

        self.TEntry01 = ttk.Entry(self.Frame_Matrix)
        self.TEntry01.place(relx=0.25, rely=0.163, relheight=0.127
                , relwidth=0.143, bordermode='ignore')
        self.TEntry01.configure(textvariable=MainWindow_support.matrix01)
        self.TEntry01.configure(width=40)
        self.TEntry01.configure(takefocus="")
        #self.TEntry01.configure(cursor="ibeam")

        self.TEntry02 = ttk.Entry(self.Frame_Matrix)
        self.TEntry02.place(relx=0.429, rely=0.163, relheight=0.127
                , relwidth=0.143, bordermode='ignore')
        self.TEntry02.configure(textvariable=MainWindow_support.matrix02)
        self.TEntry02.configure(width=40)
        self.TEntry02.configure(takefocus="")
        #self.TEntry02.configure(cursor="ibeam")

        self.TEntry03 = ttk.Entry(self.Frame_Matrix)
        self.TEntry03.place(relx=0.607, rely=0.163, relheight=0.127
                , relwidth=0.143, bordermode='ignore')
        self.TEntry03.configure(textvariable=MainWindow_support.matrix03)
        self.TEntry03.configure(width=40)
        self.TEntry03.configure(takefocus="")
        #self.TEntry03.configure(cursor="ibeam")

        self.TEntry04 = ttk.Entry(self.Frame_Matrix)
        self.TEntry04.place(relx=0.786, rely=0.163, relheight=0.127
                , relwidth=0.143, bordermode='ignore')
        self.TEntry04.configure(textvariable=MainWindow_support.matrix04)
        self.TEntry04.configure(width=40)
        self.TEntry04.configure(takefocus="")
        #self.TEntry04.configure(cursor="ibeam")

        self.TEntry10 = ttk.Entry(self.Frame_Matrix)
        self.TEntry10.place(relx=0.071, rely=0.327, relheight=0.127
                , relwidth=0.143, bordermode='ignore')
        self.TEntry10.configure(textvariable=MainWindow_support.matrix10)
        self.TEntry10.configure(width=40)
        self.TEntry10.configure(takefocus="")
        #self.TEntry10.configure(cursor="ibeam")

        self.TEntry11 = ttk.Entry(self.Frame_Matrix)
        self.TEntry11.place(relx=0.25, rely=0.327, relheight=0.127
                , relwidth=0.143, bordermode='ignore')
        self.TEntry11.configure(textvariable=MainWindow_support.matrix11)
        self.TEntry11.configure(width=40)
        self.TEntry11.configure(takefocus="")
        #self.TEntry11.configure(cursor="ibeam")

        self.TEntry12 = ttk.Entry(self.Frame_Matrix)
        self.TEntry12.place(relx=0.429, rely=0.327, relheight=0.127
                , relwidth=0.143, bordermode='ignore')
        self.TEntry12.configure(textvariable=MainWindow_support.matrix12)
        self.TEntry12.configure(width=40)
        self.TEntry12.configure(takefocus="")
        #self.TEntry12.configure(cursor="ibeam")

        self.TEntry1_7 = ttk.Entry(self.Frame_Matrix)
        self.TEntry1_7.place(relx=0.607, rely=0.327, relheight=0.127
                , relwidth=0.143, bordermode='ignore')
        self.TEntry1_7.configure(textvariable=MainWindow_support.matrix13)
        self.TEntry1_7.configure(width=40)
        self.TEntry1_7.configure(takefocus="")
        #self.TEntry1_7.configure(cursor="ibeam")

        self.TEntry1_1 = ttk.Entry(self.Frame_Matrix)
        self.TEntry1_1.place(relx=0.786, rely=0.327, relheight=0.127
                , relwidth=0.143, bordermode='ignore')
        self.TEntry1_1.configure(textvariable=MainWindow_support.matrix14)
        self.TEntry1_1.configure(width=40)
        self.TEntry1_1.configure(takefocus="")
        #self.TEntry1_1.configure(cursor="ibeam")

        self.TEntry1_2 = ttk.Entry(self.Frame_Matrix)
        self.TEntry1_2.place(relx=0.071, rely=0.49, relheight=0.127
                , relwidth=0.143, bordermode='ignore')
        self.TEntry1_2.configure(textvariable=MainWindow_support.matrix20)
        self.TEntry1_2.configure(width=40)
        self.TEntry1_2.configure(takefocus="")
        #self.TEntry1_2.configure(cursor="ibeam")

        self.TEntry1_3 = ttk.Entry(self.Frame_Matrix)
        self.TEntry1_3.place(relx=0.25, rely=0.49, relheight=0.127
                , relwidth=0.143, bordermode='ignore')
        self.TEntry1_3.configure(textvariable=MainWindow_support.matrix21)
        self.TEntry1_3.configure(width=40)
        self.TEntry1_3.configure(takefocus="")
        #self.TEntry1_3.configure(cursor="ibeam")

        self.TEntry1_4 = ttk.Entry(self.Frame_Matrix)
        self.TEntry1_4.place(relx=0.429, rely=0.49, relheight=0.127
                , relwidth=0.143, bordermode='ignore')
        self.TEntry1_4.configure(textvariable=MainWindow_support.matrix22)
        self.TEntry1_4.configure(width=40)
        self.TEntry1_4.configure(takefocus="")
        #self.TEntry1_4.configure(cursor="ibeam")

        self.TEntry1_5 = ttk.Entry(self.Frame_Matrix)
        self.TEntry1_5.place(relx=0.607, rely=0.49, relheight=0.127
                , relwidth=0.143, bordermode='ignore')
        self.TEntry1_5.configure(textvariable=MainWindow_support.matrix23)
        self.TEntry1_5.configure(width=40)
        self.TEntry1_5.configure(takefocus="")
        #self.TEntry1_5.configure(cursor="ibeam")

        self.TEntry1_6 = ttk.Entry(self.Frame_Matrix)
        self.TEntry1_6.place(relx=0.786, rely=0.49, relheight=0.127
                , relwidth=0.143, bordermode='ignore')
        self.TEntry1_6.configure(textvariable=MainWindow_support.matrix24)
        self.TEntry1_6.configure(width=40)
        self.TEntry1_6.configure(takefocus="")
        #self.TEntry1_6.configure(cursor="ibeam")

        self.TEntry1_8 = ttk.Entry(self.Frame_Matrix)
        self.TEntry1_8.place(relx=0.071, rely=0.653, relheight=0.127
                , relwidth=0.143, bordermode='ignore')
        self.TEntry1_8.configure(textvariable=MainWindow_support.matrix30)
        self.TEntry1_8.configure(width=40)
        self.TEntry1_8.configure(takefocus="")
        #self.TEntry1_8.configure(cursor="ibeam")

        self.TEntry1_8 = ttk.Entry(self.Frame_Matrix)
        self.TEntry1_8.place(relx=0.25, rely=0.653, relheight=0.127
                , relwidth=0.143, bordermode='ignore')
        self.TEntry1_8.configure(textvariable=MainWindow_support.matrix31)
        self.TEntry1_8.configure(width=40)
        self.TEntry1_8.configure(takefocus="")
        #self.TEntry1_8.configure(cursor="ibeam")

        self.TEntry1_9 = ttk.Entry(self.Frame_Matrix)
        self.TEntry1_9.place(relx=0.429, rely=0.653, relheight=0.127
                , relwidth=0.143, bordermode='ignore')
        self.TEntry1_9.configure(textvariable=MainWindow_support.matrix32)
        self.TEntry1_9.configure(width=40)
        self.TEntry1_9.configure(takefocus="")
        #self.TEntry1_9.configure(cursor="ibeam")

        self.TEntry1_10 = ttk.Entry(self.Frame_Matrix)
        self.TEntry1_10.place(relx=0.607, rely=0.653, relheight=0.127
                , relwidth=0.143, bordermode='ignore')
        self.TEntry1_10.configure(textvariable=MainWindow_support.matrix33)
        self.TEntry1_10.configure(width=40)
        self.TEntry1_10.configure(takefocus="")
        #self.TEntry1_10.configure(cursor="ibeam")

        self.TEntry1_10 = ttk.Entry(self.Frame_Matrix)
        self.TEntry1_10.place(relx=0.786, rely=0.653, relheight=0.127
                , relwidth=0.143, bordermode='ignore')
        self.TEntry1_10.configure(textvariable=MainWindow_support.matrix34)
        self.TEntry1_10.configure(width=40)
        self.TEntry1_10.configure(takefocus="")
        #self.TEntry1_10.configure(cursor="ibeam")

        self.TEntry1_11 = ttk.Entry(self.Frame_Matrix)
        self.TEntry1_11.place(relx=0.071, rely=0.816, relheight=0.127
                , relwidth=0.143, bordermode='ignore')
        self.TEntry1_11.configure(textvariable=MainWindow_support.matrix40)
        self.TEntry1_11.configure(width=40)
        self.TEntry1_11.configure(takefocus="")
        #self.TEntry1_11.configure(cursor="ibeam")

        self.TEntry1_11 = ttk.Entry(self.Frame_Matrix)
        self.TEntry1_11.place(relx=0.25, rely=0.816, relheight=0.127
                , relwidth=0.143, bordermode='ignore')
        self.TEntry1_11.configure(textvariable=MainWindow_support.matrix41)
        self.TEntry1_11.configure(width=40)
        self.TEntry1_11.configure(takefocus="")
        #self.TEntry1_11.configure(cursor="ibeam")

        self.TEntry1_11 = ttk.Entry(self.Frame_Matrix)
        self.TEntry1_11.place(relx=0.429, rely=0.816, relheight=0.127
                , relwidth=0.143, bordermode='ignore')
        self.TEntry1_11.configure(textvariable=MainWindow_support.matrix42)
        self.TEntry1_11.configure(width=40)
        self.TEntry1_11.configure(takefocus="")
        #self.TEntry1_11.configure(cursor="ibeam")

        self.TEntry1_11 = ttk.Entry(self.Frame_Matrix)
        self.TEntry1_11.place(relx=0.607, rely=0.816, relheight=0.127
                , relwidth=0.143, bordermode='ignore')
        self.TEntry1_11.configure(textvariable=MainWindow_support.matrix43)
        self.TEntry1_11.configure(width=40)
        self.TEntry1_11.configure(takefocus="")
        #self.TEntry1_11.configure(cursor="ibeam")

        self.TEntry1_11 = ttk.Entry(self.Frame_Matrix)
        self.TEntry1_11.place(relx=0.786, rely=0.816, relheight=0.127
                , relwidth=0.143, bordermode='ignore')
        self.TEntry1_11.configure(textvariable=MainWindow_support.matrix44)
        self.TEntry1_11.configure(width=40)
        self.TEntry1_11.configure(takefocus="")
        #self.TEntry1_11.configure(cursor="ibeam")

        self.Frame_Border_Select = tk.LabelFrame(top)
        self.Frame_Border_Select.place(relx=0.78, rely=0.0, relheight=0.783, relwidth=0.211)
        self.Frame_Border_Select.configure(relief='groove')
        self.Frame_Border_Select.configure(font=font9)
        self.Frame_Border_Select.configure(foreground="black")
        self.Frame_Border_Select.configure(text='''Border''')
        self.Frame_Border_Select.configure(background="#d9d9d9")
        self.Frame_Border_Select.configure(highlightbackground="#d9d9d9")
        self.Frame_Border_Select.configure(highlightcolor="black")
        self.Frame_Border_Select.configure(width=130)

        self.Radiobutton_Extend = tk.Radiobutton(self.Frame_Border_Select)
        self.Radiobutton_Extend.place(relx=0.077, rely=0.122, relheight=0.151, relwidth=0.592, bordermode='ignore')
        self.Radiobutton_Extend.configure(activebackground="#ececec")
        self.Radiobutton_Extend.configure(activeforeground="#000000")
        self.Radiobutton_Extend.configure(background="#d9d9d9")
        self.Radiobutton_Extend.configure(disabledforeground="#a3a3a3")
        self.Radiobutton_Extend.configure(foreground="#000000")
        self.Radiobutton_Extend.configure(highlightbackground="#d9d9d9")
        self.Radiobutton_Extend.configure(highlightcolor="black")
        self.Radiobutton_Extend.configure(justify='left')
        self.Radiobutton_Extend.configure(text='''Extend''')
        self.Radiobutton_Extend.configure(value="0")
        self.Radiobutton_Extend.configure(variable=MainWindow_support.borderAction)
        self.Radiobutton_Extend.configure(anchor='w')

        self.Radiobutton_Wrap = tk.Radiobutton(self.Frame_Border_Select)
        self.Radiobutton_Wrap.place(relx=0.077, rely=0.286, relheight=0.151
                , relwidth=0.592, bordermode='ignore')
        self.Radiobutton_Wrap.configure(activebackground="#ececec")
        self.Radiobutton_Wrap.configure(activeforeground="#000000")
        self.Radiobutton_Wrap.configure(background="#d9d9d9")
        self.Radiobutton_Wrap.configure(disabledforeground="#a3a3a3")
        self.Radiobutton_Wrap.configure(foreground="#000000")
        self.Radiobutton_Wrap.configure(highlightbackground="#d9d9d9")
        self.Radiobutton_Wrap.configure(highlightcolor="black")
        self.Radiobutton_Wrap.configure(justify='left')
        self.Radiobutton_Wrap.configure(text='''Wrap''')
        self.Radiobutton_Wrap.configure(value="1")
        self.Radiobutton_Wrap.configure(variable=MainWindow_support.borderAction)
        self.Radiobutton_Wrap.configure(anchor='w')

        self.Radiobutton_Mirror = tk.Radiobutton(self.Frame_Border_Select)
        self.Radiobutton_Mirror.place(relx=0.077, rely=0.449, relheight=0.151
                , relwidth=0.592, bordermode='ignore')
        self.Radiobutton_Mirror.configure(activebackground="#ececec")
        self.Radiobutton_Mirror.configure(activeforeground="#000000")
        self.Radiobutton_Mirror.configure(background="#d9d9d9")
        self.Radiobutton_Mirror.configure(disabledforeground="#a3a3a3")
        self.Radiobutton_Mirror.configure(foreground="#000000")
        self.Radiobutton_Mirror.configure(highlightbackground="#d9d9d9")
        self.Radiobutton_Mirror.configure(highlightcolor="black")
        self.Radiobutton_Mirror.configure(justify='left')
        self.Radiobutton_Mirror.configure(text='''Mirror''')
        self.Radiobutton_Mirror.configure(value="2")
        self.Radiobutton_Mirror.configure(variable=MainWindow_support.borderAction)
        self.Radiobutton_Mirror.configure(anchor='w')

        self.Entry_Divisor = tk.Entry(top)
        self.Entry_Divisor.place(relx=0.602, rely=0.064, height=26, relwidth=0.088)
        self.Entry_Divisor.configure(background="white")
        self.Entry_Divisor.configure(disabledforeground="#a3a3a3")
        self.Entry_Divisor.configure(font="TkFixedFont")
        self.Entry_Divisor.configure(foreground="#000000")
        self.Entry_Divisor.configure(highlightbackground="#d9d9d9")
        self.Entry_Divisor.configure(highlightcolor="black")
        self.Entry_Divisor.configure(insertbackground="black")
        self.Entry_Divisor.configure(selectbackground="#c4c4c4")
        self.Entry_Divisor.configure(selectforeground="black")
        self.Entry_Divisor.configure(textvariable=MainWindow_support.divisor)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.488, rely=0.064, height=31, width=70)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Divisor:''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Presets")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                command=lambda:MainWindow_support.setPreset("sharpen"),
                font="TkMenuFont",
                foreground="#000000",
                label="Sharpen")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                command=lambda:MainWindow_support.setPreset("box_blur"),
                font="TkMenuFont",
                foreground="#000000",
                label="Box_Blur")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                command=lambda:MainWindow_support.setPreset("gaussian_blur_3x3"),
                font="TkMenuFont",
                foreground="#000000",
                label="Gaussian_blur(3x3)")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                command=lambda:MainWindow_support.setPreset("gaussian_blur_5x5"),
                font="TkMenuFont",
                foreground="#000000",
                label="Gaussian_Blur(5x5)")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                command=lambda:MainWindow_support.setPreset("emboss"),
                font="TkMenuFont",
                foreground="#000000",
                label="Emboss")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                command=lambda:MainWindow_support.setPreset("unsharpen"),
                font="TkMenuFont",
                foreground="#000000",
                label="Unsharpen")

        self.Save = tk.Button(top)
        self.Save.place(relx=0.878, rely=0.831, height=42, width=67)
        self.Save.configure(activebackground="#ececec")
        self.Save.configure(activeforeground="#000000")
        self.Save.configure(background="#d9d9d9")
        self.Save.configure(command= lambda: MainWindow_support.save(self))
        self.Save.configure(disabledforeground="#a3a3a3")
        self.Save.configure(foreground="#000000")
        self.Save.configure(highlightbackground="#d9d9d9")
        self.Save.configure(highlightcolor="black")
        self.Save.configure(pady="0")
        self.Save.configure(text='''SAVE !''')

        self.openFile = tk.Button(top, command= lambda:MainWindow_support.openfile(self))
        self.openFile.place(relx=0.016, rely=0.831, height=42, width=139)
        self.openFile.configure(activebackground="#ececec")
        self.openFile.configure(activeforeground="#000000")
        self.openFile.configure(background="#d9d9d9")
        self.openFile.configure()
        self.openFile.configure(disabledforeground="#a3a3a3")
        self.openFile.configure(foreground="#000000")
        self.openFile.configure(highlightbackground="#d9d9d9")
        self.openFile.configure(highlightcolor="black")
        self.openFile.configure(pady="0")
        self.openFile.configure(text='''Select an image''')

        self.ApplyConvolution = tk.Button(top)
        self.ApplyConvolution.place(relx=0.585, rely=0.831, height=42, width=62)
        self.ApplyConvolution.configure(activebackground="#ececec")
        self.ApplyConvolution.configure(activeforeground="#000000")
        self.ApplyConvolution.configure(background="#d9d9d9")
        self.ApplyConvolution.configure(command=lambda:MainWindow_support.applyConvolution(self))
        self.ApplyConvolution.configure(disabledforeground="#a3a3a3")
        self.ApplyConvolution.configure(foreground="#000000")
        self.ApplyConvolution.configure(highlightbackground="#d9d9d9")
        self.ApplyConvolution.configure(highlightcolor="black")
        self.ApplyConvolution.configure(pady="0")
        self.ApplyConvolution.configure(text='''Preview''')

        self.checkbutton_grayscale = tk.Checkbutton(top)
        self.checkbutton_grayscale.place(relx=0.488, rely=0.224, relheight=0.118, relwidth=0.171)
        self.checkbutton_grayscale.configure(activebackground="#ececec")
        self.checkbutton_grayscale.configure(activeforeground="#000000")
        self.checkbutton_grayscale.configure(background="#d9d9d9")
        self.checkbutton_grayscale.configure(disabledforeground="#a3a3a3")
        self.checkbutton_grayscale.configure(foreground="#000000")
        self.checkbutton_grayscale.configure(highlightbackground="#d9d9d9")
        self.checkbutton_grayscale.configure(highlightcolor="black")
        self.checkbutton_grayscale.configure(justify='left')
        self.checkbutton_grayscale.configure(text='''Grayscale''')
        self.checkbutton_grayscale.configure(anchor='w')
        self.checkbutton_grayscale.configure(variable=MainWindow_support.grayscale)

        self.checkbutton_resize = tk.Checkbutton(top)
        self.checkbutton_resize.place(relx=0.488, rely=0.35, relheight=0.118, relwidth=0.171)
        self.checkbutton_resize.configure(activebackground="#ececec")
        self.checkbutton_resize.configure(activeforeground="#000000")
        self.checkbutton_resize.configure(background="#d9d9d9")
        self.checkbutton_resize.configure(disabledforeground="#a3a3a3")
        self.checkbutton_resize.configure(foreground="#000000")
        self.checkbutton_resize.configure(highlightbackground="#d9d9d9")
        self.checkbutton_resize.configure(highlightcolor="black")
        self.checkbutton_resize.configure(justify='left')
        self.checkbutton_resize.configure(text='''Resize(faster)''')
        self.checkbutton_resize.configure(variable=MainWindow_support.resize)
        self.checkbutton_resize.configure(anchor='w')


        self.progressbar = ttk.Progressbar(root, variable=MainWindow_support.progress_var, maximum=1)
        self.progressbar.place(relx=0.485, rely=0.631, height=20, width=175)

if __name__ == '__main__':
    vp_start_gui()




