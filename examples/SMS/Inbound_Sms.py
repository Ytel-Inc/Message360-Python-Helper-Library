'''
	Description	:	The request response returned here contains a list of SMS messages associated with your Message360 account
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
          #'page':'1',
          #'pagesize':'1',
          #'datesent':'X',
          #'to':'9492080471',
          #'from':'9492080471'
}

response = message360Credential.inbound_sms(params)

print response
