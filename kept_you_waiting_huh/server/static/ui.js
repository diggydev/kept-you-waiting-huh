var secretId = ""

function sendCommand(command) {
  $.post("/",{"command": command, "secretId": secretId},
  function (data, status){
    secretId = data["secretId"];
    screenData = data["screen"];
    var c=document.getElementById("screen");
    var ctx=c.getContext("2d");
    var map = document.getElementById("map");
    for (y = 0; y < screenData.length; y++) {
      for (x = 0; x < screenData[y].length; x++) {
        ctx.drawImage(map, screenData[y][x][0]*8, screenData[y][x][1]*8, 8, 8, x*8, y*8, 8, 8);
      }
    }
    console.log(data);
    $('#map').hide();
  }
);
}

$(document).ready(function(){
  console.log('b');
  //$('#map').hide();
  sendCommand('myCommand');
});
