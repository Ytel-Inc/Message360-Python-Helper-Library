'''
Description	:	The HTTP POST method is used to request this resource. The format of this resources URI is below.
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
		#'Page':'2',		#Which page of the overall response will be returned. Zero indexed
		#'PageSize':'1',		#Number of individual resources listed in the response per page
		#'FriendlyName':'',	
		#'NumberType':'voice',	
}


response = message360Credential.listnumber(params)
print response

