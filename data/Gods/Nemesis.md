---
type: smite-god
name: Nemesis
pantheon: Greek
role: Jungle
specializations:
- Mobile
- Shielding
- Constant Damage
damage_type: physical
release_date: November 12, 2024
base_stats:
  health:
    base: 619.0
    per_level: 94.0
  mana:
    base: 296.0
    per_level: 42.0
  physical_prot:
    base: 19.0
    per_level: 3.0
  magical_prot:
    base: 27.5
    per_level: 1.5
  attack_speed:
    base: 1.0
    per_level: 1.51
  move_speed:
    base: 380.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Nemesis Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 4 hit chain. Attacks in order of 1, 1, 0.75, 1.25x damage and swing time
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Physical Damage to an enemy in front of you
- slot: Passive
  name: Scales of Fate
  details:
  - 'Reduction: 7% Per Stack'
  - 'Increase: 7% Per Stack'
  - 'Max Stacks: 3'
  - 'Duration: 5 seconds'
  description: ATTACKS STEAL POWER Hitting enemies with Attacks reduces the target's
    Inhand Power, Strength, and Intelligence while increasing yours
- slot: 1st Ability
  name: Swift Vengeance
  cooldown:
  - 11.0
  cost:
  - 50.0
  details:
  - Deals Physical Damage to all enemies hit
  - May Dash again within 2 seconds
  - May use Attacks and Abilities between Dashes
  - 'Damage: 60 | 90 | 120 | 150 | 180'
  - 'Damage Scaling: 45% Strength'
  - 'Range: 4.8 meters'
  - 'Radius: 1.6 meters'
  - 'Cooldown: 11 seconds'
  - 'Cost: 50 mana'
  description: Dash in a line, passing through all enemies
- slot: 2nd Ability
  name: Slice and Dice
  cooldown:
  - 10.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Enemies in the center of the slash take additional damage and are Slowed
  - 'Damage: 70 | 100 | 130 | 160 | 190'
  - 'Damage Scaling: 40% Strength + 25% Intelligence'
  - 'Center Damage: 85 | 145 | 205 | 265 | 325'
  - 'Center Damage Scaling: 90% Strength + 75% Intelligence'
  - 'Slow: 30%'
  - 'Slow Duration: 2 seconds'
  - 'Range: 5.6 meters'
  - 'Cone Angle: 150 degrees'
  - 'Center Cone Angle: 45 degrees'
  - 'Cooldown: 10 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Slash in a cone, dealing Physical Damage to all enemies hit
- slot: 3rd Ability
  name: Retribution
  cooldown:
  - 14.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Reflect a percentage of the damage taken from gods as Physical Damage
  - Heal for a percentage of the damage taken during the effect
  - Hard CC effects remove the Shield
  - 'Shield Health: 100 | 150 | 200 | 250 | 300'
  - 'Shield Health Scaling: 7.5% Max Health'
  - 'Shield Duration: 2 seconds'
  - 'Reflect Damage: 40% of Damage Blocked'
  - 'Reflect Damage Scaling: 20% Strength'
  - 'Heal: 40% of Damage Blocked'
  - 'Heal Scaling: 5% Intelligence'
  - 'Cooldown: 14 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Gain a Health Shield for a duration
- slot: Ultimate
  name: Divine Judgement
  cooldown:
  - 90.0
  cost:
  - 90.0
  - 95.0
  - 100.0
  - 105.0
  - 110.0
  details:
  - Gain Movement Speed and a percentage of the enemy's protections
  - Reduce enemy's Movement Speed and Protections by the same amount
  - Gain Protections equal to the enemy with the most Protections
  - On hitting an enemy, a homing projectile spawns from them, granting the buffs
    when it reaches you
  - 'Damage: 15 | 17.5 | 20 | 22.5 | 25% of Enemy''s Current Health'
  - 'Damage Scaling: 45% Strength + 65% Intelligence'
  - 'Movement Speed: 10 | 12.5 | 15 | 17.5 | 20%'
  - 'Protections: 25%'
  - 'Duration: 5 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 1.6 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 90 | 95 | 100 | 105 | 110 mana'
  description: Choose a single enemy god, dealing Physical Damage to them and all
    enemies in an area around them
aspects:
- name: Aspect of Justice
  kit_changes: Divine Judgement no longer does damage in an area but instead averages
    Nemesis's and the enemy god's current Health as long as Nemesis has less than
    the target.
source_url: https://wiki.smite2.com/w/Nemesis
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Nemesis Basic Attack
- Scales of Fate
- Swift Vengeance
- Slice and Dice
- Retribution
- Divine Judgement
<!-- WIKI:END -->
