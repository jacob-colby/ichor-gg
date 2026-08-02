---
type: smite-build
god: Chaac
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fulmination
  aspect_pick_rate: 0.2
  aspect_win_rate: 0.44
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.48
    win_rate: 0.62
    alternates:
    - name: Transcendence
      pick_rate: 0.09
      win_rate: 0.75
    - name: Mystical Mail
      pick_rate: 0.05
      win_rate: 0.5
  - name: Genji's Guard
    pick_rate: 0.14
    win_rate: 0.33
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.67
    - name: Mystical Mail
      pick_rate: 0.11
      win_rate: 0.6
  - name: The World Stone
    pick_rate: 0.09
    win_rate: 0.75
    alternates:
    - name: Genji's Guard
      pick_rate: 0.19
      win_rate: 0.63
    - name: Shield of the Phoenix
      pick_rate: 0.09
      win_rate: 0.5
  - name: Spirit Robe
    pick_rate: 0.15
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.75
    - name: Rod of Tahuti
      pick_rate: 0.07
      win_rate: 0.67
  - name: Heartseeker
    pick_rate: 0.08
    win_rate: 1.0
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.08
      win_rate: 0.0
    - name: Jotunn's Revenge
      pick_rate: 0.05
      win_rate: 0.5
  - name: Killing Stone
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Triton's Conch
      pick_rate: 0.08
      win_rate: 1.0
    - name: Circle of Protection
      pick_rate: 0.08
      win_rate: 0.5
  source_url: https://smitebrain.com/gods/chaac/
  last_verified: '2026-08-01'
  god_win_rate: 0.6136363636363636
  god_matches_won: 27
  god_matches_played: 44
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - The Crusher
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - The Crusher
  - Jotunn's Revenge
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
    this god: Kinetic Cuirass, Amanita Charm, The Crusher, Jotunn''s Revenge, Runeforged
    Hammer, Berserker''s Shield, Eye of Providence, Blink Rune, Hydra''s Lament, Oni
    Hunter''s Garb, Shield Splitter, Avenging Blade, Eye of the Storm, Spectral Armor,
    Shield of the Phoenix, Freya''s Tears, Breastplate of Valor, Mantle Of Discord,
    Erosion, Pharaoh''s Curse, Draconic Scale, Golden Blade, Lernaean Bow, Yogi''s
    Necklace, The Reaper, Leviathan''s Hide, Damaru, Genji''s Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.63
    Shifter's Shield:
      total: 0.58
      efficiency: 0.58
      win: 0.62
      pick: 0.48
      fit: 0.53
    The Crusher:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.48
    Heartseeker:
      total: 0.71
      efficiency: 0.53
      win: 1.0
      pick: 0.08
      fit: 0.48
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.53
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: burst
  slot_order:
  - Blink Rune
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - The Crusher
  - Heartseeker
  flex_slots:
  - Blink Rune
  - Kinetic Cuirass
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Heartseeker, Jotunn''s Revenge, The Crusher, Blink Rune, Kinetic Cuirass,
    Hydra''s Lament, Runeforged Hammer, Amanita Charm, Berserker''s Shield, Eye of
    Providence, Oni Hunter''s Garb, Breastplate of Valor, Shield of the Phoenix, Avenging
    Blade, Freya''s Tears, Spectral Armor, Shield Splitter, Mantle Of Discord, Lernaean
    Bow, Eye of the Storm, Pharaoh''s Curse, Yogi''s Necklace, The Reaper, Golden
    Blade, Erosion, Damaru, Draconic Scale, Genji''s Guard.'
  slot_scores:
    Blink Rune:
      total: 0.53
      efficiency: 0.87
      win: 0.5
      pick: 0.0
      fit: 0.0
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.48
    Shifter's Shield:
      total: 0.56
      efficiency: 0.58
      win: 0.62
      pick: 0.48
      fit: 0.38
    The Crusher:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.44
    Heartseeker:
      total: 0.71
      efficiency: 0.53
      win: 1.0
      pick: 0.08
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Shield of the Phoenix
  - Runeforged Hammer
  - Shifter's Shield
  - The Crusher
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - The Crusher
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
    this god: Amanita Charm, Shield of the Phoenix, Runeforged Hammer, The Crusher,
    Jotunn''s Revenge, Kinetic Cuirass, The Reaper, Berserker''s Shield, Blink Rune,
    Eye of Providence, Hydra''s Lament, Chandra''s Grace, Oni Hunter''s Garb, Avenging
    Blade, Eye of the Storm, Spectral Armor, Riptalon, Shield Splitter, Golden Blade,
    Phoenix Feather, Pharaoh''s Curse, Breastplate of Valor, Yogi''s Necklace, Lernaean
    Bow, Erosion, Freya''s Tears, Draconic Scale, Genji''s Guard.'
  slot_scores:
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.75
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.5
    Shifter's Shield:
      total: 0.58
      efficiency: 0.58
      win: 0.62
      pick: 0.48
      fit: 0.51
    The Crusher:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.49
    Heartseeker:
      total: 0.71
      efficiency: 0.53
      win: 1.0
      pick: 0.08
      fit: 0.49
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.81
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - The Crusher
  - Heartseeker
  flex_slots:
  - Avenging Blade
  - Kinetic Cuirass
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Heartseeker, The Crusher, Jotunn''s Revenge, Avenging Blade, Kinetic
    Cuirass, Blink Rune, Amanita Charm, Runeforged Hammer, Berserker''s Shield, Hydra''s
    Lament, Eye of Providence, Oni Hunter''s Garb, The Reaper, Shield Splitter, Spectral
    Armor, Stone of Binding, Void Shield, Breastplate of Valor, Eye of the Storm,
    Shield of the Phoenix, Screeching Gargoyle, Mantle Of Discord, Freya''s Tears,
    Lernaean Bow, Pharaoh''s Curse, Avatar''s Parashu, Void Stone, Genji''s Guard.'
  slot_scores:
    Avenging Blade:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.69
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.56
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.54
    Shifter's Shield:
      total: 0.57
      efficiency: 0.58
      win: 0.62
      pick: 0.48
      fit: 0.44
    The Crusher:
      total: 0.56
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.58
    Heartseeker:
      total: 0.73
      efficiency: 0.53
      win: 1.0
      pick: 0.08
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
  - Runeforged Hammer
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
    Underrated for this god: Kinetic Cuirass, Amanita Charm, The Crusher, Jotunn''s
    Revenge, Runeforged Hammer, Berserker''s Shield, Eye of Providence, Blink Rune,
    Hydra''s Lament, Genji''s Guard, Oni Hunter''s Garb, Shield Splitter, Avenging
    Blade, Eye of the Storm, Spectral Armor, Shield of the Phoenix, Freya''s Tears,
    Breastplate of Valor, Mantle Of Discord, Erosion, Pharaoh''s Curse, Draconic Scale,
    Golden Blade, Lernaean Bow, Yogi''s Necklace, The Reaper, Leviathan''s Hide, Damaru.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.63
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.45
    The Crusher:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.48
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.53
  starter: *id001
---
