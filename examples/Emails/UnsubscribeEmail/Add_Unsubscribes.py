'''
Description	:	Add email addresses to the Unsubscribe list.
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
		 'Email':'ex@ex.com',
}


response = message360Credential.Add_Unsubscribes_Email_Address(params)
print response

