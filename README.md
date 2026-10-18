# CELLOG — the spreadsheet slog

*An Excel esports manager: CELL + SLOG. Plan every hour, train seven skills,
climb five leagues — one cell at a time.*

**Play it at [cellog.vercel.app](https://cellog.vercel.app)** (Vercel project
`cellog`, team shilkteam; every push to `main` redeploys it). The same build is
also on GitHub Pages at [shilk3.github.io/cellog](https://shilk3.github.io/cellog/)
(the repository was renamed from `excel-run-sim`; the old Pages address no
longer works). The cellog.website domain has been retired.

**Guides** (☰ menu, also offline): 🗺️ [Mechanics Map](https://cellog.vercel.app/guide/map.html)
— every mechanic as a box with arrows for what it pushes on (tap one to
trace it) — and 📊 [Mechanics Infographic](https://cellog.vercel.app/guide/infographic.html),
every rule and number. They're copies of two claude.ai artifacts, built by
`python3 tools/build_guides.py <infographic Main.dc.html> <map .html>`;
rebuild them whenever a rule changes, with the usual version bump.

A mobile-first simulation game: manage a rising Excel esports competitor. Every
day has up to 24 hours — split them across Skill Training, Gym, Sleep,
Relax, and Food. Everything is connected:

- **Skill Training** raises one of 7 case specialties — Data Analysis,
  Mapping, Text Processing, Game Logic, Math & Formulas, Time & Dates, and
  Cards & Random. During the season only 1-3 skills are "active"
  (trainable) each round — 1 in 30% of weeks, 2 in 50%, 3 in 20% —
  revealed at the start of that round's week —
  every match that week tests exactly those skills. The other 4-6 sit
  locked and slowly rust. Preseason and the off-season (at home or at
  training camp) have no matches, so all 7 are open.
- **Gym** raises Physical Health — but low Physical Health caps how much
  your skill training actually helps.
- **Sleep** builds Rest: 7h holds it, each hour short costs 1.3 a day,
  each hour over adds 1.4. Rest below 80 wears down Physical Health and
  Calm, more the lower it goes. Sleep also adds +1.5 Calm a day
  at 7h, +3 at 8h or more.
- **Relax** builds Calm on its own (training doesn't drain it): 3h
  holds it, each hour short costs 2.4 a day, each hour over adds 2.4.
  Relax past 100 isn't wasted: Calm past 100 becomes 😎 Chill, a reserve (half rate,
  up to 130, fading 1 a day) that drains first on short-Relax days — match
  day still counts Calm as 100 at most. Let it hit 0 and you burn out,
  tanking your training until you recover.
- **Food** builds Nutrition, which keeps tomorrow's day at full length — see below.
  **Carb loading:** once Nutrition is already at 100, each Food hour past 1h banks one extra hour for the next
  day only (up to +3h at 4h of Food) — it moves hours between days, 1:1.
  End Week / To Match carry on with the plan as it is, so unassigned extra hours
  go unused (the week summary says how many).
- **Decay is universal**: every stat needs upkeep or it slips — an
  inactive skill, Gym, Sleep, Relax, or Food below its
  threshold hours (shown as a marker on each slider) causes that stat to
  fall instead of rise.
- **Rest** swings training itself (skills and Gym), smoothly: ×1 at 70
  Rest or below, rising to ×2 at 100 (85 Rest trains at ×1.5).
  **Overcharge:** with Rest already at 100, sleeping past 7h pushes that
  day's training higher still — ×3 at 10h, ×4 at 12h, linear between. **Calm** swings match day specifically: low
  Calm can cut your active skills' effect on a match in half.
  **Nutrition** swings how many hours you get at all: below 40 your day
  shrinks to 16h, sliding up to a full 24h at 90+.
- Every Gym hour carries a 2.5% injury chance that day (8h, the max, is
  20%; Sports Physio cuts it). An injury costs 5–10 Health and locks the
  Gym for 3–5 days, but never stops you playing matches. A hired 🧊 Recovery
  Program takes 1–3 days off, even when hired after you're hurt (at least 1
  day left; once per injury).
- **Energy Items** (in Staff & Items) are instant top-ups, each usable
  once a week: ☕ Coffee $40 (+10 Rest, −4 Rest the next day), 🧃 Energy
  Drink $90 (+15 Rest, +10 Calm, then −5 Rest, −3 Calm), 💆 Spa
  Day $250 (+10 Rest, +30 Calm, no crash). Nothing goes past 100.
- **Equipment** (also in Staff & Items) is bought outright and works until
  the current year ends, then wears out — never pro-rated, so buy early:
  🖥️ Second Monitor $700 (+5% skill training), 💻 Gaming PC $5,000
  (+10%), 🪑 Ergonomic Chair $2,400 (−20% Gym injury risk), 🎧
  Noise-cancelling Headphones $900 (+0.5 Calm a day), 🛏️ Memory-foam
  Mattress $2,800 (−25% Rest lost from short sleep).
- **Prize money**: a win pays $60 + your new rating ÷ 20 (about $85 at
  rating 500); a loss pays nothing. Winning the playoffs adds a $1,000
  champion bonus (+40 rating).
- Skills train up to 50 on your own. **Staff** are hired a week at a time
  (a week ends after each match), paid up front, pro-rated if hired
  mid-week; someone already hired can be moved up to a newly unlocked
  level for just the extra wages. Every coach and support-team member has an optional
  🔁 Auto-rehire switch that keeps them on at the same level each new week
  (a coach even when their skill isn't in that week's focus)
  while you can afford it (if you can't, they're off that week, the switch
  turns itself off and you're told). A hired Coach lifts that
  skill's ceiling (Lv1 60 … Lv5 100), speeds training and stops that skill
  rusting while hired (even in a week you don't train it), but never past
  your league cap (see Specialisations below). Above the ceiling
  a skill holds with an hour a day and slips with less. Physical Health caps
  at 70 without a hired Sports Physio. Higher staff levels need a one-off
  fee and a high enough league, and cost more per week; wages are tuned so
  you can afford roughly 90% of what you'd want in a 1-skill week and 40% in
  a 3-skill week.
- **Work** funds everything else. 9h/day, except on paid **🏖️ annual
  leave** — the whole 21-day preseason (skill coaches are half price then
  too): the Work (or Pro Duties) row is greyed
  out, pay continues as normal, no chances are at risk (used ones still
  come back on time, shown on the row), and a Pro's
  technique clock waits; it comes back at the full requirement when the
  season starts (a screen says so if your plan then needs trimming). A job
  search carries on as normal through leave. Otherwise no exceptions (up
  to 4h of overtime on top pays half your hourly rate — $4/h at the
  starting $70/day, rising with raises) — you
  start with 3.0 chances, and the bar shows exactly what today's shortfall
  will cost before you end the day. Pay is tied to still *having* the job,
  not to hitting the exact hour target every day: come up short and you
  lose a chunk of a chance scaled to the shortfall (a near-miss costs
  barely anything, skipping the day entirely costs a full chance,
  regained after 3 weeks), but you're still paid in full. Only running out
  of chances actually costs you income — you're fired, and the same slider
  becomes a Job Search until you log a random 10–40 cumulative hours
  (rolled each time you lose the job, and shown on the slider) — at least 1h
  of searching a day, or the day can't end, so you can't idle into debt. Once you've
  reached League 2 (ever) and your 7 skills average 75+ (85+ once League 1
  is your best), while employed, you go pro automatically (a screen says
  so). The sponsorship lasts to the end of the year whatever your skills
  do, and is renewed only if the average still clears the bar when the year
  ends; if not, the new-year screen
  says so and you're unemployed, back to a Job Search. As a pro: Work
  drops to 5h/day of Pro Duties, same chances rule. Pros also have to stay
  current — there are 20 Excel techniques, and one you haven't mastered
  appears roughly every 38 days as a pro (Half 19, Short 10) needing 30–45h
  (Half 15–23, Short 8–12) to master — any Pro Duties hours beyond the 5h
  minimum go toward it. That's about 2.5 years as a pro to master all 20,
  after which no more arrive; masteries are kept for good. Falling behind
  never costs you progress, but every not-yet-mastered technique costs 5%
  match performance.
- **Cost of living**: $50/day, charged no matter what — employed or not,
  every phase. Pay isn't flat: Work starts at $70/day and rises $10 at
  each year end up to $150; Pro Duties start at $150/day (or your work pay,
  if higher) and rise $10 a year with no limit. Pay never drops: losing the
  job keeps your rate for the next one, and losing the sponsor moves your
  work rate up to your pro rate (as far as $150). The new-year screen includes a cash-flow summary of the
  year just finished — pay earned, match winnings, expenses paid, the net,
  and any raise you just earned.

**End Day / To Match**: End Day plays one day. To Match (End Week outside the
season, up to 7 days) repeats today's plan up to and including the next match,
then shows the result plus a week summary of how every stat moved. It stops
early so you can re-plan on an injury, losing/finding a job or going pro,
burnout, a new technique to master, or Nutrition shrinking the day below what
your plan needs. Each of those events also gets its own screen whenever it happens —
after End Day too — saying what changed and what to do about it. Summary
screens share one layout: icon, title, then sections — how it went (key
facts), a Start / Now / Change table for every skill, Health, Rest, Calm,
Nutrition, cash and rating, and a short "What's next" list.

**Specialisations**: pick 3 ⭐ skills. They can reach your best league's
skill cap and the other 4 stop 20 lower — League 5: 60/40, League 4: 70/50,
League 3: 80/60, League 2: 90/70, League 1: 100/80 (coaches still set each
skill's own ceiling). Change them any time from Career, but a skill that
stops being one drops straight to the lower cap (the picker shows exactly
what each change costs first). Every rival has 3 specialisations too, fixed
for good, under the same caps, with levels that follow their rating — so
they rise and fall with their results.

**Experience**: every match a ⭐ specialisation is in the week's focus earns
it 🎓 XP, win or lose — +2 in a Full game (+4 Half, +8 Short), double in
playoff matches; a focus skill that isn't a ⭐ earns nothing, except +1 (+2,
+4) in a playoff — but only while you play in League 4 or higher. Up to 100
per skill and it never rusts, so a ⭐ fills in about 3–5 seasons; rotating
your ⭐s fills all seven in about 10–13. XP is also each
skill's floor: a skill never rusts below its XP, and a ⭐ specialisation you
swap out only drops to its XP if that's above the lower cap (XP 100 → it
stays at 100). It shows as a
violet strip along the bottom of each skill bar (Plan and Career), as XP
rows on the result screen and as 🎓 Experience in the progress tables.
Experience sets your ⏱ finish time: 30:00, less a minute per 10 XP (the
week's focus skills' average), less 0–6 minutes of the day's form — never
over 30:00. Rivals' experience comes with their league (League 5: 0, 4: ~10,
3: ~25, 2: ~45, 1: ~65, a little higher or lower with rating).

**Match day**: both sides get a match-day rating = performance × 8 +
focus-skill edge + luck, and the higher one wins — unless the scores end up
level: a ⏱ dead heat (real totals within 60 — about 1 even game in 4), won
by the faster finish. When luck carried the winner past that line, the margin
shown is how far past it they got, on the luck's ⅕ scale (61–67 → by 1). No draws, league or playoffs. Rating isn't part of it:
it rises and falls with results (on rating-vs-rating Elo maths, a 300 gap =
10-to-1) as a record of how you've done, and sets prize money. Your
performance comes from your stats — all 7 skills averaged (55%), Health
(25%), Calm (15%) and Rest (5%); a rival's from their 7 skills, with Health,
Calm and Rest at 80. Rivals' skills are anchored to their league: a
mid-table rival's ⭐ skills sit 10 under the league cap, ±0.06 per rating
point from the league's middle. Whoever averages higher in the week's focus
skills gets 10 match-day rating per point ahead (🎯 Focus-skill edge) —
shown on the result screen and the next-match preview. Luck is random for
both sides every match, drawn so the odds follow an Elo-style curve on the
match-day gap (a 250 gap makes you a 10-to-1 favourite) — upsets always
stay possible — and the scores
show each side's luck at a fifth of its real draw (topped up just enough to
explain an upset), so luck reads as the small nudge it usually is. The result
screen leads with VICTORY / DEFEAT by the margin and the round, then your
win chance, both sides' numbers side by side (Head to Head), what changed
(rating, table position, cash, record), a preview of the next match
(opponent, ratings, table places, win chance and the week's focus) and
Continue — with the collapsible explanations below it. Both finish times show
under Head to Head, lit up when they settled a dead heat. League tables rank
by wins, then head-to-head between tied players, then rating; they show W–L
and form (the last 5 results). Seasons from before v4.76 keep their draws
(W–D–L).

**Game length**: chosen when a game starts, and each length keeps its own
save — so up to three games on one device (☰ → 🎮 Games to switch, start or
restart one). ☰ → 💾 Export / Import Save has a tab per length, so each game
is exported or imported on its own: a code only goes into its own length's
slot, and importing a game you're not playing leaves you in the one you are. All three have the same 5 leagues, and a year ends on the day
of the Final.

| Length | Preseason | League size (rounds) | Playoffs | Up / down | Year |
|---|---|---|---|---|---|
| Short | 1 week | 10 (9) | top 4: SF → Final | 2 / 2 | ~12 weeks |
| Half | 2 weeks | 20 (19) | top 8: QF → Final | 3 / 3 | ~24 weeks |
| Full | 3 weeks | 40 (39) | top 16: R16 → Final | 4 / 4 | ~46 weeks |

The off-season is one week per playoff round (Short 14 days, Half 21, Full
28). A save from before game lengths is the Full game. The numbers below are
the Full game's.

**The season**: a 21-day preseason to train (annual leave), then a 39-round regular season —
one match a week against a named rival, the full schedule known in advance.
Finish in the top 16 of your 40-competitor league to reach the knockout
playoffs (Round of 16 → Quarterfinal → Semifinal → Final, single elimination).
Lose a playoff match and you're out; win the Final and you're champion. The
day of the Final is the year's last day for everyone. Miss the playoffs and
you get a 28-day off-season up to it, so missing the cut is never a worse
deal than qualifying and getting knocked out early. Get knocked out and you
get the off-season too, for the rest of the playoff window (Round of 16
exit: 21 days, Quarterfinal: 14, Semifinal: 7). Reach the Final, win or
lose, and the new year starts straight after it. When the season ends every
skill slider goes back to 0h, so the off-season starts with a fresh plan.

**🏕️ Training camp** (optional, paid): spend the off-season at an
all-inclusive camp instead — $60 a day for the days left, paid up front (it
covers living costs). Camp life takes 10h a day and runs Sleep, Relax, Food
and Gym for you, as if you'd planned an hour over each one's minimum (8h,
4h, 2h, 2h; no injuries — an injury you already have swaps the Gym session
for rehab, which holds Health); the other 14h are all for skills, with 8h
sleep's usual training boost (×2.33 once Rest is full), every support role at the best level your league allows and a coach on every skill at the
best level you've unlocked. Work stops (unpaid leave; a pro's sponsor counts
it as Pro Duties and keeps paying; a job search waits) and hired staff are
paused, picked up again by auto-rehire after camp. It's offered when your
season ends; if you can't pay yet, the top bar keeps the offer — its price
falls each day.

**Leagues**: 5 tiers (League 1 at the top, League 5 at the bottom — new
careers start at the bottom). Every league has a persistent roster of 199
named rivals total across all 5 tiers, whose ratings evolve from real
simulated results every week, exactly like yours — it's a living world, not
scenery. Every tier runs a genuine round-robin schedule in lockstep with
your own matches, so all 5 tables are live and visible from round 1 of the
season, not just once it ends. Four go up from every league below League 1:
the playoff champion, plus the top 3 of the table other than the champion
— so a top-3 finish is always promoted, and anyone who makes the playoffs
can still win their way up. Finish bottom 4 and you're relegated. This
applies to every competitor in every league, not just you — every league
plays out its own knockout too — so rivals you've never played can climb or
fall in the background. Promotion/relegation is applied once the playoffs
are over. Check the Leagues screen any time to see all 5 tables, or jump
there directly from the Career modal.

**Phase screens**: every change of phase (preseason → season, season →
playoffs or training camp, playoffs → camp/offseason, offseason → the new
year) opens a screen that sums up the phase just finished — table finish,
rating, cash and biggest skill gains — and says what's coming next. A new
career starts with a five-page quick tutorial right after you name your
player; replay it any time from the menu (📖 Quick Tutorial).

**Completion** (📈 in Career) is one percentage of how much of CELLOG
you've done. Every goal counts: each league climbed, each of the 7 skills at
100 and its XP at 100, every pro technique (half a goal each), and top of
the League 1 table and its playoffs. Partly done counts partly, and each
goal keeps its best, so rust or a lost title never takes it back down.

**Match History** (menu, the Log header, Leagues and Career) has an
**Upcoming** tab — the rest of the regular season with each opponent's rating,
table position and your win chance, then your path through the playoff
bracket once it starts, plus the whole playoff bracket (seeds, results, the
champion) during the playoffs and offseason — and keeps every match
you play — tap one to reopen its full result screen — plus every result in
all 5 leagues, round by round, for this season and last. Tap any rival's
name (there or in a league table) to see their season so far. Your matches
and every rival's page share one layout: round, W/L, the opponent with their
table position going in, their rating, the rating change, and your (or
their) own position going in, for this season and last.

Pages opened from another page go back one step when closed (✕ or tapping
outside), keeping your scroll position — e.g. Leagues → a rival → ✕ returns
to Leagues.

Rating, Cash, stats, and unlocked staff levels all carry over between years
and leagues.

## Playing it on your iPhone

This is a installable web app (PWA) — no App Store or Xcode needed.

1. Host the folder (see below) or open `index.html` directly in Safari.
2. In Safari, tap the **Share** icon → **Add to Home Screen** → **Add**.
3. Launch it from your home screen — it runs full-screen and saves your
   progress on-device (`localStorage`), with basic offline support via a
   service worker.
4. Safari and the Home Screen app keep **separate saves**. To move a career
   between them (or to another device), open ☰ → **💾 Export / Import Save**,
   tap **Copy save code** (or Share / Save to Files), then paste it into
   **Import** on the other side. The code is your whole career, gzipped and
   base64'd (~20 KB).

### Running it locally

It's a static site with no build step or dependencies:

```sh
python3 -m http.server 8000
# then open http://localhost:8000 on your phone (same network) or in a browser
```

For access from an iPhone on the same Wi-Fi, serve it from your computer and
open `http://<your-computer-ip>:8000` in Safari, or deploy the folder as-is
to any static host (GitHub Pages, Netlify, Vercel, etc.) and open that HTTPS
URL in Safari.

## Maybe later

Ideas discussed and parked for now:

- **Upkeep that grows with level** — higher skills rust faster (about 4 a
  week at 100), coaches halve rust instead of stopping it, and the hours
  needed to hold a skill rise with it (1h below 60, 2h at 60–79, 3h at 80+).
  Parked because it may make the game too hard alongside specialisations.

## Files

- `index.html` — markup/layout
- `style.css` — mobile-first dark UI
- `game.js` — game state, daily simulation, match/shop logic, rendering
- `manifest.webmanifest`, `sw.js`, `icons/` — PWA install + offline support
