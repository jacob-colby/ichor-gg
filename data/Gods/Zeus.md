---
type: smite-god
name: Zeus
pantheon: Greek
role: Mid
specializations:
- Sharpshooter
- Nuker
damage_type: magical
release_date: May 2, 2024
base_stats:
  health:
    base: 569.48
    per_level: 86.48
  mana:
    base: 316.32
    per_level: 42.0
  physical_prot:
    base: 19.0
    per_level: 3.0
  magical_prot:
    base: 27.5
    per_level: 1.5
  attack_speed:
    base: 1.0
    per_level: 1.61
  move_speed:
    base: 375.0
    per_level: 0.0
  attack_power:
    base: 44.4
    per_level: 2.4
  health_regen:
    base: 1.82
    per_level: 0.2
  mana_regen:
    base: 1.56
    per_level: 0.12
abilities:
- slot: Basic Attack
  name: Zeus Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - Attacks apply Charges
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Fire a projectile that deals Magical Damage to the first enemy hit
  damage_type: magical
  detail_kinds:
  - null
  - null
  - magical
  - mechanic
  - mechanic
- slot: Passive
  name: Overcharge
  details:
  - Enemies take increased Attack damage from you for each Charge they have
  - Non-god enemies immediately take 3 stacks
  - Overcharge's effect stacks with Critical Strikes
  - 'Damage Increase: 15% Per Stack'
  - 'Debuff Duration: 5 seconds'
  - 'Max Debuff Stacks: 3'
  description: '''s effect stacks with Critical Strikes Deal damage to apply Charges'
  damage_type: magical
  detail_kinds:
  - magical
  - null
  - null
  - magical
  - debuff
  - debuff
- slot: 1st Ability
  name: Chain Lightning
  cooldown:
  - 12.0
  - 11.5
  - 11.0
  - 10.5
  - 10.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - This ability stops on first target hit, and does not pass through walls
  - 'Damage: 70 | 115 | 160 | 205 | 250'
  - 'Damage Scaling: 60% Intelligence'
  - 'Slow: 20%'
  - 'Slow Duration: 2 seconds'
  - 'Bounces: 5 | 5 | 5 | 6 | 6'
  - 'Range: 8.8 meters'
  - 'Radius: 0.56 meters'
  - 'Cooldown: 12 | 11.5 | 11 | 10.5 | 10 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Hurl a bolt of lightning that arcs between enemies, dealing Magical
    Damage and Slowing
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
  name: Thunderclap
  cooldown:
  - 12.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - You also gain increased Attack Speed, Movement Speed, and Haste
  - 'Damage: 70 | 120 | 170 | 220 | 270'
  - 'Damage Scaling: 75% Intelligence'
  - 'Attack Speed: 30%'
  - 'Movement Speed: 20 | 22.5 | 25 | 27.5 | 30%'
  - 'Haste: 10 | 11.25 | 12.5 | 13.75 | 15%'
  - 'Buff Duration: 4 seconds'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 12 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: You also gain increased Attack Speed , Movement Speed , and Haste Call
    down lightning, dealing Magical Damage to nearby enemies
  damage_type: magical
  detail_kinds:
  - buff
  - magical
  - magical
  - buff
  - buff
  - buff
  - buff
  - mechanic
  - mechanic
  - mechanic
- slot: 3rd Ability
  name: Detonate Charge
  cooldown:
  - 12.0
  - 11.5
  - 11.0
  - 10.5
  - 10.0
  cost:
  - 70.0
  - 75.0
  - 80.0
  - 85.0
  - 90.0
  details:
  - Enemies at Max Charges are Stunned
  - This ability cannot be activated unless an enemy has a Charge
  - Damage is multiplied by 1, 1.7, 2.4x based on the number of Charges
  - 'Damage: 40 | 65 | 90 | 115 | 140'
  - 'Damage Scaling: 30% Intelligence'
  - 'Stun Duration: 0.5 seconds'
  - 'Cooldown: 12 | 11.5 | 11 | 10.5 | 10 seconds'
  - 'Cost: 70 | 75 | 80 | 85 | 90 mana'
  description: Detonate the Charges on all enemies, dealing Magical Damage for each
    Charge
  damage_type: magical
  detail_kinds:
  - stun
  - null
  - null
  - magical
  - magical
  - stun
  - mechanic
  - mechanic
- slot: Ultimate
  name: Lightning Storm
  cooldown:
  - 90.0
  - 85.0
  - 80.0
  - 75.0
  - 70.0
  cost:
  - 100.0
  details:
  - This ability hits 5 times over 4.5 seconds
  - 'Damage: 120 | 150 | 180 | 210 | 240'
  - 'Damage Scaling: 75% Intelligence'
  - 'Range: 8.8 meters'
  - 'Radius: 4.8 meters'
  - 'Cooldown: 90 | 85 | 80 | 75 | 70 seconds'
  - 'Cost: 100 mana'
  description: Conjure a lightning storm that deals Magical Damage repeatedly in an
    area
  damage_type: magical
  detail_kinds:
  - null
  - magical
  - magical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
aspects: []
source_url: https://wiki.smite2.com/w/Zeus
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Zeus Basic Attack
- Overcharge
- Chain Lightning
- Thunderclap
- Detonate Charge
- Lightning Storm
<!-- WIKI:END -->
