---
type: smite-god
name: Apollo
pantheon: Greek
role: Carry
specializations:
- Constant Damage
- Global
- Utility
damage_type: physical
release_date: May 19, 2025
base_stats:
  health:
    base: 577.0
    per_level: 94.0
  mana:
    base: 322.62
    per_level: 48.3
  physical_prot:
    base: 20.04
    per_level: 2.76
  magical_prot:
    base: 25.3
    per_level: 1.38
  attack_speed:
    base: 1.0
    per_level: 1.4
  move_speed:
    base: 375.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Apollo Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Fire a projectile that deals Physical Damage to the first enemy hit
- slot: Passive
  name: Audacity
  details:
  - 'Bonus Attack Speed: 100%'
  - 'Bonus Basic Attack Projectile Speed: 20%'
  description: FASTER ATTACKS AFTER HITS Gain a stack of for each successful Basic
    Attack on any enemy and for each successful damaging ability on enemy gods. At
    10 stacks you gain increased Attack Speed and Basic Attack Projectile Speed for
    your next 5 Basic Attacks
- slot: 1st Ability
  name: So Beautiful
  cooldown:
  - 11.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage: 90 | 150 | 210 | 270 | 330'
  - 'Damage Scaling: 90% Strength'
  - 'Range: 8.8 meters'
  - 'Radius: 0.8 meters'
  - 'Cooldown: 11 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Send a projectile forward that deals Physical Damage
- slot: 2nd Ability
  name: Serenade
  cooldown:
  - 15.0
  cost:
  - 60.0
  details:
  - 'Mesmerize Duration: 1.5 | 1.7 | 1.9 | 2.1 | 2.3 seconds'
  - 'Protections: 10 | 15 | 20 | 25 | 30'
  - 'Protection Buff Duration: 5 seconds'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 15 seconds'
  - 'Cost: 60 mana'
  description: MESMERIZE AND PROTECT Sing to Mesmerize all nearby enemies and gain
    additional protections
- slot: 3rd Ability
  name: The Moves
  cooldown:
  - 15.0
  cost:
  - 70.0
  details:
  - Any enemy hit provides 1 stack of Audacity
  - 'Damage: 80 | 125 | 170 | 215 | 260'
  - 'Damage Scaling: 70% Strength'
  - 'Speed Buff: 15 | 17.5 | 20 | 22.5 | 25%'
  - 'Speed Buff Duration: 5 seconds'
  - 'Slow: 15 | 17.5 | 20 | 22.5 | 25%'
  - 'Slow Duration: 5 seconds'
  - 'Range: 7.2 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 15 seconds'
  - 'Cost: 70 mana'
  description: Dash forward dealing Physical Damage and Knocking Aside all enemies.
    At the end of the Dash all nearby allies gain a Speed Buff and all nearby enemies
    are Slowed
- slot: Ultimate
  name: Across the Sky
  cooldown:
  - 110.0
  cost:
  - 20.0
  details:
  - 2 Allies can join the Chariot ride by interacting with his takeoff location. Allies
    have until Apollo reaches max height to join
  - Carrying an Ally costs additional mana
  - You are CC Immune while using this ability
  - 'Damage: 70 | 95 | 120 | 145 | 170'
  - 'Damage Scaling: 25% Strength'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 110 seconds'
  - 'Cost: 20 mana'
  - 'Cost Per Second: 35 | 40 | 45 | 50 | 55 mana'
  - 'Carrying Ally Bonus Cost: 5% mana'
  description: Ride your Chariot across the sky, choosing when to land. When descending
    you deal Physical Damage every 0.15 seconds for 0.6 seconds, Knocking Back enemies
    on the last tick
aspects:
- name: Aspect of Harmony
  kit_changes: Audacity now grants free So Beautiful casts but no Attack Speed. So
    Beautiful scales with item Health, lowers enemy Attack Speed, and grants nearby
    allies Attack Speed on god or jungle boss hits, but deals less Base Damage. Serenade
    now shields nearby allies and Protections while it holds. Buffing an ally grants
    an Audacity stack.
source_url: https://wiki.smite2.com/w/Apollo
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Apollo Basic Attack
- Audacity
- So Beautiful
- Serenade
- The Moves
- Across the Sky
<!-- WIKI:END -->
