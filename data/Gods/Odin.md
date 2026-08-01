---
type: smite-god
name: Odin
pantheon: Norse
role: Solo Jungle
specializations:
- Tank
- Shielding
- Mobile
damage_type: physical
release_date: May 2, 2024
base_stats:
  health:
    base: 661.0
    per_level: 94.0
  mana:
    base: 296.0
    per_level: 42.0
  physical_prot:
    base: 20.52
    per_level: 3.24
  magical_prot:
    base: 31.4
    per_level: 1.5
  attack_speed:
    base: 0.98
    per_level: 1.4
  move_speed:
    base: 370.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Odin Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 4 hit chain. Attacks in order of 1, 1, 1, 1.5x damage and swing time
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Physical Damage to an enemy in front of you
- slot: Passive
  name: Path to Valhalla
  details:
  - 'Movement Speed: 4% Per Stack'
  - 'Strength: 10% Per Stack'
  - 'Intelligence: 10% Per Stack'
  - 'Buff Duration: 10 seconds'
  - 'Max Buff Stacks: 2'
  description: GOD DEATHS GRANT POWER When a god dies, gain a brief increase to Movement
    Speed , Strength , and Intelligence
- slot: 1st Ability
  name: Lunge
  cooldown:
  - 14.0
  - 13.5
  - 13.0
  - 12.5
  - 12.0
  cost:
  - 40.0
  - 45.0
  - 50.0
  - 55.0
  - 60.0
  details:
  - If you have a Shield from Raven Shout, it explodes upon landing
  - 'Damage: 120 | 170 | 220 | 270 | 320'
  - 'Damage Scaling: 75% Strength'
  - 'Range: 8.8 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 14 | 13.5 | 13 | 12.5 | 12 seconds'
  - 'Cost: 40 | 45 | 50 | 55 | 60 mana'
  description: Leap forward, dealing Physical Damage to nearby enemies as you land
- slot: 2nd Ability
  name: Raven Shout
  cooldown:
  - 14.0
  - 13.5
  - 13.0
  - 12.5
  - 12.0
  cost:
  - 45.0
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  details:
  - After the duration, the Shield explodes dealing Physical Damage equal to the remaining
    Shield Health to nearby enemies
  - If the Shield is at full HP when it explodes, it deals bonus Physical Damage
  - While the Shield has HP, you deal Physical Damage around you every second
  - 'Pulse Damage: 10 | 15.5 | 21 | 26.5 | 32'
  - 'Pulse Damage Scaling: 4% Strength + 5% Intelligence'
  - 'Shield Health: 100 | 155 | 210 | 265 | 320'
  - 'Shield Health Scaling: 40% Strength + 50% Intelligence'
  - 'Shield Duration: 4 seconds'
  - 'Bonus Physical Damage: 15%'
  - 'Explosion Radius: 3.2 meters'
  - 'Cooldown: 14 | 13.5 | 13 | 12.5 | 12 seconds'
  - 'Cost: 45 | 50 | 55 | 60 | 65 mana'
  description: Gain a Health Shield for a duration
- slot: 3rd Ability
  name: Gungnir's Might
  cooldown:
  - 14.0
  - 13.5
  - 13.0
  - 12.5
  - 12.0
  cost:
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  - 90.0
  details:
  - The pulses Slow
  - The spear deals Physical Damage and Stuns if fired after two pulses. Can only
    Stun the first god Hit
  - If you refire the spear early, nearby allies gain an Attack Speed buff and this
    ability has a 20% reduced cooldown
  - This ability passes through and damages all enemies, but stops on walls
  - 'Pulse Damage: 50 | 80 | 110 | 140 | 170'
  - 'Pulse Damage Scaling: 60% Intelligence'
  - 'Projectile Damage: 60 | 115 | 170 | 225 | 280'
  - 'Projectile Damage Scaling: 75% Strength'
  - 'Stun Duration: 0.9 seconds'
  - 'Attack Speed: 30 | 32.5 | 35 | 37.5 | 40%'
  - 'Buff Duration: 4 seconds'
  - 'Pulse Radius: 3.2 meters'
  - 'Projectile Range: 8.8 meters'
  - 'Projectile Radius: 0.48 meters'
  - 'Cooldown: 14 | 13.5 | 13 | 12.5 | 12 seconds'
  - 'Cost: 50 | 60 | 70 | 80 | 90 mana'
  description: Charge up, pulsing Physical Damage around you twice, then throw your
    spear
- slot: Ultimate
  name: Ring of Spears
  cooldown:
  - 100.0
  - 95.0
  - 90.0
  - 85.0
  - 80.0
  cost:
  - 100.0
  details:
  - Enemies in the area cannot Heal, and have reduced Strength and Intelligence
  - Enemies who leave the area take Physical Damage and are Slowed, unless exiting
    through a segment of the ring destroyed by Attacks
  - Ring of Spears does not block ally movement or projectiles, only enemy Attacks
    and enemy god movement
  - The Ring is made of 8 Segments that each have 5 Hit Points, an enemy Attack will
    deal 1 Hit Point per hit
  - You are Slow and Root Immune while in the Ring
  - 'Damage: 120 | 190 | 260 | 330 | 400'
  - 'Damage Scaling: 75% Strength'
  - 'Strength and Intelligence Debuff: -15 | -17.5 | -20 | -22.5 | -25%'
  - 'Slow: 25%'
  - 'Slow Duration: 5 seconds'
  - 'Permanent Strength Buff: 5 Per Stack'
  - 'Permanent Intelligence Buff: 8 Per Stack'
  - 'Max Stacks: 10'
  - 'Radius: 4.8 meters'
  - 'Cooldown: 100 | 95 | 90 | 85 | 80 seconds'
  - 'Cost: 100 mana'
  description: Enemies in the area cannot Heal , and have reduced Strength and Intelligence
    Enemies who leave the area take Physical Damage and are Slowed , unless exiting
    through a segment of the ring destroyed by Attacks does not block ally movement
    or projectiles, only enemy Attacks and enemy god movement Create a spear ring
    of walls that impedes enemies. Enemy gods who die in the ring grant Odin a permanent
    Strength and Intelligence buff . Gain a stack of Path to Valhalla
aspects: []
source_url: https://wiki.smite2.com/w/Odin
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Odin Basic Attack
- Path to Valhalla
- Lunge
- Raven Shout
- Gungnir's Might
- Ring of Spears
<!-- WIKI:END -->
