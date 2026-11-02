---
type: smite-god
name: Chronos
pantheon: Greek
role: Mid Carry
specializations:
- Constant Damage
damage_type: magical
release_date: June 30, 2026
base_stats:
  health:
    base: 577.0
    per_level: 94.0
  mana:
    base: 316.0
    per_level: 42.0
  physical_prot:
    base: 17.5
    per_level: 2.76
  magical_prot:
    base: 27.4
    per_level: 1.38
  attack_speed:
    base: 0.98
    per_level: 1.51
  move_speed:
    base: 375.0
    per_level: 0.0
  attack_power:
    base: 44.0
    per_level: 2.21
  health_regen:
    base: 1.82
    per_level: 0.2
  mana_regen:
    base: 1.57
    per_level: 0.14
abilities:
- slot: Basic Attack
  name: Chronos Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Fire a projectile that deals Magical Damage to the first enemy hit
  damage_type: magical
  detail_kinds:
  - null
  - magical
  - mechanic
  - mechanic
- slot: Passive
  name: Time Lord
  details:
  - You gain 1 stack every 1.5 minutes
  - Grants up to 125 Intelligence after 37.5 minutes.
  - 'Intelligence: 5 Per Stack'
  - 'Max Stacks: 25'
  description: You become empowered as time flows around you. Over time you gain stacks
    that grant Intelligence . Stacks have a maximum and are permanent
  detail_kinds:
  - null
  - null
  - buff
  - buff
- slot: 1st Ability
  name: Time Rift
  cooldown:
  - 5.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - Hitting a god permanently increases Time Rift damage by 1
  - 'Damage: 80 | 125 | 170 | 215 | 260'
  - 'Damage Scaling: 80% Intelligence'
  - 'Range: 8.8 meters'
  - 'Radius: 1.6 meters'
  - 'Cooldown: 5 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Hitting a god permanently increases damage by 1 Create a rift in time
    that deals Magical Damage to all enemies in the area
  damage_type: magical
  detail_kinds:
  - null
  - magical
  - magical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 2nd Ability
  name: Accelerate
  cooldown:
  - 12.0
  cost:
  - 60.0
  details:
  - 'Section 1: Heal based on your max Health per second'
  - 'Section 2: Abilities cost no Mana'
  - 'Section 3: Increased Intelligence'
  - 'Section 4: Increased Intelligence contribution to your Attacks'
  - You gain bonus Movement Speed every 1 second while Accelerate is active
  - Every 4 uses of Accelerate permanently grants Chronos Intelligence and Attack
    Speed
  - 'Initial Movement Speed: 10%'
  - 'Additional Movement Speed Over Time: 12 | 14 | 16 | 18 | 20%'
  - 'Attack Speed: 25 | 27.5 | 30 | 32.5 | 35%'
  - 'Heal: 1% Max Health'
  - 'Intelligence: 30%'
  - 'Intelligence Attack Contribution: +35%'
  - 'Buff Duration: 7 seconds'
  - 'Permanent Intelligence Per Stack: 2'
  - 'Permanent Attack Speed Per Stack: 0.5%'
  - 'Cooldown: 12 seconds'
  - 'Cost: 60 mana'
  description: You gain bonus Movement Speed every 1 second while is active Every
    4 uses of permanently grants Chronos Intelligence and Attack Speed yourself for
    a duration. You gain Movement Speed (initial plus increasing over time) and Attack
    Speed . While is active, the Wheel of Time stops; the quadrant it stopped on determines
    which bonus you receive
  detail_kinds:
  - heal
  - buff
  - buff
  - buff
  - buff
  - buff
  - buff
  - buff
  - buff
  - heal
  - buff
  - buff
  - buff
  - buff
  - buff
  - mechanic
  - mechanic
- slot: 3rd Ability
  name: Stop Time
  cooldown:
  - 16.0
  - 15.5
  - 15.0
  - 14.5
  - 14.0
  cost:
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  - 85.0
  details:
  - There is a 1 second delay between the initial hit and being Stunned
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage: 50 | 75 | 100 | 125 | 150'
  - 'Damage Scaling: 45% Intelligence'
  - 'Attack Speed Slow: 20%'
  - 'Stun Duration: 1 second'
  - 'Range: 11.2 meters'
  - 'Radius: 1.2 meters'
  - 'Cooldown: 16 | 15.5 | 15 | 14.5 | 14 seconds'
  - 'Cost: 65 | 70 | 75 | 80 | 85 mana'
  description: Fire spinning gears of time forward. Enemies hit have their Attack
    Speed reduced , ramping into a Stun . They take Magical Damage on impact and Magical
    Damage when Stunned
  damage_type: magical
  detail_kinds:
  - stun
  - null
  - magical
  - magical
  - debuff
  - stun
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: Ultimate
  name: Rewind
  cooldown:
  - 100.0
  - 95.0
  - 90.0
  - 85.0
  - 80.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - You are CC Immune for the duration of this ability
  - The Heal is not affected by Healing Reduction
  - 'Time Rewound: 8 seconds'
  - 'Cooldown: 100 | 95 | 90 | 85 | 80 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Teleport through time to a recent position, restoring your Health and
    Mana to their earlier values. All of your Cooldowns are reset instantly
  detail_kinds:
  - mechanic
  - heal
  - mechanic
  - mechanic
  - mechanic
aspects:
- name: Aspect of Relativity
  kit_changes: Time Lord no longer grants Intelligence but instead creates a persistent
    Time Field arond you. Allies in your Time Field gain bonuses when you use your
    other abilities.
source_url: https://wiki.smite2.com/w/Chronos
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Chronos Basic Attack
- Time Lord
- Time Rift
- Accelerate
- Stop Time
- Rewind
<!-- WIKI:END -->
