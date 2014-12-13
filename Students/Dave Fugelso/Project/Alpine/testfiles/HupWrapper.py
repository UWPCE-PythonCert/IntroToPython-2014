
#////////////////////////////////////////////////////////////////////////////////////////////////////
# Image Request

# This expects the body to contain the appId and a path of a locally stored image file
class AlpineFetchImageResponseHandler(ResponseHandler):
   def response(self, responseCode, headers, mimeType, body):
      print 'have image for : ' + headers
      try:
         d = json.loads(body)
         if (d.has_key('path') and d.has_key('appId'):
            #TBD: Check if appId is still current appId 
            SendImage (d['path'], d['appId'])
         else:
            print 'Bad format for SendImage'
       except:
         print 'bad json into response handler for image request'
         

def imageRequest (d):
	eb.request('GET','/RequestImage/', None, json.dumps(d),'application/json',[], AlpineFetchImageResponseHandler())


   
# This will be replaced by Configurator! 
def RegisterHandlers (eb):
	# Except these. These are not MIP callback handlers
	HupInterface.requestCallback('RequestImage', imageRequest)
   imageHandler = 
   
   
#////////////////////////////////////////////////////////////////////////////////////////////////////
# Register callbacks for Alpine initiated request
  def setup():
    global srv, eb, myHandler 
   
   
    #handler1 = AlpineRequestHandler('HeadUnitID', RequestHeadUnitID)
    #handler3 = AlpineRequestHandler('SetTemplate1', template1)
    myHandler = MyResponseHandler()


    # HttpGatewayRequestHandler is currently stubbed out and will be fixed by Jack Friday morning.
    handler2 = HttpGatewayRequestHandler(btMCSSF, host=address_to_handset, port=port_of_handset_server)

    # Template 1 handler

    eb = EventBroker()

   RegisterHandlers (eb)