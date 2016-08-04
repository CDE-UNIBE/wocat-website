# -*- coding: utf-8 -*-

data = {


    'header': {
        'name': 'Header first level in home demo',
        'template': 'widgets/header.html',
        'context': {
            'id': '1',
            'toplinks': [
                { 'href': 'http://google.de/1', 'text': '<i class="fa fa-facebook" aria-hidden="true"></i>', },
                { 'href': 'http://bing.de/2', 'text': '<i class="fa fa-youtube" aria-hidden="true"></i>', },
                { 'href': 'http://bing.de/3', 'text': '<i class="fa fa-twitter" aria-hidden="true"></i>', },
                { 'href': 'http://google.de/1', 'text': 'Get involved', },
                { 'href': 'http://bing.de/2', 'text': 'FAQ', },
                { 'href': 'http://bing.de/3', 'text': 'Glossary', },
                { 'href': 'http://bing.de/2', 'text': 'Login', },
                {
                    'dropdown': True,
                    'text': 'EN',
                    'links': [
                        { 'href': 'http://google.de/1', 'text': 'DE', },
                        { 'href': 'http://bing.de/2', 'text': 'FR' },
                    ]
                },
                { 'href': 'http://bing.de/2', 'text': '<i class="fa fa-search" aria-hidden="true"></i>', },
            ],
            'mainnav': {
                'depth': 1,

                'links1': [
                    { 'href': 'http://google.de/1', 'text': 'Navi' },
                    { 'href': 'http://google.de/1', 'text': 'Roboto Regular Condensed' },
                    { 'href': 'http://bing.de/2', 'text': '<i class="fa fa-search" aria-hidden="true"></i> Search', 'onlyxs': True, },
                ],
            },
        },
    },

    'heading1': {
        'name': 'Heading 1',
        'template': 'widgets/heading1.html',
        'context': {
            'text': 'Heading 1: Open Sans Light 36px',
        },
    },
    'heading2': {
        'name': 'Heading 1',
        'template': 'widgets/heading2.html',
        'context': {
            'text': 'Heading 2: Open Sans Light 26px',
        },
    },
    'heading3': {
        'name': 'Heading 1',
        'template': 'widgets/heading3.html',
        'context': {
            'text': 'Heading 3: Open Sans Light 22px',
        },
    },


    'button': {
        'name': 'Button',
        'template': 'widgets/read-more-link.html',
        'context': {
            'text': 'Details siehe Styleguide',
            'href': '../../',
            'button': True,
        },
    },
}

