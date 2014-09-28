#!/usr/bin/env python

"""
Example of the very basic, minimal framework for a wxPython application.
"""

import wx

class TestFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('title', "Simple test App")
        wx.Frame.__init__(self, *args, **kwargs)


class TestApp(wx.App):
    def OnInit(self):
        """
        App initilization goes here -- not much to do in this case
        """
        f = TestFrame(None)
        f.Show()

        return True

if __name__ == "__main__":
    app = TestApp(False)
    app.MainLoop()

