$(document).ready(function() {
    $('form').submit(function (e) {
        $('#overlay').show();
        $.ajax({
            type: "POST",
            url: "/sendfiles",
            data: $('form').serialize(), // serializes the form's elements.
            dataType: 'json',
            success: function (data) {
                console.log(data)
                $('#map').text(data[0].mappings).show()
                $('#time').text(data[1].runtime).show()
                $('#overlay').hide();
            }
        });
        e.preventDefault(); // block the traditional submission of the form.
    });
    // Inject our CSRF token into our AJAX request.
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", "{{ form.csrf_token._value() }}")
            }
        }
    })
});