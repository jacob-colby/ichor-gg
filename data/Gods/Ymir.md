---
type: smite-god
name: Ymir
pantheon: Norse
role: Support
specializations:
- Brawler
- Tank
- Lockdown
damage_type: magical
release_date: May 2, 2024
base_stats:
  health:
    base: 675.1
    per_level: 108.1
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
    base: 0.98
    per_level: 1.51
  move_speed:
    base: 370.0
    per_level: 0.0
  attack_power:
    base: 44.59
    per_level: 2.59
  health_regen:
    base: 1.84
    per_level: 0.22
  mana_regen:
    base: 1.45
    per_level: 0.12
abilities:
- slot: Basic Attack
  name: Ymir Basic Attack
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
  name: Frostbite
  details:
  - Frostbitten enemies take more Attack damage from you, deal less damage to you,
    and have decreased Attack Speed
  - Frostbite's effect stacks with Critical Strikes
  - 'Damage Scaling: 175% Basic Attack Damage'
  - 'Reduced Damage Dealt: 15%'
  - 'Attack Speed Slow: 10%'
  description: Frostbitten enemies take more Attack damage from you, deal less damage
    to you , and have decreased Attack Speed 's effect stacks with Critical Strikes
    Your abilities apply when they damage or CC enemies
  damage_type: magical
  detail_kinds:
  - magical
  - null
  - magical
  - debuff
  - debuff
- slot: 1st Ability
  name: Ice Wall
  cooldown:
  - 15.0
  - 14.5
  - 14.0
  - 13.5
  - 13.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - Reactivate to destroy the Wall early
  - The Wall impedes all characters
  - Create the Wall at your feet to Displace yourself up and forward
  - Displaces enemies up and away from the Wall
  - 'Wall Duration: 2.5 | 3 | 3.5 | 4 | 4.5 seconds'
  - 'Range: 11.2 meters'
  - 'Radius: 3.25 meters'
  - 'Cooldown: 15 | 14.5 | 14 | 13.5 | 13 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Create a Wall that Knocks Back enemies on creation
  detail_kinds:
  - null
  - null
  - stun
  - stun
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 2nd Ability
  name: Glacial Strike
  cooldown:
  - 8.0
  - 7.5
  - 7.0
  - 6.5
  - 6.0
  cost:
  - 45.0
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  details:
  - Damaging area starts at Ymir and moves away over time
  - You are Slowed during activation
  - 'Damage: 90 | 150 | 210 | 270 | 330'
  - 'Damage Scaling: 70% Intelligence + 45% Strength'
  - 'Slow: 25%'
  - 'Slow Duration: 2 seconds'
  - 'Self Slow: 42.5%'
  - 'Range: 6 meters'
  - 'Radius: 3.6 meters'
  - 'Cooldown: 8 | 7.5 | 7 | 6.5 | 6 seconds'
  - 'Cost: 45 | 50 | 55 | 60 | 65 mana'
  description: Smash your club into the ground, creating a field of ice that deals
    Magical Damage and Slows
  damage_type: magical
  detail_kinds:
  - null
  - slow
  - magical
  - magical
  - slow
  - slow
  - slow
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 3rd Ability
  name: Frost Breath
  cooldown:
  - 14.0
  cost:
  - 40.0
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  details:
  - You are Rooted during activation
  - 'Damage: 65 | 100 | 135 | 170 | 205'
  - 'Damage Scaling: 55% Intelligence'
  - 'Stun Duration: 1 | 1.1 | 1.2 | 1.3 | 1.4 seconds'
  - 'Stun Duration Scaling: 0.2 seconds per 100 Item Protections, stacking up to 2
    times'
  - 'Range: 5.6 meters'
  - 'Cone Angle: 90 degrees'
  - 'Cooldown: 14 seconds'
  - 'Cost: 40 | 50 | 60 | 70 | 80 mana'
  description: Unleash your freezing breath, Stunning enemies in front of you and
    dealing Magical Damage
  damage_type: magical
  detail_kinds:
  - debuff
  - magical
  - magical
  - stun
  - stun
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: Ultimate
  name: Shards of Ice
  cooldown:
  - 70.0
  cost:
  - 80.0
  - 90.0
  - 100.0
  - 110.0
  - 120.0
  details:
  - You may cancel this ability early, dealing less damage
  - You are CC Immune while using this ability
  - Damage scales linearly from 50% to 100% based on Channel time
  - Max Channel time of 3 seconds
  - You are Rooted while Channeling
  - 'Damage: 550 | 750 | 950 | 1,150 | 1,350'
  - 'Damage Scaling: 160% Intelligence + 45% Protections'
  - 'Slow: 40%'
  - 'Radius: 5.6 meters'
  - 'Cooldown: 70 seconds'
  - 'Cost: 80 | 90 | 100 | 110 | 120 mana'
  description: Freeze the air around you, Slowing enemies as you Channel. After 3
    seconds, erupt with a burst of Magical Damage to all enemies in range
  damage_type: magical
  detail_kinds:
  - null
  - mechanic
  - null
  - null
  - debuff
  - magical
  - magical
  - slow
  - mechanic
  - mechanic
  - mechanic
aspects: []
source_url: https://wiki.smite2.com/w/Ymir
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Ymir Basic Attack
- Frostbite
- Ice Wall
- Glacial Strike
- Frost Breath
- Shards of Ice
<!-- WIKI:END -->
