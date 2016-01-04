import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
	  'conferencesid':'XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX',
          'Page':'X',
	  'PageSize':'X',
	  'Muted':'XXXXX',
	  'deaf':'XXXXX',
}

response = message360Credential.listparticipant_call(params)
print response
