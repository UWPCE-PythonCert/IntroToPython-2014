# 
# TestHarness.py
# Copyright (c) 2014 Airbiquity
#
# The tester emulates the body of requests coming over the network interface 
#     

import sys
import threading
import json
import time
import Templates
import FileCache
import logger

# Remove this import if non interface to Alpine
import HupInterface

msglogger  = logger.Logger()


'''
The following are test for the Template interface
'''

def testTemplate1 (filename):
   #print 'template1 file: ' + filename
   #msglogger.logMessage(logger.DEBUG, 'testTemplate1', filename)
   try:
      with open(filename) as tmp1_file:
         t = Templates.Template1 ()
         t.HandleRequest (tmp1_file.read())
         #print json.dumps(tmp1_file, indent=2)
   except IOError as e:
      print 'File read error' # TBD goes to error handler

def testTemplate2 (filename):
   try:
      with open(filename) as tmp1_file:
         t = Templates.Template2 ()
         t.HandleRequest (tmp1_file.read())
         #print json.dumps(tmp1_file, indent=2)
   except IOError as e:
      print 'File read error' # TBD goes to error handler

def testTemplate3 (filename):
   try:
      with open(filename) as tmp1_file:
         t = Templates.Template3 ()
         t.HandleRequest (tmp1_file.read())
         #print json.dumps(tmp1_file, indent=2)
   except IOError as e:
      print 'File read error' # TBD goes to error handler
      
def testTemplate4 (filename):
   try:
      with open(filename) as tmp1_file:
         t = Templates.Template4 ()
         t.HandleRequest (tmp1_file.read())
         #print json.dumps(tmp1_file, indent=2)
   except IOError as e:
      print 'File read error' # TBD goes to error handler

def testTemplate5 (filename):
   try:
      with open(filename) as tmp1_file:
         t = Templates.Template5 ()
         t.HandleRequest (tmp1_file.read())
         #print json.dumps(tmp1_file, indent=2)
   except IOError as e:
      print 'File read error' # TBD goes to error handler
      
def testTemplate6 (filename):
   try:
      with open(filename) as tmp1_file:
         t = Templates.Template6 ()
         t.HandleRequest (tmp1_file.read())
         #print json.dumps(tmp1_file, indent=2)
   except IOError as e:
      print 'File read error' # TBD goes to error handler
      
def testTemplate7 (filename):
   try:
      with open(filename) as tmp1_file:
         t = Templates.Template7 ()
         t.HandleRequest (tmp1_file.read())
         #print json.dumps(tmp1_file, indent=2)
   except IOError as e:
      print 'File read error' # TBD goes to error handler
            
def testTemplate8 (filename):
   try:
      with open(filename) as tmp1_file:
         t = Templates.Template8 ()
         t.HandleRequest (tmp1_file.read())
         #print json.dumps(tmp1_file, indent=2)
   except IOError as e:
      print 'File read error' # TBD goes to error handler
      
   
def testApplicationList(filename):
   try:
      with open(filename) as tmp1_file:
         t = Templates.SendApplicationInformation()
         t.HandleRequest (tmp1_file.read())
         #print json.dumps(tmp1_file, indent=2)
   except IOError as e:
      print 'File read error' # TBD goes to error handler

def testNowExecuting(filename):
   try:
      with open(filename) as tmp1_file:
         t = Templates.RequestNowExecutingInfomation()
         t.HandleRequest(tmp1_file.read())
   except IOError as e:
      print 'File read error nowExecuting.json'

def	testRequestAudioFocus(filename):
	try:
		with open(filename) as tmp1_file:
			t = Templates.RequestAudioFocusInformation()
			t.HandleRequest(tmp1_file.read())
	except IOError as e:
		print 'File read error requestAudioFocus.json'
		
def	testSetLocation(filename):
	try:
		with open(filename) as tmp1_file:
			t = Templates.RequestSetLocationInformation()
			t.HandleRequest(tmp1_file.read())
	except IOError as e:
		print 'File read error setlocation.json'

def   testPhoneIsAvailable(filename):
   try:
      with open(filename) as tmp1_file:
         t = Templates.RequestSetPhoneAvailabilityInformation()
         t.HandleRequest(tmp1_file.read())
   except IOError as e:
      print 'File read error setPhoneAvailability.json'
      
def   testGoToKeyboard():
   t = Templates.RequestRequestGoToKeyboard()
   t.HandleRequest()
   
def startMIPApp ():
	dictionary = dict()
	dict['appType'] = 1
	dict['appName'] = 'Pandora'
	# Create event broker with path '/hap/api/1.0/StartApplication'
	# and json code json.dumps(dict)

      

# Removed Native Platform Testing for TestHarness for template testers. Creating separate 
# Native Platform Test Harness.
 

def starttest(testfilepath):

    msglogger.logMessage(logger.DEBUG, 'starttest', 'start')
 
  
    #print 'Make a connection'
    #MakeAConnection()
    #time.sleep(5)
    #print 'Done with connection'
   
    # print 'test NowExecuting'
    # testNowExecuting(testfilepath + 'nowExecuting.json')
    # print 'test RequestAudioFocus'
    # testRequestAudioFocus(testfilepath + 'requestAudioFocus.json')
    # print 'test setLocation'
    # testSetLocation(testfilepath + 'setlocation.json')
    # print 'test PhoneIsAvailable'
    # testPhoneIsAvailable(testfilepath + 'setPhoneAvailability.json')
    # print 'test GoToKeyboard'
    # testGoToKeyboard()
    # time.sleep(2)


    testTemplate1( testfilepath + 'template1A.json' )
    print 'testTemplate1A done.'
    time.sleep(2)
	
    # testTemplate1( testfilepath + 'template1A2.json' )
    # print 'testTemplate1A2 done.'
    # time.sleep (3)

    # testTemplate1( testfilepath + 'template1A3.json' )
    # print 'testTemplate1A3 done.'
    # time.sleep(2)
	
    # testTemplate1( testfilepath + 'template1B.json' )
    # print 'testTemplate1B done.'
    # time.sleep(2)
	
    # testTemplate2(testfilepath + 'template2A.json')
    # print 'testTemplate2A done.'	
    # time.sleep(2)
	
    # testTemplate2(testfilepath + 'template2B.json')
    # print 'testTemplate2B done.'	
    # time.sleep(2)
	
    # testTemplate3(testfilepath + 'template3A.json')
    # print 'testTemplate3A done.'	
    # time.sleep(2)

    # testTemplate3(testfilepath + 'template3B.json')
    # print 'testTemplate3B done.'  
    # time.sleep(2)
   
    # testTemplate4(testfilepath + 'template4A.json')
    # print 'testTemplate4A done.'  
    # time.sleep(2)

    # testTemplate4(testfilepath + 'template4B.json')
    # print 'testTemplate4B done.'	
    # time.sleep(2)
	
    # testTemplate5(testfilepath + 'template5.json')
    # print 'testTemplate5 done.'	
    # time.sleep(2)

    # testTemplate6(testfilepath + 'template6.json')
    # print 'testTemplate6 done.'	
    # time.sleep(2)

    # testTemplate7(testfilepath + 'template7.json')
    # print 'testTemplate7 done.'	
    # time.sleep(2)

    # testTemplate8(testfilepath + 'template8A.json')
    # print 'testTemplate8A done.'	
    # time.sleep(2)

    # testTemplate8(testfilepath + 'template8B.json')
    # print 'testTemplate8B done.'	
    # time.sleep(2)
	
    # testApplicationList(testfilepath + 'applications.json')	

    #uncomment following to run an infinite loop to test incoming messages
    # otherwise execution will end at the end of this script.
    while (True):
        time.sleep(1)

    
    print 'Okay we\'re done.'
    HupInterface.stopHupInterface()

    print 'call exit'
    exit()
   

'''
Run tests as needed. Modify json files in testfiles to get different behaviors on tempaltes.
'''
if __name__ == "__main__":
    HupInterface.startHupInterface()
    starttest('testfiles/')
