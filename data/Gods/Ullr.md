---
type: smite-god
name: Ullr
pantheon: Norse
role: Carry
specializations:
- Lockdown
- Burst Damage
- Pressure
damage_type: physical
release_date: January 7, 2025
base_stats:
  health:
    base: 619.0
    per_level: 94.0
  health_regen:
    base: 1.85
    per_level: 0.23
  mana:
    base: 312.96
    per_level: 38.64
  mana_regen:
    base: 1.55
    per_level: 0.11
  physical_prot:
    base: 20.04
    per_level: 2.76
  magical_prot:
    base: 25.3
    per_level: 1.38
  attack_speed:
    base: 0.98
    per_level: 1.4
  attack_power:
    base: 44.4
    per_level: 2.4
  move_speed:
    base: 375.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Ullr Basic Attack
  details:
  - 'Bow: Fire a projectile that deals Physical Damage to the first enemy hit'
  - 'Bow: Projectile stops on first target hit, and does not pass through walls'
  - 'Axe: Deal Physical Damage to an enemy in front of you'
  - 'Axe: If multiple enemies are in the area, the enemy closest to the center of
    the area will be hit'
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Bow Range: 8.8 meters'
  - 'Bow Radius: 0.48 meters'
  - 'Axe Range: 1.92 meters'
  - 'Axe Cone Angle: 120 degrees'
  detail_kinds:
  - physical
  - null
  - physical
  - null
  - physical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: physical
  description: Ullr's Attacks change depending on his current stance
- slot: Passive
  name: Weapon Master
  details:
  - 'Cooldown Reduction: 1 second'
  detail_kinds:
  - buff
  description: ABILITIES REDUCE OTHER COOLDOWNS When you use an ability in either
    stance your Cooldowns in the opposite stance are reduced
- slot: 1st Ability
  name: Bladed Arrow
  cooldown:
  - 14.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - This ability passes through and damages all enemies, and does not pass through
    walls
  - 'Damage: 70 | 120 | 170 | 220 | 270'
  - 'Damage Scaling: 75% Strength'
  - 'Range: 11.2 meters'
  - 'Radius: 0.48 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  detail_kinds:
  - null
  - physical
  - physical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: physical
  description: Fire an arrow that passes through enemies and deals Physical Damage
    to all targets hit
  stance: Bow
- slot: 2nd Ability
  name: Expose Weakness
  cooldown:
  - 14.0
  cost:
  - 50.0
  details:
  - The buff persists after switching stances
  - 'Attack Speed: 20 | 25 | 30 | 35 | 40%'
  - 'Buff Duration: 4 seconds'
  - 'Cooldown: 14 seconds'
  - 'Cost: 50 mana'
  detail_kinds:
  - null
  - buff
  - buff
  - mechanic
  - mechanic
  description: Gain Attack Speed
  stance: Bow
- slot: 3rd Ability
  name: Hail of Arrows
  cooldown:
  - 15.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - The arrow remains in the ground for 3 seconds
  - If you activate Wield Axes while the arrow is deployed, the area around it becomes
    snowy for 3 seconds, Slowing enemies
  - 'Damage: 80 | 120 | 160 | 200 | 240'
  - 'Damage Scaling: 85% Strength'
  - 'Slow: 30%'
  - 'Range: 12.8 meters'
  - 'Radius: 1.6 meters'
  - 'Snow Field Radius: 2.4 meters'
  - 'Cooldown: 15 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  detail_kinds:
  - null
  - slow
  - physical
  - physical
  - slow
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: physical
  description: Fire a volley, dealing Physical Damage
  stance: Bow
- slot: Ultimate
  name: Wield Axes
  cooldown:
  - 1.0
  details:
  - While you are in Bow stance, your Attacks are ranged and you gain additional Strength
  - You also gain half of the benefit of the opposing stance
  - 'Bow Strength: 15 | 20 | 25 | 30 | 35'
  - 'Axe Lifesteal: 2.5 | 4 | 5.5 | 7 | 8.5%'
  - 'Cooldown: 1 second'
  detail_kinds:
  - buff
  - null
  - buff
  - buff
  - mechanic
  description: Change stance, Cleanse Disarms , and gain benefits depending on which
    stance you are in
  stance: Bow
- slot: 1st Ability
  name: Thrown Axe
  cooldown:
  - 14.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - This ability stops on first target hit, and does not pass through walls
  - 'Damage: 50 | 80 | 110 | 140 | 170'
  - 'Damage Scaling: 75% Strength'
  - 'Stun Duration: 0.8 | 0.9 | 1 | 1.1 | 1.2 seconds'
  - 'Range: 11.2 meters'
  - 'Radius: 0.48 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  detail_kinds:
  - null
  - physical
  - physical
  - stun
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: physical
  description: Throw an axe that Stuns and deals Physical Damage to the first enemy
    it hits
  stance: Axe
- slot: 2nd Ability
  name: Invigorate
  cooldown:
  - 14.0
  cost:
  - 50.0
  details:
  - The buff persists after switching stances
  - 'Movement Speed: 8 | 10 | 12 | 14 | 16%'
  - 'Buff Duration: 4 seconds'
  - 'Cooldown: 14 seconds'
  - 'Cost: 50 mana'
  detail_kinds:
  - null
  - buff
  - buff
  - mechanic
  - mechanic
  description: Gain Movement Speed
  stance: Axe
- slot: 3rd Ability
  name: Glory Bound
  cooldown:
  - 14.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - The axes remain in the ground for 3 seconds
  - If you activate Wield Bow while the axes are deployed, the axes tear open the
    ground, reducing Physical Protections of enemies hit
  - 'Damage: 50 | 80 | 110 | 140 | 170'
  - 'Damage Scaling: 65% Strength'
  - 'Physical Protections Reduced: 4 | 8 | 12 | 16 | 20'
  - 'Debuff Duration: 4 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 2.4 meters'
  - 'Tear Radius: 2.4 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  detail_kinds:
  - null
  - debuff
  - physical
  - physical
  - debuff
  - debuff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: physical
  description: Leap to deal Physical Damage Tear
  stance: Axe
- slot: Ultimate
  name: Wield Bow
  cooldown:
  - 1.0
  details:
  - While you are in Axe stance, your Attacks are Melee ranged and you gain additional
    Lifesteal
  - You also gain half of the benefit of the opposing stance
  - 'Bow Strength: 15 | 20 | 25 | 30 | 35'
  - 'Axe Lifesteal: 2.5 | 4 | 5.5 | 7 | 8.5%'
  - 'Cooldown: 1 second'
  detail_kinds:
  - buff
  - null
  - buff
  - buff
  - mechanic
  description: Change stance, Cleanse Disarms , and gain benefits depending on which
    stance you are in
  stance: Axe
aspects: []
source_url: https://wiki.smite2.com/w/Ullr
last_verified: '2026-08-09'
---
<!-- WIKI:START -->
- Ullr Basic Attack
- Weapon Master
- Bladed Arrow
- Expose Weakness
- Hail of Arrows
- Wield Axes
- Thrown Axe
- Invigorate
- Glory Bound
- Wield Bow
<!-- WIKI:END -->
