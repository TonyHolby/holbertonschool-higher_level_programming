document.addEventListener('DOMContentLoaded', function() {
    const button = document.querySelector('#add_item');
    button.addEventListener('click', function() {
        const newelement = document.createElement('li');
        newelement.textContent = '<li>Item</li>';
        const myList = document.querySelector('.my_list');
        myList.appendChild(newelement);
    });
});
