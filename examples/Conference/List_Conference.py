'''
Description	:	The request response returned here contains a list of all conferences associated with an account.
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
          'Page':'X',
          'PageSize':'X',
	  'FriendlyName':'X',
	  'Status':'xxxxxxx',
	  'DateCreated':'xxxx-xx-xx',
	  'DateUpdated':'xxxx-xx-xx',
}

response = message360Credential.listconference_call(params)
print response
