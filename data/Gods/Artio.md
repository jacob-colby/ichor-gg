---
type: smite-god
name: Artio
pantheon: Celtic
role: Solo Support
specializations:
- Brawler
- Lockdown
- Crowd Control
damage_type: magical
release_date: December 2, 2025
base_stats:
  health:
    base: 626.52
    per_level: 101.52
  health_regen:
    base: 1.82
    per_level: 0.2
  mana:
    base: 319.68
    per_level: 45.36
  mana_regen:
    base: 1.65
    per_level: 0.12
  physical_prot:
    base: 20.52
    per_level: 3.24
  magical_prot:
    base: 29.7
    per_level: 1.62
  attack_speed:
    base: 0.96
    per_level: 1.4
  attack_power:
    base: 44.4
    per_level: 2.4
  move_speed:
    base: 375.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Artio Basic Attack
  details:
  - 'Druid: Fire a projectile that deals Magical Damage to the first enemy hit'
  - 'Druid: Projectile stops on first target hit, and does not pass through walls'
  - 'Bear: Deal Magical Damage to an enemy in front of you'
  - 'Bear: If multiple enemies are in the area, the enemy closest to the center of
    the area will be hit'
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Druid Range: 8.8 meters'
  - 'Druid Radius: 0.48 meters'
  - 'Bear Range: 1.92 meters'
  - 'Bear Cone Angle: 120 degrees'
  detail_kinds:
  - magical
  - null
  - magical
  - null
  - magical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Artio's s change depending on her current stance
- slot: Passive
  name: Decompose
  details:
  - The Protection Debuff effect stacks up to 5 times
  - 'Protections Debuff: 2% Per Stack'
  - 'Debuff Duration: 6 seconds'
  detail_kinds:
  - debuff
  - debuff
  - debuff
  description: When Artio hits enemy gods with damaging abilities, the target will
    begin to decompose, reducing their Protections .
- slot: 1st Ability
  name: Energy Surge
  cooldown:
  - 12.0
  cost:
  - 40.0
  - 45.0
  - 50.0
  - 55.0
  - 60.0
  details:
  - Reduces enemy Healing
  - 'Damage: 70 | 105 | 140 | 175 | 210'
  - 'Damage Scaling: 35% Intelligence + 60% Strength'
  - 'Heal: 30 | 50 | 70 | 90 | 110'
  - 'Heal Scaling: 25% Intelligence'
  - 'Healing Reduction: -25%'
  - 'Healing Reduction Duration: 5 seconds'
  - 'Range: 4 meters'
  - 'Radius: 120 degrees'
  - 'Cooldown: 12 seconds'
  - 'Cost: 40 | 45 | 50 | 55 | 60 mana'
  detail_kinds:
  - debuff
  - magical
  - magical
  - heal
  - heal
  - debuff
  - debuff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Artio pulses out a strong wave of energy dealing Magical Damage to
    enemies. She will Heal herself and allies around each enemy god hit by this ability
  stance: Druid
- slot: 2nd Ability
  name: Entangling Vines
  cooldown:
  - 15.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - 'Power Debuff: -9 | -10.5 | -12 | -13.5 | -15%'
  - 'Duration: 4 seconds'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 15 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  detail_kinds:
  - debuff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  description: Cripple and Reduce Enemy Power Artio creates a thicket of vines around
    herself that Cripples enemy gods and reduces their Magical or Physical Power as
    long as they are in the area
  stance: Druid
- slot: 3rd Ability
  name: Life Tap
  cooldown:
  - 15.0
  cost:
  - 55.0
  details:
  - While Channeling she deals Magical Damage up to 5 times and Heals herself up to
    5 times
  - Each hit adds a stack of Slow to enemies
  - Enemies hit all 5 times are Rooted
  - 'Damage: 15 | 30 | 45 | 60 | 75'
  - 'Damage Scaling: 15% Intelligence'
  - 'Heal: 10 | 15 | 20 | 25 | 30'
  - 'Heal Scaling: 3% Intelligence'
  - 'Slow: 7%'
  - 'Slow Duration: 1 second'
  - 'Root Duration: 1 second'
  - 'Range: 8.8 meters'
  - 'Cooldown: 15 seconds'
  - 'Cost: 55 mana'
  detail_kinds:
  - magical
  - slow
  - debuff
  - magical
  - magical
  - heal
  - heal
  - slow
  - slow
  - debuff
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Artio channels for 2 seconds, draining the life from enemies in a line
    in front of her
  stance: Druid
- slot: Ultimate
  name: Shapeshift
  details:
  - When Artio hits at least 1 enemy with an ability, she gains 1 stack of Invigoration,
    granting her Movement Speed and Mana Regeneration
  - Stacks fall off one at a time
  - 'Movement Speed: 0 | 1 | 1.25 | 1.5 | 1.75 | 2% Per Stack'
  - 'Mana Regeneration: 0 | 0.4 | 0.8 | 1.2 | 1.6 | 2 Per Stack'
  - 'Max Stacks: 8'
  - 'Stack Duration: 6 seconds'
  detail_kinds:
  - buff
  - null
  - buff
  - buff
  - mechanic
  - mechanic
  description: Artio s between her Druid stance and Bear stance
  stance: Druid
- slot: 1st Ability
  name: Maul Prey
  cooldown:
  - 12.0
  cost:
  - 40.0
  - 45.0
  - 50.0
  - 55.0
  - 60.0
  details:
  - Reduces enemy Healing
  - 'Damage: 40 | 70 | 100 | 130 | 160'
  - 'Damage Scaling: 30% Intelligence + 50% Strength'
  - 'Healing Reduction: -25%'
  - 'Healing Reduction Duration: 5 seconds'
  - 'Range: 4 meters'
  - 'Radius: 120 degrees'
  - 'Cooldown: 12 seconds'
  - 'Cost: 40 | 45 | 50 | 55 | 60 mana'
  detail_kinds:
  - debuff
  - magical
  - magical
  - debuff
  - debuff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Artio swipes twice in front of her with her claws, dealing Magical
    Damage to enemies with each swipe
  stance: Bear
- slot: 2nd Ability
  name: Ferocious Roar
  cooldown:
  - 15.0
  cost:
  - 40.0
  - 45.0
  - 50.0
  - 55.0
  - 60.0
  details:
  - 'Stun Duration: 1 | 1.1 | 1.2 | 1.3 | 1.4 seconds'
  - 'Protections: 15 | 30 | 35 | 40 | 35'
  - 'Protections Duration: 4 seconds'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 15 seconds'
  - 'Cost: 40 | 45 | 50 | 55 | 60 mana'
  detail_kinds:
  - stun
  - buff
  - buff
  - mechanic
  - mechanic
  - mechanic
  description: Circular Area Stun Artio lets out a ferocious roar that Stuns all nearby
    enemies and increases her own Physical and Magical Protections
  stance: Bear
- slot: 3rd Ability
  name: Heavy Charge
  cooldown:
  - 15.0
  cost:
  - 55.0
  details:
  - Enemies she Dashes through take Magical Damage and are Slowed
  - Artio is Displacement Immune during this ability
  - 'Damage: 75 | 120 | 165 | 210 | 255'
  - 'Damage Scaling: 55% Intelligence + 85% Strength'
  - 'Increased Movement Speed: 100%'
  - 'Slow: 20%'
  - 'Slow Duration: 2 seconds'
  - 'Cooldown: 15 seconds'
  - 'Cost: 55 mana'
  detail_kinds:
  - null
  - mechanic
  - magical
  - magical
  - buff
  - slow
  - slow
  - mechanic
  - mechanic
  damage_type: magical
  description: Artio Dashes forward at an increased movement speed for 3 seconds
  stance: Bear
aspects:
- name: Aspect of the Denmother
  kit_changes: Artio can only change stances inside the fountain. Upon leaving the
    fountain, her abilities are enhanced and her ultimate changes based on her form.
source_url: https://wiki.smite2.com/w/Artio
last_verified: '2026-08-09'
---
<!-- WIKI:START -->
- Artio Basic Attack
- Decompose
- Energy Surge
- Entangling Vines
- Life Tap
- Shapeshift
- Maul Prey
- Ferocious Roar
- Heavy Charge
<!-- WIKI:END -->
