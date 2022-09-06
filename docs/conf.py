"""Sphinx configuration."""
project = "Hypermodern Cookiecutter Example"
author = "Paul Rousset"
copyright = "2022, Paul Rousset"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
