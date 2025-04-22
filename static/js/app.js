// for contact form 

document.getElementById('contactForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData);

    const response = await fetch('/contact/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}', // Include the CSRF token here
        },
        body: JSON.stringify(data),
    });

    const result = await response.json();
    alert(result.message);
});