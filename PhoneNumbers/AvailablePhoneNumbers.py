import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
		'areacode':'XXXX',			#Area Code
		'region':'XXX',
		'numbertype':'XXXX',
}

response = message360Credential.availablenumber(params)
print response
