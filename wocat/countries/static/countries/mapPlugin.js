/**
 * mapPlugin
 * ---------
 * jQuery Plugin for the interactive map; also include the template:
 * 'countries/map.html'
 *
 * @maybe: load this plugin in the map.html template? independent loading allows
 * more flexibility regarding plugin loading, so leave it as is right now.
 *
 * Usage example:
 *---------------
 * {% load static %}
 *
 * {% include 'countries/map.html' %}
 * <script src="https://unpkg.com/leaflet@1.0.1/dist/leaflet.js"></script>
 * <script src="{% static 'countries/mapPlugin.js' %}"></script>
 * <script>
 *   $('#map').setMap();
 * </script>
 *
 */

jQuery.fn.setMap = function( options ) {
    var settings = $.extend({
        defaultTab: $('li[role="presentation"].active a')[0],
        selectedItem: null
    }, options);

    var layerStore = {};  // store references to layergoups (tabs) .
    var activeLayer = null;  // flag for the currently active layer.

    // initialize map.
    var map = L.map('map');
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    map.setView({lat: 47.040182144806664, lng: 9.667968750000002}, 1);

    // attach behavior for click on tabs and load initial content.
    selectMapContent(settings.defaultTab);
    $('a[data-toggle="tab"]').on('show.bs.tab', function (e) {
        selectMapContent(e.target)
    });

    // register clicks on menu and load more info element.
    $('div.tab-content').on('click', 'a', function () {
        return false;
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

    function foo(e) {
        console.log(e);
    }

    function onEachFeature(feature, layer) {
        layer.bindPopup(feature.properties.name);
        layer.on('click', foo);
    }

    // Prepare geojson to use with leafleft
    function prepareMapData(data, panel) {
        var countriesJson = [];
        $.each(data, function (index, page) {
            panel.append(page.panel_text);
            // todo: wrap into try/except
            var geojson = L.geoJson(page.geojson, {
                onEachFeature: onEachFeature
            });
            geojson.on('click', function (e) {
                console.log(e)
            });
            countriesJson.push(geojson);
        });
        // aaaah - check if click elements are ok for layergroups!
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
