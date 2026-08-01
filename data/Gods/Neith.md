---
type: smite-god
name: Neith
pantheon: Egyptian
role: Carry Mid
specializations:
- Nuker
- Sharpshooter
- Global
damage_type: physical
release_date: May 2, 2024
base_stats:
  health:
    base: 569.48
    per_level: 86.48
  mana:
    base: 334.1
    per_level: 42.0
  physical_prot:
    base: 18.76
    per_level: 2.76
  magical_prot:
    base: 25.3
    per_level: 1.38
  attack_speed:
    base: 1.0
    per_level: 1.51
  move_speed:
    base: 370.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Neith Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Fire a projectile that deals Physical Damage to the first enemy hit
- slot: Passive
  name: Broken Weave
  details:
  - Detonating Weaves deals Physical Damage to nearby enemies and Roots them
  - You gain a stacking Attack Speed and Intelligence buff per Weave detonated
  - 'Damage: 25'
  - 'Damage Scaling: 5 Per Level + 15% Strength + 25% Intelligence'
  - 'Root Duration: 1 second'
  - 'Attack Speed: 4% Per Stack'
  - 'Attack Speed Scaling: 3% Strength Per Stack'
  - 'Intelligence: 8'
  - 'Intelligence Scaling: 0.4 Per Level'
  - 'Buff Duration: 30 seconds'
  - 'Max Buff Stacks: 3'
  description: Your abilities either create or detonate Weaves
- slot: 1st Ability
  name: Spirit Arrow
  cooldown:
  - 13.0
  - 12.5
  - 12.0
  - 11.5
  - 11.0
  cost:
  - 40.0
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  details:
  - This ability detonates Weaves it hits
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage: 80 | 145 | 210 | 275 | 340'
  - 'Damage Scaling: 95% Strength + 75% Intelligence'
  - 'Root Duration: 1 second'
  - 'Range: 10.4 meters'
  - 'Radius: 0.56 meters'
  - 'Cooldown: 13 | 12.5 | 12 | 11.5 | 11 seconds'
  - 'Cost: 40 | 50 | 60 | 70 | 80 mana'
  description: Fire a projectile that deals Physical Damage and Roots enemies
- slot: 2nd Ability
  name: Unravel
  cooldown:
  - 12.0
  cost:
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  - 90.0
  details:
  - This ability creates a Weave
  - You Heal for each enemy hit
  - Hitting a god Heals for more
  - Always creates a Weave in the center of the area. Creates additional Weaves for
    each enemy god hit at the locations of those gods
  - 'Damage: 80 | 130 | 180 | 230 | 280'
  - 'Damage Scaling: 55% Strength + 80% Intelligence'
  - 'Heal: 11 | 15 | 19 | 23 | 27'
  - 'Heal Scaling: 5% Intelligence'
  - 'Increased Heal: 25 | 32 | 39 | 46 | 54'
  - 'Increased Heal Scaling: 5% Intelligence'
  - 'Range: 8.8 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 12 seconds'
  - 'Cost: 50 | 60 | 70 | 80 | 90 mana'
  description: the world weaves, dealing Physical Damage to enemies in an area Increased
- slot: 3rd Ability
  name: Back Flip
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
  - This ability detonates Weaves that it hits
  - This ability can travel over walls, as long as you can reach a valid landing area
  - 'Damage: 85 | 130 | 175 | 220 | 265'
  - 'Damage Scaling: 60% Intelligence'
  - 'Slow: 30%'
  - 'Slow Duration: 2 | 2.5 | 3 | 3.5 | 4 seconds'
  - 'Range: 9.6 meters'
  - 'Cone Range: 5.6 meters'
  - Cone Angle:110 degrees
  - 'Cooldown: 15 | 14.5 | 14 | 13.5 | 13 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Deal Physical Damage and Slow enemies in front of you, then Leap backwards
- slot: Ultimate
  name: World Weaver
  cooldown:
  - 100.0
  cost:
  - 80.0
  - 90.0
  - 100.0
  - 110.0
  - 120.0
  details:
  - The arrow deals Physical Damage and Stuns
  - You can fire the arrow before it is fully charged, but it will deal reduced damage
  - Damage scales linearly from 50% to 100% based on Channel time
  - Channel for 0.5 seconds for minimum damage, or for 2 seconds to deal fully charged
    damage
  - Enemy gods can step in front of this projectile to be hit by it instead of the
    selected god
  - You can cancel this ability anytime before firing, the costs and cooldown will
    not be consumed
  - This ability passes through non-god enemies, and passes through walls, but stops
    on enemy gods
  - 'Damage: 200 | 250 | 300 | 350 | 400'
  - 'Damage Scaling: 105% Strength + 90% Intelligence'
  - 'Stun Duration: 1 second'
  - 'Cooldown: 100 seconds'
  - 'Cost: 80 | 90 | 100 | 110 | 120 mana'
  description: Charge up and fire an arrow across the world, locked on to an enemy
    god and ignoring obstacles
aspects:
- name: Aspect of Wind
  kit_changes: Broken Weave explosions no longer Root enemies and the Buff has a reduced
    duration however the Attack Speed gained is much higher. Additionally using World
    Weaver provides stacks of Broken Weave.
source_url: https://wiki.smite2.com/w/Neith
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Neith Basic Attack
- Broken Weave
- Spirit Arrow
- Unravel
- Back Flip
- World Weaver
<!-- WIKI:END -->
