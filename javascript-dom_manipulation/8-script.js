document.addEventListener('DOMContentLoaded', function() {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    fetch(url).then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        const hellovalue = document.querySelector('#hello');
        hellovalue.textContent = data.hello;
        });
    })
    .catch(error => {
      console.error('Problem during the fetch:', error);
});
