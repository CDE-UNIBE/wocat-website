$(function() {
	$('.widget-carousel .carousel').carousel({interval: 5000});
});

$(function() {
	$('.widget-members-table').each(function() {
		var membersTable = $(this);

		function applyFilters() {
			var country = membersTable.find('.widget-members-table-countryselector').val();
			var expertise = membersTable.find('.widget-members-table-expertiseselector').val();
			var sort = membersTable.find('.widget-members-table-sortselector').val();
			var page = membersTable.data('page');
			var maxpagesize = membersTable.find('.widget-members-table-members').data('maxpagesize');

			// console.log('Filter Country:', country, 'Filter Expertise:', expertise, 'Sort by:', sort);


			// iterate members
			membersTable.find('.widget-members-table-members .widget-members-table-member').each(function() {
				var member = $(this);

				var memberName = $.trim(member.find('.widget-members-table-name').text());
				var memberCountry = $.trim(member.find('.widget-members-table-country').text());
				var memberOrganisation = $.trim(member.find('.widget-members-table-organisation .member-organisation').text());
				var memberExpertises = member.find('.widget-members-table-expertises .expertise').map(function() {
						return $.trim($(this).text());
					}).get();

				// console.log('Member Name:', memberName, 'Member Organisation:', memberOrganisation, 'Member Country:', memberCountry, 'Member Expertises:', memberExpertises);

				// Country and Expertise match selection?
				if ((country != 'all') && (country != memberCountry)) member.addClass('member-hidden');
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
					case 'organisation':
						// Organisation
						var valueA = $.trim($(a).find('.widget-members-table-organisation .member-organisation').text());
						var valueB = $.trim($(b).find('.widget-members-table-organisation .member-organisation').text());
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

		membersTable.find('.widget-members-table-countryselector, .widget-members-table-expertiseselector, .widget-members-table-sortselector').change(function() {
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


	});

});


$(function() {
	// Gibt es auf der Seite ein Affix?
	if (!$('#affix').length) return;

	// Deklaration von Variablen, die beim Scrollen gebraucht und meist nicht überschrieben werden.
	var doAffix;
	var state;
	var affixElement, affixTopStop, affixBottomStop, affixHeight;


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
		affixTopStop = $('#affix-wrapper').offset().top;
		affixBottomStop = $('#affix-bottom').offset().top;
		affixHeight = affixElement.height();
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
				affixElement.removeClass('affix-fixed').css({'top': 0, 'left': 0});
				state = 'top';
			}
			return;
		}


		if ((scrollTop + affixHeight) > affixBottomStop) {
			//console.log('We are below affix area.');
			if (state != 'bottom') {
				var topOffset = affixBottomStop - affixTopStop - affixHeight;
				affixElement.removeClass('affix-fixed').css({'top': topOffset, 'left': 0});
				state = 'bottom';
			}
			return;
		}

		// We are in affix area
		//console.log('We are in the affix area.');
		if (state != 'fixed') {
			var affixLeft = $('#affix-wrapper').offset().left;
			//console.log('affixLeft: ', affixLeft);

			affixElement.addClass('affix-fixed').css({'top': '0', 'left': affixLeft});
			state = 'fixed';
		}

	}
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



