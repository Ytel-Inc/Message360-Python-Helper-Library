import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
		'page':'X',
		'pagesize':'X',
		'status':'XXXXXXX',
		'dateTranscribed':'XXXX-XX-XX',
}

response = message360Credential.listTranscription(params)
print response
