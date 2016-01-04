'''
	Description 	:	 experiment with sending an sms through Message360 and view the request response generated when doing so.
'''
import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)


params = {
          'body':'X',
          'to':'XXXXXXXXXX',
          'from':'XXXXXXXXXX',
	  'fromcountrycode':'X',
	  'tocountrycode':'X'
          #'messagestatuscallback':'X',
          #'method':'POST',#POST,'#GET'
}

response = message360Credential.send_sms(params)

print response

