$(document).ready(function(){
    table=document.getElementById("tab")
    var plan=document.getElementById('floorplan').value
    var optionsplan = document.getElementById('options')
    var options = [["room1",
    "room2",
    "room3",
    "room4",
    "room5",
    "room6"],
    ["room7",
    "room8",
    "room9",
    "room10",
    "outside",
    "wall"]]

    var draw="wall"

    var isdown = false

    $(document).mousedown(function(){
        isdown = true
    })
    $(document).mouseup(function(){
        isdown = false
    })

    room = function(elem){
        var elem = elem
        if(true){
            elem.setAttribute("class", draw)
            /*fix to use rowIndex*/
            /*console.log([elem.cellIndex,parseInt(elem.parentNode.id)])*/
           nplan[parseInt(elem.parentNode.id)][elem.cellIndex] = draw
            var elem=document.getElementById("floorplan")
            elem.setAttribute("value",nplan.join(" "))
        }
    }

    brush = function(elem){
        draw = elem.className
    }

    for(i=0;i<options.length;i++){
        row=options[i]
        erow=document.createElement("tr")
        for(b=0;b<options[i].length;b++){
            cell=row[b]
            ecell=document.createElement("td")
            ecell.setAttribute("onclick", "brush(this)")
            ecell.setAttribute("class", cell)
            ecell.innerHTML = cell
            erow.appendChild(ecell)
        }
        optionsplan.appendChild(erow)
    }

/*    width = function(){
        $("#tab tr").each(function(row, tr){
            cell=$("<td></td>")
            cell.attr("class", "wall")
            cell.attr("onclick", "room(this)")
            alert(cell, row)
            $(tr).append(cell)
        })
    }*/

    plan=plan.split(" ")
    planl=plan.length
    console.log(plan)
    nplan=[]
    for(i=0;i<planl;i++){
        row=plan[i].split(",")
        nrow=[]
        var rowe = document.createElement('tr')
        rowe.setAttribute("id", i.toString())
        rowl=row.length
        for(b=0;b<rowl;b++) {
            cell = row[b]
            /*var celle = document.createElement('td')
            celle.setAttribute("class", cell)
            celle.addEventListener("mouseover", function(e,elem){

                if(isdown){
                    elem.setAttribute("class", draw)
                    /*fix to use rowIndex*/
                    /*console.log([elem.cellIndex,parseInt(elem.parentNode.id)])*
                    nplan[parseInt(elem.parentNode.id)][elem.cellIndex] = draw
                    var elem=document.getElementById("floorplan")
                    elem.setAttribute("value",nplan.join(" "))
            }
        })*/
            var celle = document.createElement("td")
            celle.setAttribute("class", cell)
            celle.setAttribute("onclick", "room(this)")
            celle.addEventListener("mouseover", function(e){
                if(isdown){
                    this.setAttribute("class", draw)
                    /*fix to use rowIndex*/
                    /*console.log([elem.cellIndex,parseInt(elem.parentNode.id)])*/
                    nplan[parseInt(this.parentNode.id)][this.cellIndex] = draw
                    var elem=document.getElementById("floorplan")
                    elem.setAttribute("value",nplan.join(" "))
                }
            })
            rowe.appendChild(celle)
            nrow.push(cell)
        }
        table.appendChild(rowe)
        nplan.push(nrow)
    }

//    $("#plan").submit(function{
//        $("floorplan").attr("value",)
//    })
console.log(nplan)

})