document.addEventListener('DOMContentLoaded', function() {
    const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
    fetch(url).then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        const movieslist = document.querySelector('#list_movies');
        data.results.forEach(movie => {
            const element = document.createElement('li');
            element.textContent = movie.title;
            movieslist.appendChild(element);
        });
    })
    .catch(error => {
      console.error('Problem during the fetch:', error);
    });
});
