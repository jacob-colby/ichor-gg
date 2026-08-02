---
type: smite-build
god: Kali
mode: Conquest
builds:
- source: community
  aspect: Aspect of Unbound Destruction
  aspect_pick_rate: 0.33
  aspect_win_rate: 0.64
  slot_order:
  - name: Tyrfing
    pick_rate: 0.28
    win_rate: 0.66
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.18
      win_rate: 0.6
    - name: Book of Thoth
      pick_rate: 0.1
      win_rate: 0.44
  - name: Odysseus' Bow
    pick_rate: 0.18
    win_rate: 0.7
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.17
      win_rate: 0.52
    - name: Dagger of Frenzy
      pick_rate: 0.09
      win_rate: 0.67
  - name: Hastened Fatalis
    pick_rate: 0.21
    win_rate: 0.63
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.15
      win_rate: 0.67
    - name: Polynomicon
      pick_rate: 0.12
      win_rate: 0.6
  - name: The Executioner
    pick_rate: 0.1
    win_rate: 0.47
    alternates:
    - name: Dominance
      pick_rate: 0.09
      win_rate: 0.71
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.5
  - name: Manchu Bow
    pick_rate: 0.09
    win_rate: 0.75
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.08
      win_rate: 0.7
    - name: Riptalon
      pick_rate: 0.07
      win_rate: 0.67
  - name: Blinking Abyss
    pick_rate: 0.13
    win_rate: 0.75
    alternates:
    - name: Bow
      pick_rate: 0.1
      win_rate: 0.67
    - name: Manchu Bow
      pick_rate: 0.08
      win_rate: 0.8
  source_url: https://smitebrain.com/gods/kali/
  last_verified: '2026-08-01'
  god_win_rate: 0.562874251497006
  god_matches_won: 94
  god_matches_played: 167
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
  - Odysseus' Bow
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - The Crusher
  flex_slots:
  - Lernaean Bow
  - Hydra's Lament
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
    this god: Jotunn''s Revenge, The Crusher, Lernaean Bow, Hydra''s Lament, Damaru,
    Golden Blade, Runeforged Hammer, Heartseeker, Titan''s Bane, Tekko-Kagi, Pendulum
    Blade, Avenging Blade, Rage, Shield Splitter, The Reaper, Demon Blade, Riptalon,
    Berserker''s Shield, Eye of the Storm, Transcendence, Musashi''s Dual Swords,
    Eros'' Bow, Pharaoh''s Curse, Spectral Armor, Arondight, Kinetic Cuirass, Genji''s
    Guard.'
  slot_scores:
    Odysseus' Bow:
      total: 0.45
      efficiency: 0.22
      win: 0.7
      pick: 0.18
      fit: 0.37
    Lernaean Bow:
      total: 0.45
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.63
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.52
    Tyrfing:
      total: 0.53
      efficiency: 0.37
      win: 0.66
      pick: 0.28
      fit: 0.63
    Hydra's Lament:
      total: 0.45
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.41
    The Crusher:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Jotunn''s Revenge,
    Eye of Providence, Chandra''s Grace, Runeforged Hammer, Phoenix Feather, Spectral
    Armor, Shield Splitter, The Crusher, Berserker''s Shield, The Reaper, Golden Blade,
    Eye of the Storm, Avenging Blade, Hydra''s Lament, Riptalon, Pharaoh''s Curse,
    Erosion, Spirit Robe, Lernaean Bow, Damaru, Genji''s Guard, Shogun''s Ofuda, Eros''
    Bow, Bloodforge.'
  slot_scores:
    Eye of Providence:
      total: 0.45
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.41
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.51
    Shield of the Phoenix:
      total: 0.46
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.61
    Tyrfing:
      total: 0.5
      efficiency: 0.37
      win: 0.66
      pick: 0.28
      fit: 0.41
    Amanita Charm:
      total: 0.49
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Tyrfing
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, Avenging Blade, Heartseeker, Titan''s
    Bane, Pendulum Blade, The Reaper, Hydra''s Lament, Tekko-Kagi, Lernaean Bow, Riptalon,
    Runeforged Hammer, Oath-Sworn Spear, Damaru, Golden Blade, Screeching Gargoyle,
    Shield Splitter, Rage, Berserker''s Shield, Spectral Armor, Eye of the Storm,
    Kinetic Cuirass, Transcendence, Genji''s Guard, Eye of Providence, Eros'' Bow,
    Pharaoh''s Curse.'
  slot_scores:
    Avenging Blade:
      total: 0.46
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.64
    Tyrfing:
      total: 0.51
      efficiency: 0.37
      win: 0.66
      pick: 0.28
      fit: 0.5
    The Crusher:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.7
    Heartseeker:
      total: 0.45
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.7
    Titan's Bane:
      total: 0.45
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.6
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Demon Blade
  - Golden Blade
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: For fun — deliberately fights this god's kit (Crit / attack-speed party
    build). Scored on gold-value + flavor fit only; not meta-checked.
  slot_scores:
    Golden Blade:
      total: 0.22
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.57
    Lernaean Bow:
      total: 0.23
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.67
    Tyrfing:
      total: 0.23
      efficiency: 0.37
      win: 0.66
      pick: 0.28
      fit: 0.67
    Death Metal:
      total: 0.25
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.24
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.22
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Damaru
  - The Crusher
  flex_slots:
  - Hydra's Lament
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
    Underrated for this god: Jotunn''s Revenge, The Crusher, Lernaean Bow, Hydra''s
    Lament, Damaru, Golden Blade, Runeforged Hammer, Heartseeker, Titan''s Bane, Tekko-Kagi,
    Pendulum Blade, Avenging Blade, Rage, Shield Splitter, The Reaper, Demon Blade,
    Riptalon, Berserker''s Shield, Eye of the Storm, Transcendence, Musashi''s Dual
    Swords, Eros'' Bow, Pharaoh''s Curse, Spectral Armor, Arondight, Kinetic Cuirass,
    Genji''s Guard.'
  slot_scores:
    Lernaean Bow:
      total: 0.45
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.63
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.52
    Tyrfing:
      total: 0.53
      efficiency: 0.37
      win: 0.66
      pick: 0.28
      fit: 0.63
    Hydra's Lament:
      total: 0.45
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.41
    Damaru:
      total: 0.44
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.47
    The Crusher:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
---
