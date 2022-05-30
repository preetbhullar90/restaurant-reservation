/* contact form style */


function contactform() {
  let form_field8 = document.getElementById('id_message');

  if (form_field8 !== null) {
    form_field8.placeholder = 'Message..', form_field8.className += 'form-control text-white shadow-none';
    form_field8.style.borderColor = '#625b4b',
      form_field8.style.backgroundColor = '#0c0b09';

  }
}
contactform();