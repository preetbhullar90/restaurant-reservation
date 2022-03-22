/* Add date field in calender */

$('#id_date').datepicker({ minDate: 0 });


/* prevent add past date in date field */
$("#reservation-form").one('submit', (function (e) {
    e.preventDefault();
    var $this = $(this);
    var selectedDate = $('#id_date').datepicker('getDate');
    if ((selectedDate.getTime() < Date.now())) {
        alert("Please select the valid date");
    } if ((selectedDate.getTime() > Date.now())) {
        $this.submit();
    }
}));
