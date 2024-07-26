document.addEventListener('DOMContentLoaded', function() {
    const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
    fetch(url).then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        const charactername = document.querySelector('#character');
        charactername.textContent = data.name;
    })
    .catch(error => {
      console.error('Problem during the fetch:', error);
    });
});
