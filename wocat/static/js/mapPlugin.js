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

    var filterUrl = '';
    var overlayUrlHistory = [];
    var filterSelect = $('.js-set-filter li a');
    var filterSpan = $('#js-active-filter');
    var searchForm = $('.js-search');
    var detailContainer = $('#js-map-detail');
    var detailOverlay = $('#js-map-detail-overlay');

    // store references to active geojson-layers.
    var layers = [];

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

    // load initial data
    showAllProjects(settings.initialMapDataUrl);

    // -----------------
    // Search and Filter
    // -----------------

    searchForm.on('submit', function(e) {
        e.preventDefault();
        displaySearchResults(true)
    });
    filterSelect.on('click', setFilter);

    // call api for selected filter and querystring from form.
    function displaySearchResults(showContainer) {
        detailOverlay.hide();
        if (showContainer) detailContainer.empty().show();
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
        displaySearchResults(true);
        return false;
    }

    // -----------
    // Item detail
    // -----------
    detailContainer.on('click', '.js-search-detail', function() {
        getMapFeatureDetail($(this).attr('href'));
        return false;
    });
    detailOverlay.on('click', '.js-overlay-close', function() {
        if (overlayUrlHistory.length > 1) {
            overlayUrlHistory.pop(); // current element
            getMapFeatureDetail(overlayUrlHistory.pop());
        } else {
            detailOverlay.hide();
            detailContainer.show();
        }
        return false;
    });
    detailOverlay.on('click', '.show-descendant', function() {
        getMapFeatureDetail($(this).data('descendant-url'));
        return false;
    });

    // ----------------
    // AJAX and GeoJSON
    // ----------------

    function showAllProjects() {
        _getDataFromAPI(
            settings.initialMapDataUrl
        ).done(function (data) {
            // display data on map
            loadGeoJSON(data);
            displaySearchResults(false);
        });
    }

    function getMapFeatureDetail(url) {
        _getDataFromAPI(url).done(function(data) {
            // display data on map
            loadGeoJSON(data);
            // show detail overlay
            detailContainer.hide();
            detailOverlay.html(data.panel_text).show();
        });
        overlayUrlHistory.push(url);
    }

    // Load data from API.
    function _getDataFromAPI(url) {
        return $.ajax({
            url: url,
            method: 'get',
            dataType: 'json',
            headers: {
                'accepts': 'application/json'
            }
        });
    }

    // Prepare geojson to use with leafleft; data is a list of elements or a
    // single element.
    function loadGeoJSON(data) {
        if (layers.length > 0) {
            $.each(layers, function(index, layer) {
                map.removeLayer(layer)
            });
        }

        if ($.isArray(data)) {
            $.each(data, function (index, page) {
                _addLayer(page);
            });
        } else {
            _addLayer(data);
        }
    }

    function _addLayer(data) {
        var countryLayer = _getGeoJson(data);
        layers.push(countryLayer);
        map.addLayer(countryLayer);
    }

    function _getGeoJson(page) {
        try {
            return L.geoJson(page.geojson, {
                style: mapStyle,
                onEachFeature: function onEachFeature(feature, layer) {
                    layer.on('click', function() {
                        getMapFeatureDetail(
                            settings.countryDetailUrl + '?country_code=' + feature.id
                        )
                    });
                }
            });
        } catch (Error) {
            console.log(Error);
        }
    }
};
