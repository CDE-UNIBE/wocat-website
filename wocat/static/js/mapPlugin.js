jQuery.fn.setMap = function( options ) {
    var settings = $.extend({
        defaultTab: $('li[role="presentation"].active a')[0],
        selectedItem: null
    }, options);

    var layerStore = {};  // store references to layergoups (tabs) .
    var activeLayer = null;  // flag for the currently active layer.
    var defaultStyle = {
        // border styles
        "color": "#DA812C",
        "weight": 1,
        "opacity": 0.9,
        // fill styles
        "fillColor": "#F3D9C0",
        "fillOpacity": 0.5
    };
    var mapFilter = $('.map-filter');
    var collapseContainer = $('#map-legend-collapse');
    var collapseButton = $('.map-legend-collapse-button');
    var collapseIcon = collapseButton.children().first();


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

    // attach behavior for click on tabs and load initial content.
    selectMapContent(settings.defaultTab);
    $('.nav-tabs li a').on('click', function (e) {
        selectMapContent(e.target)
    });

    // show hide for legend-panel
    collapseButton.on('click', function() {
        if (collapseContainer.is(':visible')) {
            collapseContainer.hide();
            collapseButton.css('left', '0%');
            collapseIcon.removeClass('fa-caret-left').addClass('fa-caret-right')
        } else {
            _showCollapsedLegend()
        }
    });

    // reload data from api on filter change.
    mapFilter.on('change', function() {
        var target = $('li[role="presentation"].active a')[0];
        var panel = $(target.href.substr(target.href.indexOf('#')));
        var url = target.dataset.url+'?q='+$(this).val();
        loadFilteredDataToPanel(url, panel);
    });

    // Load data for clicked descendant and switch tab.
    $('div.tab-content').on('click', 'a.show-descendant', function() {
        loadSingleElementToPanel(
            $(this).data('descendant-type'),
            $(this).data('descendant-url')
        )
    });

    function loadInfoForMapElement(countryCode) {
        loadSingleElementToPanel(
            'countries',
            '/api/v1/country-detail/' + countryCode + '/'
        );
        if (collapseContainer.not(':visible')) {
            _showCollapsedLegend()
        }
    }

    function loadSingleElementToPanel(panelId, url) {
        $('a[href$="#' + panelId + '"]').tab('show');
        loadFilteredDataToPanel(
            url, $('#' + panelId)
        );
        return false;
    }

    function loadFilteredDataToPanel(url, panel) {
        panel.empty();
        getDataFromAPI(
           url,
           prepareMapData,
           panel
       );
    }

    // Load data just initially, and after that display the stored layer on
    // the map.
    function selectMapContent(target) {
        var panel = $(target.href.substr(target.href.indexOf('#')));
        getDataFromAPI(target.dataset.url, prepareMapData, panel);
    }

    // Load data from API.
    function getDataFromAPI(url, callback, panel) {
        $.ajax({
            url: url,
            method: 'get',
            dataType: 'json',
            headers: {
                'accepts': 'application/json'
            }
        }).done(function (data) {
            callback(data, panel);
        });
    }

    // Prepare geojson to use with leafleft; data is a list of elements or a
    // single element.
    function prepareMapData(data, panel) {
        panel.empty();
        var countriesJson = [];
        if ($.isArray(data)) {
            $.each(data, function (index, page) {
                panel.append(page.panel_text);
                var geoJson = _getGeoJson(page);
                if (geoJson) {
                    countriesJson.push(geoJson)
                } else {
                    console.log(page);
                }
            });
        } else {
            panel.append(data.panel_text);
            countriesJson.push(_getGeoJson(data))
        }
        layerStore[panel.attr('id')] = L.layerGroup(countriesJson);
        setMapData(panel.attr('id'));
    }

    function _getGeoJson(page) {
        try {
            return L.geoJson(page.geojson, {
                style: defaultStyle,
                onEachFeature: function onEachFeature(feature, layer) {
                    layer.on('click', function() {
                        // feature.id is the country code.
                        loadInfoForMapElement(layer.feature.id);
                    });
                    layer.bindPopup(page.title);
                }
            });
        } catch (Error) {
            // @maybe: add error text as string?
            console.log(Error);
        }
    }

    function _showCollapsedLegend() {
        collapseContainer.show();
        collapseButton.css('left', '100%');
        collapseIcon.removeClass('fa-caret-right').addClass('fa-caret-left')
    }

    // Make sure just one layer is active at a time.
    function setMapData(panelId) {
        if (activeLayer !== null) {
            map.removeLayer(activeLayer);
        }
        map.addLayer(layerStore[panelId]);
        activeLayer = layerStore[panelId];
    }
};
