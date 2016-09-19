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
                    { 'href': 'http://google.de/1', 'text': 'Wocat & SLM' },
                    { 'href': 'http://bing.de/2', 'text': 'SLM Database' },
                    { 'href': 'http://bing.de/3', 'text': 'Decision support', },
                    { 'href': 'http://bing.de/3', 'text': 'Projects & Countries', },
                    { 'href': 'http://bing.de/2', 'text': 'Media Library', },
                    { 'href': 'http://bing.de/2', 'text': 'News & Events' },
                    {
                        'dropdown': True,
                        'text': 'EN',
                        'onlyxs': True,
                        'links': [
                            { 'href': 'http://google.de/1', 'text': 'DE', },
                            { 'href': 'http://bing.de/2', 'text': 'FR' },
                        ]
                    },
                    { 'href': 'http://bing.de/2', 'text': '<i class="fa fa-search" aria-hidden="true"></i> Search', 'onlyxs': True, },
                ],
            },
        },
    },

    'userprofile': {
        'name': 'Heading 1',
        'template': 'widgets/heading1.html',
        'context': {
            'text': 'Amélie Häfliger',
        },
    },


    'avatar': {
        'name': 'Image',
        'template': 'widgets/image.html',
        'context': {
            'src': '/static/styleguide/test-images/studio-1by1.jpg',
        },
    },

    'editlink': {
        'name': 'Read more link – right align',
        'template': 'widgets/read-more-link.html',
        'context': {
            'text': 'edit profile',
            'fontawesome': 'pencil',
            'href': 'http://x',
        },
    },

    'teaser_country': {
        'name': 'Teaser for User search',
        'template': 'widgets/teaser.html',
        'context': {
            'description': '',
            'href': 'http://sinnwerkstatt.com',
            'lines': True,
            'title': 'Find more users from my country',
            'description': 'Die Mitglieder-Datenbank enthält alle Involvierten bei Wocat.',
            'readmorelink': {'text': 'search users'},
        },
    },
    'teaser_databases': {
        'name': 'Teaser for User search',
        'template': 'widgets/teaser.html',
        'context': {
            'description': '',
            'href': 'http://sinnwerkstatt.com',
            'lines': True,
            'title': 'Show user data in Qcat',
            'description': 'Dieser User hat Daten bei Qcat, der Übersicht der Wocat-Datenbanken.',
            'readmorelink': {'text': 'Qcat database'},
        },
    },


}

