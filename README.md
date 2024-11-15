[!TIP]
If you like ``moldoc`` remember to give it a star!

# Introduction

`moldoc` is a Sphinx extension for making better chemistry documentation. It
allows you to embed 3D, interactive models of molecules directly into your
compiled docs. You can see it being used in the
[stk](https://stk.readthedocs.io/en/stable/basic_examples.html) docs.

![moldoc](moldoc.gif)

It is based on https://github.com/3dmol/3Dmol.js, so anything you can draw
with `3Dmol.js` you can draw in your Python docs!

# Installation

First, run

```bash
pip install moldoc
```

and then add it to your extensions in `conf.py`

```python
extensions = [
    'moldoc',
]
```

# Adding Molecules into Your Docs

You can define molecules you show with the `moldoc` directive, which you  can
place it into your `rst` files

```rst
.. moldoc::

    import rdkit.Chem as rdkit
    moldoc_display_molecule = rdkit.MolFromSmiles("Brc1ccc(Br)cc1")
```

See result `here <https://moldoc.readthedocs.io/en/stable#adding-molecules-into-your-docs>`_

or in your Python docstrings

```python
def some_fn():
    """
    Do something.

    .. moldoc::

        import rdkit.Chem as rdkit
        moldoc_display_molecule = rdkit.MolFromSmiles("Brc1ccc(Br)cc1")

    """

    print('In some_fn()')
```

Note that the content in the `moldoc` directive is a just a Python script,
which has to define a `moldoc_display_molecule` variable holding a `rdkit.Mol`
object.

Because the content of a `moldoc` directive is just a Python script you can
define your molecules programatically

```python
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

```

# Configuration

See our [docs](https://moldoc.readthedocs.io/en/stable)!
