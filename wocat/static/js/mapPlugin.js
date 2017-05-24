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

    // initialize map.
    var map = L.map('map').setView([41, -20], 2);
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // attach behavior for click on tabs and load initial content.
    selectMapContent(settings.defaultTab);
    $('a[data-toggle="tab"]').on('show.bs.tab', function (e) {
        selectMapContent(e.target)
    });

    // register clicks on menu and load more info element.
    $('div.tab-content').on('click', 'a', function () {
        highlightItem($(this).attr('id'));
        return false;
    });

    mapFilter.on('change', function() {
        var target = $('li[role="presentation"].active a')[0];
        var panel = $(target.href.substr(target.href.indexOf('#')));
        panel.empty();
        getDataFromAPI(
           target.dataset.url+'?q='+$(this).val(),
           prepareMapData,
           panel
       );
    });

    // Load data just initially, and after that display the stored layer on
    // the map.
    function selectMapContent(target) {
        var panel = $(target.href.substr(target.href.indexOf('#')));
        if (panel.is(':empty')) {
            getDataFromAPI(target.dataset.url, prepareMapData, panel);
        } else {
            setMapData(panel.attr('id'));
        }
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

    function highlightItem(identifier) {
        console.log(identifier);
        $('#' + identifier).addClass('selected');
    }

    // Prepare geojson to use with leafleft
    function prepareMapData(data, panel) {
        var countriesJson = [];
        $.each(data, function (index, page) {
            panel.append(page.panel_text);
            try {
                var geojson = L.geoJson(page.geojson, {
                    style: defaultStyle,
                    onEachFeature: function onEachFeature(feature, layer) {
                        layer.on('click', function() {
                            highlightItem(page.identifier);
                        });
                        layer.bindPopup(page.title);
                    }
                });
            } catch (Error) {
                // @maybe: add error text as string?
            }
            countriesJson.push(geojson);
        });
        layerStore[panel.attr('id')] = L.layerGroup(countriesJson);
        setMapData(panel.attr('id'));
    }

    // Make sure just one layer is active at a time.
    // @maybe: just toggle opacity (if available).
    function setMapData(panelId) {
        if (activeLayer != null) {
            map.removeLayer(activeLayer);
        }
        map.addLayer(layerStore[panelId]);
        activeLayer = layerStore[panelId];
    }

};
