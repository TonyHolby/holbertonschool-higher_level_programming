document.addEventListener('DOMContentLoaded', function() {
    const button = document.querySelector('#red_header');
    button.addEventListener('click', function() {
        const element = document.querySelector('header');
        element.style.color = '#FF0000';
    });
});