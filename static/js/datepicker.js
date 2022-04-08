


/* Add date field in calender */

    $("#id_date").datepicker({
        dateFormat: 'dd/mm/yy'
    });


//$('#id_date').datepicker({ minDate: 0 });


/* prevent add past date in date field */
$("#reservation-form").one('submit', (function (e) {
    e.preventDefault();
    var $this = $(this);
    var selectedDate = $('#id_date').datepicker('getDate');
    if ((selectedDate.getTime() < Date.now())) {
        $("#text").html("Please enter vaild date");
    } else {
        $this.submit();
    }
}));
