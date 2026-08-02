---
type: smite-god
name: Cernunnos
pantheon: Celtic
role: Carry Jungle
specializations:
- Nuker
- Sharpshooter
- Lockdown
damage_type: physical
release_date: May 2, 2024
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
    per_level: 1.4
  move_speed:
    base: 375.0
    per_level: 0.0
  attack_power:
    base: 48.12
    per_level: 2.76
  health_regen:
    base: 1.7
    per_level: 0.2
  mana_regen:
    base: 1.33
    per_level: 0.11
abilities:
- slot: Basic Attack
  name: Cernunnos Basic Attack
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
  name: Heavy Glaive
  details:
  - 'Damage Scaling: 30% Strength + 5% Intelligence'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: MELEE ATTACKS CLEAVE Basic Attacks deal bonus Physical Damage to enemies
    in melee range
  damage_type: physical
  detail_kinds:
  - physical
  - mechanic
  - mechanic
- slot: 1st Ability
  name: Shifter Of Seasons
  details:
  - 'Spring: Self Healing'
  - 'Summer: Bonus Damage'
  - 'Fall: Protection Reduction'
  - 'Winter: Slow'
  - This effect is always active once ranked
  - Summer Season Basic Attacks deal Physical Damage if you have more Strength, or
    Magical Damage if you have more Intelligence
  - 'Spring Lifesteal: 3 | 3.5 | 4 | 4.5 | 5%'
  - 'Spring Heal Scaling: 10% Intelligence'
  - 'Summer Damage: 5 | 10 | 15 | 20 | 25'
  - 'Summer Damage Scaling: 12 | 15 | 18 | 21 | 24% Strength or Intelligence (whichever
    is higher)'
  - 'Fall Physical Protection Reduced: 5 | 10 | 15 | 20 | 25'
  - 'Fall Magical Protection Reduced: 5 | 10 | 15 | 20 | 25'
  - 'Debuff Scaling: 5% Intelligence'
  - 'Fall Debuff Duration: 10 seconds'
  - 'Winter Slow: 10 | 11 | 12 | 13 | 14%'
  - 'Winter Slow Scaling: 2.5% Intelligence'
  - 'Winter Slow Duration: 2 seconds'
  description: Activate to toggle between Spring, Summer, Fall, or Winter Basic Attack
    bonus effects
  detail_kinds:
  - heal
  - physical
  - debuff
  - slow
  - null
  - physical
  - heal
  - heal
  - physical
  - physical
  - buff
  - buff
  - buff
  - buff
  - slow
  - slow
  - slow
- slot: 2nd Ability
  name: Bramble Blast
  cooldown:
  - 15.0
  cost:
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  - 90.0
  details:
  - This Roots and Cripples a directly hit target
  - The explosion leaves a bramble area that repeatedly deals Physical Damage
  - Bramble area hits 10 times over 5 seconds
  - This ability stops and explodes on first enemy hit, on walls, or at max range
  - 'Initial Damage: 65 | 110 | 155 | 200 | 245'
  - 'Initial Damage Scaling: 75% Strength + 50% Intelligence'
  - 'Damage Per Tick: 8 | 12 | 16 | 20 | 24'
  - 'Damage Scaling Per Tick: 6% Strength + 12% Intelligence'
  - 'Root Duration: 1 second'
  - 'Range: 8.8 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 15 seconds'
  - 'Cost: 50 | 60 | 70 | 80 | 90 mana'
  description: Fire a bramble that explodes on hit or upon reaching max range, dealing
    Physical Damage in an area
  damage_type: physical
  detail_kinds:
  - debuff
  - physical
  - null
  - null
  - physical
  - physical
  - physical
  - physical
  - debuff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 3rd Ability
  name: Horn Charge
  cooldown:
  - 15.0
  - 14.5
  - 14.0
  - 13.5
  - 13.0
  cost:
  - 70.0
  - 75.0
  - 80.0
  - 85.0
  - 90.0
  details:
  - Deals Physical Damage to all enemies hit
  - Dash passes through all enemies
  - You can cancel this ability at any time
  - 'Damage: 90 | 140 | 190 | 240 | 290'
  - 'Damage Scaling: 85% Strength'
  - 'Range: 8.8 meters'
  - 'Radius: 1.6 meters'
  - 'Cooldown: 15 | 14.5 | 14 | 13.5 | 13 seconds'
  - 'Cost: 70 | 75 | 80 | 85 | 90 mana'
  description: Dash forward, passing through all types of enemies
  damage_type: physical
  detail_kinds:
  - physical
  - null
  - null
  - physical
  - physical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: Ultimate
  name: The Wild Hunt
  cooldown:
  - 90.0
  cost:
  - 100.0
  details:
  - Deals Physical Damage to all enemies in the area
  - Applies Shifter of Season effects
  - Polymorphed Enemies are Silenced, Disarmed, Slowed, and transformed to look like
    harmless animals
  - 'Damage: 240 | 320 | 400 | 480 | 540'
  - 'Damage Scaling: 80% Strength + 100% Intelligence'
  - 'Polymorph Duration: 1.5 seconds'
  - 'Slow: 20%'
  - 'Slow Duration: 1.5 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 4 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 100 mana'
  description: Polymorphed Enemies are Silenced , Disarmed , Slowed , and transformed
    to look like harmless animals Polymorph enemy gods into wild boars and start
  damage_type: physical
  detail_kinds:
  - physical
  - null
  - debuff
  - physical
  - physical
  - debuff
  - slow
  - slow
  - mechanic
  - mechanic
  - mechanic
  - mechanic
aspects:
- name: Aspect of Strife
  kit_changes: Your Basic Attacks are now melee and deal increased damage, cleave,
    and apply stronger Shifter of Seasons effects to all enemies hit. In addition,
    Horn Charge's cooldown is reduced when hitting a god or Jungle Monster and applies
    Shifter of Seasons.
source_url: https://wiki.smite2.com/w/Cernunnos
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Cernunnos Basic Attack
- Heavy Glaive
- Shifter Of Seasons
- Bramble Blast
- Horn Charge
- The Wild Hunt
<!-- WIKI:END -->
