---
type: smite-god
name: Hou Yi
pantheon: Chinese
role: Carry
specializations:
- Constant Damage
damage_type: physical
release_date: July 29, 2025
base_stats:
  health:
    base: 577.0
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
    base: 0.98
    per_level: 1.51
  move_speed:
    base: 370.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Hou Yi Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Fire a projectile that deals Physical Damage to the first enemy hit
- slot: Passive
  name: Suntouched
  details:
  - 'Buff Duration: 3 seconds'
  - Cooldown Reduction -2 seconds
  description: MARK ATTACKERS When Critically Hit or taking more than 25% of your
    Health in a single blow, become , reducing active cooldowns and Marking the enemy
    who triggered this effect. While , you cannot be Critically Hit or send another
    Mark.
- slot: 1st Ability
  name: Ricochet
  cooldown:
  - 10.0
  - 9.5
  - 9.0
  - 8.5
  - 8.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Marked enemies who are hit are Stunned
  - Ricochet bounces an additional time if you have 400 or more Intelligence
  - This ability passes through and damages all enemies, but bounces off walls
  - 'Damage: 95 | 145 | 195 | 245 | 295'
  - 'Damage Scaling: 70% Strength + 55% Intelligence'
  - 'Bonus Damage: +40% Per Ricochet'
  - 'Stun Duration: 1 second'
  - 'Range: 11.2 meters'
  - 'Radius: 0.48 meters'
  - 'Cooldown: 10 | 9.5 | 9 | 8.5 | 8 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: 'bounces an additional time if you have 400 or more Intelligence Fire
    an arrow that ricochets off walls, dealing Physical Damage to enemies it passes
    through. Deals increasing Physical Damage with each ricochet Bonus Damage: +40%
    Per'
- slot: 2nd Ability
  name: Mark of the Golden Crow
  cooldown:
  - 14.0
  cost:
  - 50.0
  details:
  - Ricochet Stuns Marked enemies
  - Divebomb Knocks Away Marked enemies
  - Sunbreaker Slows Marked enemies more
  - 'Bonus Damage: 0 | 2 | 3 | 4 | 5 | 6% for every 10% Missing Health'
  - 'Bonus Stun Duration: 0 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 seconds'
  - 'Bonus Knockback: 0 | 25 | 30 | 35 | 40 | 45%'
  - 'Bonus Slow Duration: 0 | 0.3 | 0.35 | 0.4 | 0.45 | 0.5 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 1.6 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 50 mana'
  description: Mark an enemy causing your other abilities to apply additional effects.
    While Strength is higher than Intelligence, Marked enemies take bonus Physical
    Damage based on their missing health. While Intelligence is higher than Strength,
    Marked additional effects are amplified
- slot: 3rd Ability
  name: Divebomb
  cooldown:
  - 17.0
  - 16.5
  - 16.0
  - 15.5
  - 15.0
  cost:
  - 70.0
  details:
  - Marked enemies who are hit are Knocked Away
  - You can stay in the air for 1.5 seconds before selecting a landing location
  - You can move freely while in the air, but are Slowed
  - 'Damage: 70 | 110 | 150 | 190 | 230'
  - 'Damage Scaling: 60% Strength + 40% Intelligence'
  - 'Range: 7.2 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 17 | 16.5 | 16 | 15.5 | 15 seconds'
  - 'Cost: 70 mana'
  description: Leap into the air before selecting a location to dive onto, dealing
    Physical Damage to enemies where you land
- slot: Ultimate
  name: Sunbreaker
  cooldown:
  - 90.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Marked enemies are more heavily Slowed
  - 'Damage: 80 | 90 | 100 | 110 | 120'
  - 'Damage Scaling: 25% Strength + 15% Intelligence'
  - 'Slow: 20%'
  - 'Mark Slow: 40%'
  - Slow Duration:0.5 seconds
  - 'Range: 8.8 meters'
  - 'Radius: 4.8 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Shoot down 9 suns every 0.5 seconds onto a target area, dealing Physical
    Damage and Slowing enemies hit. The first sun stays, acting as a wall that Ricochet
    can bounce off of
aspects:
- name: Aspect of the Mark
  kit_changes: Attacks now ricochet, dealing bonus damage to gods per bounce. Bounced
    Attacks cannot damage structures. Ricochet no longer bounces or stuns; it applies
    Mark of the Golden Crow on its first hit. If already marked, the mark spreads.
    Attacks hitting marked targets bounce to a nearby enemy.
source_url: https://wiki.smite2.com/w/Hou_Yi
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Hou Yi Basic Attack
- Suntouched
- Ricochet
- Mark of the Golden Crow
- Divebomb
- Sunbreaker
<!-- WIKI:END -->
