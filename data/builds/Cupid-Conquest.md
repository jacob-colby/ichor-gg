---
type: smite-build
god: Cupid
mode: Conquest
builds:
- source: community
  aspect: Aspect of Love
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.68
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.28
    win_rate: 0.52
    alternates:
    - name: Tyrfing
      pick_rate: 0.24
      win_rate: 0.61
    - name: Avenging Blade
      pick_rate: 0.17
      win_rate: 0.64
  - name: Dagger of Frenzy
    pick_rate: 0.15
    win_rate: 0.49
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.68
    - name: Tyrfing
      pick_rate: 0.11
      win_rate: 0.59
  - name: Odysseus' Bow
    pick_rate: 0.25
    win_rate: 0.63
    alternates:
    - name: Riptalon
      pick_rate: 0.15
      win_rate: 0.55
    - name: Qin's Blade
      pick_rate: 0.1
      win_rate: 0.52
  - name: Titan's Bane
    pick_rate: 0.25
    win_rate: 0.56
    alternates:
    - name: The Executioner
      pick_rate: 0.15
      win_rate: 0.64
    - name: Riptalon
      pick_rate: 0.12
      win_rate: 0.63
  - name: Riptalon
    pick_rate: 0.13
    win_rate: 0.59
    alternates:
    - name: Titan's Bane
      pick_rate: 0.21
      win_rate: 0.64
    - name: Qin's Blade
      pick_rate: 0.12
      win_rate: 0.54
  - name: Hunter's Bow
    pick_rate: 0.1
    win_rate: 0.58
    alternates:
    - name: Qin's Blade
      pick_rate: 0.09
      win_rate: 0.67
    - name: Titan's Bane
      pick_rate: 0.07
      win_rate: 0.55
  source_url: https://smitebrain.com/gods/cupid/
  last_verified: '2026-07-25'
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Riptalon
  - The Crusher
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Riptalon
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
    this god: Jotunn''s Revenge, The Crusher, Hydra''s Lament, The Reaper, Riptalon,
    Tyrfing, Tekko-Kagi, Lernaean Bow, Runeforged Hammer, Golden Blade, Damaru, Berserker''s
    Shield, Genji''s Guard, Avenging Blade, Rage, Shield Splitter, Spectral Armor,
    Chandra''s Grace, Kinetic Cuirass, Pharaoh''s Curse, Eros'' Bow, Breastplate of
    Valor, Demon Blade, Eye of Providence, Arondight, Eye of the Storm, Pendulum Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.45
    Hydra's Lament:
      total: 0.44
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.38
    The Reaper:
      total: 0.44
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.41
    Riptalon:
      total: 0.44
      efficiency: 0.26
      win: 0.59
      pick: 0.13
      fit: 0.49
    The Crusher:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.42
    Titan's Bane:
      total: 0.44
      efficiency: 0.36
      win: 0.56
      pick: 0.25
      fit: 0.32
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
    Tekko-Kagi, Lernaean Bow, Runeforged Hammer, Damaru, Golden Blade, Rage, Berserker''s
    Shield, Genji''s Guard, Avenging Blade, Spectral Armor, Shield Splitter, Chandra''s
    Grace, Kinetic Cuirass, Demon Blade, Breastplate of Valor, Eye of Providence,
    Musashi''s Dual Swords, Pharaoh''s Curse, Eros'' Bow, Arondight, Eye of the Storm,
    Pendulum Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.54
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
      efficiency: 0.35
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
      efficiency: 0.21
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
  - The Reaper
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
    god: Jotunn''s Revenge, The Crusher, Hydra''s Lament, The Reaper, Tekko-Kagi,
    Runeforged Hammer, Tyrfing, Lernaean Bow, Golden Blade, Genji''s Guard, Avenging
    Blade, Damaru, Berserker''s Shield, Spectral Armor, Shield Splitter, Chandra''s
    Grace, Kinetic Cuirass, Rage, Breastplate of Valor, Eye of Providence, Pendulum
    Blade, Arondight, Eye of the Storm, Shield of the Phoenix, Heartseeker, Pharaoh''s
    Curse, Eros'' Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.54
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
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.39
    Tekko-Kagi:
      total: 0.42
      efficiency: 0.34
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
      total: 0.44
      efficiency: 0.36
      win: 0.56
      pick: 0.25
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - The Reaper
  - Riptalon
  - The Crusher
  flex_slots:
  - Hydra's Lament
  - Kinetic Cuirass
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
    this god: The Reaper, Jotunn''s Revenge, Riptalon, Amanita Charm, The Crusher,
    Shield of the Phoenix, Chandra''s Grace, Hydra''s Lament, Kinetic Cuirass, Shield
    Splitter, Eye of Providence, Genji''s Guard, Phoenix Feather, Berserker''s Shield,
    Runeforged Hammer, Spectral Armor, Tyrfing, Spirit Robe, Bloodforge, Lernaean
    Bow, Tekko-Kagi, Golden Blade, Breastplate of Valor, Avenging Blade, Damaru, Eye
    of the Storm, Pharaoh''s Curse.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.42
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.29
    Hydra's Lament:
      total: 0.42
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.29
    The Reaper:
      total: 0.46
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.58
    Riptalon:
      total: 0.46
      efficiency: 0.26
      win: 0.59
      pick: 0.13
      fit: 0.63
    The Crusher:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.32
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
    for this god: Jotunn''s Revenge, The Crusher, The Reaper, Riptalon, Avenging Blade,
    Tekko-Kagi, Hydra''s Lament, Tyrfing, Screeching Gargoyle, Runeforged Hammer,
    Lernaean Bow, Oath-Sworn Spear, Golden Blade, Damaru, Berserker''s Shield, Genji''s
    Guard, Pendulum Blade, Heartseeker, Spectral Armor, Rage, Shield Splitter, Kinetic
    Cuirass, Chandra''s Grace, Eye of Providence, Void Stone, Breastplate of Valor,
    Pharaoh''s Curse.'
  slot_scores:
    Avenging Blade:
      total: 0.45
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.53
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.54
    The Reaper:
      total: 0.45
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.5
    Tekko-Kagi:
      total: 0.44
      efficiency: 0.34
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
      total: 0.45
      efficiency: 0.36
      win: 0.56
      pick: 0.25
      fit: 0.43
  starter: *id001
---
