$(document).ready(function(){
    console.log('this is run on page load');
    var id = []; 
    $(".CBoxAll").each(function() { 
        id.push($(this).val()); 
    });
    var csrf=$("input[name=csrfmiddlewaretoken]").val()
    mydta={'id':id, 'csrfmiddlewaretoken':csrf}
    $.ajax({
        url:"WindowsLoadData",
        method:"POST",
        data:mydta,
                                        //					dataType:'json',
        success: function (data){
            if (data.reply=='ok'){
                console.log("data submitted");
                var id =data.res;
                var i;
                for (i in id){
                    console.log(i)
                    var value=id[i];
                    // console.log(value)
                    const email = Object.keys(value)
                    const phone = Object.values(value)
                    $("tr.TableValue").each(function() {
                        var quantity1 = $(this).find(":input").val();
                        console.log(quantity1)
                        if (quantity1==i) {
                            console.log("lex")
                            $(this).find(".email").empty().append(email);
                            $(this).find(".phone").empty().append(phone);
                            $(this).find("td:eq(6)").empty().append('<div class="container1" data-toggle="modal" data-target="#exampleModalCenter">Add to list</div>'+
                            '<div class="viewDownload">Download</div>')
                        }
                    });
                }
                
            }
        },
        async:false
    });

});
