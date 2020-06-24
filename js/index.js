$( document ).ready(function() {
  var optionElement = $("#options");
  optionElement.click(function(e)
  {
    console.log(e);
    $("#div1").show();
    $("#options-img").attr("src","https://img.icons8.com/small/480/000000/cancel.png");
  });
});


// #div1{
//   display: none;
// }
