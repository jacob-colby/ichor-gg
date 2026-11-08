---
type: smite-build
god: Jormungandr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unyielding
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.55
  slot_order:
  - name: Eye of Erebus
    pick_rate: 0.38
    win_rate: 0.58
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.38
    - name: Devourer's Gauntlet
      pick_rate: 0.1
      win_rate: 0.33
  - name: Prophetic Cloak
    pick_rate: 0.22
    win_rate: 0.42
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.22
      win_rate: 0.58
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.83
  - name: Freya's Tears
    pick_rate: 0.13
    win_rate: 0.55
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.12
      win_rate: 0.5
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.57
  - name: Soul Reaver
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.45
    - name: Ethereal Staff
      pick_rate: 0.09
      win_rate: 0.57
  - name: Hide of the Nemean Lion
    pick_rate: 0.06
    win_rate: 0.2
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.75
    - name: Soul Reaver
      pick_rate: 0.05
      win_rate: 0.5
  - name: Sage's Ring
    pick_rate: 0.06
    win_rate: 0.25
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.25
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.67
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.51
    win_rate: 0.55
  - name: Bluestone Pendant
    pick_rate: 0.2
    win_rate: 0.47
  - name: Sundering Axe
    pick_rate: 0.09
    win_rate: 0.25
  source_url: https://smitebrain.com/gods/jormungandr/
  last_verified: '2026-11-08'
  god_win_rate: 0.5116279069767442
  god_matches_won: 44
  god_matches_played: 86
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-08'
  god_matches_analyzed: 5119
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Shell of Rebuke
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Genji''s Guard, Amanita Charm, Rod of Tahuti, Kinetic
    Cuirass, Shield Splitter, Jotunn''s Revenge, Gluttonous Grimoire, Breastplate
    of Valor, Soul Gem, Tyrfing, Shield of the Phoenix, Draconic Scale, Runeforged
    Hammer, Oni Hunter''s Garb, Golden Blade, Erosion, Hydra''s Lament, Eye of Providence,
    The Reaper, Nimble Ring, Shogun''s Ofuda, Midgardian Mail, Pharaoh''s Curse, Spear
    of Desolation, Screeching Gargoyle, Stone of Binding, Bragi''s Harp, Helm of Radiance,
    Leviathan''s Hide, Blood-Bound Book, Magi''s Cloak, Mantle Of Discord, Helm of
    Darkness, Lernaean Bow, Dominance, Death Metal, Tekko-Kagi, Hide of the Nemean
    Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.12
      fit: 0.24
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.54
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.55
      pick: 0.2
      fit: 0.4
    Shell of Rebuke:
      total: 0.53
      efficiency: 0.41
      win: 0.75
      pick: 0.11
      fit: 0.31
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.44
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Shell of Rebuke
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shell of Rebuke
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Shell of Rebuke
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Genji''s Guard, Soul Gem, Shield
    of the Phoenix, Rod of Tahuti, Kinetic Cuirass, The Reaper, Blood-Bound Book,
    Jotunn''s Revenge, Phoenix Feather, Shield Splitter, Gluttonous Grimoire, Yogi''s
    Necklace, Tyrfing, Golden Blade, Runeforged Hammer, Breastplate of Valor, Chandra''s
    Grace, Oni Hunter''s Garb, Riptalon, Draconic Scale, Bancroft''s Talon, Hydra''s
    Lament, Bloodforge, Erosion, Nimble Ring, Eye of Providence, Regrowth Striders,
    Shogun''s Ofuda, Pharaoh''s Curse, Midgardian Mail, Spear of Desolation, Bragi''s
    Harp, Leviathan''s Hide, Screeching Gargoyle, Glorious Pridwen, Hide of the Nemean
    Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.57
      pick: 0.12
      fit: 0.21
    Berserker's Shield:
      total: 0.56
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.52
    Shell of Rebuke:
      total: 0.52
      efficiency: 0.41
      win: 0.75
      pick: 0.11
      fit: 0.26
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.72
    Soul Gem:
      total: 0.54
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Genji's Guard
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Shell of Rebuke
  - Amanita Charm
  flex_slots:
  - Shell of Rebuke
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Genji''s Guard, Berserker''s Shield, Jotunn''s Revenge,
    Amanita Charm, Gluttonous Grimoire, Soul Gem, Kinetic Cuirass, Screeching Gargoyle,
    Stone of Binding, The Reaper, Spear of Desolation, Avenging Blade, Shield Splitter,
    Void Stone, Void Shield, Breastplate of Valor, The Crusher, Tekko-Kagi, Heartseeker,
    Tyrfing, Obsidian Shard, Shield of the Phoenix, Runeforged Hammer, Oni Hunter''s
    Garb, Titan''s Bane, Draconic Scale, Spear of the Magus, Hydra''s Lament, Toxic
    Blade, Golden Blade, Erosion, Nimble Ring, Dreamer''s Idol, Silverbranch Bow,
    Eye of Providence, Blood-Bound Book, Midgardian Mail, Helm of Radiance.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.57
      pick: 0.12
      fit: 0.19
    Berserker's Shield:
      total: 0.54
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.55
      pick: 0.2
      fit: 0.31
    Shell of Rebuke:
      total: 0.52
      efficiency: 0.41
      win: 0.75
      pick: 0.11
      fit: 0.25
    Amanita Charm:
      total: 0.53
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.34
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Tyrfing
  - Shell of Rebuke
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Genji''s Guard, Rod of Tahuti, Amanita Charm, Kinetic
    Cuirass, Tyrfing, Jotunn''s Revenge, Golden Blade, Shield Splitter, Gluttonous
    Grimoire, Breastplate of Valor, Soul Gem, Shield of the Phoenix, Oni Hunter''s
    Garb, Nimble Ring, Draconic Scale, Runeforged Hammer, Shogun''s Ofuda, Pharaoh''s
    Curse, Erosion, Hydra''s Lament, Eye of Providence, Spear of Desolation, Toxic
    Blade, Bragi''s Harp, Screeching Gargoyle, Midgardian Mail, The Reaper, Blood-Bound
    Book, Helm of Radiance, Stone of Binding, Lernaean Bow, Dominance, Leviathan''s
    Hide, Silverbranch Bow, Magi''s Cloak, Mantle Of Discord, Helm of Darkness, Hide
    of the Nemean Lion.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.57
      pick: 0.12
      fit: 0.2
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.43
    Tyrfing:
      total: 0.5
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.53
    Shell of Rebuke:
      total: 0.52
      efficiency: 0.41
      win: 0.75
      pick: 0.11
      fit: 0.26
    Amanita Charm:
      total: 0.53
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Shell of Rebuke
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Jotunn's Revenge
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Berserker''s Shield,
    Rod of Tahuti, Amanita Charm, Soul Gem, Jotunn''s Revenge, Kinetic Cuirass, Breastplate
    of Valor, Shield of the Phoenix, Spear of Desolation, Gluttonous Grimoire, Screeching
    Gargoyle, Hydra''s Lament, Shield Splitter, Chronos'' Pendant, Oni Hunter''s Garb,
    Draconic Scale, Nimble Ring, Gladiator''s Shield, Tyrfing, Blood-Bound Book, Arondight,
    Helm of Radiance, Erosion, Runeforged Hammer, Eye of Providence, Midgardian Mail,
    Golden Blade, Gem of Focus, Heartwood Charm, Helm of Darkness, Ancient Signet,
    Stone of Binding, The Reaper, Shogun''s Ofuda, Leviathan''s Hide, Chandra''s Grace,
    Pharaoh''s Curse.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.57
      pick: 0.12
      fit: 0.39
    Berserker's Shield:
      total: 0.54
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.37
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.55
      pick: 0.2
      fit: 0.52
    Shell of Rebuke:
      total: 0.52
      efficiency: 0.41
      win: 0.75
      pick: 0.11
      fit: 0.26
    Soul Gem:
      total: 0.52
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.53
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shell of Rebuke
  - Amanita Charm
  flex_slots:
  - Shell of Rebuke
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Genji''s Guard, Berserker''s
    Shield, Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield Splitter, Gluttonous
    Grimoire, Soul Gem, The Reaper, Runeforged Hammer, Breastplate of Valor, Tyrfing,
    Hydra''s Lament, Spear of Desolation, Shield of the Phoenix, The Crusher, Oni
    Hunter''s Garb, Draconic Scale, Golden Blade, Heartseeker, Erosion, Eye of Providence,
    Tekko-Kagi, Titan''s Bane, Death Metal, Midgardian Mail, Screeching Gargoyle,
    Blood-Bound Book, Stone of Binding, Bragi''s Harp, Helm of Radiance, Obsidian
    Shard, Avenging Blade, Leviathan''s Hide, Arondight, Nimble Ring, Magi''s Cloak,
    Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.57
      pick: 0.12
      fit: 0.21
    Berserker's Shield:
      total: 0.54
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.49
    Shell of Rebuke:
      total: 0.53
      efficiency: 0.41
      win: 0.75
      pick: 0.11
      fit: 0.28
    Amanita Charm:
      total: 0.53
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Shell of Rebuke
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Genji''s Guard, Berserker''s
    Shield, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Jotunn''s Revenge,
    Soul Gem, Spear of Desolation, Shield Splitter, Breastplate of Valor, The Reaper,
    Nimble Ring, Tyrfing, Blood-Bound Book, Helm of Radiance, Runeforged Hammer, Bragi''s
    Harp, Obsidian Shard, Shield of the Phoenix, Death Metal, Oni Hunter''s Garb,
    Hydra''s Lament, Ancient Signet, Draconic Scale, Golden Blade, Helm of Darkness,
    Spear of the Magus, The Crusher, Polynomicon, Erosion, Tekko-Kagi, Eye of Providence,
    Chronos'' Pendant, Heartseeker, Dreamer''s Idol, Screeching Gargoyle, Midgardian
    Mail, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.57
      pick: 0.12
      fit: 0.19
    Berserker's Shield:
      total: 0.54
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.34
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.55
      pick: 0.2
      fit: 0.31
    Shell of Rebuke:
      total: 0.52
      efficiency: 0.41
      win: 0.75
      pick: 0.11
      fit: 0.24
    Amanita Charm:
      total: 0.53
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.34
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Amanita Charm, Rod of Tahuti, Kinetic
    Cuirass, Genji''s Guard, Shield Splitter, Jotunn''s Revenge, Gluttonous Grimoire,
    Breastplate of Valor, Soul Gem, Tyrfing, Shield of the Phoenix, Draconic Scale,
    Runeforged Hammer, Oni Hunter''s Garb, Golden Blade, Erosion, Hydra''s Lament,
    Eye of Providence, The Reaper, Nimble Ring, Shogun''s Ofuda, Midgardian Mail,
    Pharaoh''s Curse, Spear of Desolation, Screeching Gargoyle, Stone of Binding,
    Bragi''s Harp, Helm of Radiance, Leviathan''s Hide, Blood-Bound Book, Magi''s
    Cloak, Mantle Of Discord, Helm of Darkness, Hide of the Nemean Lion, Lernaean
    Bow, Dominance, Death Metal, Tekko-Kagi.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.12
      fit: 0.24
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.54
    Shield Splitter:
      total: 0.51
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.55
      pick: 0.2
      fit: 0.4
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.44
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
community_aspects:
  source: SmiteBrain per-match feed, obsidian+ (data/Analysis/aspect_matches)
  complete_from: '2026-10-20'
  minimum_matches: 30
  window_rule: the newest patch window, or the last closed one when the newest holds
    fewer than minimum_matches of the aspect's matches
  aspects:
  - aspect: Aspect of the Unyielding
    status: below minimum
    matches_by_window:
      ob47: 10
      ob46: 24
---
