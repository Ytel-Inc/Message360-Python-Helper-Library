'''
Description	:	Here you can experiment with initiating or terminating a live call recording through Message360 and view the request response generated when doing so
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
          'callsid':'XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX',		#The unique identifier of each call resource
	  'Record':'XXXX',					#Set true to initiate recording or false to terminate recording
	  #'Direction':'XXX',					#The leg of the call to record
	  #'TimeLimit':'XXXX',					#Time in seconds the recording duration should not exceed
	  #'CallBackUrl':'example.com',				#URL consulted after the recording completes
	  #'Fileformat':'XXX',					#Format of the recording file. Can be .mp3 or .wav
}

response = message360Credential.recordcalls_call(params)
print response
