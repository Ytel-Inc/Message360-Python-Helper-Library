'''
Description	:	The request response returned here contains a list of calls associated with your Message360 account
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
		#'Page':'X',			#Which page of the overall response will be returned. Zero indexed
		#'PageSize':'X',		#Number of individual resources listed in the response per page
		#'To':'XXXXXXXXXX',		#Only list calls to this number
		#'From':'XXXXXXXXXX',		#Only list calls from this number
		#'DateCreated':'XXXX-XX-XX'	#Only list calls starting within the specified date range	
}

response = message360Credential.list_call(params)
print response
