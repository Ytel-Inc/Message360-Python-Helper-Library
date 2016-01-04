'''
Description	:	The request response returned here contains a conference participant resource.
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
	  'conferencesid':'XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX',
	  'participantsid':'XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX',
}

response = message360Credential.viewparticipant_call(params)
print response
