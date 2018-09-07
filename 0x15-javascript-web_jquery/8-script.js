$(function () {
  $.getJSON('https://swapi.co/api/films/?format=json', function (data, status) {
    $.each(data.results, function (index, val) {
      $('#list_movies').append('<li>' + val.title + '</li>');
    });
  });
});
