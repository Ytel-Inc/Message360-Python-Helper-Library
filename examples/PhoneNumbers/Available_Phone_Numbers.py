'''
Description	:	The request response returned here contains a list of all available phone numbers that can be purchased for use with your Message360 account.
'''
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
