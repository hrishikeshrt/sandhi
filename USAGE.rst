Usage
=====

To use Sanskrit Sandhi **as a library**,

.. code-block:: python

    import sandhi

    S = sandhi.Sandhi()
    sandhi = S.sandhi("रामः", "राजमणिः")

    # print(sandhi)
    # [['रामो राजमणिः', 'ससजुषो रुः (८।२।६६)-> हशि च (६।१।११४)-> आद् गुणः (६।१।८७)', 'रुत्व-> उत्व-> गुण-सन्धिः']]


Command-line usage
==================

After installation, a ``sandhi`` command is available:

.. code-block:: console

    $ sandhi रामः राजमणिः
    1. रामो राजमणिः | ससजुषो रुः (८।२।६६)-> हशि च (६।१।११४)-> आद् गुणः (६।१।८७) | रुत्व-> उत्व-> गुण-सन्धिः

To print only the resulting forms (without sutra and sandhi type), use:

.. code-block:: console

    $ sandhi --quiet रामः राजमणिः
    रामो राजमणिः
