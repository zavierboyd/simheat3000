makehouse = function() {
    table=document.getElementById("tab")
    var plan=document.getElementById('floorplan').value

    draw=true

    clear = function() {

    }

    toggle = function() {
        if(draw) {
            draw = false
        }else{
            draw = true
        }
    }

    room = function(elem){
        if(draw){
            elem.setAttribute("class", "clicked")
            /*fix to use rowIndex*/
            /*console.log([elem.cellIndex,parseInt(elem.parentNode.id)])*/
           nplan[parseInt(elem.parentNode.id)][elem.cellIndex] = 1
            var elem=document.getElementById("floorplan")
            elem.setAttribute("value",nplan.join(" "))
        }else{
            elem.setAttribute("class", "default")
            /*fix to use rowIndex*/
            /*console.log([elem.cellIndex,parseInt(elem.parentNode.id)])*/
            console.log(parseInt(elem.parentNode.id))
            nplan[parseInt(elem.parentNode.id)][elem.cellIndex] = 0

            var elem=document.getElementById("floorplan")
            elem.setAttribute("value",nplan.join(" "))
        }
    }

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
            cell = parseInt(row[b])
            var celle = document.createElement('td')
            if(cell==1){
                celle.setAttribute("class", "clicked")
            }
            celle.setAttribute("onclick", "room(this)")
            console.log(celle)
            rowe.appendChild(celle)
            nrow.push(cell)
        }
        table.appendChild(rowe)
        nplan.push(nrow)
    }
console.log(nplan)

}