// script.js

// Function to get the user's current geographical location
function getLocation() {
    // Check if the Geolocation API is supported by the browser
    if (navigator.geolocation) {
        // Request the user's position; success and error are handled by sendLocation and showError functions
        navigator.geolocation.getCurrentPosition(sendLocation, showError);
    } else {
        // Alert the user if Geolocation is not supported by the browser
        alert("Geolocation is not supported by this browser.");
    }
}

// Function to handle the successful retrieval of the user's position
function sendLocation(position) {
    // Extract latitude and longitude from the position object
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;

    // Send the location data to the backend server using a POST request
    fetch('/location', {
        method: 'POST', // Specify the request method
        headers: {
            'Content-Type': 'application/json', // Set the content type to JSON
        },
        body: JSON.stringify({ latitude: latitude, longitude: longitude }) // Convert the location data to JSON
    })
    .then(response => response.json()) // Parse the response as JSON
    .then(data => {
        console.log('Success:', data); // Log the success response
        // Update the webpage with the received sunrise and sunset data
        document.getElementById('sunrise').textContent = `Sunrise: ${data.sunrise}`;
        document.getElementById('sunset').textContent = `Sunset: ${data.sunset}`;
    })
    .catch((error) => {
        console.error('Error:', error); // Log any errors that occur during the fetch operation
    });
}

// Function to handle errors that occur when trying to get the user's position
function showError(error) {
    // Determine the type of error that occurred and alert the user with a corresponding message
    switch(error.code) {
        case error.PERMISSION_DENIED:
            alert("User denied the request for Geolocation."); // User denied permission
            break;
        case error.POSITION_UNAVAILABLE:
            alert("Location information is unavailable."); // Location information is unavailable
            break;
        case error.TIMEOUT:
            alert("The request to get user location timed out."); // Request timed out
            break;
        case error.UNKNOWN_ERROR:
            alert("An unknown error occurred."); // An unknown error occurred
            break;
    }
}

