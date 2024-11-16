.. moldoc documentation master file, created by
   sphinx-quickstart on Thu Oct 19 15:55:32 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to moldoc's documentation!
==================================

.. toctree::
  :hidden:
  :maxdepth: 2
  :caption: Contents:

  Modules <modules>

.. tip::

    ⭐If you like ``moldoc`` remember to give it a star!⭐

Introduction
------------

``moldoc`` is a Sphinx extension for making better chemistry documentation. It
allows you to embed 3D, interactive models of molecules directly into your
compiled docs. Like this!

.. moldoc::

    import rdkit.Chem as rdkit
    moldoc_display_molecule = rdkit.AddHs(rdkit.MolFromSmiles("Brc1ccc(Br)cc1"))
    moldoc_script = """
        let config = {
            backgroundAlpha: 0.0,
            backgroundColor: 'transparent',
        };
        let viewer = $3Dmol.createViewer(element, config);
        let model = viewer.addModel(data, 'sdf');
        model.setStyle({}, {sphere: {scale: 0.33}});
        model.setStyle({}, {stick: {}}, true);
        viewer.zoomTo();
        viewer.render();
        viewer.spin();
    """


It is based on https://github.com/3dmol/3Dmol.js, so anything you can draw
with ``3Dmol.js`` you can draw in your Python docs!

Installation
------------

First, run:

.. code-block:: bash

    pip install moldoc

and then add it to your extensions in ``conf.py``:

.. code-block:: python

    extensions = [
        "moldoc",
    ]

Adding Molecules into Your Docs
-------------------------------

You can define molecules you show with the ``moldoc`` directive, which you  can
place it into your ``rst`` files:

.. code-block:: rst

    .. moldoc::

        import rdkit.Chem as rdkit
        moldoc_display_molecule = rdkit.MolFromSmiles("Brc1ccc(Br)cc1")

.. moldoc::

    import rdkit.Chem as rdkit
    moldoc_display_molecule = rdkit.MolFromSmiles("Brc1ccc(Br)cc1")

.. _adding-molecules-into-your-docs-2:

or in your Python docstrings:

.. code-block:: python

    def some_fn():
        """
        Do something.

        .. moldoc::

            import rdkit.Chem.AllChem as rdkit
            mol = rdkit.AddHs(rdkit.MolFromSmiles("BrC1CCC(N)CC1"))
            rdkit.EmbedMolecule(mol, rdkit.ETKDGv3())
            moldoc_display_molecule = mol

        """

        print('In some_fn()')

.. moldoc::

    import rdkit.Chem.AllChem as rdkit
    mol = rdkit.AddHs(rdkit.MolFromSmiles("BrC1CCC(N)CC1"))
    rdkit.EmbedMolecule(mol, rdkit.ETKDGv3())
    moldoc_display_molecule = mol

Note that the content in the ``moldoc`` directive is a just a Python script,
which has to define a ``moldoc_display_molecule`` variable holding an
``rdkit.Mol`` object.

.. tip::

    You do not have to define an ``rdkit`` object if you don't want, you can
    also define a :class:`moldoc.molecule.Molecule`, which simply takes a list
    of atoms, bonds and positions. See an example `here <avoiding-rdkit>`_

.. _adding-molecules-into-your-docs-3:

Because the content of a ``moldoc`` directive is just a Python script you can
define your molecules programatically:

.. code-block:: python

    def some_fn():
        """
        Do something.

        .. moldoc::

            import stk

            bb1 = stk.BuildingBlock(
                smiles='NCCN',
                functional_groups=[stk.PrimaryAminoFactory()],
            )
            bb2 = stk.BuildingBlock(
                smiles='O=CC(C=O)C=O',
                functional_groups=[stk.AldehydeFactory()],
            )
            cage = stk.ConstructedMolecule(
                topology_graph=stk.cage.FourPlusSix(
                    building_blocks=(bb1, bb2),
                    optimizer=stk.MCHammer(),
                ),
            )
            moldoc_display_molecule = cage.to_rdkit_mol()

        """
        print('In some_fn()')

.. moldoc::

    import stk

    bb1 = stk.BuildingBlock(
        smiles='NCCN',
        functional_groups=[stk.PrimaryAminoFactory()],
    )
    bb2 = stk.BuildingBlock(
        smiles='O=CC(C=O)C=O',
        functional_groups=[stk.AldehydeFactory()],
    )
    cage = stk.ConstructedMolecule(
        topology_graph=stk.cage.FourPlusSix(
            building_blocks=(bb1, bb2),
            optimizer=stk.MCHammer(),
        ),
    )
    moldoc_display_molecule = cage.to_rdkit_mol()

Configuration
-------------

Using a script
..............

``moldoc`` lets you edit the `3Dmol.js <https://github.com/3dmol/3Dmol.js>`_
script that you want to use with the ``moldoc_script`` variable. This will
override the default ``moldoc`` script which means you can customize every
aspect of the rendering by using `3Dmol.js <https://github.com/3dmol/3Dmol.js>`_
directly. For example, this is how you enable auto-rotation:

.. code-block:: rst

    .. moldoc::

        import rdkit.Chem as rdkit
        moldoc_display_molecule = rdkit.AddHs(rdkit.MolFromSmiles("Brc1ccc(Br)cc1"))
        moldoc_script = """
            let config = {
                backgroundAlpha: 0.0,
                backgroundColor: 'transparent',
            };
            let viewer = $3Dmol.createViewer(element, config);
            let model = viewer.addModel(data, 'sdf');
            model.setStyle({}, {sphere: {scale: 0.33}});
            model.setStyle({}, {stick: {}}, true);
            viewer.zoomTo();
            viewer.render();
            viewer.spin();
        """

.. moldoc::

    import rdkit.Chem as rdkit
    moldoc_display_molecule = rdkit.AddHs(rdkit.MolFromSmiles("Brc1ccc(Br)cc1"))
    moldoc_script = """
        let config = {
            backgroundAlpha: 0.0,
            backgroundColor: 'transparent',
        };
        let viewer = $3Dmol.createViewer(element, config);
        let model = viewer.addModel(data, 'sdf');
        model.setStyle({}, {sphere: {scale: 0.33}});
        model.setStyle({}, {stick: {}}, true);
        viewer.zoomTo();
        viewer.render();
        viewer.spin();
    """

Avoiding rdkit
..............

Sometimes you may want to avoid using ``rdkit`` because it has valence
restrictions or it just does not fit your workflow. In those cases you can use
:class:`moldoc.molecule.Molecule`, which simply holds a list atoms, bonds and
their positions:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
