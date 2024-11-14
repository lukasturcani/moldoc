import pkgutil
import typing

from docutils import nodes
from rdkit import Chem
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx.util.docutils import SphinxDirective
from sphinx.writers.html5 import HTML5Translator

from moldoc.version import __version__


class MolDocNode(nodes.Body, nodes.Element):
    def __init__(
        self,
        moldoc_name: str,
        molecule: Chem.Mol,
        container: dict[str, str],
        script: str,
    ) -> None:
        super().__init__()
        self.moldoc_name = moldoc_name
        self.molecule = molecule
        self.container = container
        self.script = script


DEFAULT_SCRIPT = """
let viewer = $3Dmol.createViewer(element);
let model = viewer.addModel(data, 'sdf');
model.setStyle({}, {sphere: {scale: 0.33}});
model.setStyle({}, {stick: {}}, true);
viewer.zoomTo();
viewer.render();
"""


class MolDoc(SphinxDirective):
    has_content = True

    def run(self) -> list[MolDocNode]:
        content = "\n".join(self.content)
        globals_: dict[str, typing.Any] = {}
        exec(content, globals_)  # noqa: S102
        node = MolDocNode(
            moldoc_name=f'moldoc_{self.env.new_serialno("moldoc")}',
            molecule=globals_["moldoc_display_molecule"],
            container=globals_.get(
                "moldoc_container_attributes",
                {
                    "style": "width: 60%; height: 400px; position: relative;",
                },
            ),
            script=globals_.get("moldoc_script", DEFAULT_SCRIPT),
        )

        if not hasattr(self.env, "moldoc_documents"):
            self.env.moldoc_documents = set()  # type: ignore[attr-defined]

        self.env.moldoc_documents.add(self.env.docname)  # type: ignore[attr-defined]
        return [node]


def _format_attribute(key: str, value: str) -> str:
    return f'{key}="{value}"'


def _format_attributes(attributes: dict[str, str]) -> str:
    return " ".join(
        _format_attribute(key, value) for key, value in attributes.items()
    )


def html_moldoc(self: HTML5Translator, node: MolDocNode) -> None:
    if not getattr(self, "moldoc_scripts_added", False):
        self.body.append("<script>let moldoc_molecules=[];</script>")
        self.moldoc_scripts_added = True

    attributes = _format_attributes(node.container)
    molecule_sdf = Chem.MolToMolBlock(node.molecule, forceV3000=True)
    self.body.append(
        f'<div id="{node.moldoc_name}" {attributes}></div>'
        "<script>{"
        "const drawMol = () => {"
        f"let element = document.querySelector('#{node.moldoc_name}');"
        f"let data = `{molecule_sdf}`;"
        f"{node.script}"
        "};"
        "if (typeof $3Dmol === 'undefined') { "
        "moldoc_molecules.push(drawMol); } else { drawMol() }"
        "}</script>"
    )
    raise nodes.SkipNode


def copy_asset_files(app: Sphinx, exc: Exception | None) -> None:
    asset_file = "3Dmol.min.js"
    static_dir = app.builder.outdir / "_static"
    # Build is HTML and succeeded.
    if app.builder.format == "html" and exc is None:
        with static_dir.joinpath(asset_file).open("wb") as f:
            if (data := pkgutil.get_data(__package__, asset_file)) is not None:
                f.write(data)
            else:
                msg = f"{asset_file} not found"
                raise RuntimeError(msg)


def add_moldoc_scripts(
    app: Sphinx,
    pagename: str,
    templatename: str,  # noqa: ARG001
    context: dict[str, typing.Any],  # noqa: ARG001
    doctree: nodes.document,  # noqa: ARG001
) -> None:
    if (
        hasattr(app.env, "moldoc_documents")
        and pagename in app.env.moldoc_documents
    ):
        app.add_js_file("3Dmol.min.js")
        app.add_js_file(
            None,
            body=(
                "if (typeof moldoc_molecules !== 'undefined')"
                "{moldoc_molecules.forEach(f=>f());}"
            ),
        )


def purge_moldoc_documents(
    app: Sphinx,  # noqa: ARG001
    env: BuildEnvironment,
    docnames: list[str],
) -> None:
    if hasattr(env, "moldoc_documents"):
        env.moldoc_documents.difference_update(docnames)


def merge_moldoc_documents(
    app: Sphinx,  # noqa: ARG001
    env: BuildEnvironment,
    docnames: list[str],  # noqa: ARG001
    other: BuildEnvironment,
) -> None:
    if not hasattr(env, "moldoc_documents"):
        env.moldoc_documents = set()  # type: ignore[attr-defined]
    if hasattr(other, "moldoc_documents"):
        env.moldoc_documents.update(other.moldoc_documents)  # type: ignore[attr-defined]


def setup(app: Sphinx) -> dict:
    app.connect("build-finished", copy_asset_files)
    app.connect("html-page-context", add_moldoc_scripts)
    app.connect("env-purge-doc", purge_moldoc_documents)
    app.connect("env-merge-info", merge_moldoc_documents)
    app.add_directive("moldoc", MolDoc)
    app.add_node(
        node=MolDocNode,
        html=(html_moldoc, None),
    )
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
