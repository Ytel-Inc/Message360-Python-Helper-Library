'''
Description	:	Here you can experiment with modifying a call through Message360 and view the request response doing so generates
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
          'callsid':'XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX',		#The unique identifier of each call resource
	  #'Method':'XXXX',					#The method used to request the above Url parameter
	  #'Status':'XXXXXXX',					#Status to set the in-progress call to
	  #'Url':'https://devweb.ytel.com/ytelapi/gather.php',	#URL the in-progress call will be redirected to
}

response = message360Credential.interrupt_call(params)
print response
