'''
Description	:	 can experiment with Optin numbers before sending sms from toll-free number through Message360 and view the request response generated when doing so.
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
          'from':'XXXXXXXXXX',
          'to':'XXXXXXXXXX',
          'expires':'X',#0 or 1
          'authorizedby':'X',
          'authorizedhow':'X',
          'ToCountryCode':'X',
          'FromCountryCode':'X',
}

response = message360Credential.optins_sms(params)
print response
