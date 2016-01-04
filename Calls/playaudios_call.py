import YtelAPI
import YtelConstant

message360Credential = YtelAPI.Message360API(auth_id=YtelConstant.Constant.ACCOUNT_SID,auth_token=YtelConstant.Constant.AUTH_TOKEN)

params = {
          'callsid':'XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX',	#The unique identifier of each call resource
	  'AudioUrl':'exapmle audio file',		#URL to sound that should be played. You also can add more than one audio file using semicolons e.g. http://example.com/audio1.mp3;http://example.com/audio2.wav
	  'Mix':'true',					#If false, all other audio will be muted
	  'Length':'12',				#Time limit in seconds for audio play back
	  'Loop':'true',				#Repeat audio playback indefinitely
	  'Direction':'both',				#The leg of the call audio will be played to
}

response = message360Credential.playaudios_call(params)
print response
