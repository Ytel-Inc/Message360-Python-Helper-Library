'''
Description	:	Shows info on all carrier lookups associated with your Message360 account
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
		#'page':'X',
		#'pagesize':'X',
}

response = message360Credential.Carrier_Lookup_List(params)
print response

