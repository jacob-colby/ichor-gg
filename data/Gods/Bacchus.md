---
type: smite-god
name: Bacchus
pantheon: Roman
role: Support
specializations:
- Tank
- Lockdown
- Mobile
damage_type: magical
release_date: May 2, 2024
base_stats:
  health:
    base: 668.52
    per_level: 101.52
  mana:
    base: 319.68
    per_level: 45.36
  physical_prot:
    base: 20.52
    per_level: 3.24
  magical_prot:
    base: 29.81
    per_level: 1.73
  attack_speed:
    base: 0.96
    per_level: 1.4
  move_speed:
    base: 370.0
    per_level: 0.0
  attack_power:
    base: 47.76
    per_level: 2.4
  health_regen:
    base: 1.84
    per_level: 0.22
  mana_regen:
    base: 1.45
    per_level: 0.12
abilities:
- slot: Basic Attack
  name: Bacchus Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Magical Damage to an enemy in front of you
  damage_type: magical
  detail_kinds:
  - null
  - magical
  - mechanic
  - mechanic
- slot: Passive
  name: Drunk-O-Meter
  details:
  - Ranges from 0% to 100% Drunk
  - Has no effect when under 30%
  - You become Tipsy at 30% Drunk, gaining the buffs
  - You become Smashed at 60%, doubling the buffs
  - Drunkeness depletes over time at a rate of 2% per second
  - 'Strength: 5'
  - 'Intelligence: 10'
  - 'Protections: 6%'
  description: As you become more Drunk, gain Strength , Intelligence , and Protections
  detail_kinds:
  - null
  - null
  - null
  - null
  - null
  - buff
  - buff
  - buff
- slot: 1st Ability
  name: Chug
  cooldown:
  - 10.0
  cost:
  - 20.0
  details:
  - You also gain Increased Strength and Intelligence
  - Your next Attack deals an additional Magical Damage
  - Empowered Attack effect lasts for 6 seconds or until a target is successfully
    hit
  - 'Damage: 0 | 10 | 30 | 50 | 70 | 90'
  - 'Damage Scaling: 0 | 50 | 50 | 50 | 50 | 50% Physical and Magical Protection'
  - 'Heal: 0 | 30 | 45 | 60 | 75 | 80'
  - 'Strength: 0 | 8 | 13 | 18 | 23 | 28'
  - 'Intelligence: 0 | 10 | 15 | 20 | 25 | 30'
  - 'Buff Duration: 0 | 6 | 6 | 6 | 6 | 6 seconds'
  - 'Drunkenness: 40 | 46 | 52 | 58 | 64 | 70%'
  - 'Cooldown: 10 seconds'
  - 'Cost: 20 mana'
  description: Take a drink, Healing , and becoming more Drunk
  damage_type: magical
  detail_kinds:
  - buff
  - magical
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
- slot: 2nd Ability
  name: Belly Flop
  cooldown:
  - 14.0
  cost:
  - 40.0
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  details:
  - Deals Magical Damage
  - If you are Tipsy, enemies are also Slowed after they land
  - Enemies are knocked straight up
  - 'Damage: 80 | 135 | 190 | 245 | 300'
  - 'Damage Scaling: 75% Strength + 30% Physical and Magical Protection'
  - 'Slow: 20%'
  - 'Slow Duration: 2 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 2.4 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 40 | 50 | 60 | 70 | 80 mana'
  description: Leap forward to and slam into the ground belly first, Knocking Up enemies
  damage_type: magical
  detail_kinds:
  - magical
  - slow
  - stun
  - magical
  - magical
  - slow
  - slow
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 3rd Ability
  name: Belch of the Gods
  cooldown:
  - 12.0
  - 11.5
  - 11.0
  - 10.5
  - 10.0
  cost:
  - 40.0
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  details:
  - If you are Tipsy or Smashed, the final hit will Stun
  - You are Displacement Immune while Channeling
  - This ability hits 3 times, plus the final hit, over 1.5 seconds
  - Reduces enemy Healing
  - 'Damage: 30 | 45 | 60 | 75 | 90'
  - 'Damage Scaling: 17.5% Intelligence'
  - 'Stun Duration: 0.9 | 0.95 | 1 | 1.05 | 1.1 seconds'
  - 'Healing Reduction: -25%'
  - 'Healing Reduction Duration: 5 seconds'
  - 'Range: 5.6 meters'
  - 'Cone Angle: 90 degrees'
  - 'Cooldown: 12 | 11.5 | 11 | 10.5 | 10 seconds'
  - 'Cost: 40 | 50 | 60 | 70 | 80 mana'
  description: Channel a big ol' burp to deal Magical Damage repeatedly to enemies
    in front of you
  damage_type: magical
  detail_kinds:
  - stun
  - mechanic
  - null
  - debuff
  - magical
  - magical
  - stun
  - debuff
  - debuff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: Ultimate
  name: Intoxicate
  cooldown:
  - 90.0
  cost:
  - 90.0
  details:
  - If you are Smashed, gain Strength and Intelligence in anger over your lost wine
  - 'Damage: 230 | 300 | 370 | 440 | 510'
  - 'Damage Scaling: 65% Intelligence'
  - 'Intoxicate Duration: 4 seconds'
  - 'Strength: 12 | 20 | 28 | 36 | 44'
  - 'Intelligence: 20 | 30 | 40 | 50 | 60'
  - 'Buff Duration: 6 seconds'
  - 'Radius: 5.6 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 90 mana'
  description: 'Smash your jug of wine, dealing Magical Damage and Intoxicating enemies
    around you Duration: 4 seconds'
  damage_type: magical
  detail_kinds:
  - buff
  - magical
  - magical
  - debuff
  - buff
  - buff
  - buff
  - mechanic
  - mechanic
  - mechanic
aspects:
- name: Aspect of Revelry
  kit_changes: After using Chug, Bacchus's inhand attacks cleave and deal bonus damage
    scaling with Strength instead of Protections, for a short duration.
source_url: https://wiki.smite2.com/w/Bacchus
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Bacchus Basic Attack
- Drunk-O-Meter
- Chug
- Belly Flop
- Belch of the Gods
- Intoxicate
<!-- WIKI:END -->
