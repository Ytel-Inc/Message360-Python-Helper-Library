'''
Description	:	The HTTP GET method is used to request this resource. The format of this resources URI is below.
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
          'conferencesid':'XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX',
	  'participantsid':'XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX',
}

response = message360Credential.hangupParticipantAPI_call(params)
print response
