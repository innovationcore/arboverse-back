from django.contrib import admin

from arboverse_updated.models import BloodMeal, \
                                     Borning, \
                                     Country, \
                                     Disease, \
                                     FeedingPeriod,\
                                     Habitat, \
                                     Landscape, \
                                     Location, \
                                     VectorFamily, \
                                     VectorGenus, \
                                     VectorOrder, \
                                     VectorSpecies, \
                                     VectorSubFamily, \
                                     Virus, \
                                     VirusFamily, \
                                     VirusGenus, \
                                     VirusVector, \
    VectorSpeciesBloodMeal, \
    VectorSpeciesHabitat, \
    VectorSpeciesLocation, \
    VectorSpeciesLandscape, \
    VectorSpeciesFeedingPeriod

from schema_populator import VectorBloodmeal, VectorFeedingPeriod

# Register your models here.

admin.site.register(BloodMeal)
admin.site.register(Borning)
admin.site.register(Country)
admin.site.register(Disease)
admin.site.register(FeedingPeriod)
admin.site.register(Habitat)
admin.site.register(Landscape)
admin.site.register(Location)
admin.site.register(VectorFamily)
admin.site.register(VectorGenus)
admin.site.register(VectorOrder)
admin.site.register(VectorSpecies)
admin.site.register(VectorSpeciesHabitat)
admin.site.register(VectorSpeciesLocation)
admin.site.register(VectorSpeciesLandscape)
admin.site.register(VectorSpeciesBloodMeal)
admin.site.register(VectorSpeciesFeedingPeriod)
admin.site.register(VectorSubFamily)
admin.site.register(Virus)
admin.site.register(VirusFamily)
admin.site.register(VirusGenus)
admin.site.register(VirusVector)
