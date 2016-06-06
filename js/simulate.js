$("document").ready(function() {
    $("#sim").on( "click", function(e){
        var str = $("form").serialize();
        console.log(str)
        $("#out").load("/simulate", str);
    });
});