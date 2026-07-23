---
type: smite-build
god: Cupid
mode: Conquest
builds:
- source: community
  aspect: Aspect of Love
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.61
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.3
    win_rate: 0.5
    alternates:
    - name: Tyrfing
      pick_rate: 0.22
      win_rate: 0.62
    - name: Avenging Blade
      pick_rate: 0.15
      win_rate: 0.57
  - name: Dagger of Frenzy
    pick_rate: 0.17
    win_rate: 0.45
    alternates:
    - name: Tyrfing
      pick_rate: 0.11
      win_rate: 0.56
    - name: Odysseus' Bow
      pick_rate: 0.11
      win_rate: 0.6
  - name: Odysseus' Bow
    pick_rate: 0.23
    win_rate: 0.59
    alternates:
    - name: Riptalon
      pick_rate: 0.14
      win_rate: 0.51
    - name: Qin's Blade
      pick_rate: 0.11
      win_rate: 0.51
  - name: Titan's Bane
    pick_rate: 0.26
    win_rate: 0.53
    alternates:
    - name: The Executioner
      pick_rate: 0.15
      win_rate: 0.64
    - name: Qin's Blade
      pick_rate: 0.13
      win_rate: 0.47
  - name: Riptalon
    pick_rate: 0.12
    win_rate: 0.48
    alternates:
    - name: Titan's Bane
      pick_rate: 0.22
      win_rate: 0.64
    - name: Qin's Blade
      pick_rate: 0.11
      win_rate: 0.52
  - name: Hunter's Bow
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Titan's Bane
      pick_rate: 0.07
      win_rate: 0.48
    - name: Qin's Blade
      pick_rate: 0.07
      win_rate: 0.68
  source_url: https://smitebrain.com/gods/cupid/
  last_verified: '2026-07-23'
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  flex_slots:
  - Tyrfing
  - Tekko-Kagi
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, The Crusher, Hydra''s Lament, The Reaper, Tyrfing,
    Tekko-Kagi, Lernaean Bow, Runeforged Hammer, Golden Blade, Damaru, Berserker''s
    Shield, Rage, Genji''s Guard, Avenging Blade, Shield Splitter, Spectral Armor,
    Chandra''s Grace, Kinetic Cuirass, Demon Blade, Pendulum Blade, Breastplate of
    Valor, Arondight, Pharaoh''s Curse, Barbed Carver, Musashi''s Dual Swords, Eye
    of Providence, Riptalon.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.45
    Tyrfing:
      total: 0.43
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.48
    Hydra's Lament:
      total: 0.44
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.38
    The Reaper:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.41
    Tekko-Kagi:
      total: 0.43
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.42
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, The Crusher, Hydra''s Lament, The Reaper, Tyrfing,
    Tekko-Kagi, Lernaean Bow, Damaru, Runeforged Hammer, Golden Blade, Rage, Genji''s
    Guard, Berserker''s Shield, Avenging Blade, Shield Splitter, Spectral Armor, Chandra''s
    Grace, Kinetic Cuirass, Demon Blade, Musashi''s Dual Swords, Breastplate of Valor,
    Pendulum Blade, Arondight, Barbed Carver, Eye of Providence, Pharaoh''s Curse,
    Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.44
    Hydra's Lament:
      total: 0.44
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.37
    Rage:
      total: 0.41
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.4
    Damaru:
      total: 0.42
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.4
    Demon Blade:
      total: 0.39
      efficiency: 0.22
      win: 0.5
      pick: 0.0
      fit: 0.62
    The Crusher:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
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
    Titan's Bane:
      total: 0.43
      efficiency: 0.37
      win: 0.53
      pick: 0.26
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Shield Splitter
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Hydra's Lament
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
    this god: The Reaper, Jotunn''s Revenge, Amanita Charm, The Crusher, Shield of
    the Phoenix, Chandra''s Grace, Hydra''s Lament, Shield Splitter, Kinetic Cuirass,
    Eye of Providence, Phoenix Feather, Genji''s Guard, Tyrfing, Runeforged Hammer,
    Spirit Robe, Berserker''s Shield, Spectral Armor, Bloodforge, Riptalon, Lernaean
    Bow, Tekko-Kagi, Breastplate of Valor, Golden Blade, Avenging Blade, Damaru, Eye
    of the Storm, Pharaoh''s Curse.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.31
    Shield Splitter:
      total: 0.42
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.3
    Hydra's Lament:
      total: 0.43
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.29
    The Reaper:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.58
    The Crusher:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.32
    Amanita Charm:
      total: 0.46
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.49
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
    for this god: Jotunn''s Revenge, The Crusher, The Reaper, Avenging Blade, Tekko-Kagi,
    Hydra''s Lament, Tyrfing, Screeching Gargoyle, Oath-Sworn Spear, Runeforged Hammer,
    Lernaean Bow, Golden Blade, Damaru, Pendulum Blade, Genji''s Guard, Berserker''s
    Shield, Heartseeker, Riptalon, Rage, Shield Splitter, Spectral Armor, Kinetic
    Cuirass, Chandra''s Grace, Void Stone, Eye of Providence, Breastplate of Valor,
    Void Shield.'
  slot_scores:
    Avenging Blade:
      total: 0.45
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.53
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.54
    The Reaper:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.5
    Tekko-Kagi:
      total: 0.44
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.62
    The Crusher:
      total: 0.47
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.53
    Titan's Bane:
      total: 0.44
      efficiency: 0.37
      win: 0.53
      pick: 0.26
      fit: 0.43
  starter: *id001
---
