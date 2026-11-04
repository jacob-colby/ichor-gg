---
type: smite-god
name: Nox
pantheon: Roman
role: Mid Support
specializations: []
damage_type: magical
release_date: November 3, 2026
base_stats:
  health:
    base: 569.5
    per_level: 86.48
  health_regen:
    base: 1.7
    per_level: 0.2
  mana:
    base: 320.0
    per_level: 45.37
  mana_regen:
    base: 1.45
    per_level: 0.12
  physical_prot:
    base: 18.8
    per_level: 2.76
  magical_prot:
    base: 27.4
    per_level: 1.38
  attack_speed:
    base: 0.98
    per_level: 1.29
  attack_power:
    base: 36.0
    per_level: 2.42
  move_speed:
    base: 375.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Nox Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  detail_kinds:
  - null
  - magical
  - mechanic
  - mechanic
  damage_type: magical
  description: Fire a projectile that deals Magical Damage to the first enemy hit
- slot: Passive
  name: Flame of the Night
  details:
  - Taking damage from an enemy god blows out a candle, at most once every 3 seconds
  - Intelligence Per Stack +5%
  - Max Stacks 4
  detail_kinds:
  - null
  - buff
  - buff
  description: Each ability you cast lights a candle. Each lit candle increases your
    Intelligence
- slot: 1st Ability
  name: Shadow Lock
  cooldown:
  - 10.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - This is a channeled ability
  - Stay in range to keep the lock. Crowd Control does not break the lock
  - The Root and Cripple ignore Crowd Control Reduction. Cleansing removes them, but
    the damage continues
  - This ability ticks 4 times over 2 seconds
  - This ability passes through and damages non-god enemies, and passes through walls,
    but stops on enemy gods
  - 'Damage Per Tick: 40 | 60 | 75 | 95 | 100'
  - 'Damage Scaling Per Tick: 10% Intelligence'
  - 'Minion Damage: 80 | 125 | 170 | 215 | 260'
  - 'Minion Damage Scaling: 60% Intelligence'
  - 'Root Duration: 2 seconds'
  - 'Cripple Duration: 2 seconds'
  - 'Range: 10.4 meters'
  - 'Lock Break Range: 12.4 meters'
  - 'Cooldown: 10 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  detail_kinds:
  - null
  - null
  - debuff
  - null
  - null
  - magical
  - magical
  - magical
  - magical
  - debuff
  - debuff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Send your shadow forward through walls, dealing Magical Damage to minions
    and jungle monsters it passes. If it hits an enemy god, it stops and you channel,
    Rooting and Crippling them and dealing Magical Damage over time
- slot: 2nd Ability
  name: Siphon Darkness
  cooldown:
  - 13.0
  cost:
  - 70.0
  - 75.0
  - 80.0
  - 85.0
  - 90.0
  details:
  - Cancels the channeled abilities of enemy gods on cast
  - 'Damage: 90 | 160 | 230 | 300 | 370'
  - 'Damage Scaling: 80% Intelligence'
  - 'Exit Damage: 50% of the Explosion Damage'
  - 'Silence Duration: 2 seconds'
  - 'Slow: 30 | 32.5 | 35 | 37.5 | 40%'
  - 'Range: 8.8 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 13 seconds'
  - 'Cost: 70 | 75 | 80 | 85 | 90 mana'
  detail_kinds:
  - null
  - magical
  - magical
  - magical
  - debuff
  - slow
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Create a void of darkness at the target location. After a short delay
    it explodes, dealing Magical Damage and Silencing enemies inside. Enemy gods who
    walk out before it explodes take part of the explosion damage and are Slowed
- slot: 3rd Ability
  name: Shadow Step
  cooldown:
  - 15.0
  cost:
  - 75.0
  details:
  - Cancel the ability to leave the shadow early
  - You are Displacement Immune while Dashing
  - This ability passes through and damages all enemies, but stops on walls and allied
    gods
  - 'Damage: 70 | 110 | 150 | 190 | 230'
  - 'Damage Scaling: 70% Intelligence'
  - 'Shadow Duration: 8 seconds'
  - 'Range: 8.8 meters'
  - 'Explosion Radius: 4 meters'
  - 'Cooldown: 15 seconds'
  - 'Cost: 75 mana'
  detail_kinds:
  - null
  - mechanic
  - null
  - magical
  - magical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Dash forward, dealing Magical Damage to enemies in your path. If you
    hit an allied god, enter their shadow and travel with them. Leaving the shadow
    deals Magical Damage to enemies around you
- slot: Ultimate
  name: Night Terror
  cooldown:
  - 90.0
  - 85.0
  - 80.0
  - 75.0
  - 70.0
  cost:
  - 100.0
  details:
  - You are CC Immune while casting
  - This ability ticks 6 times over 5 seconds
  - This ability passes through and damages non-god enemies, but stops on walls and
    enemy gods
  - 'Damage: 200 | 250 | 300 | 350 | 400'
  - 'Damage Scaling: 40% Intelligence'
  - 'Damage Per Tick: 20 | 25 | 30 | 35 | 40'
  - 'Damage Scaling Per Tick: 10% Intelligence'
  - 'Silence Duration: 1.5 seconds'
  - 'Weaken: -30% Damage Dealt'
  - 'Weaken Duration: 5 seconds'
  - 'Range: 19.2 meters'
  - 'Radius: 3.5 meters'
  - 'Cooldown: 90 | 85 | 80 | 75 | 70 seconds'
  - 'Cost: 100 mana'
  detail_kinds:
  - mechanic
  - null
  - null
  - magical
  - magical
  - magical
  - magical
  - debuff
  - debuff
  - debuff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Fire a vortex of darkness that passes through minions and explodes
    on the first enemy god, jungle boss or Titan it hits, or at max range. Enemies
    in the explosion take Magical Damage , then Magical Damage over time, and are
    Silenced . Enemies hit are Weakened , dealing less damage
aspects:
- name: Aspect of Silent Night
  kit_changes: Coming Soon
source_url: https://wiki.smite2.com/w/Nox
last_verified: '2026-11-04'
---
<!-- WIKI:START -->
- Nox Basic Attack
- Flame of the Night
- Shadow Lock
- Siphon Darkness
- Shadow Step
- Night Terror
<!-- WIKI:END -->
