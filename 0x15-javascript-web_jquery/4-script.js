/* Handling click event with JQuery API */

$(
  function () {
    $('#toggle_header').click(
      function () {
        $('#toggle_header').toggleClass('red');
      }
    );
  }
);
