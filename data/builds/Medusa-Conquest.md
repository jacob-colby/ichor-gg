---
type: smite-build
god: Medusa
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Transcendence
    pick_rate: 0.23
    win_rate: 0.5
    alternates:
    - name: Avenging Blade
      pick_rate: 0.21
      win_rate: 0.54
    - name: Devourer's Gauntlet
      pick_rate: 0.13
      win_rate: 0.45
  - name: Avenging Blade
    pick_rate: 0.16
    win_rate: 0.51
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.1
      win_rate: 0.4
    - name: Sun Beam Bow
      pick_rate: 0.09
      win_rate: 0.57
  - name: The Executioner
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Riptalon
      pick_rate: 0.12
      win_rate: 0.41
    - name: The Crusher
      pick_rate: 0.06
      win_rate: 0.5
  - name: Titan's Bane
    pick_rate: 0.27
    win_rate: 0.44
    alternates:
    - name: Riptalon
      pick_rate: 0.1
      win_rate: 0.6
    - name: Qin's Blade
      pick_rate: 0.07
      win_rate: 0.41
  - name: Heartseeker
    pick_rate: 0.09
    win_rate: 0.59
    alternates:
    - name: Titan's Bane
      pick_rate: 0.21
      win_rate: 0.59
    - name: Riptalon
      pick_rate: 0.08
      win_rate: 0.44
  - name: Hunter's Bow
    pick_rate: 0.06
    win_rate: 0.68
    alternates:
    - name: Titan's Bane
      pick_rate: 0.09
      win_rate: 0.67
    - name: Void Shard
      pick_rate: 0.05
      win_rate: 0.53
  source_url: https://smitebrain.com/gods/medusa/
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
  - The Crusher
  - Heartseeker
  flex_slots:
  - Tyrfing
  - Heartseeker
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
    this god: Jotunn''s Revenge, The Crusher, The Reaper, Hydra''s Lament, Tyrfing,
    Tekko-Kagi, Lernaean Bow, Golden Blade, Runeforged Hammer, Damaru, Rage, Berserker''s
    Shield, Shield Splitter, Genji''s Guard, Demon Blade, Spectral Armor, Kinetic
    Cuirass, Pharaoh''s Curse, Barbed Carver, Musashi''s Dual Swords, Riptalon, Eros''
    Bow, Eye of the Storm, Chandra''s Grace, Eye of Providence.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.41
    Tyrfing:
      total: 0.44
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.51
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
      fit: 0.41
    The Crusher:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.41
    Heartseeker:
      total: 0.43
      efficiency: 0.28
      win: 0.59
      pick: 0.09
      fit: 0.41
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
    this god: Jotunn''s Revenge, The Crusher, The Reaper, Hydra''s Lament, Tyrfing,
    Tekko-Kagi, Damaru, Lernaean Bow, Runeforged Hammer, Golden Blade, Rage, Berserker''s
    Shield, Shield Splitter, Genji''s Guard, Demon Blade, Musashi''s Dual Swords,
    Spectral Armor, Kinetic Cuirass, Barbed Carver, Pharaoh''s Curse, Chandra''s Grace,
    Eye of Providence, Eye of the Storm, Riptalon, Eros'' Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.4
    Rage:
      total: 0.42
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.43
    The Reaper:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.39
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
  - Hydra's Lament
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  - Heartseeker
  flex_slots:
  - Heartseeker
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
    god: Jotunn''s Revenge, The Crusher, The Reaper, Hydra''s Lament, Heartseeker,
    Tekko-Kagi, Tyrfing, Runeforged Hammer, Lernaean Bow, Golden Blade, Genji''s Guard,
    Damaru, Berserker''s Shield, Shield Splitter, Spectral Armor, Rage, Chandra''s
    Grace, Pendulum Blade, Kinetic Cuirass, Breastplate of Valor, Eye of Providence,
    Arondight, Eye of the Storm, Shield of the Phoenix, Barbed Carver.'
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
    Heartseeker:
      total: 0.43
      efficiency: 0.28
      win: 0.59
      pick: 0.09
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
    this god: The Reaper, Jotunn''s Revenge, Amanita Charm, The Crusher, Shield of
    the Phoenix, Chandra''s Grace, Shield Splitter, Kinetic Cuirass, Hydra''s Lament,
    Eye of Providence, Phoenix Feather, Tyrfing, Berserker''s Shield, Spirit Robe,
    Runeforged Hammer, Riptalon, Spectral Armor, Genji''s Guard, Bloodforge, Lernaean
    Bow, Tekko-Kagi, Golden Blade, Damaru, Eye of the Storm, Breastplate of Valor,
    Devourer''s Gauntlet, Pharaoh''s Curse.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.28
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.3
    Shield Splitter:
      total: 0.43
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.31
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
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  - Heartseeker
  flex_slots:
  - Heartseeker
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
    for this god: Jotunn''s Revenge, The Crusher, The Reaper, Heartseeker, Tekko-Kagi,
    Hydra''s Lament, Tyrfing, Oath-Sworn Spear, Runeforged Hammer, Screeching Gargoyle,
    Lernaean Bow, Golden Blade, Damaru, Riptalon, Berserker''s Shield, Pendulum Blade,
    Rage, Genji''s Guard, Shield Splitter, Spectral Armor, Kinetic Cuirass, Void Stone,
    Eye of Providence, Chandra''s Grace, Pharaoh''s Curse, Void Shield.'
  slot_scores:
    Avenging Blade:
      total: 0.46
      efficiency: 0.41
      win: 0.51
      pick: 0.16
      fit: 0.53
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.52
    The Reaper:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.52
    Tekko-Kagi:
      total: 0.44
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.64
    The Crusher:
      total: 0.48
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.54
    Heartseeker:
      total: 0.45
      efficiency: 0.28
      win: 0.59
      pick: 0.09
      fit: 0.54
  starter: *id001
---
