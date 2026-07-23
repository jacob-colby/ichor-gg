---
type: smite-build
god: Rama
mode: Conquest
builds:
- source: community
  aspect: Aspect of Precision
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.5
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.43
    win_rate: 0.52
    alternates:
    - name: Tyrfing
      pick_rate: 0.22
      win_rate: 0.55
    - name: Avenging Blade
      pick_rate: 0.13
      win_rate: 0.57
  - name: Dagger of Frenzy
    pick_rate: 0.23
    win_rate: 0.53
    alternates:
    - name: Tyrfing
      pick_rate: 0.14
      win_rate: 0.55
    - name: Avenging Blade
      pick_rate: 0.1
      win_rate: 0.63
  - name: Odysseus' Bow
    pick_rate: 0.2
    win_rate: 0.48
    alternates:
    - name: Riptalon
      pick_rate: 0.17
      win_rate: 0.61
    - name: The Executioner
      pick_rate: 0.12
      win_rate: 0.56
  - name: Titan's Bane
    pick_rate: 0.23
    win_rate: 0.51
    alternates:
    - name: The Executioner
      pick_rate: 0.18
      win_rate: 0.53
    - name: Riptalon
      pick_rate: 0.14
      win_rate: 0.63
  - name: Deathbringer
    pick_rate: 0.12
    win_rate: 0.59
    alternates:
    - name: Titan's Bane
      pick_rate: 0.24
      win_rate: 0.65
    - name: Qin's Blade
      pick_rate: 0.11
      win_rate: 0.55
  - name: Hunter's Bow
    pick_rate: 0.11
    win_rate: 0.52
    alternates:
    - name: Deathbringer
      pick_rate: 0.09
      win_rate: 0.51
    - name: Qin's Blade
      pick_rate: 0.07
      win_rate: 0.7
  source_url: https://smitebrain.com/gods/rama/
  last_verified: '2026-07-23'
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  flex_slots:
  - Tekko-Kagi
  - Lernaean Bow
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
    this god: Jotunn''s Revenge, The Crusher, The Reaper, Tyrfing, Tekko-Kagi, Lernaean
    Bow, Hydra''s Lament, Golden Blade, Damaru, Runeforged Hammer, Rage, Berserker''s
    Shield, Avenging Blade, Demon Blade, Shield Splitter, Musashi''s Dual Swords,
    Barbed Carver, Spectral Armor, Riptalon, Pharaoh''s Curse, Eye of the Storm, Kinetic
    Cuirass, Eros'' Bow, Transcendence, Genji''s Guard, Heartseeker, Eye of Providence.'
  slot_scores:
    Lernaean Bow:
      total: 0.43
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.54
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.38
    Tyrfing:
      total: 0.44
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.54
    The Reaper:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.44
    Tekko-Kagi:
      total: 0.44
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.6
    The Crusher:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.44
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Rage
  - The Reaper
  - Damaru
  - The Crusher
  - Deathbringer
  flex_slots:
  - Rage
  - Deathbringer
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
    this god: Jotunn''s Revenge, The Crusher, The Reaper, Tyrfing, Tekko-Kagi, Damaru,
    Lernaean Bow, Hydra''s Lament, Runeforged Hammer, Golden Blade, Rage, Berserker''s
    Shield, Avenging Blade, Demon Blade, Shield Splitter, Musashi''s Dual Swords,
    Spectral Armor, Barbed Carver, Kinetic Cuirass, Riptalon, Pharaoh''s Curse, Genji''s
    Guard, Eye of the Storm, Eros'' Bow, Eye of Providence, Transcendence, Heartseeker.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.36
    Rage:
      total: 0.42
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.46
    The Reaper:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.42
    Damaru:
      total: 0.43
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.46
    The Crusher:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.42
    Deathbringer:
      total: 0.42
      efficiency: 0.22
      win: 0.59
      pick: 0.12
      fit: 0.46
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  flex_slots:
  - Tekko-Kagi
  - Tyrfing
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, The Crusher, The Reaper, Hydra''s Lament, Tekko-Kagi,
    Tyrfing, Runeforged Hammer, Lernaean Bow, Golden Blade, Genji''s Guard, Damaru,
    Avenging Blade, Berserker''s Shield, Shield Splitter, Spectral Armor, Rage, Chandra''s
    Grace, Pendulum Blade, Kinetic Cuirass, Breastplate of Valor, Eye of Providence,
    Arondight, Heartseeker, Eye of the Storm, Shield of the Phoenix, Barbed Carver,
    Transcendence.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.46
    Tyrfing:
      total: 0.42
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.4
    Hydra's Lament:
      total: 0.44
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.36
    The Reaper:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.39
    Tekko-Kagi:
      total: 0.42
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.5
    The Crusher:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - The Reaper
  - The Crusher
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
    this god: The Reaper, Amanita Charm, Jotunn''s Revenge, The Crusher, Shield of
    the Phoenix, Shield Splitter, Kinetic Cuirass, Chandra''s Grace, Eye of Providence,
    Hydra''s Lament, Tyrfing, Phoenix Feather, Runeforged Hammer, Berserker''s Shield,
    Spirit Robe, Riptalon, Bloodforge, Spectral Armor, Lernaean Bow, Genji''s Guard,
    Tekko-Kagi, Golden Blade, Damaru, Avenging Blade, Eye of the Storm, Pharaoh''s
    Curse, Rage.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.31
    Shield Splitter:
      total: 0.43
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.33
    The Reaper:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.59
    The Crusher:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.33
    Amanita Charm:
      total: 0.46
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.51
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Tekko-Kagi
  - Titan's Bane
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
    for this god: Jotunn''s Revenge, The Crusher, The Reaper, Avenging Blade, Tekko-Kagi,
    Tyrfing, Hydra''s Lament, Oath-Sworn Spear, Lernaean Bow, Runeforged Hammer, Golden
    Blade, Damaru, Riptalon, Heartseeker, Screeching Gargoyle, Berserker''s Shield,
    Rage, Shield Splitter, Pendulum Blade, Spectral Armor, Kinetic Cuirass, Void Stone,
    Genji''s Guard, Barbed Carver, Eye of Providence, Eye of the Storm, Pharaoh''s
    Curse.'
  slot_scores:
    Avenging Blade:
      total: 0.45
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.55
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.5
    The Reaper:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.55
    Tekko-Kagi:
      total: 0.45
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.68
    The Crusher:
      total: 0.48
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.57
    Titan's Bane:
      total: 0.44
      efficiency: 0.37
      win: 0.51
      pick: 0.23
      fit: 0.47
  starter: *id001
---
