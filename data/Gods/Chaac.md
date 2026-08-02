---
type: smite-god
name: Chaac
pantheon: Maya
role: Solo
specializations:
- Nuker
- Tank
- Lockdown
damage_type: physical
release_date: May 2, 2024
base_stats:
  health:
    base: 661.0
    per_level: 94.0
  mana:
    base: 299.36
    per_level: 45.36
  physical_prot:
    base: 20.28
    per_level: 3.0
  magical_prot:
    base: 29.58
    per_level: 1.5
  attack_speed:
    base: 1.0
    per_level: 1.4
  move_speed:
    base: 370.0
    per_level: 0.0
  attack_power:
    base: 47.76
    per_level: 2.4
  health_regen:
    base: 1.7
    per_level: 0.2
  mana_regen:
    base: 1.47
    per_level: 0.14
abilities:
- slot: Basic Attack
  name: Chaac Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 3 hit chain. Attacks in order of 1, 0.5, 1.5x damage and swing time
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
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
  name: Overflow
  details:
  - Cooldown -2 seconds
  - 'Heal: 10'
  - 'Heal Scaling: 12.5% Intelligence'
  - 'Heal Amount Per Level: 1'
  description: FREE CAST AFTER HITS After 5 successful Basic Attacks, the next ability
    you use costs 0 mana, has Lower Cooldown , and Heals you
  detail_kinds:
  - buff
  - heal
  - heal
  - heal
- slot: 1st Ability
  name: Thunder Strike
  cooldown:
  - 10.0
  cost:
  - 45.0
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  details:
  - The Axe remains deployed to empower Torrent or Rain Dance
  - Reactivate to destroy the Axe early
  - 'Damage: 100 | 160 | 220 | 280 | 340'
  - 'Damage Scaling: 75% Strength + 60% Intelligence'
  - 'Axe Duration: 5 seconds'
  - 'Range: 9.6 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 10 seconds'
  - 'Cost: 45 | 50 | 55 | 60 | 65 mana'
  description: Throw your Axe forward, dealing Physical Damage to enemies in the area
    where it lands
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
  - mechanic
- slot: 2nd Ability
  name: Torrent
  cooldown:
  - 10.0
  - 9.5
  - 9.0
  - 8.5
  - 8.0
  cost:
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  - 90.0
  details:
  - If the Axe is deployed, first Dash to it and deal Physical Damage to enemies that
    you pass through
  - This Dash passes through walls
  - If you Dash, you will still do the area attack upon reaching the Axe
  - Minions provide 1 stack, gods provide 2 stacks
  - 'Damage: 100 | 160 | 220 | 280 | 340'
  - 'Damage Scaling: 70% Strength'
  - 'Dash Damage: 35 | 57.5 | 80 | 102.5 | 125'
  - 'Dash Damage Scaling: 30% Strength'
  - 'Protections: 5 | 7 | 9 | 11 | 13 Per Stack'
  - 'Protection Buff Scaling: 6% Intelligence'
  - 'Buff Duration: 6 seconds'
  - 'Max Buff Stacks: 4'
  - 'Attack Radius: 3.2 meters'
  - 'Dash Radius: 1.28 meters'
  - 'Cooldown: 10 | 9.5 | 9 | 8.5 | 8 seconds'
  - 'Cost: 50 | 60 | 70 | 80 | 90 mana'
  description: If you Dash , you will still do the area attack upon reaching the Axe
    Swing your Axe around you, dealing Physical Damage to enemies and gaining Protections
    for each enemy hit
  damage_type: physical
  detail_kinds:
  - null
  - null
  - null
  - null
  - physical
  - physical
  - physical
  - physical
  - buff
  - buff
  - buff
  - buff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 3rd Ability
  name: Rain Dance
  cooldown:
  - 13.0
  cost:
  - 55.0
  - 65.0
  - 75.0
  - 85.0
  - 95.0
  details:
  - Enemies caught in the rain are Slowed and have Reduced Attack Speed
  - Heals 8 times over 6 seconds
  - If the Axe is deployed, create a Rain Storm at the Axe's location as well
  - Enemies in both Rain Storms are Slowed and Debuffed for twice as much
  - Grants a stack of Overflow every 1.5s
  - 'Heal Per Tick: 8 | 11 | 14 | 17 | 20'
  - 'Heal Scaling Per Tick: 2.5% Intelligence'
  - 'Dampening: 9 | 10.5 | 12 | 13.5 | 15'
  - 'Slow: 15 | 17.5 | 20 | 22.5 | 25%'
  - 'Attack Speed Slow: 10 | 12.5 | 15 | 17.5 | 20%'
  - 'Radius: 6.4 meters'
  - 'Axe Radius: 9.6 meters'
  - 'Cooldown: 13 seconds'
  - 'Cost: 55 | 65 | 75 | 85 | 95 mana'
  description: Create a rainstorm that Heals you over time and provides Dampening
  detail_kinds:
  - slow
  - heal
  - null
  - slow
  - null
  - heal
  - heal
  - buff
  - slow
  - debuff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: Ultimate
  name: Storm Call
  cooldown:
  - 90.0
  cost:
  - 80.0
  - 90.0
  - 100.0
  - 110.0
  - 120.0
  details:
  - You are CC Immune and gain Damage Mitigation while Channeling
  - Enemies are knocked straight up
  - 'Damage: 300 | 360 | 420 | 480 | 540'
  - 'Damage Scaling: 120% Strength + 100% Intelligence'
  - 'Damage Mitigation: 50 | 55 | 60 | 65 | 70%'
  - 'Silence Duration: 1.5 seconds'
  - 'Radius: 5.6 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 80 | 90 | 100 | 110 | 120 mana'
  description: Charge up your Lightning Axe, then unleash a blast dealing Physical
    Damage , Knocking Up , and Silencing in an area around you
  damage_type: physical
  detail_kinds:
  - mechanic
  - stun
  - physical
  - physical
  - buff
  - debuff
  - mechanic
  - mechanic
  - mechanic
aspects:
- name: Aspect of Fulmination
  kit_changes: Rain Dance no longer heals but damages enemies in the area instead.
source_url: https://wiki.smite2.com/w/Chaac
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Chaac Basic Attack
- Overflow
- Thunder Strike
- Torrent
- Rain Dance
- Storm Call
<!-- WIKI:END -->
