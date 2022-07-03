===============
Sanskrit Sandhi
===============


.. image:: https://img.shields.io/pypi/v/sandhi
        :target: https://pypi.python.org/pypi/sandhi


.. image:: https://readthedocs.org/projects/sandhi/badge/?version=latest
        :target: https://sandhi.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/pypi/pyversions/sandhi
        :target: https://pypi.python.org/pypi/sandhi
        :alt: Python Version Support

.. image:: https://img.shields.io/github/issues/hrishikeshrt/sandhi
        :target: https://github.com/hrishikeshrt/sandhi/issues
        :alt: GitHub Issues

.. image:: https://img.shields.io/github/followers/hrishikeshrt?style=social
        :target: https://github.com/hrishikeshrt
        :alt: GitHub Followers


.. image:: https://img.shields.io/twitter/follow/hrishikeshrt?style=social
        :target: https://twitter.com/hrishikeshrt
        :alt: Twitter Followers



Sanskrit Sandhi Module


* Free software: GNU General Public License v3
* Documentation: https://sandhi.readthedocs.io.


Features
========

* Form Sandhi using Ashtadhyayi Rules

Install
=======

To install Sanskrit Sandhi, run this command in your terminal:

.. code-block:: console

    $ pip install sandhi

Usage
=====

To use Sanskrit Sandhi in a project,

.. code-block:: python

    import sandhi

    S = sandhi.Sandhi()
    sandhi = S.sandhi("रामः", "राजमणिः")

    # print(sandhi)
    # [['रामो राजमणिः', 'ससजुषो रुः (८।२।६६)-> हशि च (६।१।११४)-> आद् गुणः (६।१।८७)', 'रुत्व-> उत्व-> गुण-सन्धिः']]

Credits
=======

* This package was converted from Perl version obtainable from Samsaadhanii_
* This package was created with Cookiecutter_ and the `hrishikeshrt/cookiecutter-pypackage`_ project template.

.. _Samsaadhanii: https://github.com/samsaadhanii/scl
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`hrishikeshrt/cookiecutter-pypackage`: https://github.com/hrishikeshrt/cookiecutter-pypackage
