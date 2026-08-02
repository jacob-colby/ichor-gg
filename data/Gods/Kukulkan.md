---
type: smite-god
name: Kukulkan
pantheon: Maya
role: Mid
specializations:
- Nuker
damage_type: magical
release_date: May 2, 2024
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
    base: 370.0
    per_level: 0.0
  attack_power:
    base: 40.85
    per_level: 2.21
  health_regen:
    base: 1.7
    per_level: 0.2
  mana_regen:
    base: 1.57
    per_level: 0.13
abilities:
- slot: Basic Attack
  name: Kukulkan Basic Attack
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
  name: Power of the Wind Jewel
  details:
  - This effect does not scale off Base god Mana
  - 'Intelligence From Item Mana: 7%'
  description: As you build items that provide Mana, you gain Bonus Intelligence
  detail_kinds:
  - null
  - buff
- slot: 1st Ability
  name: Zephyr
  cooldown:
  - 7.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - This ability stops on first target hit, and does not pass through walls
  - 'Damage: 85 | 135 | 185 | 235 | 285'
  - 'Damage Scaling: 85% Intelligence'
  - 'Slow: 20 | 25 | 30 | 35 | 40%'
  - 'Slow Duration: 3 seconds'
  - 'Range: 11.2 meters'
  - 'Radius: 0.64 meters'
  - 'Explosion Radius: 2.25 meters'
  - 'Cooldown: 7 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Fire a projectile that explodes on the first enemy hit. The explosion
    deals Magical Damage and Slows enemies in the area
  damage_type: magical
  detail_kinds:
  - null
  - magical
  - magical
  - slow
  - slow
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 2nd Ability
  name: Slipstream
  cooldown:
  - 13.0
  - 12.5
  - 12.0
  - 11.5
  - 11.0
  cost:
  - 40.0
  - 45.0
  - 50.0
  - 55.0
  - 60.0
  details:
  - Activate this within a Whirlwind to Dash, dealing Magical Damage and Slowing enemies
    hit
  - Movement Speed Buff is applied as 4 stacks, stacks are lost one at a time
  - Dash passes through and damages all enemies, but stops on walls
  - 'Movement Speed: 7 | 9 | 11 | 13 | 15% Per Stack'
  - 'Buff Duration: 4 seconds'
  - 'Dash Damage: 95 | 145 | 195 | 245 | 295'
  - 'Dash Damage Scaling: 90% Intelligence'
  - 'Dash Slow: 20 | 25 | 30 | 35 | 40%'
  - 'Dash Slow Duration: 3 seconds'
  - 'Dash Range: 8.8 meters'
  - 'Dash Radius: 2 meters'
  - 'Cooldown: 13 | 12.5 | 12 | 11.5 | 11 seconds'
  - 'Cost: 40 | 45 | 50 | 55 | 60 mana'
  description: Activate this within a Whirlwind to Dash , dealing Magical Damage and
    Slowing enemies hit Summon the wind to become Slow Immune and gain Movement Speed
    that fades over time
  detail_kinds:
  - null
  - buff
  - null
  - buff
  - buff
  - magical
  - magical
  - slow
  - slow
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 3rd Ability
  name: Whirlwind
  cooldown:
  - 15.0
  - 14.0
  - 13.0
  - 12.0
  - 11.0
  cost:
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  - 90.0
  details:
  - Affected enemies repeatedly take Magical Damage over time, even if they leave
    the area
  - The Whirlwind attempts to apply the effect every 0.35 seconds for 4 seconds
  - Damage Over Time is refreshed on each hit
  - Damage Over Time hits 6 times over 2.5 seconds
  - 'Damage Per Tick: 12 | 19 | 26 | 33 | 40'
  - 'Damage Scaling Per Tick: 20% Intelligence'
  - 'Range: 8.8 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 15 | 14 | 13 | 12 | 11 seconds'
  - 'Cost: 50 | 60 | 70 | 80 | 90 mana'
  description: The attempts to apply the effect every 0.35 seconds for 4 seconds Create
    a , which spreads onto all enemies that enter its area
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
  - mechanic
- slot: Ultimate
  name: Spirit of the Nine Winds
  cooldown:
  - 90.0
  cost:
  - 120.0
  details:
  - Enemies hit are also Knocked Up away from the projectile
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage: 400 | 500 | 600 | 700 | 800'
  - 'Damage Scaling: 115% Intelligence'
  - 'Range: 20.8 meters'
  - 'Radius: 1.4 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 120 mana'
  description: Summon the Sprit of the Nine Winds to deal Magical Damage in a large
    path
  damage_type: magical
  detail_kinds:
  - stun
  - null
  - magical
  - magical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
aspects:
- name: Aspect of the Squall
  kit_changes: You gain Mana from Jungle monster kills and god kills and assists.
    Zephyr has a shorter range but fires 3 projectiles. Slipstream is always a dash
    and steals protections. Whirlwind attaches to you and explodes in a blast that
    knocks back enemies.
source_url: https://wiki.smite2.com/w/Kukulkan
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Kukulkan Basic Attack
- Power of the Wind Jewel
- Zephyr
- Slipstream
- Whirlwind
- Spirit of the Nine Winds
<!-- WIKI:END -->
