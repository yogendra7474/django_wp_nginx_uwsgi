$(document).ready(function () {
    $('.update').click(function (element) {
        var currentRow=$(this).closest("tr");
        // var currentRow=$(this).closest("tr");
		// var col4=currentRow.find("td:eq(3)").html();
		// var col5=currentRow.find("td:eq(4)").text();
		// var data=col4+"\n"+col5;
		// alert(data);
        var id = $(this).attr('id');
        var csrf=$("input[name=csrfmiddlewaretoken]").val()
        mydta={'id':id, 'csrfmiddlewaretoken':csrf}
        $.ajax({
            url:"reply",
            method:"POST",
            data:mydta,
//					dataType:'json',
            success: function (data){
                if (data.reply=='ok'){
                    console.log("data submitted");
                    console.log(data.email)
                    var dataemail=data.email;
                    var dataphone=data.phone;
                    currentRow.find("td:eq(3) .email").empty().append(dataemail);
                    // currentRow.find("td:eq(3) .phone").empty().append($('<div class="error"></div>'));
                    currentRow.find("td:eq(3) .phone").empty().append(dataphone);
                    currentRow.find("td:eq(4) .emaildiv").empty().append(' <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">' + 
                    'Add to List</button> <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">' +
                    '<a class="dropdown-item" href="#">Action</a>' +
                    '</div> </div> <div class="tango mongo"> Download </div>')
                    // currentRow.find("td:eq(4)").empty().append('<div class="tangra"> <div class="pango mongo"> Add List </div> <div class="tango mongo"> Download </div> </div>');
                    // $('#' + id).append($('<div class="tangra"> <div class="pango mongo"> new div </div> <div class="pango mongo"> new div </div> </div>'));
                    var $div = $('<div class="error"></div>').html('No more foo allowed').append('<br />');
                    console.log(lag)
                }
            }
//					contentType: 'application/json; charset=utf-8',
        });
    });
});
function showDiv() {
    document.getElementById('second_related').style.display = "block";
    document.getElementById('open').style.display = "none";
  }