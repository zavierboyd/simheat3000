/*onload = function(){
    var name=document.getElementById("name")
    var mass=document.getElementById("capacity")
    var conductance=document.getElementById("conductance")
    var area=document.getElementById("area")
    var temps=document.getElementById("temps")
    var rooms = parseInt(prompt("how many rooms are in your house"))
    for(i=0;i<rooms;i++){
        var rown = document.createElement("tr")
        var rowm = document.createElement("tr")
        var rowc = document.createElement("tr")
        var rowa = document.createElement("tr")
        var rowt = document.createElement("tr")
        var cellt = document.createElement("td")
        var numt = document.createElement("input")
        numt.setAttribute("type", "text")
        numt.setAttribute("width", "20px")
        cellt.appendChild(numt)
        rowt.appendChild(cellt)
        temps.appendChild(rowt)
        for(b=0;b<rooms;b++){
            var cellm = document.createElement("td")
            var numm = document.createElement("input")
            numm.setAttribute("type", "text")
            cellm.appendChild(numm)
            rowm.appendChild(cellm)
            var cellc = document.createElement("td")
            var numc = document.createElement("input")
            numc.setAttribute("type", "text")
            cellc.appendChild(numc)
            rowc.appendChild(cellc)
            var cella = document.createElement("td")
            var numa = document.createElement("input")
            numa.setAttribute("type", "text")
            cella.appendChild(numa)
            rowa.appendChild(cella)
        }
        mass.appendChild(rowa)
        conductance.appendChild(rowa)
        area.appendChild(rowa)
    }
}*/
$(document).ready(function(){
<<<<<<< HEAD
    setTable = function(id,list,ns){
=======
    makeTable = function(id,width,height,ns){
>>>>>>> origin/master
        var elem = $(id)
        var list = list.split(" ")
        for(i=0;i<list.length;i++){
            var row=$("<tr></tr>")
<<<<<<< HEAD
            var rowl = list[i].split(",")
            for(b=0;b<rowl.length;b++){
                if(ns === "n"){
                    cell=parseInt(rowl[b])
                    input=$("<input type='number'>")
                    input.attr("value", cell)
                    input.attr("min",0)
                    row.append($("<td></td>").append(input))
                }else{
                    cell=rowl[b]
                    row.append($("<td></td>").append($("<input type='text'>").attr("value", cell)))
=======
            for(b=0;b<width;b++){
                if(ns === "n"){
                    row.append("<td><input type='number'></td>")
                }else{
                    row.append("<td><input type='text'></td>")
>>>>>>> origin/master
                }
            }
        elem.append(row)
        }
    }
<<<<<<< HEAD
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
                    tablerow.push($(td).find("input").val())
                })
                table.push(tablerow)
            })
            $("#t"+elems[y]).attr("value",table.join(" "))
            alert($("#tarea"))
            }
=======
    area = $("#pyarea").val()
    rooms =parseInt(prompt("how many rooms are in your house"))
    makeTable("#area",rooms,rooms,"n")
    /*makeTable("#temps",1,rooms,"s")
    makeTable("#name",1,rooms,"s")
    makeTable("#capacity",rooms,rooms,"n")
    makeTable("#conductance",rooms,rooms,"n")*/
    $("#click").click(function(){
        var table = []
        $("#area tr").each(function(row, tr){
            var tablerow=[]
            $(tr).children().each(function(cell, td){
                tablerow.push($(td).find("input").val())
            })
            table.push(tablerow)
        })
        $("#tarea").attr("value",table.join(" "))
    })
    $("#house").submit(function(){
        var table = []
        $("#area tr").each(function(row, tr){
            var tablerow=[]
            $(tr).children().each(function(cell, td){
                tablerow.push($(td).find("input").val())
            })
            table.push(tablerow)
        })
        $("#tarea").attr("value",table.join(" "))
        alert($("#tarea"))
>>>>>>> origin/master
        return true
    })
});
