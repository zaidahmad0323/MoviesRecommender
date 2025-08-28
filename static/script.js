document.getElementById('recommend-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const title = document.getElementById('movie-title').value;
    const recommendationsDiv = document.getElementById('recommendations');
    recommendationsDiv.innerHTML = "<p>Loading...</p>";

    try {
        const response = await fetch('http://localhost:5000/recommend', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title })
        });

        const data = await response.json();
        recommendationsDiv.innerHTML = "";
        if (data.recommendations.length === 0) {
            recommendationsDiv.innerHTML = "<p>No recommendations found.</p>";
        }
        data.recommendations.forEach(rec => {
            const div = document.createElement('div');
            div.className = "recommendation";
            div.innerHTML = `<img src="${rec.poster}" alt="${rec.title} poster"><br>${rec.title}`;
            recommendationsDiv.appendChild(div);
        });
    } catch (error) {
        recommendationsDiv.innerHTML = "<p>Error fetching recommendations.</p>";
    }
});