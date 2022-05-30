/* update booking form style */



function updatefunction() {
  let update_reservation1 = document.getElementById('id_persons');
  if (update_reservation1 !== null) {
    update_reservation1.placeholder = 'Persons..', update_reservation1.className += 'form-control text-white shadow-none';
    update_reservation1.style.borderColor = '#625b4b',
      update_reservation1.style.backgroundColor = '#0c0b09';
  }
}
updatefunction();


function update2function() {
  let update_reservation2 = document.getElementById('id_time');
  if (update_reservation2 !== null) {
    update_reservation2.placeholder = 'Time..', update_reservation2.className += 'form-control text-white shadow-none';
    update_reservation2.style.borderColor = '#625b4b',
      update_reservation2.style.backgroundColor = '#0c0b09';
  }
}
update2function();



function update3function() {
  let update_reservation3 = document.getElementById('id_date');
  if (update_reservation3 !== null) {
    update_reservation3.placeholder = '06/29/2022', update_reservation3.className += 'form-control text-white shadow-none';
    update_reservation3.style.borderColor = '#625b4b',
      update_reservation3.style.backgroundColor = '#0c0b09';
  }
}
update3function();