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
                    { 'href': 'http://google.de/1', 'text': 'Get involved' },
                    { 'href': 'http://bing.de/2', 'text': 'FAQ' },
                    { 'href': 'http://bing.de/3', 'text': 'Glossary', },
                    { 'href': 'http://bing.de/2', 'text': 'Login' },
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

    'carousel': {
        'name': 'Carousel',
        'template': 'widgets/carousel.html',
        'context': {
            'id': 1,
            'items': [
                { 'src': '/static/styleguide/test-images/header1-3by1.jpg' },
                { 'src': '/static/styleguide/test-images/header2-3by1.jpg' },
                { 'src': '/static/styleguide/test-images/header3-3by1.jpg' },
                { 'src': '/static/styleguide/test-images/header4-3by1.jpg' },
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
                { 'src': '/static/styleguide/test-images/header1-3by1.jpg' },
                { 'src': '/static/styleguide/test-images/header2-3by1.jpg' },
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
    'heading2_news': {
        'name': 'Heading 2 News',
        'template': 'widgets/heading2.html',
        'context': {
            'text': 'News',
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
            'description': 'Es gibt im Moment in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
            'readmorelink': {
                'text': 'read more',
            },
        },
    },
    'teaser_home_globalissues': {
        'name': 'Teaser with no image',
        'template': 'widgets/teaser.html',
        'context': {
            'href': 'http://sinnwerkstatt.com',
            'description': 'Es gibt im Moment in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
            'readmorelink': {
                'text': 'Read more about Global Issues',
            },
             'lines': True,
        },
    },
    'teaser_lines': {
        'name': 'Teaser with lines',
        'template': 'widgets/teaser.html',
        'context': {
            'href': 'http://sinnwerkstatt.com',
            'title': 'Lorem Titel-Ipsum vom Dolor und Amet auch',
            'lines': True,
            'description': 'Es gibt im Moment in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
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
            'description': 'Es gibt im Moment in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
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
            'description': 'Es gibt im Moment in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
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
            'imgsrc': '/static/styleguide/test-images/header1-3by1.jpg',
            'description': 'Es gibt im Moment in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
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
            'description': 'Es gibt im Moment in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
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
            'description': 'Es gibt im Moment in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
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
            'imgpos': 'top',
            'date': '24. April 2016',
            'imgsrc': '/static/styleguide/test-images/header4.jpg',
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
            'description': 'Es gibt im Moment in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
            'readmorelink': {
                'text': 'read more',
            },
        },
    },
    'teaser_super_leftimg': {
        'name': 'Super Teaser with left image',
        'template': 'widgets/teaser-super.html',
        'context': {
            'backgroundimagesrc': '/static/styleguide/test-images/header3.jpg',
            'imgpos': 'left',
            'imgsrc': '/static/styleguide/test-images/header4.jpg',
            'href': 'http://sinnwerkstatt.com',
            'date': '24. April 2016',
            'title': 'Lorem Titel-Ipsum vom Dolor und Amet auch',
            'description': 'Es gibt im Moment in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
            'readmorelink': {
                'text': 'read more',
            },
        },
    },
    'teaser_super_leftimg_nobackground': {
        'name': 'Super Teaser with left image without background',
        'template': 'widgets/teaser-super.html',
        'context': {
            'imgpos': 'left',
            'imgsrc': '/static/styleguide/test-images/header4.jpg',
            'href': 'http://sinnwerkstatt.com',
            'date': '24. April 2016',
            'title': 'Lorem Titel-Ipsum vom Dolor und Amet auch',
            'description': 'Es gibt im Moment in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
            'readmorebutton': {
                'text': 'read more',
            },
        },
    },
    'teaser_super_narrow': {
        'name': 'Super Teaser Narrow',
        'template': 'widgets/teaser-super-narrow.html',
        'context': {
            'backgroundimagesrc': '/static/styleguide/test-images/header3.jpg',
            'href': 'http://sinnwerkstatt.com',
            'date': '24. April 2016',
            'title': 'Lorem Titel-Ipsum vom Dolor und Amet auch',
            'description': 'Es gibt im Moment in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
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
            'description': 'Es gibt im Moment in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
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
            'lead': 'Es gibt im Moment in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen.',
        },
    },

    'page_lead_overlay_home': {
        'name': 'Page Lead Overlay',
        'template': 'widgets/page-lead-overlay.html',
        'context': {
            'heading': 'Wocat',
            'lead': 'Es gibt im Moment in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen.',
        },
    },

    'page_lead_overlay_noimage': {
        'name': 'Page Lead Overlay',
        'template': 'widgets/page-lead-overlay.html',
        'context': {
            'noimage': True,
            'heading': 'Page Head without image overlay',
            'lead': 'Es gibt im Moment in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen.',
        },
    },

    'page_lead_overlay_noimage_alternative': {
        'name': 'Page Lead Overlay',
        'template': 'widgets/page-lead-overlay.html',
        'context': {
            'noimage': True,
            'heading': 'Page Head without image overlay',
            'heading_iconsrc': '/static/styleguide/test-images/dog-1by1.jpg',
            'content': '<div class="row"><div class="col-sm-6">Linke Zahl: <strong>5m</strong></div><div class="col-sm-6">Rechte Zahl: <strong>100km</strong></div></div>',
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
            'src': '/static/styleguide/test-images/header1.jpg',
            'caption': 'This is the description of the image. This is the description of the image. This is the description of the image. This is the description of the image. This is the description of the image.',
            'href': 'http://xxx',
        },
    },

    'image': {
        'name': 'Image',
        'template': 'widgets/image.html',
        'context': {
            'src': '/static/styleguide/test-images/header1.jpg',
            'caption': 'This is the description of the image. This is the description of the image. This is the description of the image. This is the description of the image. This is the description of the image.',
            'href': 'http://xxx',
        },
    },
    'image_overlaycaption': {
        'name': 'Image with Overlaycaption',
        'template': 'widgets/image.html',
        'context': {
            'src': '/static/styleguide/test-images/header1.jpg',
            'overlay': {
                'date': '15. Juni 2016',
                'heading': 'Bodo Bagger',
                'text': 'This is the description of the image. This is the description of the image. This is the description of the image. This is the description of the image. This is the description of the image.',
                'links': [
                    { 'href': 'http://google.de', 'text': 'Google', },
                    { 'href': 'http://facebook.de', 'text': 'Facebook', },
                    { 'href': 'http://bing.de', 'text': 'Bing', },
                ],
            },
            'href': 'http://xxx',
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
    'readmorelink_right': {
        'name': 'Read more link – right align',
        'template': 'widgets/read-more-link.html',
        'context': {
            'text': 'weiterlesen',
            'href': 'http://x',
            'align': 'right',
        },
    },


    'richtext': {
        'name': 'Richtext',
        'template': 'widgets/richtext.html',
        'context': {
            'content':'<p><img class="filer_image right" alt="2015-09-10.jpg" src="/static/styleguide/test-images/header3.jpg" /></p><ul><li>Erster Punkt der Aufzählung</li><li>Zweiter Punkt der Aufzählung. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste. Dieser Punkt ist länger als der erste.</li><li>Dritter Punkt der Aufzählung</li></ul><p><img class="filer_image " alt="2015-09-10.jpg" src="/static/styleguide/test-images/header3.jpg" /></p><p>Jemand musste Josef K. verleumdet haben, denn ohne dass er etwas Böses getan hätte, wurde er <a href="http://127.0.0.1:8000/#">eines Morgens</a> verhaftet. »Wie ein Hund!« sagte er, es war, als sollte die Scham ihn überleben. Als Gregor Samsa eines Morgens aus unruhigen Träumen erwachte, fand er sich in seinem Bett zu einem ungeheueren Ungeziefer verwandelt. Und es war ihnen wie eine Bestätigung ihrer neuen Träume und guten Absichten, als am Ziele ihrer Fahrt die Tochter als erste sich erhob und ihren jungen Körper dehnte. »Es ist ein eigentümlicher Apparat«, sagte der Offizier zu dem Forschungsreisenden und überblickte mit einem gewissermaßen bewundernden Blick den ihm doch wohlbekannten Apparat. Sie hätten noch ins Boot springen können, aber der Reisende hob ein schweres, geknotetes Tau vom Boden, drohte ihnen damit und hielt sie dadurch von dem Sprunge ab.</p>',
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
            'countries': [
                { 'name': 'Germany', },
                { 'name': 'Niger', },
                { 'name': 'Toga', },
            ],
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
                    'name': 'Eraldo',
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
    'sidebar': {
        'name': 'Sidebar',
        'template': 'widgets/sidebar.html',
        'context': {
            'links': [
                { 'href': '#', 'text': 'Headings', 'anchorlink': True },
                { 'href': '#', 'text': 'Teaser', 'anchorlink': True },
                { 'href': '#', 'text': 'Richtext', 'anchorlink': True },
                { 'href': '#', 'text': 'Forms', 'anchorlink': True },
            ],
        },
    },
    'button': {
        'name': 'Button',
        'template': 'widgets/button.html',
        'context': {
            'text': 'Use the framework',
            'href': 'http://google.de',
        },
    },
    'button_center': {
        'name': 'Button Centered',
        'template': 'widgets/button.html',
        'context': {
            'center': True,
            'text': 'Use the framework',
            'href': 'http://google.de',
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
                { 'href': 'http://bing.de/2', 'text': 'Imprint', },
                { 'href': 'http://bing.de/2', 'text': 'Contact', },

            ],
        },
    },
}
