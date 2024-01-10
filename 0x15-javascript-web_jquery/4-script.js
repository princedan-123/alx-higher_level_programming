/* Handling click event with JQuery API */

$(
  function () {
    $('#toggle_header').click(
      function () {
        $('header').toggleClass('red green');
      }
    );
  }
);
