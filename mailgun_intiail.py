# API key:
# *****


def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
		auth=("api", "******"),
		data={"from": "Excited User <mailgun@YOUR_DOMAIN_NAME>",
			"to": ["bar@example.com", "*****"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!"})