import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
          'conferencesid':'XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXXX',	#The unique identifier of each conference resource
	  'participantnumber':'XXXXXXXXXX',			#The unique identifier of each participant resource
	  'muted':'XXXXX',
	  'deaf':'XXXXX',
	  'tocountrycode':'X',
}

response = message360Credential.addParticipant_call(params)
print response
