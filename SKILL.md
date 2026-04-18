---
name: mlb-announcer-1930s
description: Use when the user asks for a 1930s-style radio broadcast transcript, period-accurate old-time announcer call, vintage play-by-play, "Red Barber / Graham McNamee version", or any "make it sound like a 1930s broadcast" transformation of a game. Consumes the Markdown product of the `mlb-game-report` skill (with its structured ATMOSPHERE, SCORING, PLAY-BY-PLAY + Statcast sections) and produces a transcript written in the voice of a Golden Age radio sportscaster, with modern Statcast metrics translated into period-appropriate color commentary.
---

# 1930s Radio Broadcast Transcript

Transforms a structured MLB game report into a transcript of a *live* radio broadcast, as if called by a 1930s-era sportscaster. Takes the structured product of the `mlb-game-report` skill (PBP + Statcast + atmosphere + captivating-moment data) and re-voices it in period-accurate radio English.

## When to use

Triggers:
- "give me a 1930s radio call of [game]"
- "Red Barber version" / "Graham McNamee version" / "Bill Stern style"
- "vintage announcer transcript" / "old-time radio broadcast"
- "make [report] sound like a 1930s broadcast"
- "narrate the [team] game like it's 1935"

## How to use

1. **Find the source report.** The skill expects a Markdown file produced by `mlb-game-report`, usually in `~/games-attended/`. If the user hasn't specified one, list candidates with `ls ~/games-attended/*.md` and ask which game. If they reference a team+date, look for the matching file there first.

2. **Read the source .md in full.** You'll use:
   - **Frontmatter** (date, teams, venue, gamePk) for the opening
   - **AT A GLANCE** for final score, WP/LP, attendance, records — the setup facts
   - **ATMOSPHERE** (sunlight timing, weather, wind, crowd, field azimuth) for scene-setting
   - **KEY TAKEAWAYS** and **HOW IT HAPPENED** for the narrative arc
   - **MOMENT OF THE GAME** for the dramatic centerpiece
   - **PLAY-BY-PLAY** section as the call-by-call skeleton — walk through it in order
   - Statcast lines under each PBP entry to embellish (exit velocity, pitch type, distance)

3. **Load the style references.** Before writing, read these in order:
   - `references/style-guide.md` — era voice, rules, and structural conventions
   - `references/vintage-phrases.md` — period vocabulary catalog to draw from (don't copy-paste; use as inspiration)
   - `references/example-calls.md` — worked examples of how to transform PBP+Statcast into live-radio calls

4. **Compose the transcript** (see "Output structure" below). Write to `<source-stem>-broadcast.md` next to the source. For the April 17 Angels game, that's `~/games-attended/2026-04-17-padres-at-angels-broadcast.md`.

5. **Offer HTML.** If the user said "open it", "make HTML", or similar, render with pandoc using the bundled stylesheet:

   ```bash
   pandoc --from=gfm+yaml_metadata_block+smart --to=html5 --standalone \
          --wrap=preserve \
          -V document-css=false --metadata title=" " --metadata lang=en \
          OUT.md -o OUT.html
   ```

   Then inline `scripts/broadcast.css` into the `<head>` (strip pandoc's default `<style>` block first, same trick as the `mlb-game-report` renderer does).

## Output structure

```markdown
---
source: <path-to-source-md>
gamePk: <from source frontmatter>
broadcast_style: 1930s-radio
announcer: <name, e.g., "Howard 'Hap' Halliday">
---

# THE BROADCAST
## <AWAY> at <HOME> · <VENUE> · <FULL_DATE>
### *A live radio call by <ANNOUNCER>, from the press box at <VENUE>*

> **STATION IDENT.** Opening jingle. Organ fanfare.

## SIGNING ON

<Opening: scene-set using ATMOSPHERE data — weather, sunlight state, crowd,
flags over the grandstand, sponsor mention if you're feeling it. 2–4 paragraphs.>

## FIRST INNING

### TOP — <AWAY> BATTING

<For each plate appearance in the source PBP: 1–3 sentences of live call.
Embellish using Statcast (exit velo, pitch type, distance). Include the
count at key moments. Break character only for "station breaks" — short
italic asides like "*[Crowd murmurs]*" or "*[Pause for organ]*".>

### BOTTOM — <HOME> BATTING

<Same treatment, continuing the broadcast voice.>

<...repeat for every inning present in the source PBP...>

## THE FINAL OUT

<Close out: the final play, crowd reaction, final score recap, storyline
wrap-up, sign-off in character.>

> **SIGN-OFF.** Station ident. Organ fade.

---

*Broadcast transcript composed from <source-filename>. All facts — plays,
counts, scores, Statcast measurements — are drawn from the MLB Stats API
via `mlb-game-report`. The voice and embellishments are period costume.*
```

## Guardrails

- **Facts are sacred; voice is theatrical.** Every play, count, score, substitution, HR distance must match the source. Invent atmosphere, crowd reactions, sponsor asides, and announcer color — never invent plays, outcomes, players, or stats.
- **No modern references.** No references to TV, video replay, WAR, launch angle by name, analytics, "exit velocity" (translate: "the ball came off the bat like a cannon shot"). No post-1939 terminology (most radio baseball broadcasting is 1921–present, but keep it feeling Depression-era).
- **Translate, don't parrot.** If the source says `Batted: EV 104.3 mph, LA 34°, 388 ft, fly ball, to CF`, the broadcast says "My, my — Moncada got *all* of that one! High fly ball, deep to center — and that, folks, is GONE! Into the bleachers! A tremendous poke."
- **Use atmosphere.** If the source says sunset was 7:24 PM and first pitch was 6:39 PM, mention the fading light, long shadows across the infield in the 4th inning, lights coming on in the 5th.
- **Hold the captivating moment.** Whatever play the source marked as MOMENT OF THE GAME should get the most dramatic treatment of the transcript.
- **Include all innings** present in the source PBP — no skipping even for 1-2-3 innings; those get one short paragraph of call.
- **Announcer name.** Default to "Howard 'Hap' Halliday" unless the user specifies (and they might want a real historical voice like Red Barber, Graham McNamee, or Bill Stern — do that character instead if asked).

## Length

A 9-inning broadcast transcript should run long — these were two-and-a-half-hour radio shows. Expect 1500–3500 words depending on game length. Don't abbreviate. Radio-era sportscasters filled dead air with color, crowd observations, rhumba-band asides, and sponsor reads.

## When to ask before acting

- If multiple source reports could match the user's request, list them and ask.
- If the user names a real historical announcer you don't want to impersonate, fall back to the fictional composite.
- If they want something other than 1930s (say, "1950s TV version" or "Howard Cosell style"), tell them this skill is scoped to 1930s radio and offer to write the 1930s version anyway.
