from flask import jsonify, Blueprint
from flask_restful import Resource, Api, request
import re

class PhoneService(Resource):

	def __init__(self):
		super().__init__()
		
	def get(self):
		return message
  
	def post(self):
		return self.processPhoneNumbers(request.form['text-box'])

	# refactor candidate. Test outside REST
	def processPhoneNumbers(self, formData):
                
		## -- this regex works well except for contiguous array of numbers. (maybe long serial#
		## -- I couldn't get perfect before and after expr. w/o 1+ OR clauses...
		list = re.findall(r'1?[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}', formData, re.I)
		
		## -- make them pretty
		for i in range(len(list)):
			list[i] = self.phone_format(list[i])

		return list 

	# refactor candidate. Test outside REST
	def phone_format(self, phone_number):
		print (phone_number)
		# remove all the non-digits for clean number
		clean_phone_number = re.sub('[^0-9]+', '', phone_number)
		# add in the parens and hyphen

		return '(' + clean_phone_number[:3] + ') ' + clean_phone_number[3:6] + '-' + clean_phone_number[6:]
  

# cool new routing method i had to try...
phone_api = Blueprint('resources.phoneProcessor', __name__)

api = Api(phone_api)

api.add_resource(
  PhoneService, 
  '/api/v1/phoneService', 
  endpoint = 'phone'
)
