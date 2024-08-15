function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);
   let inpuField = document.getElementById('searchField');
   let rowsElement = Array.from(document.querySelectorAll('tbody, tr'));

   function onClick(){
      for(let row of rowsElement){
         row.classList.remove('select');

         if (inpuField.value !== '' && row.innerHTML.includes(inpuField.value)){
            row.className = 'select';
         }
      }
      inpuField.value = '';
   }     

}