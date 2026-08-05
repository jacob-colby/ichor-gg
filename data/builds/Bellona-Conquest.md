---
type: smite-build
god: Bellona
mode: Conquest
builds:
- source: community
  aspect: Aspect of Vindication
  aspect_pick_rate: 0.22
  aspect_win_rate: 0.49
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.4
    win_rate: 0.48
    alternates:
    - name: Golden Blade
      pick_rate: 0.17
      win_rate: 0.48
    - name: Berserker's Shield
      pick_rate: 0.16
      win_rate: 0.58
  - name: Berserker's Shield
    pick_rate: 0.31
    win_rate: 0.46
    alternates:
    - name: Golden Blade
      pick_rate: 0.16
      win_rate: 0.52
    - name: Shogun's Ofuda
      pick_rate: 0.14
      win_rate: 0.23
  - name: Kinetic Cuirass
    pick_rate: 0.17
    win_rate: 0.59
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.19
      win_rate: 0.48
    - name: Shogun's Ofuda
      pick_rate: 0.17
      win_rate: 0.5
  - name: Dwarven Plate
    pick_rate: 0.16
    win_rate: 0.54
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.15
      win_rate: 0.35
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 0.31
  - name: Hide of the Nemean Lion
    pick_rate: 0.09
    win_rate: 0.58
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.08
      win_rate: 0.64
    - name: Engraved Guard
      pick_rate: 0.08
      win_rate: 0.36
  - name: Hunter's Bow
    pick_rate: 0.08
    win_rate: 0.17
    alternates:
    - name: Medal of Defense
      pick_rate: 0.06
      win_rate: 0.4
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.75
  source_url: https://smitebrain.com/gods/bellona/
  last_verified: '2026-08-01'
  god_win_rate: 0.46875
  god_matches_won: 75
  god_matches_played: 160
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
  - Eye of Providence
  - Berserker's Shield
  - Kinetic Cuirass
  - Hydra's Lament
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Runeforged Hammer, Eye of Providence, Hydra''s Lament,
    Genji''s Guard, Shield Splitter, Oni Hunter''s Garb, Jotunn''s Revenge, The Crusher,
    Eye of the Storm, Avenging Blade, Spectral Armor, Shield of the Phoenix, Freya''s
    Tears, Mantle Of Discord, Erosion, Breastplate of Valor, Draconic Scale, Pharaoh''s
    Curse, Golden Blade, Lernaean Bow, Yogi''s Necklace, Leviathan''s Hide, Wyrmskin
    Hide, Damaru.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.54
      efficiency: 0.74
      win: 0.46
      pick: 0.31
      fit: 0.38
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.64
      win: 0.59
      pick: 0.17
      fit: 0.7
    Hydra's Lament:
      total: 0.53
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.45
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.6
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Runeforged Hammer, Eye of Providence,
    Hydra''s Lament, Chandra''s Grace, Oni Hunter''s Garb, Jotunn''s Revenge, Avenging
    Blade, The Crusher, Genji''s Guard, Eye of the Storm, The Reaper, Shield Splitter,
    Spectral Armor, Golden Blade, Phoenix Feather, Pharaoh''s Curse, Erosion, Breastplate
    of Valor, Draconic Scale, Freya''s Tears, Lernaean Bow, Yogi''s Necklace, Mantle
    Of Discord.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.58
    Berserker's Shield:
      total: 0.54
      efficiency: 0.74
      win: 0.46
      pick: 0.31
      fit: 0.4
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.64
      win: 0.59
      pick: 0.17
      fit: 0.68
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.82
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Jotunn''s Revenge, Avenging Blade, Runeforged Hammer,
    Amanita Charm, Hydra''s Lament, Genji''s Guard, Eye of Providence, Oni Hunter''s
    Garb, The Reaper, Shield Splitter, Spectral Armor, Stone of Binding, Void Shield,
    Heartseeker, Eye of the Storm, Breastplate of Valor, Shield of the Phoenix, Screeching
    Gargoyle, Mantle Of Discord, Lernaean Bow, Freya''s Tears, Avatar''s Parashu,
    Pharaoh''s Curse, Golden Blade.'
  slot_scores:
    Avenging Blade:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.7
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.57
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.64
      win: 0.59
      pick: 0.17
      fit: 0.53
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.4
    The Crusher:
      total: 0.56
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.43
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
      win: 0.46
      pick: 0.31
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
  - Berserker's Shield
  - Kinetic Cuirass
  - Hydra's Lament
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Runeforged Hammer, Eye of Providence,
    Hydra''s Lament, Genji''s Guard, Shield Splitter, Oni Hunter''s Garb, Jotunn''s
    Revenge, The Crusher, Eye of the Storm, Avenging Blade, Spectral Armor, Shield
    of the Phoenix, Freya''s Tears, Mantle Of Discord, Erosion, Breastplate of Valor,
    Draconic Scale, Pharaoh''s Curse, Golden Blade, Lernaean Bow, Yogi''s Necklace,
    Leviathan''s Hide, Wyrmskin Hide, Damaru.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.54
      efficiency: 0.74
      win: 0.46
      pick: 0.31
      fit: 0.38
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.64
      win: 0.59
      pick: 0.17
      fit: 0.7
    Hydra's Lament:
      total: 0.53
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.45
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.6
  starter: *id001
---
