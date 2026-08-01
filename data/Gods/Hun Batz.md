---
type: smite-god
name: Hun Batz
pantheon: Maya
role: Jungle
specializations:
- Slayer
- Mobile
- Crowd Control
damage_type: physical
release_date: February 3, 2025
base_stats:
  health:
    base: 619.0
    per_level: 94.0
  mana:
    base: 275.68
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
    base: 380.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Hun Batz Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 3 hit chain. Attacks in order of 1, 0.75, 1.25x damage and swing time
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Physical Damage to an enemy in front of you
- slot: Passive
  name: Infused Strikes
  details:
  - 'Strength: 4 Per Stack'
  - 'Strength Scaling: 0.2 Per Level'
  - 'Max Stacks: 4'
  - 'Buff Duration: 4 seconds'
  description: ATTACK DAMAGE AFTER ABILITY After using an ability, Hun Batz's next
    Basic Attack will deal 1.2x damage and grants Hun Batz a stacking Strength Buff
    on successful hits.
- slot: 1st Ability
  name: Somersault
  cooldown:
  - 13.0
  cost:
  - 60.0
  details:
  - Enemies hit when taking off take 25% damage
  - 'Damage: 75 | 115 | 155 | 195 | 235'
  - 'Damage Scaling: 60% Strength'
  - 'Slow: 30 | 32.5 | 35 | 37.5 | 40%'
  - 'Slow Duration: 2 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 2.4 meters'
  - 'Cooldown: 13 seconds'
  - 'Cost: 60 mana'
  description: Leap forward, dealing Physical Damage and Slowing enemies in the area
    where you land
- slot: 2nd Ability
  name: Overhand Smash
  cooldown:
  - 12.0
  - 11.5
  - 11.0
  - 10.5
  - 10.0
  cost:
  - 60.0
  details:
  - While Channeling you are Displacement Immune and Immune to Strafe and Backpedal
    Movement Penalties
  - 'Damage: 85 | 140 | 195 | 250 | 305'
  - 'Damage Scaling: 75% Strength'
  - 'Physical Protections Reduced: 8 | 10 | 12 | 14 | 16'
  - 'Debuff Duration: 2 seconds'
  - 'Range: 5.6 meters'
  - 'Cone Angle: 110 degrees'
  - 'Cooldown: 12 | 11.5 | 11 | 10.5 | 10 seconds'
  - 'Cost: 60 mana'
  description: Channel for a short duration. At the end of the Channel, deal Physical
    Damage to enemies in front of you and apply a Physical Protection Debuff
- slot: 3rd Ability
  name: Sacred Monkey
  cooldown:
  - 13.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - This ability stops on first target hit, and does not pass through walls
  - 'Damage: 80 | 135 | 190 | 245 | 300'
  - 'Damage Scaling: 55% Strength'
  - 'Mark Duration: 2 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  - 'Cooldown: 13 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Throw a projectile monkey that deals Physical Damage to any enemies
    it hits. After hitting, it will bounce to nearby enemies applying a Mark to only
    the most recently hit enemy. Reactive this ability to Teleport to the Marked enemy
- slot: Ultimate
  name: Fear No Evil
  cooldown:
  - 120.0
  - 115.0
  - 110.0
  - 105.0
  - 100.0
  cost:
  - 60.0
  details:
  - Hits every 0.25 seconds
  - Fear can only last a maximum of 1 second
  - 'Damage Per Tick: 35'
  - 'Damage Scaling Per Tick: 10% Strength'
  - 'Feared Duration: 0.5 seconds'
  - 'Lifetime: 1 | 1.25 | 1.5 | 1.75 | 2 seconds'
  - 'Range: 7.2 meters'
  - 'Radius: 5.6 meters'
  - 'Cooldown: 120 | 115 | 110 | 105 | 100 seconds'
  - 'Cost: 60 mana'
  description: Create a Totem that repeatedly Fears and deals Physical Damage to all
    enemies around it
aspects:
- name: Aspect of Disruption
  kit_changes: infused Strikes Slow gods hit by them, but do not grant Hun Batz the
    stacking Strength buff. Overhand Smash Stuns gods hit by it, but deals reduced
    damage.
source_url: https://wiki.smite2.com/w/Hun_Batz
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Hun Batz Basic Attack
- Infused Strikes
- Somersault
- Overhand Smash
- Sacred Monkey
- Fear No Evil
<!-- WIKI:END -->
