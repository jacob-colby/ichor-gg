---
type: smite-god
name: Anhur
pantheon: Egyptian
role: Carry
specializations:
- Sharpshooter
- Lockdown
- Mobility
damage_type: physical
release_date: May 2, 2024
base_stats:
  health:
    base: 619.0
    per_level: 94.0
  mana:
    base: 296.0
    per_level: 42.0
  physical_prot:
    base: 20.04
    per_level: 2.76
  magical_prot:
    base: 25.3
    per_level: 1.38
  attack_speed:
    base: 1.0
    per_level: 1.4
  move_speed:
    base: 370.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Anhur Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Fire a projectile that deals Physical Damage to the first enemy hit
- slot: Passive
  name: Enfeeble
  details:
  - 'Physical Protections Reduced: 5 + 0.75 Per Level'
  - 'Debuff Duration: 4 seconds'
  description: ATTACKS WEAKEN ENEMIES Dealing Damage to enemies reduces their Physical
    Protection
- slot: 1st Ability
  name: Shifting Sands
  cooldown:
  - 14.0
  - 13.5
  - 13.0
  - 12.5
  - 12.0
  cost:
  - 40.0
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  details:
  - Enemies in the sands are Slowed and Take Additional Damage from your basic attacks
  - The obelisk acts as a Wall
  - The Slow stacks with an additional Slow when closer to the obelisk
  - Reactive to destroy the obelisk early
  - 'Slow: 15%'
  - 'Additional Slow: 15%'
  - 'Increased Damage Taken: 12 | 15 | 18 | 21 | 24%'
  - 'Lifetime: 7.5 seconds'
  - 'Range: 11.2 meters'
  - 'Radius: 9.6 meters'
  - 'Cooldown: 14 | 13.5 | 13 | 12.5 | 12 seconds'
  - 'Cost: 40 | 50 | 60 | 70 | 80 mana'
  description: Summon an obelisk, surrounded by shifting sands Additional
- slot: 2nd Ability
  name: Impale
  cooldown:
  - 11.0
  cost:
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  - 90.0
  details:
  - The first god hit is Pushed
  - If the god hits a Wall, they are Stunned
  - The enemy god Displaced by this ability deals damage to enemies it collides with
  - This ability passes through and damages non-god enemies, but stops on walls and
    enemy gods
  - 'Damage: 125 | 185 | 245 | 305 | 365'
  - 'Damage Scaling: 90% Strength'
  - 'Stun Duration: 0.9 | 0.95 | 1 | 1.05 | 1.1 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  - 'Cooldown: 11 seconds'
  - 'Cost: 50 | 60 | 70 | 80 | 90 mana'
  description: Throw a large spear, dealing Physical Damage in a line
- slot: 3rd Ability
  name: Disperse
  cooldown:
  - 15.0
  - 14.4
  - 14.0
  - 13.5
  - 13.0
  cost:
  - 40.0
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  details:
  - Knock Back all enemies from your landing point
  - Enemies are Displaced up and away from your landing location
  - 'Damage: 90 | 130 | 170 | 210 | 250'
  - 'Damage Scaling: 75% Strength'
  - 'Range: 8.8 meters'
  - 'Radius: 2.4 meters'
  - 'Cooldown: 15 | 14.4 | 14 | 13.5 | 13 seconds'
  - 'Cost: 40 | 50 | 60 | 70 | 80 mana'
  description: Leap forward, dealing Physical Damage where you land
- slot: Ultimate
  name: Desert Fury
  cooldown:
  - 90.0
  - 85.0
  - 80.0
  - 75.0
  - 70.0
  cost:
  - 80.0
  - 85.0
  - 90.0
  - 95.0
  - 100.0
  details:
  - The final spear has an increased radius and deals a burst of bonus Physical Damage
  - You are CC Immune while using this ability
  - Ability fires 4 times, plus the final projectile, over 1.5 seconds
  - You can cancel this ability at any time
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage Per Tick: 80 | 110 | 140 | 170 | 200'
  - 'Damage Scaling Per Tick: 45% Strength'
  - 'Final Damage: 150 | 200 | 250 | 300 | 350'
  - 'Final Damage Scaling: 115% Strength'
  - 'Range: 12.8 meters'
  - 'Radius: 0.56 meters'
  - 'Final Radius: 0.72 meters'
  - 'Cooldown: 90 | 85 | 80 | 75 | 70 seconds'
  - 'Cost: 80 | 85 | 90 | 95 | 100 mana'
  description: Hurl a series of empowered spears, each dealing Physical Damage
aspects:
- name: Aspect of Pride
  kit_changes: Enfeeble no longer Debuffs enemies but dealing damage to the same enemy
    god with Basic Attacks provides Anhur up to 100% bonus Attack Speed.
source_url: https://wiki.smite2.com/w/Anhur
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Anhur Basic Attack
- Enfeeble
- Shifting Sands
- Impale
- Disperse
- Desert Fury
<!-- WIKI:END -->
