'''
Description	:	Here you can experiment with transcribing recordings that have occurred through your message360 account and view the request response generated when doing so.
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
		'recordingSid':'XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX',
}


response = message360Credential.listparticipant_call(params)
print response
