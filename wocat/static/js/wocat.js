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
			console.log('Show page: ', page, 'Max members per page: ', maxpagesize, 'First member: ', firstMemberNumber, 'Number of pages available: ', numberOfPages);
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
			console.log(membersTable.find('.widget-members-table-members .widget-members-table-member:visible'));
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


