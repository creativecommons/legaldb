from django.shortcuts import render
from django.urls import reverse


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
                "year": 2019,
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
                "year": 2019,
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
                "year": 2019,
            },
        ],
        "tags": ["art", "educational material", "musical work", "photograph"],
        "breadcrumb_links": [("Cases", "")],
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
                    "label": "Brief",
                },
                {
                    "url": "www.twitter.com",
                    "title": "Another page linked here",
                    "label": "Pleading",
                },
            ],
            "background": "Wikitravel was a wiki founded in 2003, allowing volunteer authors to add and edit content related to worldwide travel and tourism. All content on the site was published under a Creative Commons ShareAlike license. In 2005, the domain name was purchased by Internet Brands, a for-profit company. In 2012, a group of volunteer site administrators and authors approached the Wikimedia Foundation about making a new travel-oriented wiki, which would incorporate some of the content from Wikitravel owned by contributors.",
            "summary": "Internet Brands filed a lawsuit against two of those Wikitravel editors, asserting trademark infringement, unfair competition, and civil conspiracy. The Wikimedia Foundation then filed this declaratory judgment action against Internet Brands in California state court, requesting a judicial determination that they have the right to start the proposed new travel wiki and incorporate content from Wikitravel under the terms of the CC license.",
            "tags": [
                "education material",
                "open educational resources",
                "scientific research",
            ],
        },
        "breadcrumb_links": [("Cases", reverse("case_index")), ("Case detail", "")],
    }
    return render(request, "legal_db/case/detail.html", context)


def scholarship_index(request):
    context = {
        "scholarships": [
            {
                "title": "United States",
                "authors": "Wikimedia Foundation v Internet Brands",
                "license": "CC BY-SA",
                "publication_year": 2020,
            },
            {
                "title": "Belgium",
                "authors": "Linchôdmapwa v L'asbl Festival de Theatre de Spa",
                "license": "CC BY-NC-ND",
                "publication_year": 2019,
            },
            {
                "title": "United States",
                "authors": "Wikimedia Foundation v Internet Brands",
                "license": "CC BY-SA",
                "publication_year": 2020,
            },
            {
                "title": "Belgium",
                "authors": "Linchôdmapwa v L'asbl Festival de Theatre de Spa",
                "license": "CC BY-NC-ND",
                "publication_year": 2019,
            },
            {
                "title": "United States",
                "authors": "Wikimedia Foundation v Internet Brands",
                "license": "CC BY-SA",
                "publication_year": 2020,
            },
            {
                "title": "Belgium",
                "authors": "Linchôdmapwa v L'asbl Festival de Theatre de Spa",
                "license": "CC BY-NC-ND",
                "publication_year": 2019,
            },
        ],
        "tags": ["art", "educational material", "musical work", "photograph"],
        "breadcrumb_links": [("Scholarships", "")],
    }
    return render(request, "legal_db/scholarship/index.html", context)


def scholarship_detail(request):
    context = {
        "scholarship": {
            "title": "Safe to be Open: Study on the Protection of Research Data and Recommendations for Access and Usage",
            "license": "Unknown",
            "summary": "Openness has become a common concept in a growing number of scientific and academic fields. Expressions such as Open Access (OA) or Open Content (OC) are often employed for publications of papers and research results, or are contained as conditions in tenders issued by a number of funding agencies. More recently the concept of Open Data (OD) is of growing interest in some fields, particularly those that produce large amounts of data – which are not usually protected by standard legal tools such as copyright. However, a thorough understanding of the meaning of Openness – especially its legal implications – is usually lacking. Open Access, Public Access, Open Content, Open Data, Public Domain. All these terms are often employed to indicate that a given paper, repository or database does not fall under the traditional “closed” scheme of default copyright rules. However, the differences between all these terms are often largely ignored or misrepresented, especially when the scientist in question is not familiar with the law generally and copyright in particular – a very common situation in all scientific fields. On 17 July 2012 the European Commission published its Communication to the European Parliament and the Council entitled “Towards better access to scientific information: Boosting the benefits of public investments in research”. As the Commission observes, “discussions of the scientific dissemination system have traditionally focused on access to scientific publications – journals and monographs. However, it is becoming increasingly important to improve access to research data (experimental results, observations and computer-generated information), which forms the basis for the quantitative analysis underpinning many scientific publications”. The Commission believes that through more complete and wider access to scientific publications and data, the pace of innovation will accelerate and researchers will collaborate so that duplication of efforts will be avoided. Moreover, open research data will allow other researchers to build on previous research results, as it will allow involvement of citizens and society in the scientific process. In the Communication the Commission makes explicit reference to open access models of publications and dissemination of research results, and the reference is not only to access and use but most significantly to reuse of publications as well as research data. The Communication marks an official new step on the road to open access to publicly funded research results in science and the humanities in Europe. Scientific publications are no longer the only elements of its open access policy: research data upon which publications are based should now also be made available to the public. As noble as the open access goal is, however, the expansion of the open access policy to publicly funded research data raises a number of legal and policy issues that are often distinct from those concerning the publication of scientific articles and monographs. Since open access to research data – rather than publications – is a relatively new policy objective, less attention has been paid to the specific features of research data. An analysis of the legal status of such data, and on how to make it available under the correct licence terms, is therefore the subject of the following sections.",
            "publication_name": "Open Aire Plus",
            "publication_year": "2013",
            "authors": "Dietr, Nil and Guibault, Lucie and Margoni, Thomas and Siewicz, Krzysztof and Spindler, Gerald and Wiebe, Andreas",
            "link": {
                "url": "www.google.com",
                "title": "Safe to Be Open: Study on the Protection of Research Data and Recommendations for Access and Usage",
                "label": "",
            },
            "tags": [
                "education material",
                "open educational resources",
                "scientific research",
            ],
        },
        "breadcrumb_links": [
            ("Scholarships", reverse("scholarship_index")),
            ("Scholarship detail", ""),
        ],
    }
    return render(request, "legal_db/scholarship/detail.html", context)


def temp(request):
    return render(request, "legal_db/base.html")
