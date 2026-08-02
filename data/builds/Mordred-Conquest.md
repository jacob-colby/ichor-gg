---
type: smite-build
god: Mordred
mode: Conquest
builds:
- source: community
  aspect: Aspect of Rage
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.64
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.43
    win_rate: 0.57
    alternates:
    - name: Barbed Carver
      pick_rate: 0.2
      win_rate: 0.45
    - name: Bracer of The Abyss
      pick_rate: 0.08
      win_rate: 0.63
  - name: Shield of the Phoenix
    pick_rate: 0.17
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 0.58
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.53
  - name: Genji's Guard
    pick_rate: 0.18
    win_rate: 0.53
    alternates:
    - name: Shield of the Phoenix
      pick_rate: 0.14
      win_rate: 0.71
    - name: Gladiator's Shield
      pick_rate: 0.09
      win_rate: 0.67
  - name: Dwarven Plate
    pick_rate: 0.09
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.63
    - name: Gladiator's Shield
      pick_rate: 0.08
      win_rate: 0.5
  - name: Hide of the Nemean Lion
    pick_rate: 0.06
    win_rate: 0.65
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.12
      win_rate: 0.5
    - name: Draconic Scale
      pick_rate: 0.05
      win_rate: 0.67
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.31
    - name: Medal of Defense
      pick_rate: 0.06
      win_rate: 0.55
  source_url: https://smitebrain.com/gods/mordred/
  last_verified: '2026-08-01'
  god_win_rate: 0.5451977401129944
  god_matches_won: 193
  god_matches_played: 354
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Shifter's Shield
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - The Crusher
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, The Crusher, Runeforged Hammer, Jotunn''s
    Revenge, Berserker''s Shield, Eye of Providence, Blink Rune, Hydra''s Lament,
    Oni Hunter''s Garb, Shield Splitter, Avenging Blade, Eye of the Storm, Spectral
    Armor, Freya''s Tears, Breastplate of Valor, Mantle Of Discord, Erosion, Pharaoh''s
    Curse, Draconic Scale, Golden Blade, Lernaean Bow, Yogi''s Necklace, Leviathan''s
    Hide, The Reaper, Damaru.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.74
      win: 0.53
      pick: 0.18
      fit: 0.3
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.64
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.57
      win: 0.65
      pick: 0.06
      fit: 0.35
    Shifter's Shield:
      total: 0.56
      efficiency: 0.58
      win: 0.57
      pick: 0.43
      fit: 0.54
    The Crusher:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Blink Rune
  - Genji's Guard
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - Hide of the Nemean Lion
  - Blink Rune
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, The Crusher, Blink Rune, Kinetic Cuirass, Hydra''s Lament,
    Runeforged Hammer, Amanita Charm, Berserker''s Shield, Eye of Providence, Oni
    Hunter''s Garb, Breastplate of Valor, Avenging Blade, Freya''s Tears, Spectral
    Armor, Shield Splitter, Mantle Of Discord, Lernaean Bow, Eye of the Storm, Pharaoh''s
    Curse, Yogi''s Necklace, The Reaper, Golden Blade, Erosion, Heartseeker, Damaru,
    Draconic Scale.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Genji's Guard:
      total: 0.55
      efficiency: 0.74
      win: 0.53
      pick: 0.18
      fit: 0.27
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.48
    Hide of the Nemean Lion:
      total: 0.53
      efficiency: 0.57
      win: 0.65
      pick: 0.06
      fit: 0.25
    Shifter's Shield:
      total: 0.54
      efficiency: 0.58
      win: 0.57
      pick: 0.43
      fit: 0.38
    The Crusher:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Shield of the Phoenix
  - Hide of the Nemean Lion
  - Runeforged Hammer
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Genji's Guard
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Runeforged Hammer, Kinetic Cuirass, Jotunn''s Revenge,
    The Crusher, Berserker''s Shield, The Reaper, Eye of Providence, Blink Rune, Hydra''s
    Lament, Chandra''s Grace, Oni Hunter''s Garb, Avenging Blade, Eye of the Storm,
    Spectral Armor, Shield Splitter, Golden Blade, Riptalon, Phoenix Feather, Pharaoh''s
    Curse, Breastplate of Valor, Erosion, Yogi''s Necklace, Lernaean Bow, Freya''s
    Tears, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.74
      win: 0.53
      pick: 0.18
      fit: 0.27
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.61
      win: 0.5
      pick: 0.17
      fit: 0.77
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.57
      win: 0.65
      pick: 0.06
      fit: 0.36
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.51
    Shifter's Shield:
      total: 0.56
      efficiency: 0.58
      win: 0.57
      pick: 0.43
      fit: 0.52
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.82
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Genji's Guard
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - Genji's Guard
  - Hide of the Nemean Lion
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
    for this god: The Crusher, Jotunn''s Revenge, Avenging Blade, Kinetic Cuirass,
    Blink Rune, Amanita Charm, Runeforged Hammer, Berserker''s Shield, Hydra''s Lament,
    Eye of Providence, Oni Hunter''s Garb, The Reaper, Shield Splitter, Spectral Armor,
    Stone of Binding, Void Shield, Heartseeker, Breastplate of Valor, Eye of the Storm,
    Screeching Gargoyle, Mantle Of Discord, Freya''s Tears, Lernaean Bow, Pharaoh''s
    Curse, Avatar''s Parashu, Void Stone.'
  slot_scores:
    Avenging Blade:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.69
    Genji's Guard:
      total: 0.54
      efficiency: 0.74
      win: 0.53
      pick: 0.18
      fit: 0.24
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.56
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.57
      win: 0.65
      pick: 0.06
      fit: 0.28
    Shifter's Shield:
      total: 0.55
      efficiency: 0.58
      win: 0.57
      pick: 0.43
      fit: 0.44
    The Crusher:
      total: 0.56
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.58
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
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, The Crusher, Runeforged
    Hammer, Jotunn''s Revenge, Berserker''s Shield, Eye of Providence, Blink Rune,
    Hydra''s Lament, Oni Hunter''s Garb, Shield Splitter, Avenging Blade, Eye of the
    Storm, Spectral Armor, Freya''s Tears, Breastplate of Valor, Mantle Of Discord,
    Erosion, Pharaoh''s Curse, Draconic Scale, Golden Blade, Lernaean Bow, Yogi''s
    Necklace, Leviathan''s Hide, The Reaper, Damaru.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.64
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.46
    The Crusher:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: *id001
---
