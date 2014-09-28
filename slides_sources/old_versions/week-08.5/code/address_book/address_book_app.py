#!/usr/bin/env python

"""
Example of a very basic, minimal wxPython address book application

This module defines the main Frame

"""

import os

import wx
from address_book_data import AddressBook
from entry_form import AddBookForm
from switcher import Switcher
        
class AddBookFrame(wx.Frame):
    def __init__(self, add_book, *args, **kwargs):
        """
        initilizer for the main from for the AddressBook app.

        :param add_book: the address book class to manipulate
        :type add_book: A address_book_data.AddressBook instance

        """

        kwargs.setdefault('title', "Micro Address Book")
        wx.Frame.__init__(self, *args, **kwargs)

        self.add_book = add_book
        self.current_index = 0

        # creae a status bar for messages...
        self.CreateStatusBar()

        # create the entryPanel
        self.entryPanel = AddBookForm(add_book.book[self.current_index], self)
        
        # put them in a Sizer to lay out
        S = wx.BoxSizer(wx.VERTICAL)
        S.Add(wx.StaticLine(self,style=wx.LI_HORIZONTAL), 0, wx.EXPAND)
        S.Add(self.entryPanel, 0, wx.ALL|wx.EXPAND, 4)
        S.Add((1,5))
        S.Add(wx.StaticLine(self,style=wx.LI_HORIZONTAL), 0, wx.EXPAND)

        self.SetSizerAndFit(S)

        # Build up the menu bar:
        menuBar = wx.MenuBar()
        
        fileMenu = wx.Menu()

        closeMenuItem = fileMenu.Append(wx.ID_EXIT, "&Close", "Close the file" )
        self.Bind(wx.EVT_MENU, self.onClose, closeMenuItem)

        exitMenuItem = fileMenu.Append(wx.ID_EXIT, "Exit", "Exit the application")
        self.Bind(wx.EVT_MENU, self.onExit, exitMenuItem)
        menuBar.Append(fileMenu, "&File")
        
        helpMenu = wx.Menu()
        helpMenuItem = helpMenu.Append(wx.ID_HELP, "Help", "Get help")
        menuBar.Append(helpMenu, "&Help")

        self.SetMenuBar(menuBar)
    
    def next(self):
        """
        move to the next record in the address book
        """
        try:
            self.entryPanel.entry = self.add_book.book[self.current_index+1]
            self.current_index+=1
        except IndexError:
            print "At end of records...."

    def previous(self):
        """
        move to the next record in the address book
        """
        if self.current_index > 0:
            self.current_index-=1
            self.entryPanel.entry = self.add_book.book[self.current_index]

    def onNewRecord(self, evt=None):
        index = self.add_book.new_record()
        self.entryPanel.entry = self.add_book.book[index]

    def onOpen(self, evt=None):
        """This method opens an existing file"""
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
            self.add_book.load_from_file(filename=path)
        else :
            print "The file dialog was canceled"
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
    import wx.lib.inspection
    wx.lib.inspection.InspectionTool().Show()
    app.MainLoop()

