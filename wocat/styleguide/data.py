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
                { 'url': 'http://google.de/1', 'text': '<i class="fa fa-facebook" aria-hidden="true"></i>' },
                { 'url': 'http://bing.de/2', 'text': '<i class="fa fa-youtube" aria-hidden="true"></i>' },
                { 'url': 'http://bing.de/3', 'text': '<i class="fa fa-twitter" aria-hidden="true"></i>' },
                { 'url': 'http://google.de/1', 'text': 'Get involved' },
                { 'url': 'http://bing.de/2', 'text': 'FAQ' },
                { 'url': 'http://bing.de/3', 'text': 'Glossary', 'active': True, },
                { 'url': 'http://bing.de/2', 'text': 'Login' },
                {
                    'dropdown': True,
                    'text': 'EN',
                    'links': [
                        { 'url': 'http://google.de/1', 'text': 'DE', 'active': True, },
                        { 'url': 'http://bing.de/2', 'text': 'FR' },
                    ]
                },
                { 'url': 'http://bing.de/2', 'text': '<i class="fa fa-search" aria-hidden="true"></i>' },
            ],
            'mainnav': {
                'depth': 1,
                'brand2': {
                    'src': '/static/styleguide/test-images/dog-1by1.jpg',
                    'name': 'Yolo-Projekt',
                    'href': 'zurück',
                },

                'links1': [
                    { 'url': 'http://google.de/1', 'text': 'Get involved' },
                    { 'url': 'http://bing.de/2', 'text': 'FAQ' },
                    { 'url': 'http://bing.de/3', 'text': 'Glossary', 'active': True, },
                    { 'url': 'http://bing.de/2', 'text': 'Login' },
                    {
                        'dropdown': True,
                        'text': 'Yolo',
                        'links': [
                            { 'url': 'http://google.de/1', 'text': 'Swag', 'active': True, },
                            { 'url': 'http://bing.de/2', 'text': 'More Swag' },
                        ],
                    },
                ],
                'links2': [
                    { 'url': 'http://google.de/1', 'text': 'About' },
                    { 'url': 'http://bing.de/2', 'text': 'Using the framework' },
                    { 'url': 'http://bing.de/3', 'text': 'Countries', 'active': True, },
                    { 'url': 'http://bing.de/2', 'text': 'News and Events' },
                    {
                        'dropdown': True,
                        'text': 'Yolo',
                        'links': [
                            { 'url': 'http://google.de/1', 'text': 'News', 'active': True, },
                            { 'url': 'http://bing.de/2', 'text': 'Events' },
                        ],
                    },
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
                { 'url': 'http://google.de/1', 'text': '<i class="fa fa-facebook" aria-hidden="true"></i>' },
                { 'url': 'http://bing.de/2', 'text': '<i class="fa fa-youtube" aria-hidden="true"></i>' },
                { 'url': 'http://bing.de/3', 'text': '<i class="fa fa-twitter" aria-hidden="true"></i>' },
                { 'url': 'http://google.de/1', 'text': 'Get involved' },
                { 'url': 'http://bing.de/2', 'text': 'FAQ' },
                { 'url': 'http://bing.de/3', 'text': 'Glossary', 'active': True, },
                { 'url': 'http://bing.de/2', 'text': 'Login' },
                {
                    'dropdown': True,
                    'text': 'EN',
                    'links': [
                        { 'url': 'http://google.de/1', 'text': 'DE', 'active': True, },
                        { 'url': 'http://bing.de/2', 'text': 'FR' },
                    ]
                },
                { 'url': 'http://bing.de/2', 'text': '<i class="fa fa-search" aria-hidden="true"></i>' },
            ],
            'mainnav': {
                'depth': 2,
                'brand2': {
                    'src': '/static/styleguide/test-images/dog-1by1.jpg',
                    'name': 'Yolo-Projekt',
                    'href': 'zurück',
                },

                'links1': [
                    { 'url': 'http://google.de/1', 'text': 'Get involved' },
                    { 'url': 'http://bing.de/2', 'text': 'FAQ' },
                    { 'url': 'http://bing.de/3', 'text': 'Glossary', 'active': True, },
                    { 'url': 'http://bing.de/2', 'text': 'Login' },
                    {
                        'dropdown': True,
                        'text': 'Yolo',
                        'links': [
                            { 'url': 'http://google.de/1', 'text': 'Swag', 'active': True, },
                            { 'url': 'http://bing.de/2', 'text': 'More Swag' },
                        ],
                    },
                ],
                'links2': [
                    { 'url': 'http://google.de/1', 'text': 'About' },
                    { 'url': 'http://bing.de/2', 'text': 'Using the framework' },
                    { 'url': 'http://bing.de/3', 'text': 'Countries', 'active': True, },
                    { 'url': 'http://bing.de/2', 'text': 'News and Events' },
                    {
                        'dropdown': True,
                        'text': 'Yolo',
                        'links': [
                            { 'url': 'http://google.de/1', 'text': 'News', 'active': True, },
                            { 'url': 'http://bing.de/2', 'text': 'Events' },
                        ],
                    },
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
            'readmoretext': 'read more &gt;',
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
            'description': 'Es gibt im Moment in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern.',
            'readmoretext': 'read more &gt;',
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
            'readmoretext': 'read more &gt;',
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
            'readmoretext': 'read more &gt;',
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

    'image': {
        'name': 'Image',
        'template': 'widgets/image.html',
        'context': {
            'src': '/static/styleguide/test-images/header1.jpg',
            'caption': 'This is the description of the image. This is the description of the image. This is the description of the image. This is the description of the image. This is the description of the image.',
            'href': 'http://xxx',
        },
    },

    'readmorelink': {
        'name': 'Read more link',
        'template': 'widgets/read-more-link.html',
        'context': {
            'text': 'weiterlesen',
            'url': 'http://x',
        },
    },
    'readmorelink_right': {
        'name': 'Read more link – right align',
        'template': 'widgets/read-more-link.html',
        'context': {
            'text': 'weiterlesen',
            'url': 'http://x',
            'align': 'right',
        },
    },


    'richtext': {
        'name': 'Richtext',
        'template': 'widgets/richtext-content.html',
        'context': {
            'content': '<div class="rich-text"><p><img class="richtext-image right" src="/static/styleguide/test-images/header3.jpg" alt="Schönes Bild">Jemand musste Josef K. verleumdet haben, denn ohne dass er etwas Böses getan hätte, wurde er <a href="#">eines Morgens</a> verhaftet. »Wie ein Hund!« sagte er, es war, als sollte die Scham ihn überleben. Als Gregor Samsa eines Morgens aus unruhigen Träumen erwachte, fand er sich in seinem Bett zu einem ungeheueren Ungeziefer verwandelt. Und es war ihnen wie eine Bestätigung ihrer neuen Träume und guten Absichten, als am Ziele ihrer Fahrt die Tochter als erste sich erhob und ihren jungen Körper dehnte. »Es ist ein eigentümlicher Apparat«, sagte der Offizier zu dem Forschungsreisenden und überblickte mit einem gewissermaßen bewundernden Blick den ihm doch wohlbekannten Apparat. Sie hätten noch ins Boot springen können, aber der Reisende hob ein schweres, geknotetes Tau vom Boden, drohte ihnen damit und hielt sie dadurch von dem Sprunge ab.</p><div style="padding-bottom: 56.25%;" class="responsive-object"><iframe src="https://www.youtube.com/embed/SywPPK8ixiw?feature=oembed" allowfullscreen="" width="480" frameborder="0" height="270"></iframe></div><h3>Yolo!</h3><p>Jemand musste Josef K. verleumdet haben, denn ohne dass er etwas Böses getan hätte, wurde er eines Morgens verhaftet. »Wie ein Hund!« sagte er, es war, als sollte die Scham ihn überleben. Als Gregor Samsa eines Morgens aus unruhigen Träumen erwachte, fand er sich in seinem Bett zu einem ungeheueren Ungeziefer verwandelt. Und es war ihnen wie eine Bestätigung ihrer neuen Träume und guten Absichten, als am Ziele ihrer Fahrt die Tochter als erste sich erhob und ihren jungen Körper dehnte. »Es ist ein eigentümlicher Apparat«, sagte der Offizier zu dem Forschungsreisenden und überblickte mit einem gewissermaßen bewundernden Blick den ihm doch wohlbekannten Apparat. Sie hätten noch ins Boot springen können, aber der Reisende hob ein schweres, geknotetes Tau vom Boden, drohte ihnen damit und hielt sie dadurch von dem Sprunge ab.</p></div>',
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
                    'url': 'http://google.de',
                    'text': '1',
                },
                {
                    'url': '/glossar/',
                    'text': '2',
                },
                {
                    'active': True,
                    'url': 'http://google.ru',
                    'text': '3',
                },
                {
                    'url': 'http://google.ru',
                    'text': '4',
                },
                {
                    'url': 'http://google.ru',
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
            'pages': [1,2,3,4,5],
            'maxpagesize': 3,
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
                    'visible': True,
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
                    'visible': True,
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
                    'visible': True,
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
                    'visible': True,
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
                    'visible': True,
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
                    'visible': True,
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
                    'visible': True,
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
                    'visible': True,
                },
            ],
        },
    },
}
