---
type: smite-god
name: Achilles
pantheon: Greek
role: Solo Jungle
specializations:
- Brawler
- Execute
- Lockdown
damage_type: physical
release_date: February 17, 2025
base_stats:
  health:
    base: 661.0
    per_level: 94.0
  mana:
    base: 292.64
    per_level: 38.64
  physical_prot:
    base: 20.73
    per_level: 3.45
  magical_prot:
    base: 29.58
    per_level: 1.5
  attack_speed:
    base: 0.96
    per_level: 1.4
  move_speed:
    base: 375.0
    per_level: 0.0
  attack_power:
    base: 47.57
    per_level: 2.21
  health_regen:
    base: 1.84
    per_level: 0.22
  mana_regen:
    base: 1.45
    per_level: 0.12
abilities:
- slot: Basic Attack
  name: Achilles Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 2.56 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Physical Damage to an enemy in front of you
  damage_type: physical
  detail_kinds:
  - null
  - physical
  - mechanic
  - mechanic
- slot: Passive
  name: Gift of the Gods
  details:
  - Swap between armor states by using Basic Attacks while the Passive targeter is
    active inside the Fountain
  - Your chosen armor state also adds effects to Radiant Glory and Combat Dodge
  - 'Health: 25 + 10 Per Level'
  - 'Protections: 5 + 2 Per Level'
  - 'Strength: 3 + 1.5 Per Level'
  - 'Movement Speed: 1% + 0.25% Per Level'
  description: Swap between armor states by using Basic Attacks while the targeter
    is active inside the Fountain Choose to wear armor or forgo it. Wearing armor
    grants bonus Health and Protections , while forgoing it grants bonus Strength
    and Movement Speed
  detail_kinds:
  - null
  - null
  - buff
  - buff
  - buff
  - buff
- slot: 1st Ability
  name: Shield of Achilles
  cooldown:
  - 14.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - The radiated force deals reduced Physical Damage
  - Non-god targets take increased Physical Damage
  - Increased Stun duration when armored, increased Scaling when forgoing your armor
  - 'Damage: 100 | 155 | 210 | 265 | 320'
  - 'Damage Scaling: 80% Strength'
  - 'Stun Duration: 0.8 seconds'
  - 'Bonus Stun Duration: 0.2 seconds'
  - 'Bonus Damage Scaling: 15% Strength'
  - 'Cone Angle: 80 degrees'
  - 'Small Radius: 3.2 meters'
  - 'Large Radius: 8 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Punch forward with your shield, dealing Physical Damage and Stunning
    enemies in a short cone. The force of the shield radiates further, dealing reduced
    damage
  damage_type: physical
  detail_kinds:
  - physical
  - physical
  - stun
  - physical
  - physical
  - stun
  - stun
  - buff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 2nd Ability
  name: Radiant Glory
  cooldown:
  - 9.0
  cost:
  - 40.0
  - 45.0
  - 50.0
  - 55.0
  - 60.0
  details:
  - When armored, the gods' blessings also grant you a Physical Shield
  - When forgoing your armor, hitting an enemy god with your attacks from behind reduces
    their Protections
  - You may only Heal up to 4 times per ability hit
  - 'Strength: 10%'
  - 'Protections: 20%'
  - 'Crowd Control Reduction: 20 | 22.5 | 25 | 27.5 | 30%'
  - 'Buff Duration: 6.1 seconds'
  - 'Heal: 16 | 18 | 20 | 22 | 24'
  - 'Physical Shield Health: 75 + 20 Per Level'
  - 'Protections Reduced: 1 Per Level'
  - 'Debuff Duration: 3 seconds'
  - 'Cooldown: 9 seconds'
  - 'Cost: 40 | 45 | 50 | 55 | 60 mana'
  description: You are blessed by the gods, gaining bonus Strength , Protections ,
    and Crowd Control Reduction for a short duration. Damaging enemies with abilities
    during this time Heals you
  detail_kinds:
  - null
  - debuff
  - heal
  - buff
  - buff
  - buff
  - buff
  - heal
  - null
  - debuff
  - debuff
  - mechanic
  - mechanic
- slot: 3rd Ability
  name: Combat Dodge (Spear Strike)
  cooldown:
  - 14.0
  - 13.5
  - 13.0
  - 12.5
  - 12.0
  cost:
  - 22.0
  - 24.0
  - 26.0
  - 28.0
  - 30.0
  details:
  - When armored, striking an enemy god with your spear Slows them, stacking up to
    2 times
  - When forgoing your armor, the speed of your Dodge is doubled
  - You can use Abilities and Basic Attacks between Dodges
  - After readying your spear, you have 4 seconds to strike before the ability ends
  - 'Damage: 65 | 105 | 145 | 185 | 225'
  - 'Damage Scaling: 45% Strength'
  - 'Slow: 7.5% Per Stack'
  - 'Slow Duration: 3 seconds'
  - 'Dodge Range: 3.2 meters'
  - 'Spear Strike Range: 5.6 meters'
  - 'Spear Strike Radius: 0.96 meters'
  - 'Cooldown: 14 | 13.5 | 13 | 12.5 | 12 seconds'
  - 'Cost: 22 | 24 | 26 | 28 | 30 mana'
  description: Dodge in your current direction and ready your spear to strike enemies
    for Physical Damage . Hitting an enemy god with the strike allows you to recast
    the ability once before it goes on cooldown
  damage_type: physical
  detail_kinds:
  - slow
  - null
  - null
  - null
  - physical
  - physical
  - slow
  - slow
  - null
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: Ultimate
  name: Fatal Strike
  cooldown:
  - 90.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Each kill exposes your heel, increasing your damage taken
  - The dash ends early upon hitting an enemy god
  - You are CC Immune during the preparation phase, and while Dashing
  - The preparation before the Dash lasts 1 second
  - This ability passes through and damages non-god enemies, but stops on walls and
    enemy gods
  - 'Damage: 180 | 270 | 360 | 450 | 540'
  - 'Damage Scaling: 100% Strength'
  - 'Execute Health %: 35%'
  - 'Increased Damage Taken: 5%'
  - 'Debuff Duration: 10 seconds'
  - 'Dash Range: 5.6 meters'
  - 'Dash Radius: 0.96 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Prepare briefly, then Dash foward, dealing Physical Damage to enemies
    and Executing gods that are low health. Killing a god allows you to recast this
    ability up to 5 times
  damage_type: physical
  detail_kinds:
  - debuff
  - null
  - mechanic
  - null
  - null
  - physical
  - physical
  - physical
  - debuff
  - debuff
  - null
  - null
  - mechanic
  - mechanic
aspects:
- name: Aspect of Prowess
  kit_changes: Combat Dodge can now be recast after striking a Jungle Monster or Boss,
    with Spear Strike gaining increased Scaling when forgoing Achilles's Armor. Radiant
    Glory no longer grants increased Protections or Crowd Control Reduction.
source_url: https://wiki.smite2.com/w/Achilles
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Achilles Basic Attack
- Gift of the Gods
- Shield of Achilles
- Radiant Glory
- Combat Dodge (Spear Strike)
- Fatal Strike
<!-- WIKI:END -->
