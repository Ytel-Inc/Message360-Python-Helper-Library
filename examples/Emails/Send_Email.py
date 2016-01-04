'''
Description	:	This endpoint allows you to send email
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
		'to':'ex@ex.com',	#You can send email to multiple mail id separated by comma without space e.g. example@example.com,test@test.com
		'subject':'XXXX',	
		'cc':'ex@ex.com',	#You can send email to multiple mail id separated by comma without space e.g. example@example.com,test@test.com
		'bcc':'ex@ex.com',	#You can send email to multiple mail id separated by comma without space e.g. example@example.com,test@test.com
		'type':'XXXX',
		'message':'XXXXX',
		#'attachment':'XXXXX'
	}


response = message360Credential.Send_Email(params)
print response
