---
type: smite-god
name: Awilix
pantheon: Maya
role: Jungle
specializations:
- Slayer
- Mobile
damage_type: physical
release_date: March 3, 2025
base_stats:
  health:
    base: 619.0
    per_level: 94.0
  mana:
    base: 334.1
    per_level: 42.0
  physical_prot:
    base: 18.76
    per_level: 2.76
  magical_prot:
    base: 27.5
    per_level: 1.5
  attack_speed:
    base: 1.0
    per_level: 1.4
  move_speed:
    base: 380.0
    per_level: 0.0
  attack_power:
    base: 47.76
    per_level: 2.4
  health_regen:
    base: 1.7
    per_level: 0.2
  mana_regen:
    base: 1.46
    per_level: 0.13
abilities:
- slot: Basic Attack
  name: Awilix Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 3 hit chain. Attacks in order of 1, 0.75, 1.25x damage and swing time
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 2.56 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Physical Damage to an enemy in front of you
  damage_type: physical
  detail_kinds:
  - null
  - null
  - physical
  - mechanic
  - mechanic
- slot: Passive
  name: Initiative
  details:
  - The buff is extended by 2 seconds if triggered by the Leap from Summon Suku
  - 'Attack Power: 25%'
  - 'Strength: 25%'
  - 'Buff Duration: 4 seconds'
  description: If you have not taken or dealt damage in the last 5 seconds, gain increased
    Attack Power and Strength if you strike an enemy first
  detail_kinds:
  - null
  - buff
  - buff
  - buff
- slot: 1st Ability
  name: Summon Suku
  cooldown:
  - 15.0
  cost:
  - 30.0
  - 35.0
  - 40.0
  - 45.0
  - 50.0
  details:
  - Canceling this ability before leaping will not trigger the Cooldown
  - 'Damage: 85 | 135 | 180 | 235 | 285'
  - 'Damage Scaling: 70% Strength'
  - 'Movement Speed: 30%'
  - 'Range: 8.8 meters'
  - 'Radius: 2.24 meters'
  - 'Cooldown: 15 seconds'
  - 'Cost: 30 | 35 | 40 | 45 | 50 mana'
  description: Mount your Panther Suku, gaining Movement Speed but Decreased Strafe
    Speed . You may Leap off of Suku to deal Physical Damage in the target area
  damage_type: physical
  detail_kinds:
  - null
  - physical
  - physical
  - buff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 2nd Ability
  name: Feather Step
  cooldown:
  - 9.0
  cost:
  - 30.0
  - 35.0
  - 40.0
  - 45.0
  - 50.0
  details:
  - If the next attack is your third attack, you also hit all enemies in the area
    around the target
  - You are briefly Untargetable while in the air
  - 'Damage: 50 | 85 | 120 | 155 | 190'
  - 'Damage Scaling: 45% Strength'
  - 'Root Duration: 0.6 seconds'
  - 'Cripple Duration: 0.6 seconds'
  - 'Radius: 2.56 meters'
  - 'Cooldown: 9 seconds'
  - 'Cost: 30 | 35 | 40 | 45 | 50 mana'
  description: Flip over the last enemy you hit within 1.5 seconds, Rooting , Crippling
    , and dealing Physical Damage to them. The damage dealt is increased by 1.35x
    or 1.9x based on the next attack in your Basic Attack progression
  damage_type: physical
  detail_kinds:
  - null
  - mechanic
  - physical
  - physical
  - debuff
  - debuff
  - mechanic
  - mechanic
  - mechanic
- slot: 3rd Ability
  name: Moonlight Charge
  cooldown:
  - 12.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - This ability can be used while riding Suku
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage: 90 | 140 | 190 | 240 | 290'
  - 'Damage Scaling: 70% Strength'
  - 'Range: 11.2 meters'
  - 'Radius: 0.88 meters'
  - 'Cooldown: 12 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Suku comes to Awilix's aid, rushing forward dealing Physical Damage
    to all enemies. If hit from the side or behind, enemies are also Knocked Up
  damage_type: physical
  detail_kinds:
  - null
  - null
  - physical
  - physical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: Ultimate
  name: Gravity Surge
  cooldown:
  - 90.0
  - 85.0
  - 80.0
  - 75.0
  - 70.0
  cost:
  - 100.0
  details:
  - You are then bathed in moonlight, gaining Bonus Attack Speed, Attack Damage, and
    Strength, as well as protection against Roots, Slows, and Displacement for 6 seconds
  - 'Damage: 170 | 215 | 260 | 305 | 350'
  - 'Damage Scaling: 65% Strength'
  - 'Stun Duration: 0.5 seconds'
  - 'Attack Speed: 50 | 55 | 60 | 65 | 70%'
  - 'Attack Damage: 20 | 25 | 30 | 35 | 40%'
  - 'Strength: 20 | 25 | 30 | 35 | 40'
  - 'Radius: 12 meters'
  - 'Cooldown: 90 | 85 | 80 | 75 | 70 seconds'
  - 'Cost: 100 mana'
  description: You are then bathed in moonlight, gaining Bonus Attack Speed , Attack
    Damage , and Strength , as well as protection against Roots , Slows , and Displacement
    for 6 seconds Pull the closest enemy god to you that is either Knocked Up or Leaping
    . The target god takes Physical Damage and is Stunned when they land
  damage_type: physical
  detail_kinds:
  - buff
  - physical
  - physical
  - stun
  - buff
  - buff
  - buff
  - mechanic
  - mechanic
  - mechanic
aspects: []
source_url: https://wiki.smite2.com/w/Awilix
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Awilix Basic Attack
- Initiative
- Summon Suku
- Feather Step
- Moonlight Charge
- Gravity Surge
<!-- WIKI:END -->
