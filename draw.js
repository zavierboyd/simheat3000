var canvas = document.getElementById('paint');
var ctx = canvas.getContext('2d');

var sketch = document.getElementById('sketch');
var sketch_style = getComputedStyle(sketch);
canvas.width = parseInt(sketch_style.getPropertyValue('width'));
canvas.height = parseInt(sketch_style.getPropertyValue('height'));

var mouse = {x: 0, y: 0};
var paint = false
/*canvas.addEventListener('mousedown', function(e) {
    mouse.x = e.page - this.offsetLeft;
    mouse.y = e.page - this.offsetTop;
}, false);
*/

ctx.lineWidth = 5;
ctx.lineJoin = 'round';
ctx.lineCap = 'round';
ctx.strokeStyle = 'blue';

canvas.addEventListener('mousemove', function(e) {
    mouse.x = e.page - this.offsetLeft;
    mouse.y = e.page - this.offsetTop;

    paint = true
    ctx.beginPath();
    ctx.moveTo(mouse.x, mouse.y);

    canvas.addEventListener('mousemove', onPaint, false);
}, false);

canvas.addEventListener('mouseup', function() {
    canvas.removeEventListener('mousemove', onPaint, false);
}, false);

var onPaint = function() {
    ctx.lineTo(mouse.x, mouse.y);
    ctx.stroke();
};

function redraw(){
  ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height); // Clears the canvas

  ctx.strokeStyle = "#df4b26";
  ctx.lineJoin = "round";
  ctx.lineWidth = 5;

  for(var i=0; i < clickX.length; i++) {
    ctx.beginPath();
    if(clickDrag[i] && i){
      ctx.moveTo(clickX[i-1], clickY[i-1]);
     }else{
       ctx.moveTo(clickX[i]-1, clickY[i]);
     }
     ctx.lineTo(clickX[i], clickY[i]);
     ctx.closePath();
     ctx.stroke();
  }
}
var clickX = new Array();
var clickY = new Array();
var clickDrag = new Array();

function addClick(x, y, dragging)
{
  clickX.push(x);
  clickY.push(y);
  clickDrag.push(dragging);
}