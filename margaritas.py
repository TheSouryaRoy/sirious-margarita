"""
Margaritas handlers

"""

import urllib2

# TEMPLATE
MAKE = 'make'
BLEND = 'blend'

class Margaritas:
    """Interface with electric imp to run the margarita maker.
    """
    
    def __init__(self, url):
        self.imp_url = url
        self.count = 0

    def make(self):
        """Make a margarita
        
        Behavior:
            Margarita maker will make and pour the margarita.
            Refer to imp's code to set length of making and pouring. 
        """
        
        url = self.imp_url + '?value=0'
        
        # Call electrimp URL with value 0 to make a margarita
        try:
            result = urllib2.urlopen(url)
            success = True
            self.count = self.count + 1
        except urllib2.URLError, e:
            success = False
            
        return success
        
    def pour(self):
        """Pour a margarita
        
        Behavior:
            Margarita maker will only pour the margarita.
        """
        
        url = self.imp_url + '?value=1'
        
        # Call electrimp URL with value 1 to pour a margarita
        try:
            result = urllib2.urlopen(url)
            success = True
            self.count = self.count + 1
        except urllib2.URLError, e:
            success = False
            
        return success
        
    def getCount(self):
        """Return # of margaritas poured.
        """
        
        return self.count
        

class TwilioMargaritas:
    """Interface Twilio GET request with margarita handlers 
    """

    def __init__(self, url):
        self.last_req=None
        self.margarita_maker = Margaritas(url)        
    
    def ProcessRequest(self, request):
        """Process HTTP GET request from Twilio.
        """
        
        # get request text
        tw_Body = str(request.get('Body'))
        self.last_req=tw_Body
        
        success = False
        
        # check if they contain any value, if so update
        if len(tw_Body) > 0:
            
            if tw_Body.lower().split(' ')[0] == BLEND.lower():
                # If the first word is "blend" -> make+pour a margarita
                success = self.margarita_maker.make()
                     
            if tw_Body.lower().split(' ')[0] == MAKE.lower():
                # If the first word is "make" -> pour a margarita
                success = self.margarita_maker.pour()
                
        return success
        
    def getCount(self):
        """Return # of margaritas poured by margarita_maker
        """
        
        return self.margarita_maker.getCount()
                
    def getLastRequest(self):
        """Get the last request body
        """
        
        return self.last_req
        
        
