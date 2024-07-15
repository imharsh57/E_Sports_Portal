
import requests
import json

URL = 'http://www.way2sms.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)
response = sendPostRequest(URL, 'CX97133NP0QNNM9MSNSE0QR7A05GS72A', 'MDV7RXBWBZL593EX', 'stage', '9828413830', '1', 'harshit ajin is back' )

