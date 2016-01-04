'''
Description	:	Here you can experiment with updating an incoming Message360 phone number and view the request response generated when doing so.
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
		'PhoneNumber':'XXXXXXXXXX',		#The unique identifier of each incoming phone number resource
		#'FriendlyName':'XXXX',
		#'VoiceUrl':'example.com',		#URL requested once the call connects
		#'VoiceMethod':'XXXX',
		#'VoiceFallbackUrl':'exapmle.com',	#URL requested if the voice URL is not available
		#'VoiceFallbackMethod':'XXXX',		
		#'HangupCallback':'example.com',
		#'HangupCallbackMethod':'XXX',
		#'HeartbeatUrl':'example.com',		#URL requested once the call connects
		#'HeartbeatMethod':'XXX',		#URL that can be requested every 60 seconds during the call to notify of elapsed time
}


response = message360Credential.Update_Number(params)
print response

