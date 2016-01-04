import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
	'IncomingPhoneNumberSid':'XXXXXXXXXX',
}

response = message360Credential.Release_Number(params)
print response

