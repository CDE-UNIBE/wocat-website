jQuery.fn.setMap = function( options ) {
    var settings = $.extend({
        countryDetailUrl: '',
        initialMapDataUrl: ''
    }, options);

    var mapStyle = {
        // border styles
        "color": "#DA812C",
        "weight": 1,
        "opacity": 0.9,
        // fill styles
        "fillColor": "#F3D9C0",
        "fillOpacity": 0.5
    };

    var filterSelect = $('.js-set-filter li a');
    var filterSpan = $('#js-active-filter');
    var filterUrl = '';
    var searchForm = $('.js-search');
    var detailContainer = $('#map-detail');

    // initialize map.
    var map = L.map('map', {
        zoomControl: false
    }).setView([41, -20], 2);
    L.control.zoom({
        position: 'bottomright'
    }).addTo(map);

    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
    // L.tileLayer('https://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}.png', {
    //     attribution: '<a href="http://www.esri.com/legal/copyright-trademarks">Esri, HERE, DeLorme, MapmyIndia, © OpenStreetMap contributors, and the GIS user community</a>'
    // }).addTo(map);

    getDataFromAPI(settings.initialMapDataUrl);

    // -----------------
    // Search and Filter
    // -----------------

    searchForm.on('submit', function(e) {
        e.preventDefault();
        displaySearchResults()
    });
    filterSelect.on('click', setFilter);

    // call api for selected filter and querystring from form.
    function displaySearchResults() {
        detailContainer.empty();
        if (filterUrl !== '') {
            // load single type (country, project or region).
            _loadSearchResults(filterUrl, $(searchForm).serialize())
        } else {
            // load all
            filterSelect.each(function() {
                _loadSearchResults($(this).data('filter-url'), $(searchForm).serialize());
            });
        }
        return false;
    }

    // append filtered data to menu; container is purged after submitting the form.
    function _loadSearchResults(filterUrl, search_string) {
        if (filterUrl) {
            if (search_string) filterUrl += '?' + search_string;
            $.get(filterUrl).done(function (data) {
                detailContainer.append(data);
            });
        }
    }

    // apply filter from dropdown.
    function setFilter() {
        filterSpan.text($(this).text());
        filterUrl = $(this).data('filter-url');
        displaySearchResults();
        return false;
    }

    // -----------
    // Item detail
    // -----------
    detailContainer.on('click', '.js-search-detail', function(e) {
        e.preventDefault();
        getDataFromAPI($(this).attr('href'));
        return false;
    });


    // ----------------
    // AJAX and GeoJSON
    // ----------------

    // Load data from API.
    function getDataFromAPI(url) {
        $.ajax({
            url: url,
            method: 'get',
            dataType: 'json',
            headers: {
                'accepts': 'application/json'
            }
        }).done(function (data) {
            loadGeoJSON(data);
        });
    }

    // Prepare geojson to use with leafleft; data is a list of elements or a
    // single element.
    function loadGeoJSON(data) {
        if ($.isArray(data)) {
            $.each(data, function (index, page) {
                map.addLayer(_getGeoJson(page));
            });
        } else {
            map.addLayer(_getGeoJson(data));
        }
    }

    function _getGeoJson(page) {
        try {
            return L.geoJson(page.geojson, {
                style: mapStyle,
                onEachFeature: function onEachFeature(feature, layer) {
                    layer.on('click', function() {
                        getDataFromAPI(
                            settings.countryDetailUrl + '?country_code=' + feature.id
                        );
                    });
                }
            });
        } catch (Error) {
            console.log(Error);
        }
    }
};
