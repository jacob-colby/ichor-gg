---
type: smite-build
god: Xbalanque
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Nightstalker
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.57
  slot_order:
  - name: Tyrfing
    pick_rate: 0.48
    win_rate: 0.63
    alternates:
    - name: Dominance
      pick_rate: 0.13
      win_rate: 0.64
    - name: Transcendence
      pick_rate: 0.11
      win_rate: 0.53
  - name: Odysseus' Bow
    pick_rate: 0.38
    win_rate: 0.6
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.1
      win_rate: 0.66
    - name: Dominance
      pick_rate: 0.09
      win_rate: 0.61
  - name: Dominance
    pick_rate: 0.18
    win_rate: 0.63
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.21
      win_rate: 0.7
    - name: Hastened Fatalis
      pick_rate: 0.11
      win_rate: 0.49
  - name: The Executioner
    pick_rate: 0.18
    win_rate: 0.69
    alternates:
    - name: Riptalon
      pick_rate: 0.13
      win_rate: 0.62
    - name: Dominance
      pick_rate: 0.1
      win_rate: 0.61
  - name: Qin's Blade
    pick_rate: 0.1
    win_rate: 0.81
    alternates:
    - name: The Executioner
      pick_rate: 0.1
      win_rate: 0.54
    - name: Hunter's Bow
      pick_rate: 0.08
      win_rate: 0.61
  - name: Riptalon
    pick_rate: 0.13
    win_rate: 0.67
    alternates:
    - name: Manchu Bow
      pick_rate: 0.12
      win_rate: 0.71
    - name: Hunter's Bow
      pick_rate: 0.11
      win_rate: 0.46
  source_url: https://smitebrain.com/gods/xbalanque/
  last_verified: '2026-08-01'
  god_win_rate: 0.6
  god_matches_won: 201
  god_matches_played: 335
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
  - Qin's Blade
  - Riptalon
  - Damaru
  flex_slots:
  - Lernaean Bow
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Damaru, Lernaean Bow, Golden Blade, Jotunn''s Revenge, Demon
    Blade, Hydra''s Lament, Runeforged Hammer, Rage, The Crusher, Berserker''s Shield,
    Avenging Blade, Eros'' Bow, Pharaoh''s Curse, Musashi''s Dual Swords, Shield Splitter,
    Barbed Carver, Spectral Armor, Eye of the Storm, Transcendence, Tekko-Kagi, Kinetic
    Cuirass, The Reaper, Shogun''s Ofuda, Eye of Providence, Heartseeker, Bloodforge.'
  slot_scores:
    Golden Blade:
      total: 0.44
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.54
    Lernaean Bow:
      total: 0.45
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.64
    Tyrfing:
      total: 0.53
      efficiency: 0.37
      win: 0.63
      pick: 0.48
      fit: 0.64
    Qin's Blade:
      total: 0.5
      efficiency: 0.19
      win: 0.81
      pick: 0.1
      fit: 0.43
    Riptalon:
      total: 0.49
      efficiency: 0.32
      win: 0.67
      pick: 0.13
      fit: 0.46
    Damaru:
      total: 0.45
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Tyrfing
  - Rage
  - Qin's Blade
  - Riptalon
  - Damaru
  - Demon Blade
  flex_slots:
  - Rage
  - Demon Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Damaru, Lernaean Bow, Jotunn''s Revenge, Golden Blade, Rage,
    Demon Blade, Hydra''s Lament, Runeforged Hammer, The Crusher, Musashi''s Dual
    Swords, Berserker''s Shield, Avenging Blade, Shield Splitter, Eros'' Bow, Pharaoh''s
    Curse, Barbed Carver, Spectral Armor, Eye of the Storm, Kinetic Cuirass, Transcendence,
    The Reaper, Eye of Providence, Heartseeker, Tekko-Kagi, Shogun''s Ofuda, Bloodforge.'
  slot_scores:
    Tyrfing:
      total: 0.53
      efficiency: 0.37
      win: 0.63
      pick: 0.48
      fit: 0.6
    Rage:
      total: 0.43
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.57
    Qin's Blade:
      total: 0.49
      efficiency: 0.19
      win: 0.81
      pick: 0.1
      fit: 0.4
    Riptalon:
      total: 0.49
      efficiency: 0.32
      win: 0.67
      pick: 0.13
      fit: 0.42
    Damaru:
      total: 0.46
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.57
    Demon Blade:
      total: 0.43
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Tyrfing
  - Qin's Blade
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Eye
    of Providence, Chandra''s Grace, Phoenix Feather, Berserker''s Shield, Runeforged
    Hammer, Spectral Armor, Golden Blade, Shield Splitter, Pharaoh''s Curse, Jotunn''s
    Revenge, Eye of the Storm, Avenging Blade, Erosion, The Reaper, Damaru, Lernaean
    Bow, Hydra''s Lament, Spirit Robe, Shogun''s Ofuda, Bloodforge, The Crusher, Eros''
    Bow, Yogi''s Necklace.'
  slot_scores:
    Eye of Providence:
      total: 0.45
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.5
    Tyrfing:
      total: 0.5
      efficiency: 0.37
      win: 0.63
      pick: 0.48
      fit: 0.42
    Qin's Blade:
      total: 0.48
      efficiency: 0.19
      win: 0.81
      pick: 0.1
      fit: 0.3
    Riptalon:
      total: 0.51
      efficiency: 0.32
      win: 0.67
      pick: 0.13
      fit: 0.58
    Amanita Charm:
      total: 0.49
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.7
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Tyrfing
  - Qin's Blade
  - Riptalon
  - The Crusher
  flex_slots:
  - The Crusher
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Riptalon, Jotunn''s Revenge, The Crusher, Avenging Blade, Heartseeker,
    The Reaper, Titan''s Bane, Damaru, Lernaean Bow, Hydra''s Lament, Tekko-Kagi,
    Runeforged Hammer, Pendulum Blade, Oath-Sworn Spear, Golden Blade, Screeching
    Gargoyle, Berserker''s Shield, Rage, Spectral Armor, Shield Splitter, Kinetic
    Cuirass, Eros'' Bow, Pharaoh''s Curse, Eye of Providence, Void Stone, Demon Blade,
    Void Shield.'
  slot_scores:
    Avenging Blade:
      total: 0.45
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.54
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.47
    Tyrfing:
      total: 0.5
      efficiency: 0.37
      win: 0.63
      pick: 0.48
      fit: 0.46
    Qin's Blade:
      total: 0.48
      efficiency: 0.19
      win: 0.81
      pick: 0.1
      fit: 0.32
    Riptalon:
      total: 0.52
      efficiency: 0.32
      win: 0.67
      pick: 0.13
      fit: 0.64
    The Crusher:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - Damaru
  - Demon Blade
  flex_slots:
  - Jotunn's Revenge
  - Demon Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Damaru, Lernaean Bow, Golden Blade, Jotunn''s Revenge,
    Demon Blade, Hydra''s Lament, Runeforged Hammer, Rage, The Crusher, Berserker''s
    Shield, Avenging Blade, Eros'' Bow, Pharaoh''s Curse, Musashi''s Dual Swords,
    Riptalon, Shield Splitter, Barbed Carver, Spectral Armor, Eye of the Storm, Transcendence,
    Tekko-Kagi, Kinetic Cuirass, The Reaper, Shogun''s Ofuda, Eye of Providence, Heartseeker,
    Bloodforge.'
  slot_scores:
    Golden Blade:
      total: 0.44
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.54
    Lernaean Bow:
      total: 0.45
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.64
    Jotunn's Revenge:
      total: 0.44
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.21
    Tyrfing:
      total: 0.53
      efficiency: 0.37
      win: 0.63
      pick: 0.48
      fit: 0.64
    Damaru:
      total: 0.45
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.54
    Demon Blade:
      total: 0.43
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 0.87
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - Qin's Blade
  - Damaru
  flex_slots:
  - Jotunn's Revenge
  - Qin's Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Damaru, Lernaean Bow, Golden Blade,
    Jotunn''s Revenge, Demon Blade, Hydra''s Lament, Runeforged Hammer, Rage, The
    Crusher, Berserker''s Shield, Avenging Blade, Eros'' Bow, Pharaoh''s Curse, Musashi''s
    Dual Swords, Riptalon, Shield Splitter, Barbed Carver, Spectral Armor, Eye of
    the Storm, Transcendence, Tekko-Kagi, Kinetic Cuirass, The Reaper, Shogun''s Ofuda,
    Eye of Providence, Heartseeker, Bloodforge.'
  slot_scores:
    Golden Blade:
      total: 0.44
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.54
    Lernaean Bow:
      total: 0.45
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.64
    Jotunn's Revenge:
      total: 0.44
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.21
    Tyrfing:
      total: 0.53
      efficiency: 0.37
      win: 0.63
      pick: 0.48
      fit: 0.64
    Qin's Blade:
      total: 0.5
      efficiency: 0.19
      win: 0.81
      pick: 0.1
      fit: 0.43
    Damaru:
      total: 0.45
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.54
  swaps:
  - added: Qin's Blade
    removed: Demon Blade
    reason: community 81% win over 34 matches (vs 60% on this god), taking the model's
      weakest slot from Demon Blade
  starter: *id001
---
