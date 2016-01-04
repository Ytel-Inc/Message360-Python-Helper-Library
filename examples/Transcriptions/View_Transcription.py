'''
Description	:	The response returned here contains all resource properties associated with the given TranscriptionSid.
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
		'transcriptionsid':'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
}


response = message360Credential.viewTranscription(params)
print response
