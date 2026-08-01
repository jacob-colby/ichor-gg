---
type: smite-god
name: Khepri
pantheon: Egyptian
role: Support
specializations:
- Tank
- Lockdown
- Buffs
damage_type: magical
release_date: November 12, 2024
base_stats:
  health:
    base: 705.27
    per_level: 101.52
  mana:
    base: 296.0
    per_level: 42.0
  physical_prot:
    base: 20.52
    per_level: 3.24
  magical_prot:
    base: 29.7
    per_level: 1.62
  attack_speed:
    base: 0.96
    per_level: 1.4
  move_speed:
    base: 370.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Khepri Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 3 hit chain. Attacks in order of 1, 0.5, 1.5x damage and swing time
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Magical Damage to an enemy in front of you
- slot: Passive
  name: Fortitude
  details:
  - The interval is increased to 10 seconds if you have taken or dealt damage in the
    last 5 seconds
  - 'Health Shield: 2% Max Health'
  - 'Max Shield Health: 10% Max Health'
  - 'Shield Duration: 15 seconds'
  description: Every 5 seconds apply a Health Shield to yourself and nearby allies
- slot: 1st Ability
  name: Abduct
  cooldown:
  - 14.0
  cost:
  - 60.0
  details:
  - This deals Magical Damage
  - Gain Protections while Pulling a god and for 3 seconds afterwards
  - The Dash deals Magical Damage to enemies you pass through
  - Enemies are Silenced for the duration of the Grab
  - This ability passes through and damages non-god enemies, but stops on walls and
    enemy gods
  - 'Damage: 80 | 130 | 180 | 230 | 280'
  - 'Damage Scaling: 40% Intelligence'
  - 'Silence and Grab Duration: 1.5 | 1.6 | 1.7 | 1.8 | 1.9 seconds'
  - 'Protections: 25 | 35 | 45 | 55 | 65'
  - 'Range: 6.4 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 60 mana'
  description: Dash forward, Grabbing , and Pulling the first enemy god hit
- slot: 2nd Ability
  name: Rising Dawn
  cooldown:
  - 12.0
  cost:
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  - 90.0
  details:
  - Affected enemies repeatedly take Magical Damage over time
  - Affected enemies have reduced Physical Protections
  - Allies hit gain Damage Mitigation
  - After reaching max distance the sun sets, reapplying all effects in a larger area
  - Damage hits 11 times, hitting every 0.3 seconds
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage Per Tick: 8 | 12 | 16 | 20 | 24'
  - 'Damage Scaling Per Tick: 5% Intelligence'
  - 'Physical Protections Reduced: 5 | 10 | 15 | 20 | 25%'
  - 'Debuff Duration: 4 seconds'
  - 'Damage Mitigation: 10 | 15 | 20 | 25 | 30%'
  - 'Buff Duration: 4 seconds'
  - 'Range: 11.2 meters'
  - 'Projectile Radius: 1.6 meters'
  - 'Explosion Radius: 3.7 meters'
  - 'Cooldown: 12 seconds'
  - 'Cost: 50 | 60 | 70 | 80 | 90 mana'
  description: Roll the sun forward, setting ablaze all enemies it touches
- slot: 3rd Ability
  name: Solar Flare
  cooldown:
  - 13.0
  - 12.5
  - 12.0
  - 11.5
  - 11.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - 'Damage: 60 | 115 | 170 | 225 | 280'
  - 'Damage Scaling: 30% Intelligence'
  - 'Root Duration: 1.25 | 1.3 | 1.35 | 1.4 | 1.45 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 2.4 meters'
  - 'Cooldown: 13 | 12.5 | 12 | 11.5 | 11 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: AREA DAMAGE ROOT Call down the sun's ire, dealing Magical Damage and
    Rooting enemies in an area
- slot: Ultimate
  name: Scarab's Blessing
  cooldown:
  - 110.0
  cost:
  - 80.0
  - 90.0
  - 100.0
  - 110.0
  - 120.0
  details:
  - The blessing also Cleanses CC when applied
  - Blessed allies receive Strength, Intelligence, and Movement Speed
  - Blessed allies are Slow Immune
  - Successfully revive an ally to permanently gain a Protections buff
  - Executed allies do not revive
  - 'Strength and Intelligence: 25 | 32.5 | 40 | 47.5 | 55'
  - 'Movement Speed: 20 | 22.5 | 25 | 27.5 | 30%'
  - 'Buff Duration: 5 seconds'
  - 'Revived Health: 20 | 25 | 30 | 35 | 40%'
  - 'Permanent Protections Buff: 2 Per Revive'
  - 'Range: 8.8 meters'
  - 'Radius: 2.4 meters'
  - 'Cooldown: 110 seconds'
  - 'Cost: 80 | 90 | 100 | 110 | 120 meters'
  description: Blessed allies receive Strength , Intelligence , and Movement Speed
    Bless an allied god for 5 seconds. If the blessed ally would die while blessed,
    they are instead revived at Khepri's location
aspects:
- name: Aspect of Laceration
  kit_changes: Abduct no longer Pulls enemy gods but Roots them in place with Khepri,
    dealing constant Attack Damage for the duration. Khepri no longer gains Protections
    after Abduct ends.
source_url: https://wiki.smite2.com/w/Khepri
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Khepri Basic Attack
- Fortitude
- Abduct
- Rising Dawn
- Solar Flare
- Scarab's Blessing
<!-- WIKI:END -->
