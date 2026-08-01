---
type: smite-god
name: Nut
pantheon: Egyptian
role: Carry Mid
specializations:
- Nuker
- Sharpshooter
- Area Control
damage_type: magical
release_date: December 16, 2025
base_stats:
  health:
    base: 577.0
    per_level: 94.0
  mana:
    base: 296.0
    per_level: 42.0
  physical_prot:
    base: 18.76
    per_level: 2.76
  magical_prot:
    base: 25.3
    per_level: 1.38
  attack_speed:
    base: 1.0
    per_level: 1.51
  move_speed:
    base: 370.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Nut Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Fire a projectile that deals Magical Damage to the first enemy hit
- slot: Passive
  name: Flux
  details:
  - Otherwise, Attacks grant Astral Flux. Abilities consume this for bonus Magical
    Damage and effects.
  - Stacks decay every 3 seconds
  - 'Attack Speed: 2% Per Stack'
  - 'Attack Speed Per Level: 0.2% Per Stack'
  - 'Bonus Magical Damage: 10%'
  - 'Max Stacks: 10'
  description: Otherwise, Attacks grant Astral . Abilities consume this for bonus
    Magical Damage and effects. While Strength exceeds Intelligence, Ability hits
    grant Stellar which provides Attack Speed
- slot: 1st Ability
  name: Convergence
  cooldown:
  - 10.0
  cost:
  - 45.0
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  details:
  - 'Astral Flux: Consumes 4 stacks to cause targets to lose Protections'
  - Unused stacks are refunded if Nut dies while firing
  - Start the match with 2 full shots of this ability
  - If you cancel this ability without firing a shot, it goes on a 1 second cooldown
  - This ability passes through and damages all enemies, but stops on walls
  - 'Inner Damage: 50 | 55 | 60 | 65 | 70% of Basic Attack Damage'
  - 'Outer Damage: 3 | 6 | 9 | 12 | 15'
  - 'Outer Damage Scaling: 20% Intelligence + 17.5% Strength'
  - 'Protections Reduced: 15%'
  - 'Max Stacks: 16'
  - 'Range: 8.8 meters'
  - 'Radius: 0.96 meters'
  - 'Cooldown: 10 seconds'
  - 'Cost: 45 | 50 | 55 | 60 | 65 mana'
  - 'Cost Per Additional Shot: 4 Stacks'
  description: Your Attacks fire two additional projectiles that deal Magical Damage
    . Nut always shoots at least once, but may fire up to an additional 4 shots by
    using stacks. Hitting an enemy with an Attack provides 1 stack, hitting an enemy
    god provides 2
- slot: 2nd Ability
  name: Crashing Comet
  cooldown:
  - 15.0
  cost:
  - 65.0
  details:
  - 'Astral Flux: Consumes 4 stacks to cause the comet to echo, damaging and trembling
    again'
  - Enemies in the center are Rooted
  - Enemies on the edge are Trembled
  - 'Inner Damage: 100 | 150 | 200 | 250 | 300'
  - 'Inner Damage Scaling: 85% Intelligence + 50% Strength'
  - 'Outer Damage: 50 | 75 | 100 | 125 | 150'
  - 'Outer Damage Scaling: 50% Intelligence + 25% Strength'
  - 'Echo Damage: 30 | 45 | 60 | 75 | 90'
  - 'Echo Damage Scaling: 50% Intelligence'
  - 'Root Duration: 0.9 | 1 | 1.1 | 1.2 | 1.3 seconds'
  - 'Range: 8.8 meters'
  - 'Inner Radius: 1.6 meters'
  - 'Outer Radius: 4 meters'
  - 'Cooldown: 15 seconds'
  - 'Cost: 65 mana'
  description: Call down a comet that deals Magical Damage where it lands and less
    Magical Damage in an area around it
- slot: 3rd Ability
  name: Warp
  cooldown:
  - 12.0
  cost:
  - 50.0
  - 45.0
  - 50.0
  - 55.0
  - 60.0
  details:
  - 'Stellar Flux: Resets the Cooldown of Convergence and grants 8 Ammo'
  - 'Astral Flux: Consumes 4 stacks to fire 2 additional projectiles'
  - Projectiles deal increased damage to the first target hit, and reduced damage
    to subsequent hits
  - 'Damage: 40 | 75 | 110 | 145 | 180'
  - 'Damage Scaling: 40% Intelligence + 30% Strength'
  - 'Slow: 10% Per Stack'
  - 'Slow Duration: 3 seconds'
  - 'Range: 2.4 meters'
  - 'Radius: 7.2 meters'
  - 'Cooldown: 12 seconds'
  - 'Cost: 50 | 45 | 50 | 55 | 60 mana'
  description: Teleport in the direction you are moving and fire homing projectiles
    at nearby enemies that deal Magical Damage and applies a stacking slow . Subsequent
    hits deal 33% damage
- slot: Ultimate
  name: Skyfall
  cooldown:
  - 100.0
  cost:
  - 45.0
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  details:
  - Grants 2 stacks of Flux for each god hit
  - Projectile lands after 1 second, and detonates 0.5 seconds later
  - 'Projectile Damage: 200 | 260 | 320 | 380 | 440'
  - 'Projectile Damage Scaling: 80% Intelligence + 90% Strength'
  - 'Explosion Damage: 85 | 110 | 135 | 160 | 185'
  - 'Explosion Damage Scaling: 40% Intelligence + 45% Strength'
  - 'Range: 11.2 meters'
  - 'Projectile Radius: 3.2 meters'
  - 'Explosion Radius: 6.4 meters'
  - 'Cooldown: 100 seconds'
  - 'Cost: 45 | 50 | 55 | 60 | 65 mana'
  description: Become CC Immune and ascend into the sky. Fire a massive black hole
    that deals Magical Damage before detonating for additional Magical Damage and
    Pulling enemies towards the center
aspects:
- name: Aspect of the Cosmos
  kit_changes: Flux becomes Cosmic Flux (Mitigation, decays). Decaying past 10 stacks
    Heals allies. Base Damage +10%, Scaling -25%. Convergence grants a mini version
    of itself to allies on god hit. Crashing Comet Stuns and Slows. Warp grants CC
    immunity to self and 1 nearby ally. -12.5% Basic Attack Damage.
source_url: https://wiki.smite2.com/w/Nut
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Nut Basic Attack
- Flux
- Convergence
- Crashing Comet
- Warp
- Skyfall
<!-- WIKI:END -->
