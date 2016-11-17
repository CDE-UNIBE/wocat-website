$(function() {
	// Stop annoying auto cycling
	$('.widget-carousel .carousel').carousel({interval: false});
});

$(function() {
	// Members Table
	$('.widget-members-table').each(function() {
		var membersTable = $(this);

		function applyFilters() {
			if (membersTable.find('.widget-members-table-countryselector').val() == "all") {
				var country = "all";
			} else {
				var country = membersTable.find('.widget-members-table-countryselector option:selected').text();
			}
			var expertise = membersTable.find('.widget-members-table-expertiseselector').val();
			var institution = membersTable.find('.widget-members-table-institutionselector').val();
			var sort = membersTable.find('.widget-members-table-sortselector').val();
			var page = membersTable.data('page');
			var maxpagesize = membersTable.find('.widget-members-table-members').data('maxpagesize');

			// console.log('Filter Country:', country, 'Filter Expertise:', expertise, 'Filter Institution:', institution, 'Sort by:', sort);


			// iterate members
			membersTable.find('.widget-members-table-members .widget-members-table-member').each(function() {
				var member = $(this);

				var memberName = $.trim(member.find('.widget-members-table-name').text());
				var memberCountry = $.trim(member.find('.widget-members-table-country').text());
				var memberInstitution = $.trim(member.find('.widget-members-table-institution .member-institution').text());
				var memberExpertises = member.find('.widget-members-table-expertises .expertise').map(function() {
						return $.trim($(this).text());
					}).get();

				// console.log('Member Name:', memberName, 'Member Institution:', memberInstitution, 'Member Country:', memberCountry, 'Member Expertises:', memberExpertises);

				// Country and Expertise and Institution match selection?
				if ((country != 'all') && (country != memberCountry)) member.addClass('member-hidden');
				if ((institution != 'all') && (institution != memberInstitution)) member.addClass('member-hidden');
				if ((expertise != 'all') && ($.inArray(expertise, memberExpertises) == -1)) member.addClass('member-hidden');
			});

			// Sort
			var sortedTable = $(".widget-members-table-members .widget-members-table-member").sort(function(a,b) {
				switch (sort) {
					case 'name':
						// Name
						var valueA = $.trim($(a).find('.widget-members-table-name').text());
						var valueB = $.trim($(b).find('.widget-members-table-name').text());
					break;
					case 'country':
						// Country
						var valueA = $.trim($(a).find('.widget-members-table-country').text());
						var valueB = $.trim($(b).find('.widget-members-table-country').text());
					break;
					case 'institution':
						// Institution
						var valueA = $.trim($(a).find('.widget-members-table-institution .member-institution').text());
						var valueB = $.trim($(b).find('.widget-members-table-institution .member-institution').text());
					break;
				}

				valueA = valueA.toLowerCase();
				valueB = valueB.toLowerCase();

				// console.log('Values to compare: ', valueA, valueB);

				if (valueA < valueB) //sort string ascending
					return -1;
				if (valueA > valueB)
					return 1;
				return 0; //default return value (no sorting)
			});
			membersTable.find('.widget-members-table-members').html(sortedTable);



			// Pagination
			var firstMemberNumber = maxpagesize*(page-1);
			var numberOfPages = Math.ceil(membersTable.find('.widget-members-table-members .widget-members-table-member:not(.member-hidden)').length / maxpagesize);
			//console.log('Show page: ', page, 'Max members per page: ', maxpagesize, 'First member: ', firstMemberNumber, 'Number of pages available: ', numberOfPages);
			// disable pagination if only one page
			if (numberOfPages < 2) {
				membersTable.find('.pages').hide();
			} else {
				membersTable.find('.pages').show();
				// disable pagination links
				membersTable.find('.pages .pagination li').show();
				membersTable.find('.pages .pagination li:gt('+ (numberOfPages-1) +')').hide();
			}
			// get rid of members of previous pages:
			membersTable.find('.widget-members-table-members .widget-members-table-member:not(.member-hidden):lt('+ firstMemberNumber+')').addClass('member-hidden');
			// get rid of members of next pages:
			membersTable.find('.widget-members-table-members .widget-members-table-member:not(.member-hidden):gt('+ (maxpagesize-1) +')').addClass('member-hidden');

			membersTable.find('.pages .pagination li').removeClass('active');
			membersTable.find('.pages .pagination li:nth-child('+ (page) +')').addClass('active');



			// Show exactly the members we want to see
			membersTable.find('.widget-members-table-members .widget-members-table-member').each(function() {
				var member = $(this);

				if (member.hasClass('member-hidden')) {
					member.removeClass('member-hidden').hide();
				} else {
					member.show();
				}
			});

			// Show error message when no member found with filter
			if (membersTable.find('.widget-members-table-members .widget-members-table-member:not(:hidden)').length) {
				membersTable.find('.widget-members-table-nothingfound').hide();
			} else {
				membersTable.find('.widget-members-table-nothingfound').show();
			}

		}

		membersTable.find('.widget-members-table-countryselector, .widget-members-table-institutionselector, .widget-members-table-expertiseselector, .widget-members-table-sortselector').change(function() {
			// reset page
			membersTable.data('page', 1);
			applyFilters();
		});

		membersTable.find('.pagination a').click(function(event) {
			event.preventDefault();
			// set page
			var page = $(this).data('page');
			membersTable.data('page', page);
			applyFilters();
		});


		membersTable.find('.widget-members-table-headline .widget-members-table-name').click(function(event) {
			membersTable.find('.widget-members-table-sortselector').val('name').change();
		});
		membersTable.find('.widget-members-table-headline .widget-members-table-country').click(function(event) {
			membersTable.find('.widget-members-table-sortselector').val('country').change();
		});
		membersTable.find('.widget-members-table-headline .widget-members-table-institution').click(function(event) {
			membersTable.find('.widget-members-table-sortselector').val('institution').change();
		});
	});



	$('.widget-members-table').each(function() {
		// OPTION element with countries
		var countries = $(this).find('.widget-members-table-countryselector option');
		// URL hash
		var hash = window.location.hash.toUpperCase().replace("#", "");

		// Is there a country with the name of the hash?
		if (countries.filter('[value="'+ hash +'"]').length) {
			// Change the SELECT to the country
			$(this).find('.widget-members-table-countryselector').val(hash);
			$(this).find('.widget-members-table-countryselector').change(); // Doppelt hält besser
		}
	});

});




$(function() {
	// Institutions Table
	$('.widget-institutions-table').each(function() {
		var institutionsTable = $(this);

		function applyFilters() {
			if (institutionsTable.find('.widget-institutions-table-countryselector').val() == "all") {
				var country = "all";
			} else {
				var country = institutionsTable.find('.widget-institutions-table-countryselector option:selected').text();
			}
			var sort = institutionsTable.find('.widget-institutions-table-sortselector').val();
			var page = institutionsTable.data('page');
			var maxpagesize = institutionsTable.find('.widget-institutions-table-institutions').data('maxpagesize');

			console.log('Filter Country:', country, 'Sort by:', sort, 'maxpagesize:', maxpagesize);


			// iterate institutions
			institutionsTable.find('.widget-institutions-table-institutions .widget-institutions-table-institution').each(function() {
				var institution = $(this);

				var institutionName = $.trim(institution.find('.widget-institutions-table-name').text());
				var institutionCountry = $.trim(institution.find('.widget-institutions-table-country').text());

				//console.log('Institution Name:', institutionName, 'Institution Country:', institutionCountry);

				// Country and Expertise and Institution match selection?
				if ((country != 'all') && (country != institutionCountry)) institution.addClass('institution-hidden');
			});

			// Sort
			var sortedTable = $(".widget-institutions-table-institutions .widget-institutions-table-institution").sort(function(a,b) {
				switch (sort) {
					case 'name':
						// Name
						var valueA = $.trim($(a).find('.widget-institutions-table-name').text());
						var valueB = $.trim($(b).find('.widget-institutions-table-name').text());
					break;
					case 'country':
						// Country
						var valueA = $.trim($(a).find('.widget-institutions-table-country').text());
						var valueB = $.trim($(b).find('.widget-institutions-table-country').text());
					break;
				}

				valueA = valueA.toLowerCase();
				valueB = valueB.toLowerCase();

				// console.log('Values to compare: ', valueA, valueB);

				if (valueA < valueB) //sort string ascending
					return -1;
				if (valueA > valueB)
					return 1;
				return 0; //default return value (no sorting)
			});
			institutionsTable.find('.widget-institutions-table-institutions').html(sortedTable);



			// Pagination
			var firstInstitutionNumber = maxpagesize*(page-1);
			var numberOfPages = Math.ceil(institutionsTable.find('.widget-institutions-table-institutions .widget-institutions-table-institution:not(.institution-hidden)').length / maxpagesize);
			//console.log('Show page: ', page, 'Max institutions per page: ', maxpagesize, 'First institution: ', firstInstitutionNumber, 'Number of pages available: ', numberOfPages);
			// disable pagination if only one page
			if (numberOfPages < 2) {
				institutionsTable.find('.pages').hide();
			} else {
				institutionsTable.find('.pages').show();
				// disable pagination links
				institutionsTable.find('.pages .pagination li').show();
				institutionsTable.find('.pages .pagination li:gt('+ (numberOfPages-1) +')').hide();
			}
			// get rid of institutions of previous pages:
			institutionsTable.find('.widget-institutions-table-institutions .widget-institutions-table-institution:not(.institution-hidden):lt('+ firstInstitutionNumber+')').addClass('institution-hidden');
			// get rid of institutions of next pages:
			institutionsTable.find('.widget-institutions-table-institutions .widget-institutions-table-institution:not(.institution-hidden):gt('+ (maxpagesize-1) +')').addClass('institution-hidden');

			institutionsTable.find('.pages .pagination li').removeClass('active');
			institutionsTable.find('.pages .pagination li:nth-child('+ (page) +')').addClass('active');



			// Show exactly the institutions we want to see
			institutionsTable.find('.widget-institutions-table-institutions .widget-institutions-table-institution').each(function() {
				var institution = $(this);

				if (institution.hasClass('institution-hidden')) {
					institution.removeClass('institution-hidden').hide();
				} else {
					institution.show();
				}
			});

			// Show error message when no institution found with filter
			if (institutionsTable.find('.widget-institutions-table-institutions .widget-institutions-table-institution:not(:hidden)').length) {
				institutionsTable.find('.widget-institutions-table-nothingfound').hide();
			} else {
				institutionsTable.find('.widget-institutions-table-nothingfound').show();
			}

		}

		institutionsTable.find('.widget-institutions-table-countryselector, .widget-institutions-table-sortselector').change(function() {
			// reset page
			institutionsTable.data('page', 1);
			applyFilters();
		});

		institutionsTable.find('.pagination a').click(function(event) {
			event.preventDefault();
			// set page
			var page = $(this).data('page');
			institutionsTable.data('page', page);
			applyFilters();
		});


		institutionsTable.find('.widget-institutions-table-headline .widget-institutions-table-name').click(function(event) {
			institutionsTable.find('.widget-institutions-table-sortselector').val('name').change();
		});
		institutionsTable.find('.widget-institutions-table-headline .widget-institutions-table-country').click(function(event) {
			institutionsTable.find('.widget-institutions-table-sortselector').val('country').change();
		});
	});

});



$(function() {
	// Gibt es auf der Seite ein Affix?
	if (!$('#affix').length) return;

	// Deklaration von Variablen, die beim Scrollen gebraucht und meist nicht überschrieben werden.
	var doAffix;
	var state;
	var affixElement, affixTopStop, affixBottomStop, affixHeight, affixWidth;


	// Nach dem Scroll wird das Update des Affix um 50ms verzögert, um die Funktion seltener auszuführen.
	var scrollTimer = null;
	$(window).scroll(function () {
		if (scrollTimer) {
			return;
			//clearTimeout(scrollTimer);
		}
		if (doAffix) scrollTimer = setTimeout(handleScroll, 50); // set new timer
	});



	// Definition dieser Variablen bei Ready, Load und Resize. Resize umfasst auch Orientationchange und Zoom.
	function resetAffix() {
		//console.log('affixTopStop', affixTopStop, 'affixBottomStop', affixBottomStop, 'affixHeight', affixHeight);
		doAffix = $('#affix').is(":visible");
		state = null;
		affixElement = $('#affix');
		affixWrapperElement = $('#affix-wrapper');
		affixTopStop = $('#affix-wrapper').offset().top;
		affixBottomStop = $('#affix-bottom').offset().top;
		affixHeight = affixElement.height();
		affixWidth = affixWrapperElement.width();
		handleScroll();
	}
	// Calculate Affix area on resize and load ...
	$(window).on('resize load', resetAffix);
	// ... and every second ...
	setInterval(resetAffix, 1000);
	// ... and on ready.
	resetAffix();


	// Schauen, ob Viewport über, in oder unter dem Affix-Bereich ist.
	function handleScroll() {
		// reset timer
		scrollTimer = null;

		var scrollTop = $(window).scrollTop();


		if (scrollTop < affixTopStop) {
			//console.log('We are above affix area.');
			if (state != 'top') {
				affixElement.removeClass('affix-fixed').css({'top': 0, 'left': 0, 'width': '100%'});
				state = 'top';
			}
			return;
		}


		if ((scrollTop + affixHeight) > affixBottomStop) {
			//console.log('We are below affix area.');
			if (state != 'bottom') {
				var topOffset = affixBottomStop - affixTopStop - affixHeight;
				affixElement.removeClass('affix-fixed').css({'top': topOffset, 'left': 0, 'width': '100%'});
				state = 'bottom';
			}
			return;
		}

		// We are in affix area
		//console.log('We are in the affix area.');
		if (state != 'fixed') {
			var affixLeft = $('#affix-wrapper').offset().left;
			//console.log('affixLeft: ', affixLeft);

			affixElement.addClass('affix-fixed').css({'top': '0', 'left': affixLeft, 'width': affixWidth});
			state = 'fixed';
		}

	}
});






$(function() {
	// Gibt es auf der Seite eine Infobox mit Tabs?
	if (!$('.widget-tabinfobox').length) return;

	$('.widget-tabinfobox').each(function() {
		var tabinfoboxElement = $(this);
		var hash = false;

		function hashSpy() {
			var newHash = location.hash.replace('#', '');
			if (newHash !== hash) {
				hash = newHash;

				// Iterate sidebar links
				tabinfoboxElement.find('.widget-tabinfobox-sidebar a').each(function() {
					var sidebarlinkElement = $(this);
					if (sidebarlinkElement.attr('href') === '#'+hash) {
						sidebarlinkElement.parent().addClass('active');
					} else {
						sidebarlinkElement.parent().removeClass('active');
					}
				});
				// No tab active?
				if (tabinfoboxElement.find('.widget-tabinfobox-sidebar li.active').length == 0) {
					// Activate first tab as default
					tabinfoboxElement.find('.widget-tabinfobox-sidebar li').first().addClass('active');
				}


				// Iterate sections
				tabinfoboxElement.find('.widget-tabinfobox-section').each(function() {
					var sectionElement = $(this);
					if (sectionElement.attr('id') === hash) {
						sectionElement.show();

						$('html, body').stop().animate({
							scrollTop: sectionElement.offset().top
						}, 600);

					} else {
						sectionElement.hide();
					}
				});
				// No section active?
				if (tabinfoboxElement.find('.widget-tabinfobox-section:visible').length == 0) {
					// Show first tab as default
					tabinfoboxElement.find('.widget-tabinfobox-section').first().show();
				}
			}
		}
		tabinfoboxElement.find('.widget-tabinfobox-sidebar a').click(function(event) {
			window.location.hash = $(this).attr('href').replace('#', '');
			hashSpy();
			event.preventDefault();
		});
		$(window).on('hashchange', function() {
			hashSpy();
		});
		hashSpy();

	});

});



$(function() {
	$('.widget-multiselect').each(function() {
		var selectfield = $(this);
		var containerChecked = selectfield.find('.widget-options-checked');
		var containerNotChecked = selectfield.find('.widget-options-notchecked');

		function sortItems() {
			// Put selected to top and unselected to bottom container
			// Eventually sort items alphabetically

			containerChecked.find('label').each(function() {
				// move unchecked items down
				if (!$(this).find('input').prop('checked')) {
					var item = $(this).detach();
					item.appendTo( containerNotChecked );
				}
			});

			containerNotChecked.find('label').each(function() {
				// move checked items up
				if ($(this).find('input').prop('checked')) {
					var item = $(this).detach();
					item.appendTo( containerChecked );
				}
			});
		}

		selectfield.on('change', 'input', function() {
			sortItems();
		});

		if (selectfield.hasClass('widget-multiselect-nullable')) {
			// Radios are deselectable
			selectfield.on('click', '.widget-options-checked label', function() {
				// deselect this
				$(this).find('input').prop('checked', false);
				// this triggers sortItems() automatically.
			});
		}

		selectfield.find('.widget-select-customvalue').keypress(function (event) {
			var key = event.which;
			if(key == 13) { // the enter key code
				var value = $(this).val();

				// remove options that were manually entered before if this is a radio
				var singleselect = $(this).hasClass('widget-select-customvalue-singleselect');
				if (singleselect) {
					selectfield.find('.widget-select-newcustomvalue').remove();
				}

				// TODO: Make sure item is no duplicate

				// clone item template
				var newitem = $(selectfield.find('.widget-options-template').html());
				newitem
					.addClass('widget-select-newcustomvalue')
					.find('input')
					.prop('checked', true)
					.prop('value', value)
					.parent()
					.find('span').text(value);
				containerChecked.append(newitem);

				sortItems();

				// reset input
				$(this).val('');

				// Do not submit form
				event.preventDefault();
				return false;
			}
		});
	});
});


$(function() {
	$('.widget-multiselect-oneblock').each(function() {
		var selectfield = $(this);
		var selectallbutton = selectfield.find('input.widget-multiselect-oneblock-selectallbutton'); // select all button
		var regularinputs = selectfield.find('input:not(.widget-multiselect-oneblock-selectallbutton)'); // all other inputs

		// Without Select All Button we don't need logic for Select All Button.
		if (!selectallbutton.length) return;

		// Radio buttons work out of the box. JS is only needed for Checkboxes.
		if (selectfield.hasClass('widget-multiselect-singleselect')) return;

		selectallbutton.change(function(event) {
			console.log("c");
			// uncheck all other buttons
			regularinputs.removeAttr('checked');
			// check select-all-button
			$(this).prop('checked', true);

			// Do not allow unchecking
			event.preventDefault();
		});
		regularinputs.change(function() {
			// is any regular input checked?
			if (regularinputs.filter(':checked').length) {
				// uncheck select-all-button
				console.log("a");
				selectallbutton.removeAttr('checked');
			} else {
				// check select-all-button
				console.log("b");
				selectallbutton.prop('checked', true);
			}
		});
	});
});



$(function() {

	var countries;
	$.ajax({
		url: '/static/js/countries.geo.json',
		async: false,
		dataType: 'json',
		success: function (response) {
			countries = response;
		}
	});

	// Maps
	var mapcounter = 0;

	$('.widget-map').each(function() {
		// Find unique ID for this map
		mapcounter++;
		var mapElement = $(this);
		var id = 'leaflet-map' + mapcounter;
		mapElement.attr('id', id);


		// Are countries to show?
		if (mapElement.find('ul.widget-map-countryselector li').length) {
			var countryselector = [];
			// Store list of countries in countryselector.
			mapElement.find('ul.widget-map-countryselector li').each(function() {
				var countryData = {
					'iso_3166_1_alpha_3': $(this).find('.iso_3166_1_alpha_3').text()
				};
				if ($(this).find('.popup')) {
					countryData.popup = $(this).find('.popup').html();
				}
				countryselector.push(countryData);
			});
			mapElement.find('ul.widget-map-countryselector').remove();
		}

		var noInteraction = true; // We use this unless a map is fullscreen

		if (noInteraction) {
			var options = { zoomControl:false };
		} else {
			var options = {};
		}

		var view = {
			lat: 0,
			lon: 0,
			zoom: 1,
		};

		var map = L.map(id, options).setView([view.lat, view.lon], view.zoom);
		// OSM: http://{s}.tile.osm.org/{z}/{x}/{y}.png
		// Blackwhite: http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}@2x.png
		// Webspace: /static/images/tiles/tile{z}-{x}-{y}.png
		L.tileLayer('/static/images/tiles/tile{z}-{x}-{y}.png', {
			attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
			maxZoom: 5, // We don't have more tiles on local repository
		}).addTo(map);


		if (noInteraction) {
			map.dragging.disable();
			map.touchZoom.disable();
			map.doubleClickZoom.disable();
			map.scrollWheelZoom.disable();
			map.boxZoom.disable();
			map.keyboard.disable();
			if (map.tap) map.tap.disable();
		}


		var imagepath = "/static/images/leaflet/"
		var icons = {
			primary:
				L.icon({
					iconUrl: imagepath+'marker-primary.png',
					shadowUrl: imagepath+'marker-shadow.png',
					iconSize: [25, 41],
					iconAnchor: [12, 41],
					popupAnchor: [1, -34],
					shadowSize: [41, 41]
				}),
			secondary:
				L.icon({
					iconUrl: imagepath+'marker-secondary.png',
					shadowUrl: imagepath+'marker-shadow.png',
					iconSize: [25, 41],
					iconAnchor: [12, 41],
					popupAnchor: [1, -34],
					shadowSize: [41, 41]
				}),
		};


		/*
		// Display Markers
		marker = {
			lat: 51.5,
			lon: -0.09,
			marker: 'primary',
			popup: 'Yolo',
		};

		var popup = L.marker([marker.lat, marker.lon], {icon: icons[marker.marker]})
			.bindPopup(marker.popup)
			.addTo(map);
		*/



		if (countryselector) {

			// Country Code: ISO 3166-1 alpha-3
			// https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json

			var countryStyle = {
				weight: 2,
				opacity: 1,
				color: '#DA812C',
				fillOpacity: 0.3,
				fillColor: '#DA812C',
			};


			// The Leaflet Layer with all Countries
			var countriesLayerGroup = L.featureGroup();
			// Fit map to countries
			function mapToBoundaries() {
				var countriesBoudaries = countriesLayerGroup.getBounds();
				// With Leaflet pad() we could make the boundaries larger
				map.fitBounds(countriesBoudaries);
			}

			$.each(countryselector, function(index, countryData) {
				$.each(countries.features, function(index, feature) {
					if (feature.id == countryData.iso_3166_1_alpha_3) {
						var countryLayer = L.geoJson(feature, {
							style: countryStyle
						});
						countryLayer.addTo(map);

						if (countryData.popup) {
							// Add popup
							var popup = countryLayer.bindPopup( countryData.popup );
							if (noInteraction) {
								// Pan map back after popup closed
								popup.on("popupclose", function(e) {
									mapToBoundaries();
								});
							}
						}

						countriesLayerGroup.addLayer(countryLayer);
					}
				});
			});


			// Update map on resize
			var resizeTimer = null;
			$(window).resize(function () {
				if (resizeTimer) {
					clearTimeout(resizeTimer);
				}
				resizeTimer = setTimeout(mapToBoundaries, 200); // set new timer
			});

			mapToBoundaries();

		}

	});
});




$(function() {
	// Enable Scrollspy for sidebar affix navigation
	$('body').scrollspy({ target: '.widget-affix .widget-sidebar' });
});




$(function() {
	// Smooth Scroll
	$("a.anchorlink[href^='#']").on('click', function(e) {
		e.preventDefault();
		var hash = this.hash;
		$('html, body').stop().animate({
			scrollTop: $(this.hash).offset().top
		}, 600, function(){
			window.location.hash = hash;
		});
	});
});




$(function() {
	$("input.avatarfield-fileinput").each(function() {
		var fileElement = $(this); // Input type=file
		var removeButtonElement = $(fileElement.data('removebutton')); // Button zum Löschen der Datei
		var cropboxElement = $(fileElement.data('cropbox')); // Box zum Zuschneiden des Bildes
		var imageElement = cropboxElement.find('.avatarfield-cropbox-image');
		var cropinfoinputElement = $(fileElement.data('cropinfoinput')); // Hidden Input for crop info

		// Erstmal Reset
		fileElement.val("");
		cropinfoinputElement.val("{}"); // Always JSON



		removeButtonElement.click(function(event) {
			// Button zum Löschen der Datei geklickt
			fileElement.val('');
			fileElement.trigger('change'); // Feuert nicht von alleine
			event.preventDefault();
		});



		fileElement.change(function() {
			function avatarfieldError(error) {
				console.log('Error:'+ error);
				cropboxElement.hide();
				removeButtonElement.hide();
				fileElement.val('');
			}

			// console.log('Loading file: ' + fileElement.get(0).files[0].name);
			try {
				// Test if file looks good without opening it
				(function() {
					if (fileElement.get(0).files && fileElement.get(0).files[0]) {
						// Datei wurde ausgewählt
					} else {
						throw "no-file-chosen";
					}

					if (fileElement.get(0).files[0].size < 1000) {
						throw "file-too-small";
					}

					if (fileElement.get(0).files[0].size > 5000000) {
						throw 'file-too-large';
					}

					// Check mime type
					switch (fileElement.get(0).files[0].type) {
						case "image/jpeg":
						case "image/png":
						break;
						default: throw 'wrong-filetype'; break;
					}
				})();
				// console.log("File looks good.");
			}
			catch(error) {
				// Errors occured? Handle them.
				avatarfieldError(error);
				return; // Do not continue
			}




			// Try to show the image
			(function() {
				// Put selected image on page
				var reader = new FileReader();
				reader.onload = function (e) {
					imageElement.attr('src', e.target.result);
					// console.log("Reader loaded.");

					// Test if image is OK
					// http://stackoverflow.com/questions/318630/get-real-image-width-and-height-with-javascript-in-safari-chrome/670433#670433

					var realWidth, realHeight;
					$("<img/>") // Make in memory copy of image to avoid css issues
						.attr("src", imageElement.attr("src"))
						.load(function() {
							try {
								// console.log("Test image loaded.");
								testImage = $(this);
								testImage.removeAttr("width");
								testImage.removeAttr("height");

								realWidth = testImage.get(0).width;
								realHeight = testImage.get(0).height;


								// Test image size
								if (realWidth === undefined) { throw 'no-image'; return; }
								if (realHeight === undefined) { throw 'no-image'; return; }
								if (realWidth < 20) { throw 'wrong-imagesize'; return; }
								if (realHeight < 20) { throw 'wrong-imagesize'; return; }
								if (realWidth > 10000) { throw 'wrong-imagesize'; return; }
								if (realHeight > 10000) { throw 'wrong-imagesize'; return; }
								if (realHeight/realWidth > 4) { throw 'wrong-imagesize'; return; }
								if (realWidth/realHeight > 4) { throw 'wrong-imagesize'; return; }
							}
							catch(error) {
								// Errors occured? Handle them.
								avatarfieldError(error);
								return; // Do not continue
							}

							// console.log("Image looks good.");

							// Now the image finally looks fine.
							// Let the user crop the image.
							removeButtonElement.show();
							cropboxElement.show();
							cropboxElement.data('realWidth', realWidth);
							cropboxElement.data('realHeight', realHeight);

							// setup cropping interface
							cropboxElement.trigger('newimage');
					})
					.error(function() {
						// File could not be put into IMG element
						avatarfieldError('image-display-failed');
					});

				}
				reader.readAsDataURL(fileElement.get(0).files[0]);
			})();
		});

		cropboxElement.on('newimage', function() {
			// New image has been selected

			var realWidth = cropboxElement.data('realWidth');
			var realHeight = cropboxElement.data('realHeight');
			var aspectRatio = realWidth/realHeight;
			cropboxElement.data('aspectRatio', aspectRatio);
		});





		interact('.avatarfield-cropbox-marker') // TODO: Specify Element
			.draggable({
				// enable inertial throwing
				inertia: true,
				// keep the element within the area of it's parent
				restrict: {
					restriction: "parent",
					endOnly: true,
					elementRect: { top: 0, left: 0, bottom: 1, right: 1 },
				},
				// enable autoScroll
				autoScroll: true,

				// call this function on every dragmove event
				onmove: dragMoveListener,
				// call this function on every dragend event
				onend: function (event) {
					var textEl = event.target.querySelector('p');

					textEl && (textEl.textContent =
						'moved a distance of '
						+ (Math.sqrt(event.dx * event.dx +
							event.dy * event.dy)|0) + 'px');
				}
			})
			.resizable({
				preserveAspectRatio: true,
				edges: { left: true, right: true, bottom: true, top: true },

				// keep the element within the area of it's parent
				restrict: {
					restriction: "parent",
				},

			})
			.on('resizemove', function (event) {
				var target = event.target,
						x = (parseFloat(target.getAttribute('data-x')) || 0),
						y = (parseFloat(target.getAttribute('data-y')) || 0);

				// update the element's style
				target.style.width  = event.rect.width + 'px';
				target.style.height = event.rect.height + 'px';

				// translate when resizing from top or left edges
				x += event.deltaRect.left;
				y += event.deltaRect.top;

				target.style.webkitTransform = target.style.transform =
						'translate(' + x + 'px,' + y + 'px)';

				target.setAttribute('data-x', x);
				target.setAttribute('data-y', y);
				// target.textContent = Math.round(event.rect.width) + '×' + Math.round(event.rect.height);

				// save data for cropping in hidden INPUT element
				var cropinfo = JSON.parse(cropinfoinputElement.val());
				cropinfo['width'] = event.rect.width/imageElement.width();
				cropinfo['height'] = event.rect.height/imageElement.height();
				cropinfoinputElement.val( JSON.stringify(cropinfo) );
			});

			function dragMoveListener (event) {
				var target = event.target,
						// keep the dragged position in the data-x/data-y attributes
						x = (parseFloat(target.getAttribute('data-x')) || 0) + event.dx,
						y = (parseFloat(target.getAttribute('data-y')) || 0) + event.dy;

				// translate the element
				target.style.webkitTransform =
				target.style.transform =
					'translate(' + x + 'px, ' + y + 'px)';

				// update the posiion attributes
				target.setAttribute('data-x', x);
				target.setAttribute('data-y', y);

				// save data for cropping in hidden INPUT element
				var cropinfo = JSON.parse(cropinfoinputElement.val());
				cropinfo['offset-x'] = x/imageElement.width();
				cropinfo['offset-y'] = y/imageElement.height();
				cropinfoinputElement.val( JSON.stringify(cropinfo) );
			}

			// this is used later in the resizing and gesture demos
			window.dragMoveListener = dragMoveListener;



	}); // each avatarfield
}); // document ready
