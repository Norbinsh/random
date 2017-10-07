$(document).ready(function () {
    function ajaxIp() {
        $.ajax({
            cache: false,
            url : "http://ip.jsontest.com",
            dataType:"jsonp",
            success:function(data) {
                document.getElementById('h1_author').textContent = data['ip'];
            }
});
    }
    ajaxIp();
    $("#quote_button").click(function() {
        ajaxIp();
    });
});


$(document).ready(function () {
    function ajaxDate() {
        $.ajax({
            cache: false,
            url : "http://date.jsontest.com",
            dataType:"jsonp",
            success:function(data) {
                document.getElementById('main_quote').textContent = data['time'] + ' ' + data['milliseconds_since_epoch'] + ' ' + data['date'];
            }
});
    }
    ajaxDate();
    $("#quote_button").click(function() {
        ajaxDate();
    });
});



$(document).ready(function () {
    $('#twitter_button').click(function (e) {
        var textToTweet = $('#main_quote').text();
        var twtLink = 'http://twitter.com/home?status=' +encodeURIComponent(textToTweet);
        window.open(twtLink,'_blank');

    })
});





