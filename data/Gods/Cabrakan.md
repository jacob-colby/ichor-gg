---
type: smite-god
name: Cabrakan
pantheon: Maya
role: Solo Support
specializations:
- Tank
- Lockdown
- Area Control
damage_type: magical
release_date: January 20, 2025
base_stats:
  health:
    base: 626.52
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
    base: 0.98
    per_level: 1.4
  move_speed:
    base: 375.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Cabrakan Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Magical Damage to an enemy in front of you
- slot: Passive
  name: Shadow Zone
  details:
  - 'Self Damage Mitigation: 4% + 1% per 100 Item Protections'
  - 'Ally Damage Mitigation: 4%'
  - 'Damage Increase: 3%'
  - 'Debuff Duration: 4 seconds'
  - 'Radius: 4.8 meters'
  description: DAMAGE REDUCTION AURA You and nearby allies gain Damage Mitigation
    . Deal Increased Damage to enemies that damage you or nearby allies
- slot: 1st Ability
  name: Seismic Crush
  cooldown:
  - 14.0
  - 13.5
  - 13.0
  - 12.5
  - 12.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - Gain Haste, Slow Immunity, and Root Immunity while this effect is active
  - Stun duration ignores Diminishing Returns
  - 'Damage: 90 | 140 | 190 | 240 | 290'
  - 'Damage Scaling: 45% Intelligence + 75% Strength'
  - 'Stun Duration: 0.8 seconds'
  - 'Attack Speed: 70%'
  - 'Movement Speed: 15 | 20 | 25 | 30 | 35%'
  - 'Buff Duration: 5 seconds'
  - 'Cooldown: 14 | 13.5 | 13 | 12.5 | 12 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Gain Haste , Slow Immunity , and Root Immunity while this effect is
    active Become enraged, increasing your Movement Speed and Attack Speed . While
    active, your next successful Attack will Stun and deal bonus Magical Damage
- slot: 2nd Ability
  name: Refraction Shield
  cooldown:
  - 12.0
  cost:
  - 10.0
  details:
  - At Max Stacks, gain access to Enhanced Refraction Shield on a separate cooldown
  - Enhanced Refraction Shield's concussive blast deals Magical Damage and Stuns enemies
  - Restores Mana per enemy hit by Refraction Shield, or Health per enemy hit by Enhanced
    Refraction Shield
  - Cannot gain access to Enhanced Refraction Shield when it is on cooldown
  - 'Damage: 50 | 105 | 160 | 215 | 270'
  - 'Damage Scaling: 55% Intelligence'
  - 'Enhanced Damage Scaling: 75% Strength'
  - 'Stun Duration: 0.9 | 1 | 1.1 | 1.2 | 1.3 seconds'
  - 'Heal: 12 | 15 | 18 | 21 | 24 Per Target'
  - 'Bonus Heal Scaling: 0.5% Max Health'
  - 'Mana Restore: 10 | 14 | 18 | 22 | 26 Per Target'
  - 'Protections: 5 | 6 | 7 | 8 | 9'
  - 'Buff Duration: 8 seconds'
  - 'Max Stacks: 5'
  - 'Range: 3.2 meters'
  - 'Cone Angle: 120 degrees'
  - 'Cooldown: 12 seconds'
  - 'Enhanced Cooldown: 12 seconds'
  - 'Cost: 10 mana'
  description: At Max Stacks, gain access to Enhanced on a separate cooldown Enhanced
    's concussive blast deals Magical Damage and Stuns enemies Restores Mana per enemy
    hit by , or Health per enemy hit by Enhanced Cannot gain access to Enhanced when
    it is on cooldown Clash your shields, unleashing a concussive blast that deals
    Magical Damage . Taking damage charges your shields, granting Protections Enhanced
- slot: 3rd Ability
  name: Tremors
  cooldown:
  - 4.0
  cost:
  - 20.0
  - 30.0
  - 40.0
  - 50.0
  - 60.0
  details:
  - Refire for a stronger quake that deals Magical Damage and Cripples enemies, and
    incurs an increased cooldown
  - Maximum Channel duration of 10 seconds
  - Cost incurred for each slam
  - You can cancel this ability at any time
  - 'Damage: 18 | 28 | 38 | 48 | 58'
  - 'Damage Scaling: 40% Intelligence'
  - 'Refire Damage: 50 | 90 | 130 | 170 | 210'
  - 'Refire Damage Scaling: 55% Strength'
  - 'Tremble Duration: 0.55 seconds'
  - 'Cripple Duration: 1 second'
  - 'Radius: 4.8 meters'
  - 'Cooldown: 4 seconds'
  - 'Refire Cooldown: 12 seconds'
  - 'Cost: 20 | 30 | 40 | 50 | 60 mana'
  description: Repeatedly slam the ground, Trembling and dealing Magical Damage to
    enemies every 0.5 seconds while pulling them toward you in a Vortex
- slot: Ultimate
  name: Tectonic Shift
  cooldown:
  - 90.0
  - 85.0
  - 80.0
  - 75.0
  - 70.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - Refire the ability to destroy all pieces at once
  - Wall pieces can last up to 15 seconds if not destroyed
  - Wall pieces each have 3 Hit Points, an enemy Attack will deal 1 Hit Point per
    hit
  - Your Attacks will deal 3 Hit Points, instantly destroying a piece of the wall
  - 'Damage: 150 | 250 | 350 | 450 | 550'
  - 'Damage Scaling: 65% Intelligence + 95% Strength'
  - 'Range: 5.6 meters'
  - 'Radius: 4 meters'
  - 'Cooldown: 90 | 85 | 80 | 75 | 70 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Stomp the ground to create a fissure that deals Magical Damage to enemies
    in its path. From the fissure, five pieces of earth erupt to form a wall
aspects:
- name: Aspect of the Rotund Jotunn
  kit_changes: Seismic Crush Stealths you and Slows enemies instead of Stunning. Refraction
    Shield stacks energy by dealing damage and bonus damage instead of a Stun. Tremors
    spawn a vision dealing damage and Slowing on the final hit. You teleport to a
    location before casting Tectonic Shift, each wall having less Health.
source_url: https://wiki.smite2.com/w/Cabrakan
last_verified: '2026-07-25'
---
<!-- WIKI:START -->
- Cabrakan Basic Attack
- Shadow Zone
- Seismic Crush
- Refraction Shield
- Tremors
- Tectonic Shift
<!-- WIKI:END -->
