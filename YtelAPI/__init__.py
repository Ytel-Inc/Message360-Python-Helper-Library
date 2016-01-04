import base64
import hmac
import json
from hashlib import sha1
import YtelConstant

import requests



try:
    import json
except ImportError:
    import simplejson as json




class YtelError(Exception):
    pass

class Message360API(object):
    def __init__(self, auth_id, auth_token, url=YtelConstant.Constant.BASE_URL):
        self.version = YtelConstant.Constant.VERSION
        self.url = url.rstrip('/') + self.version
        self.auth_id = auth_id
        self.auth_token = auth_token
        self._api = self.url 
        self.headers = {'User-Agent':'YTEL'}
        print self._api
    def _request(self, method, path, data={}):
        path = path.rstrip('/') 
       
        if method == 'POST':
            headers = {'content-type': 'application/%s'%YtelConstant.Constant.RESPONSE_TYPE}
            headers.update(self.headers)
            r = requests.post(self._api + path, headers=headers,
                              auth=(self.auth_id, self.auth_token),
                              params=json.dumps(data))
        elif method == 'GET':
            r = requests.get(self._api + path, headers=self.headers,
                             auth=(self.auth_id, self.auth_token),
                             params=data)
        elif method == 'DELETE':
            r = requests.delete(self._api + path, headers=self.headers,
                                auth=(self.auth_id, self.auth_token),
                                params=data)
        content = r.content
        return content

    @staticmethod
    def get_param(params, key):
        try:
            return params[key]
        except KeyError:
            raise YtelError("missing mandatory parameter %s" % key)

    ## Accounts ##
    def view_account(self, params=None):
        if not params: params = {}
        return self._request('GET', '/accounts/viewaccount.%s'%YtelConstant.Constant.RESPONSE_TYPE, data=params)
    
    ## Usage ##
    def list_usage(self, params=None):
        if not params: params = {}
        return self._request('GET', '/usage/listusage.%s'%YtelConstant.Constant.RESPONSE_TYPE, data=params)
    
    ## SMS ##
    def view_sms(self, params=None):
        if not params:params ={};
        smssid = params.pop("smssid")
        return self._request('POST', '/sms/viewsms/%s.%s' %(smssid ,YtelConstant.Constant.RESPONSE_TYPE), data=params)
    
    def list_sms(self, params=None):
        if not params:params ={};
        return self._request('GET', '/sms/listsms.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)
    
    def send_sms(self, params=None):
        if not params:params ={};
        return self._request('GET', '/sms/sendsms.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)
    
    def inbound_sms(self, params=None):
        if not params:params ={};
        return self._request('GET', '/sms/getInboundsms.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)
    
    def optins_sms(self, params=None):
        if not params:params ={};
        return self._request('GET', '/sms/numberoptin.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)
    
    ## CALL ##
    def view_call(self, params=None):
        if not params:params ={};
        callsid = params.pop("callsid")
        return self._request('POST', '/calls/viewcalls/%s.%s' %(callsid ,YtelConstant.Constant.RESPONSE_TYPE), data=params)

    def list_call(self, params=None):
        if not params:params ={};
        return self._request('GET', '/calls/listcalls.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    def make_call(self, params=None):
        if not params:params ={};
        return self._request('GET', '/calls/makecall.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)	   
    
    def interrupt_call(self, params=None):
        if not params:params ={};
        return self._request('GET', '/calls/interruptcalls.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params) 
   
    def senddigits_call(self, params=None):
        if not params:params ={};
        return self._request('GET', '/calls/senddigits.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)
    
    def playaudios_call(self, params=None):
        if not params:params ={};
        return self._request('GET', '/calls/playaudios.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    def voiceeffect_call(self, params=None):
        if not params:params ={};
        return self._request('GET', '/calls/voiceeffect.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    def recordcalls_call(self, params=None):
        if not params:params ={};
        return self._request('GET', '/calls/recordcalls.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    ## CONFERENCE ##
    def viewconference_call(self, params=None):
        if not params:params ={};
        return self._request('GET', '/conferences/viewconference.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    def listconference_call(self, params=None):
        if not params:params ={};
        return self._request('GET', '/conferences/listconference.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    def addParticipant_call(self, params=None):
        if not params:params ={};
        return self._request('GET', '/Conferences/addParticipant.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    def viewparticipant_call(self, params=None):
        if not params:params ={};
        return self._request('GET', '/conferences/viewparticipant.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    def listparticipant_call(self, params=None):
        if not params:params ={};
        return self._request('GET', '/conferences/listparticipant.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    def DeafMuteParticipantAPI_call(self, params=None):
        if not params:params ={};
        return self._request('GET', '/Conferences/deafMuteParticipant.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    def hangupParticipantAPI_call(self, params=None):
        if not params:params ={};
        return self._request('GET', '/Conferences/hangupParticipant.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    def playAudioAPI_call(self, params=None):
        if not params:params ={};
        return self._request('GET', '/Conferences/playAudio.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    ## Phone Numbers ##
    def availablenumber(self, params=None):
        if not params:params ={};
        return self._request('GET', '/incomingphone/availablenumber.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    def viewnumber(self, params=None):
        if not params:params ={};
	Phone_Number = params.pop("Phone_Number")
        return self._request('GET', '/incomingphone/viewnumber/%s.%s' %(Phone_Number, YtelConstant.Constant.RESPONSE_TYPE), data=params)

    def listnumber(self, params=None):
        if not params:params ={};
        return self._request('GET', '/incomingphone/listnumber.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    def Buy_Number(self, params=None):
        if not params:params ={};
        return self._request('GET', '/incomingphone/buynumber.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    def Update_Number(self, params=None):
        if not params:params ={};
        return self._request('GET', '/incomingphone/updatenumber.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    def Release_Number(self, params=None):
        if not params:params ={};
	IncomingPhoneNumberSid = params.pop("IncomingPhoneNumberSid")
        return self._request('DELETE', '/incomingphone/releasenumber/%s.%s' %(IncomingPhoneNumberSid, YtelConstant.Constant.RESPONSE_TYPE), data=params)

    ## Recording ##
    def viewRecording(self, params=None):
        if not params:params ={};
        RecordingId = params.pop("RecordingId")
        return self._request('GET', '/recording/viewrecording/%s.%s' %(RecordingId, YtelConstant.Constant.RESPONSE_TYPE), data=params)
   
    def listRecording(self, params=None):
        if not params:params ={};
        return self._request('GET', '/recording/listrecording.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    def deleteRecording(self, params=None):
        if not params:params ={};
        RecordingId = params.pop("RecordingId")
        return self._request('DELETE', '/recording/deleterecording/%s.%s' %(RecordingId, YtelConstant.Constant.RESPONSE_TYPE), data=params)	

    ## Transcription ##

    def viewTranscription(self, params=None):
        if not params:params ={};
        transcriptionsid = params.pop("transcriptionsid")
        return self._request('GET', '/transcriptions/viewtranscription/%s.%s' %(transcriptionsid, YtelConstant.Constant.RESPONSE_TYPE), data=params)

    def listTranscription(self, params=None):
        if not params:params ={};
        return self._request('GET', '/transcriptions/listtranscription.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    def Transcribe_Audio_URL(self, params=None):
        if not params:params ={};
        return self._request('GET', '/transcriptions/audiourltranscription.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    def Transcribe_Recording(self, params=None):
        if not params:params ={};
        return self._request('GET', '/transcriptions/recordingtranscription.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    ## Email ##

    def Send_Email(self, params=None):
        if not params:params ={};
        return self._request('GET', '/email/sendemails.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    def List_Blocks_Email(self, params=None):
        if not params:params ={};
        return self._request('GET', '/email/listblockemail.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    def Delete_Blocks_Email_Address(self, params=None):
        if not params:params ={};
	Email = params.pop("Email")
        return self._request('GET', '/email/deleteblocksemail/%s.%s' %(Email, YtelConstant.Constant.RESPONSE_TYPE), data=params)

    def List_Bounces_Email(self, params=None):
        if not params:params ={};
        return self._request('GET', '/email/listbounceemail.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    def Delete_Blocks_Email_Address(self, params=None):
        if not params:params ={};
        Email = params.pop("Email")
        return self._request('GET', '/email/deletebouncesemail/%s.%s' %(Email, YtelConstant.Constant.RESPONSE_TYPE), data=params)

    def List_Spam_Reports(self, params=None):
        if not params:params ={};
        return self._request('GET', '/email/listspamemail.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    def Delete_Spam_Reports(self, params=None):
        if not params:params ={};
        Email = params.pop("Email")
        return self._request('GET', '/email/deletespamemail/%s.%s' %(Email, YtelConstant.Constant.RESPONSE_TYPE), data=params)

    def List_Invalid_Emails(self, params=None):
        if not params:params ={};
        return self._request('GET', '/email/listinvalidemail.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    def Delete_Invalid_Emails(self, params=None):
        if not params:params ={};
        Email = params.pop("Email")
        return self._request('GET', '/email/deleteinvalidemail/%s.%s' %(Email, YtelConstant.Constant.RESPONSE_TYPE), data=params)

    def Add_Unsubscribes_Email_Address(self, params=None):
        if not params:params ={};
        return self._request('GET', '/email/addunsubscribesemail.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)

    def List_Unsubscribes_Email_Address(self, params=None):
        if not params:params ={};
        return self._request('GET', '/email/listunsubscribedemail.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)
    
    def Delete_Unsubscribes_Email_Address(self, params=None):
        if not params:params ={};
        Email = params.pop("Email")
        return self._request('GET', '/email/deleteunsubscribedemail/%s.%s' %(Email, YtelConstant.Constant.RESPONSE_TYPE), data=params)
 
    ## Carrier ##
	
    def Carrier_Lookup(self, params=None):
        if not params:params ={};
        return self._request('GET', '/carrier/lookup.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params)	

    def Carrier_Lookup_List(self, params=None):
        if not params:params ={};
        return self._request('GET', '/carrier/lookuplist.%s' %YtelConstant.Constant.RESPONSE_TYPE, data=params) 

