# Message360-Python-Helper-Library

![](http://message360.com/wordpress/wp-content/uploads/2014/08/message360.png)

### Welcome to the Message360 Python Helper Library
This is home to the Official Python Message360 REST API. 

```Python
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
```

An account for Message360 is free to sign up for at [https://api.message360.com](https://api.message360.com)

### About Message360
Empowering technology to meet modern day communication needs. Through a simple to use API, developers can build, connect, and manage all communications platforms in one system. 

Communicating with prospects, leads and customers is the single most important thing when protecting and growing your business. Now, take it to the next level by imagining the possibilities and how your business can communicate with these people.

More information can be obtained about message360 at [http://www.message360.com](http://message360.com/)

### Support or Contact
Having trouble with Pages or the library?  Visit [https://api.message360.com](https://api.message360.com) and click the Help button in the bottom right corner or [contact support](mailto:support@ytel.com) and we’ll help you sort it out.

### Company Information
© 2015 Ytel, Inc. | Ytel™ All Rights Reserved. | 800.382.4913 | www.ytel.com
