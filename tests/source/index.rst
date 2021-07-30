.. moldoc-test documentation master file, created by
   sphinx-quickstart on Fri Jul 30 17:53:00 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to moldoc-test's documentation!
=======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


.. moldoc::


    import moldoc.molecule as molecule

    moldoc_display_molecule = molecule.Molecule(
        atoms=(
            molecule.Atom(6, (0., 0., 0.)),
            molecule.Atom(6, (1., 0., 0.)),
            molecule.Atom(6, (2., 0., 0.)),
            molecule.Atom(6, (3., 0., 0.)),
        ),
        bonds=(
            molecule.Bond(0, 1, 1),
            molecule.Bond(1, 2, 1),
            molecule.Bond(2, 3, 1),
        ),
    )



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
