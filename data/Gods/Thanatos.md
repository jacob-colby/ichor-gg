---
type: smite-god
name: Thanatos
pantheon: Greek
role: Jungle
specializations:
- Slayer
- Execute
- Global
damage_type: physical
release_date: June 27, 2024
base_stats:
  health:
    base: 591.1
    per_level: 108.1
  physical_prot:
    base: 19.0
    per_level: 3.0
  magical_prot:
    base: 27.5
    per_level: 1.5
  attack_speed:
    base: 0.98
    per_level: 1.4
  move_speed:
    base: 380.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Thanatos Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 3 hit chain. Attacks in order of 1, 0.75, 1.5x damage and swing time. The
    final hit cleaves
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Physical Damage to an enemy in front of you
- slot: Passive
  name: Harvester of Souls
  details:
  - Enemy gods at low health are revealed to you
  - Killing an enemy Heals you
  - Killing a god reduces your Cooldowns
  - Your abilities cost Health instead of Mana
  - The Health threshold is determined by the rank of Hovering Death, using the first
    rank value when Hovering Death is unranked
  - 'God Kill Heal: 15% of their Max Health'
  - 'NPC Kill Heal: 10% of their Max Health'
  - 'Cooldown Reduction: -5 seconds'
  description: You revel in the deaths of your foes
- slot: 1st Ability
  name: Death Scythe
  cooldown:
  - 11.0
  cost:
  - 4.0
  details:
  - You Heal for 50% of the total damage done
  - Gods take 12.5% of their Max Health as bonus Physical Damage
  - This ability stops on first target hit, and does not pass through walls
  - 'Damage: 95 | 165 | 235 | 305 | 375'
  - 'Damage Scaling: 85% Strength'
  - 'Slow: 20%'
  - 'Range: 11.2 meters'
  - 'Radius: 0.48 meters'
  - 'Cooldown: 11 seconds'
  - 'Cost: 4% Health'
  description: Fling a scythe projectile that deals Physical Damage and Slows the
    first target hit
- slot: 2nd Ability
  name: Scent of Death
  cooldown:
  - 13.0
  cost:
  - 4.0
  details:
  - You deal bonus damage to and gain bonus Movement Speed when moving towards enemies
    at low health
  - Bonus Movement Speed scales from 0% effectiveness to 100% effectiveness. 0% when
    the target's health is at Execute Threshold and 100% when the target is at 1 health
  - 'Bonus Damage: 15%'
  - 'Movement Speed: 8 | 12 | 16 | 20 | 24%'
  - 'Bonus Movement Speed: Up to 8 | 12 | 16 | 20 | 24%'
  - 'Penetration: 8 | 12 | 16 | 20 | 24'
  - 'Buff Duration: 6 seconds'
  - 'Cooldown: 13 seconds'
  - 'Cost: 4% Health'
  description: Sense death, becoming Slow Immune and gaining Movement Speed and Penetration
- slot: 3rd Ability
  name: Soul Reap
  cooldown:
  - 14.0
  - 13.5
  - 13.0
  - 12.5
  - 12.0
  cost:
  - 4.0
  details:
  - 'Damage: 100 | 150 | 200 | 250 | 300'
  - 'Damage Scaling: 80% Strength'
  - 'Silence Duration: 1 second'
  - 'Radius: 5.6 meters'
  - 'Cone Angle: 110 degrees'
  - 'Cooldown: 14 | 13.5 | 13 | 12.5 | 12 seconds'
  - 'Cost: 4% Health'
  description: CONE SILENCE DAMAGE Swing your scythe, dealing Physical Damage and
    Silencing enemies in front of you
- slot: Ultimate
  name: Hovering Death
  cooldown:
  - 90.0
  cost:
  - 6.0
  details:
  - Enemies at low health are Executed
  - You gain 125% Movement Speed while flying
  - Execute kills enemies even if their death would normally be prevented by other
    god abilities
  - If Thanatos is aiming at an invalid location when the ultimate expires, he will
    land on the last valid aimed location
  - You are CC Immune while using this ability
  - 'Damage: 110 | 145 | 180 | 215 | 250'
  - 'Damage Scaling: 80% Strength'
  - 'Execute Health %: 24 | 28 | 32 | 36 | 40%'
  - 'Stun Duration: 1 second'
  - 'Radius: 2.4 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 6% Health'
  description: Fly into the sky, then dive to a location dealing Physical Damage and
    Stunning enemies hit
aspects:
- name: Aspect of Reaping
  kit_changes: Harvester of Souls no longer Heals Thanatos but provides permanent
    Max Health. Additionally Soul Reap deals bonus damage and Heals Thanatos based
    on his Max Health.
source_url: https://wiki.smite2.com/w/Thanatos
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Thanatos Basic Attack
- Harvester of Souls
- Death Scythe
- Scent of Death
- Soul Reap
- Hovering Death
<!-- WIKI:END -->
