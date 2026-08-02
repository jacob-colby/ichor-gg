---
type: smite-god
name: Amaterasu
pantheon: Japanese
role: Solo
specializations:
- Brawler
- Tank
- Buffs
damage_type: physical
release_date: September 17, 2024
base_stats:
  health:
    base: 661.0
    per_level: 94.0
  mana:
    base: 296.0
    per_level: 42.0
  physical_prot:
    base: 20.28
    per_level: 3.0
  magical_prot:
    base: 27.5
    per_level: 1.5
  attack_speed:
    base: 0.98
    per_level: 1.61
  move_speed:
    base: 375.0
    per_level: 0.0
  attack_power:
    base: 47.95
    per_level: 2.59
  health_regen:
    base: 1.7
    per_level: 0.2
  mana_regen:
    base: 1.45
    per_level: 0.12
abilities:
- slot: Basic Attack
  name: Amaterasu Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 3 hit chain. Attacks in order of 1, 0.5, 1x damage and swing time.
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
  name: Illuminating Strike
  details:
  - 'Increased Damage Taken: 10%'
  - 'Debuff Duration: 6 seconds'
  - 'Radius: 4.8 meters'
  description: ATTACKS WEAKEN ENEMIES Basic attack or Ult an enemy 3 times to illuminate
    their weaknesses, causing them and other nearby enemies to take more damage from
    all sources
  detail_kinds:
  - debuff
  - debuff
  - mechanic
- slot: 1st Ability
  name: Divine Presence
  cooldown:
  - 12.0
  cost:
  - 30.0
  details:
  - Gold buff provides a Health Shield for 6 seconds on activation, and a persistent
    Movement Speed Buff
  - Red buff provides an Attack Speed Buff for 6 seconds on activation, and a persistent
    Strength and Intelligence Buff
  - 'Heal Per Tick: 15 | 21 | 27 | 33 | 39'
  - 'Heal Scaling Per Tick: 3.5% Intelligence'
  - 'Shield Health: 8% of your HP'
  - 'Movement Speed: 7 | 9 | 11 | 13 | 15%'
  - 'Attack Speed: 12 | 14 | 16 | 18 | 20%'
  - 'Strength: 12 | 15 | 18 | 21 | 24'
  - 'Strength Scaling: 5% Intelligence'
  - 'Intelligence: 18 | 22 | 26 | 30 | 34'
  - 'Intelligence Scaling: 3% Intelligence'
  - 'Radius: 5.6 meters'
  - 'Cooldown: 12 seconds'
  - 'Cost: 30 mana'
  description: Heal yourself over 4 seconds, and alternante between the Gold and Red
    buff effects
  detail_kinds:
  - shield
  - buff
  - heal
  - heal
  - shield
  - buff
  - buff
  - buff
  - buff
  - buff
  - buff
  - mechanic
  - mechanic
  - mechanic
- slot: 2nd Ability
  name: Heavenly Reflection
  cooldown:
  - 12.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Deal and take damage to charge the Mirror
  - Base Damage is doubled when mirror is fully charged
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage: 80 | 120 | 160 | 200 | 240'
  - 'Damage Scaling: 60% Strength + 60% Intelligence'
  - 'Damage Taken Reduction: 15%'
  - 'Damage Reduction Scaling: 5% Intelligence'
  - 'Buff Duration: 5 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 0.8 meters'
  - 'Cooldown: 12 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Charge your Mirror and decrease all damage you take while charging.
    Reactive the ability to fire a projectile that deals Physical Damage to enemies,
    increased by the mirror's charge amount
  damage_type: physical
  detail_kinds:
  - null
  - null
  - null
  - physical
  - physical
  - buff
  - buff
  - buff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 3rd Ability
  name: Glorious Charge
  cooldown:
  - 15.0
  cost:
  - 60.0
  details:
  - You can cancel this ability at any time
  - This ability passes through and damages non-god enemies, but stops on walls and
    enemy gods
  - 'Physical Damage: 80 | 135 | 190 | 245 | 300'
  - 'Physical Damage: 60% Strength'
  - 'Silence Duration: 1 second'
  - 'Range: 8.8 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 15 seconds'
  - 'Cost: 60 mana'
  description: Silence enemies in front of you for 1 second, then Dash forward and
    deal Physical Damage
  detail_kinds:
  - null
  - null
  - physical
  - physical
  - debuff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: Ultimate
  name: Dazzling Offensive
  cooldown:
  - 90.0
  cost:
  - 100.0
  details:
  - Attacks deal more damage and have bonus effects on each subsequent successful
    hit
  - 2nd hit deals 1.2x damage and Slows by 30% for 2 seconds
  - 3rd hit deals 1.4x damage and Stuns for 1.2 seconds
  - 'Damage: 100 | 150 | 200 | 250 | 300'
  - 'Damage Scaling: 45% Strength + 50% Intelligence'
  - 'Slow: 30%'
  - 'Slow Duration: 2 seconds'
  - 'Stun Duration: 1.2 seconds'
  - 'Radius: 5.6 meters'
  - 'Cone Angle: 110 degrees'
  - 'Cooldown: 90 seconds'
  - 'Cost: 100 mana'
  description: Become CC Immune and then attack 3 times to deal Physical Damage to
    enemies in front of you each time
  damage_type: physical
  detail_kinds:
  - null
  - slow
  - stun
  - physical
  - physical
  - slow
  - slow
  - stun
  - mechanic
  - mechanic
  - mechanic
  - mechanic
aspects:
- name: Aspect of Valor
  kit_changes: Divine Presence now defaults to Red Buff, and when activated, you gain
    Movement Speed, Haste and Basic Attack Power in addition to the original effects.
    It no longer alternates to Gold Buff, or heals you when activated.
source_url: https://wiki.smite2.com/w/Amaterasu
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Amaterasu Basic Attack
- Illuminating Strike
- Divine Presence
- Heavenly Reflection
- Glorious Charge
- Dazzling Offensive
<!-- WIKI:END -->
