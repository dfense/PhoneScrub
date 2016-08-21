# PhoneScrub

#####################################################################
Simple single microservice python flask project
Used to demonstrate basic round trip functionality of a simple task to 
receive a block of text from a web client, and process all the possible 
valid phone number formats from the text , and return via json result a 
list of all phone numbers found.
######################################################################

################
Install
################

Dependencies: 
- python
- flask
- flask_restful

Extract the download to any directory
to start the server, type: python app.py 

Navigate to http://<ip>:8000
This will redirect to the form entry page

Insert text into the textbox. If there are valid phone numbers in there, 
hit submit, and should get a valid result in the <div> block below the textbox.
