---
type: smite-god
name: Ne Zha
pantheon: Chinese
role: Jungle
specializations:
- Slayer
- Burst Damage
- Lockdown
damage_type: physical
release_date: February 10, 2026
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
    base: 27.5
    per_level: 1.5
  attack_speed:
    base: 0.98
    per_level: 1.51
  move_speed:
    base: 380.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Ne Zha Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 4 hit chain. Attacks in order of 1, 1, 1.5, 2x damage and swing time. Final
    attack cleaves
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Physical Damage to an enemy in front of you
- slot: Passive
  name: Righteous Spirit
  details:
  - Critical Strikes grant 2 stacks
  - Gaining a stack permanently increases Critical Strike Damage
  - 'Movement Speed: 0.5% Per Stack'
  - 'Critical Damage Increase: 0.025% Per Stack'
  - 'Stacks Duration: 12 seconds'
  - 'Max Stacks: 20'
  description: Build stacks by hitting enemies to gain Movement Speed . Stacks reset
    if you have not taken or dealt damage recently
- slot: 1st Ability
  name: Universe Ring Toss
  cooldown:
  - 10.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - Subsequent hits deal 35% damage and strengthen the Slow
  - Each hit grants a stacking Movement Speed buff
  - The extra throw from catching the ring can Critically Strike
  - The ring can bounce additional times as this ability ranks up
  - This ability stops on first target hit, and does not pass through walls
  - 'Initial Damage: 90 | 120 | 150 | 180 | 210'
  - 'Initial Damage Scaling: 60% Strength'
  - 'Bounce Damage: 75 | 100 | 125 | 150 | 175'
  - 'Bounce Damage Scaling: 20% Strength'
  - 'Free Ring Damage: 80 | 110 | 140 | 170 | 200'
  - 'Free Ring Damage Scaling: 80% Strength'
  - 'Physical Protection Reduced: 5 | 7 | 9 | 11 | 13%'
  - 'Debuff Duration: 1 second'
  - 'Slow: 12.5%'
  - 'Slow Duration: 1 second'
  - 'Debuff Duration: 5%'
  - 'Movement Speed: 5%'
  - 'Buff Duration: 2 seconds'
  - 'Bounces: 4 | 5 | 6 | 7 | 8'
  - 'Range: 0.96 meters'
  - 'Radius: 8.8 meters'
  - 'Cooldown: 10 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Throw your ring to deal Physical Damage , then bounce between enemies
    dealing Physical Damage , applying a Physical Protection Debuff and Slowing .
    After the final hit, the ring bounces into the air, granting Ne Zha an extra throw
    if he catches it
- slot: 2nd Ability
  name: Flaming Spear
  cooldown:
  - 14.0
  cost:
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  details:
  - Heal based on your Righteous Spirit stacks
  - 'Attack Speed: 35 | 40 | 45 | 50 | 55%'
  - 'Critical Strike Chance: 20%'
  - 'Buff Duration: 4 | 4.5 | 5 | 5.5 | 6 seconds'
  - 'Heal: 4 | 6 | 8 | 10 | 12 Per Stack'
  - 'Cooldown: 14 seconds'
  - 'Cost: 55 | 60 | 65 | 70 | 75 mana'
  description: Ignite your spear to gain Attack Speed and Critical Strike Chance
- slot: 3rd Ability
  name: Armillary Sash
  cooldown:
  - 12.0
  cost:
  - 75.0
  details:
  - Deal Physical Damage on arrival
  - This ability can Critically Strike
  - Ne Zha is CC Immune and cannot be targeted while Leaping to his target
  - The Stun is not affected by diminishing returns
  - This ability passes through non-god enemies, but stops on walls and enemy gods
  - 'Damage: 90 | 125 | 160 | 195 | 230'
  - 'Damage Scaling: 80% Strength'
  - 'Stun Duration: 1 second'
  - 'Range: 11.2 meters'
  - 'Radius: 0.96 meters'
  - 'Cooldown: 12 seconds'
  - 'Cost: 75 mana'
  description: Throw your , Stunning the first enemy god hit and Leaping to them
- slot: Ultimate
  name: Wind Fire Wheels
  cooldown:
  - 90.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - After landing, Dash back to the cast location
  - This ability ends early if the target dies during the combo
  - The Protections Buff refreshes when the combo ends
  - 'Initial Damage: 50 | 105 | 160 | 215 | 270'
  - 'Initial Damage Scaling: 65% Strength'
  - 'Combo Damage: 23 | 40 | 57 | 74 | 91'
  - 'Combo Damage Scaling: 45% Strength'
  - 'Landing Damage: 50 | 105 | 160 | 215 | 270'
  - 'Landing Damage Scaling: 65% Strength'
  - 'Protections Buff: 30 | 35 | 40 | 45 | 50'
  - 'Protections Buff Duration: 5 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 0.96 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Dash forward, gaining protections and becoming CC Immune . Hitting
    an enemy god deals Physical Damage and Launches them and yourself into the sky,
    triggering a 3-hit combo that deals Physical Damage . Successful timing can allow
    these to Critically Strike. After the combo, slam the target down dealing Physical
    Damage and Knocking Up nearby enemies
aspects:
- name: Aspect of the Righteous Flame
  kit_changes: Righteous Sprit no longer stacks on hitting enemies. Taking damage
    charges Righteous Spirit to provide a Heal over Time. Ring Toss can bounce to
    allies for a Movement and Attack Speed boost. Flaming Spear is now a damaging
    AoE attack that buffs Ne Zha's Attacks and consumes Righteous Spirit to burst
    heal.
source_url: https://wiki.smite2.com/w/Ne_Zha
last_verified: '2026-07-25'
---
<!-- WIKI:START -->
- Ne Zha Basic Attack
- Righteous Spirit
- Universe Ring Toss
- Flaming Spear
- Armillary Sash
- Wind Fire Wheels
<!-- WIKI:END -->
