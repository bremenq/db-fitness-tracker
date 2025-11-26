/* map-functionality.js — initialize Leaflet map from IP geolocation
Expects server endpoints:
- /get_client_info.py -> returns JSON { ip: "x.x.x.x" }
- /geolocation.py?ip=... -> returns JSON { ip: "x.x.x.x", loc: "lat,lng" , city: "", region: "", country: "" }


Notes:
- Fallback to default coords (Constructor University) for private/local IPs or failures
- Zoom level set to 12
*/


(function () {
'use strict';



const ENDPOINT_CLIENT = '/get_client_info.py';
const ENDPOINT_GEO = '/geolocation.py'; 
const GEO_PROVIDER = 'ipinfo.io';
const DEFAULT_COORDS = { lat: 53.1677, lng: 8.6510 }; // Constructor University coordinates
const DEFAULT_ZOOM = 12;
const PRIVATE_IP_REGEX = /^(10\.|172\.(1[6-9]|2[0-9]|3[0-1])\.|192\.168\.|127\.|::1$|fc00:|fe80:)/i;
const IP_VALIDATE = /^(?:\d{1,3}\.){3}\d{1,3}$/; // simple v4 check, server should validate more strictly


// UI 
const spinner = document.getElementById('spinner');
const statusText = document.getElementById('statusText');
const errorMsg = document.getElementById('errorMsg');
const retryBtn = document.getElementById('retryBtn');
const detectedIpEl = document.getElementById('detectedIp');
const detectedCoordsEl = document.getElementById('detectedCoords');
const geoProviderEl = document.getElementById('geoProvider');


let map, marker, ipAddress;


function showSpinner(show, text) {
spinner.style.display = show ? 'block' : 'none';
statusText.textContent = text || '';
errorMsg.hidden = true;
}


function showError(msg) {
spinner.style.display = 'none';
errorMsg.textContent = msg;
errorMsg.hidden = false;
statusText.textContent = 'Error';
}


function safeFetch(url, opts = {}, retries = 2) {
return fetch(url, opts).catch(err => {
if (retries > 0) return new Promise(resolve => setTimeout(resolve, 700)).then(() => safeFetch(url, opts, retries - 1));
throw err;
});
}


function initMap(coords) {
// create map one time
if (!map) {
map = L.map('map', { tap: true }).setView([coords.lat, coords.lng], DEFAULT_ZOOM);


L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
maxZoom: 19,
attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);
} else {
map.setView([coords.lat, coords.lng], DEFAULT_ZOOM);
}

//icon using default leflet icon
const icon = L.icon({
  iconUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png',
  shadowUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png'
});


if (marker) marker.remove();
marker = L.marker([coords.lat, coords.lng], { icon, keyboard: false, title: 'Your approximate location' }).addTo(map);


const popupContent = `<strong>IP:</strong> ${ipAddress || 'unknown'}`;
marker.bindPopup(popupContent, { closeButton: true, offset: [0, -10] });


// Open popup on mobile after short delay to ensure it is visible
setTimeout(() => marker.openPopup(), 500);


detectedCoordsEl.textContent = `${coords.lat.toFixed(5)}, ${coords.lng.toFixed(5)}`;
}


})();
