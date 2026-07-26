---
type: smite-god
name: Rama
pantheon: Hindu
role: Carry
specializations:
- Sharpshooter
- Sniper
- Global
damage_type: physical
release_date: February 10, 2025
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
    base: 1.0
    per_level: 1.61
  move_speed:
    base: 370.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Rama Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Fire a projectile that deals Physical Damage to the first enemy hit
- slot: Passive
  name: Astral Quiver
  details:
  - The first time your Attack hits, reduce the time to generate an Astral Arrow by
    3 seconds
  - The first time a fired Astral Arrow hits an enemy, it has a chance to drop to
    the ground
  - Dropped Astral Arrows last for 10 seconds, and picking one up restores Mana
  - You can hold up to 5 Astral Arrows
  - You always respawn with a full Astral Quiver
  - 'Mana Restore: 10'
  - 'Drop Chance: 30% + 1% Per Level'
  description: You always respawn with a full Your generates an Astral Arrow every
    12 seconds
- slot: 1st Ability
  name: Astral Strike
  cost:
  - 15.0
  - 1.0
  details:
  - While this ability is active, each Attack consumes 1 Astral Arrow and Mana
  - This ability's bonus damage is reduced by 20% to each target hit after the first
  - You cannot toggle this ability if you have no Astral Arrows
  - This ability passes through and damages all enemies, and passes through walls
  - 'Bonus Damage: 10 | 20 | 30 | 40 | 50'
  - 'Bonus Damage Scaling: 20% Strength'
  - 'Slow: 10%'
  - 'Max Slow Stacks: 3'
  - 'Slow Duration: 1.5 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  - 'Cost: 15 mana + 1 Astral Arrow Per Shot'
  description: Switch to a more powerful arrow that deals bonus Physical Damage ,
    pierces, and Slows enemies
- slot: 2nd Ability
  name: Infinite Arrows
  cooldown:
  - 15.0
  - 14.0
  - 13.0
  - 12.0
  - 11.0
  cost:
  - 40.0
  - 45.0
  - 50.0
  - 55.0
  - 60.0
  details:
  - While activating this ability, if there are any dropped Astral Arrows within 8.8
    meters of you, automatically collect them
  - While this buff is active, every third successful Attack on an enemy god will
    immediately generate an Astral Arrow
  - 'Attack Speed: 40 | 45 | 50 | 55 | 60%'
  - 'Buff Duration: 6 seconds'
  - 'Cooldown: 15 | 14 | 13 | 12 | 11 seconds'
  - 'Cost: 40 | 45 | 50 | 55 | 60 mana'
  description: Focus your mind and gain increased Attack Speed
- slot: 3rd Ability
  name: Rolling Assault
  cooldown:
  - 11.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - For the next 5 seconds after Rolling, your next Attack will have Haste and consume
    an Astral Arrow, Crippling all enemies hit and dealing bonus Physical Damage
  - 'Bonus Damage: 50 | 70 | 90 | 110 | 130'
  - 'Bonus Damage Scaling: 55% Strength'
  - 'Cripple Duration: 1 | 1.25 | 1.5 | 1.75 | 2 seconds'
  - 'Range: 7.2 meters'
  - 'Radius: 0.48 meters'
  - 'Cooldown: 11 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: For the next 5 seconds after Rolling , your next Attack will have Haste
    and consume an Astral Arrow, Crippling all enemies hit and dealing bonus Physical
    Damage Roll in the direction you are currently traveling
- slot: Ultimate
  name: Astral Barrage
  cooldown:
  - 90.0
  cost:
  - 80.0
  details:
  - Each time you pick up an Astral Arrow, the cooldown of this ability is reduced
    by 0.4 seconds
  - 'Damage: 250 | 330 | 410 | 490 | 570'
  - 'Damage Scaling: 75% Strength'
  - 'Damage Per Shot: 70 | 85 | 100%'
  - 'Range: 32 meters'
  - 'Radius: 2.4 | 1.6 | 1.2 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 80 mana'
  description: Launch yourself into the air for up to 5 seconds and shoot 3 powerful
    arrows at the ground, with each successive shot dealing increasing Physical Damage
    while decreasing in size
aspects:
- name: Aspect of Precision
  kit_changes: Astral Strike is always active, but Rama has severely decreased Attack
    Speed and no longer regen Astral Arrows. When out of Astral Arrows, reload. While
    Infinite Arrows is active, Astral Arrows are not consumed.
source_url: https://wiki.smite2.com/w/Rama
last_verified: '2026-07-25'
---
<!-- WIKI:START -->
- Rama Basic Attack
- Astral Quiver
- Astral Strike
- Infinite Arrows
- Rolling Assault
- Astral Barrage
<!-- WIKI:END -->
