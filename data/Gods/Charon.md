---
type: smite-god
name: Charon
pantheon: Greek
role: Support
specializations:
- Tank
- Mobility
- Global
damage_type: magical
release_date: March 10, 2026
base_stats:
  health:
    base: 668.52
    per_level: 101.52
  mana:
    base: 299.36
    per_level: 45.36
  physical_prot:
    base: 20.52
    per_level: 3.24
  magical_prot:
    base: 29.7
    per_level: 1.62
  attack_speed:
    base: 0.96
    per_level: 1.29
  move_speed:
    base: 380.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Charon Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Fire a projectile that deals Magical Damage to the first enemy hit
- slot: Passive
  name: Ferryman of Souls
  details:
  - While being ferried, allies take 50% of the damage you take as true damage
  - Any Stun, Displacement, Teleport, Banish, or Grab will immediately eject all allies
    from the boat
  - 'Ferrying Cooldown: 30 seconds'
  description: Any Stun , Displacement , Teleport , Banish , or Grab will immediately
    eject all allies from the boat When any friendly lane minion or jungle monster
    dies, they drop a coin for you to collect that persists for 8 seconds. COins grant
    you 1 gold and a Soul Stack. You lose all soul stacks when returning to base and
    gain 2 max health per stack lost. Allies can pay you 1 gold to ferry with you.
    This grants you a Movement Speed buff while they ride
- slot: 1st Ability
  name: Spectral Surge
  cooldown:
  - 13.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - 'Damage: 80 | 110 | 140 | 170 | 200'
  - 'Damage Scaling: 45% Intelligence'
  - 'Damage Per Tick: 6 | 8 | 10 | 12 | 14'
  - 'Damage Scaling Per Tick: 5% Intelligence'
  - 'Slow: 10 | 12.5 | 15 | 17.5 | 20%'
  - 'Trail Slow: 15%'
  - 'Silence Duration: 1 second'
  - 'Debuff Duration: 3 seconds'
  - 'Range: 9.6 meters'
  - 'Radius: 2.4 meters'
  - 'Cooldown: 13 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Line Damage Fire a soul in a line that deals Magical Damage and Slows
    all enemies, stopping on the first god hit. If the soul hits an enemy god, it
    explodes, dealing Magical Damage , and Silencing all enemies hit by the explosion,
    as well as causing all hit enemies to leave a trail behind them for 3 seconds
- slot: 2nd Ability
  name: Damnation
  cooldown:
  - 16.0
  - 15.5
  - 15.0
  - 14.5
  - 14.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Shield can only be applied once per mark per ability or basic attack
  - Shield health can reach up to 15% of your maximum health
  - 'Damage: 50 | 85 | 120 | 155 | 190'
  - 'Damage Scaling: 40% Intelligence'
  - 'Shield: 40 | 65 | 90 | 115 | 140'
  - 'Shield Max Health Scaling: 2%'
  - 'Attack Speed Reduction: -25%'
  - 'Debuff Duration: 3 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 2.4 meters'
  - 'Cooldown: 16 | 15.5 | 15 | 14.5 | 14 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: After a short delay, a burst of water from Styx appears and deals Magical
    Damage to all enemies in the area. Enemy gods hit are marked for 3 seconds. The
    marked gods are Revealed and have reduced Attack Speed . Additionally, any time
    an allied god hits a marked god, the ally gains a Shield for 3 seconds. Subsequent
    hits grant 25% of the Shield value
- slot: 3rd Ability
  name: Swift Voyage
  cooldown:
  - 17.0
  - 16.5
  - 16.0
  - 15.5
  - 15.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - 'Damage: 65 | 115 | 165 | 215 | 265'
  - 'Damage Scaling: 40% Intelligence'
  - 'Movement Speed Increase: 100%'
  - 'Dash Duration: 2.5 seconds'
  - 'Root Duration: 1 second'
  - 'Wake Root Duration: 0.5 seconds'
  - 'Radius: 4 meters'
  - 'Cooldown: 17 | 16.5 | 16 | 15.5 | 15 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Charge Forward Root Dash forward with increased Movement Speed and
    become Slow Immune and Displacement Immune while charging. Any enemy you collide
    with, or that hits the wake of your boat takes Magical Damage and is Rooted
- slot: Ultimate
  name: Summon Styx
  cooldown:
  - 110.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - 'Damage: 255 | 290 | 355 | 420 | 485'
  - 'Damage Scaling: 50% Intelligence'
  - 'Feared Duration: 0.8 | 0.9 | 1 | 1.1 | 1.2 seconds'
  - 'Protections: 20 | 25 | 30 | 35 | 40'
  - 'Movement Speed: 40%'
  - 'Buff Duration: 3 seconds'
  - 'Range: 320 meters'
  - 'Wake Range: 9.6 meters'
  - 'Cooldown: 110 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Long Range Damage Gain CC Immune and summon a massive wave across the
    battlefield. Enemy gods hit by the wake take Magical Damage and are Feared . Allied
    gods gain Protections for 3 seconds. Additionally, all allies standing within
    the zone behind the wave are granted Movement Speed
aspects:
- name: Aspect of the Tollkeeper
  kit_changes: Passive coins are pulled to you while in assist range. Damnation no
    longer applies an attack speed slow or Shield. Instead, it summons a soul on enemy
    gods hit that deals damage when you hit them. Once for attacks, three times for
    abilities. Spectral Surge refreshes the duration of the soul but does not silence.
source_url: https://wiki.smite2.com/w/Charon
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Charon Basic Attack
- Ferryman of Souls
- Spectral Surge
- Damnation
- Swift Voyage
- Summon Styx
<!-- WIKI:END -->
