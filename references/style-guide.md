# Style Guide — 1930s Radio Baseball Announcer

## The era and its sound

Radio baseball broadcasting came of age in the 1920s and matured through the 1930s. The pioneers — Graham McNamee (NBC, World Series), Red Barber (Cincinnati, then Brooklyn), Bill Stern (NBC), Ted Husing (CBS) — were Depression-era showmen who had to *paint the game* for listeners who could not see it. The voice is:

- **Theatrical.** They were doing live theater over a wire. Expect exclamations, dramatic pauses, tonal swings.
- **Verbose.** Dead air was the enemy. They filled innings with digressions about the weather, the crowd, a dog on the field, an old-timer in a straw boater behind the home dugout, the aroma of hot dogs and peanuts.
- **Folksy.** Listeners were the whole country, and the broadcaster was their neighbor. Metaphors come from farming, fishing, boxing, trains, the stockyards.
- **Formal in address.** "Ladies and gentlemen", "Good afternoon, fans", "Friends of the Angels/Padres/Cardinals everywhere". Courtly.
- **Musical in pacing.** Sentences build, pause, release. Use em-dashes and ellipses. Use italics sparingly for emphasis (in text form).
- **Rooted in the park.** Always remind the listener *where* we are: the infield dirt, the grass, the light beyond the scoreboard, the flags on the foul poles, the crowd behind the catcher.

## Structural conventions

### Opening ("signing on")

Begins with a station ident (imagined), then:

1. Greeting the audience ("Good afternoon, friends…")
2. Location ("…coming to you live from Angel Stadium here in Anaheim…")
3. Weather and conditions (translate from the ATMOSPHERE block — temperature, sky, wind direction on the flags)
4. Crowd ("…and what a crowd we have today, [number] strong, a sellout / a Sunday crowd / a Friday-night ballpark…")
5. The storyline ("…the [home] looking to [win the series / even the series / avenge last night's loss], against the [away]…")
6. The starting pitchers ("…on the hill for the Angels, José Soriano; for the Padres, Matt Waldron…")
7. Handoff to the first pitch ("…and here we go, friends, the umpires are ready, the batter's in the box, first pitch coming right up…")

Two to four paragraphs. Long enough to settle in, short enough that the game starts feeling imminent.

### Between innings

Short asides work beautifully. "Well, folks, as the teams change sides, a word about the weather…" — or a brief observation about the crowd, the flag, the setting sun, a visiting dignitary in a box seat. One paragraph between each inning is enough.

### Inning headers

Use bold or a section header to mark each inning clearly, but in the radio voice call it out: "**TOP OF THE FIRST.** Leading off for the Padres — Jake Cronenworth, the second baseman, stepping in…"

### Calling a plate appearance

Typical arc:
1. **Who's up.** "Stepping in now is [name], the [position]…"
2. **The pitch.** "The pitcher checks the sign… comes set… *here's the pitch* —"
3. **The result.** Embellished (see below).
4. **The state.** Count, outs, runners. "That brings the count to 2-and-1. One out. Men on first and second."

For routine outs, collapse to one sentence. For big moments, stretch out.

### The big moment (MOMENT OF THE GAME)

Source gives you one. Hold it. Let the count build. Describe the pitch, the swing, the flight of the ball. Follow it. React. Let the crowd react. *Then* summarize.

### Closing ("signing off")

1. Final out.
2. Quick crowd note.
3. Final score, recited clearly.
4. Decision line ("the winning pitcher, José Soriano; the loser, Matt Waldron").
5. A storyline wrap ("this one goes down as a [home-opener rout / pitchers' duel / slugfest]…").
6. Thanks to the audience, sponsor tag if you wrote one in, station ident.

## Voice rules

1. **Address the listener** often. "Folks", "friends", "ladies and gentlemen", "fans out there in radio land". Not constant — but at transitions.
2. **Use the present tense** for the live call. "He swings — *he misses* — strike two!" Past tense only in recaps between innings.
3. **Narrate pitch sequences** when the count gets interesting or the at-bat matters.
4. **Describe ball flight** physically: "high fly ball… deep to right… Tatis is back to the warning track… at the wall…". Height, direction, outfielder's path.
5. **Count and outs** reinforced constantly. Radio listeners had no scoreboard. "Two away, runners at the corners, 1-and-1 the count."
6. **Weather and sun** mentioned across the game, not just the opening. In a 6:39 PM start with 7:24 PM sunset, mention the long shadows in the 4th, the lights taking hold in the 5th, the night sky by the 7th.
7. **Crowd as a character.** "The crowd comes to its feet", "a murmur through the grandstand", "a collective groan", "an eruption of applause".
8. **Scoreboard cadence.** After runs score, re-recite the score. "And so the Angels lead it, 1 to nothing, in the bottom of the second."

## Translating Statcast into radio English

The source PBP lines look like:

```
↳ count 2-1, 4 pitches
↳ Four-Seam Fastball 92.5 mph, 2023 rpm · Batted: EV 104.3 mph, LA 34°, 388 ft, fly ball, to CF
```

Never speak those numbers as numbers in the broadcast. Translate them to observational English. See `vintage-phrases.md` for a menu. Rough scale:

### Exit velocity (EV, mph)
- 60–80: "bloop", "chopper", "flare", "soft fly", "dunker", "half-swing grounder"
- 80–90: "line drive", "solid shot", "base hit all the way"
- 90–100: "rope", "scorcher", "rifle shot", "hard-hit ball"
- 100–108: "cannon shot", "absolutely crushed", "my, did he get a hold of that"
- 108+: "I don't know that I've ever seen a ball hit harder", "like it was shot out of a gun"

### Pitch velocity (mph)
- <85: "a change-up", "slow curve", "junkball", "takes something off it"
- 85–92: "fastball", "straight stuff", "heater"
- 92–96: "good hard fastball", "live arm", "the pill is really jumping"
- 96–100: "blazing fastball", "express train", "you can hear the catcher's mitt pop from here"
- 100+: "*unprintable — that ball is a rumor*", "that's the hardest pitch I've seen thrown all year"

### HR distance (ft)
- <360: "just enough", "snuck over the short porch", "a wall-scraper"
- 360–400: "solid poke", "well-struck", "up on the bleachers"
- 400–430: "a real clout", "deep into the bleachers", "a mighty wallop"
- 430+: "a tremendous drive", "fly me to the moon", "a tape-measure job — they'll be measuring that one tomorrow in the papers"

### Launch angle (degrees)
- Don't name it. Describe trajectory: "line drive", "fly ball", "towering fly", "pop-up", "screaming liner", "one-hopper to the fence".

### Spin rate (rpm)
- Don't name it. If very high (2500+), the ball "bites", "hooks sharply", "the bottom drops out". If low on a "knuckleball", "the ball is dancing, floating, it don't know which way it's going".

## Sponsor spots (optional, period-authentic)

If you want to add one or two, keep it brief and wedged between innings. Think: Wheaties, Camel cigarettes, General Mills, Gillette Blue Blades, Lifebuoy soap, Coca-Cola. Example:

> *And while we have a moment between innings, friends — a word from our sponsor. Wheaties, the breakfast of champions. If you're looking for the energy to step to the plate each morning and knock one out of the park — that's Wheaties, the breakfast of champions.*

Don't overdo. One or two in a full broadcast is plenty.

## Things to avoid

- **No modern slang.** No "dude", "for real", "insane", "absolute unit".
- **No modern analytics terminology.** No "exit velocity", "launch angle", "WAR", "wRC+", "OPS", "K/9". Translate everything into observational language.
- **No reference to television**, video replay, instant replay, challenges, or anything that implies visual retrieval. Radio only.
- **No current-era player comps** (no "reminds me of Mike Trout"). If you want a comp, use an era-appropriate player (Lou Gehrig, Jimmie Foxx, Dizzy Dean, Carl Hubbell, Joe DiMaggio — carefully, given DiMaggio debuted in '36).
- **Nothing anachronistic.** Stick to language and references that would work on a radio broadcast from roughly 1925–1939.
- **Don't change the outcome of plays.** The voice is costume. The facts are gospel.

## A short example (for shape, not content)

*Well, friends, what a scene we have here at Angel Stadium this cool April evening — the sun just dipped behind the third-base grandstand, the flags on the light towers hanging limp in what little wind there is, and forty-four thousand five hundred fifty-one of the faithful on hand to see if the Angels can take the series from San Diego. On the mound for your Angels, José Soriano — six-foot-four, right-hander, an arm like a young cannon. For the visiting Padres, it's Matt Waldron, the knuckleball artist, and if you've never seen a knuckler, folks, you're in for a treat — that pill dances up there like a butterfly with the hiccups…*
