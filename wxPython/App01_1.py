import wx  # Import wxPython Module

app = wx.App(clearSigInt=True)

# A Frame is a Representation of a Window - Wx.Frame (parent, id, title, pos, size, style, name)
frame = wx.Frame(parent=None, id=wx.ID_ANY, title='App00', pos = (500, 300))
panel = wx.Panel(parent=frame, id=wx.ID_ANY)
welcomeText = wx.StaticText(parent=panel, label='hello, world!!!', pos=(20,20))

frame.Show() 
app.MainLoop()