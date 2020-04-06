import json

advancementFile = "advancements.json"

hiddenAdvancements = ["nether/all_effects", "adventure/arbalistic"]

with open(advancementFile, "r") as orig:
    advancements = json.load(orig)["data"]

    def getCategories():
        return list(advancements.keys())

    def getAdvancements(category):
        assert(category in getCategories())
        return list(advancements[category])
    
    def getAdvancement(category, advancement):
        assert(advancement in getAdvancements(category))
        return advancements[category][advancement]
    
test = getAdvancement("husbandry", "breed_an_animal")
print(test)