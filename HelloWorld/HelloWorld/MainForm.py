import System.Drawing
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
        self._label1.BackColor = System.Drawing.Color.DimGray
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 72, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Transparent
        self._label1.Location = System.Drawing.Point(110, 64)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(457, 246)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label1.Click += self.Label1Click
        # 
        # button1
        # 
        self._button1.ForeColor = System.Drawing.SystemColors.MenuHighlight
        self._button1.Location = System.Drawing.Point(26, 336)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(117, 58)
        self._button1.TabIndex = 2
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.ForeColor = System.Drawing.SystemColors.MenuHighlight
        self._button2.Location = System.Drawing.Point(265, 336)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(137, 58)
        self._button2.TabIndex = 3
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.ForeColor = System.Drawing.SystemColors.MenuHighlight
        self._button3.Location = System.Drawing.Point(513, 333)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(136, 65)
        self._button3.TabIndex = 4
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
        self.ClientSize = System.Drawing.Size(682, 420)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.ForeColor = System.Drawing.SystemColors.ActiveBorder
        self.Name = "MainForm"
        self.Text = "HelloWorld"
        self.ResumeLayout(False)


    def Label1Click(self, sender, e):
        pass

    def TextBox1TextChanged(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        self._label1.Text = "Hello, world!"

    def Button2Click(self, sender, e):
        self._label1.Text = " "

    def Button3Click(self, sender, e):
        Application.Exit()