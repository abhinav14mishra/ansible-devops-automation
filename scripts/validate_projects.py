from pathlib import Path
projects=sorted(Path("queue").glob("[0-9][0-9][0-9]_*"))
assert len(projects)==100, f"Expected 100 projects, found {len(projects)}"
required={"site.yml","inventory","README.md"}
for p in projects:
    missing=required-{x.name for x in p.iterdir()}
    assert not missing, f"{p}: missing {sorted(missing)}"
print("Validated 100 Ansible projects.")
