

$(document).ready(function(){
  $(".floating-input").focus(function(){
    $(".fa-plus").hide();
  })
  $(".floating-input").blur(function(){
    $(".fa-plus").show();
  })
});


$(document).ready(function(){
  $('#TitleAllCheck').change(function(e) {
      if (e.currentTarget.checked) {
        $('.TitleCheck').find('input[type="checkbox"]').prop('checked', true);
      } else {
        $('.TitleCheck').find('input[type="checkbox"]').prop('checked', false);
      }
    });
});


$(document).ready(function(){
  $('#FunctionAllCheck').change(function(e) {
      if (e.currentTarget.checked) {
        $('.FunctionCheck').find('input[type="checkbox"]').prop('checked', true);
      } else {
        $('.FunctionCheck').find('input[type="checkbox"]').prop('checked', false);
      }
    });
});


$(document).ready(function(){
  $('#SeniorityAllCheck').change(function(e) {
      if (e.currentTarget.checked) {
        $('.SeniorityCheck').find('input[type="checkbox"]').prop('checked', true);
      } else {
        $('.SeniorityCheck').find('input[type="checkbox"]').prop('checked', false);
      }
    });
});

$(document).ready(function(){
  $('#CompanysizeAllCheck').change(function(e) {
      if (e.currentTarget.checked) {
        $('.CompanysizeCheck').find('input[type="checkbox"]').prop('checked', true);
      } else {
        $('.CompanysizeCheck').find('input[type="checkbox"]').prop('checked', false);
      }
    });
});



$(document).ready(function(){
  $('#checkbox-all-ser').change(function(e) {
      if (e.currentTarget.checked) {
        $('.CBox').find('input[type="checkbox"]').prop('checked', true);
      } else {
        $('.CBox').find('input[type="checkbox"]').prop('checked', false);
      }
    });
}); 


$(document).ready(function(){
  var limit=100
  $('#checkbox-all-ser100').change(function(e) {
      if (e.currentTarget.checked) {
        $('.CBox').find('input[type="checkbox"]').prop('checked', true).length >= limit;
      } else {
        $('.CBox').find('input[type="checkbox"]').prop('checked', false);
      }
    });
}); 

$(document).ready(function(){
  var limit=1000
  $('#checkbox-all-ser1000').change(function(e) {
      if (e.currentTarget.checked) {
        $('.CBox').find('input[type="checkbox"]').prop('checked', true).length >= limit;
      } else {
        $('.CBox').find('input[type="checkbox"]').prop('checked', false);
      }
    });
});

$(document).ready(function(){

  $('#checkbox-all-serall').change(function(e) {
      if (e.currentTarget.checked) {
        $('.SearchArea').find('input[type="checkbox"]').prop('checked', true);
      } else {
        $('.SearchArea').find('input[type="checkbox"]').prop('checked', false);
      }
    });
});




$(document).ready(function(){
  $('#DashDropdown').on('click',function(e){
    e.preventDefault();
    $('#paf').toggle(300);
    e.stopPropagation();
  });
  $('#paf').on('click',function(e){
    e.stopPropagation();
  });
  $('html').click(function(){
    $("#paf").hide();
  });
});


$(document).ready(function(){
  $('.SaveContact').on('click',function(e){
    e.preventDefault();
    $('.SaveContactMenu').toggle();
    e.stopPropagation();
  });
  $('.SaveContactMenu').on('click',function(e){
    e.stopPropagation();
    if ($(e.target).is('[data-toggle=modal]')) {
      $($(e.target).data('target')).modal()
    }
  });
  $('html').click(function(){
    $(".SaveContactMenu").hide();
  });
});


$(document).ready(function(){
  $('.ShowColumn').on('click',function(e){
    e.preventDefault();
    $('.ShowColumnMenu').toggle(300);
    e.stopPropagation();
  });
  $('.ShowColumnMenu').on('click',function(e){
    e.stopPropagation();
  });
  $('body').click(function(){
    $(".ShowColumnMenu").hide();
  });
});



$(document).ready(function(){
  $('.ShowRows').on('click',function(e){
    e.preventDefault();
    $('.ShowRowsMenu').toggle();
    e.stopPropagation();
  });
  $('.ShowRowsMenu').on('click',function(e){
    e.stopPropagation();
  });
  $('body').click(function(){
    $(".ShowRowsMenu").hide();
  });
});

//                                  view of contact


// $(document).ready(function(){
//    $("body").delegate(".container1", "click", function(e){
//     e.preventDefault();
//     var parentTag = $( this ).parent();
//     $(parentTag).find('.container2').toggle();
//     if($(parentTag).find('.container2').is(":hidden")){
//       $(parentTag).find('.viewDownload').show();
//     } else{
//       $(parentTag).find('.viewDownload').hide();
//     }
//     e.stopPropagation();
//   });
//   $('html').click(function(){
//     $(".container2").hide();
//     $(".viewDownload").show();
//   });
// });


$(document).ready(function(){
  $('.parag').change(function() {
    selected=($(this).val());
    $.ajax({
      type: "get",
      url: "Client_top",
      data: {selected: selected},
      success: function(data) {
        if (data.reply=='ok'){
          appendToSearchTableRes(data.filters);
        }
      },
      error: function(data) {}
    }); 
  });
});

// function appendToSearchTableRes(filters) {
//   $("#SearchTableRes > tbody:last-child").append(`
//     <tr class="TableValue">
//       <td class="CBox"><input type="checkbox" name="checks[]"  id="clinet[]" value="${user.id}"></td>
//       <td class="TableName">
//         <div>${ user.First_Name} ${ user.Last_Name}</div>
//         <div>${ user.Primary_Department}</div>
//       </td>
//       <td class="TableCompany">${ user.Company}</td>
//       <td class="TableEmail">
//         <div><i class="far fa-envelope"></i><span>${ user.Email}</span></div>
//         <div><i class="fas fa-phone-alt"></i><span>${ user.Company_Number}</span></div>
//       </td>
//       <td class="TableAdd">
//         <div>${ user.State}</div>
//         <div>${ user.Country }</div>
//       </td>
//       <td class="TableConfidence"> ${ user.Email_Confidence}</td>
//       <td class="TableView">
//         <div> View Contact</div>
//       </td>
//     </tr>
//   `);
// }

// ------------------------------------------Column hide start

$(document).ready(function(){
  // Checkbox click
  $(".hidecol").click(function(){
      var id = this.id;
      var splitid = id.split("_");
      var colno = splitid[1];
      var checked = true;
      // Checking Checkbox state
      if($(this).is(":checked")){
          checked = true;
      }else{
          checked = false;
      }
      setTimeout(function(){
          if(checked){
              $('#SearchTableRes td:nth-child('+colno+')').hide();
              $('#SearchTableRes th:nth-child('+colno+')').hide();
          } else{
              $('#SearchTableRes td:nth-child('+colno+')').show();
              $('#SearchTableRes th:nth-child('+colno+')').show();
          }
      }, 200);
  });
});



// ------------------------------------------Column hide end 


// ------------------------------------------start 

function sortTable(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("SearchTableRes");
  switching = true;
  //Set the sorting direction to ascending:
  dir = "asc"; 
  /*Make a loop that will continue until
  no switching has been done:*/
  while (switching) {
    //start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /*Loop through all table rows (except the
    first, which contains table headers):*/
    for (i = 1; i < (rows.length - 1); i++) {
      //start by saying there should be no switching:
      shouldSwitch = false;
      /*Get the two elements you want to compare,
      one from current row and one from the next:*/
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      /*check if the two rows should switch place,
      based on the direction, asc or desc:*/
      if (dir == "asc") {
        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
          //if so, mark as a switch and break the loop:
          shouldSwitch= true;
          break;
        }
      } else if (dir == "desc") {
        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
          //if so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      /*If a switch has been marked, make the switch
      and mark that a switch has been done:*/
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      //Each time a switch is done, increase this count by 1:
      switchcount ++;      
    } else {
      /*If no switching has been done AND the direction is "asc",
      set the direction to "desc" and run the while loop again.*/
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}
// ------------------------------------------end 




$(document).ready(function () {
  $('.update').click(function (element) {
      var currentRow=$(this).closest("tr");
      // var currentRow=$(this).closest("tr");
  // var col4=currentRow.find("td:eq(3)").html();
  // var col5=currentRow.find("td:eq(4)").text();
  // var data=col4+"\n"+col5;
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
                  var dataemail=data.email;
                  var dataphone=data.phone;

                  var MyObject=data.filter2;
                  console.log(MyObject)
                  var output="";
                  var ValObj=Object.values(MyObject);
                  var ValKey=Object.keys(MyObject);
                  var i;
                  for (i = 0; i < ValObj.length; i++) {
                    output+='<button class="dropdown-item search-drop-updated" name="SaveValues[]" value="'+ValKey[i]+'">'+ValObj[i] +"</button>"
                  }
                  currentRow.find("td:eq(3) .email").empty().append(dataemail);
                  // currentRow.find("td:eq(3) .phone").empty().append($('<div class="error"></div>'));
                  currentRow.find("td:eq(3) .phone").empty().append(dataphone);
                  currentRow.find("td:eq(6)").empty().append('<div class="container1" data-toggle="modal" data-target="#exampleModalCenter">Add to list</div>'+
                  '<div class="viewDownload">Download</div>')
                  // currentRow.find("td:eq(4)").empty().append('<div class="tangra"> <div class="pango mongo"> Add List </div> <div class="tango mongo"> Download </div> </div>');
                  // $('#' + id).append($('<div class="tangra"> <div class="pango mongo"> new div </div> <div class="pango mongo"> new div </div> </div>'));
                  
              }
          }
//					contentType: 'application/json; charset=utf-8',
      });
  });
});


$(document).ready(function () {
  $('.saveSearchData, .ViewModalSubmit').click(function () {
    let name=$(".nameInput").val();
    var csrf=$("input[name=csrfmiddlewaretoken]").val();
    var ChecBox=[];
      $("input:checked").each(function() { 
        ChecBox.push($(this).val()); 
      }); 
      if (name==""){
        alert("Please enter name");
      } else if (ChecBox==""){
        alert("Please select field");
      } else{
        pinaka={name:name,ChecBox:ChecBox,csrfmiddlewaretoken:csrf};
        $.ajax({
          url:"Save",
          method:"POST",
          data:pinaka,
          dataType:'json',
          success: function (data){
            $( ".UserSaved" ).empty();
            var MyObject=data.filter2;
            var output="";
            var ValObj=Object.values(MyObject);
            var ValKey=Object.keys(MyObject);
            var i;
            for (i = 0; i < ValObj.length; i++) {
              output+='<button class="dropdown-item search-drop-updated" name="SaveValues[]" value="'+ValKey[i]+'">'+ValObj[i] +"</button>"
            }
            $( ".UserSaved" ).html(output);
            $('.modal').modal('hide');
          }
        });
      }
  });
});





$(document).ready(function(){
  $('.addToList').on('click',function(e){
    e.preventDefault();
    $('.subAddToList').toggle();
    e.stopPropagation();
  });
  $('.subAddToList').on('click',function(e){
    e.stopPropagation();
    if ($(e.target).is('[data-toggle=modal]')) {
      $($(e.target).data('target')).modal()
    }
  });
  $('html').click(function(){
    $(".subAddToList").hide();
  });
});



$(document).ready(function(){
  $('.subAddToListMenu').click(function() {
    saveId=$(this).attr("data-id");
    var SaveChecBox=[];
    $("input:checked").each(function() { 
      SaveChecBox.push($(this).val());
    });
    var csrf=$("input[name=csrfmiddlewaretoken]").val();
    saveData={saveId:saveId,SaveChecBox:SaveChecBox,csrfmiddlewaretoken:csrf};
    $.ajax({
      type: "post",
      url: "SaveUpdate",
      data: saveData,
      success: function(data) {
        if (data.reply=='ok'){
          console.log("data has been submitted")
        }
      },
      error: function(data) {
        console.log("not")
      }
    }); 
  });
});



$(document).ready(function () {
  $('.nata').click(function () {
    let name=$(".ViewModalInput").val();
    var csrf=$("input[name=csrfmiddlewaretoken]").val();
    var ChecBox=[];
      $("input:checked").each(function() { 
        ChecBox.push($(this).val()); 
      }); 
      if (name==""){
        alert("Please enter name");
      } else if (ChecBox==""){
        alert("Please select field");
      } else{
        pinaka={name:name,ChecBox:ChecBox,csrfmiddlewaretoken:csrf};
        $.ajax({
          url:"Save",
          method:"POST",
          data:pinaka,
          dataType:'json',
          success: function (data){
            $( ".UserSaved" ).empty();
            var MyObject=data.filter2;
            var output="";
            var ValObj=Object.values(MyObject);
            var ValKey=Object.keys(MyObject);
            var i;
            for (i = 0; i < ValObj.length; i++) {
              output+='<button class="dropdown-item search-drop-updated" name="SaveValues[]" value="'+ValKey[i]+'">'+ValObj[i] +"</button>"
            }
            $( ".UserSaved" ).html(output);
            $('.modal').modal('hide');
          }
        });
      }
  });
});


// $(document).ready(function () {
//   $('#DownloadList').click(function () {
//     var csrf=$("input[name=csrfmiddlewaretoken]").val();
//     var ChecBox=[];
//       $("input:checked").each(function() { 
//         ChecBox.push($(this).val()); 
//       });
//       alert(ChecBox) 
//       if (ChecBox==""){
//         alert("Please select items");
//       } else{
//         pinaka={ChecBox:ChecBox,csrfmiddlewaretoken:csrf};
//         $.ajax({
//           url:"Clinet_save",
//           method:"POST",
//           data:pinaka,
//           // dataType:'json',
//           success: function (data){
//             alert("message sent")
//             if (data.reply=='ok') {
//               alert(data.error_message);
//             }
//           }
//         });
//       }
//   });
// });




