---
type: smite-god
name: The Morrigan
pantheon: Celtic
role: Mid
specializations:
- Slayer
- Nuker
- Stealth
damage_type: magical
release_date: June 27, 2024
base_stats:
  health:
    base: 569.48
    per_level: 86.48
  mana:
    base: 316.32
    per_level: 42.0
  physical_prot:
    base: 19.0
    per_level: 3.0
  magical_prot:
    base: 27.5
    per_level: 1.5
  attack_speed:
    base: 0.98
    per_level: 1.61
  move_speed:
    base: 375.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: The Morrigan Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - Has a 3 hit chain. Attacks in order of 1, 1, 1x damage and swing time. The final
    swing explodes on target, applying Doomsayer
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  - 'Explosion Radius: 1.6 meters'
  description: 'The Morrigan Notes: Fire a projectile that deals Magical Damage to
    the first enemy hit Damage Scaling : 100% Strength + 20% Intelligence + 100% Attack
    Damage Range : 8.8 meters Radius : 0.48 meters Explosion Radius : 1.6 meters Expand
    Ability Video'
- slot: Passive
  name: Doomsayer
  details:
  - Deals reduced damage against Jungle Bosses and Titans
  - 'Magical Damage: 9% of Enemy''s Health'
  - 'Reduced Damage: -80% damage'
  description: 'EXPLODING, BURNING THIRD ATTACK Notes: The third hit of your Attack
    Chain explodes, dealing Magical Damage over 3 seconds Magical Damage : 9% of Enemy''s
    Health Reduced Damage : -80% damage Expand Ability Video'
- slot: 1st Ability
  name: Deadly Aspects
  cooldown:
  - 12.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - The buildup for this ability does not break Confusion's Stealth
  - 'Damage: 105 | 160 | 215 | 270 | 325'
  - 'Damage Scaling: 90% Intelligence'
  - 'Stun Duration: 0.8 seconds'
  - 'Range: 4.8 meters'
  - 'Cone Angle: 45 degrees'
  - 'Cooldown: 12 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: 'CONE STUN DAMAGE Notes: Summon the power from all 3 of your forms,
    then activate again to deal Magical Damage and Stun enemies in front of you Damage
    : 105 | 160 | 215 | 270 | 325 Damage Scaling : 90% Intelligence Stun Duration
    : 0.8 seconds Range : 4.8 meters Cone Angle : 45 degrees Cooldown : 12 seconds
    Cost : 60 | 65 | 70 | 75 | 80 mana Expand Ability Video'
- slot: 2nd Ability
  name: Dark Omen
  cooldown:
  - 7.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - The mark deals bonus Magical Damage when that god is damaged by any god ability
    or Doomsayer
  - This ability passes through and damages all enemies, and passes through walls
  - 'Initial Damage: 55 | 85 | 115 | 145 | 175'
  - 'Initial Damage Scaling: 55% Intelligence'
  - 'Mark Damage: 55 | 85 | 115 | 145 | 175'
  - 'Mark Damage Scaling: 55% Intelligence'
  - 'Minion Damage: 65 | 125 | 185 | 245 | 305'
  - 'Minion Damage Scaling: 60% Intelligence'
  - 'Range: 11.2 meters'
  - 'Radius: 0.8 meters'
  - 'Cooldown: 7 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: 'PROJECTILE DAMAGE, MARKS Notes: Fire a wave of dark magic, dealing
    Magical Damage and marking enemies Initial Damage : 55 | 85 | 115 | 145 | 175
    Initial Damage Scaling : 55% Intelligence Mark Damage : 55 | 85 | 115 | 145 |
    175 Mark Damage Scaling : 55% Intelligence Minion Damage : 65 | 125 | 185 | 245
    | 305 Minion Damage Scaling : 60% Intelligence Range : 11.2 meters Radius : 0.8
    meters Cooldown : 7 seconds Cost : 60 | 65 | 70 | 75 | 80 mana Expand Ability
    Video'
- slot: 3rd Ability
  name: Confusion
  cooldown:
  - 15.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - The clone will walk to your target location
  - When the clone is damaged, it will appear as an illusion, changing appearance
    and losing its health bar
  - The clone grants vision around itself
  - Taking damage while stealthed breaks the effect
  - 'Movement Speed: 30 | 32.5 | 35 | 37.5 | 40%'
  - 'Buff Duration: 3 | 3.5 | 4 | 4.5 | 5 seconds'
  - 'Clone Lifetime: 10 seconds'
  - 'Cooldown: 15 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: 'STEALTH, CREATE DECOY Notes: Create a phantom clone of yourself and
    become Stealthed and gain Movement Speed Movement Speed : 30 | 32.5 | 35 | 37.5
    | 40% Buff Duration : 3 | 3.5 | 4 | 4.5 | 5 seconds Clone Lifetime : 10 seconds
    Cooldown : 15 seconds Cost : 60 | 65 | 70 | 75 | 80 mana Expand Ability Video'
- slot: Ultimate
  name: Changeling
  cooldown:
  - 120.0
  - 115.0
  - 110.0
  - 105.0
  - 100.0
  cost:
  - 100.0
  details:
  - If the god you transform into has an Ultimate Cooldown longer than this Ultimate's
    Cooldown, use the transformed target's Cooldown instead
  - You will copy all their abilities and items, all with no active Cooldowns
  - You will copy their ability ranks. If your level is different to the transform
    target's it will use the order they ranked their abilities, filling with Auto
    Skill as needed
  - If you are in the middle of firing an ability when the transformation times out,
    you will detransform the moment that ability fire ends
  - 'Cooldown: 120 | 115 | 110 | 105 | 100 seconds'
  - 'Cost: 100 mana'
  description: 'BECOME A DIFFERENT GOD Notes: If the god you transform into has an
    Cooldown longer than this ''s Cooldown, use the transformed target''s Cooldown
    instead Select a god in the current match to transform into an exact copy of.
    Gain access to their abilities and items for 10 seconds Cooldown : 120 | 115 |
    110 | 105 | 100 seconds Cost : 100 mana Expand Ability Video'
aspects:
- name: Aspect of Mischief
  kit_changes: Confusion no longer Stealths you but on refire, you swap positions
    with your clone.
source_url: https://wiki.smite2.com/w/The_Morrigan
last_verified: '2026-07-23'
---
<!-- WIKI:START -->
- The Morrigan Basic Attack
- Doomsayer
- Deadly Aspects
- Dark Omen
- Confusion
- Changeling
<!-- WIKI:END -->
