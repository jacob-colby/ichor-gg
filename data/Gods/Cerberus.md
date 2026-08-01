---
type: smite-god
name: Cerberus
pantheon: Greek
role: Solo Support
specializations:
- Tank
- Area Control
- Pressure
damage_type: magical
release_date: April 4, 2025
base_stats:
  health:
    base: 668.52
    per_level: 101.52
  mana:
    base: 299.36
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
abilities:
- slot: Basic Attack
  name: Cerberus Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 3 hit chain. Attacks in order of 1, 0.8, 0.8x damage and swing time
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Magical Damage to an enemy in front of you
- slot: Passive
  name: Spirit of Death
  details:
  - The amount stolen is based off of the base heal effect and does not include any
    increase or reduction applied
  - Severing an enemy's soul increases Healing stolen from them by 20% for 5 seconds
  description: Any time a nearby enemy god is Healed , that Heal is reduced by 25%
    and you receive 60% + 1% per level of the Heal
- slot: 1st Ability
  name: Paralyzing Spit
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
  - If your dog heads are alert, they also spit venom
  - Each head is alerted by landing a Basic Attack and all are alerted after Ghastly
    Breath is used
  - When all heads are alert the snake tail projectile Stuns targets. The Stun is
    75% less effective within 2.5 meters
  - Each projectile that hits the same target deals 20% less damage
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage: 65 | 90 | 115 | 140 | 165'
  - 'Damage Scaling: 20% Intelligence'
  - 'Stun: 1.1 | 1.2 | 1.3 | 1.4 | 1.5 seconds'
  - 'Range: 8 meters'
  - 'Radius: 0.56 meters'
  - 'Cooldown: 13 | 12.5 | 12 | 11.5 | 11 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Spit venom with your snake tail that passes through enemies dealing
    Magical Damage
- slot: 2nd Ability
  name: Ghastly Breath
  cooldown:
  - 14.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Enemies hit have their Magical Protections reduced up to 3 times
  - Enemies in the center of the breath are Slowed up to 3 times
  - Firing this ability immediately alerts all of your heads
  - Killing souls with this ability enhances its damage by 15% for the remaining duration
    up to 3 times. At 3 stacks the entire area immediately applies 3 stacks of the
    Slow
  - You can cancel this ability at any time
  - 'Damage Per Tick: 20 | 30 | 40 | 50 | 60'
  - 'Damage Scaling Per Tick: 12.5% Intelligence'
  - 'Slow: 7 | 7.5 | 8 | 8.5 | 9%'
  - 'Magical Protections Reduced: 3 | 4.5 | 6 | 7.5 | 9'
  - 'Debuff Duration: 2 seconds'
  - 'Range: 5.6 meters'
  - 'Cone Angle: 90 degrees'
  - 'Slow Cone Angle: 30 degrees'
  - 'Cooldown: 14 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Your heads release a cone of noxious breath dealing Magical Damage
    repeatedly to enemies in front of you
- slot: 3rd Ability
  name: Soul Expulsion
  cooldown:
  - 14.0
  cost:
  - 55.0
  details:
  - Killing a soul Heals you and reduces Soul Expulsion's cooldown by 2 seconds
  - 'Damage: 80 | 120 | 160 | 200 | 240'
  - 'Damage Scaling: 60% Intelligence'
  - 'Heal From Gods: 15 | 30 | 45 | 60 | 75'
  - 'Heal From Minions: 10 | 15 | 20 | 25 | 30'
  - 'Soul Health: 50 | 60 | 70 | 80 | 90'
  - 'Range: 8.8 meters'
  - 'Radius: 2.4 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 55 mana'
  description: Killing a soul Heals you and reduces 's cooldown by 2 seconds Leap
    forward dealing Magical Damage to enemies and severing their souls when you land
- slot: Ultimate
  name: Stygian Torment
  cooldown:
  - 90.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Using this ability alerts all of your heads
  - This ability can be cleansed
  - 'Damage: 180 | 255 | 330 | 405 | 480'
  - 'Damage Scaling: 55% Intelligence'
  - 'Radius: 4.8 meters'
  - 'Displacement Distance: 3.6 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Raise all enemy Gods into the air, severing their souls and dealing
    Magical Damage to them before pulling them in front of you
aspects:
- name: Aspect of Souls
  kit_changes: Ghastly Breath ticks an additional time for every 3 god souls you have
    killed but souls no longer heal. Stygian Torment now only knocks up targets.
source_url: https://wiki.smite2.com/w/Cerberus
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Cerberus Basic Attack
- Spirit of Death
- Paralyzing Spit
- Ghastly Breath
- Soul Expulsion
- Stygian Torment
<!-- WIKI:END -->
