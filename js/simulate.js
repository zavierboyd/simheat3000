$("document").ready(function() {
    $("#sim").on( "click", function(e){
        var pair = ["IRwall=", "IHwall=", "IRwindow=", "IHwindow=", "IRroof=", "IHroof=", "IRfloor=", "IHfloor="]
        var str = $("form").serialize() + "&";
/*        check = str.split("&");
        var idx = []
        for(i in check) {
            if(check[i] == pair[i]) {
                idx.push(i);
            }
        };
        var string = "please check these:"
        for(i in check) {
            switch(check[i]):
        }

        if(string == "please check these:") {
            $("#out").text( str );
        }else{

*/     $("#out").load("/winanalysis")
    });
});