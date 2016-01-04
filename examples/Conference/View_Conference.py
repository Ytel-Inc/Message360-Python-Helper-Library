'''
Description	:	The request response returned here contains all resource properties associated with the conference name.
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
          'conferencesid':'XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX',	#The unique identifier of each conference resource
}

response = message360Credential.viewconference_call(params)
print response
