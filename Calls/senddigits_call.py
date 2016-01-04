import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
          'callsid':'XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX',		#The unique identifier of each call resource
	  'PlayDtmf':'XXXX',					#DTMF digits to play to the call. 0-9, #, *, W, or w
	  'PlayDtmfDirection':'XXXX',				#The leg of the call DTMF digits should be sent to
}

response = message360Credential.senddigits_call(params)
print response
