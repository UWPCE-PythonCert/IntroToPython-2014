.. _supplement_git_states:

============
git Overview
============


Resources
=========

.. rst-class:: left
    Here are few good places to look for more info about using git:


    **Pro git**

    The semi-offical documentation -- the first few chapters are worth going through:

    https://git-scm.com/book/en

    Reading suggested at the end of session 1:
    
    http://rogerdudler.github.io/git-guide/


    https://try.github.io/levels/1/challenges/1
    
    
    ** git Branching: getting fancy **
    
    Interactive tutorial about branching -- try it right in the browser!

    http://pcottle.github.io/learnGitBranching/


A Graphical Tutorial
====================

A Picture of git
----------------

.. figure:: /_static/git_simple_timeline.png
    :width: 80%
    :class: center

.. rst-class:: build
.. container::

    A git repository is a set of points in time, with history showing where
    you've been.

    Each point has a *name* (here *A*, *B*, *C*) that uniquely identifies it,
    called a *hash*

    The path from one point to the previous is represented by the *difference*
    between the two points.

.. nextslide::

.. figure:: /_static/git_head.png
    :width: 75%
    :class: center

.. rst-class:: build
.. container::

    Each point in time can also have a label that points to it.

    One of these is *HEAD*, which always points to the place in the timeline
    that you are currently looking at.

.. nextslide::

.. figure:: /_static/git_master_branch.png
    :width: 75%
    :class: center

.. rst-class:: build
.. container::

    You may also be familiar with the label "master".

    This is the name that git automatically gives to the first *branch* in a
    repository.

    A *branch* is actually just a label that points to a specific point in
    time.

.. nextslide::

.. figure:: /_static/git_new_commit.png
    :width: 75%
    :class: center

.. rst-class:: build
.. container::

    When you make a *commit* in git, you add a new point to the timeline.

    The HEAD label moves to this new point.

    So does the label for the *branch* you are on.

.. nextslide:: Making a Branch

.. figure:: /_static/git_new_branch.png
    :width: 75%
    :class: center

.. rst-class:: build
.. container::

    You can make a new *branch* with the ``branch`` command.

    This adds a new label to the current commit.

    Notice that it *does not* check out that branch.

.. nextslide:: Making a Branch

.. figure:: /_static/git_checkout_branch.png
    :width: 75%
    :class: center

.. rst-class:: build
.. container::

    You can use the ``checkout`` command to switch to the new branch.

    This associates the HEAD label with the *session01* label.

    Use ``git branch`` to see which branch is *active*::

        $ git branch
          master
        * session01

.. nextslide:: Making a Branch

.. figure:: /_static/git_commit_on_branch.png
    :width: 75%
    :class: center

.. rst-class:: build
.. container::

    While it is checked out, new commits move the *session01* label.

    Notice that HEAD is *always* the same as "where you are now"

.. nextslide:: Making a Branch

You can use this to switch between branches and make changes in isolation.

.. rst-class:: build
.. container::

    .. figure:: /_static/git_checkout_master.png
        :width: 75%
        :class: center

    .. figure:: /_static/git_new_commit_on_master.png
        :width: 75%
        :class: center

.. nextslide:: Merging Branches

.. rst-class:: build
.. container::

    Branching allows you to keep related sets of work separate from each-other.

    In class here, you can use it to do your exercises for each session.

    Simply create a new branch for each session from your repository master
    branch.

    Do your work on that branch, and then you can issue a **pull request** in
    github to have your work evaluated.

    This is very much like how teams work in the "real world" so learning it
    here will help you.

    The final step in the process is merging your work.

.. nextslide:: Merging Branches

The ``merge`` command allows you to *combine* your work on one branch with the
work on another.

.. rst-class:: build
.. container::

    It creates a new commit which reconciles the differences:

    .. figure:: /_static/git_merge_commit.png
        :width: 75%
        :class: center

    Notice that this commit has **two** parents.


.. nextslide:: Conflicts

.. rst-class:: build
.. container::

    Sometimes when you ``merge`` two branches, you get *conflicts*.

    This happens when the same file was changed in about the same place in two
    different ways.

    Often, git can work these types of things out on its own, but if not,
    you'll need to manually edit files to fix the problem.

    You'll be helped by the fact that git will tell you which files are in
    conflict.

    Just open those files and look for conflict markers:

        * <<<<<<<<< *hash1* (stuff from the current branch)
        * ========= (the pivot point between two branches' content)
        * >>>>>>>>> *hash2* (stuff from the branch being merged)

.. nextslide:: Conflicts

Your job in fixing a conflict is to decide exactly what to keep.

You can (and should) communicate with others on your team when doing this.

Always remember to remove the conflict markers too.  They are not syntactic
code in any language and will cause errors.

Once a conflict is resolved, you can ``git add`` the file back and then commit
the merge.
