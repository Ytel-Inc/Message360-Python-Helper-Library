'''
description	:	Here you can experiment with deleting a recording and view the request response generated when doing so.
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
		'RecordingId':'XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX',
}

response = message360Credential.deleteRecording(params)
print response

