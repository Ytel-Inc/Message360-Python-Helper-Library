'''
Description	:	This endpoint allows you to retrieve entries in the Blocks list.
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
		#'Offset':'X',
		#'Limit':'X',

}
	
response = message360Credential.List_Blocks_Email(params)
print response
          
