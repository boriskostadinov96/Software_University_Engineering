function solve() {
  let textElement = document.getElementById('text').value;
  let conventionElement = document.getElementById('naming-convention').value;
  let result = '';
  
  if(conventionElement === 'Camel Case') {
    for (let currentIndex = 0; currentIndex < textElement.length; currentIndex++){
      
      if (textElement[currentIndex] === ' ') {
        result += (textElement[currentIndex+1].toUpperCase());
        currentIndex++;
      
      } else{
        result += textElement[currentIndex].toLowerCase();
      }
    }

  }else if(conventionElement === 'Pascal Case') {
    result += textElement[0].toUpperCase();

    for(let currentIndex = 1; currentIndex < textElement.length; currentIndex ++){
      
      if (textElement[currentIndex] === ' ') {
        result += (textElement[currentIndex+1].toUpperCase());
        currentIndex++;
      
      } else{
        result += textElement[currentIndex].toLowerCase();
      }
    }

  }else {
    result = 'Error!'
  }

  let finalResult = document.getElementById('result')
  finalResult.textContent = result
}