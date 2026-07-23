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
  - Tyrfing
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Hydra's Lament
  - Tyrfing
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
    this god: The Crusher, The Reaper, Hydra''s Lament, Tyrfing, Tekko-Kagi, Lernaean
    Bow, Runeforged Hammer, Golden Blade, Damaru, Rage, Berserker''s Shield, Avenging
    Blade, Shield Splitter, Genji''s Guard, Demon Blade, Spectral Armor, Kinetic Cuirass,
    Barbed Carver, Musashi''s Dual Swords, Riptalon, Pharaoh''s Curse, Eye of the
    Storm, Pendulum Blade, Eros'' Bow, Chandra''s Grace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.55
      win: 0.53
      pick: 0.44
      fit: 0.44
    Tyrfing:
      total: 0.44
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.5
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
      fit: 0.43
    The Crusher:
      total: 0.47
      efficiency: 0.49
      win: 0.51
      pick: 0.08
      fit: 0.44
    Titan's Bane:
      total: 0.44
      efficiency: 0.37
      win: 0.53
      pick: 0.39
      fit: 0.34
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
    this god: The Crusher, The Reaper, Hydra''s Lament, Tyrfing, Tekko-Kagi, Lernaean
    Bow, Damaru, Runeforged Hammer, Golden Blade, Rage, Berserker''s Shield, Avenging
    Blade, Shield Splitter, Genji''s Guard, Demon Blade, Spectral Armor, Musashi''s
    Dual Swords, Kinetic Cuirass, Barbed Carver, Riptalon, Pharaoh''s Curse, Chandra''s
    Grace, Eye of Providence, Eye of the Storm, Pendulum Blade, Eros'' Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.55
      win: 0.53
      pick: 0.44
      fit: 0.41
    Rage:
      total: 0.41
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.41
    Damaru:
      total: 0.42
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.42
    Demon Blade:
      total: 0.4
      efficiency: 0.22
      win: 0.5
      pick: 0.0
      fit: 0.64
    The Crusher:
      total: 0.47
      efficiency: 0.49
      win: 0.51
      pick: 0.08
      fit: 0.42
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
    god: The Crusher, The Reaper, Hydra''s Lament, Tekko-Kagi, Tyrfing, Runeforged
    Hammer, Lernaean Bow, Golden Blade, Genji''s Guard, Damaru, Avenging Blade, Berserker''s
    Shield, Shield Splitter, Spectral Armor, Rage, Chandra''s Grace, Pendulum Blade,
    Kinetic Cuirass, Breastplate of Valor, Eye of Providence, Arondight, Eye of the
    Storm, Shield of the Phoenix, Barbed Carver.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.55
      win: 0.53
      pick: 0.44
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
      total: 0.47
      efficiency: 0.49
      win: 0.51
      pick: 0.08
      fit: 0.43
    Titan's Bane:
      total: 0.44
      efficiency: 0.37
      win: 0.53
      pick: 0.39
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
  - Shield Splitter
  - Hydra's Lament
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
    this god: The Reaper, Amanita Charm, The Crusher, Shield of the Phoenix, Chandra''s
    Grace, Shield Splitter, Hydra''s Lament, Kinetic Cuirass, Eye of Providence, Phoenix
    Feather, Tyrfing, Runeforged Hammer, Riptalon, Spirit Robe, Berserker''s Shield,
    Bloodforge, Spectral Armor, Genji''s Guard, Lernaean Bow, Tekko-Kagi, Golden Blade,
    Avenging Blade, Damaru, Devourer''s Gauntlet, Eye of the Storm, Breastplate of
    Valor, Pharaoh''s Curse.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.55
      win: 0.53
      pick: 0.44
      fit: 0.3
    Shield Splitter:
      total: 0.43
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.31
    Hydra's Lament:
      total: 0.42
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.28
    The Reaper:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.59
    The Crusher:
      total: 0.45
      efficiency: 0.49
      win: 0.51
      pick: 0.08
      fit: 0.33
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
    for this god: The Crusher, The Reaper, Avenging Blade, Tekko-Kagi, Hydra''s Lament,
    Tyrfing, Oath-Sworn Spear, Runeforged Hammer, Lernaean Bow, Screeching Gargoyle,
    Golden Blade, Damaru, Riptalon, Pendulum Blade, Berserker''s Shield, Rage, Shield
    Splitter, Genji''s Guard, Spectral Armor, Kinetic Cuirass, Void Stone, Eye of
    Providence, Eye of the Storm, Barbed Carver, Chandra''s Grace.'
  slot_scores:
    Avenging Blade:
      total: 0.45
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.54
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.55
      win: 0.53
      pick: 0.44
      fit: 0.53
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
      total: 0.49
      efficiency: 0.49
      win: 0.51
      pick: 0.08
      fit: 0.55
    Titan's Bane:
      total: 0.45
      efficiency: 0.37
      win: 0.53
      pick: 0.39
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Damaru
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Hydra's Lament
  - Damaru
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
    this god: The Crusher, The Reaper, Hydra''s Lament, Damaru, Runeforged Hammer,
    Rage, Tekko-Kagi, Tyrfing, Avenging Blade, Spectral Armor, Shield Splitter, Lernaean
    Bow, Musashi''s Dual Swords, Pendulum Blade, Genji''s Guard, Barbed Carver, Golden
    Blade, Arondight, Eye of the Storm, Amanita Charm, Kinetic Cuirass, Chandra''s
    Grace, Breastplate of Valor, Eye of Providence.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.55
      win: 0.53
      pick: 0.44
      fit: 0.53
    Hydra's Lament:
      total: 0.45
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.53
    Damaru:
      total: 0.43
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.49
    The Crusher:
      total: 0.48
      efficiency: 0.49
      win: 0.51
      pick: 0.08
      fit: 0.51
    Titan's Bane:
      total: 0.45
      efficiency: 0.37
      win: 0.53
      pick: 0.39
      fit: 0.41
  starter: *id001
  aspect: Aspect of the Heroic Tutor
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
      total: 0.52
      efficiency: 0.55
      win: 0.53
      pick: 0.44
      fit: 0.41
    Rage:
      total: 0.41
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.41
    Damaru:
      total: 0.42
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.42
    Demon Blade:
      total: 0.4
      efficiency: 0.22
      win: 0.5
      pick: 0.0
      fit: 0.64
    The Crusher:
      total: 0.47
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
  - Hydra's Lament
  - Transcendence
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
    god: The Crusher, The Reaper, Hydra''s Lament, Runeforged Hammer, Spectral Armor,
    Damaru, Tekko-Kagi, Genji''s Guard, Avenging Blade, Pendulum Blade, Tyrfing, Rage,
    Shield Splitter, Chandra''s Grace, Amanita Charm, Lernaean Bow, Breastplate of
    Valor, Arondight, Kinetic Cuirass, Golden Blade, Eye of the Storm, Eye of Providence,
    Barbed Carver, Shield of the Phoenix.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.55
      win: 0.53
      pick: 0.44
      fit: 0.53
    Transcendence:
      total: 0.42
      efficiency: 0.4
      win: 0.52
      pick: 0.53
      fit: 0.15
    Hydra's Lament:
      total: 0.44
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.4
    The Reaper:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.45
    The Crusher:
      total: 0.48
      efficiency: 0.49
      win: 0.51
      pick: 0.08
      fit: 0.48
    Titan's Bane:
      total: 0.44
      efficiency: 0.37
      win: 0.53
      pick: 0.39
      fit: 0.38
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Shield Splitter
  - The Reaper
  - The Crusher
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Spectral Armor
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
    this god: Amanita Charm, The Reaper, The Crusher, Shield of the Phoenix, Shield
    Splitter, Chandra''s Grace, Spectral Armor, Kinetic Cuirass, Hydra''s Lament,
    Eye of Providence, Phoenix Feather, Spirit Robe, Runeforged Hammer, Bloodforge,
    Genji''s Guard, Erosion, Damaru, Eye of the Storm, Avenging Blade, Devourer''s
    Gauntlet, Breastplate of Valor, Tyrfing, Umbral Link, Riptalon, Rage, Berserker''s
    Shield, Pharaoh''s Curse.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.55
      win: 0.53
      pick: 0.44
      fit: 0.34
    Shield Splitter:
      total: 0.43
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.36
    The Reaper:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
    The Crusher:
      total: 0.46
      efficiency: 0.49
      win: 0.51
      pick: 0.08
      fit: 0.36
    Spectral Armor:
      total: 0.43
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.21
    Amanita Charm:
      total: 0.48
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Avenging Blade
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
    Oath-Sworn Spear, Runeforged Hammer, Screeching Gargoyle, Pendulum Blade, Damaru,
    Spectral Armor, Rage, Tyrfing, Void Stone, Shield Splitter, Void Shield, Genji''s
    Guard, Lernaean Bow, Amanita Charm, Kinetic Cuirass, Golden Blade, Barbed Carver,
    Riptalon, Musashi''s Dual Swords, Eye of the Storm.'
  slot_scores:
    Avenging Blade:
      total: 0.45
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.57
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.55
      win: 0.53
      pick: 0.44
      fit: 0.62
    The Reaper:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.62
    The Crusher:
      total: 0.5
      efficiency: 0.49
      win: 0.51
      pick: 0.08
      fit: 0.63
    Heartseeker:
      total: 0.44
      efficiency: 0.28
      win: 0.53
      pick: 0.22
      fit: 0.63
    Titan's Bane:
      total: 0.47
      efficiency: 0.37
      win: 0.53
      pick: 0.39
      fit: 0.53
  starter: *id001
  aspect: Aspect of the Heroic Tutor
---
