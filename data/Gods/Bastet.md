---
type: smite-god
name: Bastet
pantheon: Egyptian
role: Jungle
specializations:
- Slayer
- Mobile
damage_type: physical
release_date: June 16, 2026
base_stats:
  health:
    base: 619.0
    per_level: 94.0
  mana:
    base: 296.0
    per_level: 42.0
  physical_prot:
    base: 18.76
    per_level: 2.76
  magical_prot:
    base: 25.42
    per_level: 1.5
  attack_speed:
    base: 0.98
    per_level: 1.4
  move_speed:
    base: 380.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Bastet Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 3 hit chain. Attacks in order of 1, 0.7, 1.3x damage and swing time
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Physical Damage to an enemy in front of you
- slot: Passive
  name: Nightstalker
  details:
  - You gain bonus Lifesteal against gods than other enemies
  - 'God Lifesteal Buff: 6% + 0.6% Per Level'
  - 'Minion Lifesteal Buff: 6% + 0.15% Per Level'
  - 'Strength Buff: 2 + 0.5 Per Level'
  - 'Max Buff Stacks: 3'
  - 'Buff Duration: 10 seconds'
  - 'Reveal Duration: 6 seconds'
  description: Hitting enemies grants Lifesteal . Hitting enemy gods additionally
    grants stacks of Strength and Reveals them to you for a duration
- slot: 1st Ability
  name: Pounce
  cooldown:
  - 14.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Cancel early to put this ability on Cooldown
  - 'Damage: 95 | 150 | 205 | 260 | 315'
  - 'Damage Scaling: 90% Strength'
  - 'Movement Speed: 25%'
  - 'Range: 8.8 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Leap to a target location, dealing Physical Damage to enemies in the
    area. For a short duration, reactivate to Leap back to your initial location.
    You gain increased Movement Speed while you can return
- slot: 2nd Ability
  name: Razor Whip
  cooldown:
  - 10.0
  cost:
  - 40.0
  - 45.0
  - 50.0
  - 55.0
  - 60.0
  details:
  - 'Damage Per Tick: 40 | 55 | 70 | 85 | 100'
  - 'Damage Scaling Per Tick: 30% Strength'
  - 'Bleed Duration: 2 seconds'
  - 'Range: 5.6 meters'
  - 'Cone Angle: 68 degrees'
  - 'Cooldown: 10 seconds'
  - 'Cost: 40 | 45 | 50 | 55 | 60 mana'
  description: Cone Bleed Swipe at enemies in a cone, causing them to Bleed for Physical
    Damage over time
- slot: 3rd Ability
  name: Ensnaring Claw
  cooldown:
  - 16.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Cat attacks once per second
  - Cat is immune until it hits an enemy or reaches max range
  - 'Damage: 55 | 90 | 125 | 160 | 195'
  - 'Damage Scaling: 60% Strength'
  - 'Cat Attack Damage: 20 | 25 | 30 | 35 | 40'
  - 'Cat Attack Damage Scaling: 30% Strength + 30% Intelligence + 30% Attack Damage'
  - 'Root Duration: 0.5 seconds'
  - 'Slow: 20%'
  - 'Slow Duration: 2 seconds'
  - 'Cat Duration: 4 seconds'
  - 'Range: 11.2 meters'
  - 'Radius: 1.6 meters'
  - 'Cooldown: 16 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Send a cat forward. If it hits an enemy, it Roots them and nearby enemies
    briefly and deals Physical Damage . The cat persists for a duration or until defeated,
    attacking nearby enemies for Physical Damage and applying a Slow
- slot: Ultimate
  name: Cat Call
  cooldown:
  - 90.0
  cost:
  - 90.0
  - 95.0
  - 100.0
  - 105.0
  - 110.0
  details:
  - Cats cannot block movement and cannot attack structures
  - Cats Dash attack bleeding enemies, dealing Physical Damage and Slowing them
  - When you cast Razor Whip, each cat resets its Dash Cooldown and Dashes to the
    first enemy hit
  - When you cast Pounce, cats follow you through the Leap
  - 'Cat Dash Damage: 40 | 65 | 90 | 115 | 140'
  - 'Cat Dash Damage Scaling: 50% Strength'
  - 'Cat Attack Damage: 5 | 10 | 15 | 20 | 25'
  - 'Cat Attack Damage Scaling: 20% Strength'
  - 'Slow: 12 | 14 | 16 | 18 | 20%'
  - 'Slow Duration: 2 seconds'
  - 'Strength Buff: 21 | 27 | 33 | 39 | 45'
  - 'Buff Duration: 10 seconds'
  - 'Cats Dash Range: 3.2 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 90 | 95 | 100 | 105 | 110'
  description: Summon 3 spirit cats that follow you and attack nearby enemies for
    a duration. While they are active, you gain Strength
aspects:
- name: Aspect of the Watchful Pride
  kit_changes: Pounce can no longer be activated again to return to you to your starting
    location; hitting an enemy god with it grants Protections to nearby allies. Razor
    Whip deals less damage but Disarms bleeding enemies. Ensnaring Claw Stuns instead
    of Rooting. Cat Call becomes Huntress of Bast.
source_url: https://wiki.smite2.com/w/Bastet
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Bastet Basic Attack
- Nightstalker
- Pounce
- Razor Whip
- Ensnaring Claw
- Cat Call
<!-- WIKI:END -->
