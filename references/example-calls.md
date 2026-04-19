# Example Calls — Source PBP → Broadcast Transcript

These show how to transform structured play-by-play entries (with their Statcast sub-lines) into radio-era narration. Study the pattern; don't copy verbatim.

## The most important thing: LIVE PRESENT TENSE

Every example below uses **present tense** for the live call. The announcer is narrating as the play unfolds, *not* recounting it afterward. Past tense ("Moncada homered", "Schanuel went 3-for-5") is the wrong mode for a live broadcast — it turns the transcript into a recap. Keep the reader in the moment.

**Quick tense tell-tales:**
- ✅ "He *swings* — *he misses* — strike two!"
- ✅ "That ball *is going*, *is going* — *gone!*"
- ✅ "Cronenworth *steps in*." / "The pitcher *checks* the runner."
- ❌ "He swung and missed for strike two." *(past tense — wrong for live)*
- ❌ "That ball went into the bleachers." *(past tense — wrong)*
- ❌ "Cronenworth stepped in." *(past tense — wrong)*

Past tense is permissible only in (a) between-innings recaps of earlier innings, (b) the closing sign-off summary, and (c) color asides about career/weather/history that preceded the broadcast.

---

**Format reminder:** every example below follows the **radio-script shape** from `radio-script-format.md` — each script line is a bold `[HH:MM:SS] LABEL:` paragraph. Old prose-with-blockquote examples have been rewritten.

---

## Example 1: A home run (the Moment of the Game material)

### Source (from plays.csv + pitches.csv)

```
idx=10 · inning=2 bottom · batter=Moncada · pitcher=Waldron · event=Home Run
count 2-1 · 4 pitches · Four-Seam 92.5 mph, 2023 rpm
EV 104.3, LA 34°, 388 ft, fly ball, CF
[Padres 0, Angels 1]
```

### Script

```
**[00:21:15] HALLIDAY:** Yoán Moncada digs in, the third sacker,
batting from the left side. Count runs to two and one.

**[00:21:24] HALLIDAY:** Waldron — who has been dancing that
knuckleball up there all evening — this time goes with the straight
stuff. Fastball. Moncada — a short stride — and a *mighty* cut —

**[00:21:33] HALLIDAY:** Oh, he got every bit of it! High drive,
deep to center! Merrill turns, running back, running back — but
there is *nothing* to do but watch it go! That ball lands ten rows
up in the center-field bleachers!

**[00:21:41] SFX:** *[CROWD — ANGEL STADIUM EXPLOSION]*

**[00:21:45] HALLIDAY:** A four-bagger for Moncada — his third
circuit clout of the young season — and the Angels have struck
first here at Angel Stadium! Angels one, Padres nothing, bottom of
the second.
```

Five script lines covering what was one dramatic paragraph in the old prose version. Note the SFX break right after the call — that's where the crowd does the emotional lifting; the transcript acknowledges it explicitly.

---

## Example 2: A routine groundout

### Source

```
idx=11 · inning=2 bottom · batter=Peraza · pitcher=Waldron · event=Groundout
count 0-0 · 1 pitch · Knuckle Ball 80.7 mph
(ground ball, 4-3)
```

### Script

```
**[00:22:04] HALLIDAY:** Oswald Peraza up. First-pitch knuckler —
chopped weakly to the second sacker. Cronenworth picks it up, easy
toss to France. One away.
```

Single script line. Don't stretch routine plays unless they open or close an inning.

---

## Example 3: A nine-pitch strikeout

### Source

```
idx=16 · inning=2 bottom · batter=Trout · pitcher=Waldron · event=Strikeout
count 2-3 · 9 pitches · Four-Seam 93.4 mph, 1999 rpm (swinging K)
```

### Script

```
**[00:26:18] HALLIDAY:** Now stepping to the dish — Mike Trout, the
centerfielder, the Angels' captain. Bases empty, two away in the
second.

**[00:26:28] HALLIDAY:** Waldron gets the sign, the stretch —
*ball one*, outside.

**[00:26:36] HALLIDAY:** The knuckler comes in, Trout lays off —
*ball two*. Two and oh.

**[00:26:44] HALLIDAY:** Waldron has to come in with one — and he
does — *strike one, called!* Two and one.

**[00:26:54] HALLIDAY:** Another knuckler — fouled back into the
screen. Two and two.

**[00:27:04] HALLIDAY:** Full count to Trout, a payoff pitch
coming. Waldron takes his time. The stretch. The pitch —

**[00:27:13] HALLIDAY:** *Swung on and missed!* A nine-pitch at-bat
and Waldron gets Mike Trout! The Padres' man earns his money on
that one, folks — worked through Trout's strike zone and found the
one he wanted.

**[00:27:26] SFX:** *[SMATTERING OF APPLAUSE]*
```

Nine-pitch at-bats deserve pitch-by-pitch breakdown. Each pitch is its own short line so the rhythm matches the call.

---

## Example 4: Inning-break transition

### Between bottom-2nd Angels-at-bat and top-3rd Padres-at-bat

```
**[00:28:42] SFX:** *[CROWD — APPLAUSE AS ANGELS JOG OFF]*

**[00:28:48] HALLIDAY:** End of two. Angels three, Padres nothing.
We'll take a short break.

**[00:29:02] COMMERCIAL:** *[SPONSOR SPOT — WHEATIES: THE BREAKFAST
OF CHAMPIONS, 15 SECONDS]*

**[00:29:17] MUSIC:** *ORGAN — FAST BRIDGE INTO THE THIRD.*

---

### ▲ TOP 3RD — PADRES BATTING · ANGELS PITCHING

**[00:29:28] HALLIDAY:** And we're back at Angel Stadium, top of
the third, Angels on top three to nothing. Nick Castellanos
leading off for the Padres...
```

Notice how the inning boundary is a full **stage transition**: SFX closing the frame, announcer outro, commercial break (optional), musical bridge, new section header, new half-inning begins. The divider `---` + `### ▲ TOP 3RD — …` header visually anchors the shift.

---

## Example 5: SFX-only atmosphere during a quiet moment

Between batters, between pitches, or during a pitching change, it's fine to have a SFX-only script line with no announcer immediately before or after:

```
**[01:02:14] SFX:** *[CROWD SETTLES — MURMUR]*

**[01:02:19] SFX:** *[VENDOR CALL — "HOT DOGS! GET YOUR HOT DOGS!"]*

**[01:02:24] HALLIDAY:** A cool April evening here at Angel
Stadium, the lights taking hold as we move into the middle
innings…
```

These are pure atmosphere — grounded in the real data (it *is* cool, it *is* April, the lights *are* coming on per the atmosphere block). No facts fabricated.

---

## Example 6: Pitching change

### When `plays.csv` shows a pitcher change between rows

```
**[01:15:22] SFX:** *[MURMUR — BALL GOES TO THE MANAGER]*

**[01:15:28] HALLIDAY:** Washington walking to the hill. Here comes
the signal — and Jim Washington's going to make a change. Waldron
is out. Three and two-thirds of work, eight hits, six earned runs
— a tough night for the young knuckleballer.

**[01:15:46] SFX:** *[POLITE APPLAUSE FOR WALDRON]*

**[01:15:52] HALLIDAY:** Coming in from the bullpen — David Morgan.
A right-hander, in his third season with the Padres. Let's see
what he's got tonight.

**[01:16:10] MUSIC:** *ORGAN — "HARD LUCK HARRY" SHORT BRIDGE.*
```

---

## Example 7: The final out and sign-off

```
**[02:55:14] HALLIDAY:** Two away, ninth inning, Tatis Junior at
the plate. Romano ready. The stretch. The pitch —

**[02:55:22] HALLIDAY:** *Swung on and missed!* Strike three! That
will do it, folks — the Angels shut out the Padres, eight to
nothing, here at Angel Stadium!

**[02:55:30] SFX:** *[GAME-ENDING CROWD ROAR — SUSTAINED]*

**[02:55:50] HALLIDAY:** The winning pitcher: José Soriano, five
and two-thirds of scoreless ball, eight strikeouts. The losing
pitcher: Matt Waldron, just didn't have his best knuckler tonight.
The star of the game — Nolan Schanuel, three hits in five trips.

**[02:56:24] HALLIDAY:** From Angel Stadium on this fine April
Friday, this is Howard "Hap" Halliday saying so long. Tomorrow's
another ballgame. Good night, folks.

**[02:57:50] MUSIC:** *PROGRAM CLOSE — ORGAN FANFARE.*

**[02:58:00] STATION ID:** *[KFI LOS ANGELES — SIGN-OFF]*
```

---

## Lessons from these examples

1. **One beat per line.** A pitch, a reaction, an SFX, a crowd note — each is its own paragraph.
2. **SFX is a line, not an aside.** Crowd noise, music, station idents all get their own `SFX:` / `MUSIC:` / `STATION ID:` line at the right timestamp.
3. **Timestamps always lead.** Fixed-width `[HH:MM:SS]` format; approximate from play-index / duration ratio.
4. **Labels always ALL CAPS + colon.** `HALLIDAY:`, `SFX:`, `MUSIC:`, `COMMERCIAL:`, `STATION ID:`.
5. **Inning transitions are structural.** SFX close the previous frame, divider rule + header opens the next.
6. **Facts stay gospel.** Every pitch, count, score, Statcast metric, player name ties to the CSV dataset. Atmosphere, crowd reaction, sponsor reads are the costume.

## Example 4: A double with a runner scoring

### Source

```
5. **Frazier** (vs. Waldron) — *Double.* Adam Frazier doubles (2) on a sharp line drive to right fielder Fernando Tatis Jr. Logan O'Hoppe scores. Adam Frazier to 3rd. **[Padres 0, Angels 2]**
    ↳ count 1-2, 4 pitches
    ↳ Four-Seam Fastball 93.2 mph, 2192 rpm · Batted: EV 100.2 mph, LA 22°, 309 ft, line drive, to RF
```

### Broadcast

> *Adam Frazier steps in, the second sacker for your Angels, a left-handed batter. Count runs to one-and-two. Waldron — the fastball again —*
>
> *Line drive! Right field! A scorcher! Tatis Junior is back — back — he's at the wall — and that ball is off the fence, one hop! O'Hoppe scores easily from second. Frazier — he's rounding first, rounding second, he's going for three, he's got it! A stand-up triple! Er — excuse me, friends — the official scorer has that as a double, Frazier moves on to third on a misplay. The Angels lead it two to nothing. Two down in the second, Frazier on third.*

Notice the self-correction — very authentic to the era. If the scorer's ruling would change the call mid-flight, announcers often fixed it on the fly. Also: describe the outfielder's route, the wall, where the runners end up.

---

## Example 5: A walk

### Source

```
4. **O'Hoppe** (vs. Waldron) — *Hit By Pitch.* Logan O'Hoppe hit by pitch.
    ↳ count 3-1, 4 pitches
    ↳ Sinker 92.0 mph, 1876 rpm
```

### Broadcast

> *O'Hoppe at the plate, the young catcher. Count runs to three-and-one. Here's the pitch — and Waldron catches him on the elbow! O'Hoppe grimaces, he's shaking it out — but he's all right, taking his base. That'll put the tying run — no, a baserunner — at first. One away.*

Short, but note the weather/wound detail. Always give the listener a picture.

---

## Example 6: Opening an inning after a pitching change

### Broadcast

> *Well, folks, welcome back to Angel Stadium, top of the sixth, Angels on top by a score of eight to nothing. And as you might expect, a new man on the hill for San Diego — David Morgan coming in to relieve Waldron, who went three and two-thirds — and he'll be looking to stop the bleeding here.*
>
> *Morgan, a right-hander, in his third season with the Padres. Let's see how he looks…*

Between-inning pitching changes get a short setup. Mention the reliever's handedness and a period-appropriate one-liner about their record or role.

---

## Example 7: Incorporating the atmosphere over time

**Early innings:**
> *The sun still above the third-base grandstand, shining right in the batter's eye here at Angel Stadium — Schanuel gives a little squint, steps out, adjusts his cap…*

**Middle innings (sunset passes):**
> *The light is fading fast now, folks — the sun has slipped behind the stands, the long shadows are stretching across the infield, and those big white light towers have come up. We'll be playing under the lights the rest of the way.*

**Late innings:**
> *A cool night now at Angel Stadium. The stars are out over the center-field pavilion, the lights are blazing, and the Angels are three outs away from the shutout.*

Use the ATMOSPHERE block from the source to pace this arc. Sunlight is a character.

---

## Example 8: Closing the broadcast

> *Swung on and missed! Strike three! That'll do it, ladies and gentlemen — the Angels have shut out the Padres, eight to nothing, here at Angel Stadium on this fine April Friday evening!*
>
> *The winning pitcher: José Soriano, five and two-thirds of goose eggs, eight strikeouts. The losing pitcher: Matt Waldron, who just didn't have his best knuckler tonight. And the star of the game has to be Nolan Schanuel, three hits in five trips, driving in a run, scoring one.*
>
> *The crowd of forty-four thousand five hundred fifty-one giving their club a warm ovation as they head into the clubhouse. A fine night of baseball here in Anaheim.*
>
> *From Angel Stadium, this is Howard Halliday — saying so long. Tomorrow, same teams, same time, same station. Good night, everyone.*

---

## General lessons from these examples

1. **The count matters.** Radio listeners kept track — say it aloud at 0-2, 3-0, 3-2 pivot moments.
2. **Describe the ball.** Direction, height, trajectory, which fielder is chasing.
3. **Follow the runners.** Who scored, who advanced, who's on which base.
4. **Mention the score** after every scoring play. Re-anchor.
5. **Pace with the game.** Quick innings = quick call. Big moments = slow the call down.
6. **Use the atmosphere** throughout — not just the opening. Mention sunlight shifting, lights coming on, crowd swelling, wind changing.
7. **Stay in character** even during weird moments (challenges, delays) — the 1930s equivalent is "waiting on the umpires' conference".
