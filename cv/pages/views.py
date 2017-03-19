from django.views.generic.base import TemplateView


class TestView(TemplateView):
    template_name = "base.html"
#     Just the banner and copyright info, nothing more.


class ReferencesView(TemplateView):
    template_name = "references.html"


class InterestView(TemplateView):
    template_name = "interests.html"


class ExperienceView(TemplateView):
    template_name = "experience.html"


class SkillsView(TemplateView):
    template_name = "skills.html"


class BioView(TemplateView):
    template_name = "home.html"
