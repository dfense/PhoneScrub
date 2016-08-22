// form.js
$(document).ready(function() {
    // allocate once
    var warnMessage = "";
    var _MINLENGTH = 10;
    var _MAXLENGTH = 1024;

    // process the form
    $('form').submit(function(event) {
    	warnMessage="";

        // get the form data
        var formData = {
            'textBox'             : $('textarea[name=text-box]').val(),
        };


	//------------- check minimum and maximum lengths -----------
	if( formData.textBox.length  > _MAXLENGTH){
		warnMessage = "WARNING: The maximum length of " +  _MAXLENGTH +
		" characters has been exceeded. Please fix and try again.";
		
	} 
	else if( formData.textBox.length < _MINLENGTH){
		warnMessage = "WARNING: The minimum length to be submitted is" +
		 _MINLENGTH + " characters. Please fix and try again."
	}
	if(warnMessage.length){
	
		var options = {
    			"backdrop" : "static",
			"keyboard" : "true"
		};

		$('#basicModal').modal(options);
		$("#count").text(warnMessage);
		$("#tInfo").text("The current character length is: " + 
					formData.textBox.length);

		event.preventDefault();
		return false;
	}
	


        //------------- process the form ------------------
        $.ajax({
            type        : 'POST', 
            //url         : "http://requestb.in/1l61cx41"  //debug site
            url         : '/api/v1/phoneService', // the url where we want to POST
            data        : formData, // our data object
            dataType    : 'json', // what type of data do we expect back from the server
            encode      : true,
        })
            // using the done promise callback
            .done(function(data) {
		// clear out the <div> for last query. --could append also...
		$("#result-phone-numbers").empty()
		$.each(data, function(index, value)
		{
			$("#result-phone-numbers").append("<H4>" + value + "</H4>")
                	console.log(value); 
		});
		console.log(data)

                // here we will handle errors and validation messages
            });

        // stop the form from submitting the normal way and refreshing the page
        event.preventDefault();
    });

});
