---
type: smite-build
god: Izanami
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Tyrfing
    pick_rate: 0.46
    win_rate: 0.62
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.33
      win_rate: 0.62
    - name: Avenging Blade
      pick_rate: 0.05
      win_rate: 0.51
  - name: Bragi's Harp
    pick_rate: 0.27
    win_rate: 0.64
    alternates:
    - name: Dagger of Frenzy
      pick_rate: 0.18
      win_rate: 0.56
    - name: Tyrfing
      pick_rate: 0.13
      win_rate: 0.65
  - name: Odysseus' Bow
    pick_rate: 0.26
    win_rate: 0.64
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.19
      win_rate: 0.62
    - name: Riptalon
      pick_rate: 0.11
      win_rate: 0.65
  - name: Titan's Bane
    pick_rate: 0.26
    win_rate: 0.63
    alternates:
    - name: The Executioner
      pick_rate: 0.13
      win_rate: 0.63
    - name: Odysseus' Bow
      pick_rate: 0.12
      win_rate: 0.6
  - name: Qin's Blade
    pick_rate: 0.16
    win_rate: 0.6
    alternates:
    - name: Titan's Bane
      pick_rate: 0.23
      win_rate: 0.6
    - name: Riptalon
      pick_rate: 0.11
      win_rate: 0.72
  - name: Deathbringer
    pick_rate: 0.1
    win_rate: 0.74
    alternates:
    - name: Titan's Bane
      pick_rate: 0.13
      win_rate: 0.63
    - name: Riptalon
      pick_rate: 0.1
      win_rate: 0.63
  source_url: https://smitebrain.com/gods/izanami/
  last_verified: '2026-07-23'
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - The Crusher
  - Deathbringer
  - Titan's Bane
  flex_slots:
  - The Crusher
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
    this god: Jotunn''s Revenge, The Crusher, The Reaper, Hydra''s Lament, Tekko-Kagi,
    Lernaean Bow, Golden Blade, Runeforged Hammer, Damaru, Rage, Berserker''s Shield,
    Avenging Blade, Shield Splitter, Genji''s Guard, Demon Blade, Spectral Armor,
    Kinetic Cuirass, Pharaoh''s Curse, Barbed Carver, Musashi''s Dual Swords, Riptalon,
    Eros'' Bow, Eye of the Storm, Chandra''s Grace, Eye of Providence, Transcendence.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.41
    Tyrfing:
      total: 0.51
      efficiency: 0.39
      win: 0.62
      pick: 0.46
      fit: 0.51
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
    Deathbringer:
      total: 0.47
      efficiency: 0.22
      win: 0.74
      pick: 0.1
      fit: 0.41
    Titan's Bane:
      total: 0.47
      efficiency: 0.37
      win: 0.63
      pick: 0.26
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
  - Damaru
  - Deathbringer
  - Titan's Bane
  flex_slots:
  - Damaru
  - Rage
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
    this god: Jotunn''s Revenge, The Crusher, The Reaper, Hydra''s Lament, Tekko-Kagi,
    Damaru, Lernaean Bow, Runeforged Hammer, Golden Blade, Rage, Berserker''s Shield,
    Avenging Blade, Shield Splitter, Genji''s Guard, Demon Blade, Musashi''s Dual
    Swords, Spectral Armor, Kinetic Cuirass, Barbed Carver, Pharaoh''s Curse, Chandra''s
    Grace, Eye of Providence, Eye of the Storm, Riptalon, Eros'' Bow, Transcendence.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.4
    Tyrfing:
      total: 0.51
      efficiency: 0.39
      win: 0.62
      pick: 0.46
      fit: 0.48
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
    Deathbringer:
      total: 0.48
      efficiency: 0.22
      win: 0.74
      pick: 0.1
      fit: 0.43
    Titan's Bane:
      total: 0.47
      efficiency: 0.37
      win: 0.63
      pick: 0.26
      fit: 0.3
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - The Crusher
  - Deathbringer
  - Titan's Bane
  flex_slots:
  - Deathbringer
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
    god: Jotunn''s Revenge, The Crusher, The Reaper, Hydra''s Lament, Tekko-Kagi,
    Runeforged Hammer, Lernaean Bow, Golden Blade, Genji''s Guard, Damaru, Avenging
    Blade, Berserker''s Shield, Shield Splitter, Spectral Armor, Rage, Chandra''s
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
      total: 0.5
      efficiency: 0.39
      win: 0.62
      pick: 0.46
      fit: 0.4
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
    Deathbringer:
      total: 0.46
      efficiency: 0.22
      win: 0.74
      pick: 0.1
      fit: 0.3
    Titan's Bane:
      total: 0.47
      efficiency: 0.37
      win: 0.63
      pick: 0.26
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Deathbringer
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Titan's Bane
  - Deathbringer
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
    this god: The Reaper, Jotunn''s Revenge, Amanita Charm, The Crusher, Shield of
    the Phoenix, Chandra''s Grace, Shield Splitter, Kinetic Cuirass, Hydra''s Lament,
    Eye of Providence, Phoenix Feather, Berserker''s Shield, Spirit Robe, Runeforged
    Hammer, Riptalon, Spectral Armor, Genji''s Guard, Bloodforge, Lernaean Bow, Tekko-Kagi,
    Golden Blade, Avenging Blade, Damaru, Eye of the Storm, Devourer''s Gauntlet,
    Breastplate of Valor, Pharaoh''s Curse.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.28
    Tyrfing:
      total: 0.49
      efficiency: 0.39
      win: 0.62
      pick: 0.46
      fit: 0.37
    The Reaper:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.57
    Deathbringer:
      total: 0.45
      efficiency: 0.22
      win: 0.74
      pick: 0.1
      fit: 0.27
    Titan's Bane:
      total: 0.46
      efficiency: 0.37
      win: 0.63
      pick: 0.26
      fit: 0.21
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
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - The Crusher
  - Deathbringer
  - Titan's Bane
  flex_slots:
  - Deathbringer
  - The Reaper
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
    Hydra''s Lament, Oath-Sworn Spear, Runeforged Hammer, Screeching Gargoyle, Lernaean
    Bow, Golden Blade, Damaru, Riptalon, Heartseeker, Berserker''s Shield, Pendulum
    Blade, Rage, Shield Splitter, Genji''s Guard, Spectral Armor, Kinetic Cuirass,
    Void Stone, Eye of Providence, Chandra''s Grace, Void Shield, Pharaoh''s Curse.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.52
    Tyrfing:
      total: 0.5
      efficiency: 0.39
      win: 0.62
      pick: 0.46
      fit: 0.43
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
    Deathbringer:
      total: 0.46
      efficiency: 0.22
      win: 0.74
      pick: 0.1
      fit: 0.33
    Titan's Bane:
      total: 0.49
      efficiency: 0.37
      win: 0.63
      pick: 0.26
      fit: 0.44
  starter: *id001
---
