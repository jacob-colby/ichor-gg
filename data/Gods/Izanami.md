---
type: smite-god
name: Izanami
pantheon: Japanese
role: Carry
specializations:
- Pressure
- Burst Damage
- Constant Damage
damage_type: physical
release_date: November 12, 2024
base_stats:
  health:
    base: 569.48
    per_level: 86.48
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
    base: 1.02
    per_level: 1.51
  move_speed:
    base: 370.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Izanami Basic Attack
  details:
  - Projectile speed increases with higher Attack Speed, up to a maximum of a 45%
    increase at 2.0 Attack Speed
  - Item effects only trigger on the first target hit per attack
  - This ability passes through and damages all enemies, but stops on walls
  - 'Initial Damage Scaling: 75% Strength + 15% Intelligence + 75% Attack Damage'
  - 'Return Damage Scaling: 35% Strength + 7% Intelligence + 35% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Throw a piercing projectile that deals Physical Damage to all enemies
    hit. The projectile returns to you after reaching tis max range or hitting a wall,
    dealing Physical Damage to any enemies hit on its way back
- slot: Passive
  name: Death Draws Nigh
  details:
  - Each stack fades 10 seconds after the damage was taken
  - Stack count cannot drop below the percentage of your current missing health
  - 'Percent Penetration: 0.3% Per Stack'
  - 'Intelligence: 0.5 Per Stack'
  - 'Intelligence Per Level: 0.05 Per Stack'
  - 'Max Stacks: 50'
  description: Gain Percent Penetration and Intelligence for each 1% of your Max Health
    taken as damage
- slot: 1st Ability
  name: Sickle Storm
  cooldown:
  - 11.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Attacks deal Bonus Damage to Structures
  - Applies a stacking Bleed effect to enemies hit
  - Projectile speed increases with higher Attack Speed, up to a maximum of a 45%
    Increase at 2.0 Attack Speed
  - Bleed Damage is multiplied with each Stack, and ticks every 0.5 seconds
  - Can be activated without breaking Stealth from Fade Away
  - Cancelling this ability will end the effect early
  - 'Attack Speed: 30 | 35 | 40 | 45 | 50%'
  - 'Damage Scaling: 100% Strength + 20% Intelligence'
  - 'Bonus Structure Damage: 5 | 10 | 15 | 20 | 25'
  - 'Bleed Damage: 5 | 10 | 15 | 20 | 25 + 30% Intelligence over 4 ticks'
  - 'Max Debuff Stacks: 3'
  - 'Debuff Duration: 2 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  - 'Cooldown: 11 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Significantly increases your Attack Speed for 6 seconds, but your Attacks
    no longer pierce enemies or return to you
- slot: 2nd Ability
  name: Spectral Projection
  cooldown:
  - 14.0
  - 13.5
  - 13.0
  - 12.5
  - 12.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - Reduces enemy Healing
  - Can be cast without breaking Stealth from Fade Away
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage: 50 | 90 | 130 | 170 | 210'
  - 'Damage Scaling: 80% Strength + 75% Intelligence'
  - 'Slow: 20 | 22.5 | 25 | 27.5 | 30%'
  - 'Slow Duration: 2 seconds'
  - 'Healing Reduction: -25%'
  - 'Healing Reduction Duration: 5 seconds'
  - 'Range: 11.2 meters'
  - 'Radius: 0.8 meters'
  - 'Cooldown: 14 | 13.5 | 13 | 12.5 | 12 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Send forth a spectral projection of yourself, dealing Physical Damage
    and Slowing all enemies in a line
- slot: 3rd Ability
  name: Fade Away
  cooldown:
  - 17.0
  - 16.5
  - 16.0
  - 15.5
  - 15.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - Gain Movement Speed while in Stealth
  - Sickle Storm and Spectral Projection can be used without breaking Stealth
  - 'Movement Speed: 15 | 20 | 25 | 30 | 35%'
  - 'Buff Duration: 3 | 3.5 | 4 | 4.5 | 5 seconds'
  - 'Range: 8.8 meters'
  - 'Cooldown: 17 | 16.5 | 16 | 15.5 | 15 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Descend into the underworld, becoming Stealthed , and Leap away from
    your current position
- slot: Ultimate
  name: Dark Portal
  cooldown:
  - 90.0
  cost:
  - 100.0
  details:
  - Damaged enemies are also Silenced and Slowed
  - Slowing and Damage over time effects start strong, and fade away over 2 seconds
  - Slow is not affected by diminishing returns
  - 'Damage: 180 | 260 | 340 | 420 | 500'
  - 'Damage Scaling: 100% Strength + 30% Intelligence'
  - 'Damage Over Time: 50 | 80 | 110 | 140 | 170 over 4 ticks'
  - 'Damage Over Time Scaling: 70% Intelligence over 4 ticks'
  - 'Silence Duration: 2 seconds'
  - 'Initial Slow Amount: 60%'
  - 'Range: 9.6 meters'
  - 'Radius: 2.4 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 100 mana'
  description: Summon a dark portal which deals instant Physical Damage and Physical
    Damage over time
aspects: []
source_url: https://wiki.smite2.com/w/Izanami
last_verified: '2026-07-25'
---
<!-- WIKI:START -->
- Izanami Basic Attack
- Death Draws Nigh
- Sickle Storm
- Spectral Projection
- Fade Away
- Dark Portal
<!-- WIKI:END -->
