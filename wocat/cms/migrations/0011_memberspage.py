# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-27 16:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks
import wocat.cms.blocks
import wocat.cms.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('cms', '0010_auto_20160627_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembersPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('content', wagtail.wagtailcore.fields.StreamField((('heading', wocat.cms.blocks.HeadingBlock()), ('rich_text', wocat.cms.blocks.RichTextBlock()), ('image', wocat.cms.blocks.ImageBlock()), ('embed', wocat.cms.blocks.EmbedBlock()), ('teaser', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('content', wocat.cms.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('top', 'Top'), ('left', 'Left'), ('right', 'Right')], required=False)), ('large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))), required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))), ('columns_1_to_1', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wocat.cms.blocks.HeadingBlock()), ('rich_text', wocat.cms.blocks.RichTextBlock()), ('image', wocat.cms.blocks.ImageBlock()), ('embed', wocat.cms.blocks.EmbedBlock()), ('teaser', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('content', wocat.cms.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('top', 'Top'), ('left', 'Left'), ('right', 'Right')], required=False)), ('large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))), required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)))))))), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wocat.cms.blocks.HeadingBlock()), ('rich_text', wocat.cms.blocks.RichTextBlock()), ('image', wocat.cms.blocks.ImageBlock()), ('embed', wocat.cms.blocks.EmbedBlock()), ('teaser', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('content', wocat.cms.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('top', 'Top'), ('left', 'Left'), ('right', 'Right')], required=False)), ('large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))), required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))))))))), ('columns_1_to_2', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wocat.cms.blocks.HeadingBlock()), ('rich_text', wocat.cms.blocks.RichTextBlock()), ('image', wocat.cms.blocks.ImageBlock()), ('embed', wocat.cms.blocks.EmbedBlock()), ('teaser', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('content', wocat.cms.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('top', 'Top'), ('left', 'Left'), ('right', 'Right')], required=False)), ('large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))), required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)))))))), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wocat.cms.blocks.HeadingBlock()), ('rich_text', wocat.cms.blocks.RichTextBlock()), ('image', wocat.cms.blocks.ImageBlock()), ('embed', wocat.cms.blocks.EmbedBlock()), ('teaser', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('content', wocat.cms.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('top', 'Top'), ('left', 'Left'), ('right', 'Right')], required=False)), ('large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))), required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))))))))), ('columns_2_to_1', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wocat.cms.blocks.HeadingBlock()), ('rich_text', wocat.cms.blocks.RichTextBlock()), ('image', wocat.cms.blocks.ImageBlock()), ('embed', wocat.cms.blocks.EmbedBlock()), ('teaser', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('content', wocat.cms.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('top', 'Top'), ('left', 'Left'), ('right', 'Right')], required=False)), ('large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))), required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)))))))), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wocat.cms.blocks.HeadingBlock()), ('rich_text', wocat.cms.blocks.RichTextBlock()), ('image', wocat.cms.blocks.ImageBlock()), ('embed', wocat.cms.blocks.EmbedBlock()), ('teaser', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('content', wocat.cms.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('top', 'Top'), ('left', 'Left'), ('right', 'Right')], required=False)), ('large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))), required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))))))))), ('columns_1_to_1_to_1', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wocat.cms.blocks.HeadingBlock()), ('rich_text', wocat.cms.blocks.RichTextBlock()), ('image', wocat.cms.blocks.ImageBlock()), ('embed', wocat.cms.blocks.EmbedBlock()), ('teaser', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('content', wocat.cms.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('top', 'Top'), ('left', 'Left'), ('right', 'Right')], required=False)), ('large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))), required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)))))))), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wocat.cms.blocks.HeadingBlock()), ('rich_text', wocat.cms.blocks.RichTextBlock()), ('image', wocat.cms.blocks.ImageBlock()), ('embed', wocat.cms.blocks.EmbedBlock()), ('teaser', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('content', wocat.cms.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('top', 'Top'), ('left', 'Left'), ('right', 'Right')], required=False)), ('large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))), required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)))))))), ('middle_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wocat.cms.blocks.HeadingBlock()), ('rich_text', wocat.cms.blocks.RichTextBlock()), ('image', wocat.cms.blocks.ImageBlock()), ('embed', wocat.cms.blocks.EmbedBlock()), ('teaser', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('content', wocat.cms.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('top', 'Top'), ('left', 'Left'), ('right', 'Right')], required=False)), ('large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))), required=False)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)))))))))))), blank=True)),
            ],
            options={
                'verbose_name': 'Members',
            },
            bases=(wocat.cms.models.UniquePageMixin, 'wagtailcore.page'),
        ),
    ]
