---
type: smite-god
name: Ishtar
pantheon: Babylonian
role: Carry
specializations:
- Sharpshooter
- Constant Damage
damage_type: physical
release_date: April 21, 2026
base_stats:
  health:
    base: 611.5
    per_level: 86.48
  mana:
    base: 276.0
    per_level: 42.0
  physical_prot:
    base: 18.8
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
  name: Ishtar Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Fire a projectile that deals Physical Damage to the first enemy hit
- slot: Passive
  name: Mark of Vengeance
  cooldown:
  - 20.0
  details:
  - Each Attack against the marked god grants stacking Attack Speed
  - Securing a Kill or Assist on the marked god grants Movement Speed and permanent
    Strength
  - 'Attack Speed: 5% per stack'
  - 'Movement Speed: 20%'
  - 'Strength: 5 per stack'
  - 'Attack Speed Duration: 4 seconds'
  - 'Movement Speed Duration: 5 seconds'
  - 'Max Attack Speed Stacks: 6'
  - 'Max Strength Stacks: 5'
  - 'Cooldown: 20 seconds'
  description: When you drop below 75% Health, apply to the enemy god that most recently
    damaged you for 10 seconds
- slot: 1st Ability
  name: Imbue Arrows
  cooldown:
  - 12.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - 'Strike Shot: Lob explosions that deal bonus Physical Damage in an area; may fire
    over walls'
  - 'Spread Shot: Fire 5 arrows in a cone, side arrows deal reduced Physical Damage;
    only the center arrow applies on-hit item effects'
  - 'Storm Shot: Gain Attack Speed and fire faster, longer-ranged shots that deal
    reduced Physical Damage. These Attacks cannot hit structures'
  - Empowered Attacks do not damage player-made deployables or wards
  - 'Strike Shot Bonus Damage: 5 | 11 | 17 | 23 | 29'
  - 'Spread Shot Side Arrow Damage: 9%'
  - 'Storm Shot Attack Speed Bonus: 20 | 25 | 30 | 35 | 40%'
  - 'Storm Shot Projectile Speed: 120%'
  - 'Buff Duration: 6 seconds'
  - 'Storm Shot Attack Damage: -20%'
  - 'Strike Shot Range: 7.52 meters'
  - 'Strike Shot Radius: 1.6 meters'
  - 'Storm Shot Range: 12.8 meters'
  - 'Cooldown: 12 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: 'Spread Shot: Fire 5 arrows in a cone, side arrows deal reduced Physical
    Damage ; only the center arrow applies on-hit item effects Storm Shot: Gain Attack
    Speed and fire faster, longer-ranged shots that deal reduced Physical Damage .
    These Attacks cannot hit structures Imbue your arrows with heavenly light, empowering
    your Attacks as Strike Shot, Spread Shot, or Storm Shot'
- slot: 2nd Ability
  name: Rolling Thunder
  cooldown:
  - 13.5
  cost:
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  details:
  - Enemies hit by more than 1 strike are Mesmerized
  - 'Damage: 60 | 85 | 110 | 135 | 160'
  - 'Damage Scaling: 40% Strength'
  - 'Mesmerize Duration: 0.75 seconds'
  - 'Range: 2.4 meters'
  - 'Radius: 8.8 meters'
  - 'Cooldown: 13.5 seconds'
  - 'Cost: 55 | 60 | 65 | 70 | 75 mana'
  description: Call down four lightning strikes in a line, dealing Physical Damage
    per strike to enemies in each area. Ishtar may aim which direction the strikes
    travel
- slot: 3rd Ability
  name: Jolt
  cooldown:
  - 15.0
  - 14.5
  - 14.0
  - 13.5
  - 13.0
  cost:
  - 60.0
  details:
  - Hitting an enemy god Roots them as you Leap backwards and loose an arrow that
    deals Physical Damage in an area around them
  - The arrow from this ability can Critically Strike and trigger on-hit item effects
  - 'Dash Damage: 80 | 120 | 160 | 200 | 240'
  - 'Dash Damage Scaling: 60% Strength'
  - 'Arrow Damage: 20 | 30 | 40 | 50 | 60'
  - 'Arrow Damage Scaling: 120% Basic Attack Damage'
  - 'Range: 2.4 meters'
  - 'Arrow Radius: 1.6 meters'
  - 'Cooldown: 15 | 14.5 | 14 | 13.5 | 13 seconds'
  - 'Cost: 60 mana'
  description: Dash forward with your blades, dealing Physical Damage to enemies in
    your path
- slot: Ultimate
  name: Blades of Retribution
  cooldown:
  - 90.0
  cost:
  - 100.0
  details:
  - Refire within 3 seconds to recall the swords towards you
  - Enemies hit by both the outgoing volley and the recall are Stunned
  - Each sword hit after the first on the same target deals reduced Physical Damage;
    the reduction resets before the recall
  - 'Damage: 90 | 115 | 140 | 165 | 190'
  - 'Damage Scaling: 55% Strength'
  - 'Damage Reduction: -40% per sword, up to a max of -80%'
  - 'Cripple Duration: 1.25 seconds'
  - 'Stun Duration: 1 second'
  - 'Range: 12.8 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 100 mana'
  description: Each sword hit after the first on the same target deals reduced Physical
    Damage ; the reduction resets before the recall Become CC Immune and summon five
    swords of light, firing them out in a cone. Each sword deals Physical Damage and
    Cripples enemies
aspects:
- name: Aspect of the Passionate Storm
  kit_changes: Your Spread Shot cone is always active on your Attacks. Imbue Arrows
    no longer changes stance; it grants Attack Speed and lets you build Storm's Kiss
    whenever you hit a target with an Attack while Imbue is active. Rolling Thunder
    now grans you small Movement Speed bonus per strike. Jolt consumes Storm's Kiss
    stacks on hit; at 8 or more stacks, the arrow you fire after the backflip deals
    bonus damage, and at 15 or more stacks the Rooted target explodes for bonus Physical
    Damage over double the area when you land.
source_url: https://wiki.smite2.com/w/Ishtar
last_verified: '2026-07-25'
---
<!-- WIKI:START -->
- Ishtar Basic Attack
- Mark of Vengeance
- Imbue Arrows
- Rolling Thunder
- Jolt
- Blades of Retribution
<!-- WIKI:END -->
