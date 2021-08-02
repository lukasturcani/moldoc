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

.. moldoc::

    import moldoc.molecule as molecule

    moldoc_display_molecule = molecule.Molecule(
        atoms=(
            molecule.Atom(7, (i, 0., 0.))
            for i in range(4)
        ),
        bonds=(
            molecule.Bond(0, 1, 1),
            molecule.Bond(1, 2, 1),
            molecule.Bond(2, 3, 1),
        ),
    )

.. moldoc::

    # The content of a moldoc directive is just a Python script
    # which needs to define a moldoc_display_molecule variable.

    import moldoc.molecule as molecule

    moldoc_display_molecule = molecule.Molecule(
        atoms=(
            # molecule.Atom(atomic_number, position)
            molecule.Atom(6, (-0.06, -0.17, 0.)),
            molecule.Atom(17, (-1.35, 1.04, -0.04)),
            molecule.Atom(35, (1.65, 0.73, -0.06)),
            molecule.Atom(1, (-0.15, -0.88, -0.87)),
            molecule.Atom(1, (-0.09, -0.72, 0.97)),
        ),
        bonds=(
            # molecule.Bond(atom1_id, atom2_id, order)
            molecule.Bond(0, 1, 1),
            molecule.Bond(0, 2, 1),
            molecule.Bond(0, 3, 1),
            molecule.Bond(0, 4, 1),
        ),
    )


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
