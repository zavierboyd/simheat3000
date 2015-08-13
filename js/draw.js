house = function() {
table=document.getElementById("tab")
var plan=[]

room = function(elem){
    elem.setAttribute("class", "clicked")
    /*fix to use rowIndex*/ console.log([elem.cellIndex,parseInt(elem.parentNode.id)])
    plan[parseInt(elem.parentNode.id)][elem.cellIndex] = 1
    var elem=document.getElementById("data")
    elem.setAttribute("value",plan.join(" "))
}

console.log(plan)
for(i=0;i<5;i++){
    var row=[]
    var element = document.createElement('tr')
    element.setAttribute("id",i.toString()+" ")
    for(b=0;b<5;b++){
        var cell=0
        row.push(cell)
        var element2 = document.createElement('td')
        element2.setAttribute("onclick","room(this)")
         element2.setAttribute("id",b.toString()+","+i.toString())
        element.appendChild(element2)
}
    plan.push(row)
    table.appendChild(element)
}
}