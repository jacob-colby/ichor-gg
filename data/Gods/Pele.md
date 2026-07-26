---
type: smite-god
name: Pele
pantheon: Polynesian
role: Jungle
specializations:
- Slayer
- Mobile
- Burst Damage
damage_type: physical
release_date: December 10, 2024
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
  name: Pele Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Physical Damage to an enemy in front of you
- slot: Passive
  name: Everlasting Flame
  cooldown:
  - 30.0
  details:
  - 'Strength: 10'
  - 'Strength Scaling: 2 Per Level'
  - 'Lifesteal: 15%'
  - 'Buff Duration: 6 seconds'
  - 'Cooldown: 30 seconds'
  description: LOW HEALTH = +STRENGTH AND +LIFESTEAL When you drop below 50% health,
    gain increased Strength and Lifesteal . This effect has a cooldown
- slot: 1st Ability
  name: Pyroclast
  cooldown:
  - 13.0
  cost:
  - 40.0
  - 45.0
  - 50.0
  - 55.0
  - 60.0
  details:
  - The number of shards returning is dependent on the rank of this ability
  - Pele has 2 charges of this ability
  - This ability passes through and damages all enemies, and passes through walls
  - 'Initial Damage: 70 | 110 | 150 | 190 | 230'
  - 'Initial Damage Scaling: 65% Strength'
  - 'Return Damage: 25'
  - 'Return Damage Scaling: 15% Strength'
  - 'Return Projectiles: 1 | 2 | 3 | 4 | 5'
  - 'Fuel Regained: 10'
  - 'Range: 9.6 meters'
  - 'Cooldown: 13 seconds'
  - 'Cost: 40 | 45 | 50 | 55 | 60 mana'
  description: Fires a Magma projectile that deals Physical Damage and grants fuel
    per enemy god hit. At max range the Magma persists and fires additional shard
    projectiles back to you, dealing Physical Damage to enemies
- slot: 2nd Ability
  name: Eruption
  cooldown:
  - 14.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - At ranks 3 and 5 this area gains additional explosion areas, which deal reduced
    Physical Damage and have a smaller Knock up
  - Activating this ability while in the amplified state of Magma Rush will cause
    you to dash a short distance before erupting
  - 'Inner Ring Damage: 85 | 130 | 175 | 220 | 265'
  - 'Inner Ring Damage Scaling: 65% Strength'
  - 'Outer Rings Damage: 0 | 0 | 140 | 180 | 220'
  - 'Outer Rings Damage Scaling: 45% Strength'
  - 'Eruption Areas: 1 | 1 | 2 | 2 | 3'
  - 'Inner Ring Radius: 2.4 meters'
  - 'Middle Ring Radius: 4 meters'
  - 'Outer Ring Radius: 5.6 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: 'Gain a burst of speed before dealing Physical Damage and Knocking
    Up enemies around you Areas: 1 | 1 | 2 | 2 | 3'
- slot: 3rd Ability
  name: Magma Rush
  details:
  - Reactive this ability to amplify the effect, expending more fuel but dealing increased
    Physical Damage and gaining additional movement speed
  - Fuel Regens 5 per second when this ability is deactivated
  - This ability cannot be activated when under 10 Fuel
  - This ability triggers no items
  - 'Damage: 15 | 20 | 25 | 30 | 35'
  - 'Damage Scaling: 5% Strength'
  - 'Amped Damage: 30 | 45 | 60 | 75 | 90'
  - 'Amped Damage Scaling: 15% Strength'
  - 'Movement Speed: 30%'
  - 'Amped Movement Speed: 60%'
  - 'Radius: 1.6 meters'
  - 'Fuel Cost: 5 per 0.5 seconds'
  - 'Amped Fuel Cost: 10 per 0.5 seconds'
  description: Repeatedly deal Physical Damage to nearby enemies and gain Movement
    Speed while this ability is active. uses Fuel for its duration and has no cooldown
- slot: Ultimate
  name: Volcanic Lightning
  cooldown:
  - 90.0
  cost:
  - 100.0
  details:
  - For the next 10 seconds or 4 Attacks, every time you Attack an enemy, you deal
    reduced Damage and also fire a cone attack
  - This ability triggers only one item across all 5 possible hits
  - The Dash passes through and damages non-god enemies, but stops on walls and enemy
    gods, while the cone attacks pass through and damage all enemies, and pass through
    walls
  - 'Damage: 180 | 255 | 330 | 405 | 480'
  - 'Damage Scaling: 60% Strength'
  - 'Cone Damage: 100 | 140 | 180 | 220 | 260'
  - 'Cone Damage Scaling: 40% Strength'
  - 'Slow: 30 | 32.5 | 35 | 37.5 | 40%'
  - 'Slow Duration: 3 seconds'
  - 'Basic Attack Damage Reduction: 50%'
  - 'Dash Range: 9.6 meters'
  - 'Radius: 5.6 meters'
  - 'Cone Angle: 110 degrees'
  - 'Cooldown: 90 seconds'
  - 'Cost: 100 mana'
  description: Become CC Immune then Dash forward dealing Physical Damage and Slowing
    the first enemy god hit, and firing a cone attack that deals Physical Damage to
    other enemies
aspects:
- name: Aspect of Obsidian
  kit_changes: You only gain Fuel from Pyroclast and when damaged by enemies instead
    of over time. Magma Rush can no longer be refired but now provides Healing. Additionally
    Everlasting Flame now provides Protections instead of Strength and Lifesteal,
    and Volcanic Lightning damage no longer has Strength Scaling.
source_url: https://wiki.smite2.com/w/Pele
last_verified: '2026-07-25'
---
<!-- WIKI:START -->
- Pele Basic Attack
- Everlasting Flame
- Pyroclast
- Eruption
- Magma Rush
- Volcanic Lightning
<!-- WIKI:END -->
