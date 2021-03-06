utterson
=========

tl;dr;
-------

Utterson is a ncurses based management UI for Jekyll based sites. A specific 
set of conventions are defined and followed allowing utterson to manage many 
aspects of a Jekyll site.

ntl;
-----

Utterson is primarily a management wrapper for blogs and sites that leverage 
Jekyll. Jekyll is a static site generation tool that is blog aware. At it's 
core, Jekyll is just a transformation engine that takes text files written 
in specific markup languages and converts them to a static web site. Jekyll is
very flexible, allowing the end users to leverage it in any way they would like. 
This flexibility does come at a cost, Jekyll only provides the raw tools to 
build a blog or site. Standardized management tools and gui's do not fit into 
the Jekyll mindset. Those are layers the end user is expected to design and 
implement.

Utterson was created specifically to provide a single convention for a Jekyll 
based site. By standardizing on a single convention, a management interface 
could be written that allows for automation of many tasks. Interestingly, the 
full power of Jekyll is still available but by following the conventions users
can take advantage of the management functionality utterson provides.

Utterson was initially created to manage a personal blog. The choice of python
and ncurses was simply for shell based management and because why not. Any 
and all enhancement ideas are welcomed.  

Documentation
======================

All documentation can be found at the following GitHub repo:
<https://github.com/jrmycanady/Utterson>