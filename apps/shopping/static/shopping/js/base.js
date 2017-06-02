$(document).ready(function(){
  $('.sameAsShipping').click(function(){
  })
})

$(document).on("change", "select#sort_by", function(){
  $.ajax({
    url: '/products/orderBy',
    type: 'POST',
    data: $('#sort_form').serialize(),
    success: function(response) {
      $('#products_display').html(response)
    }
  })
});
