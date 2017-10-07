const shortUrl = 'https://en.wikipedia.org/?curid='

function getRandomId()
{
    $.ajax (
        {
            type: "GET",
            url: 'https://en.wikipedia.org/w/api.php?action=query&generator=random&grnnamespace=0&prop=extracts&' +
            'exchars=600&format=json&callback=?',
            contentType: "application/json; charset=utf-8",
            dataType: "json"
        }
    )
        .done(function(data)
        {
            let myArr = Object.values(data.query.pages)[0];
            let cleanExtract = /<p>(.|\n)*?<\/p>/.exec(myArr['extract']);

            if ($('#rich_well').length) {
                $('#rich_well').html('<a href="'+shortUrl+myArr['pageid']+'" target="_blank">'+'<h1>' + myArr['title'] + '</h1>'+ '</a>' + '\n' +  cleanExtract[0]);
            }
            else {
                $('#random_here').append('<div class="well" id="rich_well"></div>');
                $('#rich_well').html('<a href="'+shortUrl+myArr['pageid']+'" target="_blank">'+'<h1>' + myArr['title'] + '</h1>'+ '</a>' + '\n' +  cleanExtract[0]);
            }
        })
}

function retSearchVal() {
    let inputValue= $('#search_input').val();
    return inputValue;
}

function multiArticles() {
    let searchItem = retSearchVal();
    if (searchItem.length > 0) {
            $.ajax (
        {
            type:"GET",
            url: 'https://en.wikipedia.org/w/api.php?action=opensearch&search='+searchItem+'&limit=10&namespace=0&format=json&callback=?',
            contentType: "application/json; charset=utf-8",
            dataType: "json"

        }
    )
                .done(function(multiData)
                    {
                    if(multiData[1].length == 0) {
                        $('#random_here').append('<div class="alert alert-danger"> No results... </div>')
                    }
                    else {
                        $('#rich_well').remove();
                        for (let i=0; i<multiData[1].length; i++) {
                            $('#random_here').append('<div class="well" id="' + 'well_' + i + '"></div>');
                            $("#" + 'well_' + i).html('<a href="'+multiData[3][i]+'" target="_blank">'+'<h1>' + multiData[1][i] + '</h1>'+ '</a>' + '\n' +  multiData[2][i]);
                            // $("#"+'well_' + i).html('Test');
                        }
                    }
                    }
                )
    }
    else {
        alert("Empty searches are not allowed");
    }
}

$(document).ready(function DoOnLoad()
{
    getRandomId();
    $('#random_button').click(function() {
       getRandomId();
    });

    $('#search_button').click(function() {
        multiArticles();
    });

});