# -*- coding: utf-8 -*-
# # Data for the styleguide context
#

data = {
    'header1': {
        'name': 'Header first level',
        'template': 'widgets/header.html',
        'context': {
            'id': '1',
            'toplinks': [
                { 'href': 'http://google.de/1', 'text': '<i class="fa fa-facebook" aria-hidden="true"></i>' },
                { 'href': 'http://bing.de/2', 'text': '<i class="fa fa-youtube" aria-hidden="true"></i>' },
                { 'href': 'http://bing.de/3', 'text': '<i class="fa fa-twitter" aria-hidden="true"></i>' },
                { 'href': 'http://google.de/1', 'text': 'Get involved' },
                { 'href': 'http://bing.de/2', 'text': 'FAQ' },
                { 'href': 'http://bing.de/3', 'text': 'Glossary', 'active': True, },
                { 'href': 'http://bing.de/2', 'text': 'Login' },
                {
                    'dropdown': True,
                    'text': 'EN',
                    'links': [
                        { 'href': 'http://google.de/1', 'text': 'DE', 'active': True, },
                        { 'href': 'http://bing.de/2', 'text': 'FR' },
                    ]
                },
                { 'href': 'http://bing.de/2', 'text': '<i class="fa fa-search" aria-hidden="true"></i>', },
            ],
            'mainnav': {
                'depth': 1,

                'links1': [
                    { 'href': 'http://google.de/1', 'text': 'Get involved' },
                    { 'href': 'http://bing.de/2', 'text': 'FAQ' },
                    { 'href': 'http://bing.de/3', 'text': 'Glossary', 'active': True, },
                    { 'href': 'http://bing.de/2', 'text': 'Login' },
                    {
                        'dropdown': True,
                        'text': 'Yolo',
                        'links': [
                            { 'href': 'http://google.de/1', 'text': 'Swag', 'active': True, },
                            { 'href': 'http://bing.de/2', 'text': 'More Swag' },
                        ],
                    },
                    {
                        'dropdown': True,
                        'text': 'EN',
                        'onlyxs': True,
                        'links': [
                            { 'href': 'http://google.de/1', 'text': 'DE', 'active': True, },
                            { 'href': 'http://bing.de/2', 'text': 'FR' },
                        ]
                    },
                    { 'href': 'http://bing.de/2', 'text': '<i class="fa fa-search" aria-hidden="true"></i> Search', 'onlyxs': True, },
                ],
                'links2': [
                ],
            },
        },
    },

    'header1_home': {
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
                    { 'href': 'http://bing.de/2', 'text': 'Global SLM Database' },
                    { 'href': 'http://bing.de/2', 'text': 'Page FKA Media Library' },
                    { 'href': 'http://bing.de/3', 'text': 'Decision support for SLM', },
                    { 'href': 'http://bing.de/3', 'text': 'Projects & Countries', },
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


    'header2': {
        'name': 'Header 2nd level',
        'template': 'widgets/header.html',
        'context': {
            'id': '2',
            'toplinks': [
                { 'href': 'http://google.de/1', 'text': '<i class="fa fa-facebook" aria-hidden="true"></i>' },
                { 'href': 'http://bing.de/2', 'text': '<i class="fa fa-youtube" aria-hidden="true"></i>' },
                { 'href': 'http://bing.de/3', 'text': '<i class="fa fa-twitter" aria-hidden="true"></i>' },
                { 'href': 'http://google.de/1', 'text': 'Get involved' },
                { 'href': 'http://bing.de/2', 'text': 'FAQ' },
                { 'href': 'http://bing.de/3', 'text': 'Glossary', 'active': True, },
                { 'href': 'http://bing.de/2', 'text': 'Login' },
                {
                    'dropdown': True,
                    'text': 'EN',
                    'links': [
                        { 'href': 'http://google.de/1', 'text': 'DE', 'active': True, },
                        { 'href': 'http://bing.de/2', 'text': 'FR' },
                    ]
                },
                { 'href': 'http://bing.de/2', 'text': '<i class="fa fa-search" aria-hidden="true"></i> Search' },
            ],
            'mainnav': {
                'depth': 2,
                'brand2': {
                    'src': '/static/styleguide/test-images/dog-1by1.jpg',
                    'name': 'Yolo-Projekt',
                    'href': 'zurück',
                },

                'links1': [
                ],
                'links2': [
                    { 'href': 'http://google.de/1', 'text': 'About' },
                    { 'href': 'http://bing.de/2', 'text': 'Using the framework' },
                    { 'href': 'http://bing.de/3', 'text': 'Countries', 'active': True, },
                    { 'href': 'http://bing.de/2', 'text': 'News and Events' },
                    {
                        'dropdown': True,
                        'text': 'Yolo',
                        'links': [
                            { 'href': 'http://google.de/1', 'text': 'News', 'active': True, },
                            { 'href': 'http://bing.de/2', 'text': 'Events' },
                        ],
                    },
                    {
                        'dropdown': True,
                        'text': 'EN',
                        'onlyxs': True,
                        'links': [
                            { 'href': 'http://google.de/1', 'text': 'DE', 'active': True, },
                            { 'href': 'http://bing.de/2', 'text': 'FR' },
                        ]
                    },
                    { 'href': 'http://bing.de/2', 'text': '<i class="fa fa-search" aria-hidden="true"></i> Search', 'onlyxs': True, },
                ],
            },
        },
    },
    'header2_project': {
        'name': 'Header 2nd level Project',
        'template': 'widgets/header.html',
        'context': {
            'id': '2',
            'toplinks': [
                { 'href': 'http://google.de/1', 'text': '<i class="fa fa-facebook" aria-hidden="true"></i>' },
                { 'href': 'http://bing.de/2', 'text': '<i class="fa fa-youtube" aria-hidden="true"></i>' },
                { 'href': 'http://bing.de/3', 'text': '<i class="fa fa-twitter" aria-hidden="true"></i>' },
                { 'href': 'http://google.de/1', 'text': 'Get involved' },
                { 'href': 'http://bing.de/2', 'text': 'FAQ' },
                { 'href': 'http://bing.de/3', 'text': 'Glossary', },
                { 'href': 'http://bing.de/2', 'text': 'Login' },
                {
                    'dropdown': True,
                    'text': 'EN',
                    'links': [
                        { 'href': 'http://google.de/1', 'text': 'DE', 'active': True, },
                        { 'href': 'http://bing.de/2', 'text': 'FR' },
                    ]
                },
                { 'href': 'http://bing.de/2', 'text': '<i class="fa fa-search" aria-hidden="true"></i> Search' },
            ],
            'mainnav': {
                'depth': 2,
                'brand2': {
                    'name': 'DS-SLM',
                    'href': 'zurück',
                },

                'links1': [
                ],
                'links2': [
                    { 'href': 'http://google.de/1', 'text': 'About' },
                    { 'href': 'http://bing.de/2', 'text': 'Using the framework' },
                    { 'href': 'http://bing.de/3', 'text': 'Countries', },
                    { 'href': 'http://bing.de/2', 'text': 'News and Events' },
                    {
                        'dropdown': True,
                        'text': 'EN',
                        'onlyxs': True,
                        'links': [
                            { 'href': 'http://google.de/1', 'text': 'DE', 'active': True, },
                            { 'href': 'http://bing.de/2', 'text': 'FR' },
                        ]
                    },
                    { 'href': 'http://bing.de/2', 'text': '<i class="fa fa-search" aria-hidden="true"></i> Search', 'onlyxs': True, },
                ],
            },
        },
    },

    'carousel': {
        'name': 'Carousel',
        'template': 'widgets/carousel.html',
        'context': {
            'id': 1,
            'items': [
                { 'src': '/static/styleguide/test-images/header8-3by1.jpg' },
                { 'src': '/static/styleguide/test-images/header9-3by1.jpg' },
                { 'src': '/static/styleguide/test-images/header10-3by1.jpg' },
                { 'src': '/static/styleguide/test-images/header11-3by1.jpg' },
                { 'src': '/static/styleguide/test-images/header12-3by1.jpg' },
                { 'src': '/static/styleguide/test-images/header13-3by1.jpg' },
                { 'src': '/static/styleguide/test-images/header14-3by1.jpg' },
                { 'src': '/static/styleguide/test-images/header15-3by1.jpg' },
                { 'src': '/static/styleguide/test-images/header16-3by1.jpg' },
                { 'src': '/static/styleguide/test-images/header1-3by1.jpg' },
                { 'src': '/static/styleguide/test-images/header2-3by1.jpg' },
                { 'src': '/static/styleguide/test-images/header3-3by1.jpg' },
                { 'src': '/static/styleguide/test-images/header4-3by1.jpg' },
                { 'src': '/static/styleguide/test-images/header5-3by1.jpg' },
                { 'src': '/static/styleguide/test-images/header6-3by1.jpg' },
                { 'src': '/static/styleguide/test-images/header7-3by1.jpg' },
            ],
        },
    },


    'carousel_ugly': {
        'name': 'Carousel with ugly images',
        'template': 'widgets/carousel.html',
        'context': {
            'id': 2,
            'items': [
                { 'src': '/static/styleguide/test-images/header1.jpg' },
                { 'src': '/static/styleguide/test-images/small.jpg' },
            ],
        },
    },


    'carousel_widgetchooser_two': {
        'name': 'Carousel Widgetchooser with two images',
        'template': 'widgets/carousel-widgetchooser.html',
        'context': {
            'id': 'wc2',
            'items': [
                { 'src': '/static/styleguide/test-images/header2-3by1.jpg' },
                { 'src': '/static/styleguide/test-images/header1-3by1.jpg' },
            ],
        },
    },
    'carousel_widgetchooser_one': {
        'name': 'Carousel Widgetchooser with one image',
        'template': 'widgets/carousel-widgetchooser.html',
        'context': {
            'id': 'wc1',
            'items': [
                { 'src': '/static/styleguide/test-images/header3-3by1.jpg' },
            ],
        },
    },
    'carousel_widgetchooser_zero': {
        'name': 'Carousel Widgetchooser with no images',
        'template': 'widgets/carousel-widgetchooser.html',
        'context': {
            'id': 'wc0',
            'items': [
            ],
        },
    },


    'heading1': {
        'name': 'Heading 1',
        'template': 'widgets/heading1.html',
        'context': {
            'text': 'Besuch des Bürgermeisters',
        },
    },
    'heading2': {
        'name': 'Heading 2',
        'template': 'widgets/heading2.html',
        'context': {
            'text': 'Die Fotografie von Geistern',
        },
    },
    'heading2_b': {
        'name': 'B',
        'template': 'widgets/heading2.html',
        'context': {
            'text': 'B',
        },
    },
    'heading4': {
        'name': 'Heading 4',
        'template': 'widgets/heading4.html',
        'context': {
            'text': 'Consortium Partners',
        },
    },
    'heading4_link': {
        'name': 'Heading 4',
        'template': 'widgets/heading4.html',
        'context': {
            'text': 'Consortium Partners',
            'href': 'http://google.de',
        },
    },
    'heading3_news': {
        'name': 'Heading 3 News',
        'template': 'widgets/heading3.html',
        'context': {
            'text': 'News',
        },
    },
    'heading3_media': {
        'name': 'Heading 3 Media',
        'template': 'widgets/heading3.html',
        'context': {
            'text': 'Media',
        },
    },
    'heading2_countries': {
        'name': 'Heading 2 Countries',
        'template': 'widgets/heading2.html',
        'context': {
            'text': 'Countries',
        },
    },
    'heading2_projects': {
        'name': 'Heading 2 News',
        'template': 'widgets/heading2.html',
        'context': {
            'text': 'Projects',
        },
    },
    'heading2_regions': {
        'name': 'Heading 2 News',
        'template': 'widgets/heading2.html',
        'context': {
            'text': 'Regions',
        },
    },
    'heading2_link': {
        'name': 'Heading 2 with link',
        'template': 'widgets/heading2.html',
        'context': {
            'text': 'Eine Überschrift mit Link',
            'href': 'http://x',
        },
    },
    'heading3': {
        'name': 'Heading 3',
        'template': 'widgets/heading3.html',
        'context': {
            'text': 'Die Fotografie von Geistern',
        },
    },
    'heading3_link': {
        'name': 'Heading 3 with link',
        'template': 'widgets/heading3.html',
        'context': {
            'text': 'Eine Überschrift mit Link',
            'href': 'http://x',
        },
    },


    'teaser_noimg': {
        'name': 'Teaser with no image',
        'template': 'widgets/teaser.html',
        'context': {
            'href': 'http://sinnwerkstatt.com',
            'date': '24. April 2016',
            'title': 'Lorem Titel-Ipsum vom Dolor und Amet auch',
            'author': 'Tobias Kauer Jr.',
            'description': 'Es gibt im Moment17 in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
            'readmorelink': {
                'text': 'read more',
            },
        },
    },
    'teaser_noimg_external': {
        'name': 'Teaser with external link',
        'template': 'widgets/teaser.html',
        'context': {
            'href': 'http://sinnwerkstatt.com',
            'date': '24. April 2016',
            'title': 'Lorem Titel-Ipsum vom Dolor und Amet auch',
            'external': True,
            'author': 'Tobias Kauer Jr.',
            'description': 'Es gibt im Moment17b in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
            'readmorelink': {
                'text': 'read more',
            },
        },
    },
    'teaser_kenya': {
        'name': 'Teaser with no image',
        'template': 'widgets/teaser.html',
        'context': {
            'href': 'http://sinnwerkstatt.com',
            'title': 'Kenya',
            'flag_iso_3166_1_alpha_3': 'ken',
            'description': ' Ein paar Zahlen zu Algerien: Lala und Blubblub. ',
            'readmorelink': {
                'text': 'to the country',
            },
        },
    },
    'teaser_nigeria': {
        'name': 'Teaser with no image',
        'template': 'widgets/teaser.html',
        'context': {
            'href': 'http://sinnwerkstatt.com',
            'title': 'Nigeria',
            'flag_iso_3166_1_alpha_3': 'nga',
            'description': ' Ein paar Zahlen zu Algerien: Lala und Blubblub. ',
            'readmorelink': {
                'text': 'to the country',
            },
        },
    },
    'teaser_home_globalissues_image': {
        'name': 'Home Global Issues Image',
        'template': 'widgets/image.html',
        'context': {
            'src': '/static/styleguide/test-images/ziegen-4by3.jpg',
        },
    },
    'teaser_home_globalissues': {
        'name': 'Teaser with no image',
        'template': 'widgets/overlay-teaser.html',
        'context': {
            'description': 'Climate Change, Disaster Risk, Food Security, Sustainable Development Goals.',
            'title': 'Global Issues',
            'flapmd': True,
            'links': [
                {'href': 'http://google.de', 'text': 'learn more'},
            ],
            'style': 'box',
        },
    },
    'teaser_lines': {
        'name': 'Teaser with lines',
        'template': 'widgets/teaser.html',
        'context': {
            'href': 'http://sinnwerkstatt.com',
            'title': 'Lorem Titel-Ipsum vom Dolor und Amet auch',
            'lines': True,
            'description': 'Es gibt im Moment18 in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
            'readmorelink': {
                'text': 'read more',
            },
        },
    },
    'teaser_lines_leftimage': {
        'name': 'Teaser with lines and left image',
        'template': 'widgets/teaser.html',
        'context': {
            'href': 'http://sinnwerkstatt.com',
            'title': 'Lorem Titel-Ipsum vom Dolor und Amet auch',
            'lines': True,
            'imgpos': 'left',
            'imgsrc': '/static/styleguide/test-images/header4.jpg',
            'description': 'Es gibt im Moment19 in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
            'readmorelink': {
                'text': 'read more',
            },
        },
    },
    'teaser_lines_rightimage': {
        'name': 'Teaser with lines and right image',
        'template': 'widgets/teaser.html',
        'context': {
            'href': 'http://sinnwerkstatt.com',
            'title': 'Lorem Titel-Ipsum vom Dolor und Amet auch',
            'lines': True,
            'imgpos': 'right',
            'imgsrc': '/static/styleguide/test-images/header4.jpg',
            'description': 'Es gibt im Moment20 in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
            'readmorelink': {
                'text': 'read more',
            },
        },
    },
    'teaser_lines_rightimage_circle': {
        'name': 'Teaser with lines and circular right image',
        'template': 'widgets/teaser.html',
        'context': {
            'href': 'http://sinnwerkstatt.com',
            'title': 'Lorem Titel-Ipsum vom Dolor und Amet auch',
            'lines': True,
            'imgpos': 'right',
            'imgcircle': True,
            'imgsrc': '/static/styleguide/test-images/studio-1by1.jpg',
            'description': 'Es gibt im Moment20 in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
            'readmorelink': {
                'text': 'read more',
            },
        },
    },
    'teaser_lines_large_leftimage': {
        'name': 'Teaser with lines and large left image and external link',
        'template': 'widgets/teaser.html',
        'context': {
            'href': 'http://sinnwerkstatt.com',
            'external': True,
            'title': 'Lorem Titel-Ipsum vom Dolor und Amet auch',
            'lines': True,
            'imgpos': 'left',
            'largeimg': True,
            'imgsrc': '/static/styleguide/test-images/global-issues-3by1.jpg',
            'description': 'Es gibt im Moment21 in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
            'readmorelink': {
                'text': 'read more',
            },
        },
    },
    'teaser_lines_large_rightimage': {
        'name': 'Teaser with lines and large right image',
        'template': 'widgets/teaser.html',
        'context': {
            'href': 'http://sinnwerkstatt.com',
            'title': 'Lorem Titel-Ipsum vom Dolor und Amet auch',
            'lines': True,
            'imgpos': 'right',
            'largeimg': True,
            'imgsrc': '/static/styleguide/test-images/header1-3by1.jpg',
            'description': 'Es gibt im Moment22 in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
            'readmorelink': {
                'text': 'read more',
            },
        },
    },
    'teaser_lines_topimage': {
        'name': 'Teaser with lines and top image',
        'template': 'widgets/teaser.html',
        'context': {
            'href': 'http://sinnwerkstatt.com',
            'title': 'Lorem Titel-Ipsum vom Dolor und Amet auch extra langer Titel, der nie auf eine Zeile passt, was total oft zu Umbrüchen führt.',
            'lines': True,
            'imgpos': 'top',
            'imgsrc': '/static/styleguide/test-images/header4.jpg',
            'description': 'Es gibt im Moment23 in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
            'readmorelink': {
                'text': 'read more',
            },
        },
    },
    'teaser_lines_home_news': {
        'name': 'Teaser with lines and top image',
        'template': 'widgets/teaser.html',
        'context': {
            'href': 'http://sinnwerkstatt.com',
            'title': 'Building resilience',
            'imgpos': 'right',
            'bottomline': True,
            'date': '24. April 2016',
            'imgsrc': '/static/styleguide/test-images/header4.jpg',
            'description': 'Es gibt im Moment in diese Mannschaft…',
            'readmorelink': {
                'text': 'read more',
            },
        },
    },
    'teaser_lines_home_news_long': {
        'name': 'Teaser with lines and top image',
        'template': 'widgets/teaser.html',
        'context': {
            'href': 'http://sinnwerkstatt.com',
            'title': 'See what happens if we write a long article about building resilience!',
            'imgpos': 'right',
            'bottomline': True,
            'date': '24. April 2016',
            'imgsrc': '/static/styleguide/test-images/header3.jpg',
            'description': 'Es gibt im Moment in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind…',
            'readmorelink': {
                'text': 'read more',
            },
        },
    },

    'teaser_topimg': {
        'name': 'Teaser with top image',
        'template': 'widgets/teaser.html',
        'context': {
            'imgpos': 'top',
            'imgsrc': '/static/styleguide/test-images/header4.jpg',
            'href': 'http://sinnwerkstatt.com',
            'date': '24. April 2016',
            'title': 'Lorem Titel-Ipsum vom Dolor und Amet auch',
            'description': 'Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt.',
            'readmorelink': {
                'text': 'read more',
            },
        },
    },
    'teaser_leftimg': {
        'name': 'Teaser with left image',
        'template': 'widgets/teaser.html',
        'context': {
            'imgpos': 'left',
            'imgsrc': '/static/styleguide/test-images/header4.jpg',
            'href': 'http://sinnwerkstatt.com',
            'date': '24. April 2016',
            'title': 'Lorem Titel-Ipsum vom Dolor und Amet auch',
            'description': 'Es gibt im Moment6 in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
            'readmorelink': {
                'text': 'read more',
            },
        },
    },
    'teaser_super_leftimg': {
        'name': 'Super Teaser with left image (just concept!)',
        'template': 'widgets/teaser-super.html',
        'context': {
            'backgroundimagesrc': '/static/styleguide/test-images/header3.jpg',
            'imgpos': 'left',
            'imgsrc': '/static/styleguide/test-images/header4.jpg',
            'href': 'http://sinnwerkstatt.com',
            'date': '24. April 2016',
            'title': 'Lorem Titel-Ipsum vom Dolor und Amet auch',
            'description': 'Es gibt im Moment5 in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
            'readmorelink': {
                'text': 'read more',
            },
        },
    },
    'teaser_super_leftimg_nobackground': {
        'name': 'Super Teaser with left image without background (just concept!)',
        'template': 'widgets/teaser-super.html',
        'context': {
            'imgpos': 'left',
            'imgsrc': '/static/styleguide/test-images/header4.jpg',
            'href': 'http://sinnwerkstatt.com',
            'date': '24. April 2016',
            'title': 'Lorem Titel-Ipsum vom Dolor und Amet auch',
            'description': 'Es gibt im Moment4 in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
            'readmorebutton': {
                'text': 'read more',
            },
        },
    },
    'teaser_super_narrow': {
        'name': 'Super Teaser Narrow (just concept!)',
        'template': 'widgets/teaser-super-narrow.html',
        'context': {
            'backgroundimagesrc': '/static/styleguide/test-images/header3.jpg',
            'href': 'http://sinnwerkstatt.com',
            'date': '24. April 2016',
            'title': 'Lorem Titel-Ipsum vom Dolor und Amet auch',
            'description': 'Es gibt im Moment2 in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
            'readmorebutton': {
                'text': 'read more',
            },
        },
    },
    'teaser_rightimg': {
        'name': 'Teaser with right image',
        'template': 'widgets/teaser.html',
        'context': {
            'imgpos': 'right',
            'imgsrc': '/static/styleguide/test-images/header4.jpg',
            'href': 'http://sinnwerkstatt.com',
            'date': '24. April 2016',
            'title': 'Lorem Titel-Ipsum vom Dolor und Amet auch',
            'description': 'Es gibt im Moment1 in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
            'readmorelink': {
                'text': 'read more',
            },
        },
    },

    'teaser_rightimg': {
        'name': 'Teaser with right image and Bottomline',
        'template': 'widgets/teaser.html',
        'context': {
            'imgpos': 'right',
            'imgsrc': '/static/styleguide/test-images/header4.jpg',
            'href': 'http://sinnwerkstatt.com',
            'date': '24. April 2016',
            'bottomline': True,
            'title': 'Lorem Titel-Ipsum vom Dolor und Amet auch',
            'description': 'Es gibt im Moment3 in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
            'readmorelink': {
                'text': 'read more',
            },
        },
    },

    'page_lead_overlay': {
        'name': 'Page Lead Overlay',
        'template': 'widgets/page-lead-overlay.html',
        'context': {
            'heading': 'Styleguide',
            'lead': 'Es gibt im Moment7 in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen.',
        },
    },
    'page_lead_overlay_small': {
        'name': 'Page Lead Overlay Small',
        'template': 'widgets/page-lead-overlay.html',
        'context': {
            'small': True,
            'heading': 'Small Overlay',
            'lead': 'Es gibt im Moment8 in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen.',
        },
    },

    'page_lead_overlay_home': {
        'name': 'Page Lead Overlay',
        'template': 'widgets/overlay-teaser.html',
        'context': {
            'description': 'WOCAT (World Overview of Conservation Approaches and Technologies) is an established global network which supports innovation and decision-making processes in Sustainable Land Management (SLM).',
            'title': 'Wocat',
            'links': [
                {'href': 'http://google.de', 'text': 'Discover Wocat'},
            ],
            'style': 'largebox',
        },
    },


    'page_lead_overlay_project': {
        'name': 'Page Lead Overlay',
        'template': 'widgets/page-lead-overlay.html',
        'context': {
            'heading': 'Decision support for mainstreaming and scaling out SLM',
            'lead': 'The DS-SLM project contributes to arresting and reversing current global trends in land degradation by supporting 15 countries in mainstreaming and scaling out SLM.',
        },
    },
    'page_lead_overlay_projectcountries': {
        'name': 'Page Lead Overlay',
        'template': 'widgets/page-lead-overlay.html',
        'context': {
            'heading': 'Projects and Countries',
            'lead': 'Es gibt im Moment10 in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen.',
        },
    },
    'page_lead_overlay_noimage': {
        'name': 'Page Lead Overlay no Image',
        'template': 'widgets/page-lead-overlay.html',
        'context': {
            'noimage': True,
            'heading': 'Page Head without image overlay',
            'lead': 'Es gibt im Moment11 in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen.',
        },
    },

    'page_lead_overlay_noimage_alternative': {
        'name': 'Page Lead Overlay no Image Alternative',
        'template': 'widgets/page-lead-overlay.html',
        'context': {
            'noimage': True,
            'heading': 'Page Head without image overlay',
            'heading_iconsrc': '/static/styleguide/test-images/dog-1by1.jpg',
            'content': '<div class="row"><div class="col-sm-6">Linke Zahl: <strong>5m</strong></div><div class="col-sm-6">Rechte Zahl: <strong>100km</strong></div></div>',
        },
    },

    'overlay_teaser': {
        'name': 'Overlay Teaser – Box',
        'template': 'widgets/overlay-teaser.html',
        'context': {
            'style': 'box',
            'title': 'Overlay Teaser Box',
            'description': 'Es gibt im Moment12 in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen.',
            'links': [
                { 'href': 'http://google.de', 'text': 'Google', },
                { 'href': 'http://facebook.de', 'text': 'Facebook', },
                { 'href': 'http://bing.de', 'text': 'extern Bing', 'external': True },
            ],
        },
    },

    'overlay_teaser_widgetchooser': {
        'name': 'Overlay Teaser – Widgetchooser',
        'template': 'widgets/overlay-teaser-widgetchooser.html',
        'context': {
            'imgsrc': '/static/styleguide/test-images/surfing.jpg',
            'style': 'box',
            'title': 'Overlay Teaser Box',
            'description': 'Es gibt im Moment13 in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen.',
            'links': [
                { 'href': 'http://google.de', 'text': 'Google', },
                { 'href': 'http://facebook.de', 'text': 'Facebook', },
                { 'href': 'http://bing.de', 'text': 'extern Bing', 'external': True },
            ],
        },
    },
    'overlay_teaser_widgetchooser_flapmd': {
        'name': 'Overlay Teaser – Widgetchooser – Flap box at MD screen size',
        'template': 'widgets/overlay-teaser-widgetchooser.html',
        'context': {
            'imgsrc': '/static/styleguide/test-images/surfing.jpg',
            'style': 'box',
            'title': 'Overlay Teaser Box',
            'flapmd': True,
            'description': 'Es gibt im Moment13b in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen.',
            'links': [
                { 'href': 'http://google.de', 'text': 'Google', },
                { 'href': 'http://facebook.de', 'text': 'Facebook', },
                { 'href': 'http://bing.de', 'text': 'extern Bing', 'external': True },
            ],
        },
    },
    'overlay_teaser_widgetchooser_map': {
        'name': 'Overlay Teaser – Widgetchooser Map',
        'template': 'widgets/overlay-teaser-widgetchooser.html',
        'context': {
            'size': 'large',
            'countries': [
                { 'iso_3166_1_alpha_3': 'LSO', 'popup': '<a href="x">Lesotho</a>', },
                { 'iso_3166_1_alpha_3': 'MAR', 'popup': '<a href="x">Morocco</a>', },
                { 'iso_3166_1_alpha_3': 'NGA', 'popup': '<a href="x">Nigeria</a>', },
                { 'iso_3166_1_alpha_3': 'TUN', 'popup': '<a href="x">Tunisia</a>', },

                { 'iso_3166_1_alpha_3': 'BGD', 'popup': '<a href="x">Bangladesh</a>', },
                { 'iso_3166_1_alpha_3': 'CHN', 'popup': '<a href="x">China</a>', },
                { 'iso_3166_1_alpha_3': 'PHL', 'popup': '<a href="x">Philippines</a>', },
                { 'iso_3166_1_alpha_3': 'THA', 'popup': '<a href="x">Thailand</a>', },

                { 'iso_3166_1_alpha_3': 'BIH', 'popup': '<a href="x">Bosnia & Herzegovina</a>', },
                { 'iso_3166_1_alpha_3': 'TUR', 'popup': '<a href="x">Turkey</a>', },
                { 'iso_3166_1_alpha_3': 'UZB', 'popup': '<a href="x">Uzbekistan</a>', },

                { 'iso_3166_1_alpha_3': 'ARG', 'popup': '<a href="x">Argentinia</a>', },
                { 'iso_3166_1_alpha_3': 'COL', 'popup': '<a href="x">Colombia</a>', },
                { 'iso_3166_1_alpha_3': 'ECU', 'popup': '<a href="x">Equador</a>', },
                { 'iso_3166_1_alpha_3': 'PAN', 'popup': '<a href="x">Panama</a>', },
            ],
            'style': 'box',
            'title': 'Overlay Teaser Box',
            'description': 'Es gibt im Moment14 in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen.',
            'links': [
                { 'href': 'http://google.de', 'text': 'Google', },
                { 'href': 'http://facebook.de', 'text': 'Facebook', },
                { 'href': 'http://bing.de', 'text': 'extern Bing', 'external': True },
            ],
        },
    },
    'overlay_teaser_bottom': {
        'name': 'Overlay Teaser – Bottom',
        'template': 'widgets/overlay-teaser.html',
        'context': {
            'style': 'bottom',
            'title': 'Overlay Teaser Bottom',
            'description': 'Es gibt im Moment15 in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen.',
            'links': [
                { 'href': 'http://google.de', 'text': 'Google', },
                { 'href': 'http://facebook.de', 'text': 'Facebook', },
                { 'href': 'http://bing.de', 'text': 'Bing', },
            ],
        },
    },
    'overlay_teaser_home_map': {
        'name': 'Overlay Teaser Home Map',
        'template': 'widgets/overlay-teaser.html',
        'context': {
            'style': 'box',
            'title': 'Projects and Countries',
            'description': 'Es gibt im Moment16 in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen.',
            'links': [
                { 'href': 'http://google.de', 'text': 'explore Projects and Countries', },
            ],
        },
    },
    'overlay_teaser_home_database': {
        'name': 'Overlay Teaser Home Database',
        'template': 'widgets/overlay-teaser.html',
        'context': {
            'style': 'box',
            'title': 'Global Database on Sustainable Land Management',
            'description': 'The Wocat database on SLM contains a vast range of good practices from all over the world.',
            'links': [
                { 'href': 'http://google.de', 'text': 'About the SLM Database', },
            ],
        },
    },

    'avatarfield': {
        'name': 'Avatar Field',
        'template': 'widgets/avatarfield.html',
        'context': {
            'id': 'avatarfield',
            'label': 'Avatar',
        },
    },
    'nullboolean': {
        'name': 'Nullboolean',
        'template': 'widgets/nullboolean.html',
        'context': {
            'id': 'nullboolean',
            'label': 'Hollywood hat alle Apollo-Missionen auf dem Mond gedreht',
            'value': True,
            'nullable': True,
        },
    },
    'nullboolean_error': {
        'name': 'Nullboolean with Error',
        'template': 'widgets/nullboolean.html',
        'context': {
            'id': 'nullboolean2',
            'label': 'Hollywood hat alle Apollo-Missionen auf dem Mond gedreht',
            'value': False,
            'error': True,
            'help': 'Ja nö oder egal?',
            'nullable': True,
        },
    },
    'nullboolean_nonull': {
        'name': 'Nullboolean not Nullable',
        'template': 'widgets/nullboolean.html',
        'context': {
            'id': 'nullboolean3',
            'label': 'Hollywood hat alle Apollo-Missionen auf dem Mond gedreht',
            'value': False,
        },
    },

    'multiselect': {
        'name': 'Multiselect',
        'template': 'widgets/multiselect.html',
        'context': {
            'id': 'multiselect',
            'label': 'Was zählt zu deiner Expertise?',
            'allowcustom': True,
            'options': [
                {'value':'alt', 'label':'Alt', 'checked':True},
                {'value':'neu', 'label':'Neu', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern', 'checked':False},
                {'value':'neu 2016', 'label':'neu 2016', 'checked':False},
            ],
        },
    },
    'multiselect_full': {
        'name': 'Multiselect with many values',
        'template': 'widgets/multiselect.html',
        'context': {
            'id': 'multiselect',
            'label': 'In welchen Ländern ist dein Projekt aktiv?',
            'allowcustom': True,
            'options': [
                {'value':'alt', 'label':'Alt1', 'checked':True},
                {'value':'alt', 'label':'Alt2', 'checked':True},
                {'value':'alt', 'label':'Alt3', 'checked':True},
                {'value':'alt', 'label':'Alt4', 'checked':True},
                {'value':'alt', 'label':'Alt5', 'checked':True},
                {'value':'alt', 'label':'Alt6', 'checked':True},
                {'value':'alt', 'label':'Alt7', 'checked':True},
                {'value':'alt', 'label':'Alt8', 'checked':True},
                {'value':'alt', 'label':'Alt9', 'checked':True},
                {'value':'alt', 'label':'Alt10', 'checked':True},
                {'value':'alt', 'label':'Alt11', 'checked':True},
                {'value':'alt', 'label':'Alt12', 'checked':True},
                {'value':'alt', 'label':'Alt13', 'checked':True},
                {'value':'alt', 'label':'Alt14', 'checked':True},
                {'value':'alt', 'label':'Alt15', 'checked':True},
                {'value':'alt', 'label':'Alt1', 'checked':True},
                {'value':'alt', 'label':'Alt2', 'checked':True},
                {'value':'alt', 'label':'Alt3', 'checked':True},
                {'value':'alt', 'label':'Alt4', 'checked':True},
                {'value':'alt', 'label':'Alt5', 'checked':True},
                {'value':'alt', 'label':'Alt6', 'checked':True},
                {'value':'alt', 'label':'Alt7', 'checked':True},
                {'value':'alt', 'label':'Alt8', 'checked':True},
                {'value':'alt', 'label':'Alt9', 'checked':True},
                {'value':'alt', 'label':'Alt10', 'checked':True},
                {'value':'alt', 'label':'Alt11', 'checked':True},
                {'value':'alt', 'label':'Alt12', 'checked':True},
                {'value':'alt', 'label':'Alt13', 'checked':True},
                {'value':'alt', 'label':'Alt14', 'checked':True},
                {'value':'alt', 'label':'Alt15', 'checked':True},
                {'value':'neu', 'label':'Neu', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern1', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern2', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern3', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern4', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern5', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern6', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern7', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern8', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern9', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern10', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern11', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern12', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern13', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern14', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern15', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern16', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern17', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern18', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern19', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern20', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern21', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern22', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern23', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern24', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern25', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern26', 'checked':False},
                {'value':'neu 2016', 'label':'neu 2016', 'checked':False},
            ],
        },
    },
    'multiselect_oneblock': {
        'name': 'Multiselect Oneblock',
        'template': 'widgets/multiselect-oneblock.html',
        'context': {
            'id': 'multiselect-oneblock',
            'label': 'Welche Länder kennst du?',
            'options': [
                {'value':'alt', 'label':'Afghanistan', 'checked':True},
                {'value':'neu', 'label':'Chile', 'checked':False},
                {'value':'von gestern', 'label':'Ghana', 'checked':False},
                {'value':'neu 2016', 'label':'France', 'checked':False},
                {'value':'von gestern', 'label':'Ecuador', 'checked':False},
                {'value':'neu 2016', 'label':'Germany', 'checked':False},
                {'value':'von gestern', 'label':'England', 'checked':False},
                {'value':'neu 2016', 'label':'Catalunya', 'checked':False},
                {'value':'neu 2016', 'label':'Vatican', 'checked':False},
            ],
        },
    },
    'multiselect_oneblock_selectallbutton': {
        'name': 'Multiselect Oneblock Selectallbutton',
        'template': 'widgets/multiselect-oneblock.html',
        'context': {
            'id': 'multiselect-oneblock-countries',
            'label': 'Countries',
            'selectallbutton': {'value':'all', 'label':'all Countries', 'checked': True },
            'options': [
                {'value':'alt', 'label':'Afghanistan', 'checked':False},
                {'value':'neu', 'label':'Chile', 'checked':False},
                {'value':'von gestern', 'label':'Ghana', 'checked':False},
                {'value':'neu 2016', 'label':'France', 'checked':False},
                {'value':'von gestern', 'label':'Ecuador', 'checked':False},
                {'value':'neu 2016', 'label':'Germany', 'checked':False},
                {'value':'von gestern', 'label':'England', 'checked':False},
                {'value':'neu 2016', 'label':'Catalunya', 'checked':False},
                {'value':'neu 2016', 'label':'Vatican', 'checked':False},
                {'value':'alt', 'label':'Afghanistan', 'checked':False},
                {'value':'neu', 'label':'Chile', 'checked':False},
                {'value':'von gestern', 'label':'Ghana', 'checked':False},
                {'value':'neu 2016', 'label':'France', 'checked':False},
                {'value':'von gestern', 'label':'Ecuador', 'checked':False},
                {'value':'neu 2016', 'label':'Germany', 'checked':False},
                {'value':'von gestern', 'label':'England', 'checked':False},
                {'value':'neu 2016', 'label':'Catalunya', 'checked':False},
                {'value':'neu 2016', 'label':'Vatican', 'checked':False},
                {'value':'alt', 'label':'Afghanistan', 'checked':False},
                {'value':'neu', 'label':'Chile', 'checked':False},
                {'value':'von gestern', 'label':'Ghana', 'checked':False},
                {'value':'neu 2016', 'label':'France', 'checked':False},
                {'value':'von gestern', 'label':'Ecuador', 'checked':False},
                {'value':'neu 2016', 'label':'Germany', 'checked':False},
                {'value':'von gestern', 'label':'England', 'checked':False},
                {'value':'neu 2016', 'label':'Catalunya', 'checked':False},
                {'value':'neu 2016', 'label':'Vatican', 'checked':False},
            ],
        },
    },


    'singleselect': {
        'name': 'Singleselect',
        'template': 'widgets/multiselect.html',
        'context': {
            'id': 'singleselect',
            'label': 'Von wann ist dein Longboard?',
            'singleselect': True,
            'allowcustom': True,
            'options': [
                {'value':'alt', 'label':'Alt', 'checked':False},
                {'value':'neu', 'label':'Neu', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern', 'checked':False},
                {'value':'neu 2016', 'label':'neu 2016', 'checked':True},
            ],
        },
    },
    'singleselect_nullable': {
        'name': 'Singleselect with null option',
        'template': 'widgets/multiselect.html',
        'context': {
            'id': 'singleselect-null',
            'label': 'Von wann ist dein Longboard, wenn du eins hast?',
            'singleselect': True,
            'allowcustom': True,
            'nullable': True,
            'options': [
                {'value':'alt', 'label':'Alt', 'checked':False},
                {'value':'neu', 'label':'Neu', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern', 'checked':False},
                {'value':'neu 2016', 'label':'neu 2016', 'checked':True},
            ],
        },
    },
    'singleselect_error': {
        'name': 'Singleselect with error',
        'template': 'widgets/multiselect.html',
        'context': {
            'id': 'singleselect2',
            'label': 'Von wann ist dein Longboard?',
            'singleselect': True,
            'allowcustom': True,
            'options': [
                {'value':'alt', 'label':'Alt', 'checked':False},
                {'value':'neu', 'label':'Neu', 'checked':False},
                {'value':'von gestern', 'label':'Von gestern', 'checked':False},
                {'value':'neu 2016', 'label':'neu 2016', 'checked':True},
            ],
            'error': True,
            'help': 'Hier klickste was rein.'
        },
    },

    'dropzone': {
        'name': 'Dropzone',
        'template': 'widgets/dropzone.html',
        'context': {
            'apiurl': '/static/styleguide/js/dropzone-endpoint.html',
        },
    },


    'dsf_teaser': {
        'name': 'DSF Teaser',
        'template': 'widgets/dsf-teaser.html',
        'context': {
            'module1href': 'http://google.de/1',
            'module2href': 'http://google.de/2',
            'module3href': 'http://google.de/3',
            'module4href': 'http://google.de/4',
            'module5href': 'http://google.de/5',
            'module6href': 'http://google.de/6',
            'module7href': 'http://google.de/7',
        },
    },

    'columns_1_1': {
        'name': 'Columns 1:1',
        'template': 'widgets/columns-1-1.html',
        'context': {
            'left_column': '<h2 style="background-color: #eee;">Left Column</h2>',
            'right_column': '<h2 style="background-color: #eee;">Right Column</h2>',
        },
    },
    'columns_2_1': {
        'name': 'Columns 2:1',
        'template': 'widgets/columns-2-1.html',
        'context': {
            'left_column': '<h2 style="background-color: #eee;">Left Column</h2>',
            'right_column': '<h2 style="background-color: #eee;">Right Column</h2>',
        },
    },
    'columns_1_2': {
        'name': 'Columns 1:2',
        'template': 'widgets/columns-1-2.html',
        'context': {
            'left_column': '<h2 style="background-color: #eee;">Left Column</h2>',
            'right_column': '<h2 style="background-color: #eee;">Right Column</h2>',
        },
    },
    'columns_1_1_1': {
        'name': 'Columns 1:1:1',
        'template': 'widgets/columns-1-1-1.html',
        'context': {
            'left_column': '<h2 style="background-color: #eee;">Left Column</h2>',
            'middle_column': '<h2 style="background-color: #eee;">Middle Column</h2>',
            'right_column': '<h2 style="background-color: #eee;">Right Column</h2>',
        },
    },

    'horizontal_ruler' : {
        'name': 'Horizontal Ruler',
        'template': 'widgets/horizontal-ruler.html',
        'context': {
        },
    },

    'image': {
        'name': 'Image',
        'template': 'widgets/image.html',
        'context': {
            'src': '/static/styleguide/test-images/header2.jpg',
            'caption': 'This is the description of the image. This is the description of the image. This is the description of the image. This is the description of the image. This is the description of the image.',
            'href': 'http://xxx',
        },
    },
    'image_nocaption': {
        'name': 'Image',
        'template': 'widgets/image.html',
        'context': {
            'src': '/static/styleguide/test-images/header1.jpg',
        },
    },
    'image_logo': {
        'name': 'Image Logo',
        'template': 'widgets/image.html',
        'context': {
            'src': '/static/images/Wocat_Logo.svg',
            'href': 'http://x',
        },
    },

    'image_gallery': {
        'name': 'Image Gallery',
        'template': 'widgets/image-gallery.html',
        'context': {
            'cols': 4,
            'images': [
                {
                    'src': '/static/styleguide/test-images/header4.jpg',
                    'description': 'This is the description of the image. This is the description of the image.',
                    'href': 'http://xxx1',
                },
                {
                    'src': '/static/styleguide/test-images/header1.jpg',
                    'description': 'This is the description of the image. This is the description of the image.',
                },
                {
                    'src': '/static/styleguide/test-images/header3.jpg',
                    'href': 'http://yyy2',
                },
                {
                    'src': '/static/styleguide/test-images/header4.jpg',
                    'description': 'This is the description of the image. This is the description of the image.',
                    'href': 'http://xxx3',
                    'shrink': 1,
                },
                {
                    'src': '/static/styleguide/test-images/header1.jpg',
                    'description': 'This is the description of the image. This is the description of the image.',
                    'shrink': 2,
                },
                {
                    'src': '/static/styleguide/test-images/header3.jpg',
                    'href': 'http://yyy4',
                    'shrink': 1,
                },
            ],
        },
    },

    'image_gallery_verticalalign': {
        'name': 'Image Gallery Vertical Align',
        'template': 'widgets/image-gallery.html',
        'context': {
            'cols': 4,
            'verticalalign': True,
            'images': [
                {
                    'src': '/static/styleguide/test-images/dog-1by1.jpg',
                    'shrink': 2,
                    'href': 'http://xxx1',
                },
                {
                    'src': '/static/styleguide/test-images/header2-3by1.jpg',
                },
                {
                    'src': '/static/styleguide/test-images/surfing.jpg',
                    'shrink': 1,
                    'href': 'http://yyy2',
                },
                {
                    'src': '/static/styleguide/test-images/header4.jpg',
                    'href': 'http://xxx3',
                    'shrink': 1,
                },
                {
                    'src': '/static/styleguide/test-images/girls-1by1.jpg',
                    'shrink': 2,
                },
                {
                    'src': '/static/styleguide/test-images/header3.jpg',
                    'href': 'http://yyy4',
                    'shrink': 1,
                },
            ],
        },
    },


    'button': {
        'name': 'Button',
        'template': 'widgets/read-more-link.html',
        'context': {
            'text': 'Use the framework',
            'href': 'http://google.de',
            'button': True,
        },
    },
    'button_fontawesome': {
        'name': 'Button',
        'template': 'widgets/read-more-link.html',
        'context': {
            'text': 'Use the framework',
            'fontawesome': 'gears',
            'href': 'http://google.de',
            'button': True,
        },
    },
    'button_center': {
        'name': 'Button Centered',
        'template': 'widgets/read-more-link.html',
        'context': {
            'align': 'center',
            'text': 'Use the framework',
            'href': 'http://google.de',
            'button': True,
        },
    },
    'button_right': {
        'name': 'Button Right',
        'template': 'widgets/read-more-link.html',
        'context': {
            'align': 'right',
            'text': 'Use the framework',
            'href': 'http://google.de',
            'button': True,
        },
    },
    'readmorelink': {
        'name': 'Read more link',
        'template': 'widgets/read-more-link.html',
        'context': {
            'text': 'weiterlesen',
            'href': 'http://x',
        },
    },
    'readmorelink_fontawesome': {
        'name': 'Read more link Fontawesome',
        'template': 'widgets/read-more-link.html',
        'context': {
            'text': 'bearbeiten',
            'fontawesome': 'pencil',
            'href': 'http://x',
        },
    },
    'readmorelink_right': {
        'name': 'Read more link – right align',
        'template': 'widgets/read-more-link.html',
        'context': {
            'text': 'weiterlesen',
            'href': 'http://x',
            'align': 'right',
        },
    },
    'readmorelink_projects': {
        'name': 'Read more link',
        'template': 'widgets/read-more-link.html',
        'context': {
            'text': 'Show all projects including archived',
            'href': 'http://x',
        },
    },
    'readmorelink_countries': {
        'name': 'Read more link',
        'template': 'widgets/read-more-link.html',
        'context': {
            'text': 'Show all countries including stubs',
            'href': 'http://x',
        },
    },
    'readmorelink_news': {
        'name': 'Read all news',
        'template': 'widgets/read-more-link.html',
        'context': {
            'text': 'Show all news',
            'href': 'http://x',
        },
    },


    'richtext': {
        'name': 'Richtext',
        'template': 'widgets/richtext.html',
        'context': {
            'content': '<div class="rich-text"><p><img class="richtext-image right" src="/static/styleguide/test-images/header3.jpg" alt="Schönes Bild">Jemand musste Josef K. verleumdet haben, denn ohne dass er etwas Böses getan hätte, wurde er <a href="#">eines Morgens</a> verhaftet. »Wie ein Hund!« sagte er, es war, als sollte die Scham ihn überleben. Als Gregor Samsa eines Morgens aus unruhigen Träumen erwachte, fand er sich in seinem Bett zu einem ungeheueren Ungeziefer verwandelt. Und es war ihnen wie eine Bestätigung ihrer neuen Träume und guten Absichten, als am Ziele ihrer Fahrt die Tochter als erste sich erhob und ihren jungen Körper dehnte. »Es ist ein eigentümlicher Apparat«, sagte der Offizier zu dem Forschungsreisenden und überblickte mit einem gewissermaßen bewundernden Blick den ihm doch wohlbekannten Apparat. Sie hätten noch ins Boot springen können, aber der Reisende hob ein schweres, geknotetes Tau vom Boden, drohte ihnen damit und hielt sie dadurch von dem Sprunge ab.</p><div style="padding-bottom: 56.25%;" class="responsive-object"><iframe src="https://www.youtube.com/embed/SywPPK8ixiw?feature=oembed" allowfullscreen="" width="480" frameborder="0" height="270"></iframe></div><h3>Yolo!</h3><p>Jemand musste Josef K. verleumdet haben, denn ohne dass er etwas Böses getan hätte, wurde er eines Morgens verhaftet. »Wie ein Hund!« sagte er, es war, als sollte die Scham ihn überleben. Als Gregor Samsa eines Morgens aus unruhigen Träumen erwachte, fand er sich in seinem Bett zu einem ungeheueren Ungeziefer verwandelt. Und es war ihnen wie eine Bestätigung ihrer neuen Träume und guten Absichten, als am Ziele ihrer Fahrt die Tochter als erste sich erhob und ihren jungen Körper dehnte. »Es ist ein eigentümlicher Apparat«, sagte der Offizier zu dem Forschungsreisenden und überblickte mit einem gewissermaßen bewundernden Blick den ihm doch wohlbekannten Apparat. Sie hätten noch ins Boot springen können, aber der Reisende hob ein schweres, geknotetes Tau vom Boden, drohte ihnen damit und hielt sie dadurch von dem Sprunge ab.</p></div>',
        },
    },
    'richtext_project': {
        'name': 'Richtext',
        'template': 'widgets/richtext.html',
        'context': {
            'content': '<div class="rich-text"><h3>About the project</h3><p>Jemand musste Josef K. verleumdet haben, denn ohne dass er etwas Böses getan hätte, wurde er eines Morgens verhaftet. »Wie ein Hund!« sagte er, es war, als sollte die Scham ihn überleben. Als Gregor Samsa eines Morgens aus unruhigen Träumen erwachte, fand er sich in seinem Bett zu einem ungeheueren Ungeziefer verwandelt. Und es war ihnen wie eine Bestätigung ihrer neuen Träume und guten Absichten, als am Ziele ihrer Fahrt die Tochter als erste sich erhob und ihren jungen Körper dehnte.</p></div>',
        },
    },

    'embed': {
        'name': 'Embed',
        'template': 'widgets/embed.html',
        'context': {
            'embed': '<div style="padding-bottom: 56.25%;" class="responsive-object"><iframe src="https://www.youtube.com/embed/BrPYsOhRj4I?feature=oembed" allowfullscreen="" width="480" frameborder="0" height="270"></iframe></div>',
        },
    },


    'pagination': {
        'name': 'Pagination',
        'template': 'widgets/pagination.html',
        'context': {
            'pages': [
                {
                    'href': 'http://google.de',
                    'text': '1',
                },
                {
                    'href': '/glossar/',
                    'text': '2',
                },
                {
                    'active': True,
                    'href': 'http://google.ru',
                    'text': '3',
                },
                {
                    'href': 'http://google.ru',
                    'text': '4',
                },
                {
                    'href': 'http://google.ru',
                    'text': '5',
                },
            ],
        },
    },

    'members_table': {
        'name': 'Members Table',
        'template': 'widgets/members-table.html',
        'context': {
            'allcountries': 'All Countries',
            'countries': [
                { 'name': 'Germany', },
                { 'name': 'Niger', },
                { 'name': 'Toga', },
            ],
            'allorganisations': 'All Organisations',
            'organisations': [
                { 'name': 'Sinnwerkstatt', },
                { 'name': 'Telekom', },
                { 'name': 'O2', },
                { 'name': 'Google', },
                { 'name': 'Müllermilch', },
                { 'name': 'Nutella', },
                { 'name': 'Oranienhof', },
                { 'name': 'Microsoft', },
                { 'name': 'Adobe', },
                { 'name': 'Calumet', },
            ],
            'allexpertises': 'All Expertiese',
            'expertises': [
                { 'name': 'Strippen ziehen', },
                { 'name': 'Schrauben drehn', },
                { 'name': 'Werkstatt stehn', },
                { 'name': 'Fahne wehn', },
            ],
            'pages': [1,2,3,4], # Math.ceil ( Anzahl Members / Members pro Seite )
            'maxpagesize': 3, # Members pro Seite
            'members': [
                {
                    'avatarsrc': '/static/styleguide/test-images/dog-1by1.jpg',
                    'url': 'http://google.de',
                    'name': 'Eraldo mit sehr langem Namen',
                    'href': 'http://x',
                    'country': 'Germany',
                    'organisation': 'Sinnwerkstatt',
                    'position': 'Manager',
                    'expertises': [
                    ],
                    'visible': True,
                },
                {
                    'avatarsrc': '/static/styleguide/test-images/giraffe-1by1.jpg',
                    'url': 'http://google.de',
                    'name': 'Tomi',
                    'href': 'http://x',
                    'country': 'Niger',
                    'organisation': 'Telekom',
                    'position': 'Manager',
                    'expertises': [
                        { 'name': 'Strippen ziehen', },
                    ],
                    'visible': True,
                },
                {
                    'avatarsrc': '/static/styleguide/test-images/studio-1by1.jpg',
                    'url': 'http://google.de',
                    'name': 'Udo',
                    'href': 'http://x',
                    'country': 'Germany',
                    'organisation': 'O2',
                    'position': 'Manager',
                    'expertises': [
                        { 'name': 'Schrauben drehn', },
                    ],
                    'visible': True,
                },
                {
                    'avatarsrc': '/static/styleguide/test-images/silhouette-1by1.jpg',
                    'url': 'http://google.de',
                    'name': 'Matthias',
                    'country': 'Niger',
                    'organisation': 'Google',
                    'position': 'Manager',
                    'expertises': [
                        { 'name': 'Werkstatt stehn', },
                        { 'name': 'Fahne wehn', },
                    ],
                    'visible': False,
                },
                {
                    'avatarsrc': '/static/styleguide/test-images/girls-1by1.jpg',
                    'url': 'http://google.de',
                    'name': 'Nuts',
                    'country': 'Toga',
                    'organisation': 'Microsoft',
                    'position': 'Manager',
                    'expertises': [
                        { 'name': 'Strippen ziehen', },
                        { 'name': 'Fahne wehn', },
                    ],
                    'visible': False,
                },
                {
                    'avatarsrc': '/static/styleguide/test-images/giraffe-1by1.jpg',
                    'url': 'http://google.de',
                    'name': 'Cheffe',
                    'country': 'Germany',
                    'organisation': 'Google',
                    'position': 'Manager',
                    'expertises': [
                        { 'name': 'Strippen ziehen', },
                        { 'name': 'Schrauben drehn', },
                        { 'name': 'Werkstatt stehn', },
                    ],
                    'visible': False,
                },
                {
                    'avatarsrc': '/static/styleguide/test-images/dog-1by1.jpg',
                    'url': 'http://google.de',
                    'name': 'Riot',
                    'country': 'Niger',
                    'organisation': 'Adobe',
                    'position': 'Manager',
                    'expertises': [
                        { 'name': 'Werkstatt stehn', },
                        { 'name': 'Fahne wehn', },
                    ],
                    'visible': False,
                },
                {
                    'avatarsrc': '/static/styleguide/test-images/studio-1by1.jpg',
                    'url': 'http://google.de',
                    'name': 'Lene',
                    'country': 'Toga',
                    'organisation': 'Nutella',
                    'position': 'Manager',
                    'expertises': [
                        { 'name': 'Strippen ziehen', },
                        { 'name': 'Schrauben drehn', },
                        { 'name': 'Fahne wehn', },
                    ],
                    'visible': False,
                },
                {
                    'avatarsrc': '/static/styleguide/test-images/silhouette-1by1.jpg',
                    'url': 'http://google.de',
                    'name': 'Markus',
                    'country': 'Niger',
                    'organisation': 'Oranienhof',
                    'position': 'Manager',
                    'expertises': [
                        { 'name': 'Strippen ziehen', },
                    ],
                    'visible': False,
                },
                {
                    'avatarsrc': '/static/styleguide/test-images/girls-1by1.jpg',
                    'url': 'http://google.de',
                    'name': 'Johanna',
                    'country': 'Germany',
                    'organisation': 'Müllermilch',
                    'position': 'Manager',
                    'expertises': [
                        { 'name': 'Strippen ziehen', },
                        { 'name': 'Schrauben drehn', },
                        { 'name': 'Werkstatt stehn', },
                        { 'name': 'Fahne wehn', },
                    ],
                    'visible': False,
                },
                {
                    'avatarsrc': '/static/styleguide/test-images/giraffe-1by1.jpg',
                    'url': 'http://google.de',
                    'name': 'Tobi',
                    'country': 'Toga',
                    'organisation': 'Calumet',
                    'position': 'Manager',
                    'expertises': [
                        { 'name': 'Strippen ziehen', },
                        { 'name': 'Schrauben drehn', },
                        { 'name': 'Fahne wehn', },
                    ],
                    'visible': False,
                },
            ],
        },
    },
    'breadcrumb': {
        'name': 'Breadcrumb with 3 entries',
        'template': 'widgets/breadcrumb.html',
        'context': {
            'links': [
                { 'href': 'http://google.de', 'text': 'Kontakt' },
                { 'href': 'http://bing.de', 'text': 'Presse' },
                { 'text': 'Newsletter' },
            ],
        },
    },
    'breadcrumb_project': {
        'name': 'Breadcrumb with 3 entries',
        'template': 'widgets/breadcrumb.html',
        'context': {
            'links': [
                { 'href': 'http://google.de', 'text': 'Home' },
                { 'href': 'http://bing.de', 'text': 'Project and Countries' },
                { 'text': 'DS-SLM' },
            ],
        },
    },
    'file_link_pdf': {
        'name': 'File Link – PDF',
        'template': 'widgets/file-link.html',
        'context': {
            'title': 'Project flyer',
            'filename': 'Flyer Export 2016.pdf',
            'filesize': '130&#8239;kB',
            'type': 'pdf',
            'fileurl': 'http://google.de',
        },
    },
    'file_link_video': {
        'name': 'File Link – Video',
        'template': 'widgets/file-link.html',
        'context': {
            'filename': 'video-no-title.avi',
            'filesize': '56&#8239;MB',
            'type': 'video',
            'fileurl': 'http://google.de',
        },
    },
    'file_link_xls': {
        'name': 'File Link – XLS',
        'template': 'widgets/file-link.html',
        'context': {
            'title': 'Wocat calculation',
            'fileurl': 'http://google.de',
        },
    },
    'sidebar': {
        'name': 'Sidebar',
        'template': 'widgets/sidebar.html',
        'context': {
            'links': [
                { 'href': '#affix-headings', 'text': 'Headings', 'anchorlink': True, 'color': '#403D38', },
                { 'href': '#affix-carousel', 'text': 'Carousel', 'anchorlink': True, 'color': '#6E3237', },
                { 'href': '#affix-teaser', 'text': 'Teaser', 'anchorlink': True, 'color': '#604F3B', },
                { 'href': '#affix-media', 'text': 'Media', 'anchorlink': True, 'color': '#3B482E', },
                { 'href': '#affix-richtext', 'text': 'Richtext', 'anchorlink': True, 'color': '#22454E', },
                { 'href': '#affix-links', 'text': 'Links', 'anchorlink': True, 'color': '#2D446B', },
                { 'href': '#affix-forms', 'text': 'Forms', 'anchorlink': True, 'color': '#3A3451', },
                { 'href': '#affix-map', 'text': 'Map', 'anchorlink': True, 'color': '#344351', },
            ],
        },
    },


    'map_large': {
        'name': 'Map Large',
        'template': 'widgets/map.html',
        'context': {
            'size': 'large',
            'countries': [
                { 'iso_3166_1_alpha_3': 'LSO', 'popup': '<a href="x">Lesotho</a>', },
                { 'iso_3166_1_alpha_3': 'MAR', 'popup': '<a href="x">Morocco</a>', },
                { 'iso_3166_1_alpha_3': 'NGA', 'popup': '<a href="x">Nigeria</a>', },
                { 'iso_3166_1_alpha_3': 'TUN', 'popup': '<a href="x">Tunisia</a>', },

                { 'iso_3166_1_alpha_3': 'BGD', 'popup': '<a href="x">Bangladesh</a>', },
                { 'iso_3166_1_alpha_3': 'CHN', 'popup': '<a href="x">China</a>', },
                { 'iso_3166_1_alpha_3': 'PHL', 'popup': '<a href="x">Philippines</a>', },
                { 'iso_3166_1_alpha_3': 'THA', 'popup': '<a href="x">Thailand</a>', },

                { 'iso_3166_1_alpha_3': 'BIH', 'popup': '<a href="x">Bosnia & Herzegovina</a>', },
                { 'iso_3166_1_alpha_3': 'TUR', 'popup': '<a href="x">Turkey</a>', },
                { 'iso_3166_1_alpha_3': 'UZB', 'popup': '<a href="x">Uzbekistan</a>', },

                { 'iso_3166_1_alpha_3': 'ARG', 'popup': '<a href="x">Argentinia</a>', },
                { 'iso_3166_1_alpha_3': 'COL', 'popup': '<a href="x">Colombia</a>', },
                { 'iso_3166_1_alpha_3': 'ECU', 'popup': '<a href="x">Equador</a>', },
                { 'iso_3166_1_alpha_3': 'PAN', 'popup': '<a href="x">Panama</a>', },
            ],
        },
    },
    'map': {
        'name': 'Map',
        'template': 'widgets/map.html',
        'context': {
            'countries': [
                { 'iso_3166_1_alpha_3': 'LSO', 'popup': '<a href="x">Lesotho</a>', },
                { 'iso_3166_1_alpha_3': 'MAR', 'popup': '<a href="x">Morocco</a>', },
                { 'iso_3166_1_alpha_3': 'NGA', 'popup': '<a href="x">Nigeria</a>', },
                { 'iso_3166_1_alpha_3': 'TUN', 'popup': '<a href="x">Tunisia</a>', },

                { 'iso_3166_1_alpha_3': 'BGD', 'popup': '<a href="x">Bangladesh</a>', },
                { 'iso_3166_1_alpha_3': 'CHN', 'popup': '<a href="x">China</a>', },
                { 'iso_3166_1_alpha_3': 'PHL', 'popup': '<a href="x">Philippines</a>', },
                { 'iso_3166_1_alpha_3': 'THA', 'popup': '<a href="x">Thailand</a>', },

                { 'iso_3166_1_alpha_3': 'BIH', 'popup': '<a href="x">Bosnia & Herzegovina</a>', },
                { 'iso_3166_1_alpha_3': 'TUR', 'popup': '<a href="x">Turkey</a>', },
                { 'iso_3166_1_alpha_3': 'UZB', 'popup': '<a href="x">Uzbekistan</a>', },

                { 'iso_3166_1_alpha_3': 'ARG', 'popup': '<a href="x">Argentinia</a>', },
                { 'iso_3166_1_alpha_3': 'COL', 'popup': '<a href="x">Colombia</a>', },
                { 'iso_3166_1_alpha_3': 'ECU', 'popup': '<a href="x">Equador</a>', },
                { 'iso_3166_1_alpha_3': 'PAN', 'popup': '<a href="x">Panama</a>', },
            ],
        },
    },
    'map_small': {
        'name': 'Map Small',
        'template': 'widgets/map.html',
        'context': {
            'size': 'small',
            'countries': [
                { 'iso_3166_1_alpha_3': 'AUT', },
                { 'iso_3166_1_alpha_3': 'BIH', },
                { 'iso_3166_1_alpha_3': 'CHE', },
                { 'iso_3166_1_alpha_3': 'ECU', },
                { 'iso_3166_1_alpha_3': 'CMR', },
                { 'iso_3166_1_alpha_3': 'KEN', },
                { 'iso_3166_1_alpha_3': 'NGA', },
                { 'iso_3166_1_alpha_3': 'DZA', },
            ],
        },
    },
    'map_teaser_project': {
        'name': 'Map Teaser Multiple',
        'template': 'widgets/teaser.html',
        'context': {
            'map': {
                'countries': [
                    { 'iso_3166_1_alpha_3': 'LSO', 'popup': '<a href="x">Lesotho</a>', },
                    { 'iso_3166_1_alpha_3': 'MAR', 'popup': '<a href="x">Morocco</a>', },
                    { 'iso_3166_1_alpha_3': 'NGA', 'popup': '<a href="x">Nigeria</a>', },
                    { 'iso_3166_1_alpha_3': 'TUN', 'popup': '<a href="x">Tunisia</a>', },

                    { 'iso_3166_1_alpha_3': 'BGD', 'popup': '<a href="x">Bangladesh</a>', },
                    { 'iso_3166_1_alpha_3': 'CHN', 'popup': '<a href="x">China</a>', },
                    { 'iso_3166_1_alpha_3': 'PHL', 'popup': '<a href="x">Philippines</a>', },
                    { 'iso_3166_1_alpha_3': 'THA', 'popup': '<a href="x">Thailand</a>', },

                    { 'iso_3166_1_alpha_3': 'BIH', 'popup': '<a href="x">Bosnia & Herzegovina</a>', },
                    { 'iso_3166_1_alpha_3': 'TUR', 'popup': '<a href="x">Turkey</a>', },
                    { 'iso_3166_1_alpha_3': 'UZB', 'popup': '<a href="x">Uzbekistan</a>', },

                    { 'iso_3166_1_alpha_3': 'ARG', 'popup': '<a href="x">Argentinia</a>', },
                    { 'iso_3166_1_alpha_3': 'COL', 'popup': '<a href="x">Colombia</a>', },
                    { 'iso_3166_1_alpha_3': 'ECU', 'popup': '<a href="x">Equador</a>', },
                    { 'iso_3166_1_alpha_3': 'PAN', 'popup': '<a href="x">Panama</a>', },
                ],
            },
            'title': 'Decision support for mainstreaming and scaling out SLM',
            'description': 'The DS-SLM project contributes to arresting and reversing current global trends in land degradation by supporting 15 countries in mainstreaming and scaling out SLM.',
            'href': 'x',
            'readmorelink': {
                'text': 'to the project',
            },
        },
    },
    'map_teaser_project1': {
        'name': 'Project Teaser Map 1',
        'template': 'widgets/teaser.html',
        'context': {
            'map': {
                'countries': [
                    { 'iso_3166_1_alpha_3': 'SOM', },
                    { 'iso_3166_1_alpha_3': 'SDN', },
                    { 'iso_3166_1_alpha_3': 'UGA', },
                    { 'iso_3166_1_alpha_3': 'ZWE', },
                ],
            },
            'title': 'Project Alpha',
            'description': 'The project alpha is bla bla and lorem ipsum. Numbers are five and nine.',
            'href': 'x',
            'readmorelink': {
                'text': 'to the project',
            },
        },
    },
    'map_teaser_project2': {
        'name': 'Map Teaser Country',
        'template': 'widgets/teaser.html',
        'context': {
            'map': {
                'size': 'small',
                'countries': [
                    { 'iso_3166_1_alpha_3': 'DzA', },
                ],
            },
            'title': 'Algier',
            'flag_iso_3166_1_alpha_3': 'dZa',
            'description': 'Ein paar Zahlen zu Algerien: Lala und Blubblub.',
            'href': 'x',
            'readmorelink': {
                'text': 'to the country',
            },
        },
    },
    'map_teaser_project3': {
        'name': 'Project Map Teaser 3',
        'template': 'widgets/teaser.html',
        'context': {
            'map': {
                'size': 'small',
                'countries': [
                    { 'iso_3166_1_alpha_3': 'KEN', },
                ],
            },
            'title': 'Kenya',
            'flag_iso_3166_1_alpha_3': 'ken',
            'description': 'Ein paar Zahlen zu Kenia: Lala und Blubblub.',
            'href': 'x',
            'readmorelink': {
                'text': 'to the country',
            },
        },
    },
    'map_teaser_project4': {
        'name': 'Project Map Teaser 4',
        'template': 'widgets/teaser.html',
        'context': {
            'map': {
                'size': 'small',
                'countries': [
                    { 'iso_3166_1_alpha_3': 'NGA', },
                ],
            },
            'title': 'Nigeria',
            'flag_iso_3166_1_alpha_3': 'nga',
            'description': 'Ein paar Zahlen zu Nigeria: Lala und Blubblub.',
            'href': 'x',
            'readmorelink': {
                'text': 'to the country',
            },
        },
    },

    'definition': {
        'name': 'Definition',
        'template': 'widgets/definition.html',
        'context': {
            'tag': 'Wocat',
            'definition': 'Ein Trainer ist nicht ein Idiot! Ein Trainer sei sehen was passieren in Platz.\nIn diese Spiel es waren zwei, drei diese Spieler waren schwach wie eine Flasche leer!',
        },
    },
    'definition_acronym': {
        'name': 'Definition',
        'template': 'widgets/definition.html',
        'context': {
            'tag': 'LADA',
            'acronym': True,
            'definition': ' Land Degradation Assessments in Drylands',
        },
    },

    'media': {
        'name': 'Media',
        'template': 'widgets/teaser.html',
        'context': {
            'imgpos': 'top',
            'imgsrc': '/static/styleguide/test-images/header3-3by1.jpg',
            'title': 'Eisberge',
            'description': 'Eine Dokumentation über Gletscher in Kenia. Oder gehörten die Schritte hinter ihm zu einem der unzähligen Gesetzeshüter dieser Stadt, und die stählerne Acht um seine Handgelenke würde gleich zuschnappen?',
            'author': 'Eraldo Energy',
            'mediastyle': True,
            'readmorelink': {
                'text': 'Download Book',
            },
        },
    },
    'media_ytimage': {
        'name': 'Media',
        'template': 'widgets/teaser.html',
        'context': {
            'imgpos': 'top',
            'imgsrc': '/static/styleguide/test-images/youtube-thumb.jpg',
            'title': 'Auf die Größe kommts an. Besonders bei Titeln über mehrere Zeilen.',
            'description': 'Oder gehörten die Schritte hinter ihm zu einem der unzähligen Gesetzeshüter dieser Stadt, und die stählerne Acht um seine Handgelenke würde gleich zuschnappen?',
            'mediastyle': True,
            'readmorelink': {
                'text': 'View Video',
            },
        },
    },
    'media_defaultvideo': {
        'name': 'Media',
        'template': 'widgets/teaser.html',
        'context': {
            'imgpos': 'top',
            'imgsrc': '/static/images/media-thumbs/video.svg',
            'title': 'Jagt auf Lianen',
            'description': 'Ein Video ohne Bild. Oder gehörten die Schritte hinter ihm zu einem der unzähligen Gesetzeshüter dieser Stadt, und die stählerne Acht um seine Handgelenke würde gleich zuschnappen?',
            'mediastyle': True,
            'readmorelink': {
                'text': 'View Video',
            },
        },
    },
    'media_highimage': {
        'name': 'Media',
        'template': 'widgets/teaser.html',
        'context': {
            'imgpos': 'top',
            'imgsrc': '/static/styleguide/test-images/giraffe-vertical.jpg',
            'title': 'Die Giraffe',
            'description': 'Oder gehörten die Schritte hinter ihm zu einem der unzähligen Gesetzeshüter dieser Stadt, und die stählerne Acht um seine Handgelenke würde gleich zuschnappen?',
            'mediastyle': True,
            'readmorelink': {
                'text': 'Show Media',
            },
        },
    },
    'media_defaultbook': {
        'name': 'Media',
        'template': 'widgets/teaser.html',
        'context': {
            'imgpos': 'top',
            'imgsrc': '/static/images/media-thumbs/book.svg',
            'title': 'Südafrika und die Pinguine',
            'description': 'Ein Buch ohne eigenem Bild. Oder gehörten die Schritte hinter ihm zu einem der unzähligen Gesetzeshüter dieser Stadt, und die stählerne Acht um seine Handgelenke würde gleich zuschnappen?',
            'mediastyle': True,
            'readmorelink': {
                'text': 'Show Media',
            },
        },
    },
    'media_defaultbrochure': {
        'name': 'Media',
        'template': 'widgets/teaser.html',
        'context': {
            'imgpos': 'top',
            'imgsrc': '/static/images/media-thumbs/brochure.svg',
            'title': 'Lose Blattsammlung',
            'description': 'Broschüre ohne Bild. Oder gehörten die Schritte hinter ihm zu einem der unzähligen Gesetzeshüter dieser Stadt, und die stählerne Acht um seine Handgelenke würde gleich zuschnappen?',
            'mediastyle': True,
            'readmorelink': {
                'text': 'Show Media',
            },
        },
    },
    'footer': {
        'name': 'Footer',
        'template': 'widgets/footer.html',
        'context': {
            'links': [
                { 'href': 'http://google.de/1', 'text': '<i class="fa fa-facebook" aria-hidden="true"></i>', 'onlyxs': True, },
                { 'href': 'http://bing.de/2', 'text': '<i class="fa fa-youtube" aria-hidden="true"></i>', 'onlyxs': True, },
                { 'href': 'http://bing.de/3', 'text': '<i class="fa fa-twitter" aria-hidden="true"></i>', 'onlyxs': True, },
                { 'href': 'http://google.de/1', 'text': 'Get involved', 'onlyxs': True, },
                { 'href': 'http://bing.de/2', 'text': 'FAQ', 'onlyxs': True, },
                { 'href': 'http://bing.de/3', 'text': 'Glossary', 'active': True, 'onlyxs': True, },
                { 'href': 'http://bing.de/2', 'text': 'Login', 'onlyxs': True, },
                { 'href': 'http://bing.de/2', 'text': 'Legal Disclaimer', },
                { 'href': 'http://bing.de/2', 'text': 'Contact', },
                { 'href': 'http://bing.de/2', 'text': 'Active', 'active': True, },

            ],
        },
    },
    'footer_demo': {
        'name': 'Footer',
        'template': 'widgets/footer.html',
        'context': {
            'links': [
                { 'href': 'http://google.de/1', 'text': '<i class="fa fa-facebook" aria-hidden="true"></i>', 'onlyxs': True, },
                { 'href': 'http://bing.de/2', 'text': '<i class="fa fa-youtube" aria-hidden="true"></i>', 'onlyxs': True, },
                { 'href': 'http://bing.de/3', 'text': '<i class="fa fa-twitter" aria-hidden="true"></i>', 'onlyxs': True, },
                { 'href': 'http://google.de/1', 'text': 'Get involved', 'onlyxs': True, },
                { 'href': 'http://bing.de/2', 'text': 'FAQ', 'onlyxs': True, },
                { 'href': 'http://bing.de/3', 'text': 'Glossary', 'onlyxs': True, },
                { 'href': 'http://bing.de/2', 'text': 'Login', 'onlyxs': True, },
                { 'href': 'http://bing.de/2', 'text': 'Legal Disclaimer', },
                { 'href': 'http://bing.de/2', 'text': 'Contact', },

            ],
        },
    },
    'affix': {
        'name': 'Affix',
        'template': 'widgets/affix.html',
        'context': {
            'sidebar_links': [
                { 'href': '#affix-1', 'kicker': 'Module 1', 'text': 'Operational Strategy and Action plan', 'anchorlink': True, },
                { 'href': '#affix-2', 'kicker': 'Module 2', 'text': 'National and Subnational Level', 'anchorlink': True },
                { 'href': '#affix-3', 'kicker': 'Module 3', 'text': 'Landscape Level', 'anchorlink': True },
                { 'href': '#affix-4', 'kicker': 'Module 4', 'text': 'Sea Level', 'anchorlink': True },
                { 'href': '#affix-5', 'kicker': 'Module 5', 'text': 'SLM Territorial Planning', 'anchorlink': True },
                { 'href': '#affix-6', 'kicker': 'Module 6', 'text': 'Implementation and scaling out', 'anchorlink': True },
                { 'href': '#affix-7', 'kicker': 'Module 7', 'text': 'Knowledge management platform for informed decision making', 'anchorlink': True },
            ],
            'sections': [
                {
                    'id': 'affix-1',
                    'content': '<h2>Module 1</h2><p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus.</p><p>Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Fusce vulputate eleifend sapien.</p><p>Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Nullam accumsan lorem in dui. Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ac dui quis mi consectetuer lacinia. Nam pretium turpis et arcu. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis, ipsum. Sed aliquam ultrices mauris. Integer ante arcu, accumsan a, consectetuer eget, posuere ut, mauris. Praesent adipiscing. Phasellus ullamcorper ipsum rutrum nunc. Nunc nonummy metus. Vestibulum volutpat pretium libero. Cras id dui. Aenean ut eros et nisl sagittis vestibulum. Nullam nulla eros, ultricies sit amet, nonummy id, imperdiet feugiat, pede.</p><p>Sed lectus. Donec mollis hendrerit risus. Phasellus nec sem in justo pellentesque facilisis. Etiam imperdiet imperdiet orci. Nunc nec neque. Phasellus leo dolor, tempus non, auctor et, hendrerit quis, nisi. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet, leo. Maecenas malesuada. Praesent congue erat at massa. Sed cursus turpis vitae tortor. Donec posuere vulputate arcu. Phasellus accumsan cursus velit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed aliquam, nisi quis porttitor congue, elit erat euismod orci, ac placerat dolor lectus quis orci. Phasellus consectetuer vestibulum elit. Aenean tellus metus, bibendum sed, posuere ac, mattis non, nunc. Vestibulum fringilla pede sit amet augue. In turpis. Pellentesque posuere. Praesent turpis. Aenean posuere, tortor sed cursus feugiat, nunc augue blandit nunc, eu sollicitudin urna dolor sagittis lacus. Donec elit libero, sodales nec, volutpat a, suscipit non, turpis. Nullam sagittis. Suspendisse pulvinar, augue ac venenatis condimentum, sem libero volutpat nibh, nec pellentesque velit pede quis nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Fusce id purus. Ut varius tincidunt libero. Phasellus dolor. Maecenas vestibulum mollis</p>',
                },
                {
                    'id': 'affix-2',
                    'content': '<h2>Module 2</h2><p>Li Europan lingues es membres del sam familie. Lor separat existentie es un myth. Por scientie, musica, sport etc, litot Europa usa li sam vocabular. Li lingues differe solmen in li grammatica, li pronunciation e li plu commun vocabules. Omnicos directe al desirabilite de un nov lingua franca: On refusa continuar payar custosi traductores. At solmen va esser necessi far uniform grammatica, pronunciation e plu sommun paroles. Ma quande lingues coalesce, li grammatica del resultant lingue es plu simplic e regulari quam ti del coalescent lingues. Li nov lingua franca va esser plu simplic e regulari quam li existent Europan lingues.</p><p>It va esser tam simplic quam Occidental in fact, it va esser Occidental. A un Angleso it va semblar un simplificat Angles, quam un skeptic Cambridge amico dit me que Occidental es. Li Europan lingues es membres del sam familie. Lor separat existentie es un myth. Por scientie, musica, sport etc, litot Europa usa li sam vocabular. Li lingues differe solmen in li grammatica, li pronunciation e li plu commun vocabules. Omnicos directe al desirabilite de un nov lingua franca: On refusa continuar payar custosi traductores. At solmen va esser necessi far uniform grammatica, pronunciation e plu sommun paroles.</p><p>Ma quande lingues coalesce, li grammatica del resultant lingue es plu simplic e regulari quam ti del coalescent lingues. Li nov lingua franca va esser plu simplic e regulari quam li existent Europan lingues. It va esser tam simplic quam Occidental in fact, it va esser Occidental. A un Angleso it va semblar un simplificat Angles, quam un skeptic Cambridge amico dit me que Occidental es. Li Europan lingues es membres del sam familie. Lor separat existentie es un myth. Por scientie, musica, sport etc, litot Europa usa li sam vocabular. Li lingues differe solmen in li grammatica, li pronunciation e li plu commun vocabules.</p><p>Omnicos directe al desirabilite de un nov lingua franca: On refusa continuar payar custosi traductores. At solmen va esser necessi far uniform grammatica, pronunciation e plu sommun paroles. Ma quande lingues coalesce, li grammatica del resultant lingue es plu simplic e regulari quam ti del coalescent lingues. Li nov lingua franca va esser plu simplic e regulari quam li existent Europan lingues. It va esser tam simplic quam Occidental in fact, it va esser Occidental. A un Angleso it va semblar un simplificat Angles, quam un skeptic Cambridge amico dit me que Occidental es. Li Europan lingues es membres del sam familie. Lor separat existentie es un myth. Por scientie, musica, sport etc, litot Europa usa li sam vocabular. Li lingues differe solmen in li grammatica, li pronunciation e li plu commun vocabules. Omnicos directe al desirabilite de un nov lingua franca: On refusa continuar payar custosi traductores. At solmen va esser necessi far uniform grammatica, pronunciation e plu sommun paroles. Ma quande lingues coalesce, li grammatica del resultant lingue es plu simplic e regulari quam ti del coalescent lingues. Li nov lingua franca va esser plu simplic e regulari quam li existent Europan lingues.</p>',
                },
                {
                    'id': 'affix-3',
                    'content': '<h2>Module 3</h2><p>Eine wunderbare Heiterkeit hat meine ganze Seele eingenommen, gleich den süßen Frühlingsmorgen, die ich mit ganzem Herzen genieße. Ich bin allein und freue mich meines Lebens in dieser Gegend, die für solche Seelen geschaffen ist wie die meine. Ich bin so glücklich, mein Bester, so ganz in dem Gefühle von ruhigem Dasein versunken, daß meine Kunst darunter leidet. Ich könnte jetzt nicht zeichnen, nicht einen Strich, und bin nie ein größerer Maler gewesen als in diesen Augenblicken.</p><p>Wenn das liebe Tal um mich dampft, und die hohe Sonne an der Oberfläche der undurchdringlichen Finsternis meines Waldes ruht, und nur einzelne Strahlen sich in das innere Heiligtum stehlen, ich dann im hohen Grase am fallenden Bache liege, und näher an der Erde tausend mannigfaltige Gräschen mir merkwürdig werden; wenn ich das Wimmeln der kleinen Welt zwischen Halmen, die unzähligen, unergründlichen Gestalten der Würmchen, der Mückchen näher an meinem Herzen fühle, und fühle die Gegenwart des Allmächtigen, der uns nach seinem Bilde schuf, das Wehen des Alliebenden, der uns in ewiger Wonne schwebend trägt und erhält; mein Freund!</p><p>Wenns dann um meine Augen dämmert, und die Welt um mich her und der Himmel ganz in meiner Seele ruhn wie die Gestalt einer Geliebten - dann sehne ich mich oft und denke : ach könntest du das wieder ausdrücken, könntest du dem Papiere das einhauchen, was so voll, so warm in dir lebt, daß es würde der Spiegel deiner Seele, wie deine Seele ist der Spiegel des unendlichen Gottes! - mein Freund - aber ich gehe darüber zugrunde, ich erliege unter der Gewalt der Herrlichkeit dieser Erscheinungen. Eine wunderbare Heiterkeit hat meine ganze Seele eingenommen, gleich den süßen Frühlingsmorgen, die ich mit ganzem Herzen genieße.</p><p>Ich bin allein und freue mich meines Lebens in dieser Gegend, die für solche Seelen geschaffen ist wie die meine. Ich bin so glücklich, mein Bester, so ganz in dem Gefühle von ruhigem Dasein versunken, daß meine Kunst darunter leidet. Ich könnte jetzt nicht zeichnen, nicht einen Strich, und bin nie ein größerer Maler gewesen als in diesen Augenblicken. Wenn das liebe Tal um mich dampft, und die hohe Sonne an der Oberfläche der undurchdringlichen Finsternis meines Waldes ruht, und nur einzelne Strahlen sich in das innere Heiligtum stehlen, ich dann im hohen Grase am fallenden Bache liege, und näher an der Erde tausend mannigfaltige Gräschen mir merkwürdig werden; wenn ich das Wimmeln der kleinen Welt zwischen Halmen, die unzähligen, unergründlichen Gestalten der Würmchen, der Mückchen näher an meinem Herzen fühle, und fühle die Gegenwart des Allmächtigen, der uns nach seinem Bilde schuf, das Wehen des Alliebenden, der uns in ewiger Wonne schwebend trägt und erhält; mein Freund! Wenns dann um meine Augen dämmert, und die Welt um mich her und der Himmel ganz in meiner Seele ruhn wie die Gestalt einer Geliebten - dann sehne ich mich oft und denke : ach könntest du das wieder ausdrücken, könntest du dem Papiere das einhauchen, was so voll, so warm in dir lebt, daß es würde der Spiegel deiner</p>',
                },
                {
                    'id': 'affix-4',
                    'content': '<h2>Module 4</h2><p>Jemand musste Josef K. verleumdet haben, denn ohne dass er etwas Böses getan hätte, wurde er eines Morgens verhaftet. »Wie ein Hund! « sagte er, es war, als sollte die Scham ihn überleben. Als Gregor Samsa eines Morgens aus unruhigen Träumen erwachte, fand er sich in seinem Bett zu einem ungeheueren Ungeziefer verwandelt. Und es war ihnen wie eine Bestätigung ihrer neuen Träume und guten Absichten, als am Ziele ihrer Fahrt die Tochter als erste sich erhob und ihren jungen Körper dehnte. »Es ist ein eigentümlicher Apparat«, sagte der Offizier zu dem Forschungsreisenden und überblickte mit einem gewissermaßen bewundernden Blick den ihm doch wohlbekannten Apparat.</p><p>Sie hätten noch ins Boot springen können, aber der Reisende hob ein schweres, geknotetes Tau vom Boden, drohte ihnen damit und hielt sie dadurch von dem Sprunge ab. In den letzten Jahrzehnten ist das Interesse an Hungerkünstlern sehr zurückgegangen. Aber sie überwanden sich, umdrängten den Käfig und wollten sich gar nicht fortrühren. Jemand musste Josef K. verleumdet haben, denn ohne dass er etwas Böses getan hätte, wurde er eines Morgens verhaftet. »Wie ein Hund! « sagte er, es war, als sollte die Scham ihn überleben. Als Gregor Samsa eines Morgens aus unruhigen Träumen erwachte, fand er sich in seinem Bett zu einem ungeheueren Ungeziefer verwandelt.</p><p>Und es war ihnen wie eine Bestätigung ihrer neuen Träume und guten Absichten, als am Ziele ihrer Fahrt die Tochter als erste sich erhob und ihren jungen Körper dehnte. »Es ist ein eigentümlicher Apparat«, sagte der Offizier zu dem Forschungsreisenden und überblickte mit einem gewissermaßen bewundernden Blick den ihm doch wohlbekannten Apparat. Sie hätten noch ins Boot springen können, aber der Reisende hob ein schweres, geknotetes Tau vom Boden, drohte ihnen damit und hielt sie dadurch von dem Sprunge ab. In den letzten Jahrzehnten ist das Interesse an Hungerkünstlern sehr zurückgegangen. Aber sie überwanden sich, umdrängten den Käfig und wollten sich gar nicht fortrühren.</p><p>Jemand musste Josef K. verleumdet haben, denn ohne dass er etwas Böses getan hätte, wurde er eines Morgens verhaftet. »Wie ein Hund! « sagte er, es war, als sollte die Scham ihn überleben. Als Gregor Samsa eines Morgens aus unruhigen Träumen erwachte, fand er sich in seinem Bett zu einem ungeheueren Ungeziefer verwandelt. Und es war ihnen wie eine Bestätigung ihrer neuen Träume und guten Absichten, als am Ziele ihrer Fahrt die Tochter als erste sich erhob und ihren jungen Körper dehnte. »Es ist ein eigentümlicher Apparat«, sagte der Offizier zu dem Forschungsreisenden und überblickte mit einem gewissermaßen bewundernden Blick den ihm doch wohlbekannten Apparat. Sie hätten noch ins Boot springen können, aber der Reisende hob ein schweres, geknotetes Tau vom Boden, drohte ihnen damit und hielt sie dadurch von dem Sprunge ab. In den letzten Jahrzehnten ist das Interesse an Hungerkünstlern sehr zurückgegangen. Aber sie überwanden sich, umdrängten den Käfig und wollten sich gar nicht fortrühren. Jemand musste Josef K. verleumdet haben, denn ohne dass er etwas Böses getan hätte, wurde er eines Morgens verhaftet. »Wie ein Hund! « sagte er, es war, als sollte die Scham ihn überleben.</p>',
                },
                {
                    'id': 'affix-5',
                    'content': '<h2>Module 5</h2><p>Es gibt im Moment in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern. Letzte Spiel hatten wir in Platz drei Spitzen: Elber, Jancka und dann Zickler. Wir müssen nicht vergessen Zickler. Zickler ist eine Spitzen mehr, Mehmet eh mehr Basler. Ist klar diese Wörter, ist möglich verstehen, was ich hab gesagt? Danke. Offensiv, offensiv ist wie machen wir in Platz.</p><p>Zweitens: ich habe erklärt mit diese zwei Spieler: nach Dortmund brauchen vielleicht Halbzeit Pause. Ich habe auch andere Mannschaften gesehen in Europa nach diese Mittwoch. Ich habe gesehen auch zwei Tage die Training. Ein Trainer ist nicht ein Idiot! Ein Trainer sei sehen was passieren in Platz. In diese Spiel es waren zwei, drei diese Spieler waren schwach wie eine Flasche leer! Haben Sie gesehen Mittwoch, welche Mannschaft hat gespielt Mittwoch? Hat gespielt Mehmet oder gespielt Basler oder hat gespielt Trapattoni? Diese Spieler beklagen mehr als sie spielen! Wissen Sie, warum die Italienmannschaften kaufen nicht diese Spieler? Weil wir haben gesehen viele Male solche Spiel!</p><p>Haben gesagt sind nicht Spieler für die italienisch Meisters! Strunz! Strunz ist zwei Jahre hier, hat gespielt 10 Spiele, ist immer verletzt! Was erlauben Strunz? Letzte Jahre Meister Geworden mit Hamann, eh, Nerlinger. Diese Spieler waren Spieler! Waren Meister geworden! Ist immer verletzt! Hat gespielt 25 Spiele in diese Mannschaft in diese Verein. Muß respektieren die andere Kollegen! haben viel nette kollegen! Stellen Sie die Kollegen die Frage! Haben keine Mut an Worten, aber ich weiß, was denken über diese Spieler. Mussen zeigen jetzt, ich will, Samstag, diese Spieler müssen zeigen mich, seine Fans, müssen alleine die Spiel gewinnen. Muß allein die Spiel gewinnen!</p><p>Ich bin müde jetzt Vater diese Spieler, eh der Verteidiger diese Spieler. Ich habe immer die Schuld über diese Spieler. Einer ist Mario, einer andere ist Mehmet! Strunz ich spreche nicht, hat gespielt nur 25 Prozent der Spiel. Ich habe fertig! . . . wenn es gab Fragen, ich kann Worte wiederholen. . . Es gibt im Moment in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern. Letzte Spiel hatten wir in Platz drei Spitzen: Elber, Jancka und dann Zickler. Wir müssen nicht vergessen Zickler. Zickler ist eine Spitzen mehr, Mehmet eh mehr Basler. Ist klar diese Wörter, ist möglich verstehen, was ich hab gesagt? Danke. Offensiv, offensiv ist wie machen wir in Platz. Zweitens: ich habe erklärt mit diese zwei Spieler: nach Dortmund brauchen vielleicht Halbzeit Pause. Ich habe auch andere Mannschaften gesehen in Europa nach diese Mittwoch. Ich habe gesehen auch zwei Tage die Training. Ein Trainer ist nicht ein Idiot! Ein Trainer sei sehen was passieren in Platz. In diese Spiel es waren zwei, drei</p>',
                },
                {
                    'id': 'affix-6',
                    'content': '<h2>Module 6</h2><p>Zwei flinke Boxer jagen die quirlige Eva und ihren Mops durch Sylt. Franz jagt im komplett verwahrlosten Taxi quer durch Bayern. Zwölf Boxkämpfer jagen Viktor quer über den großen Sylter Deich. Vogel Quax zwickt Johnys Pferd Bim. Sylvia wagt quick den Jux bei Pforzheim. Polyfon zwitschernd aßen Mäxchens Vögel Rüben, Joghurt und Quark. "Fix, Schwyz! " quäkt Jürgen blöd vom Paß. Victor jagt zwölf Boxkämpfer quer über den großen Sylter Deich. Falsches Üben von Xylophonmusik quält jeden größeren Zwerg. Heizölrückstoßabdämpfung. Zwei flinke Boxer jagen die quirlige Eva und ihren Mops durch Sylt. Franz jagt im komplett verwahrlosten Taxi quer durch Bayern.</p><p>Zwölf Boxkämpfer jagen Viktor quer über den großen Sylter Deich. Vogel Quax zwickt Johnys Pferd Bim. Sylvia wagt quick den Jux bei Pforzheim. Polyfon zwitschernd aßen Mäxchens Vögel Rüben, Joghurt und Quark. "Fix, Schwyz! " quäkt Jürgen blöd vom Paß. Victor jagt zwölf Boxkämpfer quer über den großen Sylter Deich. Falsches Üben von Xylophonmusik quält jeden größeren Zwerg. Heizölrückstoßabdämpfung. Zwei flinke Boxer jagen die quirlige Eva und ihren Mops durch Sylt. Franz jagt im komplett verwahrlosten Taxi quer durch Bayern. Zwölf Boxkämpfer jagen Viktor quer über den großen Sylter Deich. Vogel Quax zwickt Johnys Pferd Bim. Sylvia wagt quick den Jux bei Pforzheim.</p><p>Polyfon zwitschernd aßen Mäxchens Vögel Rüben, Joghurt und Quark. "Fix, Schwyz! " quäkt Jürgen blöd vom Paß. Victor jagt zwölf Boxkämpfer quer über den großen Sylter Deich. Falsches Üben von Xylophonmusik quält jeden größeren Zwerg. Heizölrückstoßabdämpfung. Zwei flinke Boxer jagen die quirlige Eva und ihren Mops durch Sylt. Franz jagt im komplett verwahrlosten Taxi quer durch Bayern. Zwölf Boxkämpfer jagen Viktor quer über den großen Sylter Deich. Vogel Quax zwickt Johnys Pferd Bim. Sylvia wagt quick den Jux bei Pforzheim. Polyfon zwitschernd aßen Mäxchens Vögel Rüben, Joghurt und Quark. "Fix, Schwyz! " quäkt Jürgen blöd vom Paß. Victor jagt zwölf Boxkämpfer quer über den großen Sylter Deich.</p><p>Falsches Üben von Xylophonmusik quält jeden größeren Zwerg. Heizölrückstoßabdämpfung. Zwei flinke Boxer jagen die quirlige Eva und ihren Mops durch Sylt. Franz jagt im komplett verwahrlosten Taxi quer durch Bayern. Zwölf Boxkämpfer jagen Viktor quer über den großen Sylter Deich. Vogel Quax zwickt Johnys Pferd Bim. Sylvia wagt quick den Jux bei Pforzheim. Polyfon zwitschernd aßen Mäxchens Vögel Rüben, Joghurt und Quark. "Fix, Schwyz! " quäkt Jürgen blöd vom Paß. Victor jagt zwölf Boxkämpfer quer über den großen Sylter Deich. Falsches Üben von Xylophonmusik quält jeden größeren Zwerg. Heizölrückstoßabdämpfung. Zwei flinke Boxer jagen die quirlige Eva und ihren Mops durch Sylt. Franz jagt im komplett verwahrlosten Taxi quer durch Bayern. Zwölf Boxkämpfer jagen Viktor quer über den großen Sylter Deich. Vogel Quax zwickt Johnys Pferd Bim. Sylvia wagt quick den Jux bei Pforzheim. Polyfon zwitschernd aßen Mäxchens Vögel Rüben, Joghurt und Quark. "Fix, Schwyz! " quäkt Jürgen blöd vom Paß. Victor jagt zwölf Boxkämpfer quer über den großen Sylter Deich. Falsches Üben von Xylophonmusik quält jeden größeren Zwerg. Heizölrückstoßabdämpfung. Zwei flinke Boxer jagen die quirlige Eva und ihren Mops durch Sylt. Franz jagt im komplett verwahrlosten Taxi quer durch Bayern. Zwölf Boxkämpfer jagen Viktor quer</p>',
                },
                {
                    'id': 'affix-7',
                    'content': '<h2>Module 7</h2><p>Eine wunderbare Heiterkeit hat meine ganze Seele eingenommen, gleich den süßen Frühlingsmorgen, die ich mit ganzem Herzen genieße. Ich bin allein und freue mich meines Lebens in dieser Gegend, die für solche Seelen geschaffen ist wie die meine. Ich bin so glücklich, mein Bester, so ganz in dem Gefühle von ruhigem Dasein versunken, daß meine Kunst darunter leidet. Ich könnte jetzt nicht zeichnen, nicht einen Strich, und bin nie ein größerer Maler gewesen als in diesen Augenblicken.</p><p>Wenn das liebe Tal um mich dampft, und die hohe Sonne an der Oberfläche der undurchdringlichen Finsternis meines Waldes ruht, und nur einzelne Strahlen sich in das innere Heiligtum stehlen, ich dann im hohen Grase am fallenden Bache liege, und näher an der Erde tausend mannigfaltige Gräschen mir merkwürdig werden; wenn ich das Wimmeln der kleinen Welt zwischen Halmen, die unzähligen, unergründlichen Gestalten der Würmchen, der Mückchen näher an meinem Herzen fühle, und fühle die Gegenwart des Allmächtigen, der uns nach seinem Bilde schuf, das Wehen des Alliebenden, der uns in ewiger Wonne schwebend trägt und erhält; mein Freund!</p><p>Wenns dann um meine Augen dämmert, und die Welt um mich her und der Himmel ganz in meiner Seele ruhn wie die Gestalt einer Geliebten - dann sehne ich mich oft und denke : ach könntest du das wieder ausdrücken, könntest du dem Papiere das einhauchen, was so voll, so warm in dir lebt, daß es würde der Spiegel deiner Seele, wie deine Seele ist der Spiegel des unendlichen Gottes! - mein Freund - aber ich gehe darüber zugrunde, ich erliege unter der Gewalt der Herrlichkeit dieser Erscheinungen. Eine wunderbare Heiterkeit hat meine ganze Seele eingenommen, gleich den süßen Frühlingsmorgen, die ich mit ganzem Herzen genieße.</p><p>Ich bin allein und freue mich meines Lebens in dieser Gegend, die für solche Seelen geschaffen ist wie die meine. Ich bin so glücklich, mein Bester, so ganz in dem Gefühle von ruhigem Dasein versunken, daß meine Kunst darunter leidet. Ich könnte jetzt nicht zeichnen, nicht einen Strich, und bin nie ein größerer Maler gewesen als in diesen Augenblicken. Wenn das liebe Tal um mich dampft, und die hohe Sonne an der Oberfläche der undurchdringlichen Finsternis meines Waldes ruht, und nur einzelne Strahlen sich in das innere Heiligtum stehlen, ich dann im hohen Grase am fallenden Bache liege, und näher an der Erde tausend mannigfaltige Gräschen mir merkwürdig werden; wenn ich das Wimmeln der kleinen Welt zwischen Halmen, die unzähligen, unergründlichen Gestalten der Würmchen, der Mückchen näher an meinem Herzen fühle, und fühle die Gegenwart des Allmächtigen, der uns nach seinem Bilde schuf, das Wehen des Alliebenden, der uns in ewiger Wonne schwebend trägt und erhält; mein Freund! Wenns dann um meine Augen dämmert, und die Welt um mich her und der Himmel ganz in meiner Seele ruhn wie die Gestalt einer Geliebten - dann sehne ich mich oft und denke : ach könntest du das wieder ausdrücken, könntest du dem Papiere das einhauchen, was so voll, so warm in dir lebt, daß es würde der Spiegel deiner</p>',
                },
            ],
        },
    },
    'tab_infobox': {
        'name': 'Tab Infobox',
        'template': 'widgets/tab-infobox.html',
        'context': {
            'sidebar_links': [
                { 'href': '#tabinfobox-1', 'kicker': 'Module 1', 'text': 'Operational Strategy and Action plan', 'anchorlink': True, 'color': '#403D38', },
                { 'href': '#tabinfobox-2', 'kicker': 'Module 2', 'text': 'National and Subnational Level', 'anchorlink': True, 'color': '#6E3237', },
                { 'href': '#tabinfobox-3', 'kicker': 'Module 3', 'text': 'Landscape Level', 'anchorlink': True, 'color': '#604F3B', },
                { 'href': '#tabinfobox-4', 'kicker': 'Module 4', 'text': 'Sea Level', 'anchorlink': True, 'color': '#3B482E', },
                { 'href': '#tabinfobox-5', 'kicker': 'Module 5', 'text': 'SLM Territorial Planning', 'anchorlink': True, 'color': '#22454E', },
                { 'href': '#tabinfobox-6', 'kicker': 'Module 6', 'text': 'Implementation and scaling out', 'anchorlink': True, 'color': '#2D446B', },
                { 'href': '#tabinfobox-7', 'kicker': 'Module 7', 'text': 'Knowledge management platform for informed decision making', 'anchorlink': True, 'color': '#3A3451', },
            ],
            'sections': [
                {
                    'id': 'tabinfobox-1',
                    'content': '<h2>Module 1</h2><p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus.</p><p>Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Fusce vulputate eleifend sapien.</p><p>Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Nullam accumsan lorem in dui. Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ac dui quis mi consectetuer lacinia. Nam pretium turpis et arcu. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis, ipsum. Sed aliquam ultrices mauris. Integer ante arcu, accumsan a, consectetuer eget, posuere ut, mauris. Praesent adipiscing. Phasellus ullamcorper ipsum rutrum nunc. Nunc nonummy metus. Vestibulum volutpat pretium libero. Cras id dui. Aenean ut eros et nisl sagittis vestibulum. Nullam nulla eros, ultricies sit amet, nonummy id, imperdiet feugiat, pede.</p><p>Sed lectus. Donec mollis hendrerit risus. Phasellus nec sem in justo pellentesque facilisis. Etiam imperdiet imperdiet orci. Nunc nec neque. Phasellus leo dolor, tempus non, auctor et, hendrerit quis, nisi. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet, leo. Maecenas malesuada. Praesent congue erat at massa. Sed cursus turpis vitae tortor. Donec posuere vulputate arcu. Phasellus accumsan cursus velit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed aliquam, nisi quis porttitor congue, elit erat euismod orci, ac placerat dolor lectus quis orci. Phasellus consectetuer vestibulum elit. Aenean tellus metus, bibendum sed, posuere ac, mattis non, nunc. Vestibulum fringilla pede sit amet augue. In turpis. Pellentesque posuere. Praesent turpis. Aenean posuere, tortor sed cursus feugiat, nunc augue blandit nunc, eu sollicitudin urna dolor sagittis lacus. Donec elit libero, sodales nec, volutpat a, suscipit non, turpis. Nullam sagittis. Suspendisse pulvinar, augue ac venenatis condimentum, sem libero volutpat nibh, nec pellentesque velit pede quis nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Fusce id purus. Ut varius tincidunt libero. Phasellus dolor. Maecenas vestibulum mollis</p>',
                },
                {
                    'id': 'tabinfobox-2',
                    'content': '<h2>Module 2</h2><p>Omnicos directe al desirabilite de un nov lingua franca: On refusa continuar payar custosi traductores. At solmen va esser necessi far uniform grammatica, pronunciation e plu sommun paroles. Ma quande lingues coalesce, li grammatica del resultant lingue es plu simplic e regulari quam ti del coalescent lingues. Li nov lingua franca va esser plu simplic e regulari quam li existent Europan lingues.</p>',
                },
                {
                    'id': 'tabinfobox-3',
                    'content': '<h2>Module 3</h2><p>Eine wunderbare Heiterkeit hat meine ganze Seele eingenommen, gleich den süßen Frühlingsmorgen, die ich mit ganzem Herzen genieße. Ich bin allein und freue mich meines Lebens in dieser Gegend, die für solche Seelen geschaffen ist wie die meine. Ich bin so glücklich, mein Bester, so ganz in dem Gefühle von ruhigem Dasein versunken, daß meine Kunst darunter leidet. Ich könnte jetzt nicht zeichnen, nicht einen Strich, und bin nie ein größerer Maler gewesen als in diesen Augenblicken.</p><p>Wenn das liebe Tal um mich dampft, und die hohe Sonne an der Oberfläche der undurchdringlichen Finsternis meines Waldes ruht, und nur einzelne Strahlen sich in das innere Heiligtum stehlen, ich dann im hohen Grase am fallenden Bache liege, und näher an der Erde tausend mannigfaltige Gräschen mir merkwürdig werden; wenn ich das Wimmeln der kleinen Welt zwischen Halmen, die unzähligen, unergründlichen Gestalten der Würmchen, der Mückchen näher an meinem Herzen fühle, und fühle die Gegenwart des Allmächtigen, der uns nach seinem Bilde schuf, das Wehen des Alliebenden, der uns in ewiger Wonne schwebend trägt und erhält; mein Freund!</p><p>Wenns dann um meine Augen dämmert, und die Welt um mich her und der Himmel ganz in meiner Seele ruhn wie die Gestalt einer Geliebten - dann sehne ich mich oft und denke : ach könntest du das wieder ausdrücken, könntest du dem Papiere das einhauchen, was so voll, so warm in dir lebt, daß es würde der Spiegel deiner Seele, wie deine Seele ist der Spiegel des unendlichen Gottes! - mein Freund - aber ich gehe darüber zugrunde, ich erliege unter der Gewalt der Herrlichkeit dieser Erscheinungen. Eine wunderbare Heiterkeit hat meine ganze Seele eingenommen, gleich den süßen Frühlingsmorgen, die ich mit ganzem Herzen genieße.</p><p>Ich bin allein und freue mich meines Lebens in dieser Gegend, die für solche Seelen geschaffen ist wie die meine. Ich bin so glücklich, mein Bester, so ganz in dem Gefühle von ruhigem Dasein versunken, daß meine Kunst darunter leidet. Ich könnte jetzt nicht zeichnen, nicht einen Strich, und bin nie ein größerer Maler gewesen als in diesen Augenblicken. Wenn das liebe Tal um mich dampft, und die hohe Sonne an der Oberfläche der undurchdringlichen Finsternis meines Waldes ruht, und nur einzelne Strahlen sich in das innere Heiligtum stehlen, ich dann im hohen Grase am fallenden Bache liege, und näher an der Erde tausend mannigfaltige Gräschen mir merkwürdig werden; wenn ich das Wimmeln der kleinen Welt zwischen Halmen, die unzähligen, unergründlichen Gestalten der Würmchen, der Mückchen näher an meinem Herzen fühle, und fühle die Gegenwart des Allmächtigen, der uns nach seinem Bilde schuf, das Wehen des Alliebenden, der uns in ewiger Wonne schwebend trägt und erhält; mein Freund! Wenns dann um meine Augen dämmert, und die Welt um mich her und der Himmel ganz in meiner Seele ruhn wie die Gestalt einer Geliebten - dann sehne ich mich oft und denke : ach könntest du das wieder ausdrücken, könntest du dem Papiere das einhauchen, was so voll, so warm in dir lebt, daß es würde der Spiegel deiner</p>',
                },
                {
                    'id': 'tabinfobox-4',
                    'content': '<h2>Module 4</h2><p>Jemand musste Josef K. verleumdet haben, denn ohne dass er etwas Böses getan hätte, wurde er eines Morgens verhaftet. »Wie ein Hund! « sagte er, es war, als sollte die Scham ihn überleben. Als Gregor Samsa eines Morgens aus unruhigen Träumen erwachte, fand er sich in seinem Bett zu einem ungeheueren Ungeziefer verwandelt. Und es war ihnen wie eine Bestätigung ihrer neuen Träume und guten Absichten, als am Ziele ihrer Fahrt die Tochter als erste sich erhob und ihren jungen Körper dehnte. »Es ist ein eigentümlicher Apparat«, sagte der Offizier zu dem Forschungsreisenden und überblickte mit einem gewissermaßen bewundernden Blick den ihm doch wohlbekannten Apparat.</p><p>Sie hätten noch ins Boot springen können, aber der Reisende hob ein schweres, geknotetes Tau vom Boden, drohte ihnen damit und hielt sie dadurch von dem Sprunge ab. In den letzten Jahrzehnten ist das Interesse an Hungerkünstlern sehr zurückgegangen. Aber sie überwanden sich, umdrängten den Käfig und wollten sich gar nicht fortrühren. Jemand musste Josef K. verleumdet haben, denn ohne dass er etwas Böses getan hätte, wurde er eines Morgens verhaftet. »Wie ein Hund! « sagte er, es war, als sollte die Scham ihn überleben. Als Gregor Samsa eines Morgens aus unruhigen Träumen erwachte, fand er sich in seinem Bett zu einem ungeheueren Ungeziefer verwandelt.</p><p>Und es war ihnen wie eine Bestätigung ihrer neuen Träume und guten Absichten, als am Ziele ihrer Fahrt die Tochter als erste sich erhob und ihren jungen Körper dehnte. »Es ist ein eigentümlicher Apparat«, sagte der Offizier zu dem Forschungsreisenden und überblickte mit einem gewissermaßen bewundernden Blick den ihm doch wohlbekannten Apparat. Sie hätten noch ins Boot springen können, aber der Reisende hob ein schweres, geknotetes Tau vom Boden, drohte ihnen damit und hielt sie dadurch von dem Sprunge ab. In den letzten Jahrzehnten ist das Interesse an Hungerkünstlern sehr zurückgegangen. Aber sie überwanden sich, umdrängten den Käfig und wollten sich gar nicht fortrühren.</p><p>Jemand musste Josef K. verleumdet haben, denn ohne dass er etwas Böses getan hätte, wurde er eines Morgens verhaftet. »Wie ein Hund! « sagte er, es war, als sollte die Scham ihn überleben. Als Gregor Samsa eines Morgens aus unruhigen Träumen erwachte, fand er sich in seinem Bett zu einem ungeheueren Ungeziefer verwandelt. Und es war ihnen wie eine Bestätigung ihrer neuen Träume und guten Absichten, als am Ziele ihrer Fahrt die Tochter als erste sich erhob und ihren jungen Körper dehnte. »Es ist ein eigentümlicher Apparat«, sagte der Offizier zu dem Forschungsreisenden und überblickte mit einem gewissermaßen bewundernden Blick den ihm doch wohlbekannten Apparat. Sie hätten noch ins Boot springen können, aber der Reisende hob ein schweres, geknotetes Tau vom Boden, drohte ihnen damit und hielt sie dadurch von dem Sprunge ab. In den letzten Jahrzehnten ist das Interesse an Hungerkünstlern sehr zurückgegangen. Aber sie überwanden sich, umdrängten den Käfig und wollten sich gar nicht fortrühren. Jemand musste Josef K. verleumdet haben, denn ohne dass er etwas Böses getan hätte, wurde er eines Morgens verhaftet. »Wie ein Hund! « sagte er, es war, als sollte die Scham ihn überleben.</p>',
                },
                {
                    'id': 'tabinfobox-5',
                    'content': '<h2>Module 5</h2><p>Es gibt im Moment in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern. Letzte Spiel hatten wir in Platz drei Spitzen: Elber, Jancka und dann Zickler. Wir müssen nicht vergessen Zickler. Zickler ist eine Spitzen mehr, Mehmet eh mehr Basler. Ist klar diese Wörter, ist möglich verstehen, was ich hab gesagt? Danke. Offensiv, offensiv ist wie machen wir in Platz.</p><p>Zweitens: ich habe erklärt mit diese zwei Spieler: nach Dortmund brauchen vielleicht Halbzeit Pause. Ich habe auch andere Mannschaften gesehen in Europa nach diese Mittwoch. Ich habe gesehen auch zwei Tage die Training. Ein Trainer ist nicht ein Idiot! Ein Trainer sei sehen was passieren in Platz. In diese Spiel es waren zwei, drei diese Spieler waren schwach wie eine Flasche leer! Haben Sie gesehen Mittwoch, welche Mannschaft hat gespielt Mittwoch? Hat gespielt Mehmet oder gespielt Basler oder hat gespielt Trapattoni? Diese Spieler beklagen mehr als sie spielen! Wissen Sie, warum die Italienmannschaften kaufen nicht diese Spieler? Weil wir haben gesehen viele Male solche Spiel!</p><p>Haben gesagt sind nicht Spieler für die italienisch Meisters! Strunz! Strunz ist zwei Jahre hier, hat gespielt 10 Spiele, ist immer verletzt! Was erlauben Strunz? Letzte Jahre Meister Geworden mit Hamann, eh, Nerlinger. Diese Spieler waren Spieler! Waren Meister geworden! Ist immer verletzt! Hat gespielt 25 Spiele in diese Mannschaft in diese Verein. Muß respektieren die andere Kollegen! haben viel nette kollegen! Stellen Sie die Kollegen die Frage! Haben keine Mut an Worten, aber ich weiß, was denken über diese Spieler. Mussen zeigen jetzt, ich will, Samstag, diese Spieler müssen zeigen mich, seine Fans, müssen alleine die Spiel gewinnen. Muß allein die Spiel gewinnen!</p><p>Ich bin müde jetzt Vater diese Spieler, eh der Verteidiger diese Spieler. Ich habe immer die Schuld über diese Spieler. Einer ist Mario, einer andere ist Mehmet! Strunz ich spreche nicht, hat gespielt nur 25 Prozent der Spiel. Ich habe fertig! . . . wenn es gab Fragen, ich kann Worte wiederholen. . . Es gibt im Moment in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern. Letzte Spiel hatten wir in Platz drei Spitzen: Elber, Jancka und dann Zickler. Wir müssen nicht vergessen Zickler. Zickler ist eine Spitzen mehr, Mehmet eh mehr Basler. Ist klar diese Wörter, ist möglich verstehen, was ich hab gesagt? Danke. Offensiv, offensiv ist wie machen wir in Platz. Zweitens: ich habe erklärt mit diese zwei Spieler: nach Dortmund brauchen vielleicht Halbzeit Pause. Ich habe auch andere Mannschaften gesehen in Europa nach diese Mittwoch. Ich habe gesehen auch zwei Tage die Training. Ein Trainer ist nicht ein Idiot! Ein Trainer sei sehen was passieren in Platz. In diese Spiel es waren zwei, drei</p>',
                },
                {
                    'id': 'tabinfobox-6',
                    'content': '<h2>Module 6</h2><p>Zwei flinke Boxer jagen die quirlige Eva und ihren Mops durch Sylt. Franz jagt im komplett verwahrlosten Taxi quer durch Bayern.</p>',
                },
                {
                    'id': 'tabinfobox-7',
                    'content': '<h2>Module 7</h2><p>Eine wunderbare Heiterkeit hat meine ganze Seele eingenommen, gleich den süßen Frühlingsmorgen, die ich mit ganzem Herzen genieße. Ich bin allein und freue mich meines Lebens in dieser Gegend, die für solche Seelen geschaffen ist wie die meine. Ich bin so glücklich, mein Bester, so ganz in dem Gefühle von ruhigem Dasein versunken, daß meine Kunst darunter leidet. Ich könnte jetzt nicht zeichnen, nicht einen Strich, und bin nie ein größerer Maler gewesen als in diesen Augenblicken.</p><p>Wenn das liebe Tal um mich dampft, und die hohe Sonne an der Oberfläche der undurchdringlichen Finsternis meines Waldes ruht, und nur einzelne Strahlen sich in das innere Heiligtum stehlen, ich dann im hohen Grase am fallenden Bache liege, und näher an der Erde tausend mannigfaltige Gräschen mir merkwürdig werden; wenn ich das Wimmeln der kleinen Welt zwischen Halmen, die unzähligen, unergründlichen Gestalten der Würmchen, der Mückchen näher an meinem Herzen fühle, und fühle die Gegenwart des Allmächtigen, der uns nach seinem Bilde schuf, das Wehen des Alliebenden, der uns in ewiger Wonne schwebend trägt und erhält; mein Freund!</p><p>Wenns dann um meine Augen dämmert, und die Welt um mich her und der Himmel ganz in meiner Seele ruhn wie die Gestalt einer Geliebten - dann sehne ich mich oft und denke : ach könntest du das wieder ausdrücken, könntest du dem Papiere das einhauchen, was so voll, so warm in dir lebt, daß es würde der Spiegel deiner Seele, wie deine Seele ist der Spiegel des unendlichen Gottes! - mein Freund - aber ich gehe darüber zugrunde, ich erliege unter der Gewalt der Herrlichkeit dieser Erscheinungen. Eine wunderbare Heiterkeit hat meine ganze Seele eingenommen, gleich den süßen Frühlingsmorgen, die ich mit ganzem Herzen genieße.</p><p>Ich bin allein und freue mich meines Lebens in dieser Gegend, die für solche Seelen geschaffen ist wie die meine. Ich bin so glücklich, mein Bester, so ganz in dem Gefühle von ruhigem Dasein versunken, daß meine Kunst darunter leidet. Ich könnte jetzt nicht zeichnen, nicht einen Strich, und bin nie ein größerer Maler gewesen als in diesen Augenblicken. Wenn das liebe Tal um mich dampft, und die hohe Sonne an der Oberfläche der undurchdringlichen Finsternis meines Waldes ruht, und nur einzelne Strahlen sich in das innere Heiligtum stehlen, ich dann im hohen Grase am fallenden Bache liege, und näher an der Erde tausend mannigfaltige Gräschen mir merkwürdig werden; wenn ich das Wimmeln der kleinen Welt zwischen Halmen, die unzähligen, unergründlichen Gestalten der Würmchen, der Mückchen näher an meinem Herzen fühle, und fühle die Gegenwart des Allmächtigen, der uns nach seinem Bilde schuf, das Wehen des Alliebenden, der uns in ewiger Wonne schwebend trägt und erhält; mein Freund! Wenns dann um meine Augen dämmert, und die Welt um mich her und der Himmel ganz in meiner Seele ruhn wie die Gestalt einer Geliebten - dann sehne ich mich oft und denke : ach könntest du das wieder ausdrücken, könntest du dem Papiere das einhauchen, was so voll, so warm in dir lebt, daß es würde der Spiegel deiner</p>',
                },
            ],
        },
    },
}
