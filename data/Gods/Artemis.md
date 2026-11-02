---
type: smite-god
name: Artemis
pantheon: Greek
role: Carry
specializations:
- Sharpshooter
- Lockdown
damage_type: physical
release_date: February 21, 2025
base_stats:
  health:
    base: 569.48
    per_level: 86.48
  mana:
    base: 296.0
    per_level: 42.0
  physical_prot:
    base: 18.76
    per_level: 2.76
  magical_prot:
    base: 25.3
    per_level: 1.38
  attack_speed:
    base: 1.02
    per_level: 1.51
  move_speed:
    base: 370.0
    per_level: 0.0
  attack_power:
    base: 47.95
    per_level: 2.59
  health_regen:
    base: 1.7
    per_level: 0.2
  mana_regen:
    base: 1.33
    per_level: 0.11
abilities:
- slot: Basic Attack
  name: Artemis Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Fire a projectile that deals Physical Damage to the first enemy hit
  damage_type: physical
  detail_kinds:
  - null
  - physical
  - mechanic
  - mechanic
- slot: Passive
  name: Still Target
  details:
  - You are able to detect nearby enemy gods in stealth grass
  description: Artemis deals 15% Increased Attack Damage to gods and 30% to minions
    that are afflicted by Crowd Control
- slot: 1st Ability
  name: Transgressor's Fate
  cooldown:
  - 14.0
  - 13.0
  - 12.0
  - 11.0
  - 10.0
  cost:
  - 45.0
  details:
  - A max of 4 traps can be placed at the same time
  - The trap deals damage every 1 second for 3 seconds
  - 'Damage Per Tick: 26 | 36 | 46 | 56 | 66'
  - 'Damage Scaling Per Tick: 30% Strength'
  - 'Root Duration: 1.75 seconds'
  - 'Cripple Duration: 1.75 seconds'
  - 'Range: 6.4 meters'
  - 'Radius: 0.8 meters'
  - 'Cooldown: 14 | 13 | 12 | 11 | 10 seconds'
  - 'Cost: 45 mana'
  description: Place a trap on the ground. Enemy gods that come in contact with it
    activate it, Rooting , Crippling , and repeatedly dealing Physical Damage over
    3 seconds
  damage_type: physical
  detail_kinds:
  - null
  - null
  - physical
  - physical
  - debuff
  - debuff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 2nd Ability
  name: Vengeful Assault
  cooldown:
  - 14.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - On activation you are cleansed of Slows and become Slow Immune for 0.6 seconds
  - While the buff is active, gain a charge each time you hit an enemy god with a
    Basic Attack
  - After reaching 4 charges they are consumed, extending the duration of the buff
    by 3 seconds
  - 'Movement Speed: 25%'
  - 'Attack Speed: 25 | 35 | 45 | 55 | 65%'
  - 'Buff Duration: 3 | 3.5 | 4 | 4.5 | 5 seconds'
  - 'Cooldown: 14 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Greatly increase your Movement Speed and Attack Speed
  detail_kinds:
  - slow
  - null
  - null
  - buff
  - buff
  - buff
  - mechanic
  - mechanic
- slot: 3rd Ability
  name: Suppress the Insolent
  cooldown:
  - 9.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - 'Damage: 100 | 150 | 200 | 250 | 300'
  - 'Damage Scaling: 65% Strength'
  - 'Slow: 25%'
  - 'Slow: 2 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 2.4 meters'
  - 'Cooldown: 9 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: AREA DAMAGE SLOW Fire a volley at a target area dealing Physical Damage
    and Slowing enemies
  damage_type: physical
  detail_kinds:
  - physical
  - physical
  - slow
  - slow
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: Ultimate
  name: Calydonian Boar
  cooldown:
  - 90.0
  cost:
  - 45.0
  details:
  - Deals Physical Damage and Stuns enemies
  - The Boar is Immune until it hits the first god and then continues to charge other
    gods for its lifetime
  - You are CC Immune for 1.5 seconds after activating this ability
  - The Boar will Basic Attack minions if there are no nearby gods
  - 'Dash Damage: 150 | 220 | 290 | 360 | 430'
  - 'Dash Damage Scaling: 90% Strength'
  - 'Stun: 0.9 | 1 | 1.1 | 1.2 | 1.3 seconds'
  - 'Boar Health: 350 | 450 | 550 | 650 | 750'
  - 'Radius: 9.6 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 45 mana'
  description: Summon the great that charges the nearest enemy god
  detail_kinds:
  - physical
  - mechanic
  - mechanic
  - null
  - physical
  - physical
  - stun
  - mechanic
  - mechanic
  - mechanic
  - mechanic
aspects:
- name: Aspect of the Wild
  kit_changes: Transgressor's Fate no longer roots or cripples gods but can now target
    minions. Triggered traps now also heal Artemis and deal damage to enemies in a
    larger area.
source_url: https://wiki.smite2.com/w/Artemis
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Artemis Basic Attack
- Still Target
- Transgressor's Fate
- Vengeful Assault
- Suppress the Insolent
- Calydonian Boar
<!-- WIKI:END -->
