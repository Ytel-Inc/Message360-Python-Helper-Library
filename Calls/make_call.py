import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
	 'To': '9492080471', 			#Please enter the To number.
	 'From' : '2153832794',			#This number to display on Caller ID as calling
	 'FromCountryCode' : '1',				
	 'ToCountryCode' : '1',
	 'Url' : 'http://devweb.ytel.com/ytelapi/YTELAPI-10.php',			#URL requested once the call connects	
	 #'Method':'Post/Get',			#Specifies the HTTP method used to request the required URL once call connects
	 #'StatusCallBack':'example.com',	#URL that can be requested to receive notification when call has ended. A set of default parameters will be sent here once the call is finished
	 #'StatusCallBackMethod':'GET',		#Specifies the HTTP methodlinkclass used to request StatusCallbackUrl.
	 #'FallBackUrl':'example.com',		#URL requested if the initial Url parameter fails or encounters an error
	 #'FallBackMethod':'Get/Post',		#Specifies the HTTP method used to request the required FallbackUrl once call connects
	 #'HeartBeatUrl':'example.com',		#URL that can be requested every 60 seconds during the call to notify of elapsed time
	 #'HeartBeatMethod':'Post/Get',		#Specifies the HTTP method used to request HeartbeatUrl
	 #'Timeout':'XXXX',			#Time (in seconds) Message360 should wait while the call is ringing before canceling the call
	 #'PlayDtmf':'XXXXXXXXXX',		#DTMF Digits to play to the call once it connects. 0-9, #, or *
	 #'HideCallerId':'True/False',		#Specifies if the caller id will be hidden
	 #'Record':'True/False',		#Specifies if the call should be recorded
	 #'RecordCallBack':'example.com',	#Recording parameters will be sent here upon completion
	 #'RecordCallBackMethod':'Get/Post',	#Method used to request the RecordCallback URL
	 #'Transcribe':'True/False',		#Specifies if the call recording should be transcribed
	 #'TranscribeCallBack':'example.com',	#Transcription parameters will be sent here upon completion
}

response = message360Credential.make_call(params)
print response
