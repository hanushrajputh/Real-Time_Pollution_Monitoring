document.addEventListener("DOMContentLoaded", function() {
    fetch("/pollution_data")
        .then(response => response.json())
        .then(data => {
            const map = L.map('map').setView([12.9716, 77.5946], 10);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

            data.forEach(item => {
                L.circle([item.location[0], item.location[1]], {
                    color: item.pollution_level > 150 ? 'red' : 'green',
                    radius: 500
                }).addTo(map)
                .bindPopup(`Pollution Level: ${item.pollution_level}`);
            });
        });
});
