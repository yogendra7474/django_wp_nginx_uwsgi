// $(document).ready(function(){
//     $("#submitid").click(function(event){
//         event.preventDefault();
//         $.ajax({
//             type: "POST",
//             url:'pagination_p', // name of url
//             data : {    
//             name : $('#inputid').val(),
//             csrfmiddlewaretoken: '{{ csrf_token }}',
//         },
//         success: function () {
//         },
//         error: function () {}
//         });
//     });
//  });   

$(document).ready(function(){
    $("a").click(function(event){
        event.preventDefault();
        var page_n = $(this).attr('href');
        console.log(page_n)
        $.ajax({
            type: "POST",
            url:'/pagination_p', // name of url
            data : {    
            page_n : page_n, //page_number
            csrfmiddlewaretoken: '{{ csrf_token }}',
        },
        success: function (resp) {
            $('#posts').html('')
            $.each(resp.results, function(i, val) {
                $('#posts').append('<h2>' + val.title + '</h2>')
            });
        },
        error: function () {}
        });
    });
 });   