#!/usr/bin/env python3
"""Post-process a broadcast .md to add player/team spans, run-spans, and
sb-tag pills linking every tagged PA back to the game-log anchor.

Usage: tag-broadcast.py <dataset-dir> <broadcast-md>
"""
import csv, re, sys, pathlib

if len(sys.argv) != 3:
    sys.exit("usage: tag-broadcast.py DATASET_DIR BROADCAST_MD")

ds = pathlib.Path(sys.argv[1])
md_path = pathlib.Path(sys.argv[2])
game = next(csv.DictReader((ds / "game.csv").open()))
plays = list(csv.DictReader((ds / "plays.csv").open()))
batting = list(csv.DictReader((ds / "batting.csv").open()))
pitching = list(csv.DictReader((ds / "pitching.csv").open()))

slug = ds.name
GAMELOG = f"{slug}.html"
away_short = game["away_team_short"]
home_short = game["home_team_short"]
away_abbr = game["away_abbr"]
home_abbr = game["home_abbr"]

md = md_path.read_text()
pre, so, rest = md.partition('<div class="radio-script">')
body, sc, post = rest.partition('</div>')

# Gather roster last names from batting + pitching tables.
def last(n): return (n or "").split()[-1] if n else ""
players = set()
for p in batting + pitching:
    ln = last(p.get("name", ""))
    if ln and len(ln) > 2:
        players.add(ln)

# 1. sb-tag pills — injected FIRST so we don't collide with later spans.
TAG_CLASS = {"HR":"hr","3B":"hit","2B":"hit","1B":"hit","K":"k","ꓘ":"k",
             "BB":"walk","IBB":"walk","HBP":"walk","SH":"sac","SF":"sac",
             "GIDP":"dp","DP":"dp","TP":"dp","WP":"err","PB":"err","BK":"err",
             "SB":"hit","CS":"out",
             # Out-type tags — visually "out" flavor.
             "FO":"out","GO":"out","LO":"out","PO":"out","FC":"out"}
def pill(idx, letter, klass):
    return (f' <a href="{GAMELOG}#play-{idx}" title="See play {idx} in the game log">'
            f'<span class="sb-tag sb-{klass}">{letter}</span></a>')

paragraphs = re.split(r'\n\n+', body)
already = set()
for i, para in enumerate(paragraphs):
    for m in re.finditer(r'#play-(\d+)', para):
        already.add(int(m.group(1)))

cursor = 0
claimed: set[int] = set()
def find_para(batter_last, after_idx):
    # Batter is a match if EITHER (a) the name appears in the first 60 chars
    # of spoken content (typical leadoff pattern "Rolfe up — ..."), OR (b) the
    # batter's name is the FIRST known player in the first ~200 chars. This
    # avoids false-positives where the batter appears only as a fielder
    # ("...to Gehrig at first") in a play primarily about someone else.
    bname_re = re.compile(rf'(?<![a-zA-Z]){re.escape(batter_last)}(?![a-zA-Z])')
    first_name_re = re.compile(
        r'(?<![a-zA-Z])(' + '|'.join(re.escape(n) for n in sorted(players, key=len, reverse=True)) + r')(?![a-zA-Z])'
    )
    # Search forward starting at after_idx; if nothing matches, retry from 0
    # (the transcript may reorder plays vs paragraphs). Never claim a paragraph
    # twice.
    for start in (after_idx, 0):
        for j in range(start, len(paragraphs)):
            if j in claimed: continue
            p = paragraphs[j]
            if "HALLIDAY:" not in p: continue
            if 'class="sb-tag' in p: continue
            if not bname_re.search(p): continue
            spoken = re.sub(r'^\*\*\[[^\]]+\]\s*HALLIDAY:\*\*\s*', '', p.lstrip())
            if bname_re.search(spoken[:60]):
                return j
            m = first_name_re.search(spoken[:200])
            if m and m.group(1) == batter_last:
                return j
    return None

for pl in plays:
    tag = (pl.get("event_tag") or "").strip()
    if not tag or tag not in TAG_CLASS: continue
    idx = int(pl["idx"])
    bl = last(pl["batter"])
    if idx in already:
        j = find_para(bl, cursor)
        if j is not None: cursor = max(cursor, j + 1)
        continue
    j = find_para(bl, cursor)
    if j is None: continue
    paragraphs[j] = paragraphs[j].rstrip() + pill(idx, tag, TAG_CLASS[tag])
    already.add(idx); claimed.add(j); cursor = j + 1

body = "\n\n".join(paragraphs)

# 2. Team-name spans (scoped to HALLIDAY lines only — avoid title block).
for tname, team_short, abbr in (
    (home_short, home_short, home_abbr),
    (away_short, away_short, away_abbr),
):
    if not tname: continue
    body = re.sub(
        rf'\b{re.escape(tname)}\b(?![^<]*</span>)',
        rf'<span class="team-name t-{abbr}">{tname}</span>',
        body,
    )

# 3. Player spans
for name in sorted(players, key=len, reverse=True):
    body = re.sub(
        rf'\b{re.escape(name)}\b(?![^<]*</span>)',
        rf'<span class="player">{name}</span>',
        body,
    )

# 4. Run-word spans
for phrase in ["round-tripper","circuit clout","cross the plate","tape-measure"]:
    body = re.sub(rf'\b{re.escape(phrase)}\b', rf'<span class="run">{phrase}</span>', body)
for v in ["scores","scored"]:
    body = re.sub(rf'\b{v}\b(?![^<]*</span>)', rf'<span class="run">{v}</span>', body)

md_path.write_text(pre + so + body + sc + post)
print(f"tags: {sum(1 for _ in re.finditer(r'sb-tag sb-', body))}, players: {len(players)}")
