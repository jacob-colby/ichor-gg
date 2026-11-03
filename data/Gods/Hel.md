---
type: smite-god
name: Hel
pantheon: Norse
role: Mid Support
specializations:
- Nuker
- Healing
- Burst Damage
damage_type: magical
release_date: September 22, 2026
base_stats:
  health:
    base: 569.5
    per_level: 86.48
  health_regen:
    base: 1.7
    per_level: 0.2
  mana:
    base: 316.0
    per_level: 42.0
  mana_regen:
    base: 1.56
    per_level: 0.12
  physical_prot:
    base: 17.5
    per_level: 2.76
  magical_prot:
    base: 27.4
    per_level: 1.38
  attack_speed:
    base: 0.98
    per_level: 1.51
  attack_power:
    base: 36.0
    per_level: 2.79
  move_speed:
    base: 370.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Hel Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  detail_kinds:
  - null
  - magical
  - mechanic
  - mechanic
  damage_type: magical
  description: Fire a projectile that deals Magical Damage to the first enemy hit
- slot: Passive
  name: Stance Attunement
  details:
  - Your current stance gradually attunes over 3 seconds
  - 'Increased Damage: +20%'
  detail_kinds:
  - null
  - buff
  description: Remain in a stance to become attuned. In Dark Stance, gain increased
    Damage
  stance: Light
- slot: 1st Ability
  name: Decay
  cooldown:
  - 8.0
  cost:
  - 45.0
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  details:
  - This ability passes through and damages non-god enemies, and passes through walls,
    but stops on enemy gods
  - 'Damage: 90 | 150 | 190 | 240 | 290'
  - 'Damage Scaling: 60% Intelligence'
  - 'Range: 8.8 meters'
  - 'Explosion Radius: 3.4 meters'
  - 'Cooldown: 8 seconds'
  - 'Cost: 45 | 50 | 55 | 60 | 65 mana'
  detail_kinds:
  - null
  - magical
  - magical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Fire an orb that deals Magical Damage . The orb explodes when it hits
    an enemy god or reaches maximum range
  stance: Light
- slot: 2nd Ability
  name: Hinder
  cooldown:
  - 10.0
  cost:
  - 60.0
  details:
  - 'Protections: 5 | 10 | 15 | 20 | 25%'
  - 'Debuff Duration: 3 seconds'
  - 'Slow: 20 | 25 | 30 | 35 | 40%'
  - 'Slow Duration: 3 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 3.4 meters'
  - 'Cooldown: 10 seconds'
  - 'Cost: 60 mana'
  detail_kinds:
  - debuff
  - debuff
  - slow
  - slow
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  description: Area Shred and Slow Debuff all enemies in the targeted area, reducing
    their Protections and Slowing them
  stance: Light
- slot: 3rd Ability
  name: Repulse
  cooldown:
  - 12.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - 'Damage: 70 | 120 | 170 | 220 | 270'
  - 'Damage Scaling: 110% Intelligence'
  - 'Radius: 4.8 meters'
  - 'Cooldown: 12 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  detail_kinds:
  - magical
  - magical
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Area Damage Conjure a burst around you that deals Magical Damage to
    nearby enemies
  stance: Light
- slot: Ultimate
  name: Switch Stances
  cooldown:
  - 1.0
  details:
  - 'Mana Regen: 3 | 3 | 4 | 5 | 6 | 7'
  - 'Self Strength and Intelligence: 0 | 30 | 40 | 50 | 60 | 70'
  - 'Ally Strength and Intelligence: 0 | 15 | 20 | 25 | 30 | 35'
  - 'Range: 8.8 meters'
  - 'Cooldown: 1 second'
  detail_kinds:
  - buff
  - buff
  - buff
  - mechanic
  - mechanic
  description: Switch between Dark and Light Stances. You gain Mana Regen in both
    stances. You and nearby allied gods gain Strength and Intelligence
  stance: Light
- slot: Passive
  name: Stance Attunement
  details:
  - Your current stance gradually attunes over 3 seconds
  - 'Reduced Strength and Intelligence: 12%'
  detail_kinds:
  - null
  - debuff
  description: Remain in a stance to become attuned. In Light Stance, nearby enemy
    gods lose Strength and Intelligence
  stance: Dark
- slot: 1st Ability
  name: Restoration
  cooldown:
  - 10.0
  cost:
  - 45.0
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  details:
  - This ability passes through and damages non-god enemies, and passes through walls,
    but stops on gods
  - 'Damage: 70 | 120 | 170 | 220 | 270'
  - 'Damage Scaling: 50% Intelligence'
  - 'Heal: 45 | 60 | 75 | 90 | 105'
  - 'Heal Scaling: 30% Intelligence'
  - 'Mana Restore: 55 | 70 | 85 | 100 | 115'
  - 'Range: 8.8 meters'
  - 'Cooldown: 10 seconds'
  - 'Cost: 45 | 50 | 55 | 60 | 65'
  detail_kinds:
  - null
  - magical
  - magical
  - heal
  - heal
  - buff
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Fire an orb that deals Magical Damage . Hitting an ally god Heals them
    and restores Mana . You Heal and restore Mana when you hit an enemy or ally god
  stance: Dark
- slot: 2nd Ability
  name: Cleanse
  cooldown:
  - 12.0
  cost:
  - 60.0
  details:
  - 'CC Immunity Duration: 1.5 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 3.4 meters'
  - 'Cooldown: 12 seconds'
  - 'Cost: 60 mana'
  detail_kinds:
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  description: Area Remove all Crowd Control effects from allied gods in the target
    area and briefly make them CC Immune
  stance: Dark
- slot: 3rd Ability
  name: Inspire
  cooldown:
  - 10.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Allies Heal 6 times over 5 seconds
  - 'Self Heal: 45 | 60 | 75 | 90 | 105'
  - 'Self Heal Scaling: 10% Intelligence'
  - 'Ally Heal Per Tick: 11 | 13 | 15 | 17 | 19'
  - 'Ally Heal Per Tick Scaling: 5% Intelligence'
  - 'Movement Speed: 20%'
  - 'Attack Speed: 20%'
  - 'Buff Duration: 5 seconds'
  - 'Radius: 4.8 meters'
  - 'Cooldown: 10 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  detail_kinds:
  - heal
  - heal
  - heal
  - heal
  - heal
  - buff
  - buff
  - buff
  - mechanic
  - mechanic
  - mechanic
  description: You and nearby allies become buffed. Heal yourself instantly and nearby
    allies over time. You both gain Movement Speed and Attack Speed
  stance: Dark
- slot: Ultimate
  name: Switch Stances
  cooldown:
  - 1.0
  details:
  - 'Mana Regen: 3 | 3 | 4 | 5 | 6 | 7'
  - 'Self Protections: 0 | 13 | 16 | 19 | 22 | 25'
  - 'Ally Protections: 0 | 6.5 | 8 | 9.5 | 11 | 12.5'
  - 'Range: 8.8 meters'
  - 'Cooldown: 1 second'
  detail_kinds:
  - buff
  - buff
  - buff
  - mechanic
  - mechanic
  description: Switch between Dark and Light Stances. You gain Mana Regen in both
    stances. You and nearby allied gods gain Protections
  stance: Dark
aspects:
- name: Aspect of Divergence
  kit_changes: Deal damage or heal allies to fully attune to your Dark or Light stance,
    locking yourself to that form for the remainder of the match. While attuned, gain
    enhanced abilities and an new ultimate.
source_url: https://wiki.smite2.com/w/Hel
last_verified: '2026-11-03'
---
<!-- WIKI:START -->
- Hel Basic Attack
- Stance Attunement
- Decay
- Hinder
- Repulse
- Switch Stances
- Stance Attunement
- Restoration
- Cleanse
- Inspire
- Switch Stances
<!-- WIKI:END -->
