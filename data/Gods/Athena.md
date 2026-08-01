---
type: smite-god
name: Athena
pantheon: Greek
role: Support
specializations:
- Tank
- Lockdown
- Global
damage_type: magical
release_date: May 2, 2024
base_stats:
  health:
    base: 668.52
    per_level: 101.52
  mana:
    base: 296.0
    per_level: 42.0
  physical_prot:
    base: 20.73
    per_level: 3.45
  magical_prot:
    base: 29.7
    per_level: 1.62
  attack_speed:
    base: 0.98
    per_level: 1.51
  move_speed:
    base: 370.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Athena Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 3 hit chain. Attacks in order of 1, 1, 2x damage and swing time. The final
    hit cleaves
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Magical Damage to an enemy in front of you
- slot: Passive
  name: Reach
  details:
  - Deals 1.25x damage to the first target hit
  - This Attack can Critically Strike
  - This Attack can trigger Item Effects
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage Scaling: 70% Intelligence + 125% Strength'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: After using an ability, your next Attack becomes a ranged projectile
    that deals Bonus Magical Damage
- slot: 1st Ability
  name: Preemptive Strike
  cooldown:
  - 14.0
  cost:
  - 40.0
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  details:
  - Deals Magical Damage and Slows enemies
  - Gain Protections when you hit an enemy god
  - Buildup takes 0.66 seconds
  - This ability passes through and damages non-god enemies, but stops on walls and
    enemy gods
  - 'Damage: 80 | 130 | 180 | 230 | 280'
  - 'Damage Scaling: 55% Strength'
  - 'Slow: 20 | 22.5 | 25 | 27.5 | 30%'
  - 'Slow Duration: 2 seconds'
  - 'Protections: 15 | 20 | 25 | 30 | 35 + 10%'
  - 'Buff Duration: 4 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 0.96 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 40 | 50 | 60 | 70 | 80 mana'
  description: Charge up, then Dash forward
- slot: 2nd Ability
  name: Confound
  cooldown:
  - 16.0
  - 15.5
  - 15.0
  - 14.5
  - 14.0
  cost:
  - 60.0
  - 65.0
  - 79.0
  - 75.0
  - 80.0
  details:
  - Deals Magical Damage
  - Taunted enemies are Slowed by 25%
  - 'Damage: 40 | 65 | 90 | 115 | 140'
  - 'Damage Scaling: 20% Intelligence'
  - 'Taunt Duration: 0.75 | 0.9 | 1.05 | 1.2 | 1.35 seconds'
  - 'Taunt Duration Scaling: 0.2 seconds per 115 Item Protections, stacking up to
    2 times'
  - 'Range: 5.6 meters'
  - 'Cone Angle: 90 degrees'
  - 'Cooldown: 16 | 15.5 | 15 | 14.5 | 14 seconds'
  - 'Cost: 60 | 65 | 79 | 75 | 80 mana'
  description: Taunt enemies in front of you
- slot: 3rd Ability
  name: Shield Wall
  cooldown:
  - 12.0
  cost:
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  - 90.0
  details:
  - Deals Magical Damage initially
  - After a brief delay, deals additional Magical Damage
  - Applies a Slow on each hit
  - The delay between the first and second attack is 2 seconds
  - The total amount of damage if all hits connect is 540 + 100% Intelligence
  - 'Initial Damage: 60 | 100 | 140 | 180 | 220'
  - 'Initial Damage Scaling: 45% Intelligence'
  - 'Final Damage: 80 | 140 | 200 | 260 | 320'
  - 'Final Damage Scaling: 55% Intelligence'
  - 'Slow Duration: 2 seconds'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 12 seconds'
  - 'Cost: 50 | 60 | 70 | 80 | 90 mana'
  description: Create a Phalanx of Soldiers that strike twice in an area
- slot: Ultimate
  name: Defender of Olympus
  cooldown:
  - 120.0
  - 115.0
  - 110.0
  - 105.0
  - 100.0
  cost:
  - 80.0
  - 90.0
  - 100.0
  - 110.0
  - 120.0
  details:
  - Apply a Health Shield and Movement Speed to your ally
  - Deal Magical Damage to nearby enemies upon landing
  - You are CC Immune while Channeling this ability
  - Channel lasts for 3.34 seconds
  - If your target dies before your Channel completes you will still go to their location
  - 'Damage: 340 | 415 | 490 | 565 | 640'
  - 'Damage Scaling: 90% Intelligence'
  - 'Shield Health: 200 | 225 | 250 | 275 | 300'
  - 'Shield Health Scaling: 15% Max Health'
  - 'Movement Speed: 10 | 12.5 | 15 | 17.5 | 20%'
  - 'Cooldown: 120 | 115 | 110 | 105 | 100 seconds'
  - 'Cost: 80 | 90 | 100 | 110 | 120 mana'
  description: Teleport to the aid of the targeted god, anywhere on the map
aspects:
- name: Aspect of War
  kit_changes: Defender of Olympus now targets visible enemy gods instead of allies,
    dealing no landing damage but causing the enemy to take increased damage while
    Athena is channeling.
source_url: https://wiki.smite2.com/w/Athena
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Athena Basic Attack
- Reach
- Preemptive Strike
- Confound
- Shield Wall
- Defender of Olympus
<!-- WIKI:END -->
