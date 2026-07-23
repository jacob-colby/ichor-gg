---
type: smite-god
name: Guan Yu
pantheon: Chinese
role: Solo Support
specializations:
- Brawler
- Healing
- Pressure
damage_type: physical
release_date: May 5, 2025
base_stats:
  health:
    base: 661.0
    per_level: 94.0
  mana:
    base: 334.1
    per_level: 42.0
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
    base: 375.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Guan Yu Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 4 hit chain. Attacks in order of 1, 1, 1.3, 1.75x damage and swing time.
    The third hit cleaves
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: 'Guan Yu Notes: Deal Physical Damage to an enemy in front of you Damage
    Scaling : 100% Strength + 20% Intelligence + 100% Attack Damage Range : 1.92 meters
    Cone Angle : 120 degrees Expand Ability Video'
- slot: Passive
  name: Battle Fervor
  details:
  - Fervor provides Attack Speed per stack
  - At maximum stacks it provides more Attack Speed
  - Gain 1 stack when Attacking a minion, and 3 stacks when Attacking an enemy god
  - Abilities gain 1 stack per tick of damage
  - Dealing damage resets the max stacks buff duration
  - Despite the description, taking damage does not provide stacks of Fervor
  - 'Attack Speed: 1% Per Stack'
  - 'Attack Speed At Max: 15%'
  - 'Bonus Attack Speed At Max: 1% Per Level'
  - 'Max Stacks Buff Duration: 5 seconds'
  - 'Max Stacks: 20'
  description: 'DAMAGE GRANTS ATTACK SPEED Notes: Gain stacks of Fervor when dealing
    or taking damage Attack Speed : 1% Per Stack Attack Speed At Max : 15% Bonus Attack
    Speed At Max : 1% Per Level Max Stacks Buff Duration : 5 seconds Max Stacks :
    20 Expand Ability Video'
- slot: 1st Ability
  name: Conviction
  cooldown:
  - 14.0
  cost:
  - 45.0
  details:
  - Healing allied gods reduces cooldowns for Guan Yu and his allies
  - Allies are Healed for 75% of the total
  - Can be cast during any of Guan Yu's other abilities
  - If Guan Yu would benefit from the Cooldown Reduction, but it was used during the
    cast of another ability, that ability will receive the Cooldown Reduction when
    it goes on cooldown
  - 'Heal: 45 | 70 | 95 | 120 | 145'
  - 'Heal Scaling: 6% Intelligence'
  - 'Cooldown Reduction: -2 seconds'
  - 'Ally Cooldown Reduction: -1.5 seconds'
  - 'Cooldown Reduction Scaling: 0.3% Intelligence'
  - 'Radius: 4.8 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 45 mana'
  description: 'AREA HEAL, COOLDOWN REDUCTION Notes: If Guan Yu would benefit from
    the Cooldown Reduction , but it was used during the cast of another ability, that
    ability will receive the Cooldown Reduction when it goes on cooldown Heal yourself
    and nearby allied gods Heal : 45 | 70 | 95 | 120 | 145 Heal Scaling : 6% Intelligence
    Cooldown Reduction : -2 seconds Ally Cooldown Reduction : -1.5 seconds Cooldown
    Reduction Scaling : 0.3% Intelligence Radius : 4.8 meters Cooldown : 14 seconds
    Cost : 45 mana Expand Ability Video'
- slot: 2nd Ability
  name: Warrior's Will
  cooldown:
  - 13.0
  cost:
  - 50.0
  details:
  - Hitting enemy gods reduces your cooldowns
  - 'Damage: 90 | 145 | 200 | 255 | 310'
  - 'Damage Scaling: 60% Strength'
  - 'Slow: 30 | 32.5 | 35 | 37.5 | 40%'
  - 'Slow Scaling: 2 seconds'
  - 'Slow Duration: 2% Intelligence'
  - 'Cooldown Reduction: -2 seconds'
  - 'Cooldown Reduction Scaling: 0.2% Intelligence'
  - 'Range: 5.05 meters'
  - 'Radius: 0.96 meters'
  - 'Cooldown: 13 seconds'
  - 'Cost: 50 mana'
  description: 'DASH DAMAGE SLOW Notes: Dash forward, dealing Physical Damage to and
    Slowing enemies you pass through Damage : 90 | 145 | 200 | 255 | 310 Damage Scaling
    : 60% Strength Slow : 30 | 32.5 | 35 | 37.5 | 40% Slow Scaling : 2 seconds Slow
    Duration : 2% Intelligence Cooldown Reduction : -2 seconds Cooldown Reduction
    Scaling : 0.2% Intelligence Range : 5.05 meters Radius : 0.96 meters Cooldown
    : 13 seconds Cost : 50 mana Expand Ability Video'
- slot: 3rd Ability
  name: Taolu Assault
  cooldown:
  - 13.0
  cost:
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  details:
  - Damages 10 times over 3 seconds
  - Every 25% Attack Speed increases the number of damage ticks by 1
  - You can cancel this ability at any time
  - 'Damage: 16 | 27 | 38 | 49 | 60'
  - 'Damage Scaling: 22.5% Strength + 15% Intelligence'
  - 'Protections Stolen: 3 | 5 | 7 | 9 | 11'
  - 'Protections Stolen Scaling: 1.5% Intelligence'
  - 'Protections Stolen Duration: 5 seconds'
  - 'Range: 4.8 meters'
  - 'Cooldown: 13 seconds'
  - 'Cost: 55 | 60 | 65 | 70 | 75 mana'
  description: 'CHANNEL DAMAGE, STEAL PROTECTIONS Notes: Swing your blade in a flurry,
    dealing Physical Damage repeatedly and stealing protections from enemies hit up
    to 3 times Damage : 16 | 27 | 38 | 49 | 60 Damage Scaling : 22.5% Strength + 15%
    Intelligence Protections Stolen : 3 | 5 | 7 | 9 | 11 Protections Stolen Scaling
    : 1.5% Intelligence Protections Stolen Duration : 5 seconds Range : 4.8 meters
    Cooldown : 13 seconds Cost : 55 | 60 | 65 | 70 | 75 mana Expand Ability Video'
- slot: Ultimate
  name: Cavalry Charge
  cooldown:
  - 90.0
  cost:
  - 80.0
  - 90.0
  - 100.0
  - 110.0
  - 120.0
  details:
  - Enemies hit by previous strikes take increased damage from the strike, stacking
    for each previous hit
  - You swing faster as you gain Attack Speed
  - You can ride the horse for a max of 4 seconds followed by a 0.67 second final
    swing
  - You can cancel this ability at any time, performing the final swing early
  - 'Damage: 85 | 110 | 135 | 160 | 185'
  - 'Damage Scaling: 30% Strength + 25% Intelligence'
  - 'Damage Escalation: 20%'
  - 'Slow: 30 | 32.5 | 35 | 37.5 | 40%'
  - 'Slow Duration: 2 seconds'
  - 'Stun Duration: 1.5 seconds'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 80 | 90 | 100 | 110 | 120 mana'
  description: 'MOUNT, ATTACK, STUN Notes: Mount a warhorse, gaining CC Immunity .
    Strike enemies while riding, dealing Physical Damage . Dismount with a final swing
    that also Stuns all enemies hit Damage : 85 | 110 | 135 | 160 | 185 Damage Scaling
    : 30% Strength + 25% Intelligence Damage Escalation : 20% Slow : 30 | 32.5 | 35
    | 37.5 | 40% Slow Duration : 2 seconds Stun Duration : 1.5 seconds Radius : 3.2
    meters Cooldown : 90 seconds Cost : 80 | 90 | 100 | 110 | 120 mana Expand Ability
    Video'
aspects:
- name: Aspect of the General
  kit_changes: Battle Fervor now provides Intelligence instead of Attack Speed. Conviction
    now applies an additional Heal over Time and will share Protections from Taolu
    Assault. However, Guan Yu loses all Strength scaling and reduced Intelligence
    damage scaling.
source_url: https://wiki.smite2.com/w/Guan_Yu
last_verified: '2026-07-23'
---
<!-- WIKI:START -->
- Guan Yu Basic Attack
- Battle Fervor
- Conviction
- Warrior's Will
- Taolu Assault
- Cavalry Charge
<!-- WIKI:END -->
