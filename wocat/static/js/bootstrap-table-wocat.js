function imgFormatter(value, row) {
    return (value) ? '<img src="' + value + '" class="table-logo">' : '';
}

function boolFormatter(value, row) {
    return (value) ? '<span class="glyphicon glyphicon-ok" aria-hidden="true"></span>' : '<span class="glyphicon glyphicon-remove" aria-hidden="true"></span>';
}

function nameFormatter(value, row) {
    if (row.external_url === "") {
        return value
    } else {
        return '<a href="' + row.external_url + '" target="_blank">' + value + '</a>'
    }
}

function memberNameFormatter(value, row) {
    return '<a href="' + row.url + '">' + value + '</a>'
}

function functionFormatter(value, row) {
    if (row.institution_url !== "") {
        var institution = '<a href="' + row.institution_url + '" target="_blank">' + row.institution_name + '</a>'
    } else {
        var institution = row.institution_name
    }
    if (row.position === "") {
        return institution
    } else {
        return institution + ((institution === "") ? "" : "<br>") + "<i>" + row.position + '</i>'
    }
}

function drfQueryParams(params) {
    /*
     Map query params to the default params of the django rest framework.
     */
    if ('filter' in params) {
        /*
         Filters are expected as query-params, not within the keyword
         'filter' - so put the 'filter' params to the querystring.
         */
        $.each(JSON.parse(params.filter), function (key, value) {
            if (key === 'country_name') key = 'country';
            params[key] = value;
            // The filters (select2) also set the search option (if no
            // other search input is available). This is probably not
            // desirable, so filters are removed from the search.
            if (params.search === value) params.search = $('.search > input').val();
        });
        delete params['filter'];
    }
    if (params.sort !== undefined) {
        /*
         Change keyword and use '-' for descending sort.
         */
        var sortFieldMapping = {
            'full_name': 'last_name'
        };
        Object.keys(sortFieldMapping).forEach(function (key) {
            params.sort = params.sort.replace(key, sortFieldMapping[key]);
        });
        params['ordering'] = (params.order === 'desc') ? '-' : '';
        params['ordering'] += params.sort;
        delete params['sort'];
    }
    return params
}

