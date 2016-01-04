'''
Description	:	Here you can experiment with transcribing audio located at a URL and view the request response generated when doing so.
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
		'audiourl':'audiourl.extestion',				
}

response = message360Credential.Transcribe_Audio_URL(params)
print response

