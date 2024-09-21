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


.. moldoc::

    # The content of a moldoc directive is just a Python script
    # which needs to define a moldoc_display_molecule variable.

    import moldoc.molecule as molecule

    atoms = [molecule.Atom(6, (i, 0., 0.)) for i in range(10)]
    bonds = [molecule.Bond(i-1, i, 1) for i in range(1, 10)]

    moldoc_display_molecule = molecule.Molecule(
        atoms=atoms,
        bonds=bonds,
    )

.. moldoc::

    # The content of a moldoc directive is just a Python script
    # which needs to define a moldoc_display_molecule variable.

    import moldoc.molecule as molecule

    atoms = [
        molecule.Atom(7, (0.81017, -0.047, -0.3944)),
        molecule.Atom(6, (-0.5692, -0.046, -0.0024)),
        molecule.Atom(1, (1.22049, 0.8686, -0.0569)),
        molecule.Atom(1, (1.38133, -0.790, 0.09084)),
        molecule.Atom(1, (-0.9453, 1.0112, -0.0206)),
        molecule.Atom(1, (-0.6627, -0.384, 1.06005)),
        molecule.Atom(1, (-1.2344, -0.611, -0.6763)),
    ]
    bonds = [
        molecule.Bond(0, 1, 1.0),
        molecule.Bond(0, 2, 1.0),
        molecule.Bond(0, 3, 1.0),
        molecule.Bond(1, 4, 1.0),
        molecule.Bond(1, 5, 1.0),
        molecule.Bond(1, 6, 1.0),
    ]

    moldoc_display_molecule = molecule.Molecule(
        atoms=atoms,
        bonds=bonds,
        config=molecule.MoleculeConfig(
            atom_scale=1,
        ),
    )

.. moldoc::

    # The content of a moldoc directive is just a Python script
    # which needs to define a moldoc_display_molecule variable.

    import moldoc.molecule as molecule

    atoms = [
        molecule.Atom(7, (0.81017, -0.047, -0.3944)),
        molecule.Atom(6, (-0.5692, -0.046, -0.0024)),
        molecule.Atom(1, (1.22049, 0.8686, -0.0569)),
        molecule.Atom(1, (1.38133, -0.790, 0.09084)),
        molecule.Atom(1, (-0.9453, 1.0112, -0.0206)),
        molecule.Atom(1, (-0.6627, -0.384, 1.06005)),
        molecule.Atom(1, (-1.2344, -0.611, -0.6763)),
    ]
    bonds = [
        molecule.Bond(0, 1, 1.0),
        molecule.Bond(0, 2, 1.0),
        molecule.Bond(0, 3, 1.0),
        molecule.Bond(1, 4, 1.0),
        molecule.Bond(1, 5, 1.0),
        molecule.Bond(1, 6, 1.0),
    ]

    moldoc_display_molecule = molecule.Molecule(
        atoms=atoms,
        bonds=bonds,
        config=molecule.MoleculeConfig(
            atom_scale=1,
            background_color=molecule.Color(255, 0, 0),
            is_outlined=False,
        ),
    )

.. moldoc::

    # The content of a moldoc directive is just a Python script
    # which needs to define a moldoc_display_molecule variable.

    import moldoc.molecule as molecule

    atoms = [
        molecule.Atom(7, (0.81017, -0.047, -0.3944)),
        molecule.Atom(6, (-0.5692, -0.046, -0.0024)),
        molecule.Atom(1, (1.22049, 0.8686, -0.0569)),
        molecule.Atom(1, (1.38133, -0.790, 0.09084)),
        molecule.Atom(1, (-0.9453, 1.0112, -0.0206)),
        molecule.Atom(1, (-0.6627, -0.384, 1.06005)),
        molecule.Atom(1, (-1.2344, -0.611, -0.6763)),
    ]
    bonds = [
        molecule.Bond(0, 1, 1.0),
        molecule.Bond(0, 2, 1.0),
        molecule.Bond(0, 3, 1.0),
        molecule.Bond(1, 4, 1.0),
        molecule.Bond(1, 5, 1.0),
        molecule.Bond(1, 6, 1.0),
    ]

    moldoc_display_molecule = molecule.Molecule(
        atoms=atoms,
        bonds=bonds,
        config=molecule.MoleculeConfig(
            is_outlined=False,
            atom_scale=1,
            material=molecule.MeshLambertMaterial(),
        ),
    )

.. moldoc::

    # The content of a moldoc directive is just a Python script
    # which needs to define a moldoc_display_molecule variable.

    import moldoc.molecule as molecule

    atoms = [
        molecule.Atom(7, (0.81017, -0.047, -0.3944)),
        molecule.Atom(6, (-0.5692, -0.046, -0.0024)),
        molecule.Atom(1, (1.22049, 0.8686, -0.0569)),
        molecule.Atom(1, (1.38133, -0.790, 0.09084)),
        molecule.Atom(1, (-0.9453, 1.0112, -0.0206)),
        molecule.Atom(1, (-0.6627, -0.384, 1.06005)),
        molecule.Atom(1, (-1.2344, -0.611, -0.6763)),
    ]
    bonds = [
        molecule.Bond(0, 1, 1.0),
        molecule.Bond(0, 2, 1.0),
        molecule.Bond(0, 3, 1.0),
        molecule.Bond(1, 4, 1.0),
        molecule.Bond(1, 5, 1.0),
        molecule.Bond(1, 6, 1.0),
    ]

    moldoc_display_molecule = molecule.Molecule(
        atoms=atoms,
        bonds=bonds,
        config=molecule.MoleculeConfig(
            is_outlined=False,
            material=molecule.MeshLambertMaterial(),
        ),
    )

.. moldoc::

    # The content of a moldoc directive is just a Python script
    # which needs to define a moldoc_display_molecule variable.

    import moldoc.molecule as molecule

    atoms = [
        molecule.Atom(7, (0.81017, -0.047, -0.3944)),
        molecule.Atom(6, (-0.5692, -0.046, -0.0024)),
        molecule.Atom(1, (1.22049, 0.8686, -0.0569)),
        molecule.Atom(1, (1.38133, -0.790, 0.09084)),
        molecule.Atom(1, (-0.9453, 1.0112, -0.0206)),
        molecule.Atom(1, (-0.6627, -0.384, 1.06005)),
        molecule.Atom(1, (-1.2344, -0.611, -0.6763)),
    ]
    bonds = [
        molecule.Bond(0, 1, 1.0),
        molecule.Bond(0, 2, 1.0),
        molecule.Bond(0, 3, 1.0),
        molecule.Bond(1, 4, 1.0),
        molecule.Bond(1, 5, 1.0),
        molecule.Bond(1, 6, 1.0),
    ]

    moldoc_display_molecule = molecule.Molecule(
        atoms=atoms,
        bonds=bonds,
        config=molecule.MoleculeConfig(
            is_outlined=False,
            material=molecule.MeshNormalMaterial(),
        ),
    )

.. moldoc::

    # The content of a moldoc directive is just a Python script
    # which needs to define a moldoc_display_molecule variable.

    import moldoc.molecule as molecule

    atoms = [
        molecule.Atom(7, (0.81017, -0.047, -0.3944)),
        molecule.Atom(6, (-0.5692, -0.046, -0.0024)),
        molecule.Atom(1, (1.22049, 0.8686, -0.0569)),
        molecule.Atom(1, (1.38133, -0.790, 0.09084)),
        molecule.Atom(1, (-0.9453, 1.0112, -0.0206)),
        molecule.Atom(1, (-0.6627, -0.384, 1.06005)),
        molecule.Atom(1, (-1.2344, -0.611, -0.6763)),
    ]
    bonds = [
        molecule.Bond(0, 1, 1.0),
        molecule.Bond(0, 2, 1.0),
        molecule.Bond(0, 3, 1.0),
        molecule.Bond(1, 4, 1.0),
        molecule.Bond(1, 5, 1.0),
        molecule.Bond(1, 6, 1.0),
    ]

    moldoc_display_molecule = molecule.Molecule(
        atoms=atoms,
        bonds=bonds,
        config=molecule.MoleculeConfig(
            is_outlined=False,
            material=molecule.MeshPhongMaterial(),
        ),
    )

.. moldoc::

    # The content of a moldoc directive is just a Python script
    # which needs to define a moldoc_display_molecule variable.

    import moldoc.molecule as molecule

    atoms = [
        molecule.Atom(7, (0.81017, -0.047, -0.3944)),
        molecule.Atom(6, (-0.5692, -0.046, -0.0024)),
        molecule.Atom(1, (1.22049, 0.8686, -0.0569)),
        molecule.Atom(1, (1.38133, -0.790, 0.09084)),
        molecule.Atom(1, (-0.9453, 1.0112, -0.0206)),
        molecule.Atom(1, (-0.6627, -0.384, 1.06005)),
        molecule.Atom(1, (-1.2344, -0.611, -0.6763)),
    ]
    bonds = [
        molecule.Bond(0, 1, 1.0),
        molecule.Bond(0, 2, 1.0),
        molecule.Bond(0, 3, 1.0),
        molecule.Bond(1, 4, 1.0),
        molecule.Bond(1, 5, 1.0),
        molecule.Bond(1, 6, 1.0),
    ]

    moldoc_display_molecule = molecule.Molecule(
        atoms=atoms,
        bonds=bonds,
        config=molecule.MoleculeConfig(
            is_outlined=False,
            material=molecule.MeshPhongMaterial(
                shininess=1.,
                reflectivity=1.,
                flat_shading=True,
            ),
        ),
    )

.. moldoc::

    # The content of a moldoc directive is just a Python script
    # which needs to define a moldoc_display_molecule variable.

    import moldoc.molecule as molecule

    atoms = [
        molecule.Atom(7, (0.81017, -0.047, -0.3944)),
        molecule.Atom(6, (-0.5692, -0.046, -0.0024)),
        molecule.Atom(1, (1.22049, 0.8686, -0.0569)),
        molecule.Atom(1, (1.38133, -0.790, 0.09084)),
        molecule.Atom(1, (-0.9453, 1.0112, -0.0206)),
        molecule.Atom(1, (-0.6627, -0.384, 1.06005)),
        molecule.Atom(1, (-1.2344, -0.611, -0.6763)),
    ]
    bonds = [
        molecule.Bond(0, 1, 1.0),
        molecule.Bond(0, 2, 1.0),
        molecule.Bond(0, 3, 1.0),
        molecule.Bond(1, 4, 1.0),
        molecule.Bond(1, 5, 1.0),
        molecule.Bond(1, 6, 1.0),
    ]

    moldoc_display_molecule = molecule.Molecule(
        atoms=atoms,
        bonds=bonds,
        config=molecule.MoleculeConfig(
            is_outlined=False,
            material=molecule.MeshPhysicalMaterial(
                clearcoat=0,
                clearcoat_roughness=0.5,
                roughness=0.4,
                metalness=0.5,
                flat_shading=True,
            ),
        ),
    )

.. moldoc::

    # The content of a moldoc directive is just a Python script
    # which needs to define a moldoc_display_molecule variable.

    import moldoc.molecule as molecule

    atoms = [
        molecule.Atom(7, (0.81017, -0.047, -0.3944)),
        molecule.Atom(6, (-0.5692, -0.046, -0.0024)),
        molecule.Atom(1, (1.22049, 0.8686, -0.0569)),
        molecule.Atom(1, (1.38133, -0.790, 0.09084)),
        molecule.Atom(1, (-0.9453, 1.0112, -0.0206)),
        molecule.Atom(1, (-0.6627, -0.384, 1.06005)),
        molecule.Atom(1, (-1.2344, -0.611, -0.6763)),
    ]
    bonds = [
        molecule.Bond(0, 1, 1.0),
        molecule.Bond(0, 2, 1.0),
        molecule.Bond(0, 3, 1.0),
        molecule.Bond(1, 4, 1.0),
        molecule.Bond(1, 5, 1.0),
        molecule.Bond(1, 6, 1.0),
    ]

    moldoc_display_molecule = molecule.Molecule(
        atoms=atoms,
        bonds=bonds,
        config=molecule.MoleculeConfig(
            is_outlined=False,
            material=molecule.MeshStandardMaterial(
                metalness=0.3,
                roughness=0.2,
                flat_shading=True,
            ),
        ),
    )


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
