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
                    'src': '/static/styleguide/test-images/eidgenossen-logo.jpg',
                    'shrink': 0,
                    'href': 'http://xxx1',
                },
                {
                    'src': '/static/styleguide/test-images/uni-bern-logo.jpg',
                    'shrink': 2,
                },
                {
                    'src': '/static/styleguide/test-images/food-logo.jpg',
                    'shrink': 2,
                    'href': 'http://yyy2',
                },
                {
                    'src': '/static/styleguide/test-images/isric-logo.jpg',
                    'href': 'http://xxx3',
                    'shrink': 0,
                },
                {
                    'src': '/static/styleguide/test-images/ciat-logo.png',
                    'shrink': 2,
                },
                {
                    'src': '/static/styleguide/test-images/icarda-logo.jpg',
                    'href': 'http://yyy4',
                    'shrink': 1,
                },
                {
                    'src': '/static/styleguide/test-images/icimod-logo.jpg',
                    'href': 'http://yyy4',
                    'shrink': 1,
                },
                {
                    'src': '/static/styleguide/test-images/giz-logo.jpg',
                    'href': 'http://yyy4',
                    'shrink': 1,
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
            'title': 'Wiki',
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
            'src': '/static/styleguide/test-images/silhouette-1by1.jpg',
        },
    },
}

