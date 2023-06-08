/* global $ */
$(document).ready(function (){
    $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function(data){
	    const trans = data.hello;
	    $('#hello').text(trans);
    });
});
