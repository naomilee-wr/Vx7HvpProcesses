# -*- coding: utf-8 -*-
#
# Vx7 QMS documentation build configuration file, created by
# sphinx-quickstart on Sat May 12 19:34:31 2018.

#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.


# -- Define here your working directory -------------------------------------------------------------------------------
import os
import sys
import sphinx_bootstrap_theme

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- Some general info  about the project -----------------------------------------------------------------------------

project = u'WR VxWorks and HVP Process Documentation'
copyright = u'2020, Wind River Systems, Inc.'
author = u'NaomiLee'


# -- A few basic configurations ---------------------------------------------------------------------------------------

# The documentation in this project will be mostly generated from .rst files
# In This project, every auto-documented module/class has its own .rst file, under the main documentation dir,
#   which is rendered into an .html page.
# Get more information here: http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
source_suffix = ['.rst']

# This is the name of the main page of the project.
# It means that you need to have an `index.rst` file where you will design the landing page of your project.
# It will be rendered into an .html page that you can find at: `_build/html/index.html`
# (this is a standard name. change it only if you know what you are doing)
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build']

# List here any paths that contain templates, relative to this directory.
# You can find some not-so-intuitive information here: http://www.sphinx-doc.org/en/master/templating.html
# But the best way to learn is by example, right? :)
# So, for example, in this project, I wanted to change the title of the Table Of Contents in the sidebar.
#   So I copied `<Sphinx install dir>/themes/basic/globaltoc.html` into the `_templates` folder,
#      and replaced 'Table of Content' with 'Universe'.
# #CHNAGEME# In documentation_template_for_your_next_project/_templates/globaltoc.html
#            Change "Universe" into the name of your project
templates_path = ['_templates']

# -- Define and configure non-default extensions ----------------------------------------------------------------------

# You can find a list of available extension here: http://www.sphinx-doc.org/en/master/extensions.html
extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc', 'sphinx.ext.imgmath']

# Above extensions explanation and configurations:

# todo: When you use the syntax ".. todo:: some todo comment" in your docstring,
#         it will appear in a highlighted box in the documentation.
#       In order for this extension to work, make sure you include the following:
todo_include_todos = True

# viewcode: Next to each function/module in the documentation, you will have an internal link to the source code.
#           The source code will have colors defined by the Pygments (syntax highlighting) style.
#           You can checkout the available pygments here: https://help.farbox.com/pygments.html
pygments_style = 'native'

# autodoc: 
#          It allows Sphinx to automatically generate documentation for the docstrings in your code.
#          Get more info here: http://www.sphinx-doc.org/en/master/ext/autodoc.html
# Some useful configurations:
autoclass_content = "both"  # Include both the class's and the init's docstrings.
autodoc_member_order = 'bysource'  # In the documentation, keep the same order of members as in the code.
autodoc_default_flags = ['members']  # Default: include the docstrings of all the class/module members.

# Additional stuff for the LaTeX preamble.
#'preamble': '',


# -- Options for HTML output -----------------------------------------------------------------------------------------

# The theme to use for HTML and HTML Help pages.
# You can find available themes here: http://www.sphinx-doc.org/en/master/theming.html

html_theme = 'bootstrap'
html_theme_path=sphinx_bootstrap_theme.get_html_theme_path()

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Defining the static path allows me to add my own logo for the project:
#   (make sure the theme of your choice support the use of logo.
#CHNAGEME# Add a photo of your choice under _static folder, and link to its name here.
html_logo = '_static/WIND-Logo-Red-Screen-Md.png'

# Custom sidebar templates, must be a dictionary that maps document names to template names.
# In This project I chose to include in the sidebar:
#   - Table of Contents: I chose globaltoc as it is less refined,
#     and configured the title by editing the globaltoc template (see explanation above, in the templates_path comment)
#   - Search box: appears below the TOc, and can be configured by editing css attributes.

html_sidebars = {'**': [],}

#html_sidebars = {
#    '**': [
#		'globaltoc.html',
#        'searchbox.html'
#    ]
#}

html_theme_options = {
    # Navigation bar title. (Default: ``project`` value)
    'navbar_title': "Wind River VxWorks and HVP Process Documentation",

    # Tab name for entire site. (Default: "Site")
    'navbar_site_name': "Processes",

    # A list of tuples containing pages or urls to link to.
    # Valid tuples should be in the following forms:
    #    (name, page)                 # a link to a page
    #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
    #    (name, "http://example.com", True) # arbitrary absolute url
    # Note the "1" or "True" value above as the third argument to indicate
    # an arbitrary url.
    'navbar_links': [
        ("Getting Started (WIP)", "./GettingStarted/GettingStarted.html", 1),
        ("Processes by Roles (WIP)", "../../GettingStarted/ByRoles.html", 1),
        ("Generic Plans and Documents", "./GenericPlans/GenericIndex.html", 1),
        ("Work Instructions", "./WorkInstructions/WorkInstructionsIndex.html", 1),        
    ],

    # Render the next and previous page links in navbar. (Default: true)
    'navbar_sidebarrel': True,

    # Render the current pages TOC in the navbar. (Default: true)
    'navbar_pagenav': False,

    # Tab name for the current pages TOC. (Default: "Page")
    'navbar_pagenav_name': "Page",

    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    'globaltoc_depth': 1,
       
    # Include hidden TOCs in Site navbar?
    #
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the build
    # will break.
    #
    # Values: "true" (default) or "false"
    'globaltoc_includehidden': "true",

    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    'navbar_class': "navbar navbar-inverse",

    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': "true",

    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    'source_link_position': "footer",

    # Bootswatch (http://bootswatch.com/) theme.
    #
    # Options are nothing (default) or the name of a valid theme
    # such as "amelia" or "cosmo".
    'bootswatch_theme': "simplex",

    # Choose Bootstrap version.
    # Values: "3" (default) or "2" (in quotes)
    'bootstrap_version': "3",
}
