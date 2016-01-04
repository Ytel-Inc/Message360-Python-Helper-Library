'''
	Description	:	Get the  response of contains a list of SMS messages associated with your Message360 account
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
          #'page':'X',
          #'pagesize':'X',
          #'datesent':'XXXX-XX-XX',
          #'to':'XXXXXXXXXX',
          #'from':'XXXXXXXXXX'
}

response = message360Credential.list_sms(params)

print response
