#!/usr/bin/env python3
"""
Bundle the voice pack: one zip with the recordings, names.tsv, templates.tsv and the
Lua module, in the folder layout of the game install, plus MAW-NPC-Voices-EN-INSTALL.txt, -LICENSE.txt and a .sha256 file.

    python -I pack_voices.py --out ../../Data/Voices/MAW-NPC-Voices-EN-1.0.0.zip

INSTALL.txt and LICENSE.txt come from the repository root.
Defaults: recordings, names.tsv, templates.tsv and pics.tsv from <repository>/Data/Voices, the module from
<repository>/Scripts/General/zzzMaw_NPCVoices.lua. Run it from Tools/Voice; it needs
no packages.
"""

import argparse
import hashlib
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent



def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--voices", type=Path, default=HERE.parent.parent / "Data" / "Voices",
                    help="folder with NPC/ (the recordings), names.tsv and templates.tsv")
    ap.add_argument("--module", type=Path, default=HERE.parent.parent / "Scripts" / "General" / "zzzMaw_NPCVoices.lua")
    ap.add_argument("--out", required=True, type=Path, help="the zip to write (a .sha256 file goes next to it)")
    args = ap.parse_args(argv)

    npc_dir, names, patterns, pics = args.voices / "NPC", args.voices / "names.tsv", args.voices / "templates.tsv", args.voices / "pics.tsv"
    docs = [HERE.parent.parent / "INSTALL.txt", HERE.parent.parent / "LICENSE.txt"]
    recordings = sorted(p for p in npc_dir.glob("*") if p.suffix in (".ogg", ".wav"))
    for needed, what in ((names, "names.tsv"), (patterns, "templates.tsv"), (args.module, "the Lua module"), (pics, "pics.tsv"),
                         (docs[0], "INSTALL.txt"), (docs[1], "LICENSE.txt")):
        if not needed.is_file():
            print(f"missing {what}: {needed}", file=sys.stderr)
            return 1
    if not recordings:
        print(f"no recordings in {npc_dir}", file=sys.stderr)
        return 1

    with zipfile.ZipFile(args.out, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for doc in docs:
            z.write(doc, "MAW-NPC-Voices-EN-" + doc.name)  # a prefix: the German edition has its own INSTALL.txt
        z.write(args.module, "Scripts/General/zzzMaw_NPCVoices.lua")
        z.write(names, "Data/Voices/names.tsv")
        z.write(patterns, "Data/Voices/templates.tsv")
        z.write(pics, "Data/Voices/pics.tsv")
        for p in recordings:
            z.write(p, "Data/Voices/NPC/" + p.name)
    with zipfile.ZipFile(args.out) as z:
        if z.testzip() is not None:
            print("the zip is damaged", file=sys.stderr)
            return 1
        entries = len(z.namelist())
    digest = sha256(args.out)
    args.out.with_name(args.out.name + ".sha256").write_text(f"{digest} *{args.out.name}\n", encoding="ascii")
    print(f"{args.out}: {entries} entries, {args.out.stat().st_size / 1e6:.1f} MB, sha256 {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
