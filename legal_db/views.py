from django.shortcuts import render


def index(request):
    return render(request, "legal_db/index.html")


def case_index(request):
    context = {
        "cases": [
            {
                "country": "United States",
                "name": "Wikimedia Foundation v Internet Brands",
                "license": "CC BY-SA",
                "year": 2020,
            },
            {
                "country": "Belgium",
                "name": "Linchôdmapwa v L'asbl Festival de Theatre de Spa",
                "license": "CC BY-NC-ND",
                "year": 2019
            },
            {
                "country": "United States",
                "name": "Wikimedia Foundation v Internet Brands",
                "license": "CC BY-SA",
                "year": 2020,
            },
            {
                "country": "Belgium",
                "name": "Linchôdmapwa v L'asbl Festival de Theatre de Spa",
                "license": "CC BY-NC-ND",
                "year": 2019
            },
            {
                "country": "United States",
                "name": "Wikimedia Foundation v Internet Brands",
                "license": "CC BY-SA",
                "year": 2020,
            },
            {
                "country": "Belgium",
                "name": "Linchôdmapwa v L'asbl Festival de Theatre de Spa",
                "license": "CC BY-NC-ND",
                "year": 2019
            }
        ],
        "tags": ["art", "educational material", "musical work", "photograph"]
    }
    return render(request, "legal_db/case/index.html", context)

def case_detail(request):
    context = {
        "case": {
            "name": "Wikimedia Foundation v Internet Brands",
            "country": "United States",
            "courts": "Superior Court of California",
            "year": "2013",
            "links": [
                {
                    "url": "www.google.com",
                    "title": "WMF complaint for declaratory judgement September 2012",
                    "label": "Brief"
                },
                {
                    "url": "www.twitter.com",
                    "title": "Another page linked here",
                    "label": "Pleading"
                }
            ],
            "background": "Wikitravel was a wiki founded in 2003, allowing volunteer authors to add and edit content related to worldwide travel and tourism. All content on the site was published under a Creative Commons ShareAlike license. In 2005, the domain name was purchased by Internet Brands, a for-profit company. In 2012, a group of volunteer site administrators and authors approached the Wikimedia Foundation about making a new travel-oriented wiki, which would incorporate some of the content from Wikitravel owned by contributors.",
            "summary": "Internet Brands filed a lawsuit against two of those Wikitravel editors, asserting trademark infringement, unfair competition, and civil conspiracy. The Wikimedia Foundation then filed this declaratory judgment action against Internet Brands in California state court, requesting a judicial determination that they have the right to start the proposed new travel wiki and incorporate content from Wikitravel under the terms of the CC license.",
            "tags": ["education material", "open educational resources", "scientific research"]
        }
    }
    return render(request, 'legal_db/case/detail.html', context)
