# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../../PycharmProjects/becode/'))


# -- Project information -----------------------------------------------------

project = 'Patrick\'s Docs'
copyright = '2021, Patrick Brunswyck'
author = 'Patrick Brunswyck'

# The full version, including alpha/beta/rc tags
release = 'alpha'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# python -m pip install sphinx_autodoc_defaultargs

extensions = ['sphinx.ext.githubpages',
              'sphinx_rtd_dark_mode',
              'sphinx.ext.autodoc',
              'sphinx_autodoc_defaultargs',
              'sphinx.ext.todo',
              'sphinx_gallery.gen_gallery',
              'matplotlib.sphinxext.plot_directive',
              'IPython.sphinxext.ipython_directive',
              'IPython.sphinxext.ipython_console_highlighting',
              'sphinx.ext.doctest',
              'sphinx.ext.inheritance_diagram',
              'numpydoc',
              'sphinx_revealjs',
              'sphinx.ext.graphviz'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates', 'templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['gallery']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_dark_mode'
html_style = 'css/my_theme.css'
#html_theme = 'sphinx_rtd_theme'
#html_theme = 'groundwork'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static', 'gallery']

todo_include_todos = True

sphinx_gallery_conf = {
     'examples_dirs': '../gallery_code',   # path to your example scripts
     'gallery_dirs': 'gallery',  # path to where to save gallery generated output
     'download_all_examples': True
}

rst_prolog = """
.. |default| raw:: html

    <div class="default-value-section">""" + \
    ' <span class="default-value-label">Default:</span>'
