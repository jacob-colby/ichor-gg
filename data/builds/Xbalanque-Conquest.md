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
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - Qin's Blade
  - Riptalon
  - The Crusher
  flex_slots:
  - Lernaean Bow
  - The Crusher
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Jotunn''s Revenge, Lernaean Bow, The Crusher, Golden Blade,
    Damaru, Tekko-Kagi, The Reaper, Demon Blade, Rage, Runeforged Hammer, Hydra''s
    Lament, Berserker''s Shield, Avenging Blade, Musashi''s Dual Swords, Shield Splitter,
    Eros'' Bow, Pharaoh''s Curse, Barbed Carver, Spectral Armor, Eye of the Storm,
    Kinetic Cuirass, Transcendence, Eye of Providence, Shogun''s Ofuda, Bloodforge,
    Amanita Charm.'
  slot_scores:
    Lernaean Bow:
      total: 0.45
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.64
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.55
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
    Riptalon:
      total: 0.47
      efficiency: 0.27
      win: 0.67
      pick: 0.13
      fit: 0.46
    The Crusher:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.31
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
    this god: Riptalon, Jotunn''s Revenge, The Crusher, Lernaean Bow, Damaru, Golden
    Blade, Rage, Demon Blade, The Reaper, Runeforged Hammer, Tekko-Kagi, Hydra''s
    Lament, Musashi''s Dual Swords, Avenging Blade, Berserker''s Shield, Shield Splitter,
    Eros'' Bow, Pharaoh''s Curse, Barbed Carver, Spectral Armor, Eye of the Storm,
    Kinetic Cuirass, Transcendence, Eye of Providence, Shogun''s Ofuda, Bloodforge,
    Deathbringer.'
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
      total: 0.47
      efficiency: 0.27
      win: 0.67
      pick: 0.13
      fit: 0.42
    Damaru:
      total: 0.44
      efficiency: 0.37
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
  - Jotunn's Revenge
  - Shield Splitter
  - Tyrfing
  - Qin's Blade
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shield Splitter
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Amanita Charm, The Reaper, Jotunn''s Revenge, Shield Splitter,
    Kinetic Cuirass, The Crusher, Shield of the Phoenix, Eye of Providence, Chandra''s
    Grace, Phoenix Feather, Spectral Armor, Spirit Robe, Runeforged Hammer, Lernaean
    Bow, Hydra''s Lament, Berserker''s Shield, Bloodforge, Golden Blade, Pharaoh''s
    Curse, Damaru, Eye of the Storm, Avenging Blade, Tekko-Kagi, Genji''s Guard, Erosion,
    Rage.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.44
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.12
    Shield Splitter:
      total: 0.43
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.37
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
      total: 0.49
      efficiency: 0.27
      win: 0.67
      pick: 0.13
      fit: 0.58
    Amanita Charm:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Qin's Blade
  - Riptalon
  - Tekko-Kagi
  - The Crusher
  flex_slots:
  - Qin's Blade
  - Tekko-Kagi
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
    for this god: Riptalon, Jotunn''s Revenge, The Crusher, The Reaper, Tekko-Kagi,
    Avenging Blade, Lernaean Bow, Runeforged Hammer, Hydra''s Lament, Oath-Sworn Spear,
    Golden Blade, Heartseeker, Damaru, Rage, Screeching Gargoyle, Pendulum Blade,
    Berserker''s Shield, Spectral Armor, Shield Splitter, Titan''s Bane, Kinetic Cuirass,
    Eye of Providence, Eros'' Bow, Pharaoh''s Curse, Void Stone, Void Shield, Eye
    of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.47
    Tyrfing:
      total: 0.51
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
      total: 0.5
      efficiency: 0.27
      win: 0.67
      pick: 0.13
      fit: 0.64
    Tekko-Kagi:
      total: 0.45
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.69
    The Crusher:
      total: 0.48
      efficiency: 0.49
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
  - The Crusher
  flex_slots:
  - Golden Blade
  - Damaru
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Lernaean Bow, The Crusher, Golden
    Blade, Damaru, Tekko-Kagi, The Reaper, Demon Blade, Rage, Runeforged Hammer, Hydra''s
    Lament, Berserker''s Shield, Avenging Blade, Musashi''s Dual Swords, Shield Splitter,
    Eros'' Bow, Pharaoh''s Curse, Barbed Carver, Spectral Armor, Eye of the Storm,
    Kinetic Cuirass, Transcendence, Eye of Providence, Shogun''s Ofuda, Riptalon,
    Bloodforge, Amanita Charm.'
  slot_scores:
    Golden Blade:
      total: 0.44
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.54
    Lernaean Bow:
      total: 0.45
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.64
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.55
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
      total: 0.43
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.54
    The Crusher:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.31
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - Qin's Blade
  - The Crusher
  flex_slots:
  - Golden Blade
  - Qin's Blade
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
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Lernaean Bow, The
    Crusher, Golden Blade, Damaru, Tekko-Kagi, The Reaper, Demon Blade, Rage, Runeforged
    Hammer, Hydra''s Lament, Berserker''s Shield, Avenging Blade, Musashi''s Dual
    Swords, Shield Splitter, Eros'' Bow, Pharaoh''s Curse, Barbed Carver, Spectral
    Armor, Eye of the Storm, Kinetic Cuirass, Transcendence, Eye of Providence, Shogun''s
    Ofuda, Riptalon, Bloodforge, Amanita Charm.'
  slot_scores:
    Golden Blade:
      total: 0.44
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.54
    Lernaean Bow:
      total: 0.45
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.64
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.55
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
    The Crusher:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.31
  swaps:
  - added: Qin's Blade
    removed: Damaru
    reason: community 81% win over 34 matches (vs 60% on this god), taking the model's
      weakest slot from Damaru
  starter: *id001
---
