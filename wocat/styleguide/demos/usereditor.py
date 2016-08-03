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

    'usereditor': {
        'name': 'Heading 1',
        'template': 'widgets/heading1.html',
        'context': {
            'text': 'Register at Wocat',
        },
    },

    'avatar': {
        'name': 'Image',
        'template': 'widgets/image.html',
        'context': {
            'src': '/static/styleguide/test-images/studio-1by1.jpg',
        },
    },


    'multiselect': {
        'name': 'Multiselect with many values',
        'template': 'widgets/multiselect.html',
        'context': {
            'id': 'multiselect',
            'label': 'Experiences',
            'allowcustom': True,
            'options': [
                {'value':'alt', 'label':'Questionnaire on SLM Technologies (QT)', 'checked':False},
                {'value':'alt', 'label':'Questionnaire on SLM Approaches (QA)', 'checked':True},
                {'value':'alt', 'label':'Questionnaire on Mapping (QM)', 'checked':False},
                {'value':'alt', 'label':'Watershed Management Module', 'checked':False},
                {'value':'alt', 'label':'Climate Change Adaptation Module', 'checked':False},
            ],
        },
    },

}

