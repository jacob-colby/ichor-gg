---
type: smite-god
name: Merlin
pantheon: Arthurian
role: Mid
specializations:
- Nuker
- Burst Damage
damage_type: magical
release_date: March 24, 2025
base_stats:
  health:
    base: 569.48
    per_level: 86.48
  health_regen:
    base: 1.7
    per_level: 0.2
  mana:
    base: 337.46
    per_level: 45.36
  mana_regen:
    base: 1.56
    per_level: 0.12
  physical_prot:
    base: 17.48
    per_level: 2.76
  magical_prot:
    base: 27.38
    per_level: 1.38
  attack_speed:
    base: 0.96
    per_level: 1.4
  attack_power:
    base: 40.85
    per_level: 2.21
  move_speed:
    base: 370.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Merlin Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  detail_kinds:
  - null
  - magical
  - mechanic
  - mechanic
  damage_type: magical
  description: Fire a projectile that deals Magical Damage to the first enemy hit
- slot: Passive
  name: Overload
  details:
  - The damage from this ability can trigger Ability Item effects
  - 'Damage: 20'
  - 'Damage Scaling: 20% Intelligence'
  - 'Max Stacks: 3'
  - 'Buff Duration: 5 seconds'
  detail_kinds:
  - null
  - magical
  - magical
  - mechanic
  - mechanic
  damage_type: magical
  description: Using an ability provides 1 stack of . Firing a Attack consumes 1 stack
    of and deals Magical Damage to enemies hit
- slot: 1st Ability
  name: Eclipse
  cooldown:
  - 12.0
  cost:
  - 60.0
  details:
  - Marked enemies take additional Magical Damage every 0.4 seconds while within the
    outer range of Eclipse
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage: 50 | 75 | 100 | 125 | 150'
  - 'Damage Scaling: 55% Intelligence'
  - 'Damage Per Tick: 5 | 15 | 25 | 35 | 45'
  - 'Damage Scaling Per Tick: 10% Intelligence'
  - 'Range: 9.6 meters'
  - 'Initial Radius: 0.8 meters'
  - 'Max Radius: 2.4 meters'
  - 'Outer Radius: 4 meters'
  - 'Cooldown: 12 seconds'
  - 'Cost: 60 mana'
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
  - mechanic
  - mechanic
  damage_type: magical
  description: Marked enemies take additional Magical Damage every 0.4 seconds while
    within the outer range of Conjure a celestial orb that grows in size as it travels,
    dealing Magical Damage to enemies and marking them
  stance: Arcane
- slot: 2nd Ability
  name: Vortex
  cooldown:
  - 14.0
  - 13.5
  - 13.0
  - 12.5
  - 12.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - 'Damage: 65 | 95 | 125 | 155 | 185'
  - 'Damage Scaling: 70% Intelligence'
  - 'Range: 9.6 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 14 | 13.5 | 13 | 12.5 | 12 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  detail_kinds:
  - magical
  - magical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: ELEMENTAL CONTROL SPELLS Deploy a field of arcane energy. After a delay,
    the deals Magical Damage and Pulls enemies towards the center
  stance: Arcane
- slot: 3rd Ability
  name: Flicker
  cooldown:
  - 24.0
  - 23.0
  - 22.0
  - 21.0
  - 20.0
  cost:
  - 70.0
  details:
  - Heal a percentage of the damage taken within the last 4 seconds
  - 'Heal: 22.5% of Recent Damage Taken'
  - 'Range: 4.8 meters'
  - 'Cooldown: 24 | 23 | 22 | 21 | 20 seconds'
  - 'Cost: 70 mana'
  detail_kinds:
  - heal
  - heal
  - mechanic
  - mechanic
  - mechanic
  description: You quickly Teleport a short distance. Depending on your current Stance,
    you gain different effects when using this ability
  stance: Arcane
- slot: Ultimate
  name: Elemental Mastery
  cooldown:
  - 40.0
  - 40.0
  - 35.0
  - 30.0
  - 25.0
  - 20.0
  cost:
  - 40.0
  - 40.0
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  details:
  - After the explosion reaches its apex, it collapses in on itself dealing Magical
    Damage again
  - During the explosion time, you can choose which stance to enter into next
  - 'Damage: 0 | 80 | 110 | 140 | 170 | 210'
  - 'Damage Scaling: 15% Intelligence'
  - 'Radius: 4 meters'
  - 'Cooldown: 40 | 40 | 35 | 30 | 25 | 20 seconds'
  - 'Cost: 40 | 40 | 50 | 60 | 70 | 80 mana'
  detail_kinds:
  - magical
  - null
  - magical
  - magical
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Tap into your inner potential, exploding with energy in your current
    stance dealing Magical Damage and Knocking Up enemies hit. Depending on your current
    Stance, you gain different effects when using this ability
  stance: Arcane
- slot: 1st Ability
  name: Radiate
  cooldown:
  - 14.0
  - 13.5
  - 13.0
  - 12.5
  - 12.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Each time Radiate hits an enemy, it also applies a Burn, dealing additional Magical
    Damage over time
  - Burn does damage every 0.5 seconds for 2 seconds
  - 'Damage: 12 | 19 | 26 | 33 | 40'
  - 'Damage Scaling: 20% Intelligence'
  - 'Damage Per Tick: 5 | 10 | 15 | 20 | 25'
  - 'Damage Scaling Per Tick: 5% Intelligence'
  - 'Range: 7.2 meters'
  - 'Radius: 0.8 meters'
  - 'Cooldown: 14 | 13.5 | 13 | 12.5 | 12 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  detail_kinds:
  - debuff
  - debuff
  - magical
  - magical
  - magical
  - magical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Each time hits an enemy, it also applies a Burn , dealing additional
    Magical Damage over time Channel a beam of intense fire for 2 seconds that deals
    Magical Damage every 0.25 seconds
  stance: Fire
- slot: 2nd Ability
  name: Dragonfire
  cooldown:
  - 16.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - If caught in the center of the area, enemies are afflicted by Radiate's Burn and
    gods have their Protections Reduced
  - The dragons persist for 3 seconds
  - 'Damage: 12 | 15 | 18 | 21 | 24'
  - 'Damage Scaling: 20% Intelligence'
  - 'Protections Reduced: 4% Per Stack'
  - 'Max Debuff Stacks: 4'
  - 'Deploy Range: 8 meters'
  - 'Range: 4 meters'
  - 'Cone Angle: 80 degrees'
  - 'Cooldown: 16 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  detail_kinds:
  - debuff
  - null
  - magical
  - magical
  - debuff
  - debuff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Summon forth 2 ethereal dragons that deal Magical Damage to enemies
    every 0.25 seconds
  stance: Fire
- slot: 3rd Ability
  name: Flicker
  cooldown:
  - 24.0
  - 23.0
  - 22.0
  - 21.0
  - 20.0
  cost:
  - 70.0
  details:
  - For 4 seconds, your Attacks apply Radiate's Burn to enemies hit
  - 'Range: 4.8 meters'
  - 'Cooldown: 24 | 23 | 22 | 21 | 20 seconds'
  - 'Cost: 70 mana'
  detail_kinds:
  - debuff
  - mechanic
  - mechanic
  - mechanic
  description: You quickly Teleport a short distance. Depending on your current Stance,
    you gain different effects when using this ability
  stance: Fire
- slot: 1st Ability
  name: Frostbolt
  cooldown:
  - 6.0
  cost:
  - 60.0
  details:
  - This ability deals an additional 15% damage if the enemy hit is Slowed
  - This ability stops on first target hit, and does not pass through walls
  - 'Damage: 60 | 95 | 130 | 165 | 200'
  - 'Damage Scaling: 55% Intelligence'
  - 'Range: 11.2 meters'
  - 'Radius: 0.64 meters'
  - 'Explosion Radius: 3.2 meters'
  - 'Cooldown: 6 seconds'
  - 'Cost: 60 mana'
  detail_kinds:
  - slow
  - null
  - magical
  - magical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Fire a that explodes when it hits an enemy, dealing Magical Damage
    in a small area
  stance: Ice
- slot: 2nd Ability
  name: Blizzard
  cooldown:
  - 6.0
  cost:
  - 60.0
  details:
  - Enemies hit are debuffed with a stacking Slow
  - This ability hits 8 times over 4 seconds
  - 'Damage Per Tick: 10 | 25 | 40 | 55 | 70'
  - 'Damage Scaling Per Tick: 15% Intelligence'
  - 'Slow: 8% Per Stack'
  - 'Max Debuff Stacks: 5'
  - 'Slow Duration: 2 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 6 seconds'
  - 'Cost: 60 mana'
  detail_kinds:
  - slow
  - null
  - magical
  - magical
  - slow
  - slow
  - slow
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Create a , dealing Magical Damage repeatedly to enemies in an area
  stance: Ice
- slot: 3rd Ability
  name: Flicker
  cooldown:
  - 24.0
  - 23.0
  - 22.0
  - 21.0
  - 20.0
  cost:
  - 70.0
  details:
  - Ability Cooldowns are reduced
  - Ability Cooldown Reduction does not apply to Flicker
  - 'Cooldown Reduction: 2 seconds'
  - 'Range: 4.8 meters'
  - 'Cooldown: 24 | 23 | 22 | 21 | 20 seconds'
  - 'Cost: 70 mana'
  detail_kinds:
  - null
  - null
  - buff
  - mechanic
  - mechanic
  - mechanic
  description: Ability Cooldown Reduction does not apply to You quickly Teleport a
    short distance. Depending on your current Stance, you gain different effects when
    using this ability
  stance: Ice
- slot: Ultimate
  name: Elemental Mastery
  cooldown:
  - 40.0
  - 40.0
  - 35.0
  - 30.0
  - 25.0
  - 20.0
  cost:
  - 40.0
  - 40.0
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  details:
  - After the explosion reaches its apex, it collapses in on itself dealing Magical
    Damage again
  - During the explosion time, you can choose which stance to enter into next
  - 'Damage: 0 | 80 | 110 | 140 | 170 | 210'
  - 'Damage Scaling: 15% Intelligence'
  - 'Slow: 0 | 20 | 20 | 20 | 20 | 20%'
  - 'Slow Duration: 0 | 2 | 2 | 2 | 2 | 2 seconds'
  - 'Radius: 4 meters'
  - 'Cooldown: 40 | 40 | 35 | 30 | 25 | 20 seconds'
  - 'Cost: 40 | 40 | 50 | 60 | 70 | 80 mana'
  detail_kinds:
  - magical
  - null
  - magical
  - magical
  - slow
  - slow
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Tap into your inner potential, exploding with energy in your current
    stance dealing Magical Damage and Slowing enemies hit. Depending on your current
    Stance, you gain different effects when using this ability
  stance: Ice
aspects:
- name: Aspect of Pandemonium
  kit_changes: Elemental Mastery has a reduced cooldown and each time it is used,
    a random Stance is selected with 2 random primary abilities, Flicker will always
    persist. Using Elemental Mastery provides an Intelligence buff for a short duration.
source_url: https://wiki.smite2.com/w/Merlin
last_verified: '2026-08-09'
---
<!-- WIKI:START -->
- Merlin Basic Attack
- Overload
- Eclipse
- Vortex
- Flicker
- Elemental Mastery
- Radiate
- Dragonfire
- Flicker
- Frostbolt
- Blizzard
- Flicker
- Elemental Mastery
<!-- WIKI:END -->
