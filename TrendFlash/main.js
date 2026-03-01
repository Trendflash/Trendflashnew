// main.js
document.addEventListener("DOMContentLoaded", () => {
  fetch('articles.json')
    .then(res => res.json())
    .then(articles => {
      const container = document.querySelector('.list');
      container.innerHTML = '';
      articles.slice().reverse().forEach(article => {
        const a = document.createElement('a');
        a.href = article.link;
        a.textContent = article.title;
        container.appendChild(a);
      });
    })
    .catch(err => console.error("記事の読み込みに失敗しました:", err));
});