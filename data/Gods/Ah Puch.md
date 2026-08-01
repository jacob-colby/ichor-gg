---
type: smite-god
name: Ah Puch
pantheon: Maya
role: Mid
specializations:
- Nuker
- Burst Damage
- Area Control
damage_type: magical
release_date: May 19, 2026
base_stats:
  health:
    base: 619.0
    per_level: 94.0
  mana:
    base: 320.0
    per_level: 45.37
  physical_prot:
    base: 19.2
    per_level: 3.24
  magical_prot:
    base: 27.7
    per_level: 1.73
  attack_speed:
    base: 0.96
    per_level: 1.4
  move_speed:
    base: 370.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Ah Puch Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Fire a projectile that deals Magical Damage to the first enemy hit
- slot: Passive
  name: Hollow Ground
  details:
  - Enemy gods and the Fire Giant can destroy corpses with 2 Attacks
  - You can have up to 6 corpses; placing more removes the oldest
  - Corpses last up to 45 seconds
  - 'Cooldown Reduction: 1 second'
  - 'Max Health Restore: 3%'
  - 'Max Mana Restore: 3%'
  description: Exhume decaying corpses at will. When you walk over a decaying corpse,
    reduce the Cooldown of Undead Surge and Corpse Explosion , and restore a portion
    of your max Health and Mana
- slot: 1st Ability
  name: Undead Surge
  cooldown:
  - 10.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Reduces enemy Healing
  - Corpses explode on contact, at max range, or when reactivating Undead Surge
  - Corpses collapse after exploding and remain behind
  - This ability stops on first target hit, and does not pass through walls
  - 'Damage: 90 | 110 | 130 | 150 | 170'
  - 'Damage Scaling: 35% Intelligence'
  - 'Slow: 20 | 25 | 30 | 35 | 40%'
  - 'Slow Duration: 2 seconds'
  - 'Healing Reduction: -25%'
  - 'Healing Reduction Duration: 5 seconds'
  - 'Range: 9.6 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 10 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Corpses explode on contact, at max range, or when reactivating Raise
    two decaying corpses from the underworld that surge forward, dealing Magical Damage
    . Enemies hit are Slowed and have Reduced Healing for a duration
- slot: 2nd Ability
  name: Corpse Explosion
  cooldown:
  - 10.0
  cost:
  - 60.0
  details:
  - Any corpses in the area detonate, dealing additional Magical Damage
  - 'Damage: 60 | 70 | 80 | 90 | 100'
  - 'Damage Scaling: 30% Intelligence'
  - 'Corpse Damage: 55 | 80 | 105 | 130 | 155'
  - 'Corpse Damage Scaling: 30% Intelligence'
  - 'Range: 8.8 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 10 seconds'
  - 'Cost: 60 mana'
  description: Cause the target area to explode, dealing Magical Damage Corpse
- slot: 3rd Ability
  name: Fleeting Breath
  cooldown:
  - 10.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Enemies that Heal while affected by miasma take bonus Magical Damage and are Stunned
    at the end of its effect
  - The corpse falls to the ground and remains behind
  - 'Tick Damage: 24 | 32 | 40 | 48 | 56'
  - 'Tick Damage Scaling: 16% Intelligence'
  - 'Bonus Damage: 50 | 100 | 150 | 200 | 250'
  - 'Bonus Damage Scaling: 40% Intelligence'
  - 'Debuff Duration: 4 seconds'
  - 'Stun Duration: 1.5 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 2.08 meters'
  - 'Cooldown: 10 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Throw a charm from the underworld that awakens a decaying corpse, applying
    miasma to enemies in an area, dealing Magical Damage over time
- slot: Ultimate
  name: Empty the Crypts
  cooldown:
  - 110.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Each tick applies stacking Healing Reduction and Damage Dealt Reduction (stacks
    refresh)
  - After casting this ability, your next 3 Attacks also launch zombies that leave
    decaying corpses behind
  - 'Damage Per Tick: 50 | 55 | 60 | 65 | 70'
  - 'Damage Scaling Per Tick: 15% Intelligence'
  - 'Healing Reduction: 25% per stack'
  - 'Damage Dealt Reduction: 3% per stack'
  - 'Debuff Duration: 5 seconds'
  - 'Max Stacks: 3'
  - 'Radius: 16 meters'
  - 'Cooldown: 110 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Unleash a field of spirits at a target location for 6 seconds. Enemies
    inside the field take Magical Damage every 0.5 seconds
aspects:
- name: Aspect of the Death March
  kit_changes: Each decaying corpse you walk over reduces the Cooldown of Fleeting
    Breath instead of the Cooldown of Corpse Explosion. Corpse Explosion becomes Wraith
    Call, which haunts enemy gods dealing bonus damage and significantly debuffing
    targets on ability hits. Empty The Crypts deals less damage per tick but Slows
    haunted enemy gods inside the field.
source_url: https://wiki.smite2.com/w/Ah_Puch
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Ah Puch Basic Attack
- Hollow Ground
- Undead Surge
- Corpse Explosion
- Fleeting Breath
- Empty the Crypts
<!-- WIKI:END -->
