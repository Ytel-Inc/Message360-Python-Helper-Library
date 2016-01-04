'''
description	:	Here you can experiment with playing audio to conference participants.
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
          'conferencesid':'XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX',
	  'participantsid':'XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX',
	  'audiourl':'audiourl.extension',
}

response = message360Credential.playAudioAPI_call(params)
print response

