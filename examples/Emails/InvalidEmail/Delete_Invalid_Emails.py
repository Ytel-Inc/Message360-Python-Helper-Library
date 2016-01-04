'''
description	:	This endpoint allows you to delete entries in the Invalid Emails list.
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
		'Email':'ex@ex.com',
}
	

response = message360Credential.Delete_Invalid_Emails(params)

print response
