---
type: smite-god
name: Ra
pantheon: Egyptian
role: Mid
specializations:
- Sniper
- Healing
- Buffs
damage_type: magical
release_date: October 29, 2024
base_stats:
  health:
    base: 569.48
    per_level: 86.48
  mana:
    base: 322.62
    per_level: 48.3
  physical_prot:
    base: 17.48
    per_level: 2.76
  magical_prot:
    base: 27.38
    per_level: 1.38
  attack_speed:
    base: 0.96
    per_level: 1.4
  move_speed:
    base: 375.0
    per_level: 0.0
  attack_power:
    base: 40.85
    per_level: 2.21
  health_regen:
    base: 1.7
    per_level: 0.2
  mana_regen:
    base: 1.56
    per_level: 0.12
abilities:
- slot: Basic Attack
  name: Ra Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Fire a projectile that deals Magical Damage to the first enemy hit
  damage_type: magical
  detail_kinds:
  - null
  - magical
  - mechanic
  - mechanic
- slot: Passive
  name: Speed of Light
  details:
  - 'Movement Speed: 5% Per Stack'
  - 'Buff Duration: 15 seconds'
  - 'Max Buff Stacks: 3'
  description: USE ABILITY, MOVE FASTER After using an ability gain Movement Speed
  detail_kinds:
  - buff
  - buff
  - buff
- slot: 1st Ability
  name: Celestial Beam
  cooldown:
  - 10.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage: 95 | 155 | 215 | 275 | 335'
  - 'Damage Scaling: 105% Intelligence'
  - 'Range: 12.8 meters'
  - 'Radius: 0.72 meters'
  - 'Cooldown: 10 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80'
  description: Summon a moving beam of intense light, dealing Magical Damage to enemies
  damage_type: magical
  detail_kinds:
  - null
  - magical
  - magical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 2nd Ability
  name: Divine Light
  cooldown:
  - 14.0
  - 13.5
  - 13.0
  - 12.5
  - 12.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - For a period after activation, Attacks fire solar rays, dealing Magical Damage
  - The solar rays count as abilities, trigger ability effects at 50% effectiveness,
    and pierce targets
  - Enemies looking at you gain additional Slow stacks and are Blinded by the explosion
  - A Slow stack is applied every 0.5 seconds
  - The explosion occurs after 2 seconds
  - The explosion passes through and damages all enemies, but stops on walls
  - The solar rays pass through and damage all enemies, and pass through walls
  - 'Damage: 85 | 135 | 185 | 235 | 285'
  - 'Damage Scaling: 70% Intelligence'
  - 'Solar Ray Damage: 10 | 20 | 30 | 40 | 50'
  - 'Solar Ray Damage Scaling: 85% Intelligence'
  - 'Solar Ray Duration: 4 seconds'
  - 'Slow: 5%'
  - 'Slow Duration: 3 seconds'
  - 'Radius: 4.8 meters'
  - 'Cooldown: 14 | 13.5 | 13 | 12.5 | 12 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: For a period after activation, Attacks fire solar rays , dealing Magical
    Damage Emanate light in the area around you that repeatedly Slows enemies before
    exploding dealing Magical Damage
  damage_type: magical
  detail_kinds:
  - buff
  - null
  - slow
  - slow
  - null
  - null
  - null
  - magical
  - magical
  - magical
  - magical
  - buff
  - slow
  - slow
  - mechanic
  - mechanic
  - mechanic
- slot: 3rd Ability
  name: Solar Blessing
  cooldown:
  - 15.0
  - 14.5
  - 14.0
  - 13.5
  - 13.0
  cost:
  - 65.0
  - 75.0
  - 85.0
  - 95.0
  - 105.0
  details:
  - The light empowers you and allied gods in the area, granting Strength, Intelligence,
    and Protections
  - The pillar of light ticks 6 times over 6 seconds
  - 'Damage Per Tick: 20 | 32 | 44 | 56 | 68'
  - 'Damage Scaling Per Tick: 35% Intelligence'
  - 'Heal Per Tick: 16 | 22 | 28 | 34 | 40'
  - 'Strength: 10 | 15 | 20 | 25 | 30'
  - 'Intelligence: 20 | 25 | 30 | 35 | 40'
  - 'Protections: 15 | 20 | 25 | 30 | 35'
  - 'Range: 8.8 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 15 | 14.5 | 14 | 13.5 | 13 seconds'
  - 'Cost: 65 | 75 | 85 | 95 | 105 mana'
  description: The light empowers you and allied gods in the area, granting Strength
    , Intelligence , and Protections Summon a pillar of blessed light repeatedly dealing
    Magical Damage and Healing allies
  damage_type: magical
  detail_kinds:
  - buff
  - null
  - magical
  - magical
  - heal
  - buff
  - buff
  - buff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: Ultimate
  name: Searing Pain
  cooldown:
  - 80.0
  - 75.0
  - 70.0
  - 65.0
  - 60.0
  cost:
  - 90.0
  details:
  - Deals bonus damage to gods based on their Max Health
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage: 375 | 450 | 525 | 600 | 675'
  - 'Damage Scaling: 125% Intelligence'
  - 'True Damage: 8% of Enemy''s Max Health'
  - 'Range: 19.2 meters'
  - 'Radius: 1.6 meters'
  - 'Cooldown: 80 | 75 | 70 | 65 | 60 seconds'
  - 'Cost: 90 mana'
  description: Blast enemies in front of you with a wave of extreme heat, dealing
    Magical Damage
  damage_type: magical
  detail_kinds:
  - magical
  - null
  - magical
  - magical
  - magical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
aspects:
- name: Aspect of Thermotherapy
  kit_changes: Solar Blessing and Searing Pain only deal base damage with no scaling.
    In return, Solar Blessing can be placed on allied gods, attaching to them and
    Searing Pain Heals allied hits.
source_url: https://wiki.smite2.com/w/Ra
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Ra Basic Attack
- Speed of Light
- Celestial Beam
- Divine Light
- Solar Blessing
- Searing Pain
<!-- WIKI:END -->
