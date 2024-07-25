document.addEventListener('DOMContentLoaded', function() {
    const button = document.querySelector('#update_header');
    button.addEventListener('click', function() {
        const element = document.querySelector('header');
        element.textContent = 'New Header!!!';
    });
});
