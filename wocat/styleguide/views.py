import pprint

from django.template.defaultfilters import slugify
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from .data import data


class StyleguideView(TemplateView):
    template_name = 'styleguide/index.html'

    def get_template_names(self):
        template_name = self.kwargs.get('template')
        if template_name:
            return ['styleguide/demos/{}.html'.format(slugify(template_name))]
        return super().get_template_names()

    def recursive_mark_safe(self, context):
        for key, value in context.items():
            if isinstance(value, dict):
                value = self.recursive_mark_safe(value)
            elif isinstance(value, str):
                # print(value)
                value = mark_safe(value)
            context[key] = value
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # TODO: Split in sub-methods

        for item, values in data.items():
            name = values.get('name')
            template = values.get('template')
            item_context = values.get('context')
            if item_context:
                item_context = self.recursive_mark_safe(item_context)
            # Create rendering for meta data
            meta_context = dict()
            meta_context['name'] = name
            meta_context['template'] = template
            input = """{{% include "{}" %}}""".format(template)
            meta_context['input'] = input
            meta_context['context'] = pprint.pformat(item_context)

            item_meta = render_to_string("styleguide/_meta.html", context=meta_context)
            context[item + "_meta"] = item_meta

            item_output = render_to_string(template, context=item_context)
            context[item + "_output"] = item_output

            context[item] = item_meta + item_output
        return context
