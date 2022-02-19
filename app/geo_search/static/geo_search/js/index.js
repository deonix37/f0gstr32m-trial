(() => {
    const searchForm = document.getElementById('search-form');
    const searchLocationIcon = new L.Icon.Default({
        className: 'search-location-marker',
    });

    let map;
    let searchLocationMarker;
    let nearbyLocationsGroup;

    window.addEventListener('map:init', function (evt) {
        map = evt.detail.map;
        nearbyLocationsGroup = new L.featureGroup().addTo(map);
    });

    searchForm.addEventListener('submit', async (evt) => {
        evt.preventDefault();

        await fetch(
            `/ajax/cities?${new URLSearchParams(new FormData(searchForm))}`,
        ).then((response) => {
            if (response.ok) {
                return response.json();
            }

            return Promise.reject(response);
        }).then((response) => {
            if (!response.searchLocation) {
                return alert('Не найдено');
            }

            if (searchLocationMarker) {
                map.removeLayer(searchLocationMarker);
            }
            nearbyLocationsGroup.clearLayers();

            searchLocationMarker = L.marker(response.searchLocation, {
                icon: searchLocationIcon,
            }).addTo(map);

            if (response.nearbyLocations.length) {
                for (const location of response.nearbyLocations) {
                    nearbyLocationsGroup.addLayer(L.marker(location));
                }

                map.fitBounds(nearbyLocationsGroup.getBounds());
            } else {
                map.setView(searchLocationMarker.getLatLng(), 9);
            }
        }).catch((response) => {
            alert(response.statusText);
        });
    });
})();
