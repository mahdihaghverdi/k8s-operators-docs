import json
import logging
import pprint
import shutil
import tomllib
from pathlib import Path

logger = logging.getLogger("generator")

ROOT = Path(__file__).parent.parent
DOCS = ROOT / "docs"


def load_operators():
    with open(ROOT / "operators.config.toml", "rb") as f:
        return tomllib.load(f)["operators"]


def copy_docs(operators: list[dict]):
    for operator in operators:
        operator_name = operator["name"]
        source = ROOT / operator_name / "docs"
        target = DOCS / operator_name
        shutil.copytree(source, target)


def add_operator_name_to_file_paths(nav_dict: dict, operator_name: str) -> dict:
    edit_path = lambda p: operator_name + "/" + p

    for k, v in nav_dict.items():
        if isinstance(v, str):
            nav_dict[k] = edit_path(v)
        elif isinstance(v, list):
            nav_dict[k] = [edit_path(v_) for v_ in v]
        elif isinstance(v, dict):
            nav_dict[k] = add_operator_name_to_file_paths(v, operator_name)

    return nav_dict

def create_the_canonical_nav(operators: list[dict]) -> list[dict]:
    ZENSICAL_NAV_CONF = "zensical.nav.txt"
    nav = []
    with open(ROOT / ZENSICAL_NAV_CONF) as f:
        nav.extend(eval(f.read()))

    for operator in operators:
        operator_name = operator["name"]
        with open(ROOT / operator_name / ZENSICAL_NAV_CONF) as f:
            nav_list = eval(f.read())
            for dict_ in nav_list:
                add_operator_name_to_file_paths(dict_, operator_name)
            nav.append({operator_name: nav_list})
    return nav


def make_nav_toml_acceptable(nav: list[dict]) -> str:
    toml_acceptable_nav = "nav = " + json.dumps(nav, indent=4).replace(":", ' =') + "\n\n"
    return toml_acceptable_nav


def create_zensical_toml(toml_acceptable_nav: str):
    lines = []
    with (
        open(ROOT / "project.section.txt") as f,
        open(ROOT / "project.theme.txt") as theme,
        open(ROOT / "project.extensions.txt") as extensions,
    ):
        lines.extend(f.readlines())
        lines.append(toml_acceptable_nav)
        lines.extend(theme.readlines())
        lines.extend(extensions.readlines())

    with open("zensical.toml", "w") as f:
        f.writelines(lines)

    with open("zensical.toml") as f:
        pprint.pprint(f.readlines())


def main():
    operators = load_operators()

    copy_docs(operators)
    canonical_nav = create_the_canonical_nav(operators)
    toml_acceptable_nav = make_nav_toml_acceptable(canonical_nav)

    create_zensical_toml(toml_acceptable_nav)


if __name__ == "__main__":
    main()