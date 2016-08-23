# -*- coding: utf-8 -*-

data = {

    'image_gallery_verticalalign_home': {
        'name': 'Image Gallery Vertical Align Home',
        'template': 'widgets/image-gallery.html',
        'context': {
            'cols': 3,
            'verticalalign': True,
            'images': [
                {
                    'src': '/static/styleguide/test-images/consortium-partners/SDC.svg',
                    'shrink': 1,
                    'href': 'http://xxx1',
                },
                {
                    'src': '/static/styleguide/test-images/consortium-partners/CDE.svg',
                    'shrink': 3,
                },
                {
                    'src': '/static/styleguide/test-images/consortium-partners/FAO.svg',
                    'shrink': 2,
                    'href': 'http://yyy2',
                },
                {
                    'src': '/static/styleguide/test-images/consortium-partners/ISRIC.svg',
                    'href': 'http://xxx3',
                    'shrink': 1,
                },
                {
                    'src': '/static/styleguide/test-images/consortium-partners/CIAT.svg',
                    'shrink': 3,
                },
                {
                    'src': '/static/styleguide/test-images/consortium-partners/ICARDA.svg',
                    'href': 'http://yyy4',
                    'shrink': 2,
                },
                {
                    'src': '/static/styleguide/test-images/consortium-partners/ICIMOD.svg',
                    'href': 'http://yyy4',
                    'shrink': 3,
                },
                {
                    'src': '/static/styleguide/test-images/consortium-partners/GIZ.svg',
                    'href': 'http://yyy4',
                    'shrink': 2,
                },
            ],
        },
    },

    'teaser_home_media': {
        'name': 'Teaser with lines and top image',
        'template': 'widgets/teaser.html',
        'context': {
            'href': 'http://sinnwerkstatt.com',
            'imgpos': 'top',
            'imgsrc': '/static/styleguide/test-images/media.jpg',
            'description': 'Unsere Medien umfassen unter anderem globale Bücher, nationale Bücher, Videos und Trainings.',
            'readmorelink': {
                'text': 'show all media',
            },
        },
    },
    'teaser_home_wiki': {
        'name': 'Teaser with lines and top image',
        'template': 'widgets/teaser.html',
        'context': {
            'href': 'http://sinnwerkstatt.com',
            'imgpos': 'top',
            'external': True,
            'imgsrc': '/static/styleguide/test-images/wiki.jpg',
            'description': 'Das Wocat-Wiki enthält Wissen und Diskussionen.',
            'readmorelink': {
                'text': 'go to wiki',
            },
        },
    },

    'image_nocaption_square': {
        'name': 'Image',
        'template': 'widgets/image.html',
        'context': {
            'src': '/static/styleguide/test-images/global-issues-4by3.jpg',
        },
    },
    'consortiumpartners': {
        'name': 'Heading 3',
        'template': 'widgets/heading3.html',
        'context': {
            'text': 'Consortium Partners',
        },
    },
    'heading3_wiki': {
        'name': 'Heading 3 Media',
        'template': 'widgets/heading3.html',
        'context': {
            'text': 'Wiki',
        },
    },
}

