import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
          'smssid':'XXXXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'#Message SID
}

response = message360Credential.view_sms(params)

print response
