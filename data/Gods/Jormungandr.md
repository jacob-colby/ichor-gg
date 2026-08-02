---
type: smite-god
name: Jormungandr
pantheon: Norse
role: Solo Support
specializations:
- Tank
- Area Control
- Constant Damage
- Global
damage_type: magical
release_date: August 26, 2025
base_stats:
  health:
    base: 668.5
    per_level: 101.52
  mana:
    base: 296.0
    per_level: 42.0
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
  attack_power:
    base: 20.0
    per_level: 4.0
  health_regen:
    base: 1.84
    per_level: 0.22
  mana_regen:
    base: 1.45
    per_level: 0.12
abilities:
- slot: Basic Attack
  name: Jormungandr Basic Attack
  details:
  - Increasing Attack Speed decreases the Overheat speed
  - 5 attacks per second, decreasing while firing to a minimum of 2 per second
  - Attacks proc item hit effects for 40% damage and 20% healing
  - 'Base Overheat Rate: 1.5'
  - 'Base Cooling Rate: 2.5'
  - 'Tick Rate: 0.1 seconds'
  - 'Inhand Movement Penalty: 50%'
  - 'Base Inhand Power: 20'
  - 'Damage Scaling: 40% Strength + 8% Intelligence + 40% Attack Damage'
  - 'Attack Speed Conversion: 25%'
  - 'Range: 5.6 meters'
  - 'Cone Angle: 45 degrees'
  description: Deal Magical Damage to all enemies in front of you. As you attack,
    your Overheat increases causing your firing rate to decrease
  damage_type: magical
  detail_kinds:
  - buff
  - null
  - null
  - null
  - null
  - null
  - null
  - null
  - magical
  - mechanic
  - mechanic
  - mechanic
- slot: Passive
  name: Immovable
  details:
  - 'Hard Displacement effects include: Banish, Grab, Knockback, Levitate, and Vortex
    effects'
  - 'Damage Scaling: 6% Max Health or 115% Strength (whichever is higher)'
  - 'Slow: 15%'
  - 'Increased Damage Taken: 5%'
  - 'Dazed Duration: 2 seconds'
  - 'Debuff Max Stacks: 14'
  - 'Debuff Duration: 6 seconds'
  description: You are Hard Displacement Immune , but are instead Dazed , a debuff
    that Slows you and increases the damage you take . Additionally, hits from Attacks
    and Venomous Haze cause enemy gods to gain a Debuff stack. At max stacks, the
    next hit deals damage based on your Max Health or Strength , and resets the Debuff
  damage_type: magical
  detail_kinds:
  - stun
  - magical
  - slow
  - debuff
  - debuff
  - debuff
  - debuff
- slot: 1st Ability
  name: Venomous Haze
  cooldown:
  - 13.0
  - 12.5
  - 12.0
  - 11.5
  - 11.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - The cloud deals Magical Damage, Slows, and reduces enemy Healing
  - While within the cloud, you gain extra Cooling for your Attacks
  - Interacting with a toxic cloud with other abilities reduces their duration to
    8 seconds
  - You can have a maximum of 9 clouds active at once
  - 'Damage: 80 | 120 | 160 | 200 | 240'
  - 'Damage Scaling: 40% Intelligence'
  - 'Damage Per Tick: 10 | 20 | 30 | 40 | 50'
  - 'Damage Scaling Per Tick: 5% Intelligence'
  - 'Slow: 20%'
  - 'Slow Duration: 1.5 seconds'
  - 'Healing Reduction: -25%'
  - 'Healing Reduction Duration: 5 seconds'
  - 'Extra Cooling: 25% Base Rate'
  - 'Range: 12 meters'
  - 'Inner Radius: 1.6 meters'
  - 'Outer Radius: 2.4 meters'
  - 'Cooldown: 13 | 12.5 | 12 | 11.5 | 11 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: The cloud deals Magical Damage , Slows , and reduces enemy Healing
    Fire noxious spit at an area dealing Magical Damage and creating a toxic cloud
    that persists for 20 seconds
  damage_type: magical
  detail_kinds:
  - magical
  - buff
  - null
  - null
  - magical
  - magical
  - magical
  - magical
  - slow
  - slow
  - debuff
  - debuff
  - buff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 2nd Ability
  name: Consuming Bellow
  cooldown:
  - 12.0
  cost:
  - 70.0
  details:
  - Each cloud Empowers you and the roar, increasing its size and causing it to deal
    bonus Magical Damage per cloud.
  - While Empowered, your Attacks fire at their maximum rate
  - Size increases up to 3 times, but the bonus damage is uncapped
  - Each cloud provides 2 seconds of Attack Empowerment, up to 6 seconds max
  - 'Damage: 120 | 180 | 240 | 300 | 360'
  - 'Damage Scaling: 45% Intelligence + 30% Strength'
  - 'Bonus Damage: 20 | 25 | 30 | 35 | 40'
  - 'Bonus Damage Scaling: 10% Intelligence'
  - 'Slow: 30%'
  - 'Debuff Duration: 1.5 seconds'
  - 'Inner Radius: 3.2 meters'
  - 'Outer Radius: 4.8 meters'
  - 'Cooldown: 12 seconds'
  - 'Cost: 70 mana'
  description: Each cloud provides 2 seconds of Attack Empowerment , up to 6 seconds
    max Channel briefly, drawing power from nearby toxic clouds, then roar to deal
    Magical Damage , Slow , and Tremble enemies around you
  damage_type: magical
  detail_kinds:
  - magical
  - buff
  - null
  - buff
  - magical
  - magical
  - magical
  - magical
  - slow
  - debuff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 3rd Ability
  name: Submerge
  cooldown:
  - 14.0
  cost:
  - 70.0
  - 75.0
  - 80.0
  - 85.0
  - 90.0
  details:
  - While submerged, you pulse out a ring, gaining vision of enemies
  - Emerging through a toxic cloud creates two new clouds
  - Taking damage while in Stealth partially reveals you
  - 'Damage: 70 | 125 | 180 | 235 | 290'
  - 'Damage Scaling: 50% Intelligence + 40% Strength'
  - 'Movement Speed: 35%'
  - 'Max Submerge Duration: 5 seconds'
  - 'Radius: 3.2 meters'
  - 'Pulse Radius: 20 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 70 | 75 | 80 | 85 | 90 mana'
  description: 'into the ground, becoming Stealthed and gaining Movement Speed . Reactivate
    to emerge, Knocking Up and dealing Magical Damage to enemies Max Duration: 5 seconds'
  damage_type: magical
  detail_kinds:
  - null
  - null
  - null
  - magical
  - magical
  - buff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: Ultimate
  name: The World Serpent
  cooldown:
  - 90.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - Emerging out of the ground and your body Crashing Down deals Magical Damage to
    enemies hit
  - Each time you Emerge and Submerge, you Knock Up enemies and leave behind a low
    duration toxic cloud
  - Each enemy god hit with this ability provides a stacking Protections buff when
    the ability ends
  - You are CC Immune during this ability
  - If you cannot dive to the target location when the time expires, the ability will
    end
  - 'Damage: 150 | 200 | 250 | 300 | 350'
  - 'Damage Scaling: 35% Intelligence + 30% Strength'
  - 'Emerge/Crash Damage: 75 | 100 | 125 | 150 | 175'
  - 'Emerge/Crash Damage Scaling: 20% Intelligence + 15% Strength'
  - 'Protections: 10 | 12 | 14 | 16 | 18'
  - 'Max Protections Stacks: 4'
  - Buff Duration 6 seconds
  - 'Range: 16 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Enter into the world before diving up to 3 times across the battlefield.
    Each time you Submerge you deal Magical Damage to enemies hit
  damage_type: magical
  detail_kinds:
  - magical
  - stun
  - buff
  - mechanic
  - null
  - magical
  - magical
  - magical
  - magical
  - buff
  - buff
  - buff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
aspects:
- name: Aspect of the Unyielding
  kit_changes: Toxic clouds do not deal tick damage but allied gods within them gain
    Damage Reduction. Within them, you do not gain Cooling but lower cooldown for
    Venomous Haze. Consuming Bellow does not deal bonus damage but allies gain INT
    and STR. Submerge Knockup height is increased.
source_url: https://wiki.smite2.com/w/Jormungandr
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Jormungandr Basic Attack
- Immovable
- Venomous Haze
- Consuming Bellow
- Submerge
- The World Serpent
<!-- WIKI:END -->
