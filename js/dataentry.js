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
    makeTable = function(id,width,height){
        alert(id)
        var elem = $(id)
        for(i=0;i<height;i++){
            var row=$("<tr></tr>")
            for(b=0;b<width;b++){
                row.append("<td></td>").append("<input type='number'>")
            }
        elem.append(row)
        }
    }
    rooms =parseInt(prompt("how many rooms are in your house"))
    makeTable("#area",rooms,rooms)
    makeTable("#temps",1,rooms)
    makeTable("#name",1,rooms)
    makeTable("#capacity",rooms,rooms)
    makeTable("#conductance",rooms,rooms)
});
