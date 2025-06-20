// This is a minimal service worker.
// Its presence is what makes the browser treat the site as a PWA
// and show the "Add to Home Screen" prompt.

self.addEventListener('install', (event) => {
  console.log('Service Worker: Installed');
});

self.addEventListener('activate', (event) => {
  console.log('Service Worker: Activated');
});

self.addEventListener('fetch', (event) => {
  // For now, we are just passing through the network request.
  // This is where you would add offline caching logic in a more advanced PWA.
  event.respondWith(fetch(event.request));
});