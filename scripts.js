// Fetch images from the Flask app
fetch('http://127.0.0.1:5000/images')
.then(response => response.json())
.then(images => {
    // Get the column elements
    const col1 = document.getElementById('col1');
    const col2 = document.getElementById('col2');
    const col3 = document.getElementById('col3');

    // Distribute images round-robin
    images.forEach((image, index) => {
        const img = document.createElement('img');
        img.src = `http://127.0.0.1:5000/static/images/${image}`;
        img.alt = image;

        // Append to the correct column based on index
        if (index % 3 === 0) {
            col1.appendChild(img);
        } else if (index % 3 === 1) {
            col2.appendChild(img);
        } else {
            col3.appendChild(img);
        }
    });
})
.catch(error => console.error('Error fetching images:', error));