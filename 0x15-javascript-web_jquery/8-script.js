/* Fetching data from an API */
$(
  function () {
    const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
    $.get(url, (data) => {
      for (const i of data.results) {
        $('UL#list_movies').append(i.title);
      }
    });
  }
);
