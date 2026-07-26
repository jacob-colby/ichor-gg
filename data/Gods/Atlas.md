---
type: smite-god
name: Atlas
pantheon: Greek
role: Support
specializations:
- Tank
- Crowd Control
- Area Control
damage_type: magical
release_date: May 5, 2026
base_stats:
  health:
    base: 705.3
    per_level: 101.52
  mana:
    base: 299.0
    per_level: 45.37
  physical_prot:
    base: 20.5
    per_level: 3.24
  magical_prot:
    base: 29.7
    per_level: 1.62
  attack_speed:
    base: 0.96
    per_level: 1.4
  move_speed:
    base: 370.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Atlas Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 3 hit chain. Attacks in order of 1.25, 1.25, 1.25x damage and swing time.
    The final hit cleaves
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Magical Damage to an enemy in front of you
- slot: Passive
  name: The Astrolabe
  cost:
  - 20.0
  details:
  - Empowered Astrolabe Strikes deal damage in an area, with increased swing time;
    enemy gods are Trembled and minions are Stunned
  - While your Astrolabe is deployed with Unburden, your Empowered Astrolabe Strike
    resolves at the Astrolabe's location, dealing 3 times Basic Attack Damage to enemies
    around it
  - While you are holding your Astrolabe, Empowered Astrolabe Strikes damage enemies
    in front of you
  - Empowered Astrolabe Strikes are spent even if no enemies are hit
  - 'Empowered Astrolabe Strike Damage: Basic Attack Damage + 8 per level'
  - 'Tremble Duration: 2 seconds'
  - 'Stun Duration: 2 seconds'
  - 'Energy from Gods: 1.25'
  - 'Energy from Minions: 0.125'
  - 'Max Energy: 30'
  - 'Radius: 1.5 meters'
  - 'Cost: 20 energy'
  description: You gain Energy in your Astrolabe when you take damage from enemy gods
    or deal damage with your Attacks or Abilities (minions grant reduced Energy).
    At enough Energy, you may press your interact key to unleash an Empowered Astrolabe
    Strike, consuming Energy. This does not trigger automatically from your next Attack
- slot: 1st Ability
  name: Unburden
  cooldown:
  - 14.0
  - 13.0
  - 12.0
  - 11.0
  - 10.0
  cost:
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  - 85.0
  details:
  - While the Astrolabe is deployed, gain Movement Speed
  - Gravity Pull changes based on whether your Astrolabe is deployed or held
  - 'Deploy Damage: 60 | 95 | 130 | 165 | 200'
  - 'Deploy Damage Scaling: 40% Intelligence'
  - 'Explosion Damage: 23'
  - 'Explosion Damage Scaling: 6 per level'
  - 'Deploy Slow: 20 | 22.5 | 25 | 27.5 | 30%'
  - 'Deploy Slow Duration: 2 seconds'
  - 'Movement Speed: 5%'
  - 'Range: 8 meters'
  - 'Radius: 4 meters'
  - 'Cooldown: 14 | 13 | 12 | 11 | 10 seconds'
  - 'Cost: 65 | 70 | 75 | 80 | 85 mana'
  - 'Cost Per Attack: 5 mana'
  description: Throw your Astrolabe to a target location, dealing Magical Damage and
    Slowing enemies. While deployed, your Attacks cause explosions at the Astrolabe
    that deal Magical Damage to enemies and cost Mana per explosion. The Astrolabe
    returns after 5 seconds or on refire
- slot: 2nd Ability
  name: Gravity Pull
  cooldown:
  - 16.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - Pull and Launch each deal Magical Damage
  - This ability cannot Pull or Launch enemies through walls.
  - 'Pull Damage: 50 | 80 | 110 | 140 | 170'
  - 'Pull Damage Scaling: 35% Intelligence'
  - 'Launch Damage: 50 | 80 | 110 | 140 | 170'
  - 'Launch Damage Scaling: 35% Intelligence'
  - 'Deployable Radius: 4 meters'
  - 'Range: 5.6 meters'
  - 'Cone Angle: 75 degrees'
  - 'Cooldown: 16 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Pull enemies toward your Astrolabe. Enemy gods who are too close are
    pulled into it. If you are holding your Astrolabe, you become Knock Up Immune
    , and enemies pulled into the Astrolabe are held in front of you before being
    Launched in the direction you are facing. If your Astrolabe is deployed, held
    enemies are Launched toward you from its location
- slot: 3rd Ability
  name: Kinetic Charge
  cooldown:
  - 16.0
  - 15.5
  - 15.0
  - 14.5
  - 14.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - The Dash has a maximum duration of 3 seconds
  - 'Damage: 80 | 130 | 180 | 230 | 280'
  - 'Damage Scaling: 40% Intelligence'
  - 'Ally Movement Speed: 25 | 27.5 | 30 | 32.5 | 35%'
  - 'Slow: 25% + 25% per ally cleansed'
  - 'Slow Duration: 2.5 seconds'
  - 'Maximum Slow: 75%'
  - 'Cleanse Radius: 4 meters'
  - 'Explosion Radius: 2.4 meters'
  - 'Cooldown: 16 | 15.5 | 15 | 14.5 | 14 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Dash forward, dealing Magical Damage to minions and cleansing yourself
    of Slows . Each allied god you pass near is cleansed of Slows and gains Movement
    Speed . While Dashing , you are Slow and Knock Up Immune . Hitting an enemy god
    stops the Dash and releases an explosion that Slows ; each Slow you cleanse from
    an ally during the Dash strengthens that explosion's Slow
- slot: Ultimate
  name: Gamma-Ray Burst
  cooldown:
  - 90.0
  cost:
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  - 85.0
  details:
  - Debuff duration refreshes on subsequent ticks
  - The radius of this ability shrinks as it travels
  - This ability passes through and damages all enemies, and passes through walls
  - 'Radiation Tick Damage: 35 | 45 | 55 | 65 | 75'
  - 'Radiation Tick Damage Scaling: 10% Intelligence'
  - 'Focused Beam Damage: 120 | 180 | 240 | 300 | 360'
  - 'Focused Beam Damage Scaling: 40% Intelligence'
  - 'Protection Reduction: 5% per stack'
  - 'Power Reduction: 3% per stack'
  - 'Debuff Duration: 5 seconds'
  - 'Max Radiation Stacks: 5 | 5 | 6 | 6 | 7'
  - 'Range: 320 meters'
  - 'Starting Radius: 4.8 meters'
  - 'Final Radius: 3.2 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 65 | 70 | 75 | 80 | 85 mana'
  description: Tear open the sky and call down a . Enemies in the area take Magical
    Damage over time and gain Radiation stacks that reduce their Protections and Power
    . After 5 seconds or when you refire, the burst focuses into a traveling beam
    that deals Magical Damage and applies 3 stacks of Radiation
aspects:
- name: Aspect of the Unburdened
  kit_changes: Your Attack now throws your astrolabe. Unburden is used to reposition
    the astrolabe. Gravity no longer pulls when the astrolabe is deployed. Kinetic
    Charge can be used to kick the astrolabe forward. Your passive now reduces the
    cooldown of Gamma-Ray Burst.
source_url: https://wiki.smite2.com/w/Atlas
last_verified: '2026-07-25'
---
<!-- WIKI:START -->
- Atlas Basic Attack
- The Astrolabe
- Unburden
- Gravity Pull
- Kinetic Charge
- Gamma-Ray Burst
<!-- WIKI:END -->
