---
type: smite-god
name: Loki
pantheon: Norse
role: Jungle
specializations:
- Slayer
- Stealth
damage_type: physical
release_date: May 2, 2024
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
  name: Loki Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 5 hit chain. Attacks in order of 1, 0.5, 0.5, 0.5, 1.5x damage and swing
    time
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Physical Damage to an enemy in front of you
- slot: Passive
  name: Behind You
  details:
  - The increased damage from this effect also triggers on enemies Blinded by Agonizing
    Visions
  - 'Damage: 115%'
  description: Hitting enemies from behind deals Bonus Damage
- slot: 1st Ability
  name: Vanish
  cooldown:
  - 15.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Your next Attack deals additional Physical Damage over time
  - Hits 4 times over 2 seconds
  - Killing a god resets the cooldown of this ability
  - You are Slow Immune while Stealthed
  - Stealthed gods are invisible to enemies unless they enter an enemy structure's
    attack area
  - Taking damage while in Stealth partially reveals you for 0.165 seconds
  - Stealth is broken when hit by Hard CC
  - 'Damage Per Tick: 30 | 45 | 60 | 75 | 90'
  - 'Damage Scaling Per Tick: 20% Strength'
  - 'Movement Speed: 35%'
  - 'Buff Duration: 4 seconds'
  - 'Cooldown: 15 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Disappear in a puff of smoke, become Stealthed and gain Movement Speed
- slot: 2nd Ability
  name: Agonizing Visions
  cooldown:
  - 13.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - Damaged enemies have Reduced Damage
  - Enemies hit four times are Blinded
  - This ability hits 8 times over 3.5 seconds
  - Blinded players have their game camera obscured
  - The Vision acts as a wall to enemies only
  - Loki benefits from Behind You on Blinded enemies from all directions
  - 'Damage: 20 | 25 | 30 | 35 | 40'
  - 'Damage Scaling: 15% Strength'
  - 'Blind Duration: 3 seconds'
  - 'Damage Dealt Reduction: 5%'
  - 'Debuff Duration: 2.5 seconds'
  - 'Max Debuff Stacks: 3'
  - 'Range: 8.8 meters'
  - 'Radius: 4 meters'
  - 'Cooldown: 13 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Summon a vision of Loki that repeatedly deals Physical Damage to nearby
    enemies
- slot: 3rd Ability
  name: Flurry Strike
  cooldown:
  - 9.0
  cost:
  - 40.0
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  details:
  - The final hit deals Bonus Physical Damage and applies a stronger Slow
  - This is a Channeled ability
  - You are Displacement Immune while Channeling
  - Hits 6 times over 1.5 seconds
  - Slow is refreshed with each hit but does not stack
  - This ability can benefit from Behind You
  - 'Damage: 20 | 30 | 40 | 50 | 60'
  - 'Damage Scaling: 25% Strength'
  - 'Final Hit Damage: 55 | 75 | 95 | 115 | 135'
  - 'Final Hit Damage Scaling: 60% Strength'
  - 'Slow: 15%'
  - 'Final Hit Slow: 30%'
  - 'Slow Duration: 2.25 seconds'
  - 'Radius: 3.2 meters'
  - 'Cone Angle: 90 degrees'
  - 'Cooldown: 9 seconds'
  - 'Cost: 40 | 50 | 60 | 70 | 80 mana'
  description: Unleash a flurry of dagger strikes, dealing Physical Damage repeatedly
    and Slowing enemies in front of you
- slot: Ultimate
  name: Assassinate
  cooldown:
  - 90.0
  cost:
  - 90.0
  details:
  - The first strike deals Physical Damage and Cripples enemies in the area
  - The second strike deals Physical Damage and Stuns enemies in front of you
  - Loki locks onto the enemy god closest to the center of the Teleport location,
    if there is one
  - 'First Strike Damage: 70 | 105 | 140 | 175 | 210'
  - 'First Strike Damage Scaling: 35% Strength'
  - 'Second Strike Damage: 100 | 145 | 190 | 235 | 280'
  - 'Second Strike Damage Scaling: 80% Strength'
  - 'Stun Duration: 0.75 seconds'
  - 'Teleport Range: 8.8 meters'
  - 'First Strike Radius: 1.6 meters'
  - 'Second Strike Range: 4.8 meters'
  - 'Second Strike Cone Angle: 105 degrees'
  - 'Cooldown: 90 seconds'
  - 'Cost: 90 mana'
  description: Teleport to the target location, then strike twice to assassinate a
    foe
aspects:
- name: Aspect of Agony
  kit_changes: Vanish no longer grants Stealth, but it inflicts Blind instead of Bleed.
    Agonizing Visions can be cast on allies, providing damage mitigation while slowing
    enemies. Behind you now deals bonus damage scaling with your Health and Protections
    rather than its percentage increase.
source_url: https://wiki.smite2.com/w/Loki
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Loki Basic Attack
- Behind You
- Vanish
- Agonizing Visions
- Flurry Strike
- Assassinate
<!-- WIKI:END -->
