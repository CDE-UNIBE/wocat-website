$(function() {
	// Stop annoying auto cycling
	$('.widget-carousel .carousel').carousel({interval: false});
});

$(function() {
	$('.js-language-switcher-link').on('click', function(e) {
		e.preventDefault();
		var lang = $(this).data('language');
		var form = $(this).closest('.js-language-switcher-container').find('form');
		var href = $(this).attr('href');
		if (href !== '' && href !== '#') {
			form.find('input[name="next"]').val(href);
		}
		form.find('input[name="language"]').val(lang);
		form.submit();
	});
});

$(function() {
	// Members Table
	$('.widget-members-table').each(function() {
		var membersTable = $(this);

		// Default order
		membersTable.data('sort', 'name');
		membersTable.data('order', 'asc');

		function applyFilters() {
			if (membersTable.find('.widget-members-table-countryselector').val() == "all") {
				var country = "all";
			} else {
				var country = membersTable.find('.widget-members-table-countryselector option:selected').text();
			}
			var expertise = membersTable.find('.widget-members-table-expertiseselector').val();
			var institution = membersTable.find('.widget-members-table-institutionselector').val();
			var sort = membersTable.data('sort');
			var order = membersTable.data('order');
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

				if (valueA < valueB)
					if (order == 'asc') {
						return -1;
					} else {
						return 1;
					}
				if (valueA > valueB)
				if (order == 'asc') {
					return 1;
				} else {
					return -1;
				}
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
			if ((membersTable.data('sort') == 'name') && (membersTable.data('order') == 'asc')) {
				membersTable.data('order', 'desc');
				membersTable.find('.widget-members-table-name-sortarrow i.fa-caret-down').hide();
				membersTable.find('.widget-members-table-name-sortarrow i.fa-caret-up').show();
			} else {
				membersTable.data('sort', 'name');
				membersTable.data('order', 'asc');
				membersTable.find('.widget-members-table-name-sortarrow i.fa-caret-down').show();
				membersTable.find('.widget-members-table-name-sortarrow i.fa-caret-up').hide();
			}
			membersTable.find('.widget-members-table-country-sortarrow i, .widget-members-table-institution-sortarrow i').hide();
			applyFilters();
		});
		membersTable.find('.widget-members-table-headline .widget-members-table-country').click(function(event) {
			if ((membersTable.data('sort') == 'country') && (membersTable.data('order') == 'asc')) {
				membersTable.data('order', 'desc');
				membersTable.find('.widget-members-table-country-sortarrow i.fa-caret-down').hide();
				membersTable.find('.widget-members-table-country-sortarrow i.fa-caret-up').show();
			} else {
				membersTable.data('sort', 'country');
				membersTable.data('order', 'asc');
				membersTable.find('.widget-members-table-country-sortarrow i.fa-caret-down').show();
				membersTable.find('.widget-members-table-country-sortarrow i.fa-caret-up').hide();
			}
			membersTable.find('.widget-members-table-name-sortarrow i, .widget-members-table-institution-sortarrow i').hide();
			applyFilters();
		});
		membersTable.find('.widget-members-table-headline .widget-members-table-institution').click(function(event) {
			if ((membersTable.data('sort') == 'institution') && (membersTable.data('order') == 'asc')) {
				membersTable.data('order', 'desc');
				membersTable.find('.widget-members-table-institution-sortarrow i.fa-caret-down').hide();
				membersTable.find('.widget-members-table-institution-sortarrow i.fa-caret-up').show();
			} else {
				membersTable.data('sort', 'institution');
				membersTable.data('order', 'asc');
				membersTable.find('.widget-members-table-institution-sortarrow i.fa-caret-down').show();
				membersTable.find('.widget-members-table-institution-sortarrow i.fa-caret-up').hide();
			}
			membersTable.find('.widget-members-table-name-sortarrow i, .widget-members-table-country-sortarrow i').hide();
			applyFilters();
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
		// Default order
		institutionsTable.data('sort', 'name');
		institutionsTable.data('order', 'asc');

		function applyFilters() {
			if (institutionsTable.find('.widget-institutions-table-countryselector').val() == "all") {
				var country = "all";
			} else {
				var country = institutionsTable.find('.widget-institutions-table-countryselector option:selected').text();
			}
			var sort = institutionsTable.data('sort');
			var order = institutionsTable.data('order');
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
				if (valueA < valueB)
					if (order == 'asc') {
						return -1;
					} else {
						return 1;
					}
				if (valueA > valueB)
				if (order == 'asc') {
					return 1;
				} else {
					return -1;
				}
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
			if ((institutionsTable.data('sort') == 'name') && (institutionsTable.data('order') == 'asc')) {
				institutionsTable.data('order', 'desc');
				institutionsTable.find('.widget-institutions-table-name-sortarrow i.fa-caret-down').hide();
				institutionsTable.find('.widget-institutions-table-name-sortarrow i.fa-caret-up').show();
			} else {
				institutionsTable.data('sort', 'name');
				institutionsTable.data('order', 'asc');
				institutionsTable.find('.widget-institutions-table-name-sortarrow i.fa-caret-down').show();
				institutionsTable.find('.widget-institutions-table-name-sortarrow i.fa-caret-up').hide();
			}
			institutionsTable.find('.widget-institutions-table-country-sortarrow i').hide();
			applyFilters();


		});
		institutionsTable.find('.widget-institutions-table-headline .widget-institutions-table-country').click(function(event) {
			if ((institutionsTable.data('sort') == 'country') && (institutionsTable.data('order') == 'asc')) {
				institutionsTable.data('order', 'desc');
				institutionsTable.find('.widget-institutions-table-country-sortarrow i.fa-caret-down').hide();
				institutionsTable.find('.widget-institutions-table-country-sortarrow i.fa-caret-up').show();
			} else {
				institutionsTable.data('sort', 'country');
				institutionsTable.data('order', 'asc');
				institutionsTable.find('.widget-institutions-table-country-sortarrow i.fa-caret-down').show();
				institutionsTable.find('.widget-institutions-table-country-sortarrow i.fa-caret-up').hide();
			}
			institutionsTable.find('.widget-institutions-table-name-sortarrow i').hide();
			applyFilters();
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
