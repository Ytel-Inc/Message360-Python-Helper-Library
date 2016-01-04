import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)


"""
0 All
1  (Outbound Call)
2  (Inbound Call)
3  (Outbound SMS)
4  (Inbound SMS)
5  (Transcription)
6  (Email)
7  (Number Purchased)
8  (Direct Mail Verifiedaddress)
9  (Direct Mail Postcard)
10 (Direct Mail Letters)
11 (Direct Mail Checks)
12 (Direct Mail Prints)
13 (Direct Mail Areamails)
"""
params = {
          #'ProductCode':'X',# code from 0 to 13,
          #'startDate':'YYYY-MM-DD',
          #'endDate':'YYYY-MM-DD'
}

response = message360Credential.list_usage(params);

print response
