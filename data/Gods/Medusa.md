---
type: smite-god
name: Medusa
pantheon: Greek
role: Carry
specializations:
- Burst Damage
- Lockdown
- Pressure
damage_type: physical
release_date: December 10, 2024
base_stats:
  health:
    base: 569.48
    per_level: 86.48
  mana:
    base: 302.3
    per_level: 48.3
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
    base: 380.0
    per_level: 0.0
  attack_power:
    base: 44.4
    per_level: 2.4
  health_regen:
    base: 1.7
    per_level: 0.2
  mana_regen:
    base: 1.33
    per_level: 0.11
abilities:
- slot: Basic Attack
  name: Medusa Basic Attack
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
  name: Sidewinder
  description: NO MOVEMENT PENALTY You suffer no movement penalty when strafing and
    half the movement penalty when backpedaling
- slot: 1st Ability
  name: Viper Shot
  cooldown:
  - 12.0
  - 11.5
  - 11.0
  - 10.5
  - 10.0
  cost:
  - 50.0
  details:
  - Each successful hit on an enemy god reduces the Cooldown of this ability by 0.5
    seconds
  - 'Damage Per Tick: 10 | 15 | 20 | 25 | 30'
  - 'Damage Scaling Per Tick: 8% Strength + 8% Intelligence'
  - 'Attack Speed: 40 | 45 | 50 | 55 | 60%'
  - 'Attack Speed Scaling: 15% Strength'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  - 'Cooldown: 12 | 11.5 | 11 | 10.5 | 10 seconds'
  - 'Cost: 50 mana'
  description: Gain Increased Attack Speed and augment your next 4 Attacks, shooting
    vipers that poison the target hit, dealing Physical Damage every 0.5 seconds for
    1.5 seconds
  damage_type: physical
  detail_kinds:
  - null
  - physical
  - physical
  - buff
  - buff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 2nd Ability
  name: Acid Spray
  cooldown:
  - 14.0
  - 13.5
  - 13.0
  - 12.5
  - 12.0
  cost:
  - 40.0
  - 45.0
  - 50.0
  - 55.0
  - 60.0
  details:
  - Reduces enemy Healing
  - Acid Spray will explode on statues Medusa has created
  - This ability stops on first target hit, and does not pass through walls
  - 'Damage: 90 | 145 | 200 | 255 | 310'
  - 'Damage Scaling: 65% Strength + 80% Intelligence'
  - 'Healing Reduction: -25%'
  - 'Healing Reduction Duration: 5 seconds'
  - 'Range: 7.2 meters'
  - 'Radius: 0.64 meters'
  - 'Cone Range: 7.2 meters'
  - 'Cone Angle: 70 degrees'
  - 'Cooldown: 14 | 13.5 | 13 | 12.5 | 12 seconds'
  - 'Cost: 40 | 45 | 50 | 55 | 60 mana'
  description: will explode on statues Medusa has created Spit acid that deals Physical
    Damage to the first enemy hit, then spraying out in a cone behind them Cone
  damage_type: physical
  detail_kinds:
  - debuff
  - null
  - null
  - physical
  - physical
  - debuff
  - debuff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 3rd Ability
  name: Lacerate
  cooldown:
  - 16.0
  - 15.5
  - 15.0
  - 14.5
  - 14.0
  cost:
  - 70.0
  details:
  - The first enemy god you encounter causes you to stop before Damaging and Rooting
    them
  - Destroy statues instantly when colliding with them during this ability
  - This ability passes through and damages non-god enemies, but stops on walls and
    enemy gods
  - 'Damage: 80 | 130 | 180 | 230 | 280'
  - 'Damage Scaling: 75% Strength + 40% Intelligence'
  - 'Root Duration: 1 second'
  - 'Range: 8.8 meters'
  - 'Radius: 0.96 meters'
  - 'Cooldown: 16 | 15.5 | 15 | 14.5 | 14 seconds'
  - 'Cost: 70 mana'
  description: Dash forward, dealing Physical Damage to all enemies you pass through
  damage_type: physical
  detail_kinds:
  - physical
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
  name: Petrify
  cooldown:
  - 90.0
  cost:
  - 100.0
  details:
  - Enemies are dealt Physical Damage and Stunned if they look at you
  - Enemies are dealt reduced Physical Damage and Slowed if they are not looking at
    you
  - You are CC Immune while using this ability
  - Enemy gods that are killed while affected by this ability are turned into a stone
    statue and remain behind as a reminder to others
  - Statues last indefinitely but may be destroyed with 4 Attacks or by Lacerate
  - When a statue is destroyed, the cooldown of Lacerate is reduced by 5 seconds,
    you gain a temporary Strength and Intelligence buff, and you gain a permanent
    Strength and Intelligence buff
  - This ability passes through and damages all enemies, but stops on walls
  - 'Damage: 270 | 365 | 460 | 555 | 650'
  - 'Damage Scaling: 80% Strength + 95% Intelligence'
  - 'Not Looking Damage Reduction: -15%'
  - 'Slow: 20 | 25 | 30 | 35 | 40%'
  - 'Slow Duration: 3 seconds'
  - 'Stun Duration: 2 seconds'
  - 'Temporary Strength and Intelligence Buff: 10%'
  - 'Buff Duration: 10 seconds'
  - 'Permanent Strength and Intelligence Buff: 5'
  - 'Range: 11.2 meters'
  - 'Cone Angle: 40 degrees'
  - 'Cooldown: 90 seconds'
  - 'Cost: 100 mana'
  description: When a statue is destroyed, the cooldown of Lacerate is reduced by
    5 seconds, you gain a temporary Strength and Intelligence buff , and you gain
    a permanent Strength and Intelligence buff Remove your mask, revealing your true
    face to deliver a powerful blast from your horrifying gorgon gaze
  damage_type: physical
  detail_kinds:
  - physical
  - physical
  - mechanic
  - null
  - null
  - buff
  - null
  - physical
  - physical
  - physical
  - slow
  - slow
  - stun
  - buff
  - buff
  - buff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
aspects: []
source_url: https://wiki.smite2.com/w/Medusa
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Medusa Basic Attack
- Sidewinder
- Viper Shot
- Acid Spray
- Lacerate
- Petrify
<!-- WIKI:END -->
