document.addEventListener('DOMContentLoaded', function() {
    const button = document.querySelector("#toggle_header");
    button.addEventListener('click', function() {
        const element = document.querySelector('header');
        if (element.classList.contains('red')) {
            element.classList.remove('red');
            element.classList.add('green');
        } else if (element.classList.contains('green')) {
            element.classList.remove('green');
            element.classList.add('red');
        } else {
            element.classList.add('red');
        }
    });
});
