---
type: smite-god
name: Ratatoskr
pantheon: Norse
role: Jungle
specializations:
- Slayer
- Mobile
- Global
damage_type: physical
release_date: April 7, 2026
base_stats:
  health:
    base: 661.0
    per_level: 94.0
  mana:
    base: 279.04
    per_level: 45.36
  physical_prot:
    base: 19.0
    per_level: 3.0
  magical_prot:
    base: 27.5
    per_level: 1.5
  attack_speed:
    base: 0.98
    per_level: 1.4
  move_speed:
    base: 380.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Ratatoskr Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 4 hit chain. Attacks in order of 1, 0.5, 0.5, 1.25x damage and swing time.
    The final hit cleaves
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Physical Damage to an enemy in front of you
- slot: Passive
  name: Acorn of Yggdrasil
  details:
  - After purchasing an Acorn, you cannot perform other actions and are Rooted for
    0.7 seconds
  description: You spawn with a Magic Acorn in your inventory. This can be upgraded
    anywhere on the map to provide different bonuses
- slot: 1st Ability
  name: Dart
  cooldown:
  - 14.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - This ability's Cooldown is reduced when dealing damage to enemy gods with other
    abilities. Once per ability, per god
  - This ability can Critically Strike
  - This ability can be modified by purchasing the Briskberry Acorn
  - 'Damage: 70 | 105 | 140 | 175 | 210'
  - 'Damage Scaling: 70% Strength'
  - 'Slow: 15 | 17.5 | 20 | 22.5 | 25%'
  - 'Slow Duration: 2 seconds'
  - 'Cooldown Reduction: -1 second'
  - 'Range: 8.8 meters'
  - 'Briskberry Dash Range: 6 meters'
  - 'Radius: 0.8 meters'
  - 'Briskberry Dash Radius: 1.2 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Dash forward, dealing Physical Damage and Slowing enemies hit, stopping
    on enemy gods
- slot: 2nd Ability
  name: Flurry
  cooldown:
  - 14.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - This ability can be modified by purchasing the Ashwhorl Acorn
  - 'Damage: 25 | 40 | 55 | 70 | 85'
  - 'Damage Scaling: 25% Strength'
  - 'Ashwhorl Damage: 20 | 25 | 30 | 35 | 40'
  - 'Ashwhorl Damage Scaling: 20% Strength'
  - 'Physical Protections Reduced: 2 | 3 | 4 | 5 | 6'
  - 'Debuff Duration: 3 seconds'
  - 'Ashwhorl Attack Speed: 6 | 7 | 8 | 9 | 10%'
  - 'Ashwhorl Buff Duration: 5 seconds'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Spin 4 times and deal Physical Damage to enemies around you, reducing
    their Physical Protections
- slot: 3rd Ability
  name: Acorn Blast
  cooldown:
  - 12.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Enemies hit by multiple acorns take 40% less damage on each acorn, down to a minimum
    of 20% damage
  - This ability can be modified by purchasing the Thistlethorn Acorn
  - This ability passes through and damages all enemies, but stops on walls
  - 'Damage: 70 | 90 | 110 | 130 | 150'
  - 'Damage Scaling: 55% Strength'
  - 'Thistlethorn Damage: 40 | 55 | 70 | 85 | 100'
  - 'Thistlethorn Damage Scaling: 40% Strength'
  - 'Thistlethorn Explosion Damage: 30 | 40 | 50 | 60 | 70'
  - 'Thistlethorn Explosion Damage Scaling: 25% Strength'
  - 'Stun Duration: 1 second'
  - 'Range: 8.8 meters'
  - 'Cone Angle: 20 degrees'
  - 'Cooldown: 12 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Fire a blast of 3 Acorns that deal Physical Damage . Enemies hit by
    3 Acorns are Stunned
- slot: Ultimate
  name: Through the Cosmos
  cooldown:
  - 110.0
  - 105.0
  - 100.0
  - 95.0
  - 90.0
  cost:
  - 100.0
  details:
  - You are CC Immune during this ability
  - 'Damage: 200 | 260 | 320 | 380 | 440'
  - 'Damage Scaling: 90% Strength'
  - 'Range: 14.4 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 110 | 105 | 100 | 95 | 90 seconds'
  - 'Cost: 100 mana'
  description: Fly into the sky. Choose and leap to a location, up to twice, before
    landing at a final location dealing Physical Damage and Knocking Up enemies
aspects:
- name: Aspect of the Thickbark
  kit_changes: Your tier 3 Acorn effects change. Briskberry causes Dart to knockback
    enemy gods, marking them to explode. Ashwhorl provides Flurry 2 charges, protections
    and healing. Thistlethorn causes Acorn Blast to fire 5 projectiles and debuffs
    enemies.
source_url: https://wiki.smite2.com/w/Ratatoskr
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Ratatoskr Basic Attack
- Acorn of Yggdrasil
- Dart
- Flurry
- Acorn Blast
- Through the Cosmos
<!-- WIKI:END -->
