async function solution() {
    const main = document.getElementById('main');
    const url = `http://localhost:3030/jsonstore/advanced/articles/list`;

    const response = await fetch(url);
    const data = await response.json();

    data.forEach(a => {
        let divAccordion = createElement('div', '', ['class', 'acordion']);
        let divHead = createElement('div', '', ['class', 'head'])
        let span = createElement('span')
        let button = createElement('button', 'More', ['class', 'button', 'id', a._id])

        let divExtra = createElement('div', '', ['class', 'extra']);
        let p = createElement('p');

        button.addEventListener('click', toggle);

        divExtra.appendChild(p);
        divAccordion.appendChild(divExtra);
        divHead.appendChild(button);
        divHead.appendChild(span);
        divAccordion.appendChild(divHead)
        main.appendChild(divAccordion);
    })

    function createElement(type, content,attributes = []){
        const element = document.createElement(type);

        if(content){
            element.textContent = content;
        }
    }
}