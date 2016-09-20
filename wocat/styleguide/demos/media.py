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
                    { 'href': 'http://bing.de/2', 'text': 'Media Library', 'active': True },
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


    'multiselect_language': {
        'name': 'Multiselect Language',
        'template': 'widgets/multiselect-oneblock.html',
        'context': {
            'id': 'multiselect-language',
            'label': 'Language',
            'selectallbutton': {'value':'all', 'label':'all Languages', 'checked': True },
            'options': [
                {'value':'alt', 'label':'English', 'checked':False},
                {'value':'neu', 'label':'Italian', 'checked':False},
                {'value':'neu', 'label':'German', 'checked':False},
                {'value':'von gestern', 'label':'French', 'checked':False},
            ],
        },
    },


    'multiselect_continent': {
        'name': 'Multiselect Continent',
        'template': 'widgets/multiselect-oneblock.html',
        'context': {
            'id': 'multiselect-language',
            'label': 'Continent',
            'selectallbutton': {'value':'all', 'label':'all Continents', 'checked': True },
            'options': [
                {'value':'alt', 'label':'Australia', 'checked':False},
                {'value':'neu', 'label':'Asia', 'checked':False},
                {'value':'neu', 'label':'Africa', 'checked':False},
                {'value':'von gestern', 'label':'America', 'checked':False},
                {'value':'von gestern', 'label':'Europe', 'checked':False},
            ],
        },
    },

}

