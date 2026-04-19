# Stretch Goals

Ideas we've agreed are worth exploring but haven't started. Not part of the current skill — document first, implement later.

---

## 1. "Fun facts" color commentary

### The goal

Announcers in any era — and especially the 1930s radio voices this skill emulates — weren't just calling pitches. They filled innings with **color commentary**: player birthplaces, career milestones, family connections, historical parallels ("first time since Lou Gehrig in '32…"), franchise lore, ballpark trivia. It's the glue between plays. Right now the broadcast has a little of it (we already pull player bios and standings via MCP) but we could go deeper — every at-bat could have a one-liner of personality behind the name.

**Desired feel:** one or two color asides per half-inning, woven into the at-bats or between-inning breaks. Not every player, not every pitch. The leadoff hitter of a big inning gets a tidbit. The pitcher who just gave up the moment-of-the-game HR gets context. A 3-for-3 hitter in the 7th gets noted. The other 20 at-bats are called plain.

### The hard constraint

This is in **direct tension** with the invariant we've established across both artifacts: *facts are gospel, no fabrication*. Announcers hallucinating "his dad played for this team in '98" would turn a keepsake record into an untrustworthy one. We cannot ship fun facts that come from an LLM's training data — too many plausible-sounding falsehoods at the rates we'd generate.

Every specific factual claim in a fun fact must be **backed by a live lookup** at broadcast-composition time. Color/flavor framing is free; numbers, dates, comparisons, career claims, and biographical specifics are not.

### Source inventory

What we can query reliably, sorted by how much of the announcer's palette each unlocks:

| Category | Source | Reliability | Coverage | Example use |
|---|---|---|---|---|
| **Player bio** — name, birthplace, handedness, age, height/weight, draft year | `mcp__mlb__get_player_bio` | High — structured API | All MLB players | *"A right-hander out of Bluefield, West Virginia, in his third big-league season"* |
| **Season stats (current)** — AVG, OPS, HR count, K/BB, etc. | `mcp__mlb__get_player_stats` (group=season) | High | All MLB players | *"Brings a .340 average into this game — best in the junior circuit"* |
| **Career totals** — career H, HR, W-L, ERA | `mcp__mlb__get_player_stats` (group=career) | High | All players | *"That's career hit number five hundred, folks"* |
| **League leaderboards** — HR leaders, wins, whiffs | `mcp__mlb__get_stat_leaders` | High | Real-time | *"Eight strikeouts tonight — fourth-most in the league"* |
| **Standings** — division races, wild card | `mcp__mlb__get_standings` | High | Daily | *"With this win they pull within two-and-a-half of the front-runners"* |
| **Recent transactions** — call-ups, IL moves | `mcp__mlb__get_transactions` | High | Rolling window | *"Up from the farm just this morning"* |
| **Team / venue metadata** — founding year, stadium opened, capacity | `mcp__mlb__get_team_info` | Medium — some gaps | All 30 teams | *"Angel Stadium, built in sixty-six, seats forty-five and change"* |
| **Historical "on this date"** | Lahman DB (offline) or Retrosheet parsing | Medium — requires local lookup tooling | 1871+ | *"On this date in 1941, Joe DiMaggio's streak hit thirty games"* |
| **Game-situation streaks** — player hot/cold last 7 / 15 / 30 days | Computed from `mcp__mlb__get_player_stats` with date-range | Medium — more queries, might not all be exposed | Last season | *"Four hits in his last three games — he's locked in"* |
| **Head-to-head history** — batter vs. pitcher | Requires game-log join across seasons | Low — significant infrastructure | Full MLB | *"Oh-for-twelve lifetime against Clayton Kershaw"* |
| **Franchise lore** — notable past games, rivalries, nicknames | Wikipedia, SABR Bio Project | Low — unstructured, citation-shaky | All teams | *(Skip. High hallucination risk.)* |
| **Player family connections** — "his dad played" | Wikipedia / team pages | Low — no reliable API | Partial | *(Skip unless MCP adds this explicitly.)* |

### Proposed architecture (for when we build it)

1. **Define a fixed repertoire of fact types** the announcer is allowed to assert — only those with high-reliability sources (bio, season, career, leaderboards, standings, transactions, team/venue, on-this-date-Lahman).
2. **Build a "color card" builder** — before composing the broadcast, for each *featured* player (defined as: starting pitchers, top-3 hitters by source-calculated performance, the moment-of-the-game batter, any HR hitter), call a standardized battery of MCP queries and store the raw returns in a `color_cards.json` per-game file alongside the CSV dataset. One card per featured player with just the fact types above.
3. **Announcer prompt cites only from the cards.** The SKILL.md would hard-rule: *a fun fact appears in the transcript only if a matching field appears in the player's color card.* Anything else is fabrication and forbidden.
4. **Audit trail.** Each fun-fact aside in the transcript carries a hidden HTML comment `<!-- source: get_player_bio:birthplace -->` so a reviewer can verify post-hoc. Strippable from the final display but preserved in the Markdown.
5. **"On this date" module** — separate, opt-in. Download Lahman once to `~/.cache/lahman/`; a helper returns anniversaries for the game's date. Wraps in the same card format.

### Risks and open questions

- **Aggressive querying.** Color cards for ~10 featured players × 5 queries each = 50 MCP calls per game generation. Need to check rate-limit behavior.
- **MCP query surface might not cover head-to-head or rolling windows** cleanly. Could need a separate library like `pybaseball` (which carefully scrapes Baseball-Reference and risks ToS trouble, per our earlier notes).
- **Tension with the 1930s voice.** Some modern-era fact types (spin rate, WAR, OPS+) don't translate well to period vocabulary. The translation table in `references/translations.md` would need to grow.
- **Audit-trail comments pollute the Markdown** if we don't strip them on HTML render. Have pandoc drop them, or post-process.

### Minimum viable first cut (when we start)

- Color cards for **starting pitchers and the moment-of-the-game batter only** (4 players per game).
- Fact types: bio (birthplace, handedness), season AVG / ERA, career HR / W, one recent-form line.
- 1–3 asides total per broadcast. If it feels forced, cut it.
- No "on this date", no head-to-head, no franchise lore. Those come later after the pipeline is proven.

### When to revisit

After: (a) we've synced 5+ attended games and the existing flow feels stable; (b) we've confirmed the MCP rate-limit profile; (c) there's a concrete broadcast moment we listened to and thought "this would've landed with a fun fact here" — not just theorizing.
