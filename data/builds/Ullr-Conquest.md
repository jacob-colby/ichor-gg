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
      win_rate: 0.72
  - name: Jotunn's Revenge
    pick_rate: 0.44
    win_rate: 0.53
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.39
      win_rate: 0.57
    - name: Transcendence
      pick_rate: 0.1
      win_rate: 0.6
  - name: Hydra's Lament
    pick_rate: 0.38
    win_rate: 0.55
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.3
      win_rate: 0.6
    - name: Heartseeker
      pick_rate: 0.07
      win_rate: 0.53
  - name: Heartseeker
    pick_rate: 0.4
    win_rate: 0.54
    alternates:
    - name: Titan's Bane
      pick_rate: 0.38
      win_rate: 0.59
    - name: The Crusher
      pick_rate: 0.03
      win_rate: 0.53
  - name: Titan's Bane
    pick_rate: 0.29
    win_rate: 0.56
    alternates:
    - name: Heartseeker
      pick_rate: 0.3
      win_rate: 0.62
    - name: Lucerne Hammer
      pick_rate: 0.1
      win_rate: 0.55
  - name: Blinking Abyss
    pick_rate: 0.15
    win_rate: 0.62
    alternates:
    - name: Lucerne Hammer
      pick_rate: 0.11
      win_rate: 0.57
    - name: Titan's Bane
      pick_rate: 0.08
      win_rate: 0.73
  source_url: https://smitebrain.com/gods/ullr/
  last_verified: '2026-07-23'
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Titan's Bane
  - The Reaper
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
    this god: The Crusher, The Reaper, Tyrfing, Tekko-Kagi, Lernaean Bow, Golden Blade,
    Runeforged Hammer, Damaru, Rage, Berserker''s Shield, Avenging Blade, Shield Splitter,
    Genji''s Guard, Demon Blade, Spectral Armor, Kinetic Cuirass, Pharaoh''s Curse,
    Musashi''s Dual Swords, Riptalon, Barbed Carver, Eros'' Bow, Eye of the Storm,
    Eye of Providence, Chandra''s Grace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.55
      win: 0.53
      pick: 0.44
      fit: 0.4
    Transcendence:
      total: 0.45
      efficiency: 0.4
      win: 0.55
      pick: 0.86
      fit: 0.15
    Hydra's Lament:
      total: 0.48
      efficiency: 0.45
      win: 0.55
      pick: 0.38
      fit: 0.35
    The Reaper:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.4
    The Crusher:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.41
    Titan's Bane:
      total: 0.44
      efficiency: 0.37
      win: 0.56
      pick: 0.29
      fit: 0.31
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Rage
  - Damaru
  - Demon Blade
  - The Crusher
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
    this god: The Crusher, The Reaper, Tyrfing, Tekko-Kagi, Damaru, Lernaean Bow,
    Runeforged Hammer, Golden Blade, Rage, Berserker''s Shield, Avenging Blade, Shield
    Splitter, Demon Blade, Genji''s Guard, Musashi''s Dual Swords, Spectral Armor,
    Kinetic Cuirass, Barbed Carver, Pharaoh''s Curse, Eye of the Storm, Eye of Providence,
    Chandra''s Grace, Riptalon, Eros'' Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.55
      win: 0.53
      pick: 0.44
      fit: 0.4
    Hydra's Lament:
      total: 0.48
      efficiency: 0.45
      win: 0.55
      pick: 0.38
      fit: 0.35
    Rage:
      total: 0.42
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.43
    Damaru:
      total: 0.42
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.43
    Demon Blade:
      total: 0.4
      efficiency: 0.22
      win: 0.5
      pick: 0.0
      fit: 0.66
    The Crusher:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Titan's Bane
  - The Reaper
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
    god: The Crusher, The Reaper, Tekko-Kagi, Tyrfing, Runeforged Hammer, Lernaean
    Bow, Golden Blade, Genji''s Guard, Damaru, Avenging Blade, Berserker''s Shield,
    Shield Splitter, Spectral Armor, Rage, Chandra''s Grace, Pendulum Blade, Kinetic
    Cuirass, Breastplate of Valor, Eye of Providence, Arondight, Eye of the Storm,
    Shield of the Phoenix, Barbed Carver.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.55
      win: 0.53
      pick: 0.44
      fit: 0.46
    Transcendence:
      total: 0.45
      efficiency: 0.4
      win: 0.55
      pick: 0.86
      fit: 0.13
    Hydra's Lament:
      total: 0.48
      efficiency: 0.45
      win: 0.55
      pick: 0.38
      fit: 0.36
    The Reaper:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.39
    The Crusher:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.43
    Titan's Bane:
      total: 0.44
      efficiency: 0.37
      win: 0.56
      pick: 0.29
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Transcendence
  - The Crusher
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Amanita Charm, The Crusher, Shield of the Phoenix, Chandra''s
    Grace, Shield Splitter, Kinetic Cuirass, Eye of Providence, Phoenix Feather, Tyrfing,
    Berserker''s Shield, Spirit Robe, Riptalon, Runeforged Hammer, Spectral Armor,
    Genji''s Guard, Bloodforge, Lernaean Bow, Tekko-Kagi, Golden Blade, Avenging Blade,
    Damaru, Eye of the Storm, Breastplate of Valor, Devourer''s Gauntlet, Pharaoh''s
    Curse.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.55
      win: 0.53
      pick: 0.44
      fit: 0.27
    Transcendence:
      total: 0.45
      efficiency: 0.4
      win: 0.55
      pick: 0.86
      fit: 0.1
    Hydra's Lament:
      total: 0.46
      efficiency: 0.45
      win: 0.55
      pick: 0.38
      fit: 0.27
    The Reaper:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.57
    The Crusher:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.31
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
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Transcendence
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
    for this god: The Crusher, The Reaper, Avenging Blade, Tekko-Kagi, Tyrfing, Oath-Sworn
    Spear, Runeforged Hammer, Screeching Gargoyle, Lernaean Bow, Golden Blade, Damaru,
    Riptalon, Berserker''s Shield, Pendulum Blade, Rage, Genji''s Guard, Shield Splitter,
    Spectral Armor, Kinetic Cuirass, Void Stone, Eye of Providence, Pharaoh''s Curse,
    Void Shield, Chandra''s Grace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.55
      win: 0.53
      pick: 0.44
      fit: 0.52
    Transcendence:
      total: 0.45
      efficiency: 0.4
      win: 0.55
      pick: 0.86
      fit: 0.13
    Hydra's Lament:
      total: 0.47
      efficiency: 0.45
      win: 0.55
      pick: 0.38
      fit: 0.3
    The Reaper:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.52
    The Crusher:
      total: 0.48
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.54
    Titan's Bane:
      total: 0.46
      efficiency: 0.37
      win: 0.56
      pick: 0.29
      fit: 0.44
  starter: *id001
---
