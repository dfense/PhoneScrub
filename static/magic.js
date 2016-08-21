// magic.js
$(document).ready(function() {

    // process the form
    $('form').submit(function(event) {

        // get the form data
        var formData = {
            'text-box'             : $('textarea[name=text-box]').val(),
        };


        // process the form
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
