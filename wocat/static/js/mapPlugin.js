jQuery.fn.setMap = function( options ) {
    var settings = $.extend({
        countryDetailUrl: '',
        initialMapDataUrl: '',
        isInitialDetailPanel: 'false',
        showPanelFn: null
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
    var detailPanel = $('#map-panel');

    // store references to active geojson-layers.
    var layers = [];

    // initialize map.
    var map = L.map('map', {
        zoomControl: false
    }).setView([20, -30], 2);
    L.control.zoom({
        position: 'bottomright'
    }).addTo(map);

    L.tileLayer('https://services.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}.png', {
        minZoom: 2,
        attribution: '<a href="http://www.esri.com/legal/copyright-trademarks">Sources: Esri, HERE, DeLorme, Intermap, increment P Corp., GEBCO, USGS, FAO, NPS, NRCAN, GeoBase, IGN, Kadaster NL, Ordnance Survey, Esri Japan, METI, Esri China (Hong Kong), swisstopo, MapmyIndia, © OpenStreetMap contributors, and the GIS User Community</a>'
    }).addTo(map);

    // Load initial data depending on context. 'Detail'Pages such as ProjectPage
    // should initially display the panel, 'generic' pages should start with
    // the panel closed.
    if (settings.isInitialDetailPanel === 'true') {
        getMapFeatureDetail(settings.initialMapDataUrl);
    } else {
        showAllProjects(settings.initialMapDataUrl);
    }

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
        detailOverlay.hide();
        detailPanel.addClass('is-expanded');
        detailContainer.show();

        // purge layers on map and in the overlay-history.
        _purgeLayers();
        overlayUrlHistory.length = 0;

        if (filterUrl !== '') {
            // load single type (country, project or region).
            detailContainer.children('div').each(function() {
                $(this).empty();
            });
            _loadSearchResults(filterUrl, $(searchForm).serialize())
        } else {
            // load all
            filterSelect.each(function() {
                _loadSearchResults($(this).data('filter-url'), $(searchForm).serialize());
            });
        }
        return false;
    }

    // replace filtered data for container (projects, countries, regions);
    // container is purged after submitting the form.
    // three distinct containers guarantee the same ordering despite async
    // responses.
    function _loadSearchResults(filterUrl, search_string) {
        if (filterUrl) {
            var splitUrl = filterUrl.split('/');
            var targetClass = splitUrl[splitUrl.length - 2];
            var targetContainer = detailContainer.find('.' + targetClass).first();
            targetContainer.html(
                '<span class="glyphicon glyphicon-refresh spinning"></span>'
            );
            filterUrl += '?' + search_string;
            $.get(filterUrl).done(function (data) {
                targetContainer.html(data);
                setMapContext(data)
            });
        }
    }

    // apply filter from dropdown.
    function setFilter(event) {
        event.preventDefault();
        filterSpan.text($(this).text());
        filterUrl = $(this).data('filter-url');
        displaySearchResults();
    }

    // display country shapes on the map for all elements in the detailContainer
    function setMapContext(html) {
        $(html).find('li a').each(function() {
            _getDataFromAPI($(this).attr('href')).done(function(data) {
                loadGeoJSON(data);
            });
        });
    }

    // -----------
    // Item detail
    // -----------
    detailContainer.on('click', '.js-search-detail', function() {
        getMapFeatureDetail($(this).data('href'));
    });
    detailOverlay.on('click', '.js-overlay-close', function() {
        if (overlayUrlHistory.length > 1) {
            // load data from 'history'
            overlayUrlHistory.pop(); // pop current element
            getMapFeatureDetail(overlayUrlHistory.pop());
        } else {
            // 'initial' state: load data as defined in the filter/search box.
            displaySearchResults();
        }
        return false;
    });
    detailOverlay.on('click', '.show-descendant', function() {
        getMapFeatureDetail($(this).data('descendant-url'));
    });

    // ----------------
    // AJAX and GeoJSON
    // ----------------
    // For initial display: show elements as set by the url, defaults to all
    // countries.
    function showAllProjects() {
        _getDataFromAPI(
            settings.initialMapDataUrl
        ).done(function (data) {
            // display data on map
            loadGeoJSON(data);
        });
    }

    // Load and show single element in detail overlay
    function getMapFeatureDetail(url) {
        detailPanel.addClass('is-expanded');
        settings.showPanelFn();
        _purgeLayers();
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
        if ($.isArray(data)) {
            $.each(data, function (index, page) {
                _addLayer(page);
            });
        } else {
            _addLayer(data);
        }
    }

    // add layer to map and store reference
    function _addLayer(data) {
        var countryLayer = _getGeoJson(data);
        layers.push(countryLayer);
        map.addLayer(countryLayer);
    }

    // remove all layers from map
    function _purgeLayers() {
        if (layers.length > 0) {
            $.each(layers, function(index, layer) {
                map.removeLayer(layer)
            });
            layers = [];
        }
    }

    function _getGeoJson(page) {
        try {
            return L.geoJson(page.geojson, {
                style: mapStyle,
                onEachFeature: function onEachFeature(feature, layer) {
                    layer.on('click touch touchend', function() {
                        getMapFeatureDetail(
                            settings.countryDetailUrl + '?country_code=' + feature.id
                        )
                    });
                }
            });
        } catch (Error) {
            // console.log(Error);
        }
    }
};
