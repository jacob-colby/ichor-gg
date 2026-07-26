---
type: smite-god
name: Cupid
pantheon: Roman
role: Carry
specializations:
- Nuker
- Area Control
- Healing
damage_type: physical
release_date: November 25, 2024
base_stats:
  health:
    base: 569.48
    per_level: 86.48
  mana:
    base: 296.0
    per_level: 42.0
  physical_prot:
    base: 18.76
    per_level: 2.76
  magical_prot:
    base: 25.3
    per_level: 1.38
  attack_speed:
    base: 1.0
    per_level: 1.61
  move_speed:
    base: 375.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Cupid Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Fire a projectile that deals Physical Damage to the first enemy hit
- slot: Passive
  name: Lovestruck
  details:
  - Heart Bomb, Share the Love, and Fields of Love always consume up to 8 stacks on
    use, granting them additional Damage, Healing, and bonus effects
  - 'Damage Increase: 2% Per Stack'
  - 'Heal Increase: 2% Per Stack'
  - 'Max Stacks: 16'
  description: Heart Bomb, Share the Love, and Fields of Love always consume up to
    8 stacks on use, granting them additional Damage , Healing , and bonus effects
    Hitting a Basic Attack grants a stack, or 2 stacks if the target is an enemy god
- slot: 1st Ability
  name: Heart Bomb
  cooldown:
  - 12.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - After 3 seconds, the enemy's heart explodes, dealing Physical Damage to all enemies
    within the radius
  - If you have 8 stacks of Lovestruck, all enemies in the explosion area are Stunned
  - Deals additional damage to minions
  - This ability stops on first target hit, and does not pass through walls
  - 'Initial Damage: 50 | 80 | 110 | 140 | 170'
  - 'Initial Damage Scaling: 80% Strength + 55% Intelligence'
  - 'Explosion Damage: 60 | 90 | 120 | 150 | 180'
  - 'Explosion Damage Scaling: 80% Strength + 55% Intelligence'
  - 'Minion Bonus Damage: 60%'
  - 'Slow: 20%'
  - 'Stun Duration: 0.8 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  - 'Explosion Radius: 4 meters'
  - 'Cooldown: 12 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Fire an Arrow of Love, dealing Physical Damage to the first enemy hit
    and Slowing them
- slot: 2nd Ability
  name: Share the Love
  cooldown:
  - 13.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - When the bomb explodes, 3 hearts spawn around the detonation location, Healing,
    Restoring Mana, and granting Attack Speed up to 3 stacks to any ally that picks
    them up
  - If you have 8 stacks of Lovestruck, the hearts also provide a temporary Strength
    and Intelligence Buff
  - The hearts persist for 8 seconds
  - When you or an ally pick up a heart, gain a stack of Lovestruck
  - If an ally picks up the heart, you Heal for 60% of the value and also Restore
    Mana
  - 'Damage: 65 | 115 | 165 | 215 | 265'
  - 'Damage Scaling: 65% Strength + 35% Intelligence'
  - 'Heal: 15 | 25 | 35 | 45 | 55'
  - 'Heal Scaling: 3.5% Intelligence'
  - 'Mana Restore: 20 | 25 | 30 | 35 | 40'
  - 'Mana Restore Scaling: 5% Intelligence'
  - 'Attack Speed: 10% Per Stack'
  - 'Strength: 5 | 10 | 15 | 20 | 25'
  - 'Strength Scaling: 10% Strength'
  - 'Intelligence: 5 | 10 | 15 | 20 | 25'
  - 'Intelligence Scaling: 5% Intelligence'
  - 'Buff Duration: 5 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 1.6 meters'
  - 'Cooldown: 13 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: When the bomb explodes, 3 hearts spawn around the detonation location,
    Healing , Restoring Mana , and granting Attack Speed up to 3 stacks to any ally
    that picks them up Lob an explosive bomb at a location that detonates after 0.75
    seconds, dealing Physical Damage to all enemies hit
- slot: 3rd Ability
  name: Flutter
  cooldown:
  - 16.0
  - 15.0
  - 14.0
  - 13.0
  - 12.0
  cost:
  - 70.0
  details:
  - You also gain Attack Speed after dashing, which is active for the same duration
    as the trail and stacks with the trail's buff
  - 'Attack Speed: 10 | 12.5 | 15 | 17.5 | 20%'
  - 'Movement Speed: 30%'
  - 'Lifetime: 6 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 2.59 meters'
  - 'Cooldown: 16 | 15 | 14 | 13 | 12 seconds'
  - 'Cost: 70 mana'
  description: Dash forward quickly, leaving behind a trail that increases all allies'
    Attack Speed and Movement Speed
- slot: Ultimate
  name: Fields of Love
  cooldown:
  - 100.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - The arrows grow for 2 seconds before exploding, dealing Physical Damage and Mesmerizing
    all enemies inside the area, while Healing all allies
  - If you have 8 stacks of Lovestruck, enemies are Stunned instead of Mesmerized
  - 'Damage: 200 | 280 | 360 | 440 | 520'
  - 'Damage Scaling: 100% Strength + 75% Intelligence'
  - 'Heal: 60 | 75 | 90 | 105 | 120'
  - 'Heal Scaling: 12.5% Intelligence'
  - 'Slow: 30%'
  - 'Mesmerize Duration: 1 second'
  - 'Stun Duration: 1 second'
  - 'Range: 8.8 meters'
  - 'Radius: 5.6 meters'
  - 'Cooldown: 100 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Fire a volley of arrows in an area, Slowing and Crippling all enemies
    inside
aspects:
- name: Aspect of Love
  kit_changes: Heart Bomb's damage is decreased but the enemy hit has reduced Attack
    Speed and the explosion area heals allies. At 8 stacks of Lovestruck, allies also
    gain a Health Shield.
source_url: https://wiki.smite2.com/w/Cupid
last_verified: '2026-07-25'
---
<!-- WIKI:START -->
- Cupid Basic Attack
- Lovestruck
- Heart Bomb
- Share the Love
- Flutter
- Fields of Love
<!-- WIKI:END -->
