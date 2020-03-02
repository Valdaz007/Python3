import wx  # Import wxPython Module

def main():
    app = MyApp()
    app.MainLoop()


class MyApp(wx.App):
    
    def __init__(self):
        super().__init__(clearSigInt = True)

        #Initialize Frame
        self.InitFrame()

    def InitFrame(self):
        # Add Frame Contents Here
        frame = MyFrame(None, "App01", (200,200))
        frame.Show()

class MyFrame(wx.Frame):
    
    def __init__(self, parent, title, pos):
        super().__init__(parent = parent, title = title, pos = pos)

        self.OnInit()

    def OnInit(self):
        # Add Panels Here
        panel = MyPanel(self)

class MyPanel(wx.Panel):
    
    def __init__(self, parent):
        super().__init__(parent)
        # Add Panel Contents Here
        welcomeText = wx.StaticText(self, label='hello, world!!!', pos=(20,20))


if __name__ == '__main__':
    main()