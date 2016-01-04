'''
Description	:	Here you can experiment with adding voice audio effects on a call through Message360 and view the request response generated when doing so.
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
          'callsid':'XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX',		#The unique identifier of each call resource
	  #'AudioDirection':'XXX',				
	  #'PitchSemiTones':'XX',				#value between -14 and 14
	  #'PitchOctaves':'X',					#value between -1 and 1
	  #'Rate':'XXXXX',					#value greater than 0
	  #'Tempo':'XXXX',					#value greater than 0
}

response = message360Credential.view_call(params)
print response
