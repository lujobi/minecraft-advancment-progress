import json

advancementFile = "advancements.json"

hiddenAdvancements = ["nether/all_effects", "adventure/arbalistic"]

with open(advancementFile, "r") as orig:
    parsed = json.load(orig)
    advancements = parsed["data"]

    def getCategories():
        return list(advancements.keys())

    def getAdvancements(category):
        assert(category in getCategories())
        return list(advancements[category])
    
    def getAdvancement(category, advancement):
        assert(advancement in getAdvancements(category))
        return advancements[category][advancement]

    def getMeta():
        return parsed["meta"]
    