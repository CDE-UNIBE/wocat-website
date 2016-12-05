from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.models import register_snippet

from wocat.cms.models import UniquePageMixin, HeaderPageMixin
from wocat.core.blocks import CORE_BLOCKS

from wocat.countries.models import Continent, Country
from wocat.languages.models import Language


class MediaLibraryPage(UniquePageMixin, HeaderPageMixin, Page):
    template = 'medialibrary/library.html'

    content = StreamField(
        CORE_BLOCKS,
        blank=True
    )

    content_panels = Page.content_panels + HeaderPageMixin.content_panels + [
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + HeaderPageMixin.search_fields + [
        index.SearchField('content'),
    ]

    class Meta:
        verbose_name = _('Media Library')

    parent_page_types = ['cms.HomePage']

    # subpage_types = ['medialibrary.MediaPage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context['types'] = MediaType.objects.all()
        items = Media.objects.all()
        media_type = request.GET.get('type', request.POST.get('type'))
        if media_type and media_type != '0':
            items = items.filter(media_type=media_type)
            context['type'] = media_type

        search = request.GET.get('search')
        if search:
            items = items.filter(
                Q(title__icontains=search) | Q(abstract__icontains=search) | Q(author__icontains=search) | Q(
                    content__icontains=search)
            )
            context['search'] = search

        context['years'] = set(Media.objects.values_list('year', flat=True))
        year = request.GET.get('year')
        if year:
            items = items.filter(year=year)
            context['year'] = int(year)

        context['languages'] = Language.objects.all()
        language = request.GET.get('language')
        if language:
            items = items.filter(languages__code=language)
            context['language'] = language

        context['continents'] = Continent.objects.all()
        continent = request.GET.get('continent')
        if continent:
            items = items.filter(continent=continent)
            context['continent'] = continent

        countries = Country.objects.all()
        context['countries'] = countries
        country = request.GET.get('country')
        if country:
            items = items.filter(countries__code=country)
            context['country'] = country

        context['items'] = items
        return context


@register_snippet
class MediaType(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=255,
        unique=True,
    )
    icon = models.CharField(
        _('Icon name'),
        max_length=255,
        help_text=_('Fontawesome icon name.'),
        blank=True,
    )
    default_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_('Default image'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    @property
    def image(self):
        return self.default_image

    def __str__(self):
        return self.name

    panels = [
        FieldPanel('name'),
        FieldPanel('icon'),
        ImageChooserPanel('default_image'),
    ]


class Media(models.Model):
    title = models.CharField(
        _('Title'),
        max_length=255,
        unique=True
    )
    abstract = models.TextField(
        _('Abstract'),
    )
    teaser_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_('Teaser image'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    @property
    def image(self):
        return self.teaser_image or self.media_type.image

    video = models.URLField(
        verbose_name=_('Video'),
        blank=True,
    )

    year = models.PositiveIntegerField(
        _('Year'),
        default=timezone.now().year,
        validators=[MaxValueValidator(4000)],
        blank=True, null=True
    )

    languages = models.ManyToManyField(
        verbose_name=_('Languages'),
        to=Language,
        blank=True
    )

    content = StreamField(
        CORE_BLOCKS,
        blank=True,
    )
    file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True, blank=True,
        on_delete=models.PROTECT,
        related_name='+',
        help_text=_('This field is only used if the content is empty.'),
    )
    author = models.CharField(
        _('Author'),
        max_length=255,
        blank=True,
    )
    countries = models.ManyToManyField(
        verbose_name=_('Countries'),
        to=Country,
        blank=True,
    )
    continent = models.ForeignKey(
        to=Continent,
        blank=True, null=True,
    )
    media_type = models.ForeignKey(
        'MediaType',
        verbose_name=_('Type'),
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = _('Media')
        verbose_name_plural = _('Media')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('media:detail', args=[self.id])

    panels = [
        FieldPanel('title'),
        FieldPanel('abstract'),
        FieldPanel('media_type'),
        FieldPanel('video'),
        DocumentChooserPanel('file'),
        ImageChooserPanel('teaser_image'),
        FieldPanel('author'),
        FieldPanel('countries'),
        FieldPanel('continent'),
        FieldPanel('year'),
        FieldPanel('languages'),
        StreamFieldPanel('content'),
    ]
