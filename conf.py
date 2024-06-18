# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
# sys.path.insert(0, os.path.abspath("C:\\Users\\sykang1\\PycharmProjects\\SphinxProject"))
# sys.path.insert(0, os.path.abspath(".."))
from doc_test import __version__ as VERSION


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'doc_test'
copyright = '2024, sykang1'
author = 'sykang1'
release = VERSION

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.napoleon', 'sphinx.ext.autodoc', 'sphinx.ext.todo',
              'sphinx.ext.githubpages', 'sphinx.ext.viewcode',
              'sphinx_autodoc_typehints']

templates_path = ['_templates']
exclude_patterns = []

language = 'ko'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# sphinx.ext.todo
tool_include_todos = True