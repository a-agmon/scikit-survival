#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# scikit-survival documentation build configuration file
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
from setuptools_scm import get_version

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
# https://docs.readthedocs.io/en/latest/faq.html?highlight=environ#how-do-i-change-behavior-for-read-the-docs
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
if on_rtd:
    sys.path.insert(0, os.path.abspath(os.path.pardir))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.8'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
]

autosummary_generate = True
autodoc_default_flags = ['members', 'inherited-members']

# Napoleon settings
napoleon_google_docstring = True
napoleon_include_init_with_doc = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'scikit-survival'
copyright = '2015-2019, Sebastian Pölsterl'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = get_version(root='..', relative_to=__file__)
# The short X.Y version.
version = '.'.join(release.split('.')[:2])

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', '**/README.*', 'Thumbs.db', '.DS_Store']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'nature'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'scikit-survivaldoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'scikit-survival.tex', 'scikit-survival Documentation',
   'Sebastian Pölsterl', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'scikit-survival', 'scikit-survival Documentation',
     ['Sebastian Pölsterl'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'scikit-survival', 'scikit-survival Documentation',
   'Sebastian Pölsterl', 'scikit-survival', 'Survival analysis on top of scikit-learn',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

if on_rtd:
    MOCK_MODULES = [
        # external dependencies
        'cvxopt',
        'cvxpy',
        'numexpr',
        'numpy',
        'osqp',
        'pandas',
        'pandas.api.types',
        'scipy',
        'scipy.integrate',
        'scipy.io.arff',
        'scipy.linalg',
        'scipy.optimize',
        'scipy.sparse',
        'scipy.special',
        'scipy.stats',
        'sklearn',
        'sklearn.base',
        'sklearn.dummy',
        'sklearn.ensemble',
        'sklearn.ensemble._base',
        'sklearn.ensemble._forest',
        'sklearn.ensemble._gb',
        'sklearn.ensemble._gb_losses',
        'sklearn.ensemble._gradient_boosting',
        'sklearn.ensemble.base',
        'sklearn.ensemble.forest',
        'sklearn.ensemble.gradient_boosting',
        'sklearn.exceptions',
        'sklearn.externals.joblib',
        'sklearn.linear_model',
        'sklearn.metrics',
        'sklearn.metrics.pairwise',
        'sklearn.model_selection',
        'sklearn.pipeline',
        'sklearn.preprocessing',
        'sklearn.svm',
        'sklearn.tree',
        'sklearn.tree._classes',
        'sklearn.tree._splitter',
        'sklearn.tree._tree',
        'sklearn.tree.tree',
        'sklearn.utils',
        'sklearn.utils._joblib',
        'sklearn.utils.extmath',
        'sklearn.utils.fixes',
        'sklearn.utils.metaestimators',
        'sklearn.utils.validation',
        # our C modules
        'sksurv.bintrees._binarytrees',
        'sksurv.ensemble._coxph_loss',
        'sksurv.kernels._clinical_kernel',
        'sksurv.linear_model._coxnet',
        'sksurv.svm._minlip',
        'sksurv.svm._prsvm',
        'sksurv.tree._criterion']

    MOCK_VERSIONS = {
        'pandas': '0.22.0',
        'sklearn': '0.22.0',
    }

    from unittest.mock import Mock

    class MockModule(Mock):
        """mock imports"""

        @classmethod
        def __getattr__(cls, name):
            if name in ('__file__', '__path__'):
                return '/dev/null'
            elif name[0] == name[0].upper() and name[0] != "_":
                # Not very good, we assume Uppercase names are classes...
                mocktype = type(name, (), {})
                mocktype.__module__ = __name__
                return mocktype
            else:
                return MockModule()

    sys.modules.update((mod_name, MockModule()) for mod_name in MOCK_MODULES)
    for mod, ver in MOCK_VERSIONS.items():
        setattr(sys.modules[mod], '__version__', ver)
