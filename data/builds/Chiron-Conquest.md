---
type: smite-build
god: Chiron
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Heroic Tutor
  aspect_pick_rate: 0.12
  aspect_win_rate: 0.51
  slot_order:
  - name: Transcendence
    pick_rate: 0.53
    win_rate: 0.52
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.12
      win_rate: 0.51
    - name: Lernaean Bow
      pick_rate: 0.11
      win_rate: 0.51
  - name: Jotunn's Revenge
    pick_rate: 0.44
    win_rate: 0.53
    alternates:
    - name: Transcendence
      pick_rate: 0.11
      win_rate: 0.52
    - name: Avenging Blade
      pick_rate: 0.09
      win_rate: 0.59
  - name: Heartseeker
    pick_rate: 0.22
    win_rate: 0.53
    alternates:
    - name: The Crusher
      pick_rate: 0.17
      win_rate: 0.61
    - name: Odysseus' Bow
      pick_rate: 0.12
      win_rate: 0.56
  - name: Titan's Bane
    pick_rate: 0.39
    win_rate: 0.53
    alternates:
    - name: Heartseeker
      pick_rate: 0.15
      win_rate: 0.64
    - name: The Crusher
      pick_rate: 0.08
      win_rate: 0.48
  - name: The Crusher
    pick_rate: 0.08
    win_rate: 0.51
    alternates:
    - name: Titan's Bane
      pick_rate: 0.21
      win_rate: 0.55
    - name: Heartseeker
      pick_rate: 0.13
      win_rate: 0.58
  - name: Hunter's Bow
    pick_rate: 0.07
    win_rate: 0.52
    alternates:
    - name: Skeggox
      pick_rate: 0.07
      win_rate: 0.58
    - name: Titan's Bane
      pick_rate: 0.07
      win_rate: 0.58
  source_url: https://smitebrain.com/gods/chiron/
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
  - The Reaper
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
    this god: The Crusher, The Reaper, Hydra''s Lament, Tekko-Kagi, Tyrfing, Lernaean
    Bow, Runeforged Hammer, Golden Blade, Damaru, Avenging Blade, Rage, Shield Splitter,
    Berserker''s Shield, Genji''s Guard, Barbed Carver, Pendulum Blade, Spectral Armor,
    Eye of the Storm, Arondight, Kinetic Cuirass, Riptalon, Demon Blade, Musashi''s
    Dual Swords, Chandra''s Grace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.55
      win: 0.53
      pick: 0.44
      fit: 0.49
    Transcendence:
      total: 0.43
      efficiency: 0.4
      win: 0.52
      pick: 0.53
      fit: 0.19
    Hydra's Lament:
      total: 0.39
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.4
    The Reaper:
      total: 0.4
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.48
    The Crusher:
      total: 0.43
      efficiency: 0.49
      win: 0.51
      pick: 0.08
      fit: 0.48
    Titan's Bane:
      total: 0.43
      efficiency: 0.37
      win: 0.53
      pick: 0.39
      fit: 0.38
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Transcendence
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
    this god: The Crusher, The Reaper, Hydra''s Lament, Tyrfing, Tekko-Kagi, Lernaean
    Bow, Damaru, Runeforged Hammer, Golden Blade, Rage, Berserker''s Shield, Avenging
    Blade, Shield Splitter, Genji''s Guard, Demon Blade, Spectral Armor, Musashi''s
    Dual Swords, Kinetic Cuirass, Barbed Carver, Riptalon, Pharaoh''s Curse, Chandra''s
    Grace, Eye of Providence, Eye of the Storm, Pendulum Blade, Eros'' Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.55
      win: 0.53
      pick: 0.44
      fit: 0.41
    Transcendence:
      total: 0.42
      efficiency: 0.4
      win: 0.52
      pick: 0.53
      fit: 0.15
    Rage:
      total: 0.36
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.42
    Damaru:
      total: 0.37
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.42
    Demon Blade:
      total: 0.35
      efficiency: 0.22
      win: 0.5
      pick: 0.0
      fit: 0.64
    The Crusher:
      total: 0.42
      efficiency: 0.49
      win: 0.51
      pick: 0.08
      fit: 0.42
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
  - The Reaper
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Crusher, The Reaper, Hydra''s Lament, Tekko-Kagi, Runeforged Hammer,
    Tyrfing, Lernaean Bow, Genji''s Guard, Avenging Blade, Golden Blade, Damaru, Shield
    Splitter, Pendulum Blade, Spectral Armor, Chandra''s Grace, Berserker''s Shield,
    Kinetic Cuirass, Rage, Breastplate of Valor, Arondight, Eye of Providence, Eye
    of the Storm, Barbed Carver, Shield of the Phoenix.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.55
      win: 0.53
      pick: 0.44
      fit: 0.5
    Transcendence:
      total: 0.42
      efficiency: 0.4
      win: 0.52
      pick: 0.53
      fit: 0.14
    Hydra's Lament:
      total: 0.39
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.39
    The Reaper:
      total: 0.39
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.43
    The Crusher:
      total: 0.43
      efficiency: 0.49
      win: 0.51
      pick: 0.08
      fit: 0.46
    Titan's Bane:
      total: 0.43
      efficiency: 0.37
      win: 0.53
      pick: 0.39
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - The Crusher
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Titan's Bane
  - Amanita Charm
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
    this god: The Reaper, The Crusher, Amanita Charm, Shield of the Phoenix, Chandra''s
    Grace, Shield Splitter, Kinetic Cuirass, Hydra''s Lament, Eye of Providence, Phoenix
    Feather, Runeforged Hammer, Spirit Robe, Bloodforge, Tyrfing, Genji''s Guard,
    Spectral Armor, Riptalon, Berserker''s Shield, Lernaean Bow, Tekko-Kagi, Avenging
    Blade, Eye of the Storm, Devourer''s Gauntlet, Golden Blade, Breastplate of Valor,
    Damaru, Erosion.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.55
      win: 0.53
      pick: 0.44
      fit: 0.32
    Transcendence:
      total: 0.42
      efficiency: 0.4
      win: 0.52
      pick: 0.53
      fit: 0.12
    The Reaper:
      total: 0.42
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.62
    The Crusher:
      total: 0.41
      efficiency: 0.49
      win: 0.51
      pick: 0.08
      fit: 0.35
    Titan's Bane:
      total: 0.41
      efficiency: 0.37
      win: 0.53
      pick: 0.39
      fit: 0.25
    Amanita Charm:
      total: 0.41
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
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Heartseeker
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
    for this god: The Crusher, The Reaper, Avenging Blade, Tekko-Kagi, Hydra''s Lament,
    Tyrfing, Oath-Sworn Spear, Runeforged Hammer, Screeching Gargoyle, Lernaean Bow,
    Pendulum Blade, Golden Blade, Damaru, Riptalon, Shield Splitter, Genji''s Guard,
    Rage, Berserker''s Shield, Spectral Armor, Kinetic Cuirass, Void Stone, Barbed
    Carver, Eye of the Storm, Eye of Providence, Chandra''s Grace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.55
      win: 0.53
      pick: 0.44
      fit: 0.58
    Transcendence:
      total: 0.43
      efficiency: 0.4
      win: 0.52
      pick: 0.53
      fit: 0.15
    The Reaper:
      total: 0.41
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.57
    The Crusher:
      total: 0.45
      efficiency: 0.49
      win: 0.51
      pick: 0.08
      fit: 0.59
    Heartseeker:
      total: 0.41
      efficiency: 0.28
      win: 0.53
      pick: 0.22
      fit: 0.59
    Titan's Bane:
      total: 0.45
      efficiency: 0.37
      win: 0.53
      pick: 0.39
      fit: 0.49
  starter: *id001
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
  - The Reaper
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: The Crusher, The Reaper, Hydra''s Lament, Runeforged Hammer, Damaru,
    Tekko-Kagi, Rage, Tyrfing, Avenging Blade, Shield Splitter, Spectral Armor, Pendulum
    Blade, Lernaean Bow, Barbed Carver, Genji''s Guard, Golden Blade, Arondight, Musashi''s
    Dual Swords, Eye of the Storm, Amanita Charm, Kinetic Cuirass, Chandra''s Grace,
    Bloodforge, Breastplate of Valor.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.55
      win: 0.53
      pick: 0.44
      fit: 0.57
    Transcendence:
      total: 0.43
      efficiency: 0.4
      win: 0.52
      pick: 0.53
      fit: 0.22
    Hydra's Lament:
      total: 0.4
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.45
    The Reaper:
      total: 0.41
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.44
      efficiency: 0.49
      win: 0.51
      pick: 0.08
      fit: 0.54
    Titan's Bane:
      total: 0.44
      efficiency: 0.37
      win: 0.53
      pick: 0.39
      fit: 0.44
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Rage
  - Damaru
  - Demon Blade
  - The Crusher
  flex_slots:
  - Rage
  - Demon Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, The Reaper, Hydra''s Lament, Tyrfing, Tekko-Kagi, Lernaean
    Bow, Damaru, Runeforged Hammer, Golden Blade, Rage, Spectral Armor, Berserker''s
    Shield, Avenging Blade, Pharaoh''s Curse, Eros'' Bow, Shield Splitter, Genji''s
    Guard, Demon Blade, Amanita Charm, Musashi''s Dual Swords, Kinetic Cuirass, Barbed
    Carver, Riptalon, Chandra''s Grace, Eye of Providence, Shogun''s Ofuda.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.55
      win: 0.53
      pick: 0.44
      fit: 0.41
    Transcendence:
      total: 0.42
      efficiency: 0.4
      win: 0.52
      pick: 0.53
      fit: 0.15
    Rage:
      total: 0.36
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.42
    Damaru:
      total: 0.37
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.42
    Demon Blade:
      total: 0.35
      efficiency: 0.22
      win: 0.5
      pick: 0.0
      fit: 0.64
    The Crusher:
      total: 0.42
      efficiency: 0.49
      win: 0.51
      pick: 0.08
      fit: 0.42
  starter: *id001
  aspect: Aspect of the Heroic Tutor
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
  - The Reaper
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Crusher, The Reaper, Hydra''s Lament, Runeforged Hammer, Tekko-Kagi,
    Spectral Armor, Genji''s Guard, Pendulum Blade, Avenging Blade, Damaru, Tyrfing,
    Shield Splitter, Rage, Chandra''s Grace, Lernaean Bow, Arondight, Breastplate
    of Valor, Amanita Charm, Kinetic Cuirass, Golden Blade, Barbed Carver, Eye of
    the Storm, Eye of Providence, Shield of the Phoenix.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.55
      win: 0.53
      pick: 0.44
      fit: 0.56
    Transcendence:
      total: 0.43
      efficiency: 0.4
      win: 0.52
      pick: 0.53
      fit: 0.16
    Hydra's Lament:
      total: 0.4
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.4
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.48
    The Crusher:
      total: 0.44
      efficiency: 0.49
      win: 0.51
      pick: 0.08
      fit: 0.5
    Titan's Bane:
      total: 0.43
      efficiency: 0.37
      win: 0.53
      pick: 0.39
      fit: 0.4
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - The Crusher
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - The Crusher
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, The Reaper, The Crusher, Shield of the Phoenix, Shield
    Splitter, Chandra''s Grace, Kinetic Cuirass, Spectral Armor, Hydra''s Lament,
    Eye of Providence, Phoenix Feather, Spirit Robe, Runeforged Hammer, Bloodforge,
    Genji''s Guard, Erosion, Eye of the Storm, Avenging Blade, Devourer''s Gauntlet,
    Breastplate of Valor, Tyrfing, Umbral Link, Riptalon, Damaru, Berserker''s Shield,
    Glorious Pridwen, Pharaoh''s Curse.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.55
      win: 0.53
      pick: 0.44
      fit: 0.35
    Transcendence:
      total: 0.42
      efficiency: 0.4
      win: 0.52
      pick: 0.53
      fit: 0.14
    The Reaper:
      total: 0.43
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.65
    The Crusher:
      total: 0.42
      efficiency: 0.49
      win: 0.51
      pick: 0.08
      fit: 0.37
    Titan's Bane:
      total: 0.41
      efficiency: 0.37
      win: 0.53
      pick: 0.39
      fit: 0.27
    Amanita Charm:
      total: 0.43
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.64
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, The Reaper, Avenging Blade, Hydra''s Lament, Tekko-Kagi,
    Oath-Sworn Spear, Pendulum Blade, Runeforged Hammer, Screeching Gargoyle, Damaru,
    Spectral Armor, Tyrfing, Void Stone, Rage, Shield Splitter, Void Shield, Lernaean
    Bow, Genji''s Guard, Riptalon, Amanita Charm, Barbed Carver, Golden Blade, Kinetic
    Cuirass, Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.55
      win: 0.53
      pick: 0.44
      fit: 0.66
    Transcendence:
      total: 0.43
      efficiency: 0.4
      win: 0.52
      pick: 0.53
      fit: 0.18
    The Reaper:
      total: 0.43
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.65
    The Crusher:
      total: 0.46
      efficiency: 0.49
      win: 0.51
      pick: 0.08
      fit: 0.66
    Heartseeker:
      total: 0.42
      efficiency: 0.28
      win: 0.53
      pick: 0.22
      fit: 0.66
    Titan's Bane:
      total: 0.46
      efficiency: 0.37
      win: 0.53
      pick: 0.39
      fit: 0.56
  starter: *id001
  aspect: Aspect of the Heroic Tutor
---
