.. moldoc-test documentation master file, created by
   sphinx-quickstart on Fri Jul 30 17:53:00 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to moldoc-test's documentation!
=======================================

.. toctree::
  :maxdepth: 2
  :caption: Contents:

  nest/index.rst
  nest/foo.rst
  nest/nest/index.rst
  nest/nest/nest/index.rst
  nest/nest/nest/nest/index.rst
  nest/nest/nest/nest/nest/index.rst

.. moldoc::

    import rdkit.Chem as rdkit
    moldoc_display_molecule = rdkit.MolFromSmiles("CCCC")

.. moldoc::

    import rdkit.Chem as rdkit
    moldoc_display_molecule = rdkit.MolFromSmiles("NNNN")

.. moldoc::

    import rdkit.Chem as rdkit
    moldoc_display_molecule = rdkit.MolFromSmiles("Brc1ccc(Br)cc1")
    moldoc_script = """
        let config = {
            backgroundAlpha: 0.0,
            backgroundColor: 'transparent',
        };
        let viewer = $3Dmol.createViewer(element, config);
        let model = viewer.addModel(data, 'sdf');
        model.setStyle({}, {sphere: {}});
        model.setStyle({}, {stick: {}}, true);
        viewer.zoomTo();
        viewer.render();
    """

.. moldoc::

    import rdkit.Chem as rdkit
    moldoc_display_molecule = rdkit.MolFromSmiles("Brc1ccc(Br)cc1")
    moldoc_script = """
        let config = {
            backgroundAlpha: 0.0,
            backgroundColor: 'orange',
        };
        let viewer = $3Dmol.createViewer(element, config);
        let model = viewer.addModel(data, 'sdf');
        model.setStyle({}, {sphere: {scale: 0.33}});
        model.setStyle({}, {stick: {}}, true);
        viewer.zoomTo();
        viewer.render();
    """

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
