$(document).ready(function(){
    setTable = function(id,list,ns){
        var elem = $(id)
        var list = list.split(" ")
        for(i=0;i<list.length;i++){
            var row=$("<tr></tr>")
            var rowl = list[i].split(",")
            for(b=0;b<rowl.length;b++){
                if(ns === "n"){
                    cell=parseFloat(rowl[b])
                    input=$("<input type='number'>")
                    input.attr("value", cell)
                    input.attr("min",0)
                    input.attr("step","any")
                    input.attr("required")
                    row.append($("<td></td>").append(input))
                }else{
                    cell=rowl[b]
                    row.append($("<td></td>").append($("<input type='text'>").attr("value", cell)))
                }
            }
        elem.append(row)
        }
    }
    var area = $("#pyarea").val()
    var temps = $("#pytemps").val()
    var names = $("#pynames").val()
    var capacity = $("#pycapacity").val()
    var conductance = $("#pyconductance").val()
    setTable("#area",area,"n")
    setTable("#temps",temps,"n")
    setTable("#names",names,"s")
    setTable("#capacity",capacity,"n")
    setTable("#conductance",conductance,"n")

    $("#house").submit(function(){
        elems=["area","temps","names","capacity","conductance"]
        for(y=0;y<elems.length;y++){
            var table = []
            $("#"+elems[y]+" tr").each(function(row, tr){
                var tablerow=[]
                $(tr).children().each(function(cell, td){
                    cell=$(td).find("input").val()
                    if(!(cell)){
                        tablerow.push(0)
                    }else{
                        tablerow.push(cell)
                    }
                })
                table.push(tablerow)
            })
            $("#t"+elems[y]).attr("value",table.join(" "))
        }
        return true
    })
});
