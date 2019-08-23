$(document).ready(function() {
    $('#upload-file-btn').click(function() {
        var form_data = new FormData($('#upload-file')[0]);
        $.ajax({
            type: 'POST',
            url: '/uploadajax',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            dataType: 'json',
            success: function(data) {
                console.log(data)
                $('#map').text(data[0].mappings).show()
                $('#time').text(data[1].runtime).show()
                $('#overlay').hide();
            },
        });
    });
});