---
type: smite-god
name: Hercules
pantheon: Roman
role: Solo
specializations:
- Tank
- Brawler
- Lockdown
damage_type: physical
release_date: October 17, 2024
base_stats:
  health:
    base: 619.0
    per_level: 94.0
  mana:
    base: 296.0
    per_level: 42.0
  physical_prot:
    base: 19.0
    per_level: 3.0
  magical_prot:
    base: 26.5
    per_level: 1.5
  attack_speed:
    base: 0.96
    per_level: 1.4
  move_speed:
    base: 370.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Hercules Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 3 hit chain. Attacks in order of 1, 1, 1.5x damage and swing time
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: 'Hercules Notes: Deal Physical Damage to an enemy in front of you Damage
    Scaling : 100% Strength + 20% Intelligence + 100% Attack Damage Range : 1.92 meters
    Cone Angle : 120 degrees Expand Ability Video'
- slot: Passive
  name: Apotheosis
  details:
  - At 4 stacks, enter an empowered state that immediately subtracts 2 seconds from
    active cooldowns and provides an additional Strength, Protections, and Cleaving
    Attacks buff for the duration
  - Each activation of an ability can only grant 1 stack
  - Strength from Apotheosis is equal to 1 stack of Strength from taking damage from
    gods
  - 'Strength: 4 Per Stack'
  - 'Strength Scaling: 0.5 Per Level'
  - 'Apotheosis Protections: 10'
  - 'Apotheosis Protections Scaling: 2 Per Level'
  - 'Apotheosis Buff Duration: 10 seconds'
  - 'Apotheosis Buff Duration Scaling: 1 second Per Level'
  description: 'HIT ABILITIES, BECOME EMPOWERED Notes: At 4 stacks, enter an empowered
    state that immediately subtracts 2 seconds from active cooldowns and provides
    an additional Strength , Protections , and Cleaving Attacks buff for the duration
    Strength from is equal to 1 stack of Strength from taking damage from gods Hercules
    gains Strength when enemy gods damage him. This stacks up to 3 times and lasts
    5 seconds. Additionally, hit a target with an ability to gain a stack towards
    achieving , or 2 stacks from his Ultimate Strength : 4 Per Stack Strength Scaling
    : 0.5 Per Level Protections : 10 Protections Scaling : 2 Per Level Buff Duration
    : 10 seconds Buff Duration Scaling : 1 second Per Level Expand Ability Video'
- slot: 1st Ability
  name: Driving Strike
  cooldown:
  - 13.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - 'Damage: 80 | 150 | 220 | 290 | 360'
  - 'Damage Scaling: 85% Strength'
  - 'Stun: 0.6 | 0.7 | 0.8 | 0.9 | 1 second'
  - 'Range: 5.6 meters'
  - 'Radius: 0.8 meters'
  - 'Cooldown: 13 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: 'DASH, PUSHING ENEMIES Dash forward, dealing Physical Damage , Stunning
    , and Pushing enemies hit Damage : 80 | 150 | 220 | 290 | 360 Damage Scaling :
    85% Strength Stun : 0.6 | 0.7 | 0.8 | 0.9 | 1 second Range : 5.6 meters Radius
    : 0.8 meters Cooldown : 13 seconds Cost : 50 | 55 | 60 | 65 | 70 mana Expand Ability
    Video'
- slot: 2nd Ability
  name: Earthbreaker
  cooldown:
  - 13.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - 'Damage: 75 | 130 | 185 | 240 | 295'
  - 'Damage Scaling: 65% Strength'
  - 'Range: 7.2 meters'
  - 'Radius: 1.12 meters'
  - 'Cooldown: 13 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: 'LINE, PULLS ENEMIES AT END Create a rift that deals Physical Damage
    to enemies in front of you. Enemies hit by the end area are Pulled to you Damage
    : 75 | 130 | 185 | 240 | 295 Damage Scaling : 65% Strength Range : 7.2 meters
    Radius : 1.12 meters Cooldown : 13 seconds Cost : 50 | 55 | 60 | 65 | 70 mana
    Expand Ability Video'
- slot: 3rd Ability
  name: Mitigate Wounds
  cooldown:
  - 15.0
  cost:
  - 50.0
  details:
  - 'Initial Heal: 60 | 75 | 90 | 105 | 120'
  - 'Delayed Heal: 25 | 26.25 | 27.5 | 28.75 | 30% of Recent Damage Taken'
  - 'Attack Speed: 15 | 17.5 | 20 | 22.5 | 25%'
  - 'Protections: 10 | 15 | 20 | 25 | 30'
  - 'Protections Scaling: 30% of Protections from Items'
  - 'Buff Duration: 4 seconds'
  - 'Cooldown: 15 seconds'
  - 'Cost: 50 mana'
  description: 'HEAL, PROTECT Immediately Heal yourself and gain Attack Speed and
    Protections . At the end of the duration Heal yourself again for a percentage
    of damage taken during the effect Initial Heal : 60 | 75 | 90 | 105 | 120 Delayed
    Heal : 25 | 26.25 | 27.5 | 28.75 | 30% of Recent Damage Taken Attack Speed : 15
    | 17.5 | 20 | 22.5 | 25% Protections : 10 | 15 | 20 | 25 | 30 Protections Scaling
    : 30% of Protections from Items Buff Duration : 4 seconds Cooldown : 15 seconds
    Cost : 50 mana Expand Ability Video'
- slot: Ultimate
  name: Excavate
  cooldown:
  - 90.0
  - 85.0
  - 80.0
  - 75.0
  - 70.0
  cost:
  - 100.0
  details:
  - This ability can hit multiple times
  - Subsequent hits on the same enemy deal 50% less damage
  - The boulder lasts for 2.2 seconds after landing
  - This ability passes through and damages all enemies, but bounces off walls
  - 'Damage: 320 | 430 | 540 | 650 | 760'
  - 'Damage Scaling: 100% Strength'
  - 'Throw Range: 7.2 meters'
  - 'Roll Range: 7.2 meters'
  - 'Radius: 2.4 meters'
  - 'Cooldown: 90 | 85 | 80 | 75 | 70 seconds'
  - 'Cost: 100 mana'
  description: 'AREA KNOCKUP, ROLLING BOULDER Notes: Hurl a boulder at a location,
    Knocking Up enemies at the landing spot. The boulder then rolls and bounces off
    walls, dealing Physical Damage to enemies hit Damage : 320 | 430 | 540 | 650 |
    760 Damage Scaling : 100% Strength Throw Range : 7.2 meters Roll Range : 7.2 meters
    Radius : 2.4 meters Cooldown : 90 | 85 | 80 | 75 | 70 seconds Cost : 100 mana
    Expand Ability Video'
aspects:
- name: Aspect of Preservation
  kit_changes: Mitigate Wounds no longer Heals based on damage or provides Attack
    Speed. Instead Hercules gains a Stack when he or nearby allied gods take damage
    from Attacks and when the ability ends, stacks are expended to Heal nearby allied
    gods.
source_url: https://wiki.smite2.com/w/Hercules
last_verified: '2026-07-23'
---
<!-- WIKI:START -->
- Hercules Basic Attack
- Apotheosis
- Driving Strike
- Earthbreaker
- Mitigate Wounds
- Excavate
<!-- WIKI:END -->
