$("document").ready(function() {
    var clicks = 0
    $("#sim").on( "click", function(e){
        var str = $("form").serialize();
        console.log(str)
        $("#out").load("/simulate", str, function(){
            console.log($("#save").val())
            if($("#save").val() == 0) {
                var i = $("#comp").text()
                console.log(i)
                $("#save").val(i)
                $("#sim").val("Simulate and Compare")
            }else{
                var ncost = Number($("#comp").text())
                var ocost = Number($("#save").val())
                var ccost = ocost-ncost
                $("#compare").text("You have saved " + ccost + "kWh.")
            };
        });
    });
});