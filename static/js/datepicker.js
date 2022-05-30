$("#id_date").datepicker({
    minDate: 0
});


/* prevent add past date in date field */

$("#reservation-form").one('submit', (function (e) {
    e.preventDefault();
    var $this = $(this);
    var selectedDate = $('#id_date').datepicker('getDate');
    if ((selectedDate < Date.now())) {
        $("#text").html("Please enter future date");
    } else {
        $this.submit();
    }
}));