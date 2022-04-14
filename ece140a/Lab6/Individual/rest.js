
var form = document.getElementById('send');
var data = $('#sensor-data').data();

var clicked = false;

function SwitchToggle() {
  document.addEventListener('DOMContentLoaded', function () {
    var checkbox = document.querySelector('input[type="checkbox"]');

    checkbox.addEventListener('change', function () {
      if (checkbox.checked) {
        console.log('Checked');
      } else {
        console.log('Not checked');
      }
    });
  });

function addTable() {
  let appendToTable = function(Timestamp, Distance, xAngle, yAngle) {
    let table = document.querySelector('.dataTable');
    let newRow = document.createElement('tr');
    newRow.innerHTML = `
      <th>${Timestamp}</th>
      <th>${Distance}</th>
      <th>${xAngle}</th>
      <th>${yAngle}</th>
    `;
    
    table.appendChild(newRow)
    return newRow
  }

  for (let item of data.items) {
    appendToTable(item.Timestamp, item.Distance, item.xAngle, item.yAngle)
  }
}