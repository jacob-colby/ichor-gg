---
type: smite-build
god: Jormungandr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unyielding
  aspect_pick_rate: 0.3
  aspect_win_rate: 0.63
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.4
    win_rate: 0.63
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.59
    - name: Eye of Erebus
      pick_rate: 0.16
      win_rate: 0.69
  - name: Sun Beam Bow
    pick_rate: 0.15
    win_rate: 0.73
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.15
      win_rate: 0.67
    - name: Sanguine Lash
      pick_rate: 0.1
      win_rate: 0.4
  - name: Ethereal Staff
    pick_rate: 0.11
    win_rate: 0.73
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.09
      win_rate: 0.67
    - name: Golden Blade
      pick_rate: 0.09
      win_rate: 0.67
  - name: Freya's Tears
    pick_rate: 0.19
    win_rate: 0.56
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.1
      win_rate: 0.9
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.56
  - name: Brawler’s Beat Stick
    pick_rate: 0.1
    win_rate: 0.89
    alternates:
    - name: Freya's Tears
      pick_rate: 0.14
      win_rate: 0.54
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.5
  - name: Medal of Defense
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Medallion
      pick_rate: 0.04
      win_rate: 1.0
    - name: Draconic Scale
      pick_rate: 0.04
      win_rate: 1.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.3
    win_rate: 0.57
  - name: Sundering Axe
    pick_rate: 0.19
    win_rate: 0.63
  - name: Bluestone Pendant
    pick_rate: 0.13
    win_rate: 0.62
  source_url: https://smitebrain.com/gods/jormungandr/
  last_verified: '2026-10-10'
  god_win_rate: 0.6138613861386139
  god_matches_won: 62
  god_matches_played: 101
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-10'
  god_matches_analyzed: 4063
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Brawler’s Beat Stick
  - Berserker's Shield
  - Jotunn's Revenge
  - Draconic Scale
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s
    Revenge, Kinetic Cuirass, Shield Splitter, Breastplate of Valor, Golden Blade,
    Runeforged Hammer, Eye of the Storm, Erosion, Pharaoh''s Curse, Eye of Providence,
    Lernaean Bow, Shogun''s Ofuda, Hydra''s Lament, Shield of the Phoenix, Stone of
    Binding, Tyrfing, Nimble Ring, Helm of Radiance, Gluttonous Grimoire, Magi''s
    Cloak, Avenging Blade, Mantle Of Discord, Screeching Gargoyle, Midgardian Mail,
    Bragi''s Harp, Tekko-Kagi, Daybreak Gavel, Spear of Desolation, Hide of the Nemean
    Lion, Heartseeker, Rod of Asclepius, Leviathan''s Hide, Void Shield, Stampede,
    Ancile.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.61
      efficiency: 0.42
      win: 0.89
      pick: 0.22
      fit: 0.34
    Berserker's Shield:
      total: 0.61
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.31
    Draconic Scale:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.12
      fit: 0.48
    Silverbranch Bow:
      total: 0.63
      efficiency: 0.53
      win: 0.9
      pick: 0.17
      fit: 0.25
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Brawler’s Beat Stick
  - Draconic Scale
  - Silverbranch Bow
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Brawler’s Beat Stick
  - Berserker's Shield
  - Jotunn's Revenge
  - Draconic Scale
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Amanita Charm, Rod of Tahuti, Berserker''s Shield, Jotunn''s
    Revenge, Shield of the Phoenix, Kinetic Cuirass, Rod of Asclepius, Golden Blade,
    Soul Gem, Runeforged Hammer, Breastplate of Valor, Shield Splitter, Eye of the
    Storm, Pharaoh''s Curse, The Reaper, Yogi''s Necklace, Lernaean Bow, Erosion,
    Shogun''s Ofuda, Hydra''s Lament, Gluttonous Grimoire, Eye of Providence, Phoenix
    Feather, Tyrfing, Chandra''s Grace, Riptalon, Nimble Ring, Avenging Blade, Lifebinder,
    Helm of Radiance, Stone of Binding, Glorious Pridwen, Daybreak Gavel, Midgardian
    Mail, Bragi''s Harp, Tekko-Kagi, Sphere of Negation.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.6
      efficiency: 0.42
      win: 0.89
      pick: 0.22
      fit: 0.28
    Berserker's Shield:
      total: 0.61
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.49
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.32
    Draconic Scale:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.12
      fit: 0.46
    Silverbranch Bow:
      total: 0.64
      efficiency: 0.53
      win: 0.9
      pick: 0.17
      fit: 0.26
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.76
  community_ordered:
  - Brawler’s Beat Stick
  - Draconic Scale
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Brawler’s Beat Stick
  - Berserker's Shield
  - Jotunn's Revenge
  - Draconic Scale
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Draconic Scale, Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield,
    Amanita Charm, Stone of Binding, Avenging Blade, Screeching Gargoyle, Kinetic
    Cuirass, Gluttonous Grimoire, Void Shield, Breastplate of Valor, Spear of Desolation,
    Spear of the Magus, Void Stone, Heartseeker, Shield Splitter, Soul Gem, Tekko-Kagi,
    Obsidian Shard, Golden Blade, Runeforged Hammer, Toxic Blade, Titan''s Bane, The
    Crusher, Eye of the Storm, Hydra''s Lament, Lernaean Bow, Erosion, Nimble Ring,
    Pharaoh''s Curse, The Reaper, Helm of Radiance, Eye of Providence, Shield of the
    Phoenix, Doom Orb, Shogun''s Ofuda, Tyrfing.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.6
      efficiency: 0.42
      win: 0.89
      pick: 0.22
      fit: 0.26
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.47
    Draconic Scale:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.12
      fit: 0.37
    Silverbranch Bow:
      total: 0.66
      efficiency: 0.53
      win: 0.9
      pick: 0.17
      fit: 0.42
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Brawler’s Beat Stick
  - Draconic Scale
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Brawler’s Beat Stick
  - Berserker's Shield
  - Nimble Ring
  - Draconic Scale
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s
    Revenge, Nimble Ring, Golden Blade, Kinetic Cuirass, Gluttonous Grimoire, Breastplate
    of Valor, Tyrfing, Shield Splitter, Runeforged Hammer, Soul Gem, Pharaoh''s Curse,
    Riptalon, Lernaean Bow, Shogun''s Ofuda, Erosion, Helm of Radiance, Eye of Providence,
    Stone of Binding, Eye of the Storm, Shield of the Phoenix, Hydra''s Lament, Toxic
    Blade, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, The Reaper, Spear of
    Desolation, Spear of the Magus, Bragi''s Harp, Midgardian Mail, Mantle Of Discord,
    Tekko-Kagi, Rod of Asclepius, Avenging Blade.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.6
      efficiency: 0.42
      win: 0.89
      pick: 0.22
      fit: 0.26
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.43
    Nimble Ring:
      total: 0.57
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.3
    Draconic Scale:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.12
      fit: 0.37
    Silverbranch Bow:
      total: 0.65
      efficiency: 0.53
      win: 0.9
      pick: 0.17
      fit: 0.36
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Brawler’s Beat Stick
  - Draconic Scale
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Brawler’s Beat Stick
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Draconic Scale
  - Silverbranch Bow
  flex_slots:
  - Breastplate of Valor
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Draconic Scale, Rod of Tahuti, Jotunn''s
    Revenge, Berserker''s Shield, Breastplate of Valor, Amanita Charm, Kinetic Cuirass,
    Shield of the Phoenix, Spear of Desolation, Hydra''s Lament, Screeching Gargoyle,
    Soul Gem, Chronos'' Pendant, Shield Splitter, Golden Blade, Nimble Ring, Runeforged
    Hammer, Helm of Radiance, Gluttonous Grimoire, Erosion, Pharaoh''s Curse, Eye
    of Providence, Stone of Binding, Shogun''s Ofuda, Gladiator''s Shield, Eye of
    the Storm, Arondight, Gem of Focus, Lernaean Bow, Spear of the Magus, Magi''s
    Cloak, Rod of Asclepius, Daybreak Gavel, Mantle Of Discord, Obsidian Shard, Midgardian
    Mail, Tyrfing.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.6
      efficiency: 0.42
      win: 0.89
      pick: 0.22
      fit: 0.28
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.41
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.39
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.52
    Draconic Scale:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.12
      fit: 0.39
    Silverbranch Bow:
      total: 0.63
      efficiency: 0.53
      win: 0.9
      pick: 0.17
      fit: 0.2
  community_ordered:
  - Brawler’s Beat Stick
  - Draconic Scale
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Brawler’s Beat Stick
  - Berserker's Shield
  - Jotunn's Revenge
  - Draconic Scale
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Draconic Scale, Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged
    Hammer, Breastplate of Valor, Golden Blade, Eye of the Storm, Gluttonous Grimoire,
    Hydra''s Lament, Heartseeker, Lernaean Bow, Erosion, Spear of Desolation, Tekko-Kagi,
    Eye of Providence, Spear of the Magus, Avenging Blade, Shield of the Phoenix,
    Stone of Binding, Helm of Radiance, Tyrfing, Titan''s Bane, Soul Gem, The Crusher,
    Obsidian Shard, Pharaoh''s Curse, Magi''s Cloak, The Reaper, Nimble Ring, Shogun''s
    Ofuda, Screeching Gargoyle, Mantle Of Discord, Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.6
      efficiency: 0.42
      win: 0.89
      pick: 0.22
      fit: 0.3
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.45
    Draconic Scale:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.12
      fit: 0.42
    Silverbranch Bow:
      total: 0.64
      efficiency: 0.53
      win: 0.9
      pick: 0.17
      fit: 0.27
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Brawler’s Beat Stick
  - Draconic Scale
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Brawler’s Beat Stick
  - Berserker's Shield
  - Jotunn's Revenge
  - Draconic Scale
  - Silverbranch Bow
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Draconic Scale, Rod of Tahuti, Jotunn''s
    Revenge, Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Breastplate of Valor, Shield Splitter, Spear of the Magus, Spear of Desolation,
    Nimble Ring, Golden Blade, Runeforged Hammer, Helm of Radiance, Soul Gem, Obsidian
    Shard, Eye of the Storm, Hydra''s Lament, Lernaean Bow, Rod of Asclepius, Bragi''s
    Harp, Heartseeker, Erosion, Pharaoh''s Curse, Tekko-Kagi, Stone of Binding, Eye
    of Providence, Tyrfing, Shield of the Phoenix, Shogun''s Ofuda, Jade Scepter,
    Doom Orb, Wish-Granting Pearl, Avenging Blade, Death Metal, Chronos'' Pendant,
    Magi''s Cloak.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.6
      efficiency: 0.42
      win: 0.89
      pick: 0.22
      fit: 0.26
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.35
    Draconic Scale:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.12
      fit: 0.36
    Silverbranch Bow:
      total: 0.64
      efficiency: 0.53
      win: 0.9
      pick: 0.17
      fit: 0.29
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Brawler’s Beat Stick
  - Draconic Scale
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s
    Revenge, Kinetic Cuirass, Shield Splitter, Breastplate of Valor, Golden Blade,
    Runeforged Hammer, Eye of the Storm, Erosion, Pharaoh''s Curse, Eye of Providence,
    Lernaean Bow, Draconic Scale, Shogun''s Ofuda, Hydra''s Lament, Shield of the
    Phoenix, Stone of Binding, Tyrfing, Nimble Ring, Helm of Radiance, Gluttonous
    Grimoire, Magi''s Cloak, Avenging Blade, Mantle Of Discord, Screeching Gargoyle,
    Midgardian Mail, Bragi''s Harp, Tekko-Kagi, Daybreak Gavel, Spear of Desolation,
    Hide of the Nemean Lion, Heartseeker, Rod of Asclepius, Leviathan''s Hide, Void
    Shield, Stampede, Ancile.'
  slot_scores:
    Berserker's Shield:
      total: 0.61
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.58
    Shield Splitter:
      total: 0.57
      efficiency: 0.55
      win: 0.67
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.56
      pick: 0.32
      fit: 0.43
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Freya's Tears
  starter: *id001
---
