# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
# Add the project root and src directory to the Python path
# This allows Sphinx to find your Python modules for autodoc
sys.path.insert(0, os.path.abspath('../src')) # Path to your src folder
sys.path.insert(0, os.path.abspath('..'))    # Path to the module_4 folder (parent of source)

project = 'Module 4: Pizza Ordering System'
copyright = '2025, Sara Nasab'
author = 'Sara Nasab'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc', # Enables automatic documentation from docstrings
]

# Configure autodoc to include members, undoc-members, show-inheritance,
# and crucially, var-members (for module-level variables like your price dictionaries)
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
    'var-members': True, # This tells autodoc to include module-level variables
}

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']