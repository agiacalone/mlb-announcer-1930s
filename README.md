# mlb-announcer-1930s

A [Claude Code](https://claude.com/claude-code) skill that takes a structured MLB game dataset (produced by the companion [`mlb-game-report`](https://github.com/agiacalone/mlb-game-report) skill) and re-voices it as a **1930s-era radio broadcast transcript** — as if called by a Golden Age sportscaster.

The skill operates in **two modes**, chosen automatically from the game date:

- **Mode A (game 1925–1949):** he's in his own era. No time-travel framing, no marveling at the modern game, period player comps (Ruth, Gehrig, Foxx) natural rather than forced.
- **Mode B (game 1950+):** he's time-traveled to the present. He keeps his 1930s voice but describes the modern game fluently, translating Statcast/ABS/sabermetrics into period vocabulary — *"the Signal Corps tracking apparatus"* for Statcast, *"the electric umpire"* for ABS, *"the slide-rule school"* and *"the IBM-tabulator fellows"* for analytics, *"the cinematograph review"* for video challenges.

Modern player names, dates, and every fact are preserved exactly from the source dataset. The voice is costume; the facts are gospel.

## Input: the CSV dataset

As of the `mlb-game-report` refactor, every game produces a structured CSV dataset directory:

```
~/games-attended/2026-04-17-padres-at-angels/
├── game.csv       # meta: teams, venue, weather, attendance, WP/LP/SV, …
├── plays.csv      # 1 row per plate appearance: batter, pitcher, event, desc, count, scoring
├── pitches.csv    # 1 row per pitch: type, speed, EV, LA, distance, trajectory
├── batting.csv    # batter lines
├── pitching.csv   # pitcher lines + decisions
└── linescore.csv  # inning-by-inning
```

The announcer reads those CSVs directly (not the rendered `.md`) for all factual content — plays, counts, Statcast, lineups. The companion `.md`'s ATMOSPHERE narrative is consulted for the precomposed sunlight-arc phrasing. Backward compat: if only a `.md` exists (pre-refactor report), the skill falls back to Markdown parsing.

## A taste

> *Good evening, friends, and a warm welcome to you from the press box here at Angel Stadium in Anaheim, California — it is Friday, the seventeenth of April, in the year of our Lord nineteen hundred and twenty — er, pardon your announcer, folks — two thousand and twenty-six. Your old friend Hap Halliday still catches himself once in a while, but I promise you he is here and he is present and he is ready to call a ballgame.*

> *LINE DRIVE! Right field! A scorcher! Tatis Junior is back — back — he's at the warning track — and that ball is off his glove one-hop to the wall! The Signal Corps tracking fellows give us a hundred-point-two miles per hour off the stick, a twenty-two degree angle of flight, three hundred and nine feet of ribbon line drive to the right gardener. A proper cannon shot, friends.*

## Layout

```
mlb-announcer-1930s/
├── SKILL.md                       # trigger criteria + composition rules
├── references/
│   ├── style-guide.md             # era voice, structural conventions
│   ├── vintage-phrases.md         # period vocabulary catalog
│   ├── translations.md            # modern→1930s translations (Statcast, ABS, etc.)
│   └── example-calls.md           # worked PBP→broadcast transformations
└── scripts/
    └── broadcast.css              # Depression-era radio-script HTML stylesheet
```

## Install

This is a [Claude Code user skill](https://docs.claude.com/en/docs/claude-code/skills). Clone it into your Claude Code skills directory so it auto-loads in every session:

```bash
git clone https://github.com/agiacalone/mlb-announcer-1930s.git \
    ~/.claude/skills/mlb-announcer-1930s
```

Or, if you prefer to keep the repo in your normal source tree and symlink:

```bash
git clone https://github.com/agiacalone/mlb-announcer-1930s.git ~/git/mlb-announcer-1930s
ln -s ~/git/mlb-announcer-1930s ~/.claude/skills/mlb-announcer-1930s
```

Verify Claude Code picked it up by running `/skills` inside Claude Code (or starting a new session) — `mlb-announcer-1930s` should appear in the available-skills list.

### Companion skill

This skill consumes the output of [`mlb-game-report`](https://github.com/agiacalone/mlb-game-report). Install that one first:

```bash
git clone https://github.com/agiacalone/mlb-game-report.git \
    ~/.claude/skills/mlb-game-report
```

### Dependencies

- **Pure Claude** for the transcript itself — no additional runtime deps.
- **[pandoc](https://pandoc.org/)** (optional, for HTML rendering): `brew install pandoc`
  - Without pandoc, you'll still get the Markdown transcript; HTML rendering will be skipped with a note.

## Use

Once both skills are installed, a typical session looks like this:

```text
You: Give me a keepsake report for the Angels game on April 17 2026, I attended with my daughter
Claude: [invokes mlb-game-report → ~/games-attended/2026-04-17-padres-at-angels.md]

You: Now a 1930s radio call of that game
Claude: [invokes mlb-announcer-1930s → ~/games-attended/2026-04-17-padres-at-angels-broadcast.md
        and opens the styled HTML in your browser]
```

The skill will auto-trigger on phrases like:

- *"give me a 1930s radio call of [game]"*
- *"Red Barber version"* / *"Graham McNamee version"*
- *"vintage announcer transcript"*
- *"old-time radio broadcast"*
- *"make it sound like a 1930s broadcast"*
- *"narrate the [team] game like it's 1935"*

## The conceit

A 1930s radio sportscaster has time-traveled to the present. He keeps his voice, his courtly address, his folksy idiom — but the game in front of him is modern. He has been here long enough to have been briefed on Statcast, sabermetrics, ABS, the pitch clock, and replay review; he just describes them in period-accurate analogues.

**Key rule:** the **game's date is real**, not transplanted to the 1930s. A 2026 game gets a 2026 masthead. The dissonance is the charm.

**Never** used: "computer" (1930s: a human who computed), "algorithm", "data", "software", "app", "stream", "AI". See [`references/translations.md`](references/translations.md) for the full vocabulary table and modern→period substitutions.

## What the output looks like

Each run produces a Markdown file, optionally rendered to a self-contained HTML file styled like a Depression-era broadcast script (paper-tone background, Courier typography for station idents, serif body for the spoken call, ornamental rules). The transcript structure:

1. **Frontmatter** (source, gamePk, broadcast_style, announcer)
2. **Masthead** — teams, venue, date (real, not 1930s)
3. **SIGNING ON** — scene-setting opener using weather, crowd, sunlight from the source
4. **Each inning** (TOP and BOTTOM) — every plate appearance called in period voice
5. **THE FINAL OUT** — closing call, recap, sign-off

Default announcer: the fictional *Howard "Hap" Halliday*. The user can request a real historical voice (Red Barber, Graham McNamee, Bill Stern) if preferred.

## Credits & Inspiration

- Voice draws on Graham McNamee (NBC, 1920s–30s World Series), Red Barber (Cincinnati and Brooklyn), Bill Stern (NBC), and Ted Husing (CBS).
- Data sourced through [`mlb-game-report`](https://github.com/agiacalone/mlb-game-report), which fetches from the public [MLB Stats API](https://statsapi.mlb.com/).

## License

MIT. See [`LICENSE`](LICENSE) if present; otherwise assume MIT.
