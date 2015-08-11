house = function() {
table=document.getElementById("tab")

room = function(elem){
    elem.setAttribute("class", "clicked")
    /*fix to use rowIndex*/ console.log([elem.cellIndex,parseInt(elem.parentNode.id)])
    bob[parseInt(elem.parentNode.id)][elem.cellIndex] = 1
}

sendData = function() {
    var elem=document.getElementById("data")
    elem.setAttribute("value",bob.join(" "))
    if(submit_button) {
        var sub=document.getElementById("submit")
        sub.setAttribute("type","submit")
        submit_button=false
    }
}
var submit_button=true
var bob=[]
console.log(bob)
for(i=0;i<50;i++){
    var row=[]
    var element = document.createElement('tr')
    element.setAttribute("id",i.toString()+" ")
    for(b=0;b<50;b++){
        var cell=0
        row.push(cell)
        var element2 = document.createElement('td')
        element2.setAttribute("onclick","room(this)")
         element2.setAttribute("id",b.toString()+","+i.toString())
        element.appendChild(element2)
}
    bob.push(row)
    table.appendChild(element)
}
}