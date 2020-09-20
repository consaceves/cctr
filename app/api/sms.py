from flask import Blueprint, request
from twilio.rest import Client

app = Blueprint("sms", __name__)


@app.route('/sendSMS', methods=['POST'])
def send_SMS():
  # Your Account Sid and Auth Token from twilio.com/console
  # DANGER! This is insecure. See http://twil.io/secure
  account_sid = 'AC76d9b17b2c23170b7019924f709f366b'
  auth_token = '46dc0f63ab4b2c060b7de0902f2c55cd'
  client = Client(account_sid, auth_token)

  message = client.messages \
      .create(
          messaging_service_sid='MG08f11c8d39627fac261716dd1e9daec4',
          body='Help! I\'ve injured myself while training with DebbieAI - please send medical services to this address immediately: ' + request.json.get('address'),
          to=request.json.get('number')
      )
  return {'messageID': message.sid}, 200