---
type: smite-build
god: Sun Wukong
mode: Conquest
builds:
- source: community
  aspect: Aspect of Transformation
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.29
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.48
    win_rate: 0.45
    alternates:
    - name: Book of Thoth
      pick_rate: 0.09
      win_rate: 0.5
    - name: Lifebinder
      pick_rate: 0.07
      win_rate: 0.0
  - name: Gladiator's Shield
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.2
      win_rate: 0.67
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.2
  - name: Freya's Tears
    pick_rate: 0.2
    win_rate: 0.22
    alternates:
    - name: Genji's Guard
      pick_rate: 0.18
      win_rate: 0.75
    - name: Runeforged Hammer
      pick_rate: 0.07
      win_rate: 0.67
  - name: Genji's Guard
    pick_rate: 0.2
    win_rate: 0.44
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.09
      win_rate: 0.75
    - name: Gladiator's Shield
      pick_rate: 0.07
      win_rate: 1.0
  - name: Brawler’s Beat Stick
    pick_rate: 0.11
    win_rate: 0.75
    alternates:
    - name: Triton's Conch
      pick_rate: 0.08
      win_rate: 0.33
    - name: Shield of the Phoenix
      pick_rate: 0.05
      win_rate: 0.5
  - name: Medal of Disruption
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.67
    - name: Gladiator's Shield
      pick_rate: 0.08
      win_rate: 0.5
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.37
    win_rate: 0.53
  - name: Bluestone Pendant
    pick_rate: 0.24
    win_rate: 0.45
  - name: Archmage's Gem
    pick_rate: 0.11
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/sun-wukong/
  last_verified: '2026-09-11'
  god_win_rate: 0.45652173913043476
  god_matches_won: 21
  god_matches_played: 46
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-11'
  god_matches_analyzed: 3080
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Brawler’s Beat Stick
  - Berserker's Shield
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield,
    Amanita Charm, Kinetic Cuirass, Shield Splitter, Eye of the Storm, Avenging Blade,
    Gluttonous Grimoire, Lernaean Bow, Breastplate of Valor, Hydra''s Lament, Erosion,
    Shield of the Phoenix, Pharaoh''s Curse, Eye of Providence, Heartseeker, Draconic
    Scale, Shogun''s Ofuda, Golden Blade, Tekko-Kagi, Bragi''s Harp, Rod of Asclepius,
    Daybreak Gavel, Nimble Ring, Helm of Radiance, Midgardian Mail, Stone of Binding,
    Dominance, Spear of the Magus, Titan''s Bane, Death Metal, Leviathan''s Hide,
    Jade Scepter, The Crusher, Void Shield.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.53
      efficiency: 0.42
      win: 0.75
      pick: 0.24
      fit: 0.25
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.37
    Hide of the Nemean Lion:
      total: 0.57
      efficiency: 0.52
      win: 0.75
      pick: 0.15
      fit: 0.32
    Runeforged Hammer:
      total: 0.59
      efficiency: 0.57
      win: 0.67
      pick: 0.11
      fit: 0.56
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Brawler’s Beat Stick
  - Hide of the Nemean Lion
  - Runeforged Hammer
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Brawler’s Beat Stick
  - Berserker's Shield
  - Shield of the Phoenix
  - Hide of the Nemean Lion
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Amanita Charm, Rod of Tahuti, Berserker''s Shield,
    Shield of the Phoenix, Jotunn''s Revenge, Kinetic Cuirass, Rod of Asclepius, Shield
    Splitter, Eye of the Storm, Soul Gem, Erosion, Ethereal Staff, The Reaper, Breastplate
    of Valor, Eye of Providence, Yogi''s Necklace, Draconic Scale, Phoenix Feather,
    Gluttonous Grimoire, Avenging Blade, Pharaoh''s Curse, Shogun''s Ofuda, Lernaean
    Bow, Hydra''s Lament, Stone of Binding, Midgardian Mail, Helm of Radiance, Chandra''s
    Grace, Daybreak Gavel, Magi''s Cloak, Leviathan''s Hide, Sphere of Negation, Void
    Shield, Stampede, Heartseeker, Ancile, Lifebinder.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.55
      efficiency: 0.42
      win: 0.75
      pick: 0.24
      fit: 0.33
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.48
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.11
      fit: 0.71
    Hide of the Nemean Lion:
      total: 0.58
      efficiency: 0.52
      win: 0.75
      pick: 0.15
      fit: 0.37
    Runeforged Hammer:
      total: 0.58
      efficiency: 0.57
      win: 0.67
      pick: 0.11
      fit: 0.53
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.84
  community_ordered:
  - Brawler’s Beat Stick
  - Shield of the Phoenix
  - Hide of the Nemean Lion
  - Runeforged Hammer
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Runeforged Hammer
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Brawler’s Beat Stick
  - Gluttonous Grimoire
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Runeforged Hammer, Jotunn''s Revenge, Gluttonous
    Grimoire, Berserker''s Shield, Avenging Blade, Amanita Charm, Heartseeker, Spear
    of the Magus, Stone of Binding, Obsidian Shard, Spear of Desolation, Tekko-Kagi,
    Titan''s Bane, Kinetic Cuirass, The Crusher, Soul Gem, Void Shield, Screeching
    Gargoyle, The Reaper, Void Stone, Breastplate of Valor, Shield Splitter, Doom
    Orb, Eye of the Storm, The World Stone, Avatar''s Parashu, Hydra''s Lament, Lernaean
    Bow, Dreamer''s Idol, Pendulum Blade, Shield of the Phoenix, Nimble Ring, Daybreak
    Gavel, Helm of Radiance, Erosion, Pharaoh''s Curse, Rod of Asclepius, Eye of Providence.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.52
      efficiency: 0.42
      win: 0.75
      pick: 0.24
      fit: 0.17
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.56
    Hide of the Nemean Lion:
      total: 0.56
      efficiency: 0.52
      win: 0.75
      pick: 0.15
      fit: 0.22
    Runeforged Hammer:
      total: 0.57
      efficiency: 0.57
      win: 0.67
      pick: 0.11
      fit: 0.42
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Brawler’s Beat Stick
  - Hide of the Nemean Lion
  - Runeforged Hammer
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Brawler’s Beat Stick
  - Berserker's Shield
  - Nimble Ring
  - Hide of the Nemean Lion
  - Runeforged Hammer
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Rod of Tahuti, Berserker''s Shield, Nimble Ring,
    Golden Blade, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire, Tyrfing,
    Riptalon, Kinetic Cuirass, Lernaean Bow, Silverbranch Bow, Toxic Blade, Pharaoh''s
    Curse, Breastplate of Valor, Soul Gem, Shogun''s Ofuda, Shield Splitter, Tekko-Kagi,
    Bragi''s Harp, Eye of the Storm, Hydra''s Lament, The Reaper, Shield of the Phoenix,
    Daybreak Gavel, Dominance, Avenging Blade, Helm of Radiance, Bracer of The Abyss,
    Rod of Asclepius, Spear of the Magus, Erosion, Eye of Providence, Qin''s Blade,
    Vital Amplifier, Heartseeker, Draconic Scale, Obsidian Shard.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.65
    Brawler’s Beat Stick:
      total: 0.52
      efficiency: 0.42
      win: 0.75
      pick: 0.24
      fit: 0.16
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.45
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.36
    Hide of the Nemean Lion:
      total: 0.56
      efficiency: 0.52
      win: 0.75
      pick: 0.15
      fit: 0.21
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.57
      win: 0.67
      pick: 0.11
      fit: 0.36
  community_ordered:
  - Brawler’s Beat Stick
  - Hide of the Nemean Lion
  - Runeforged Hammer
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Runeforged Hammer
  flex_slots:
  - Breastplate of Valor
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Runeforged Hammer, Jotunn''s Revenge,
    Rod of Tahuti, Breastplate of Valor, Berserker''s Shield, Shield of the Phoenix,
    Amanita Charm, Spear of Desolation, Hydra''s Lament, Soul Gem, Chronos'' Pendant,
    Kinetic Cuirass, Screeching Gargoyle, Gluttonous Grimoire, Arondight, Gem of Focus,
    Nimble Ring, Eye of Erebus, Helm of Radiance, Rod of Asclepius, Shield Splitter,
    Spear of the Magus, Prophetic Cloak, Chandra''s Grace, Eye of the Storm, Daybreak
    Gavel, Obsidian Shard, Erosion, Pharaoh''s Curse, Jade Scepter, Lernaean Bow,
    Eye of Providence, Wish-Granting Pearl, Avenging Blade, Totem of Death, Draconic
    Scale, Pendulum Blade, Shogun''s Ofuda.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.52
      efficiency: 0.42
      win: 0.75
      pick: 0.24
      fit: 0.17
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.44
      pick: 0.33
      fit: 0.44
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.49
    Hide of the Nemean Lion:
      total: 0.56
      efficiency: 0.52
      win: 0.75
      pick: 0.15
      fit: 0.23
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.57
      win: 0.67
      pick: 0.11
      fit: 0.34
  community_ordered:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Hide of the Nemean Lion
  - Runeforged Hammer
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield,
    Amanita Charm, Runeforged Hammer, Kinetic Cuirass, Shield Splitter, Eye of the
    Storm, Avenging Blade, Gluttonous Grimoire, Lernaean Bow, Breastplate of Valor,
    Hydra''s Lament, Erosion, Pharaoh''s Curse, Eye of Providence, Heartseeker, Draconic
    Scale, Shogun''s Ofuda, Golden Blade, Shield of the Phoenix, Tekko-Kagi, Bragi''s
    Harp, Rod of Asclepius, Daybreak Gavel, Nimble Ring, Helm of Radiance, Midgardian
    Mail, Stone of Binding, Dominance, Spear of the Magus, Titan''s Bane, Death Metal,
    Leviathan''s Hide, Jade Scepter, The Crusher, Void Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shield Splitter:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.51
    Runeforged Hammer:
      total: 0.59
      efficiency: 0.57
      win: 0.67
      pick: 0.11
      fit: 0.56
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Runeforged Hammer
  starter: *id001
---
