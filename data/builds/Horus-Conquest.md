---
type: smite-build
god: Horus
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Falcon
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.0
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.37
    win_rate: 0.66
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.19
      win_rate: 0.56
    - name: Gauntlet of Thebes
      pick_rate: 0.1
      win_rate: 0.63
  - name: Genji's Guard
    pick_rate: 0.19
    win_rate: 0.63
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 0.51
    - name: Breastplate of Valor
      pick_rate: 0.12
      win_rate: 0.6
  - name: Shell of Rebuke
    pick_rate: 0.1
    win_rate: 0.69
    alternates:
    - name: Genji's Guard
      pick_rate: 0.29
      win_rate: 0.57
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.6
  - name: Breastplate of Valor
    pick_rate: 0.07
    win_rate: 0.71
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.6
    - name: Shell of Rebuke
      pick_rate: 0.12
      win_rate: 0.64
  - name: Dwarven Plate
    pick_rate: 0.08
    win_rate: 0.74
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.39
    - name: Spirit Robe
      pick_rate: 0.06
      win_rate: 0.72
  - name: Shield
    pick_rate: 0.06
    win_rate: 0.8
    alternates:
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.5
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.44
  source_url: https://smitebrain.com/gods/horus/
  last_verified: '2026-08-01'
  god_win_rate: 0.6051948051948052
  god_matches_won: 233
  god_matches_played: 385
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Death's Toll
    upgrade: Death's Embrace
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Dwarven Plate — magical protection
    swap_item: Dwarven Plate
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Amanita Charm, Kinetic Cuirass, Eye of Providence,
    Berserker''s Shield, Freya''s Tears, Shield of the Phoenix, Oni Hunter''s Garb,
    Erosion, Jotunn''s Revenge, Draconic Scale, Spectral Armor, Shield Splitter, Hydra''s
    Lament, Pharaoh''s Curse, The Crusher, Eye of the Storm, Leviathan''s Hide, Midgardian
    Mail, Gladiator''s Shield, Yogi''s Necklace, Hide of the Nemean Lion, Stone of
    Binding, Mantle Of Discord, Screeching Gargoyle, Shogun''s Ofuda.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.66
    Genji's Guard:
      total: 0.61
      efficiency: 0.72
      win: 0.63
      pick: 0.19
      fit: 0.42
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.71
      pick: 0.07
      fit: 0.42
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.76
    Shifter's Shield:
      total: 0.61
      efficiency: 0.56
      win: 0.66
      pick: 0.37
      fit: 0.66
    Amanita Charm:
      total: 0.56
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: &id001
    base: Death's Toll
    upgrade: Death's Embrace
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Kinetic
    Cuirass, Eye of Providence, Berserker''s Shield, Chandra''s Grace, Oni Hunter''s
    Garb, Freya''s Tears, Erosion, Jotunn''s Revenge, Phoenix Feather, Draconic Scale,
    Spectral Armor, Pharaoh''s Curse, Hydra''s Lament, Eye of the Storm, Glorious
    Pridwen, Shield Splitter, The Crusher, Yogi''s Necklace, Leviathan''s Hide, Midgardian
    Mail, Gladiator''s Shield, Hide of the Nemean Lion, The Reaper.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.72
      win: 0.63
      pick: 0.19
      fit: 0.39
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.71
      pick: 0.07
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.94
    Shifter's Shield:
      total: 0.61
      efficiency: 0.56
      win: 0.66
      pick: 0.37
      fit: 0.66
    Amanita Charm:
      total: 0.6
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shifter's Shield
  - The Crusher
  - Amanita Charm
  flex_slots:
  - The Crusher
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Breastplate of Valor, Jotunn''s Revenge, The Crusher, Amanita Charm,
    Kinetic Cuirass, Berserker''s Shield, Eye of Providence, Stone of Binding, Screeching
    Gargoyle, Avenging Blade, Oni Hunter''s Garb, Freya''s Tears, Void Shield, Shield
    of the Phoenix, Void Stone, Hydra''s Lament, Erosion, Spectral Armor, The Reaper,
    Pharaoh''s Curse, Riptalon, Shield Splitter, Draconic Scale, Yogi''s Necklace,
    Silverbranch Bow, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.72
      win: 0.63
      pick: 0.19
      fit: 0.29
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.65
      win: 0.71
      pick: 0.07
      fit: 0.29
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.54
    Shifter's Shield:
      total: 0.58
      efficiency: 0.56
      win: 0.66
      pick: 0.37
      fit: 0.46
    The Crusher:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.53
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.46
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Shifter's Shield
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    this god: Breastplate of Valor, Berserker''s Shield, Amanita Charm, Kinetic Cuirass,
    Golden Blade, Eye of Providence, Pharaoh''s Curse, Jotunn''s Revenge, The Crusher,
    Oni Hunter''s Garb, Riptalon, Hydra''s Lament, Lernaean Bow, Freya''s Tears, Tyrfing,
    Shield of the Phoenix, Shogun''s Ofuda, Silverbranch Bow, Shield Splitter, Spectral
    Armor, Yogi''s Necklace, Erosion, Eye of the Storm, Dominance, Draconic Scale,
    Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.58
      efficiency: 0.72
      win: 0.63
      pick: 0.19
      fit: 0.22
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.65
      win: 0.71
      pick: 0.07
      fit: 0.22
    Shifter's Shield:
      total: 0.56
      efficiency: 0.56
      win: 0.66
      pick: 0.37
      fit: 0.35
    Pharaoh's Curse:
      total: 0.49
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Runeforged Hammer
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Jotunn's Revenge
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Freya''s Tears,
    Jotunn''s Revenge, Amanita Charm, Shield of the Phoenix, Hydra''s Lament, Kinetic
    Cuirass, Berserker''s Shield, Eye of Providence, Oni Hunter''s Garb, The Crusher,
    Screeching Gargoyle, Chandra''s Grace, Gladiator''s Shield, Spectral Armor, Erosion,
    Shield Splitter, Prophetic Cloak, Yogi''s Necklace, Pharaoh''s Curse, Draconic
    Scale, Eye of the Storm, Arondight, Leviathan''s Hide, Midgardian Mail, Avenging
    Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.62
      efficiency: 0.72
      win: 0.63
      pick: 0.19
      fit: 0.48
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.65
      win: 0.71
      pick: 0.07
      fit: 0.48
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.47
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.61
      win: 0.56
      pick: 0.19
      fit: 0.33
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.63
    Shifter's Shield:
      total: 0.58
      efficiency: 0.56
      win: 0.66
      pick: 0.37
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Berserker''s
    Shield, Freya''s Tears, Shield of the Phoenix, Oni Hunter''s Garb, Breastplate
    of Valor, Erosion, Jotunn''s Revenge, Draconic Scale, Spectral Armor, Shield Splitter,
    Hydra''s Lament, Pharaoh''s Curse, The Crusher, Eye of the Storm, Leviathan''s
    Hide, Midgardian Mail, Gladiator''s Shield, Yogi''s Necklace, Hide of the Nemean
    Lion, Stone of Binding, Mantle Of Discord, Screeching Gargoyle, Shogun''s Ofuda.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.66
    Genji's Guard:
      total: 0.61
      efficiency: 0.72
      win: 0.63
      pick: 0.19
      fit: 0.42
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.76
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Amanita Charm:
      total: 0.56
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
---
