import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
		'page':'X',					#Which page of the overall response will be returned. Zero indexed
		'pagesize':'X',					#Number of individual resources listed in the response per page
		'callsid':'XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX',	
		'Datecreated':'XXXX-XX-XX',
}

response = message360Credential.listRecording(params)
print response
