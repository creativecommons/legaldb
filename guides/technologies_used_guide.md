# About this Guide

This guide provides a simple, comprehensive overview of the technologies used in the Creative Commons Legal DB repository. It provides explanation on how they are used within the codebase, and provides links to official recommendations to read further.

## Technologies used

### Vocabulary Design System
Creative Commons has their own internal design system, Vocabulary which helps all the websites have the same look and aesthetics. It ensures uniformity across typography, header and footer components. At the moment, work is currently underway to add the latest version of Vocabulary to this codebase.

To learn more about Vocabulary, you can check out the [Vocabulary Documentation](https://vocabulary-docs.netlify.app/)

### Django
Django is a python framework for building scalable applications. LegalDB uses Django as the back-end web framework for managing logic and creating a dynamic website.

To learn more about Django, refer to the [Django Documentation](https://docs.djangoproject.com/en/5.1/)


## HTML and CSS
LegalDB utilizes semantic HTML for their page, which means that HTML elements are used according to their intended purpose and this helps to improve accessibilty. As a beginner, the format of the HTML file might seem strange to you, that's because this project uses Django templates, which helps to combine both django and HTML for dynamic content rendering.  CSS is used for the styling and ensures responsiveness for all browsers. 

### Lektor
Lektor is a static Content Management System(CMS) that allows developers to create websites efficiently. In LegalDB, Lektor is used to generate static content. It runs offline and utilizes Python, making it a flexible option.

Learn more about Letkor on the offical [Lektor Documentation Page](https://www.getlektor.com/docs/what/)