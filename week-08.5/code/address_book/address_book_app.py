#!/usr/bin/env python

"""
Example of the very basic, minimal wxPython address book application

This module defines the main Frame
"""

import os

import wx
from address_book_data import AddressBook
from entry_form import AddBookForm
        
class AddBookFrame(wx.Frame):
    def __init__(self, add_book, *args, **kwargs):
        kwargs.setdefault('title', "Micro Address Book")
        wx.Frame.__init__(self, *args, **kwargs)

        self.add_book = add_book
        self.current_index = 1

        # put the Panel on the frame
        self.entryPanel = AddBookForm(add_book.book[self.current_index], self)

        # Build up the menu bar:
        menuBar = wx.MenuBar()
        
        fileMenu = wx.Menu()
        openMenuItem = fileMenu.Append(wx.ID_ANY, "&Open", "Open a file" )
        self.Bind(wx.EVT_MENU, self.onOpen, openMenuItem)

        closeMenuItem = fileMenu.Append(wx.ID_ANY, "&Close", "Close a file" )
        self.Bind(wx.EVT_MENU, self.onClose, closeMenuItem)

        exitMenuItem = fileMenu.Append(wx.ID_EXIT, "Exit", "Exit the application")
        self.Bind(wx.EVT_MENU, self.onExit, exitMenuItem)
        menuBar.Append(fileMenu, "&File")
        
        helpMenu = wx.Menu()
        helpMenuItem = helpMenu.Append(wx.ID_HELP, "Help", "Get help")
        menuBar.Append(helpMenu, "&Help")

        self.SetMenuBar(menuBar)
        
    def onOpen(self, evt=None):
        """This method opens an existing file"""
        print "Open a file: "
        # Create the dialog. In this case the current directory is forced as the starting
        # directory for the dialog, and no default file name is forced. This can easily
        # be changed in your program. This is an 'open' dialog, and allows multiple
        # file selections as well.
        #
        # Finally, if the directory is changed in the process of getting files, this
        # dialog is set up to change the current working directory to the path chosen.
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=os.getcwd(), 
            defaultFile="",
            wildcard="*.json",
            style=wx.OPEN | wx.CHANGE_DIR
            )

        # Show the dialog and retrieve the user response. If it is the OK response, 
        # process the data.
        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
            path = dlg.GetPath()
            print "I'd be opening file in onOpen ", path
            self.add_book.save_to_file( path )
        else :
            print "The file dialog was canceled before anything was selected"

        # Destroy the dialog. Don't do this until you are done with it!
        # BAD things can happen otherwise!
        dlg.Destroy()

    def onClose(self, evt=None):
        print "close menu selected"
        self.add_book.close()

    def onExit(self, evt=None):
        print "Exit the program here"
        print "The event passed to onExit is type ", type(evt),
        self.Close()


class AddBookApp(wx.App):
    def OnInit(self):
        """
        App initilization goes here -- not much to do, in this case
        """
        a_book = AddressBook()
        a_book.load_from_file()

        f = AddBookFrame(a_book, parent=None)
        f.Show()

        return True

if __name__ == "__main__":

    app = AddBookApp(False)



    ## set up the WIT -- to help debug sizers
#    import wx.lib.inspection
#    wx.lib.inspection.InspectionTool().Show()
    app.MainLoop()

