'''
Python course project.

This implements templates for simulation.  Please see write up.

'''
import sys
from PyQt4.QtGui import QApplication, QDialog
from ui_template import *
from functools import partial



class Button (object):

    def __init__(self, *args, **kwargs):
        '''
        Store info for a button. The args are well known.
        '''
        print 'Add Button'
        print args
        self.text = args[0]
        self.normalImage = args[1]
        self.normalImagePressed = args[2]
        self.backgroundImage = args[3]
        self.backgroundImagePressed = args[4]
        self.scrollUpButton = args[5]
        self.scrollDownButton = args[5]
        self.enabled = args[6]
        self.key = -1
       
    @property
    def Key (self):
        return self.key   
        
    @Key.setter
    def Key(self, key):
        self.key = key
  
class pyqtTemplate(object):

    def __init__(self):
        self.Buttons = [None for i in range(9)]  #max nine buttons
        self.buttonIndex = 0
        self.partialUpdate = None     
        self.appId = None
        self.loadingType = None
        self.screenId = None
        self.backgroundImage = None
        self.systemHeader = None
        self.colrRGB = None
        self.current = None
        self.totlaseconds = None
        self.active = None
        self.path = None
        self.key = None
        self.callback = None
        
    def addButtons(self, *args, **kwargs):
        '''
        Add button to template. Buttons are sent in order.
        '''
        self.Buttons[self.buttonIndex] = Button(*args, **kwargs)
        self.buttonIndex += 1

    def clearButtonList(self):
        '''
        Clear list for next display.
        '''
        self.Buttons = [None for i in range(9)]  #max nine buttons
        
    def setContentTemplateHeader(self, *args, **kwargs):
        ''' 
        Set header informaiton.
        '''
        self.partialUpdate = args[0]     
        self.appId = args[1]
        self.loadingType = args[2]
        self.screenId = args[3]
        self.backgroundImage = args[4]
        self.systemHeader = args[5]

    def setContentProgressBar(self, *args, **kwargs):
        '''
        Progress bar update.
        '''
        self.colorRGB = args[0]
        self.current = args[1]
        self.totlaseconds = args[2]
        self.active = args[3]
        
    def sendImage (self, *args, **kwargs):
        '''
        Returns a request image. (Btw this calls a registered callback. This function would normal 
        call the registered callback, thus the 'Send' instead of 'Receive.'
        
        Also, this method would normally be asynchronous, but it isn't here. (It would find the right button based on key.)
        '''
        
        #find widget by name
        wid = getattr(self.ui, self.name)
        
        if isinstance(wid, QtGui.QLabel):
            print 'have Qlabel!'
            wid.setPixmap (QtGui.QPixmap(args[0]))
        else:
            icon  = QtGui.QPixmap(args[0])
            wid.setIcon(QtGui.QIcon(icon))
            size = wid.frameSize ()
            wid.setIconSize(QtCore.QSize(size.height(),size.width()))
            print self.button.key
            #wid.clicked.connect(lambda: self.buttonClick(self.button.Key))
            wid.clicked.connect(partial(self.buttonClick, self.button.Key))

 
    def startPlatformInitialization(self, alpineInterfaceCallback):
        '''
        This defines the callback function to make calls back into HUP. 
        '''
        self.callback = alpineInterfaceCallback
        
    def buttonClick (self, key):
        '''
        Pass a button click back to HUIP for processising.
        '''
        cbDict = {}
        cbDict['Index'] = key
        cbDict['templateId'] =  self.appId
        cbDict['type'] = 0
        self.callback('TemplateButtonPress', cbDict)

    
    def setContentTemplate1 (self, *args, **kwargs):
        buttonNames = ('btn01', 'btn02', 'btn03', 'btn04', 'btn05', 'btn06')
        print 'Template 1 display'
        self.image = args[0]
        self.titlestr = args[1]
        self.img01 = args[2]
        self.img02 = args[3]
        self.text01 = args[4]
        self.text02 = args[5]
        self.text03 = args[6]
        self.text04 = args[7]

        app = QApplication(sys.argv)
        window = QDialog()
        self.ui = Ui_Template1()
        self.ui.setupUi(window)
        
        #For each button gets its image ()
        processButtons = zip (buttonNames, self.Buttons, range(1,7))
        for self.name, self.button, self.buttonId in processButtons:
            '''
            Requests to HUP are dictionaries.
            '''
            request = {}
            request['ImageID'] = self.button.normalImage
            
            #register callback for button
            self.button.Key = self.buttonId   
            
            #request the image
            self.callback ('RequestImage', request)
            


            
        #Other images in the frameSize
        self.name = 'img01'
        request['ImageID'] = self.img01
        self.callback ('RequestImage', request)           
        self.name = 'img02'
        request['ImageID'] = self.img02
        self.callback ('RequestImage', request)           
           
        #Set the text field (normally this would take into consideration length to set size.
        wid = getattr(self.ui, 'imgtitle')
        wid.setText (QtCore.QString(self.titlestr))
        wid = getattr(self.ui, 'text01')
        wid.setText (QtCore.QString(self.text01))       
        wid = getattr(self.ui, 'text02')
        wid.setText (QtCore.QString(self.text02))       
        wid = getattr(self.ui, 'text03')
        wid.setText (QtCore.QString(self.text03))       
        wid = getattr(self.ui, 'text04')
        wid.setText (QtCore.QString(self.text04))       

        #Update progress bar
        wid = getattr(self.ui, 'text04')
        wid.setText (QtCore.QString(self.text04))
        wid = getattr(self.ui, 'progbar')
        wid.setMinimum(0)
        wid.setMaximum(self.totlaseconds)
        wid.setValue (self.current * self.totlaseconds)

        window.show()
        sys.exit(app.exec_())

# Instance of template 
P = pyqtTemplate ()
        
     
'''
These function simulate the C functions that is the real interface.
'''
def AddButton (*args, **kwargs):
    P.addButtons(*args, **kwargs)
    
def ClearButtonList ():
    P.clearButtonList()
    
def SetContentTemplateHeader(*args, **kwargs):
    P.setContentTemplateHeader(*args, **kwargs)

def SetContentProgressBar(*args, **kwargs):
    P.setContentProgressBar(*args, **kwargs)
    
def SendImage (*args, **kwargs):
    P.sendImage (*args, **kwargs)
    
def startPlatformInitialization(alpineInterfaceCallback):
    P.startPlatformInitialization(alpineInterfaceCallback)
    
def SetContentTemplate1 (*args, **kwargs):
    P.setContentTemplate1(*args, **kwargs)
    
'''
Unimplemented code. this allows me to replace the C module _HupInterface
'''
def SendNowExecuting (*arg, **kwargs):
    pass
    
def SendRequestAudioFocus(*arg, **kwargs):
    pass
    
def SendSetLocation(*arg, **kwargs):
    pass
    
def SendSetLocation(*arg, **kwargs):
    pass