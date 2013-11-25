#!/usr/bin/env python

"""
A custom widget to switch between different entries in the address book

Subclassed from a wx.Panel
"""

import wx

class Switcher(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        """
        create a new swither instance.

        :param parent: the parent frame -- this is designed to go on an
                       AddBookFrame object


        :params *args, **kwargs: all the other arguments that a wx.Window takes.       
        """
        print "in __init__"
        wx.Panel.__init__(self, parent, *args, **kwargs)

        self.add_book_frame = parent

        ##Create the buttons to scroll through add_book_frame
        prev_button = wx.Button(self, label="Previous")
        prev_button.Bind(wx.EVT_BUTTON, self.onPrev)

        next_button = wx.Button(self, label="Next")
        next_button.Bind(wx.EVT_BUTTON, self.onNext)

        ## use a Sizer to lay it out
        S = wx.BoxSizer(wx.HORIZONTAL)

        S.Add(prev_button, 1, wx.ALL, 4)
        S.Add((10,1),0)
        S.Add(wx.StaticText(self,label="AddressBook"),
              0,
              wx.ALIGN_CENTER_HORIZONTAL|wx.ALL,
              4)
        S.Add((10,1),0)
        S.Add(next_button, 1,wx.ALL, 4)

        self.SetSizerAndFit(S)

    def onPrev(self, evt=None):
        # save the data in the form
        print "in onPrev" 
        self.add_book_frame.previous()
    def onNext(self, evt=None):
        # restore the form
        print "in onNext"
        self.add_book_frame.next()
class TestFrame(wx.Frame):
    """
    simple Frame with jsut enough to text the Switcher
    """
    def next(self):
        print "next() called in frame"
    def previous(self):
        print "previous() called in frame"

# I like to have a little test app so it can be run on its own
if __name__ == "__main__":

    app = wx.App(False)
    f = TestFrame(None)
    p = Switcher(f)
    f.Show()
    app.MainLoop()


