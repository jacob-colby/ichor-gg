---
type: smite-god
name: Hachiman
pantheon: Japanese
role: Carry
specializations:
- Sharpshooter
- Mobility
- Sniper
damage_type: physical
release_date: September 8, 2026
base_stats:
  health:
    base: 569.5
    per_level: 86.48
  health_regen:
    base: 1.7
    per_level: 0.2
  mana:
    base: 302.0
    per_level: 48.32
  mana_regen:
    base: 1.33
    per_level: 0.11
  physical_prot:
    base: 18.8
    per_level: 2.76
  magical_prot:
    base: 25.3
    per_level: 1.38
  attack_speed:
    base: 1.0
    per_level: 1.4
  attack_power:
    base: 36.0
    per_level: 2.42
  move_speed:
    base: 380.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Hachiman Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  detail_kinds:
  - null
  - physical
  - mechanic
  - mechanic
  damage_type: physical
  description: Fire a projectile that deals Physical Damage to the first enemy hit
- slot: Passive
  name: Master of Arms
  details:
  - Each stack refreshes the duration
  - 'Attack Speed Per Stack: 2% + 0.1% Per Level'
  - 'Mana Regen Per Stack: 0.4 + 0.04 Per Level'
  - 'Max Stats: 5'
  - 'Buff Duration: 8 seconds'
  detail_kinds:
  - null
  - buff
  - buff
  - buff
  - buff
  description: Hit enemies with your Attacks to gain a stack of Attack Speed and Mana
    Regen
- slot: 1st Ability
  name: Eagle Eye
  cooldown:
  - 12.0
  - 11.5
  - 11.0
  - 10.5
  - 10.0
  cost:
  - 50.0
  details:
  - Long-range hits deal additional bonus damage based on your Basic Attack Damage
  - 'Damage: 10 | 25 | 40 | 55 | 70'
  - 'Damage Scaling: 115% Basic Attack Damage'
  - 'Long-Range Bonus Damage: 10%'
  - 'Range: 12.8 meters'
  - 'Cooldown: 12 | 11.5 | 11 | 10.5 | 10 seconds'
  - 'Cost: 50 mana'
  detail_kinds:
  - physical
  - physical
  - physical
  - physical
  - mechanic
  - mechanic
  - mechanic
  damage_type: physical
  description: Replace your next 4 Attacks with empowered arrows that travel further
    and deal bonus Physical Damage based on your Basic Attack Damage. These Attacks
    can Critically Strike and trigger item effects
- slot: 2nd Ability
  name: Heavenly Banner
  cooldown:
  - 14.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - The banner aura stacks with the Attack Speed granted on cast
  - 'Damage: 90 | 145 | 200 | 255 | 310'
  - 'Damage Scaling: 70% Strength'
  - 'Attack Speed: 10 | 12.5 | 15 | 17.5 | 20%'
  - 'Buff Duration: 6 seconds'
  - 'Banner Duration: 6 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  detail_kinds:
  - buff
  - physical
  - physical
  - buff
  - buff
  - buff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: physical
  description: Call down a sacred banner that deals Physical Damage to enemies in
    the area and grant you Attack Speed for a duration. Leave a banner that grants
    you and allies Attack Speed while nearby
- slot: 3rd Ability
  name: Iaijutsu
  cooldown:
  - 15.0
  cost:
  - 70.0
  - 75.0
  - 80.0
  - 85.0
  - 90.0
  details:
  - Parry grants 35 Plating against a single Attack
  - 'Dash Damage: 50 | 80 | 110 | 140 | 170'
  - 'Dash Damage Scaling: 40% Strength'
  - 'Swing Damage: 50 | 80 | 110 | 140 | 170'
  - 'Swing Damage Scaling: 40% Strength'
  - 'Stun Duration: 1 second'
  - 'Max Stacks: 5 stacks'
  - 'Buff Duration: 8 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 15 seconds'
  - 'Cost: 70 | 75 | 80 | 85 | 90 mana'
  detail_kinds:
  - null
  - physical
  - physical
  - physical
  - physical
  - stun
  - buff
  - buff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  description: Dash forward, dealing Physical Damage and passing through enemies.
    At the end of the dash, swing your blade in a circle, dealing Physical Damage
    again. Enemy gods hit by both attacks are Stunned . Each enemy god hit with the
    sweep attack grants a stack of Parry
- slot: Ultimate
  name: Mounted Archery
  cooldown:
  - 110.0
  cost:
  - 50.0
  details:
  - This is a channeled ability
  - Your Movement Speed affects charge speed; moving backward slows the charge
  - Can be cancelled early
  - You can ride your horse for up to 3 seconds
  - This ability can fire through walls only if you have vision on the enemy god
  - 'Damage: 225 | 280 | 335 | 390 | 445'
  - 'Damage Scaling: 95% Strength'
  - 'Slow: 20 | 25 | 30 | 35 | 40%'
  - 'Slow Duration: 2 seconds'
  - 'Range: 13.6 meters'
  - 'Cone Angle: 45 degrees'
  - 'Cooldown: 110 seconds'
  - 'Cost: 50 mana'
  detail_kinds:
  - null
  - null
  - null
  - null
  - null
  - physical
  - physical
  - slow
  - slow
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: physical
  description: Leap onto your horse and charge forward. While mounted, you are CC
    Immune and can aim separately from your horse. Fire to launch an arrow at every
    enemy god in a cone, dealing Physical Damage and Slowing them
aspects:
- name: Aspect of the Steel Wind
  kit_changes: Eagle Eye only has 1 charge but hitting an enemy allows you to dash
    to them and deliver a sweep attack. After arriving your Interact becomes a backward
    dash. Basic Attacks have falloff damage. +4% Base Health and Health scaling.
source_url: https://wiki.smite2.com/w/Hachiman
last_verified: '2026-11-03'
---
<!-- WIKI:START -->
- Hachiman Basic Attack
- Master of Arms
- Eagle Eye
- Heavenly Banner
- Iaijutsu
- Mounted Archery
<!-- WIKI:END -->
