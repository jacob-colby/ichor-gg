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
  - Amanita Charm
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Kinetic Cuirass, Amanita Charm, Eye of Providence,
    Berserker''s Shield, Oni Hunter''s Garb, Shield of the Phoenix, Freya''s Tears,
    Blink Rune, Runeforged Hammer, Hydra''s Lament, Spectral Armor, Erosion, Jotunn''s
    Revenge, Draconic Scale, Mantle Of Discord, Pharaoh''s Curse, Shield Splitter,
    The Crusher, Eye of the Storm, Avenging Blade, Leviathan''s Hide, Yogi''s Necklace,
    Hussar''s Wings, Chandra''s Grace, Gladiator''s Shield, Midgardian Mail.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.66
    Genji's Guard:
      total: 0.61
      efficiency: 0.74
      win: 0.63
      pick: 0.19
      fit: 0.42
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.67
      win: 0.71
      pick: 0.07
      fit: 0.42
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.76
    Shifter's Shield:
      total: 0.62
      efficiency: 0.58
      win: 0.66
      pick: 0.37
      fit: 0.66
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
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
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Kinetic
    Cuirass, Berserker''s Shield, Eye of Providence, Chandra''s Grace, Oni Hunter''s
    Garb, Runeforged Hammer, Blink Rune, Spectral Armor, Hydra''s Lament, Freya''s
    Tears, Erosion, Jotunn''s Revenge, Phoenix Feather, Pharaoh''s Curse, Draconic
    Scale, Avenging Blade, Eye of the Storm, Mantle Of Discord, The Crusher, Yogi''s
    Necklace, Leviathan''s Hide, Shield Splitter, The Reaper, Spirit Robe.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.74
      win: 0.63
      pick: 0.19
      fit: 0.39
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.67
      win: 0.71
      pick: 0.07
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.94
    Shifter's Shield:
      total: 0.62
      efficiency: 0.58
      win: 0.66
      pick: 0.37
      fit: 0.66
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - The Crusher
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Breastplate of Valor, Jotunn''s Revenge, The Crusher, Avenging Blade,
    Kinetic Cuirass, Amanita Charm, Blink Rune, Berserker''s Shield, Eye of Providence,
    Oni Hunter''s Garb, Runeforged Hammer, Hydra''s Lament, Shield of the Phoenix,
    Spectral Armor, Void Shield, Screeching Gargoyle, Stone of Binding, Freya''s Tears,
    The Reaper, Mantle Of Discord, Pharaoh''s Curse, Void Stone, Yogi''s Necklace,
    Erosion, Riptalon, Heartseeker, Draconic Scale.'
  slot_scores:
    Avenging Blade:
      total: 0.53
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.6
    Genji's Guard:
      total: 0.59
      efficiency: 0.74
      win: 0.63
      pick: 0.19
      fit: 0.29
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.67
      win: 0.71
      pick: 0.07
      fit: 0.29
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.54
    Shifter's Shield:
      total: 0.59
      efficiency: 0.58
      win: 0.66
      pick: 0.37
      fit: 0.46
    The Crusher:
      total: 0.55
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.51
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Berserker's Shield
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Demon Blade
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: For fun — deliberately fights this god's kit (Crit / attack-speed party
    build). Scored on gold-value + flavor fit only; not meta-checked.
  slot_scores:
    Golden Blade:
      total: 0.3
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.57
    Lernaean Bow:
      total: 0.33
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.67
    Berserker's Shield:
      total: 0.31
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.34
    Death Metal:
      total: 0.32
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.33
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.31
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Eye of Providence, Berserker''s
    Shield, Oni Hunter''s Garb, Shield of the Phoenix, Freya''s Tears, Blink Rune,
    Runeforged Hammer, Hydra''s Lament, Breastplate of Valor, Spectral Armor, Erosion,
    Jotunn''s Revenge, Draconic Scale, Mantle Of Discord, Pharaoh''s Curse, Shield
    Splitter, The Crusher, Eye of the Storm, Avenging Blade, Leviathan''s Hide, Yogi''s
    Necklace, Hussar''s Wings, Chandra''s Grace, Gladiator''s Shield, Midgardian Mail.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.66
    Genji's Guard:
      total: 0.61
      efficiency: 0.74
      win: 0.63
      pick: 0.19
      fit: 0.42
    Berserker's Shield:
      total: 0.55
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.76
    Oni Hunter's Garb:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.43
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
---
