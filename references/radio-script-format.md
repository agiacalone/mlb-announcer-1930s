# Radio Script Format

This is the authoritative formatting spec for broadcast-transcript output. It
supersedes the "prose with blockquote" shape the earlier versions used.

The conceit (1930s time-traveling announcer, facts-are-gospel, live-present
tense) is unchanged. What changes is the *document structure*: instead of
journalistic prose, every utterance is a **script line** — speaker label,
content, timestamp — the way a real radio script from the era would read.

---

## 1. Top-level document structure

```markdown
---
source: /path/to/<slug>/
gamePk: <from game.csv>
broadcast_style: 1930s-radio-script
announcer: Howard "Hap" Halliday
---

# THE BROADCAST

<div class="script-header">

```
===================================================================
  PROGRAM:    Angels Baseball on KFI
  DATE:       Friday, April 17, 2026
  GAME:       San Diego Padres at Los Angeles Angels (0–8, Final)
  VENUE:      Angel Stadium, Anaheim, CA
  ANNOUNCER:  Howard "Hap" Halliday
  DURATION:   2:58
===================================================================
```

</div>

<div class="radio-script">

**[00:00:00] MUSIC:** *PROGRAM OPEN — ORGAN FANFARE, FADE UNDER.*

**[00:00:12] HALLIDAY:** Good evening, friends, and welcome to Angel Stadium...

...
```

### Components

1. **YAML frontmatter** — same as the game log's, plus `broadcast_style: 1930s-radio-script` and `announcer:`.
2. **`# THE BROADCAST` masthead** — single top-level heading.
3. **Title block** — a fenced code block inside `<div class="script-header">` showing PROGRAM / DATE / GAME / VENUE / ANNOUNCER / DURATION. Fixed-width ASCII styling; evokes the cover page of a real radio script.
4. **`<div class="radio-script">` body** — all script lines live inside this wrapper so CSS can style them as a script (monospace, hanging indent, column-aligned speaker labels).
5. **Inning dividers** (see §4).
6. **Close + sign-off** at the bottom.
7. Source citation (small footnote) below the script.

---

## 2. Script line format

Every paragraph in the `.radio-script` block is a **script line** shaped like:

```markdown
**[HH:MM:SS] LABEL:** content
```

- **`[HH:MM:SS]`** — timestamp in square brackets, fixed width. See §3.
- **`LABEL:`** — ALL-CAPS speaker or cue label followed by a colon. Common labels:
  - `HALLIDAY` — the announcer's utterances (content in plain text)
  - `SFX` — sound effects; content goes in *italics inside brackets*: `*[CROWD ROARS]*`
  - `MUSIC` — musical cues; content in italics: `*PROGRAM OPEN — ORGAN FANFARE, FADE UNDER.*`
  - `COMMERCIAL` — sponsor break; content in italics
  - `STATION ID` — network/station identification break
  - `ENGINEER` or `PRODUCER` — only if the source includes such notes (rare)
- **Content** — plain text for dialogue; italic for SFX/MUSIC/COMMERCIAL so they read as stage directions rather than spoken words.
- The whole `[HH:MM:SS] LABEL:` prefix is **bold** (`**...**`) so CSS can target it.

### When to start a new line

**Every time any of the following happens, break to a new script line:**

- Speaker change (always). `HALLIDAY` → `SFX` → `HALLIDAY` each becomes its own paragraph.
- A significant beat in the call — a strike call, a ball in flight, a runner scoring. Don't let a single speaker paragraph run longer than ~60 words without breaking. Radio calls are rhythmic; so is the transcript.
- An inning change (new section header, see §4).

Rule of thumb: one paragraph ≈ 5–20 seconds of broadcast time.

### Examples

```markdown
**[00:02:45] SFX:** *[CROWD MURMUR — FIRST PITCH READY]*

**[00:02:51] HALLIDAY:** And here we go, folks. Soriano — six-foot-four,
right-hander — onto the hill. Jake Cronenworth leads off.

**[00:03:02] HALLIDAY:** Soriano looks for the sign. The stretch. The
pitch — *strike one, called!* A knuckle-curve right over the corner.

**[00:03:28] HALLIDAY:** Oh-and-one to Cronenworth. Soriano back set —
and he goes to the split — *swung on, missed!* Oh-and-two. Cronenworth
is in trouble now, folks.

**[00:03:44] HALLIDAY:** Here comes the payoff — *and he fans him!*
Cronenworth goes down swinging at a knuckle-curve that fell off a table.
One away, Padres.

**[00:03:58] SFX:** *[SCATTERED APPLAUSE]*
```

---

## 3. Timestamps

### Format

`[HH:MM:SS]` — two-digit zero-padded hours, minutes, seconds in brackets.
Always exactly 10 characters (8 digits + 2 colons + brackets… actually
`[00:00:00]` is 10 characters). Fixed width so script lines align cleanly in
the HTML.

### Source of values

The skill does **not** have per-play wall-clock times in `plays.csv` today.
Approximate them by **linearly distributing play indices across the game's
total duration**:

```
play_time_sec = (play_idx / total_plays) * duration_seconds
```

Where `duration_seconds` parses `game.csv.duration` (e.g. "2:58" → 10,680 s).
`total_plays` is the highest `idx` in `plays.csv`. Round to the nearest
second.

SFX and MUSIC lines fall at natural boundaries:
- Opening music: `[00:00:00]`
- First announcer line: `[00:00:08]` to `[00:00:15]` range
- First-pitch SFX: roughly matches the first PBP entry timestamp
- Inning-break SFX/organ: interpolate between last play of one half-inning
  and first play of the next
- Closing music: 1–2 seconds after the final out's timestamp

This is approximate but good enough for "script feel." When we add
`start_time` to `plays.csv` in a future iteration, swap the interpolation
for real values.

---

## 4. Inning dividers

Each half-inning gets a section header, rendered as:

```markdown
---

### ▲ TOP 1ST — PADRES BATTING · ANGELS PITCHING

**[00:03:00] HALLIDAY:** Leading off for San Diego...
```

- Triangle glyph `▲` for top, `▼` for bottom.
- All-caps inning label.
- `TEAM BATTING · TEAM PITCHING` subtitle so the listener orientation is
  explicit.
- A `---` horizontal rule above the header to give visual separation.

---

## 5. Opening and closing

### SIGNING ON (opening)

Should be 5–10 script lines covering:

1. `[00:00:00]` MUSIC — program open
2. `[00:00:XX]` HALLIDAY — greeting + dateline + weather + crowd size
3. Optional SFX — crowd murmur, national anthem cue if appropriate
4. `[00:0X:XX]` HALLIDAY — starting pitchers, storyline
5. Handoff to first pitch: "And here we go, friends…"

### THE FINAL OUT (close)

3–8 script lines:

1. HALLIDAY — the final out of the game (live call)
2. SFX — crowd reaction
3. HALLIDAY — final score recited + decision line (WP / LP / SV)
4. HALLIDAY — storyline wrap (one sentence)
5. HALLIDAY — sign-off with announcer name
6. MUSIC — program close
7. SFX — station ident

---

## 6. Content rules (unchanged from previous versions)

These invariants from `style-guide.md` apply unchanged:

- **Live present tense.** "He swings" not "he swung." Past tense only in
  between-innings recaps.
- **Facts from the CSV dataset.** Every pitch, count, run, player name,
  Statcast number matches `plays.csv` / `pitches.csv` / `game.csv`.
- **Era-aware conceit.** 1925–1949 = his own era; 1950+ = time-traveler;
  pre-1921 = refuse.
- **No "computer" family words.** Use tabulating machine, Signal Corps
  tracking apparatus, cinematograph review, etc. (see `translations.md`).
- **The date is the source's date.** Never substitute a Depression-era year.

---

## 7. HTML-render conventions

The `<div class="radio-script">` wrapper and `<div class="script-header">`
wrapper trigger typewriter-style CSS in `scripts/broadcast.css`:

- Monospace body (Courier Prime / Menlo), ~14px
- Hanging indent per paragraph so the timestamp + LABEL column stays on the
  left and wrapped content aligns
- ALL-CAPS speaker labels in accent color
- SFX/MUSIC italic in a subtler tone
- Inning headers as small-caps rules
- Title block rendered in a `<pre>` so the ASCII frame holds

---

## 8. What changes vs. the previous prose format

| Before (prose) | After (script) |
|---|---|
| Blockquote-heavy paragraphs, 3–4 sentences each | One speaker line per beat; many short paragraphs |
| Narrative voice ("Moncada homers on a drive to center — and the crowd roars!") | Labeled speaker ("HALLIDAY: …drive to center — …"), then separate SFX line ("SFX: *[CROWD ROARS]*") |
| Occasional italic asides for atmosphere | Atmosphere is now formalized SFX/MUSIC cues between speaker lines |
| No timestamps | Every paragraph leads with `[HH:MM:SS]` |
| Section headers: "## FIRST INNING" / "### TOP — PADRES BATTING" | Now a single `### ▲ TOP 1ST — PADRES BATTING · ANGELS PITCHING` header with a horizontal rule |
| Sign-off as a final prose paragraph | Sign-off as a sequence of script lines ending in MUSIC + SFX cues |
