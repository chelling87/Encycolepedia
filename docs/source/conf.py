# Configuration file for the Sphinx documentation builder.
import sys
import os
sys.path.insert(0, os.path.abspath('../')) # path relative to conf.py

# -- Project information

project = 'Encycolepedia'
copyright = '2023, Helling'
author = 'Cole Helling'

release = '0.1'
version = '0.1.1'

# -- General configuration

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinx_exec_code',
    'sphinx.ext.autosummary', 
    'sphinx_autopackagesummary',
    'nbsphinx',
    'jupyter_sphinx'
]

autosummary_generate = True

# -- Options for HTML output

#html_theme = 'sphinx_rtd_theme'
html_theme = "sphinx_book_theme"
html_theme_options = {
    "home_page_in_toc": True,
    "repository_url": "https://github.com/chelling87/Encycolepedia",
    "use_repository_button": True,
}

exec_code_working_dir = '..'
exec_code_source_folders = ['.']
exec_code_example_dir = '.'

# -- Options for EPUB output
epub_show_urls = 'footnote'
