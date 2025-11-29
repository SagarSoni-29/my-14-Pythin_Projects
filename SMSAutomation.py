from twilio.rest import Client

account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello , I send this message from Python! ",
    from_="+917073443901",   
    to="+919034233114"     
)
print("Message sent:", message.sid)
