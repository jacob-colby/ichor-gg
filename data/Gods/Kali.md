---
type: smite-god
name: Kali
pantheon: Hindu
role: Jungle
specializations:
- Constant Damage
- Pressure
- Sustain
damage_type: physical
release_date: April 18, 2025
base_stats:
  health:
    base: 619.0
    per_level: 94.0
  mana:
    base: 272.32
    per_level: 38.64
  physical_prot:
    base: 19.0
    per_level: 3.0
  magical_prot:
    base: 27.5
    per_level: 1.5
  attack_speed:
    base: 1.02
    per_level: 1.4
  move_speed:
    base: 380.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Kali Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 3 hit chain. Attacks in order of 1, 0.5, 0.5x damage and swing time
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Physical Damage to an enemy in front of you
- slot: Passive
  name: Marked for Death
  details:
  - If a marked target dies, the enemy god closest to Kali becomes marked
  - You can use 'Interact' in the fountain to change your marked target
  - 'Physical Penetration: 5 + 0.5% Per Level'
  - 'Heal on Kill: 20%'
  - 'Heal on Assist: 7.5%'
  - 'Bonus Gold Bounty: 20%'
  description: Mark a god. Gain Physical Penetration against that god. Killing that
    god restores Health . Assists restore less Health . You also gain bonus Gold Bounty
    . Additionally, Attacks and most abilities apply Rupture to enemies
- slot: 1st Ability
  name: Nimble Strike
  cooldown:
  - 13.0
  cost:
  - 60.0
  details:
  - If you land on an enemy god, Heal for a percentage of their missing health
  - If you land on multiple gods, Heal based on the god that would heal you the most
  - Applies 2 stacks of Rupture
  - 'Damage: 85 | 140 | 195 | 250 | 305'
  - 'Damage Scaling: 80% Strength'
  - 'Heal: 20 | 30 | 40 | 50 | 60'
  - 'god Heal: 6% Missing Health'
  - 'Range: 8.8 meters'
  - 'Radius: 2.4 meters'
  - 'Cooldown: 13 seconds'
  - 'Cost: 60 mana'
  description: Leap dealing Physical Damage to enemies when landing. Heal if this
    ability lands on an enemy
- slot: 2nd Ability
  name: Lash
  cooldown:
  - 12.0
  - 11.5
  - 11.0
  - 10.5
  - 10.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Applies 1 stack of Rupture for each blade hit
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage: 35 | 45 | 55 | 65 | 75'
  - 'Damage Scaling: 25% Strength + 30% Intelligence'
  - 'Bleed Damage: 10 | 15 | 20 | 25 | 30'
  - 'Bleed Damage Scaling: 5% Strength + 7% Intelligence'
  - 'Range: 11.2 meters'
  - 'Radius: 0.48 meters'
  - 'Cooldown: 12 | 11.5 | 11 | 10.5 | 10 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Throw 3 blades forward, each dealing Physical Damage and applying a
    Bleed . The Bleed deals Physical Damage every 0.5 seconds for 3 seconds
- slot: 3rd Ability
  name: Incense
  cooldown:
  - 15.0
  cost:
  - 60.0
  details:
  - All Heals after the first are reduced by 80%. The strongest Heal is resolved first
  - Non-god targets with a stack of Rupture are damaged and Heal as if they had 3
    stacks
  - 'Damage: 35 | 55 | 75 | 95 | 115'
  - 'Damage Scaling: 15% Strength + 30% Intelligence'
  - 'Bonus Damage: 8 | 13 | 18 | 23 | 28 Per Stack'
  - 'Bonus Damage Scaling: 8% Strength + 10% Intelligence'
  - 'Heal: 18 | 26 | 34 | 42 | 50'
  - 'Bonus Heal: 8 | 10 | 12 | 14 | 16 Per Stack'
  - 'Bonus Heal Scaling: 4% Intelligence'
  - 'Stun Duration: 0.8 seconds'
  - 'Strength: 8 | 12 | 16 | 20 | 24'
  - 'Intelligence: 12 | 17 | 22 | 27 | 32'
  - 'Buff Duration: 4 | 4.5 | 5 | 5.5 | 6 seconds'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 15 seconds'
  - 'Cost: 60 mana'
  description: Stun enemies with incense, gaining bonus Strength and Intelligence
    . Siphon targets, dealing Physical Damage and Healing per hit. Damage and Heal
    increases per Rupture stack, consuming them
- slot: Ultimate
  name: Destruction
  cooldown:
  - 90.0
  cost:
  - 60.0
  - 70.0
  - 80.0
  - 90.0
  - 100.0
  details:
  - If you are below 15% Max Health when the ultimate ends, you are restored to 15%
    of your Max Health
  - Each hit applies 1 stack of Rupture
  - 'Damage: 16 | 19 | 22 | 25 | 28'
  - 'Damage Scaling: 4% Strength + 6.5% Intelligence'
  - 'Duration: 3.5 | 3.75 | 4 | 4.25 | 4.5 seconds'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 60 | 70 | 80 | 90 | 100 mana'
  description: Become Death Immune , Displacement Immune , Slow Immune , and Root
    Immune . Deal Physical Damage to nearby enemies every 0.25 seconds for the duration
aspects:
- name: Aspect of Unbound Destruction
  kit_changes: Kali's Basics are ranged. Rupture procs at 5 stacks to deal damage
    & heal her. Incense doesn't stun or proc Rupture but knocks back & applies Rupture.
    Destruction doesn't damage, prevent death, or give immunities but gives stats,
    has a lower cooldown, resets cooldown on Mark kills, makes her Basics apply 2
    Rupture stacks & pierce.
source_url: https://wiki.smite2.com/w/Kali
last_verified: '2026-07-25'
---
<!-- WIKI:START -->
- Kali Basic Attack
- Marked for Death
- Nimble Strike
- Lash
- Incense
- Destruction
<!-- WIKI:END -->
