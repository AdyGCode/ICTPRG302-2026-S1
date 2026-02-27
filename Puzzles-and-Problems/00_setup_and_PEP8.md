> [!NOTICE]
> THIS DOCUMENT IS A WORK IN PROGRESS AS OF 2025-08-10

# 🐍 00: Setup and PEP8 (A summary)

## Setup

1. Get a modern version of Python. In 2025, that's a version greater than or equal to 3.12.X.
    - Windows users: You should get it from https://www.python.org/downloads/
    - Mac users: Instead, first get homebrew:
        - https://brew.sh/
        - Then use brew to install Python: `brew install python`
    - Debian-based users: You already have Python, but might like to install `2to3` with apt
    - Other Linuxes: Check your package manager's repositories, they will have python.
    - Hard mode for non-Windows users: Install `asdf` and use that to manage Python. https://asdf-vm.com/

2. Get a code editor.  In this class, I recommend either VSCode or PyCharm -- but be sure to turn off all code-completion.  At this stage of your education, code-completion will interrupt your ability to learn, and weaken your ability.

---

## PEP8 Summary

> We want our code to be readable
AND
> We don't want to argue about formatting issues (Look up the term "bikeshedding")

So:
> We make a list of ways to write code that we all agree on.

In every company or group, everyone will decide on the standards that they follow to write code. But here, in this course, we are going to use PEP-8.

1. All indentation will be done with 4 spaces
2. Indentation will be spaces and not tabs.
3. Lines will not be more than 79 characters long.
4. Variables will be named in english, in snake_case, and will be descriptive

This is not a complete list, see the PEP8 standard: https://peps.python.org/pep-0008/
