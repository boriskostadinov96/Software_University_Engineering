function solve() {
  let inputElement = document.getElementById('input');
  let textArr = inputElement.value.split('.');
  let resultElement = document.getElementById('output');

  while (textArr.length > 0) {
    let sentences = textArr.splice(0, 3).filter(sentence => sentence.trim() !== '');
    if (sentences.length === 0) break;

    let text = sentences.join('. ').trim();

    if (text) {
      text += '.';
    }

    let p = document.createElement('p');

    p.textContent = text;

    resultElement.appendChild(p);
  }
}
