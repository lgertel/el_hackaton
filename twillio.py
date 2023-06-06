from twilio.rest import Client

account_sid = "SKf080f73e512f65eea68fed4f6b63f477"
auth_token = "bVdaFrybkTQsP5mi7l1nzVolCjXR5x5O"
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+5511997734996'
                          )

print(message.sid)
