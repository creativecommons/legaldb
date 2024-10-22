# About Guides
These Guides are meant to serve as an expansion to existing documentation for
beginners of this project, that means Guides should be directly and uniquely
related to this project. Generalized beginner level material about broader
topics like Github, Git, Command-line basics, etc. may be better served in the
Open Source documentation as a part of our new overall general beginner guides.

## Some Appropriate Guides Topic Examples
- Overview of technologies used
- Setting up this project with Docker on Windows
- Setting up this project with pipenv
- Making style changes to the project
- Troubleshooting known Windows Issues with Docker and VS Code


## Guide Conventions to Follow
- be written in Markdown format
- exist as a sibling to this `README.md` file in the `guides/` directory
- utilize [snake_case](https://en.wikipedia.org/wiki/Snake_case) naming
- have a unique name, and scope for Guide
- be sure to check that modifying an existing Guide isn't better than creating a new one
- link to existing resources where applicable, rather than duplicating work within
 a Guide (for example: you wish to explain what the `cd` command is; you should
 link to the MDN Docs, Wikipedia, etc. instead of writing it out within the Guide
 itself in a verbose fashion)
- have a clear and focused need they are addressing

## Process for creating a new Guide
1. Create a Feature Issue outlining:
   - The name of the Guide
   - The material it will cover
   - Any related resources you wish to reference or include
   - Why you believe this Guide is useful, what need is it solving?
2. Participate in any relevant discussions on the Issue to further outline the Guide, depending on the aims of the Guide, this could take some time.
3. Wait for Issue to reach a status of `status: ready for work`, once reached a PR can now be generated for adding the approved Guide to this project following the conventions listed in this `README.md`.
