---
type: smite-god
name: Osiris
pantheon: Egyptian
role: Solo
specializations:
- Brawler
- Lockdown
- Constant Damage
damage_type: physical
release_date: October 7, 2025
base_stats:
  health:
    base: 619.0
    per_level: 94.0
  mana:
    base: 299.0
    per_level: 45.37
  physical_prot:
    base: 19.2
    per_level: 3.24
  magical_prot:
    base: 27.5
    per_level: 1.5
  attack_speed:
    base: 1.0
    per_level: 1.61
  move_speed:
    base: 375.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Osiris Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 4 hit chain. Attacks in order of 0.5x, 1x, 0.5x, 1x damage and swing time.
    Attacks 3 and 4 cleave
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Physical Damage to an enemy in front of you
- slot: Passive
  name: Fragmented
  details:
  - 'After losing 8 fragments, become a spirit for 6 successful Attacks: walk through
    enemies and enemy blockers, gain Attack Speed, and your Attacks ignore movement
    penalty'
  - 'Damage Mitigation: 2% Per Missing Fragment'
  - Attack Speed 40%
  description: 'After losing 8 fragments, become a spirit for 6 successful Attacks:
    walk through enemies and enemy blockers , gain Attack Speed , and your Attacks
    ignore movement penalty Lose a fragment of your body each time you use an ability,
    gaining Damage Mitigation'
- slot: 1st Ability
  name: Sickle Strike
  cooldown:
  - 6.0
  cost:
  - 30.0
  details:
  - If a god is hit, the Sickle persists for the Slow duration
  - Deals 75% Physical Damage to minions
  - This ability passes through and damages non-god enemies, but stops on walls and
    enemy gods
  - 'Damage: 80 | 130 | 180 | 230 | 280'
  - 'Damage Scaling: 45% Strength + 35% Protections from Items'
  - 'Slow: 15 | 16.25 | 17.5 | 18.75 | 20%'
  - 'Slow Duration: 3 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 0.56 meters'
  - 'Cooldown: 6 seconds'
  - 'Cost: 30 mana'
  description: Throw your Sickle, dealing Physical Damage and Slowing the first god
    hit
- slot: 2nd Ability
  name: Spirit Flail
  cooldown:
  - 11.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - Enemies affected by Sickle Strike have their Slow increased in power and duration
  - 'Damage: 90 | 145 | 200 | 255 | 310'
  - 'Damage Scaling: 75% Strength + 55% Protections from Items'
  - 'Movement Speed: 20%'
  - 'Buff Duration: 3 seconds'
  - 'Additional Slow: 40%'
  - 'Slow Duration: 3 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 2.4 meters'
  - 'Cooldown: 11 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Strike the target area with your flail, dealing Physical Damage and
    granting Movement Speed
- slot: 3rd Ability
  name: Judgement Tether
  cooldown:
  - 15.0
  - 14.5
  - 14.0
  - 13.5
  - 13.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - The tether breaks if targets move far enough away
  - Targets still in range when the duration expires are Stunned
  - You can not apply tethers through walls, however tethers already attached can
    pass through walls
  - 'Attack Speed Reduction: 15 | 17.5 | 20 | 22.5 | 25%'
  - 'Attack Speed Reduction Scaling: 4% Protections from Items'
  - 'Damage Dealt Reduction: 10 | 12.5 | 15 | 17.5 | 20%'
  - 'Stun Duration: 1.1 seconds'
  - 'Radius: 5.6 meters'
  - 'Cooldown: 15 | 14.5 | 14 | 13.5 | 13 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Tether yourself to nearby enemy gods. Tethered enemies have reduced
    Attack Speed and reduced Damage for 4 seconds
- slot: Ultimate
  name: Lord of the Afterlife
  cooldown:
  - 70.0
  cost:
  - 30.0
  details:
  - 'On Use: Immediately max Fragment Stacks'
  - 'Damage: 250 | 345 | 440 | 535 | 630'
  - 'Damage Scaling: 80% Strength'
  - 'Root Duration: 0.8 seconds'
  - 'Negative Cooldown Rate: -30'
  - 'Debuff Duration: 6 seconds'
  - 'Range: 10.4 meters'
  - 'Radius: 2.4 meters'
  - 'Cooldown: 70 seconds'
  - 'Cost: 30 mana'
  description: Leap to a target location, dealing Physical Damage and Rooting enemies.
    Apply negative Cooldown Reduction and Healing Prevention to enemy gods hit
aspects:
- name: Aspect of the Fragmented
  kit_changes: Osiris' abilities now scale with intelligence only. Fragments are lost
    passively on casts and on ability god hits. Osiris gains % Damage Dealt or Damage
    Mitigated on how whole he is. Sickle Strike has no Cooldown and costs 4 Fragments.
    Spirit Flail consumes Sickle Strike for bonus damage but no slow. Lord of the
    Afterlife summons a slowing, damage-dealing specter, but you can no longer leap
    to a location.
source_url: https://wiki.smite2.com/w/Osiris
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Osiris Basic Attack
- Fragmented
- Sickle Strike
- Spirit Flail
- Judgement Tether
- Lord of the Afterlife
<!-- WIKI:END -->
