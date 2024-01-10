/* Handling click event with JQuery API */

$(
  function () {
    $('DIV#update_header').click(
      function () {
        $('header').text('New Header!!!');
      }
    );
  }
);
