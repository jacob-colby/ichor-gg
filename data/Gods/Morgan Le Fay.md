---
type: smite-god
name: Morgan Le Fay
pantheon: Arthurian
role: Mid
specializations:
- Nuker
- Burst Damage
damage_type: magical
release_date: February 24, 2026
base_stats:
  health:
    base: 577.0
    per_level: 94.0
  mana:
    base: 316.32
    per_level: 42.0
  physical_prot:
    base: 17.48
    per_level: 2.76
  magical_prot:
    base: 27.38
    per_level: 1.38
  attack_speed:
    base: 0.98
    per_level: 1.51
  move_speed:
    base: 375.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Morgan Le Fay Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Fire a projectile that deals Magical Damage to the first enemy hit
- slot: Passive
  name: Empowered Blade
  details:
  - Mana Regen 1
  - Cooldown Reduction -2.5 seconds
  - Bonus Intelligence 20
  - Bonus Mana Regen 5
  - Buff Duration 10 seconds
  - Permanent Intelligence 2
  description: Mark Enemies with Abilities to Become Stronger Damaging enemy gods
    with abilities Marks them and activates a shared Symbol on your sword, providing
    Mana Regen . After gaining all 5 symbols you become empowered temporarily, causing
    your Cooldowns to be decreased and providing Intelligence and Mana Regen . Additionally
    you gain 1 stack of permanent Intelligence and bonus healing towards Consuming
    Power
- slot: 1st Ability
  name: Sigil Mastery
  cooldown:
  - 11.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - 'Mark of Mind: Fear enemy gods away from the center of the sigil'
  - 'Mark of Body: Create a Slowing field that persists for 4 seconds'
  - 'Mark of Soul: Spawn a clone at the enemy god location'
  - During the targeting of this ability, you can chose which sigil to imbue
  - Clones last 4 seconds, inherit 30% of your Health and 60% of your Basic Attack
    damage
  - 'Damage: 65 | 95 | 125 | 155 | 185'
  - 'Damage Scaling: 55% Intelligence'
  - 'Area Damage: 50 | 65 | 80 | 95 | 110'
  - 'Area Damage Scaling: 40% Intelligence'
  - 'Fear Duration: 0.6 | 0.7 | 0.8 | 0.9 | 1 second'
  - 'Slow: 35%'
  - 'Range: 8.8 meters'
  - 'Radius: 2 meters'
  - 'Outer Radius: 3.2 meters'
  - 'Cooldown: 11 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Summon a crashing sword, imbued by your chosen sigil, dealing Magical
    Damage before exploding dealing Magical Damage
- slot: 2nd Ability
  name: Dragonflight
  cooldown:
  - 14.0
  - 13.5
  - 13.0
  - 12.5
  - 12.0
  cost:
  - 70.0
  - 75.0
  - 80.0
  - 85.0
  - 90.0
  details:
  - Applies Mark of Spirit to enemy gods hit
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage: 50 | 70 | 90 | 110 | 130'
  - 'Damage Scaling: 35% Intelligence'
  - 'Dash Damage: 75 | 100 | 125 | 150 | 175'
  - 'Dash Damage Scaling: 50% Intelligence'
  - 'Range: 9.6 meters'
  - 'Radius: 3.2 meters'
  - 'Dash Radius: 1.28 meters'
  - 'Cooldown: 14 | 13.5 | 13 | 12.5 | 12 seconds'
  - 'Cost: 70 | 75 | 80 | 85 | 90 mana'
  description: Summon a dragon that deals Magical Damage and Knocks Up enemies. The
    dragon then flies forward, dealing Magical Damage and Knocking Back enemies hit
- slot: 3rd Ability
  name: Shroud of Wildfire
  cooldown:
  - 13.0
  cost:
  - 60.0
  details:
  - Applies Mark of Matter to enemy gods hit
  - Using this ability increases your Movement Speed for a short duration
  - The Debuff does damage every 1 second for 4 seconds and can be extended by 1 second
    per Attack, up to an additional 4 seconds
  - This ability passes through and damages non-god enemies, but stops on walls and
    enemy gods
  - 'Damage: 80 | 100 | 120 | 140 | 160'
  - 'Damage Scaling: 35% Intelligence'
  - 'Damage Per Tick: 5 | 10 | 15 | 20 | 25'
  - 'Damage Scaling Per Tick: 5% Intelligence'
  - 'Area Damage: 20 | 25 | 30 | 35 | 40'
  - 'Area Damage Scaling: 10% Intelligence'
  - 'Bonus Damage: 60 | 90 | 120 | 150 | 180'
  - 'Bonus Damage Scaling: 20% Intelligence'
  - 'Movement Speed: 16 | 18 | 20 | 22 | 24%'
  - 'Buff Duration: 4 seconds'
  - 'Debuff Duration: 4 seconds'
  - 'Range: 9.6 meters'
  - 'Radius: 0.64 meters'
  - 'Explode Radius: 1.92 meters'
  - 'Pulse Radius: 3.2 meters'
  - 'Cooldown: 13 seconds'
  - 'Cost: 60 mana'
  description: Send out Wildfire that explodes at max range or when it hits an enemy
    god, dealing Magical Damage in a small area and afflicting enemies with a Debuff.
    Debuffed enemies take Magical Damage repeatedly. Debuffed enemy gods and Jungle
    Bosses explode for Magical Damage when hit by your Attacks. If an enemy uses a
    Movement ability while Debuffed, they take Magical Damage and the Debuff is removed
- slot: Ultimate
  name: Consuming Power
  cooldown:
  - 90.0
  cost:
  - 80.0
  - 85.0
  - 90.0
  - 95.0
  - 100.0
  details:
  - The center of the final strike deals bonus Magical Damage based on the enemy's
    Max Health
  - You are CC Immune during this ability
  - Unique Marks consumed increase the width of the energy projectiles
  - Stacks of Empowered Blade provide bonus Healing
  - You ignore all movement penalties for the duration
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage: 25 | 40 | 55 | 70 | 85'
  - 'Damage Scaling: 10% Intelligence'
  - 'Projectile Damage: 90 | 130 | 170 | 210 | 250'
  - 'Projectile Damage Scaling: 40% Intelligence'
  - 'Damage: 5% of enemy''s Max Health'
  - 'Heal: 30 | 35 | 40 | 45 | 50 + 4% Missing Health'
  - 'Bonus Heal: 4 Per Stack'
  - 'Range: 11.2 meters'
  - 'Cone Angle: 75 degrees'
  - 'Projectile Range: 14.4 meters'
  - 'Projectile Radius: 1 meter'
  - 'Final Radius: 1.5 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 80 | 85 | 90 | 95 | 100 mana'
  description: Consume Marks from enemy gods dealing Magical Damage and empowering
    you. For a short duration, fire out 3 strikes of dark energy dealing Magical Damage
    and Healing you
aspects:
- name: Aspect of the Cursed Crown
  kit_changes: Your Attacks are now melee. You gain Wrath over time and when you deal
    damage. Consuming Power has two levels that can be used at 40 and 80 Wrath. Sigil
    Mastery fires all 3 Sigils simultaneously. Shroud of Wildfire Attack explosions
    deal a percentage of your Max Health as damage.
source_url: https://wiki.smite2.com/w/Morgan_Le_Fay
last_verified: '2026-07-25'
---
<!-- WIKI:START -->
- Morgan Le Fay Basic Attack
- Empowered Blade
- Sigil Mastery
- Dragonflight
- Shroud of Wildfire
- Consuming Power
<!-- WIKI:END -->
