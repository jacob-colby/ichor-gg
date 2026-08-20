---
type: smite-build
god: Horus
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Falcon
  aspect_pick_rate: 0.02
  aspect_win_rate: 0.69
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.21
    win_rate: 0.53
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.16
      win_rate: 0.51
    - name: Runeforged Hammer
      pick_rate: 0.15
      win_rate: 0.61
  - name: Genji's Guard
    pick_rate: 0.25
    win_rate: 0.56
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.55
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.66
  - name: Breastplate of Valor
    pick_rate: 0.12
    win_rate: 0.49
    alternates:
    - name: Genji's Guard
      pick_rate: 0.21
      win_rate: 0.6
    - name: Shell of Rebuke
      pick_rate: 0.11
      win_rate: 0.61
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.66
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.63
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.59
  - name: Freya's Tears
    pick_rate: 0.07
    win_rate: 0.69
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.53
    - name: Draconic Scale
      pick_rate: 0.05
      win_rate: 0.67
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.62
    alternates:
    - name: Shield
      pick_rate: 0.06
      win_rate: 0.82
    - name: Veve Charm
      pick_rate: 0.06
      win_rate: 0.55
  community_starters:
  - name: Warrior's Axe
    pick_rate: 0.25
    win_rate: 0.53
  - name: Selflessness
    pick_rate: 0.2
    win_rate: 0.57
  - name: Bluestone Pendant
    pick_rate: 0.13
    win_rate: 0.57
  source_url: https://smitebrain.com/gods/horus/
  last_verified: '2026-08-20'
  god_win_rate: 0.5686046511627907
  god_matches_won: 489
  god_matches_played: 860
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-20'
  god_matches_analyzed: 11556
  starter:
    base: Death's Toll
    upgrade: Death's Embrace
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Berserker's Shield
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
    this god: Kinetic Cuirass, Amanita Charm, Draconic Scale, Berserker''s Shield,
    Shield of the Phoenix, Erosion, Oni Hunter''s Garb, Eye of Providence, Jotunn''s
    Revenge, Spectral Armor, The Crusher, Shield Splitter, Runeforged Hammer, Pharaoh''s
    Curse, Leviathan''s Hide, Eye of the Storm, Midgardian Mail, Gladiator''s Shield,
    Hydra''s Lament, Mantle Of Discord, Screeching Gargoyle, Stone of Binding, Prophetic
    Cloak, Ancile, Chandra''s Grace, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.56
      pick: 0.34
      fit: 0.42
    Berserker's Shield:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.76
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.69
      pick: 0.15
      fit: 0.64
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.67
      pick: 0.11
      fit: 0.66
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
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
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Draconic Scale
  - Berserker's Shield
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
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Draconic Scale,
    Berserker''s Shield, Chandra''s Grace, Oni Hunter''s Garb, Yogi''s Necklace, Erosion,
    Eye of Providence, Phoenix Feather, Jotunn''s Revenge, Spectral Armor, Runeforged
    Hammer, The Crusher, Glorious Pridwen, Pharaoh''s Curse, Leviathan''s Hide, Eye
    of the Storm, Midgardian Mail, Gladiator''s Shield, Shield Splitter, Hydra''s
    Lament, The Reaper, Ancile, Shogun''s Ofuda.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.61
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.94
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.69
      pick: 0.15
      fit: 0.59
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.67
      pick: 0.11
      fit: 0.66
    Amanita Charm:
      total: 0.64
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, Kinetic Cuirass, Amanita Charm,
    Draconic Scale, Screeching Gargoyle, Berserker''s Shield, Stone of Binding, Void
    Shield, Shield of the Phoenix, Oni Hunter''s Garb, Avenging Blade, Void Stone,
    Erosion, Spectral Armor, Eye of Providence, Runeforged Hammer, The Reaper, Hydra''s
    Lament, Riptalon, Heartseeker, Pharaoh''s Curse, Shield Splitter, Leviathan''s
    Hide, Silverbranch Bow, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.56
      pick: 0.34
      fit: 0.29
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.64
      win: 0.61
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.69
      pick: 0.15
      fit: 0.45
    The Crusher:
      total: 0.58
      efficiency: 0.64
      win: 0.61
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.46
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Kinetic Cuirass, Amanita Charm, Golden Blade, The
    Crusher, Draconic Scale, Jotunn''s Revenge, Pharaoh''s Curse, Riptalon, Oni Hunter''s
    Garb, Shield of the Phoenix, Runeforged Hammer, Tyrfing, Shogun''s Ofuda, Hydra''s
    Lament, Silverbranch Bow, Lernaean Bow, Spectral Armor, Erosion, Shield Splitter,
    Eye of Providence, Eye of the Storm, Dominance, Leviathan''s Hide, Toxic Blade,
    Midgardian Mail.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.69
      pick: 0.15
      fit: 0.34
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
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
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hydra's Lament
  - Freya's Tears
  flex_slots:
  - Kinetic Cuirass
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Shield of the Phoenix,
    Kinetic Cuirass, Amanita Charm, Hydra''s Lament, Berserker''s Shield, Draconic
    Scale, The Crusher, Screeching Gargoyle, Oni Hunter''s Garb, Chandra''s Grace,
    Gladiator''s Shield, Runeforged Hammer, Erosion, Spectral Armor, Prophetic Cloak,
    Eye of Providence, Shield Splitter, Pharaoh''s Curse, Eye of the Storm, Leviathan''s
    Hide, Midgardian Mail, Arondight, Mantle Of Discord, Stone of Binding, Glorious
    Pridwen.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.56
      pick: 0.34
      fit: 0.48
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.61
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.53
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.61
    Hydra's Lament:
      total: 0.55
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.53
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.69
      pick: 0.15
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Breastplate of Valor
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Shield of the Phoenix, Erosion, Oni Hunter''s Garb, Eye of Providence, Jotunn''s
    Revenge, Draconic Scale, Spectral Armor, The Crusher, Shield Splitter, Pharaoh''s
    Curse, Leviathan''s Hide, Eye of the Storm, Midgardian Mail, Gladiator''s Shield,
    Hydra''s Lament, Runeforged Hammer, Mantle Of Discord, Screeching Gargoyle, Stone
    of Binding, Prophetic Cloak, Ancile, Chandra''s Grace, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.56
      pick: 0.34
      fit: 0.42
    Berserker's Shield:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.64
      win: 0.49
      pick: 0.19
      fit: 0.42
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.76
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.69
      pick: 0.15
      fit: 0.64
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.66
  starter: *id001
---
