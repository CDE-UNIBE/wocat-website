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
            collapseContainer.show();
            collapseButton.css('left', '100%');
            collapseIcon.removeClass('fa-caret-right').addClass('fa-caret-left')
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
        $('a[href$="#' + $(this).data('descendant-type') + '"]').tab('show');
        loadFilteredDataToPanel(
            $(this).data('descendant-url'),
            $('#' + $(this).data('descendant-type'))
        );
        return false;
      });

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

    function highlightItem(identifier) {
        console.log(identifier);
        $('#' + identifier).addClass('selected');
    }

    // Prepare geojson to use with leafleft; data is a list of elements or a
    // single element.
    function prepareMapData(data, panel) {
        panel.empty();
        var countriesJson = [];
        if ($.isArray(data)) {
            $.each(data, function (index, page) {
                panel.append(page.panel_text);
                countriesJson.push(_getGeoJson(page))
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
                        highlightItem(page.identifier);
                    });
                    layer.bindPopup(page.title);
                }
            });
        } catch (Error) {
            // @maybe: add error text as string?
            console.log(Error);
        }
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
