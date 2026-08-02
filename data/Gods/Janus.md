---
type: smite-god
name: Janus
pantheon: Roman
role: Mid
specializations:
- Burst Damage
damage_type: magical
release_date: August 12, 2025
base_stats:
  health:
    base: 569.48
    per_level: 86.48
  mana:
    base: 319.68
    per_level: 45.36
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
    base: 1.66
    per_level: 0.13
abilities:
- slot: Basic Attack
  name: Janus Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Fire a projectile that deals Magical Damage to the first enemy hit.
  damage_type: magical
  detail_kinds:
  - null
  - magical
  - mechanic
  - mechanic
- slot: Passive
  name: Passages
  details:
  - 'Bonus Damage Scaling: 20% Intelligence'
  description: BONUS DAMAGE AFTER PORTAL When you pass through a Portal or Threshold,
    your next ability deals bonus Magical Damage . Stacks up to 2 times.
  detail_kinds:
  - magical
- slot: 1st Ability
  name: Portal
  cooldown:
  - 12.0
  cost:
  - 70.0
  details:
  - Wall portals create a passage to the other side
  - Ground portals Banish you and enemies upwards, dealing Magical Damage to enemies
    on landing.
  - 'Damage: 80 | 135 | 190 | 245 | 300'
  - 'Damage Scaling: 70% Intelligence'
  - 'Range: 8.8 meters'
  - 'Radius: 1.6 meters'
  - 'Cooldown: 12 seconds'
  - 'Cost: 70 mana'
  description: Open a portal on a surface.
  damage_type: magical
  detail_kinds:
  - null
  - debuff
  - magical
  - magical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 2nd Ability
  name: Unstable Vortex
  cooldown:
  - 9.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Hitting an enemy with both portals deals bonus Magical Damage.
  - This ability passes through and damages all enemies, and passes through walls.
  - 'Damage: 100 | 165 | 230 | 295 | 360'
  - 'Damage Scaling: 95% Intelligence'
  - 'Secondary Damage: 20 | 33 | 46 | 59 | 72'
  - 'Secondary Damage Scaling: 20% Intelligence'
  - 'Range: 11.2 meters'
  - 'Cooldown: 9 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Hitting an enemy with both portals deals bonus Magical Damage . Launch
    two linked portals, dealing Magical Damage to enemies in their path.
  damage_type: magical
  detail_kinds:
  - magical
  - null
  - magical
  - magical
  - magical
  - magical
  - mechanic
  - mechanic
  - mechanic
- slot: 3rd Ability
  name: Threshold
  cooldown:
  - 12.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - Slowed enemies are Phased, causing your abilities to deal bonus Magical Damage.
    Magical damage you deal to phased enemies ignores 15% of their Magical Protection
    from your abilities
  - 'Passive: You and allies also gain a stacking Movement Speed buff when crossing
    the rift or passing through a portal'
  - 'Damage Scaling: 25 | 30 | 35 | 40 | 45% Intelligence'
  - 'Slow: 25%'
  - 'Slow Duration: 3 seconds'
  - 'Movement Speed: 15%'
  - 'Movement Speed Max Stacks: 3'
  - 'Buff Duration: 6 seconds'
  - 'Rift Duration: 3 | 3.5 | 4 | 4.5 | 5 seconds'
  - 'Range: 8.8 meters'
  - 'Cooldown: 12 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Slowed enemies are Phased, causing your abilities to deal bonus Magical
    Damage . Magical damage you deal to phased enemies ignores 15% of their Magical
    Protection from your abilities Unleash a rift that Slows enemies and grants Movement
    Speed to allies who cross it.
  damage_type: magical
  detail_kinds:
  - slow
  - buff
  - magical
  - slow
  - slow
  - buff
  - buff
  - buff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: Ultimate
  name: Through Space and Time
  cooldown:
  - 110.0
  cost:
  - 70.0
  details:
  - You are CC Immune while firing.
  - Damage increases with distance traveled.
  - This ability cannot deal damage to enemies in the fountain.
  - Magical Protection Ignore from Phased applies to damage dealt
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage: 300 | 375 | 450 | 525 | 600'
  - 'Damage Scaling: 90% Intelligence'
  - 'Max Distance Scaling: 110% Intelligence'
  - 'Distance for Max Scaling: 128 meters'
  - 'Portal Duration: 10 seconds'
  - 'Range: 320 meters'
  - 'Projectile Radius: 0.8 meters'
  - 'Cooldown: 110 seconds'
  - 'Cost: 70 mana'
  description: Fire a global projectile that deals Magical Damage and opens portals
    for allies on any surface it passes. Enemies hit are Phased if Threshold is ranked.
  damage_type: magical
  detail_kinds:
  - mechanic
  - null
  - null
  - null
  - null
  - magical
  - magical
  - magical
  - magical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
aspects: []
source_url: https://wiki.smite2.com/w/Janus
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Janus Basic Attack
- Passages
- Portal
- Unstable Vortex
- Threshold
- Through Space and Time
<!-- WIKI:END -->
