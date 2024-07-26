document.addEventListener('DOMContentLoaded', function() {
    const button = document.querySelector('#add_item');
    button.addEventListener('click', function() {
        const newelement = document.createElement('li');
        newelement.textContent = 'Item';
        const myList = document.querySelector('.my_list');
        myList.appendChild(newelement);
    });
});
