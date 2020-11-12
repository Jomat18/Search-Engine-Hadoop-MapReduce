
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

                console.log(size)

                if (size) {
                    for(var i=0; i<size ;i++) {
                        
                        var div = $('<div> </div>', {});

                        var p = $('<p>'+data[i][1][1]+' - PageRank: '+data[i][1][0]+' - URL: <a href="/static/corpus/'+data[i][0]+'" target="_blank">'+data[i][0]+'</a></p>',{});

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