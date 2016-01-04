'''
Description	:	Here you can experiment with adding incoming phone numbers to your Message360 account and view the request response generated when doing so.
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
		'phonenumber':'XXXXXXXXXX',
}


response = message360Credential.Buy_Number(params)
print response

