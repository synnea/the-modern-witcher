
// Get the currently active category from storage.

var currentCat = localStorage.getItem('currentCat');

// save the category ID into the currentCat variable.

$( ".cat-button" ).click(function() {
    localStorage.setItem('currentCat', $(this).attr('id'));
    $('#'+currentCat).addClass('selected');
  });
  

//   Upon document load, check if the currentCat variable exists.
//   if it does, set that category to active. If it doesn't, set the default all category view to active.

  $( document ).ready(function() {
    if (currentCat) {
        $('#'+currentCat).addClass('selected');

        localStorage.removeItem('currentCat');
    } else {
        $('.cat-all').addClass('selected');
    }
  });




