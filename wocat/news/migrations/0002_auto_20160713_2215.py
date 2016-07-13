# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-13 20:15
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks
import wocat.cms.blocks
import wocat.news.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wocat.cms.blocks.HeadingBlock()), ('rich_text', wocat.cms.blocks.RichTextBlock()), ('image', wocat.cms.blocks.ImageBlock()), ('embed', wocat.cms.blocks.EmbedBlock()), ('read_more', wagtail.wagtailcore.blocks.StructBlock((('name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('button', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('teaser', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('content', wocat.cms.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('top', 'Top'), ('left', 'Left'), ('right', 'Right')], required=False)), ('large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))), required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('read_more_text', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('media_teaser', wagtail.wagtailcore.blocks.StructBlock((('media', wocat.cms.blocks.MediaChooserBlock(required=True)),))), ('image_gallery', wagtail.wagtailcore.blocks.StructBlock((('columns', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(6, '2'), (4, '3'), (3, '4')])), ('elements', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('description', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('shrink', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(1, 'Small'), (2, 'Extra small')], required=False))))))))), ('columns_1_to_1', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wocat.cms.blocks.HeadingBlock()), ('rich_text', wocat.cms.blocks.RichTextBlock()), ('image', wocat.cms.blocks.ImageBlock()), ('embed', wocat.cms.blocks.EmbedBlock()), ('read_more', wagtail.wagtailcore.blocks.StructBlock((('name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('button', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('teaser', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('content', wocat.cms.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('top', 'Top'), ('left', 'Left'), ('right', 'Right')], required=False)), ('large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))), required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('read_more_text', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('media_teaser', wagtail.wagtailcore.blocks.StructBlock((('media', wocat.cms.blocks.MediaChooserBlock(required=True)),))), ('image_gallery', wagtail.wagtailcore.blocks.StructBlock((('columns', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(6, '2'), (4, '3'), (3, '4')])), ('elements', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('description', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('shrink', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(1, 'Small'), (2, 'Extra small')], required=False)))))))))))), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wocat.cms.blocks.HeadingBlock()), ('rich_text', wocat.cms.blocks.RichTextBlock()), ('image', wocat.cms.blocks.ImageBlock()), ('embed', wocat.cms.blocks.EmbedBlock()), ('read_more', wagtail.wagtailcore.blocks.StructBlock((('name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('button', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('teaser', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('content', wocat.cms.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('top', 'Top'), ('left', 'Left'), ('right', 'Right')], required=False)), ('large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))), required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('read_more_text', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('media_teaser', wagtail.wagtailcore.blocks.StructBlock((('media', wocat.cms.blocks.MediaChooserBlock(required=True)),))), ('image_gallery', wagtail.wagtailcore.blocks.StructBlock((('columns', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(6, '2'), (4, '3'), (3, '4')])), ('elements', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('description', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('shrink', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(1, 'Small'), (2, 'Extra small')], required=False))))))))))))))), ('columns_1_to_2', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wocat.cms.blocks.HeadingBlock()), ('rich_text', wocat.cms.blocks.RichTextBlock()), ('image', wocat.cms.blocks.ImageBlock()), ('embed', wocat.cms.blocks.EmbedBlock()), ('read_more', wagtail.wagtailcore.blocks.StructBlock((('name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('button', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('teaser', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('content', wocat.cms.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('top', 'Top'), ('left', 'Left'), ('right', 'Right')], required=False)), ('large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))), required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('read_more_text', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('media_teaser', wagtail.wagtailcore.blocks.StructBlock((('media', wocat.cms.blocks.MediaChooserBlock(required=True)),))), ('image_gallery', wagtail.wagtailcore.blocks.StructBlock((('columns', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(6, '2'), (4, '3'), (3, '4')])), ('elements', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('description', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('shrink', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(1, 'Small'), (2, 'Extra small')], required=False)))))))))))), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wocat.cms.blocks.HeadingBlock()), ('rich_text', wocat.cms.blocks.RichTextBlock()), ('image', wocat.cms.blocks.ImageBlock()), ('embed', wocat.cms.blocks.EmbedBlock()), ('read_more', wagtail.wagtailcore.blocks.StructBlock((('name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('button', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('teaser', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('content', wocat.cms.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('top', 'Top'), ('left', 'Left'), ('right', 'Right')], required=False)), ('large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))), required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('read_more_text', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('media_teaser', wagtail.wagtailcore.blocks.StructBlock((('media', wocat.cms.blocks.MediaChooserBlock(required=True)),))), ('image_gallery', wagtail.wagtailcore.blocks.StructBlock((('columns', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(6, '2'), (4, '3'), (3, '4')])), ('elements', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('description', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('shrink', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(1, 'Small'), (2, 'Extra small')], required=False))))))))))))))), ('columns_2_to_1', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wocat.cms.blocks.HeadingBlock()), ('rich_text', wocat.cms.blocks.RichTextBlock()), ('image', wocat.cms.blocks.ImageBlock()), ('embed', wocat.cms.blocks.EmbedBlock()), ('read_more', wagtail.wagtailcore.blocks.StructBlock((('name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('button', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('teaser', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('content', wocat.cms.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('top', 'Top'), ('left', 'Left'), ('right', 'Right')], required=False)), ('large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))), required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('read_more_text', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('media_teaser', wagtail.wagtailcore.blocks.StructBlock((('media', wocat.cms.blocks.MediaChooserBlock(required=True)),))), ('image_gallery', wagtail.wagtailcore.blocks.StructBlock((('columns', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(6, '2'), (4, '3'), (3, '4')])), ('elements', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('description', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('shrink', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(1, 'Small'), (2, 'Extra small')], required=False)))))))))))), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wocat.cms.blocks.HeadingBlock()), ('rich_text', wocat.cms.blocks.RichTextBlock()), ('image', wocat.cms.blocks.ImageBlock()), ('embed', wocat.cms.blocks.EmbedBlock()), ('read_more', wagtail.wagtailcore.blocks.StructBlock((('name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('button', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('teaser', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('content', wocat.cms.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('top', 'Top'), ('left', 'Left'), ('right', 'Right')], required=False)), ('large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))), required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('read_more_text', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('media_teaser', wagtail.wagtailcore.blocks.StructBlock((('media', wocat.cms.blocks.MediaChooserBlock(required=True)),))), ('image_gallery', wagtail.wagtailcore.blocks.StructBlock((('columns', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(6, '2'), (4, '3'), (3, '4')])), ('elements', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('description', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('shrink', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(1, 'Small'), (2, 'Extra small')], required=False))))))))))))))), ('columns_1_to_1_to_1', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wocat.cms.blocks.HeadingBlock()), ('rich_text', wocat.cms.blocks.RichTextBlock()), ('image', wocat.cms.blocks.ImageBlock()), ('embed', wocat.cms.blocks.EmbedBlock()), ('read_more', wagtail.wagtailcore.blocks.StructBlock((('name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('button', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('teaser', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('content', wocat.cms.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('top', 'Top'), ('left', 'Left'), ('right', 'Right')], required=False)), ('large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))), required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('read_more_text', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('media_teaser', wagtail.wagtailcore.blocks.StructBlock((('media', wocat.cms.blocks.MediaChooserBlock(required=True)),))), ('image_gallery', wagtail.wagtailcore.blocks.StructBlock((('columns', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(6, '2'), (4, '3'), (3, '4')])), ('elements', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('description', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('shrink', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(1, 'Small'), (2, 'Extra small')], required=False)))))))))))), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wocat.cms.blocks.HeadingBlock()), ('rich_text', wocat.cms.blocks.RichTextBlock()), ('image', wocat.cms.blocks.ImageBlock()), ('embed', wocat.cms.blocks.EmbedBlock()), ('read_more', wagtail.wagtailcore.blocks.StructBlock((('name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('button', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('teaser', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('content', wocat.cms.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('top', 'Top'), ('left', 'Left'), ('right', 'Right')], required=False)), ('large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))), required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('read_more_text', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('media_teaser', wagtail.wagtailcore.blocks.StructBlock((('media', wocat.cms.blocks.MediaChooserBlock(required=True)),))), ('image_gallery', wagtail.wagtailcore.blocks.StructBlock((('columns', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(6, '2'), (4, '3'), (3, '4')])), ('elements', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('description', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('shrink', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(1, 'Small'), (2, 'Extra small')], required=False)))))))))))), ('middle_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wocat.cms.blocks.HeadingBlock()), ('rich_text', wocat.cms.blocks.RichTextBlock()), ('image', wocat.cms.blocks.ImageBlock()), ('embed', wocat.cms.blocks.EmbedBlock()), ('read_more', wagtail.wagtailcore.blocks.StructBlock((('name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('button', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('teaser', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('content', wocat.cms.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('top', 'Top'), ('left', 'Left'), ('right', 'Right')], required=False)), ('large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))), required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('read_more_text', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('media_teaser', wagtail.wagtailcore.blocks.StructBlock((('media', wocat.cms.blocks.MediaChooserBlock(required=True)),))), ('image_gallery', wagtail.wagtailcore.blocks.StructBlock((('columns', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(6, '2'), (4, '3'), (3, '4')])), ('elements', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('description', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('shrink', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(1, 'Small'), (2, 'Extra small')], required=False))))))))))))))), ('news_teaser', wagtail.wagtailcore.blocks.StructBlock((('news', wocat.news.blocks.NewsChooserBlock(required=True)),)))), blank=True),
        ),
    ]
