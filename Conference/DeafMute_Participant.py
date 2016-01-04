'''
Description	:	Here you can experiment with the deaf or mute conference participant API methods
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
          'conferencesid':'XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX',
	  'participantsid':'XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX',
	  #'muted':'XXXX',
	  #'deaf':'XXXX',
}

response = message360Credential.DeafMuteParticipantAPI_call(params)
print response
