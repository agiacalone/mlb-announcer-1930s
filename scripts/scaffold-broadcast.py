#!/usr/bin/env python3
"""Generate a factually-complete broadcast .md skeleton from a game dataset.

The skeleton contains every script-line shell the announcer needs:
- Correct frontmatter (source, gamePk, announcer, station)
- Fenced script-header title block (program / date / venue / crowd / duration)
- Inning dividers (▲/▼ TOP/BOTTOM Nth — AWAY BATTING · HOME PITCHING)
- One stub HALLIDAY line per play with:
    * real wall-clock timestamp (from plays.csv start_time_utc, broadcast-relative)
    * batter · pitcher · count · event · score-after (after scoring plays)
- Auto-inserted pitching-change markers when the pitcher id changes
- Stub opening (attendance, first-pitch, weather, lineups placeholders)
- Stub closing (real WP / LP / SV + final score)

The resulting .md is BORING on purpose — it's a trellis. Pair it with the
announcer skill to enrich the stubs into period radio English, then run
tag-broadcast.py to add player/team spans + sb-tag pills.

Usage: scaffold-broadcast.py <dataset-dir> [--announcer "Name"] [--station "..."]
"""
import argparse, csv, json, re, sys
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

ap = argparse.ArgumentParser()
ap.add_argument("dataset", help="Dataset directory (must contain game.csv, plays.csv)")
ap.add_argument("--announcer", default='Howard "Hap" Halliday')
ap.add_argument("--station", default="WEAF-NBC, New York (660 kc)")
ap.add_argument("--style", default="1930s-radio-script")
ap.add_argument("--mode", default="1930s-historical", help="era_mode: 1930s-historical or 1930s-time-traveler")
ap.add_argument("-o", "--output", help="Output .md path (default: <parent>/<slug>-broadcast.md)")
args = ap.parse_args()

ds = Path(args.dataset).resolve()
slug = ds.name
game = next(csv.DictReader((ds / "game.csv").open()))
plays = list(csv.DictReader((ds / "plays.csv").open()))

out = Path(args.output) if args.output else ds.parent / f"{slug}-broadcast.md"

away = game["away_team"]; away_short = game["away_team_short"]
home = game["home_team"]; home_short = game["home_team_short"]
venue = game["venue"]; city = game.get("city", ""); state = game.get("state", "")
date_iso = game["date"]
try:
    dt = datetime.strptime(date_iso, "%Y-%m-%d")
    date_long = dt.strftime("%A, %B %-d, %Y")
except ValueError:
    date_long = date_iso
duration = game.get("duration", "—") or "—"
attendance = game.get("attendance", "—") or "—"
weather = game.get("weather", "—") or "—"
first_pitch = game.get("first_pitch", "—") or "—"
wp = game.get("winning_pitcher", "") or ""
lp = game.get("losing_pitcher", "") or ""
sv = game.get("save_pitcher", "") or ""
away_score = game.get("away_score", "")
home_score = game.get("home_score", "")

# --- Timestamp layout --------------------------------------------------------
# Use real per-play start_time_utc when available; localize to the game tz.
# Broadcast-relative timestamps (HH:MM:SS from opening) = local time − (first-pitch − 10 min pre-game),
# i.e. opening runs 10 minutes before first pitch.
tz = ZoneInfo(game.get("tz") or "UTC")
def parse_utc(s):
    if not s: return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone(tz)
    except (TypeError, ValueError):
        return None

start_dts = [parse_utc(p.get("start_time_utc")) for p in plays]
first_real = next((d for d in start_dts if d), None)
if first_real:
    broadcast_start = first_real - timedelta(minutes=10)
else:
    broadcast_start = datetime.now(tz)
def ts_at(dt):
    if dt is None: return "[00:00:00]"
    delta = dt - broadcast_start
    s = max(0, int(delta.total_seconds()))
    return f"[{s//3600:02d}:{(s%3600)//60:02d}:{s%60:02d}]"

# --- Emit --------------------------------------------------------------------
def fmt_event(p):
    b = p["batter"]
    pit = p["pitcher"]
    ev = (p.get("event") or "Play").strip()
    desc = (p.get("description") or "").strip()
    count = f"{p.get('balls','0')}-{p.get('strikes','0')}"
    score = ""
    if str(p.get("is_scoring_play","")).lower() == "true":
        score = f"  [{away_short} {p.get('away_score_after','?')}, {home_short} {p.get('home_score_after','?')}]"
    return f"{b} vs. {pit} — {ev} ({count}). {desc}{score}"

def inning_header(inn, half):
    arrow = "▲" if half == "top" else "▼"
    ord_ = f"{inn}{'st' if inn==1 else 'nd' if inn==2 else 'rd' if inn==3 else 'th'}"
    bat  = (away_short if half == "top" else home_short).upper()
    pitc = (home_short if half == "top" else away_short).upper()
    return f"---\n\n### {arrow} {half.upper()} {ord_.upper()} — {bat} BATTING · {pitc} PITCHING"

lines = []
lines.append(f"""---
source: {ds.relative_to(Path.home()) if ds.is_relative_to(Path.home()) else ds}/
gamePk: {game['gamePk']}
broadcast_style: {args.style}
era_mode: {args.mode}
announcer: {args.announcer}
station: {args.station}
---

# THE BROADCAST

<div class="script-header">

```
===================================================================
  PROGRAM:    WORLD SERIES BASEBALL — NBC RED NETWORK
  GAME:       {away} at {home}
  DATE:       {date_long}
  VENUE:      {venue}, {city}, {state}
  FIRST BALL: {first_pitch}
  CROWD:      {attendance}
  DURATION:   {duration}
  ANNOUNCER:  {args.announcer}
  ORIGINATING: Station {args.station}
===================================================================
```

</div>

<div class="radio-script">

**[00:00:00] MUSIC:** *PROGRAM OPEN — NBC CHIMES, THEN MARCH FANFARE, FADE UNDER.*

**[00:00:12] STATION ID:** *<ENRICH: station ident>*

**[00:00:28] HALLIDAY:** <ENRICH: greeting, venue scene, weather, crowd ({attendance})>

**[00:01:00] HALLIDAY:** <ENRICH: storyline — series context, what this game means>

**[00:02:00] HALLIDAY:** <ENRICH: pitchers on the hill — WP {wp or '?'}, LP {lp or '?'} — and their season records>

**[00:03:00] HALLIDAY:** <ENRICH: line-ups>

**[00:03:30] SFX:** *[CROWD MURMUR, USHERS]*

**[00:04:00] MUSIC:** *BAND — NATIONAL ANTHEM (ABBREVIATED).*

**[00:05:40] SFX:** *[PLATE UMPIRE — "PLAY BALL!"]*

**[00:05:48] HALLIDAY:** <ENRICH: handoff — "And we are underway...">
""")

last_half_key = None
last_pitcher_id = None
for p, dt in zip(plays, start_dts):
    inn = int(p["inning"]); half = p["half"]
    key = (inn, half)
    if key != last_half_key:
        lines.append("")
        lines.append(inning_header(inn, half))
        lines.append("")
        last_half_key = key
        last_pitcher_id = None  # reset per half
    pit_id = p.get("pitcher_id") or ""
    if last_pitcher_id and pit_id and pit_id != last_pitcher_id:
        lines.append(f'<span class="pitching-change">🔄 <strong>Pitching change</strong> — new pitcher: {p["pitcher"]}</span>')
        lines.append("")
    last_pitcher_id = pit_id
    lines.append(f"**{ts_at(dt)} HALLIDAY:** <ENRICH> {fmt_event(p)}")
    lines.append("")

# Closing
closing_ts = ts_at(start_dts[-1] + timedelta(seconds=30)) if start_dts and start_dts[-1] else "[02:30:00]"
lines.append(f"""---

## THE FINAL OUT

**{closing_ts} SFX:** *[FINAL-OUT CROWD REACTION]*

**{closing_ts} HALLIDAY:** <ENRICH: final-score recap — {away_short} {away_score}, {home_short} {home_score}>

**{closing_ts} HALLIDAY:** <ENRICH: decisions — W: {wp}; L: {lp}{'; SV: ' + sv if sv else ''}>

**{closing_ts} HALLIDAY:** <ENRICH: storyline wrap — stars of the game>

**{closing_ts} HALLIDAY:** <ENRICH: sign-off>

**{closing_ts} MUSIC:** *NBC SIGNATURE — ORGAN FANFARE, CHIMES.*

**{closing_ts} STATION ID:** *<ENRICH: close-out station ident>*

</div>

---

*Broadcast skeleton generated from `{slug}` dataset (MLB Stats API, gamePk {game['gamePk']}). Every <ENRICH> stub is a prompt for the announcer skill to fill with period voice; plays, pitchers, batters, counts, and scores are factual from plays.csv.*
""")

out.write_text("\n".join(lines))
print(f"wrote {out}  ({len(plays)} plays)")
