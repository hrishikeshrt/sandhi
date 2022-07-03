Usage
=====

To use Sanskrit Sandhi in a project,

.. code-block:: python

    import sandhi

    S = sandhi.Sandhi()
    sandhi = S.sandhi("रामः", "राजमणिः")

    # print(sandhi)
    # [['रामो राजमणिः', 'ससजुषो रुः (८।२।६६)-> हशि च (६।१।११४)-> आद् गुणः (६।१।८७)', 'रुत्व-> उत्व-> गुण-सन्धिः']]
