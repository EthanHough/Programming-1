﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 72, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Red
        self._label1.Location = System.Drawing.Point(127, 34)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(401, 273)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.ForeColor = System.Drawing.Color.Black
        self._button1.Location = System.Drawing.Point(65, 327)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(157, 84)
        self._button1.TabIndex = 1
        self._button1.Text = "My Name"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(243, 327)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(157, 84)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(424, 327)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(157, 84)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Red
        self.ClientSize = System.Drawing.Size(655, 423)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "MyName"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "Ethan"
        

    def Button2Click(self, sender, e):
        self._label1.Text = " "
        

    def Button3Click(self, sender, e):
        Application.Exit()