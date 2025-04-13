from .models import *
from modeltranslation.translator import TranslationOptions, register

@register(Kino)
class KinoTranslationOptions(TranslationOptions):
    fields = ('nom', 'janr')

@register(Aktyor)
class AktyorTranslationOptions(TranslationOptions):
    fields = ('ism', 'davlat',)

@register(Tarif)
class TarifTranslationOptions(TranslationOptions):
    fields = ('nom',)

