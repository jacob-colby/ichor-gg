---
type: smite-god
name: Aphrodite
pantheon: Greek
role: Mid Support
specializations:
- Healing
- Buffs
- Sustain
damage_type: magical
release_date: December 10, 2024
base_stats:
  health:
    base: 569.48
    per_level: 86.48
  health_regen:
    base: 1.7
    per_level: 0.2
  mana:
    base: 316.32
    per_level: 42.0
  mana_regen:
    base: 1.65
    per_level: 0.12
  physical_prot:
    base: 17.48
    per_level: 2.76
  magical_prot:
    base: 27.38
    per_level: 1.38
  attack_speed:
    base: 0.96
    per_level: 1.4
  attack_power:
    base: 40.85
    per_level: 2.21
  move_speed:
    base: 375.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Aphrodite Basic Attack
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
  name: Center of Attention
  details:
  - 'Physical Protection: 3 Per Stack'
  - 'Magical Protection: 3 Per Stack'
  detail_kinds:
  - buff
  - buff
  description: NEARBY PLAYERS GRANT PROTECTIONS Gain Physical Protection and Magical
    Protection for each friendly or enemy god nearby
- slot: 1st Ability
  name: Kiss
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
  - The Soul Mate gains 50% of your Mana Regen
  - The Soul Mate gains 0.5 Strength and 1 Intelligence per 1 Mana Regen from items
    you have
  - If you have been linked to a Soul Mate for 5 seconds or more, switching to a new
    Soul Mate will cause both gods to become Jealous
  - Enemy gods in the path of a Kiss that will create a Soul Mate will also take Magical
    Damage and be Stunned. The Kiss will lock on to an ally god if they were in the
    area at the time of fire and not already linked
  - This ability passes through non-god enemies, and passes through walls, but stops
    on gods
  - 'Damage: 40 | 60 | 80 | 100 | 120'
  - 'Damage Scaling: 25% Intelligence'
  - 'Stun Duration: 0.8 seconds'
  - 'Jealousy Damage Increase: 6 | 8 | 10 | 12 | 14%'
  - 'Jealousy Buff Duration: 5 seconds'
  - 'Movement Speed: 6 | 6.5 | 7 | 7.5 | 8%'
  - 'Range: 8.8 meters'
  - 'Radius: 0.8 meters'
  - 'Cooldown: 14 | 13.5 | 13 | 12.5 | 12 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  detail_kinds:
  - buff
  - buff
  - null
  - magical
  - null
  - magical
  - magical
  - stun
  - buff
  - buff
  - buff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Enemy gods in the path of a that will create a Soul Mate will also
    take Magical Damage and be Stunned . The will lock on to an ally god if they were
    in the area at the time of fire and not already linked Fire a kiss projectile
    at an allied god to link a Soul Mate, giving you both Increased Movement Speed
    , and reducing ' cooldown. If the kiss hits an enemy god, they take Magical Damage
    , are Stunned , and your Soul Mate becomes Jealous, Increasing their damage dealt
- slot: 2nd Ability
  name: Back Off!
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
  - If you have a Soul Mate, deal Magical Damage, and Slow enemies hit. If an enemy
    is hit by both areas, they take reduced damage from the 2nd area
  - 'Damage: 60 | 110 | 160 | 210 | 250'
  - 'Damage Scaling: 50% Intelligence'
  - 'Soul Mate Damage: 60 | 110 | 160 | 210 | 250'
  - 'Soul Mate Damage Scaling: 30% Intelligence'
  - 'Bonus Damage: 40 | 60 | 80 | 100 | 120'
  - 'Bonus Damage Scaling: 20% Intelligence'
  - 'Slow: 30%'
  - 'Slow Duration: 2 seconds'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 14 | 13.5 | 13 | 12.5 | 12 seconds'
  - 'Cost: 70 | 75 | 80 | 85 | 90 mana'
  detail_kinds:
  - magical
  - magical
  - magical
  - magical
  - magical
  - magical
  - magical
  - slow
  - slow
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: If you have a Soul Mate, deal Magical Damage , and Slow enemies hit.
    If an enemy is hit by both areas, they take reduced damage from the 2nd area Deal
    Magical Damage , Slow , and Push away enemies around you Soul Mate
- slot: 3rd Ability
  name: Love Birds
  cooldown:
  - 16.0
  - 15.5
  - 15.0
  - 14.5
  - 14.0
  cost:
  - 70.0
  - 75.0
  - 80.0
  - 85.0
  - 90.0
  details:
  - On fire, Aphrodite and her Soul Mate start Healing repeatedly over time and have
    their active cooldowns decreased per tick
  - This ability Heals 7 times over 3 seconds
  - This ability deals Magical Damage 7 times over 3 seconds
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage Per Tick: 10 | 18 | 26 | 34 | 40'
  - 'Damage Scaling Per Tick: 5% Intelligence'
  - 'Heal Per Tick: 10 | 13 | 16 | 19 | 22'
  - 'Self Heal Scaling Per Tick: 7% Intelligence'
  - 'Ally Heal Scaling Per Tick: 7% Intelligence'
  - Active Cooldowns Decreased Per Tick 0.25 seconds
  - 'Range: 11.2 meters'
  - 'Cooldown: 16 | 15.5 | 15 | 14.5 | 14 seconds'
  - 'Cost: 70 | 75 | 80 | 85 | 90 mana'
  detail_kinds:
  - heal
  - heal
  - magical
  - null
  - magical
  - magical
  - heal
  - heal
  - heal
  - buff
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Fire a Doves projectile that deals Magical Damage repeatedly over time
    to enemies hit
- slot: Ultimate
  name: Undying Love
  cooldown:
  - 100.0
  - 97.5
  - 95.0
  - 92.5
  - 90.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - Reactivate to Leap to your Soul Mates location
  - Activating this ability instantly refreshes the cooldown on Love Birds
  - 'Buff Duration: 0.8 | 1.1 | 1.4 | 1.7 | 2 seconds'
  - 'Cooldown: 100 | 97.5 | 95 | 92.5 | 90 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  detail_kinds:
  - null
  - null
  - buff
  - mechanic
  - mechanic
  description: You and your Soul Mate become Damage Immune , CC Immune , and your
    Soul Mate gains the Jealousy effect for a short duration
aspects: []
source_url: https://wiki.smite2.com/w/Aphrodite
last_verified: '2026-11-02'
---
<!-- WIKI:START -->
- Aphrodite Basic Attack
- Center of Attention
- Kiss
- Back Off!
- Love Birds
- Undying Love
<!-- WIKI:END -->
