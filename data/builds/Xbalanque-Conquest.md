---
type: smite-build
god: Xbalanque
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Nightstalker
  aspect_pick_rate: 0.23
  aspect_win_rate: 0.5
  slot_order:
  - name: Tyrfing
    pick_rate: 0.36
    win_rate: 0.6
    alternates:
    - name: Transcendence
      pick_rate: 0.2
      win_rate: 0.51
    - name: Devourer's Gauntlet
      pick_rate: 0.1
      win_rate: 0.53
  - name: Odysseus' Bow
    pick_rate: 0.28
    win_rate: 0.64
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.11
      win_rate: 0.39
    - name: Hastened Fatalis
      pick_rate: 0.08
      win_rate: 0.67
  - name: Hastened Fatalis
    pick_rate: 0.15
    win_rate: 0.67
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.18
      win_rate: 0.49
    - name: Soul Gem
      pick_rate: 0.1
      win_rate: 0.46
  - name: Titan's Bane
    pick_rate: 0.14
    win_rate: 0.55
    alternates:
    - name: The Executioner
      pick_rate: 0.13
      win_rate: 0.52
    - name: Qin's Blade
      pick_rate: 0.13
      win_rate: 0.63
  - name: Qin's Blade
    pick_rate: 0.14
    win_rate: 0.68
    alternates:
    - name: Titan's Bane
      pick_rate: 0.12
      win_rate: 0.63
    - name: The Executioner
      pick_rate: 0.12
      win_rate: 0.57
  - name: Hunter's Bow
    pick_rate: 0.09
    win_rate: 0.59
    alternates:
    - name: Riptalon
      pick_rate: 0.09
      win_rate: 0.75
    - name: Titan's Bane
      pick_rate: 0.08
      win_rate: 0.71
  source_url: https://smitebrain.com/gods/xbalanque/
  last_verified: '2026-07-23'
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - Qin's Blade
  - The Crusher
  flex_slots:
  - Golden Blade
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
    this god: Jotunn''s Revenge, Lernaean Bow, Golden Blade, The Crusher, Damaru,
    Demon Blade, Rage, Runeforged Hammer, Hydra''s Lament, The Reaper, Tekko-Kagi,
    Berserker''s Shield, Avenging Blade, Musashi''s Dual Swords, Shield Splitter,
    Pharaoh''s Curse, Barbed Carver, Eros'' Bow, Eye of the Storm, Spectral Armor,
    Transcendence, Kinetic Cuirass, Shogun''s Ofuda, Bloodforge, Eye of Providence,
    Riptalon, Genji''s Guard.'
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
      total: 0.52
      efficiency: 0.39
      win: 0.6
      pick: 0.36
      fit: 0.64
    Qin's Blade:
      total: 0.45
      efficiency: 0.2
      win: 0.68
      pick: 0.14
      fit: 0.43
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
  - Jotunn's Revenge
  - Tyrfing
  - Rage
  - Qin's Blade
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
    this god: Jotunn''s Revenge, Damaru, Lernaean Bow, The Crusher, Rage, Golden Blade,
    Demon Blade, Runeforged Hammer, Hydra''s Lament, The Reaper, Tekko-Kagi, Berserker''s
    Shield, Musashi''s Dual Swords, Avenging Blade, Shield Splitter, Barbed Carver,
    Pharaoh''s Curse, Eros'' Bow, Spectral Armor, Eye of the Storm, Transcendence,
    Kinetic Cuirass, Bloodforge, Eye of Providence, Deathbringer, Genji''s Guard,
    Shogun''s Ofuda.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.2
    Tyrfing:
      total: 0.51
      efficiency: 0.39
      win: 0.6
      pick: 0.36
      fit: 0.6
    Rage:
      total: 0.44
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.57
    Qin's Blade:
      total: 0.44
      efficiency: 0.2
      win: 0.68
      pick: 0.14
      fit: 0.4
    Damaru:
      total: 0.45
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.57
    Demon Blade:
      total: 0.43
      efficiency: 0.22
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Tyrfing
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, The Reaper, Jotunn''s Revenge, Shield Splitter, Kinetic
    Cuirass, Shield of the Phoenix, The Crusher, Eye of Providence, Berserker''s Shield,
    Spirit Robe, Chandra''s Grace, Phoenix Feather, Runeforged Hammer, Bloodforge,
    Hydra''s Lament, Spectral Armor, Lernaean Bow, Golden Blade, Damaru, Pharaoh''s
    Curse, Genji''s Guard, Riptalon, Eye of the Storm, Devourer''s Gauntlet, Avenging
    Blade, Rage, Erosion.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.44
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.12
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.35
    Shield Splitter:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.37
    Tyrfing:
      total: 0.49
      efficiency: 0.39
      win: 0.6
      pick: 0.36
      fit: 0.42
    The Reaper:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.5
    Amanita Charm:
      total: 0.46
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Titan's Bane
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
    for this god: Jotunn''s Revenge, The Crusher, The Reaper, Titan''s Bane, Tekko-Kagi,
    Avenging Blade, Lernaean Bow, Oath-Sworn Spear, Runeforged Hammer, Hydra''s Lament,
    Riptalon, Golden Blade, Damaru, Heartseeker, Berserker''s Shield, Rage, Screeching
    Gargoyle, Shield Splitter, Spectral Armor, Pendulum Blade, Kinetic Cuirass, Void
    Stone, Pharaoh''s Curse, Eye of Providence, Barbed Carver, Demon Blade, Eros''
    Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.47
    Tyrfing:
      total: 0.49
      efficiency: 0.39
      win: 0.6
      pick: 0.36
      fit: 0.46
    The Reaper:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.56
    Tekko-Kagi:
      total: 0.45
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.69
    The Crusher:
      total: 0.48
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.57
    Titan's Bane:
      total: 0.45
      efficiency: 0.37
      win: 0.55
      pick: 0.14
      fit: 0.47
  starter: *id001
---
