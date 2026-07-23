---
type: smite-build
god: Ullr
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Transcendence
    pick_rate: 0.86
    win_rate: 0.55
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.06
      win_rate: 0.54
    - name: Hydra's Lament
      pick_rate: 0.05
      win_rate: 0.71
  - name: Jotunn's Revenge
    pick_rate: 0.45
    win_rate: 0.53
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.38
      win_rate: 0.58
    - name: Transcendence
      pick_rate: 0.1
      win_rate: 0.6
  - name: Hydra's Lament
    pick_rate: 0.39
    win_rate: 0.54
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.29
      win_rate: 0.6
    - name: Heartseeker
      pick_rate: 0.07
      win_rate: 0.51
  - name: Heartseeker
    pick_rate: 0.39
    win_rate: 0.53
    alternates:
    - name: Titan's Bane
      pick_rate: 0.39
      win_rate: 0.59
    - name: The Crusher
      pick_rate: 0.04
      win_rate: 0.53
  - name: Titan's Bane
    pick_rate: 0.28
    win_rate: 0.55
    alternates:
    - name: Heartseeker
      pick_rate: 0.3
      win_rate: 0.62
    - name: Lucerne Hammer
      pick_rate: 0.1
      win_rate: 0.57
  - name: Blinking Abyss
    pick_rate: 0.15
    win_rate: 0.6
    alternates:
    - name: Lucerne Hammer
      pick_rate: 0.11
      win_rate: 0.57
    - name: Titan's Bane
      pick_rate: 0.08
      win_rate: 0.72
  source_url: https://smitebrain.com/gods/ullr/
  last_verified: '2026-07-22'
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, The Reaper, Tyrfing, Tekko-Kagi, Runeforged Hammer, Lernaean
    Bow, Avenging Blade, Golden Blade, Shield Splitter, Damaru, Pendulum Blade, Rage,
    Barbed Carver, Arondight, Genji''s Guard, Eye of the Storm, Spectral Armor, Kinetic
    Cuirass, Bloodforge, Chandra''s Grace, Berserker''s Shield, Oath-Sworn Spear,
    Riptalon.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.53
      win: 0.53
      pick: 0.45
      fit: 0.55
    Transcendence:
      total: 0.49
      efficiency: 0.4
      win: 0.55
      pick: 0.86
      fit: 0.21
    Hydra's Lament:
      total: 0.47
      efficiency: 0.44
      win: 0.54
      pick: 0.39
      fit: 0.44
    The Crusher:
      total: 0.42
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.52
    Heartseeker:
      total: 0.42
      efficiency: 0.28
      win: 0.53
      pick: 0.39
      fit: 0.52
    Titan's Bane:
      total: 0.42
      efficiency: 0.36
      win: 0.55
      pick: 0.28
      fit: 0.42
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Rage
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
    this god: The Crusher, Tyrfing, The Reaper, Tekko-Kagi, Lernaean Bow, Damaru,
    Rage, Runeforged Hammer, Golden Blade, Avenging Blade, Shield Splitter, Demon
    Blade, Berserker''s Shield, Musashi''s Dual Swords, Spectral Armor, Genji''s Guard,
    Barbed Carver, Kinetic Cuirass, Eye of the Storm, Pharaoh''s Curse, Eye of Providence,
    Eros'' Bow, Pendulum Blade, Arondight.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.53
      win: 0.53
      pick: 0.45
      fit: 0.4
    Transcendence:
      total: 0.48
      efficiency: 0.4
      win: 0.55
      pick: 0.86
      fit: 0.15
    Hydra's Lament:
      total: 0.45
      efficiency: 0.44
      win: 0.54
      pick: 0.39
      fit: 0.35
    Rage:
      total: 0.37
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.43
    Damaru:
      total: 0.37
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.43
    Demon Blade:
      total: 0.35
      efficiency: 0.23
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Crusher, The Reaper, Tekko-Kagi, Runeforged Hammer, Tyrfing, Pendulum
    Blade, Avenging Blade, Shield Splitter, Lernaean Bow, Genji''s Guard, Golden Blade,
    Arondight, Chandra''s Grace, Damaru, Spectral Armor, Rage, Kinetic Cuirass, Barbed
    Carver, Eye of the Storm, Breastplate of Valor, Eye of Providence, Shield of the
    Phoenix, Screeching Gargoyle.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.53
      win: 0.53
      pick: 0.45
      fit: 0.56
    Transcendence:
      total: 0.49
      efficiency: 0.4
      win: 0.55
      pick: 0.86
      fit: 0.16
    Hydra's Lament:
      total: 0.47
      efficiency: 0.44
      win: 0.54
      pick: 0.39
      fit: 0.42
    The Crusher:
      total: 0.42
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.5
    Heartseeker:
      total: 0.42
      efficiency: 0.28
      win: 0.53
      pick: 0.39
      fit: 0.5
    Titan's Bane:
      total: 0.42
      efficiency: 0.36
      win: 0.55
      pick: 0.28
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Amanita Charm, The Crusher, Shield of the Phoenix, Shield
    Splitter, Kinetic Cuirass, Chandra''s Grace, Eye of Providence, Spirit Robe, Phoenix
    Feather, Bloodforge, Runeforged Hammer, Spectral Armor, Genji''s Guard, Tyrfing,
    Devourer''s Gauntlet, Eye of the Storm, Riptalon, Glorious Pridwen, Avenging Blade,
    Berserker''s Shield, Erosion, Lernaean Bow, Breastplate of Valor, Tekko-Kagi,
    Golden Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.53
      win: 0.53
      pick: 0.45
      fit: 0.33
    Transcendence:
      total: 0.48
      efficiency: 0.4
      win: 0.55
      pick: 0.86
      fit: 0.12
    Hydra's Lament:
      total: 0.45
      efficiency: 0.44
      win: 0.54
      pick: 0.39
      fit: 0.3
    The Reaper:
      total: 0.42
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.63
    Titan's Bane:
      total: 0.4
      efficiency: 0.36
      win: 0.55
      pick: 0.28
      fit: 0.25
    Amanita Charm:
      total: 0.41
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    for this god: The Crusher, The Reaper, Avenging Blade, Tekko-Kagi, Oath-Sworn
    Spear, Pendulum Blade, Screeching Gargoyle, Tyrfing, Runeforged Hammer, Lernaean
    Bow, Riptalon, Shield Splitter, Golden Blade, Damaru, Rage, Barbed Carver, Genji''s
    Guard, Spectral Armor, Void Stone, Kinetic Cuirass, Eye of the Storm, Void Shield,
    Arondight.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.53
      win: 0.53
      pick: 0.45
      fit: 0.66
    Transcendence:
      total: 0.49
      efficiency: 0.4
      win: 0.55
      pick: 0.86
      fit: 0.16
    Hydra's Lament:
      total: 0.46
      efficiency: 0.44
      win: 0.54
      pick: 0.39
      fit: 0.36
    The Crusher:
      total: 0.44
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.66
    Heartseeker:
      total: 0.44
      efficiency: 0.28
      win: 0.53
      pick: 0.39
      fit: 0.66
    Titan's Bane:
      total: 0.45
      efficiency: 0.36
      win: 0.55
      pick: 0.28
      fit: 0.56
  starter: *id001
---
