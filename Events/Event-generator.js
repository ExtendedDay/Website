document.addEventListener('DOMContentLoaded', () => {
    fetch('Events.json')
        .then(response => response.json())
        .then(data => generateEventList(data))
        .catch(error => console.error('Error loading JSON:', error));
});

function generateEventList(events) {
    const eventListContainer = document.querySelector('.event-list-container');

    events.forEach(event => {
        const eventCard = document.createElement('div');
        eventCard.className = `event-card class${event.class.toUpperCase()}`;

        const eventDate = new Date(event.date);
        const eventMonth = eventDate.toLocaleString('default', { month: 'long' });
        let eventDayNumber = eventDate.getDate().toString().padStart(2, '0');
        const eventDayName = eventDate.toLocaleString('default', { weekday: 'long' });

        eventCard.innerHTML = `
            <div class="event-date-container">
                <div class="event-month">${eventMonth}</div>
                <div class="event-day-number">${eventDayNumber}</div>
                <div class="event-day-name">${eventDayName}</div>
            </div>
            <div class="event-info">
                <div class="event-top">
                    <div class="location-container">
                        <p>Location:</p>
                        <h3>
                            <a href="${event.link}" target="_blank" rel="noopener noreferrer">
                                <div class="map-symbol bx bx-map"></div>
                                <p>${event.location}</p>
                            </a>
                        </h3>
                        <p>(${event.time})</p>
                    </div>
                    <div class="event-fee-container">
                        <p>Fee per child:</p>
                        <p>${event.cost}</p>
                        <p class="optional-text" data-visible="${event.optional}">(Optional for snacks)</p>
                    </div>
                </div>
                <div class="event-description-container">
                    <p>${event.description}</p>
                </div>
            </div>
        `;

        eventListContainer.appendChild(eventCard);
    });
}
