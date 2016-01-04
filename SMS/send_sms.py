import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)


params = {
          'body':'X',
          'to':'XXXXXXXXXX',
          'from':'XXXXXXXXXX',
          #'messagestatuscallback':'X',
          #'method':'POST',#POST,'#GET'
          'fromcountrycode':'X',
          'tocountrycode':'X'
}

response = message360Credential.send_sms(params)

print response

