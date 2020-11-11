
$(document).ready(function() {
    
    $('input[type=image]').click(function() {

        $('#pages div').empty();

        $.ajax({ 
                url: '/search',
                data: JSON.stringify({ "words" : $('#words').val() } ),
                type: 'POST',
                contentType: "application/json; charset=utf-8",
                dataType: "json"
            }).done(function(data) {
                console.log("paginas :",data)

                var size = data.length

                //console.log(size)
                
                if (size) {
                    for(var i=0; i<size ;i++) {
                        
                        var div = $('<div> </div>', {});

                        var p = $('<p>'+data[i]+' URL: <a href="/static/corpus/'+data[i]+'" target="_blank">'+data[i]+'</a></p>',{});

                        div.append(p)

                        div.appendTo($('#pages'));     
                        
                    }
                }
                else {
                    var div = $('<div> </div>', {});
            
                    var p = $('<p> No se encontraron resultados!</p>',{});

                    div.append(p)

                    div.appendTo($('#pages'));     
                }

            }).fail(function() {
                console.log('Failed');
        });        
    });    
});