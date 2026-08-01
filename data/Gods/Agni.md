---
type: smite-god
name: Agni
pantheon: Hindu
role: Mid
specializations:
- Nuker
- Burst Damage
- Sniper
damage_type: magical
release_date: January 7, 2025
base_stats:
  health:
    base: 569.48
    per_level: 86.48
  mana:
    base: 334.1
    per_level: 42.0
  physical_prot:
    base: 17.48
    per_level: 2.76
  magical_prot:
    base: 27.38
    per_level: 1.38
  attack_speed:
    base: 1.0
    per_level: 1.51
  move_speed:
    base: 370.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Agni Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Fire a projectile that deals Magical Damage to the first enemy hit
- slot: Passive
  name: Combustion
  details:
  - 'Damage: 5'
  - 'Damage Scaling: 6% Intelligence'
  - 'Debuff Duration: 3 seconds'
  - 'Hot Streak Duration: 10 seconds'
  description: ATTACK TO BURN Hitting an enemy with a Basic Attack provides 1 stack
    of . Hitting an enemy god provides 2. At 4 stacks Agni's next Flame Wave or Rain
    Fire will ignite all enemies hit, dealing Magical Damage every 0.5 seconds for
    3 seconds. When Agni kills an enemy god, he goes on a Hot Streak. When on a Hot
    Streak, is fully charged and using Flame Wave or Rain Fire does not consume
- slot: 1st Ability
  name: Noxious Fumes
  cooldown:
  - 13.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Reduces enemy Healing
  - Fumes last for 10 seconds
  - 'Damage: 10 | 20 | 30 | 40 | 50'
  - 'Damage Scaling: 5% Intelligence'
  - 'Explode Damage: 20 | 40 | 60 | 80 | 100'
  - 'Explode Damage Scaling: 20% Intelligence'
  - 'Stun Duration: 0.8 seconds'
  - 'Healing Reduction: -25%'
  - 'Healing Reduction Duration: 5 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 13 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Summon a cloud of noxious fumes which deals Magical Damage every second.
    Hitting the fumes with any of your other abilities detonates the gas, Stunning
    and dealing Magical Damage to enemies in the area
- slot: 2nd Ability
  name: Flame Wave
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
  - Ignites Noxious Fumes
  - Persists for 1 second after reaching max distance
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage: 100 | 155 | 210 | 265 | 320'
  - 'Damage Scaling: 65% Intelligence'
  - 'Range: 8 meters'
  - 'Radius: 2.59 meters'
  - 'Cooldown: 15 | 14.5 | 14 | 13.5 | 13 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Summon a wave of fire, dealing Magical Damage
- slot: 3rd Ability
  name: Path of Flames
  cooldown:
  - 16.0
  cost:
  - 70.0
  - 75.0
  - 80.0
  - 85.0
  - 90.0
  details:
  - Ignites Noxious Fumes
  - You are Displacement Immune while Dashing
  - Flame trail lasts for 3 seconds
  - Enemies that are being damaged and touch the area again have their damage duration
    refreshed
  - Damage 20 | 30 | 40 | 50 | 60
  - 'Damage Scaling: 15% Intelligence'
  - 'Range: 9.6 meters'
  - 'Radius: 0.8 meters'
  - 'Cooldown: 16 seconds'
  - 'Cost: 70 | 75 | 80 | 85 | 90 mana'
  description: Dash forward and leave a trail of fire behind you. Enemies that enter
    the area take Magical Damage every 0.5 seconds for 2 seconds
- slot: Ultimate
  name: Rain Fire
  cooldown:
  - 18.0
  cost:
  - 10.0
  details:
  - Ignites Noxious Fumes
  - You are Slowed while summoning a meteor
  - 'Damage: 115 | 160 | 205 | 250 | 295'
  - 'Damage Scaling: 60% Intelligence'
  - 'Self Slow: 50%'
  - 'Range: 10.4 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 18 seconds'
  - 'Cost: 10 mana'
  description: Summon a meteor, dealing Magical Damage . You can have up to 3 charges
    of this ability
aspects:
- name: Aspect of Combustion
  kit_changes: Your Basic Attacks now ignite enemies dealing damage over time and
    stacking 5 times. Flame Wave and Rain of Fire consume ignites dealing a burst
    of damage. Rain of Fire deals reduced damage.
source_url: https://wiki.smite2.com/w/Agni
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Agni Basic Attack
- Combustion
- Noxious Fumes
- Flame Wave
- Path of Flames
- Rain Fire
<!-- WIKI:END -->
