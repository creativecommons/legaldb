# About this Guide

This guide provides a simple, comprehensive overview of the technologies used
in the Creative Commons Legal Database (Legal DB) repository. It provides
explanation on how they are used within the codebase, and provides links to
official recommendations to read further.

## Technologies used


### Django

Django is a python framework for building scalable applications. Legal DB uses
Django as the back-end web framework for managing logic and creating a dynamic
website.

To learn more about Django, refer to the [Django Documentation |
Django](https://docs.djangoproject.com/en/4.2/)


### Hypertext Markup Language (HTML) and Cascading Style Sheets (CSS)

Legal DB utilizes semantic HTML for their page, which means that HTML elements
are used according to their intended purpose and this helps to improve
accessibilty. As a beginner, the format of the HTML file might seem strange to
you, that's because this project uses Django templates, which helps to combine
both Django and HTML for dynamic content rendering.  CSS is used for the
styling and ensures responsiveness for all browsers.


### Sassy Cascading Style Sheets (SCSS)

Referred to as CSS with superpowers, SCSS is a css extension that allows you to
do much more like nesting styles, extending CSS styles, adding varaiables and
mixins. All these features and more that come with SCSS helps to help your
stylesheet maintainable, dry and readable.

Read the [Sass: Documentation](https://sass-lang.com/documentation/) to learn
more.


### Vocabulary Design System

Creative Commons has their own internal design system, Vocabulary which helps
all the websites have the same look and aesthetics. It ensures uniformity
across typography, header and footer components. At the moment, work is
currently underway to add the latest version of Vocabulary to this codebase.

To learn more about Vocabulary, you can check out the [Vocabulary -
Docs](https://vocabulary-docs.netlify.app/)


### Webpack

Webpack is a bundler that takes different assets like JavaScript, CSS, and
images and then compiles them into a single, optimized output file. This allows
for a streamlined development process by handling dependencies and improving
load times. With webpack, it is easier to mange large projects. In this
project, webpack helps manage JavaScript and SCSS files, ensuring an optimized
build.

Learn more from the offical webpack documentation: [Concepts |
webpack](https://webpack.js.org/concepts/)
