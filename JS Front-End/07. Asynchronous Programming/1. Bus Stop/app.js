async function getInfo() {
    const stopID = document.getElementById('stopId').value;
    const url = `http://localhost:3030/jsonstore/bus/businfo/${stopID}`;

    const stopNameElement = document.getElementById('stopName');
    const timeTableElement = document.getElementById('buses');

    try {
    stopNameElement.textContent = 'Loading...'
    timeTableElement.replaceChildren();
    const res = await fetch(url);

    if(res.status !== 200){
        alert('Stop ID not found!')
    }
    const data = res.json();

    stopNameElement.textContent = data.name

    Object.entries(data.buses).forEach(b =>{
        const liElement = document.createElement('li');
        liElement.textContent = `Bus ${b[0]} arrives in ${b[1]} minutes`;
        timeTableElement.appendChild(liElement);
    })
        
    } catch (error) {
        stopNameElement.textContent = 'Error';
        
    }
    
}