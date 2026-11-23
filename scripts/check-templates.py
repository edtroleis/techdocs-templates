"""Checks the templates: front matter, category, example page, and the same files in every language."""
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
FOLDERS = {"tutorial": "tutorials", "guide": "how-to-guides", "reference": "reference", "explanation": "explanation"}
errors = []


def files(base: pathlib.Path) -> set:
    return {p.relative_to(base).as_posix() for p in base.rglob("*") if p.is_file()}


languages = sorted(p.name for p in (ROOT / "templates").iterdir() if p.is_dir())
for kind in ("templates", "examples"):
    first = files(ROOT / kind / languages[0])
    for language in languages[1:]:
        other = files(ROOT / kind / language)
        for missing in sorted(first ^ other):
            errors.append(f"{kind}: {missing} is not in every language")

for language in languages:
    for page in sorted((ROOT / "templates" / language).glob("*/*.md")):
        if page.parent.name == "sites":
            continue
        text = page.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"{page}: no front matter")
            continue
        meta = yaml.safe_load(text.split("---\n")[1]).get("template", {})
        for key in ("version", "name", "description", "category"):
            if key not in meta:
                errors.append(f"{page}: template.{key} is missing")
        if FOLDERS.get(meta.get("category")) != page.parent.name:
            errors.append(f"{page}: category {meta.get('category')!r} does not match the folder {page.parent.name}")
        example = meta.get("example")
        if example and not (ROOT / "examples" / language / "docs" / example).is_file():
            errors.append(f"{page}: example {example} does not exist")
    for site in sorted((ROOT / "templates" / language / "sites").iterdir()):
        spec = yaml.safe_load((site / "template.yml").read_text(encoding="utf-8"))
        for entry in spec.get("files", []):
            source = entry.get("source")
            if source and not (site / source).is_file():
                errors.append(f"{site}: {source} does not exist")

print("\n".join(errors) or "templates ok")
sys.exit(1 if errors else 0)
