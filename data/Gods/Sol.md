---
type: smite-god
name: Sol
pantheon: Norse
role: Mid Carry
specializations:
- Sharpshooter
- Nuker
damage_type: magical
release_date: May 30, 2024
base_stats:
  health:
    base: 569.48
    per_level: 86.48
  mana:
    base: 316.32
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
  name: Sol Basic Attack
  details:
  - Successfully hit Attacks generate Heat
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Heat Generated: 5'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Fire a projectile that deals Magical Damage to the first enemy hit
- slot: Passive
  name: Unstable Manifestation
  details:
  - Heat grants increased Strength, Intelligence, and Attack Speed from items
  - At Max Heat, increase your Attack damage
  - Ranges from 0 to 100 Heat
  - Heat starts depleting if you have not generated Heat within the last 6 seconds
  - Heat depletes over time at a rate of 3 Heat per 0.33 seconds
  - 'Strength: 0.15%'
  - 'Intelligence: 0.25%'
  - 'Attack Speed: 0.3%'
  - 'Attack Damage: 15%'
  description: Heat grants increased Strength , Intelligence , and Attack Speed from
    items Hit enemies with Attacks or use abilities to gain Heat
- slot: 1st Ability
  name: Radiance
  cooldown:
  - 10.0
  cost:
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  - 90.0
  details:
  - Enemies in the pool take Magical Damage repeatedly
  - You gain Heat when using this ability
  - Pool size scales from 1x radius at 0 Heat to 2x radius at 100 Heat
  - This ability hits 3 times over 3 seconds
  - This ability Heals 6 times over 5 seconds
  - 'Damage Per Tick: 45 | 70 | 95 | 120 | 145'
  - 'Damage Scaling Per Tick: 30% Intelligence + 15% Strength'
  - 'Heal Per Tick: 2.5% Missing Health'
  - 'Heal Scaling Per Tick: 2% Intelligence'
  - 'Heat Generated: 30 | 40 | 50 | 60 | 70'
  - 'Radius: 2.08 meters'
  - 'Cooldown: 10 seconds'
  - 'Cost: 50 | 60 | 70 | 80 | 90 mana'
  description: Create a pool of flames and Heal yourself over time for a percentage
    of your missing Health
- slot: 2nd Ability
  name: Stellar Burst
  cooldown:
  - 10.0
  cost:
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  - 90.0
  details:
  - Both the explosion and the retraction deal Magical Damage and Slow
  - Can only trigger ability based items and effects
  - This ability stops and explodes on first target hit, on walls, or at max range
  - 'Damage: 45 | 70 | 95 | 120 | 145'
  - 'Damage Scaling: 45% Intelligence + 25% Strength'
  - 'Slow: 25 | 27.5 | 30 | 32.5 | 35%'
  - 'Slow Duration: 1.5 seconds'
  - 'Heat Generated: 10'
  - 'Range: 8.8 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 10 seconds'
  - 'Cost: 50 | 60 | 70 | 80 | 90 mana'
  description: Your next Attack fires a projectile that explodes on hit or upon reaching
    max range, then retracts, and generates Heat
- slot: 3rd Ability
  name: Disapparate
  cooldown:
  - 16.0
  - 15.5
  - 15.0
  - 14.5
  - 14.0
  cost:
  - 60.0
  details:
  - The trail deals Magical Damage every 0.5 seconds
  - After 3 seconds, you become Immune and unable to attack, and the trail detonates
    dealing Magical Damage
  - You can cancel out of the Immune state early
  - This Immune state makes you Damage Immune, Healing Immune, CC Immune, Untargetable,
    and lets you pass through allies, enemies, and Impediments
  - 'Damage Per Tick: 10 | 20 | 30 | 40 | 50'
  - 'Damage Scaling Per Tick: 15% Intelligence'
  - 'Explosion Damage: 60 | 120 | 180 | 240 | 300'
  - 'Explosion Damage Scaling: 75% Intelligence + 40% Strength'
  - 'Movement Speed: 20 | 22.5 | 25 | 27.5 | 30%'
  - 'Buff Duration: 3 seconds'
  - 'Immunity Duration: 3 seconds'
  - 'Heat Generated: 10'
  - 'Radius: 1 meter'
  - 'Cooldown: 16 | 15.5 | 15 | 14.5 | 14 seconds'
  - 'Cost: 60 mana'
  description: This Immune state makes you Damage Immune , Healing Immune , CC Immune
    , Untargetable , and lets you pass through allies, enemies, and Impediments Gain
    Movement Speed and Slow Immunity , gaining Heat and leaving a trail of fire behind
    you
- slot: Ultimate
  name: Supernova
  cooldown:
  - 90.0
  - 85.0
  - 80.0
  - 75.0
  - 70.0
  cost:
  - 100.0
  details:
  - Each strike deals Magical Damage; subsequent hits deal reduced Damage
  - The first time an enemy is hit, they are Knocked Back
  - You are CC Immune while using this ability
  - Areas are selected every 0.18 seconds or when your targeter has moved more than
    1.8 meters since the last area was selected
  - 'Damage: 130 | 175 | 220 | 265 | 310'
  - 'Damage Scaling: 40% Intelligence'
  - 'Subsequent Damage: 30%'
  - 'Heat Generated: 40'
  - 'Range: 8.8 meters'
  - 'Radius: 1.92 meters'
  - 'Cooldown: 90 | 85 | 80 | 75 | 70 seconds'
  - 'Cost: 100 mana'
  description: Each strike deals Magical Damage ; subsequent hits deal reduced Damage
    Unleash flame and fury, gaining Heat and striking 8 times along a moveable ground
    target location
aspects:
- name: Aspect of Conflagration
  kit_changes: Sol's Heat provides Intelligence and Ability Damage, but no longer
    provides Strength, Attack Speed, and Attack Damage. Sol erupts and deals damage
    around her when becomes immune in Disapparate.
source_url: https://wiki.smite2.com/w/Sol
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Sol Basic Attack
- Unstable Manifestation
- Radiance
- Stellar Burst
- Disapparate
- Supernova
<!-- WIKI:END -->
