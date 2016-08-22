from flask import jsonify, Blueprint
from flask_restful import Resource, Api, request
import re

class PhoneService(Resource):
	"""PhoneService object is there to service RESTful calls for phone utility ops
	"""
	def __init__(self):
		super().__init__()
		
	def get(self):
		"""Return Empty Section
		"""
		return "Empty GET request"
  
	def post(self):
		return self.processPhoneNumbers(request.form['textBox'])

	# refactor candidate to Test outside REST-ful or just figure best Flask Unit Test
	def processPhoneNumbers(self, formData):
		"""This function takes a string <formData> and tries to parse out valid phone 
		numbers inside it, and build a list of formated phone number strings
	
		############ RED ALERT !!! RAN OUT OF TIME, SHOULD USE FLASK TEST CONTEXT 
		############ AND UNIT TESTING. WILL SAVE FOR TOMORROW :-)

		>>> p = PhoneService()
		>>> p.processPhoneNumbers("800-258-3400 This is text \n ok (913) 456-4543 \ 
					   9090009090 Ok, Date: 06/31/2016 06.31.2016"
		NADA
			

		"""
               	## -- find all the phone numbers that match this format 
		list = re.findall(r'1?[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}', formData, re.I)
	
		## -- make them pretty
		for i in range(len(list)):
			list[i] = self.phone_format(list[i])

		return list 

	# refactor candidate. Test outside REST
	def phone_format(self, phone_number):
		"""Take a phone number, and beautify it like: 
				(xxx) xxx-xxxx
	
		"""

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

