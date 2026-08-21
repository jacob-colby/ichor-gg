---
type: smite-build
god: Horus
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Falcon
  aspect_pick_rate: 0.01
  aspect_win_rate: 0.69
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.21
    win_rate: 0.54
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.16
      win_rate: 0.53
    - name: Runeforged Hammer
      pick_rate: 0.15
      win_rate: 0.61
  - name: Genji's Guard
    pick_rate: 0.24
    win_rate: 0.57
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.54
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.65
  - name: Breastplate of Valor
    pick_rate: 0.12
    win_rate: 0.51
    alternates:
    - name: Genji's Guard
      pick_rate: 0.21
      win_rate: 0.59
    - name: Shell of Rebuke
      pick_rate: 0.11
      win_rate: 0.63
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.68
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.62
    - name: Breastplate of Valor
      pick_rate: 0.06
      win_rate: 0.59
  - name: Freya's Tears
    pick_rate: 0.07
    win_rate: 0.69
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.53
    - name: Spirit Robe
      pick_rate: 0.05
      win_rate: 0.64
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.62
    alternates:
    - name: Veve Charm
      pick_rate: 0.06
      win_rate: 0.52
    - name: Shield
      pick_rate: 0.05
      win_rate: 0.82
  community_starters:
  - name: Warrior's Axe
    pick_rate: 0.25
    win_rate: 0.55
  - name: Selflessness
    pick_rate: 0.19
    win_rate: 0.57
  - name: Bluestone Pendant
    pick_rate: 0.13
    win_rate: 0.57
  source_url: https://smitebrain.com/gods/horus/
  last_verified: '2026-08-21'
  god_win_rate: 0.5733610822060354
  god_matches_won: 551
  god_matches_played: 961
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-21'
  god_matches_analyzed: 12786
  starter:
    base: Death's Toll
    upgrade: Death's Embrace
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Berserker''s Shield, Jotunn''s Revenge,
    Shield of the Phoenix, Erosion, Eye of Providence, Shield Splitter, Draconic Scale,
    Mantle Of Discord, Stone of Binding, Spectral Armor, Runeforged Hammer, Eye of
    the Storm, Leviathan''s Hide, Pharaoh''s Curse, Screeching Gargoyle, Magi''s Cloak,
    Prophetic Cloak, Shogun''s Ofuda, Midgardian Mail, Hydra''s Lament, Hide of the
    Nemean Lion, Gladiator''s Shield, Doublet of Binding, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.57
      pick: 0.33
      fit: 0.42
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.34
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.6
      win: 0.61
      pick: 0.0
      fit: 0.76
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.69
      pick: 0.15
      fit: 0.64
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.66
  starter: &id001
    base: Death's Toll
    upgrade: Death's Embrace
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Berserker''s
    Shield, Jotunn''s Revenge, Chandra''s Grace, Phoenix Feather, Erosion, Eye of
    Providence, Draconic Scale, Runeforged Hammer, Spectral Armor, Glorious Pridwen,
    Shield Splitter, Mantle Of Discord, Stone of Binding, Yogi''s Necklace, Eye of
    the Storm, Leviathan''s Hide, Pharaoh''s Curse, The Reaper, Shogun''s Ofuda, Midgardian
    Mail, Screeching Gargoyle, Hide of the Nemean Lion, Gladiator''s Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.46
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.34
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.6
      win: 0.61
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.62
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.94
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.69
      pick: 0.15
      fit: 0.59
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Stone of Binding, Kinetic Cuirass,
    Berserker''s Shield, Screeching Gargoyle, The Crusher, Void Shield, Void Stone,
    Shield of the Phoenix, Avenging Blade, Heartseeker, The Reaper, Mantle Of Discord,
    Runeforged Hammer, Shield Splitter, Erosion, Eye of Providence, Spectral Armor,
    Draconic Scale, Titan''s Bane, Leviathan''s Hide, Pharaoh''s Curse, Silverbranch
    Bow, Toxic Blade, Eye of the Storm.'
  slot_scores:
    Stone of Binding:
      total: 0.57
      efficiency: 0.54
      win: 0.61
      pick: 0.0
      fit: 0.72
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.3
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.6
      win: 0.61
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.69
      pick: 0.15
      fit: 0.45
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.46
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Amanita Charm
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass,
    Golden Blade, Pharaoh''s Curse, Runeforged Hammer, Tyrfing, Shogun''s Ofuda, Shield
    of the Phoenix, Shield Splitter, Riptalon, Lernaean Bow, Mantle Of Discord, Stone
    of Binding, Silverbranch Bow, Hydra''s Lament, The Crusher, Spectral Armor, Toxic
    Blade, Erosion, Eye of the Storm, Eye of Providence, Leviathan''s Hide, Draconic
    Scale, Screeching Gargoyle.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.24
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.69
      pick: 0.15
      fit: 0.34
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.35
    Pharaoh's Curse:
      total: 0.53
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Shield of the Phoenix, Kinetic Cuirass, Berserker''s Shield, Hydra''s Lament,
    Screeching Gargoyle, Runeforged Hammer, Shield Splitter, Mantle Of Discord, Stone
    of Binding, Prophetic Cloak, Gladiator''s Shield, Erosion, Spectral Armor, Eye
    of Providence, Chandra''s Grace, Arondight, Draconic Scale, Eye of the Storm,
    The Crusher, Leviathan''s Hide, Pharaoh''s Curse, Eye of Erebus, Magi''s Cloak,
    Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.57
      pick: 0.33
      fit: 0.48
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.28
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.6
      win: 0.61
      pick: 0.0
      fit: 0.53
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.69
      pick: 0.15
      fit: 0.63
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Berserker''s Shield,
    Jotunn''s Revenge, Shield of the Phoenix, Erosion, Eye of Providence, Shield Splitter,
    Draconic Scale, Mantle Of Discord, Stone of Binding, Spectral Armor, Eye of the
    Storm, Leviathan''s Hide, Pharaoh''s Curse, Runeforged Hammer, Screeching Gargoyle,
    Magi''s Cloak, Prophetic Cloak, Shogun''s Ofuda, Midgardian Mail, Hydra''s Lament,
    Hide of the Nemean Lion, Gladiator''s Shield, Doublet of Binding, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.57
      pick: 0.33
      fit: 0.42
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.34
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.6
      win: 0.61
      pick: 0.0
      fit: 0.76
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.69
      pick: 0.15
      fit: 0.64
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.66
  starter: *id001
---
