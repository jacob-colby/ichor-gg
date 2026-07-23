---
type: smite-build
god: Artemis
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Wild
  aspect_pick_rate: 0.32
  aspect_win_rate: 0.5
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.38
    win_rate: 0.59
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.16
      win_rate: 0.54
    - name: Tyrfing
      pick_rate: 0.12
      win_rate: 0.68
  - name: Dagger of Frenzy
    pick_rate: 0.15
    win_rate: 0.61
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.1
      win_rate: 0.64
    - name: Sun Beam Bow
      pick_rate: 0.09
      win_rate: 0.55
  - name: Odysseus' Bow
    pick_rate: 0.16
    win_rate: 0.62
    alternates:
    - name: Riptalon
      pick_rate: 0.1
      win_rate: 0.63
    - name: The Executioner
      pick_rate: 0.08
      win_rate: 0.5
  - name: Riptalon
    pick_rate: 0.21
    win_rate: 0.6
    alternates:
    - name: Titan's Bane
      pick_rate: 0.13
      win_rate: 0.59
    - name: The Executioner
      pick_rate: 0.08
      win_rate: 0.63
  - name: Titan's Bane
    pick_rate: 0.16
    win_rate: 0.66
    alternates:
    - name: Riptalon
      pick_rate: 0.1
      win_rate: 0.59
    - name: The Executioner
      pick_rate: 0.08
      win_rate: 0.59
  - name: Hunter's Bow
    pick_rate: 0.09
    win_rate: 0.45
    alternates:
    - name: Riptalon
      pick_rate: 0.07
      win_rate: 0.5
    - name: Sun Beam Bow
      pick_rate: 0.07
      win_rate: 0.76
  source_url: https://smitebrain.com/gods/artemis/
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
  - Riptalon
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Riptalon
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
    this god: Jotunn''s Revenge, Tyrfing, The Crusher, Lernaean Bow, Golden Blade,
    Hydra''s Lament, The Reaper, Damaru, Tekko-Kagi, Runeforged Hammer, Rage, Demon
    Blade, Berserker''s Shield, Avenging Blade, Shield Splitter, Musashi''s Dual Swords,
    Barbed Carver, Pharaoh''s Curse, Eros'' Bow, Eye of the Storm, Spectral Armor,
    Transcendence, Kinetic Cuirass, Genji''s Guard, Eye of Providence, Bloodforge,
    Arondight.'
  slot_scores:
    Lernaean Bow:
      total: 0.44
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.3
    Tyrfing:
      total: 0.45
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.6
    Riptalon:
      total: 0.44
      efficiency: 0.27
      win: 0.6
      pick: 0.21
      fit: 0.46
    The Crusher:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.36
    Titan's Bane:
      total: 0.47
      efficiency: 0.37
      win: 0.66
      pick: 0.16
      fit: 0.26
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Rage
  - Damaru
  - Demon Blade
  - The Crusher
  - Titan's Bane
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
    this god: Jotunn''s Revenge, The Crusher, Tyrfing, Damaru, Lernaean Bow, Hydra''s
    Lament, The Reaper, Rage, Golden Blade, Runeforged Hammer, Tekko-Kagi, Demon Blade,
    Berserker''s Shield, Avenging Blade, Musashi''s Dual Swords, Shield Splitter,
    Barbed Carver, Pharaoh''s Curse, Spectral Armor, Eros'' Bow, Kinetic Cuirass,
    Eye of the Storm, Genji''s Guard, Transcendence, Eye of Providence, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.28
    Rage:
      total: 0.43
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.52
    Damaru:
      total: 0.44
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.52
    Demon Blade:
      total: 0.42
      efficiency: 0.22
      win: 0.5
      pick: 0.0
      fit: 0.79
    The Crusher:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.34
    Titan's Bane:
      total: 0.47
      efficiency: 0.37
      win: 0.66
      pick: 0.16
      fit: 0.24
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Shield Splitter
  - Devourer's Gauntlet
  - Riptalon
  - The Crusher
  - Titan's Bane
  flex_slots:
  - The Crusher
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, The Reaper, Jotunn''s Revenge, The Crusher, Shield Splitter,
    Shield of the Phoenix, Kinetic Cuirass, Chandra''s Grace, Eye of Providence, Tyrfing,
    Hydra''s Lament, Phoenix Feather, Berserker''s Shield, Spirit Robe, Runeforged
    Hammer, Bloodforge, Lernaean Bow, Spectral Armor, Golden Blade, Genji''s Guard,
    Damaru, Eye of the Storm, Avenging Blade, Pharaoh''s Curse, Rage, Tekko-Kagi.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.19
    Shield Splitter:
      total: 0.43
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.36
    Devourer's Gauntlet:
      total: 0.46
      efficiency: 0.29
      win: 0.59
      pick: 0.38
      fit: 0.5
    Riptalon:
      total: 0.46
      efficiency: 0.27
      win: 0.6
      pick: 0.21
      fit: 0.59
    The Crusher:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.26
    Titan's Bane:
      total: 0.46
      efficiency: 0.37
      win: 0.66
      pick: 0.16
      fit: 0.16
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Riptalon
  - Tekko-Kagi
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Avenging Blade
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
    for this god: Jotunn''s Revenge, The Crusher, The Reaper, Avenging Blade, Tekko-Kagi,
    Tyrfing, Hydra''s Lament, Oath-Sworn Spear, Lernaean Bow, Runeforged Hammer, Golden
    Blade, Damaru, Heartseeker, Screeching Gargoyle, Berserker''s Shield, Rage, Shield
    Splitter, Pendulum Blade, Spectral Armor, Kinetic Cuirass, Void Stone, Genji''s
    Guard, Barbed Carver, Eye of Providence, Eye of the Storm, Pharaoh''s Curse.'
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
    Riptalon:
      total: 0.47
      efficiency: 0.27
      win: 0.6
      pick: 0.21
      fit: 0.61
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
      total: 0.5
      efficiency: 0.37
      win: 0.66
      pick: 0.16
      fit: 0.47
  starter: *id001
---
