function submit_ranges() {
    //retrieve input data and pass them to app.py
      const distance = document.getElementById("distance").value;
      const xAxis = document.getElementById("xAxis").value;
      const yAxis = document.getElementById("yAxis").value;
      const created_at = 'None';
      const rangesUrl = `/ranges/${distance}/${xAxis}/${yAxis}/${created_at}`;
  
      //fetch the querry data as json objects
      fetch(rangesUrl).then((res) => res.json()).then((response) =>{
        //separate json object categories
        var col = [];
          for (var i = 0; i < response.length; i++) {
              for (var key in response[i]) {
                  if (col.indexOf(key) === -1) {
                      col.push(key);
                  }
              }
          }
          //create table with header row 
        var table = document.createElement("table");
          var tr = table.insertRow(-1);
          for (var i = 0; i < col.length; i++) {
              var th = document.createElement("th");
              th.innerHTML = col[i];
              tr.appendChild(th);
          }
          //place the json data in the rows
        for (var i = 0; i < response.length; i++) {
  
            tr = table.insertRow(-1);
  
            for (var j = 0; j < col.length; j++) {
                var tabCell = tr.insertCell(-1);
                tabCell.innerHTML = response[i][col[j]];
            }
        }
        //generate the table in place holder
        var divShowData = document.getElementById('showData');
        divShowData.innerHTML = "";
        divShowData.appendChild(table);
      });
    
    }


function led_switch(){
    //get value from switch button
    ledSwitch = document.getElementById("led").value;
    //send value back to aoo.py
    const ledUrl = `/ledswitch/${ledSwitch}`;
    //fetch the change and update the button
    fetch(ledUrl).then((resp) => resp.json()).then((response) =>{
    document.getElementById("led").value = response["switch"];

    });
}