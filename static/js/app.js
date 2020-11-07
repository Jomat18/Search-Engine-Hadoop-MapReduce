
$(document).ready(function() {
    
    $('input[type=image]').click(function() {
        $.ajax({ 
                url: '/search',
                data: JSON.stringify({ "words" : $('#words').val() } ),
                type: 'POST',
                contentType: "application/json; charset=utf-8",
                dataType: "json"
            }).done(function(data) {
                console.log(data)
            }).fail(function() {
                console.log('Failed');
        });        
    });    
});