# API key:
# bebb0904ddbd91ae6b4b0bf930955f61-30344472-8e8342fc



def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
		auth=("api", "bebb0904ddbd91ae6b4b0bf930955f61303444728e8342fc"),
		data={"from": "Excited User <mailgun@YOUR_DOMAIN_NAME>",
			"to": ["bar@example.com", "raushanshahi2001@gmail.com"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!"})