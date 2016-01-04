'''
	Description	:	A call resource provides information about an individual call that has occurred through Message360. Both inbound and outbound voice communication through Message360 are categorized as calls. The resource properties representing a call are listed below. Call resources can be accessed at a resource URI made up of the Message360 base URL and a unique call SID.
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
          'callsid':'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX',#The unique identifier of each call resource
}

response = message360Credential.view_call(params)
print response
