from boltiot import  Bolt
import json, time
api_key="Your Bolt cloud API Key"
device_id="Your Bolt Device ID"
minimum_limit = 15
mybolt=Bolt(api_key,device_id)
print(format("Auto LED Controller",'_^50'))
error='{"success": "0", "message": "A Connection error occurred"}'
offlne='{"value": "offline", "time": null, "success": 1}'
result=mybolt.isOnline()
if result==error:
	print("\n Check weather your computer or bolt device is connected to Internet.....")
elif result==offlne:
	print("\n Bolt Device is offline....")
else:
	while True:
		print ("\n Recognizing Value from Senser.......")
		response = mybolt.analogRead('A0')
		data = json.loads(response)
		inten=int(data['value'])
		print("value from senser is: " + str(inten))
		if inten<minimum_limit:
			result=mybolt.digitalWrite('0','HIGH')
			print("LED is Sucessfully Turned ON")
		else:
			result=mybolt.digitalWrite('0','LOW')
			print("LED is Sucessfully Turned OFF")
		time.sleep(10)
  
  
  
  import json 
from time import sleep
from boltiot import Bolt
api = "api-key of boltiot"
device = "device name of boltiot"
mybolt = Bolt(api,device)
while True:
	try:
		analog_response = mybolt.analogRead('A0')
		analog_data = json.loads(analog_response)
		print("LDR value >> " + analog_data['value'])
		if int(analog_data['value']) <=200:
			digital_response=mybolt.digitalRead('0')
			digital_data=json.loads(digital_response)
			print(digital_data)
			sen_value = int(digital_data['value'])
			if sen_value==1:
				print("Motion Detected")
				mybolt.digitalWrite('1','HIGH')
				mybolt.digitalWrite('2','HIGH')
				sleep(10)
			else:
				print("Sensor's ready")
				mybolt.digitalWrite('1','LOW')
				mybolt.digitalWrite('2','LOW')
		else:
			print("Sensor's ready")
			mybolt.digitalWrite('1','LOW')
			mybolt.digitalWrite('2','LOW')
	except KeyboardInterrupt:
		exit()