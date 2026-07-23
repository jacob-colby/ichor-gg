---
type: smite-build
god: Cernunnos
mode: Conquest
builds:
- source: community
  aspect: Aspect of Strife
  aspect_pick_rate: 0.43
  aspect_win_rate: 0.58
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.54
    win_rate: 0.55
    alternates:
    - name: Tyrfing
      pick_rate: 0.09
      win_rate: 0.69
    - name: Avenging Blade
      pick_rate: 0.08
      win_rate: 0.55
  - name: Dagger of Frenzy
    pick_rate: 0.36
    win_rate: 0.57
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.61
    - name: Tyrfing
      pick_rate: 0.08
      win_rate: 0.51
  - name: Bracer of The Abyss
    pick_rate: 0.16
    win_rate: 0.59
    alternates:
    - name: Riptalon
      pick_rate: 0.14
      win_rate: 0.59
    - name: Berserker's Shield
      pick_rate: 0.09
      win_rate: 0.6
  - name: Riptalon
    pick_rate: 0.22
    win_rate: 0.59
    alternates:
    - name: Titan's Bane
      pick_rate: 0.15
      win_rate: 0.52
    - name: The Executioner
      pick_rate: 0.07
      win_rate: 0.56
  - name: Titan's Bane
    pick_rate: 0.14
    win_rate: 0.48
    alternates:
    - name: Riptalon
      pick_rate: 0.09
      win_rate: 0.58
    - name: Qin's Blade
      pick_rate: 0.07
      win_rate: 0.62
  - name: Hunter's Bow
    pick_rate: 0.07
    win_rate: 0.59
    alternates:
    - name: Titan's Bane
      pick_rate: 0.08
      win_rate: 0.69
    - name: Deathbringer
      pick_rate: 0.05
      win_rate: 0.55
  source_url: https://smitebrain.com/gods/cernunnos/
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
  - Devourer's Gauntlet
  - Riptalon
  - The Crusher
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
    this god: Jotunn''s Revenge, The Crusher, The Reaper, Hydra''s Lament, Tyrfing,
    Tekko-Kagi, Runeforged Hammer, Lernaean Bow, Titan''s Bane, Golden Blade, Damaru,
    Avenging Blade, Rage, Shield Splitter, Berserker''s Shield, Genji''s Guard, Barbed
    Carver, Pendulum Blade, Spectral Armor, Eye of the Storm, Heartseeker, Arondight,
    Transcendence, Kinetic Cuirass, Musashi''s Dual Swords, Demon Blade, Chandra''s
    Grace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.44
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.5
    Tyrfing:
      total: 0.39
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.5
    Hydra's Lament:
      total: 0.39
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.41
    Devourer's Gauntlet:
      total: 0.42
      efficiency: 0.29
      win: 0.55
      pick: 0.54
      fit: 0.3
    Riptalon:
      total: 0.41
      efficiency: 0.27
      win: 0.59
      pick: 0.22
      fit: 0.49
    The Crusher:
      total: 0.42
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.49
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Rage
  - Devourer's Gauntlet
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
    Tekko-Kagi, Lernaean Bow, Damaru, Runeforged Hammer, Golden Blade, Titan''s Bane,
    Rage, Berserker''s Shield, Avenging Blade, Shield Splitter, Genji''s Guard, Demon
    Blade, Spectral Armor, Musashi''s Dual Swords, Kinetic Cuirass, Barbed Carver,
    Pharaoh''s Curse, Chandra''s Grace, Eye of Providence, Eye of the Storm, Pendulum
    Blade, Eros'' Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.43
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.41
    Rage:
      total: 0.36
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.42
    Devourer's Gauntlet:
      total: 0.41
      efficiency: 0.29
      win: 0.55
      pick: 0.54
      fit: 0.24
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
      total: 0.41
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Devourer's Gauntlet
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
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, The Crusher, The Reaper, Hydra''s Lament, Titan''s Bane,
    Tekko-Kagi, Runeforged Hammer, Tyrfing, Lernaean Bow, Genji''s Guard, Avenging
    Blade, Golden Blade, Damaru, Shield Splitter, Pendulum Blade, Spectral Armor,
    Chandra''s Grace, Berserker''s Shield, Kinetic Cuirass, Rage, Breastplate of Valor,
    Arondight, Heartseeker, Eye of Providence, Eye of the Storm, Barbed Carver, Shield
    of the Phoenix, Transcendence.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.44
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.5
    Hydra's Lament:
      total: 0.39
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.39
    Devourer's Gauntlet:
      total: 0.41
      efficiency: 0.29
      win: 0.55
      pick: 0.54
      fit: 0.21
    Tekko-Kagi:
      total: 0.37
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.5
    The Crusher:
      total: 0.41
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.46
    Titan's Bane:
      total: 0.37
      efficiency: 0.37
      win: 0.48
      pick: 0.14
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Shield Splitter
  - Hydra's Lament
  - Devourer's Gauntlet
  - Riptalon
  - The Crusher
  flex_slots:
  - Shield Splitter
  - Hydra's Lament
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
    this god: The Reaper, Jotunn''s Revenge, Amanita Charm, The Crusher, Shield of
    the Phoenix, Shield Splitter, Chandra''s Grace, Hydra''s Lament, Kinetic Cuirass,
    Eye of Providence, Phoenix Feather, Runeforged Hammer, Bloodforge, Spirit Robe,
    Tyrfing, Spectral Armor, Genji''s Guard, Berserker''s Shield, Lernaean Bow, Tekko-Kagi,
    Avenging Blade, Eye of the Storm, Golden Blade, Breastplate of Valor, Damaru,
    Erosion.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.42
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.33
    Shield Splitter:
      total: 0.38
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.34
    Hydra's Lament:
      total: 0.38
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.3
    Devourer's Gauntlet:
      total: 0.45
      efficiency: 0.29
      win: 0.55
      pick: 0.54
      fit: 0.5
    Riptalon:
      total: 0.43
      efficiency: 0.27
      win: 0.59
      pick: 0.22
      fit: 0.62
    The Crusher:
      total: 0.4
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.36
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
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, The Reaper, Avenging Blade, Tekko-Kagi,
    Titan''s Bane, Hydra''s Lament, Tyrfing, Oath-Sworn Spear, Runeforged Hammer,
    Screeching Gargoyle, Lernaean Bow, Pendulum Blade, Heartseeker, Golden Blade,
    Damaru, Shield Splitter, Rage, Genji''s Guard, Berserker''s Shield, Spectral Armor,
    Kinetic Cuirass, Barbed Carver, Eye of the Storm, Void Stone, Transcendence, Eye
    of Providence.'
  slot_scores:
    Avenging Blade:
      total: 0.4
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.56
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.58
    Riptalon:
      total: 0.42
      efficiency: 0.27
      win: 0.59
      pick: 0.22
      fit: 0.58
    Tekko-Kagi:
      total: 0.4
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.66
    The Crusher:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.6
    Titan's Bane:
      total: 0.39
      efficiency: 0.37
      win: 0.48
      pick: 0.14
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Devourer's Gauntlet
  - Runeforged Hammer
  - The Reaper
  - The Crusher
  flex_slots:
  - Runeforged Hammer
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, The Reaper, The Crusher, Runeforged Hammer, Hydra''s
    Lament, Chandra''s Grace, Amanita Charm, Avenging Blade, Shield of the Phoenix,
    Golden Blade, Tyrfing, Titan''s Bane, Bloodforge, Tekko-Kagi, Lernaean Bow, Spectral
    Armor, Damaru, Berserker''s Shield, Kinetic Cuirass, Eye of the Storm, Shield
    Splitter, Eye of Providence, Rage, Barbed Carver, Phoenix Feather, Genji''s Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.43
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.44
    Hydra's Lament:
      total: 0.39
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.37
    Devourer's Gauntlet:
      total: 0.45
      efficiency: 0.29
      win: 0.55
      pick: 0.54
      fit: 0.52
    Runeforged Hammer:
      total: 0.39
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.38
    The Reaper:
      total: 0.43
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.68
    The Crusher:
      total: 0.41
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.44
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Rage
  - Devourer's Gauntlet
  - Musashi's Dual Swords
  - Damaru
  - The Crusher
  flex_slots:
  - Rage
  - Musashi's Dual Swords
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, The Reaper, The Crusher, Chandra''s Grace, Runeforged
    Hammer, Hydra''s Lament, Amanita Charm, Golden Blade, Shield of the Phoenix, Tyrfing,
    Avenging Blade, Berserker''s Shield, Tekko-Kagi, Lernaean Bow, Damaru, Spectral
    Armor, Bloodforge, Kinetic Cuirass, Rage, Eye of Providence, Phoenix Feather,
    Eye of the Storm, Pharaoh''s Curse, Genji''s Guard, Shield Splitter, Eros'' Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.42
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.36
    Rage:
      total: 0.36
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.36
    Devourer's Gauntlet:
      total: 0.44
      efficiency: 0.29
      win: 0.55
      pick: 0.54
      fit: 0.45
    Musashi's Dual Swords:
      total: 0.34
      efficiency: 0.31
      win: 0.5
      pick: 0.0
      fit: 0.36
    Damaru:
      total: 0.36
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.36
    The Crusher:
      total: 0.4
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.37
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Devourer's Gauntlet
  - Runeforged Hammer
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Runeforged Hammer
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, The Reaper, The Crusher, Hydra''s Lament, Chandra''s Grace,
    Runeforged Hammer, Shield of the Phoenix, Amanita Charm, Titan''s Bane, Avenging
    Blade, Tekko-Kagi, Tyrfing, Spectral Armor, Golden Blade, Kinetic Cuirass, Bloodforge,
    Genji''s Guard, Lernaean Bow, Eye of Providence, Berserker''s Shield, Shield Splitter,
    Phoenix Feather, Eye of the Storm, Damaru, Pendulum Blade, Breastplate of Valor.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.44
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.45
    Hydra's Lament:
      total: 0.39
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.36
    Devourer's Gauntlet:
      total: 0.44
      efficiency: 0.29
      win: 0.55
      pick: 0.54
      fit: 0.43
    Runeforged Hammer:
      total: 0.38
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.31
    The Crusher:
      total: 0.41
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.42
    Titan's Bane:
      total: 0.37
      efficiency: 0.37
      win: 0.48
      pick: 0.14
      fit: 0.32
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Devourer's Gauntlet
  - Riptalon
  - The Crusher
  flex_slots:
  - Kinetic Cuirass
  - Eye of Providence
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
    this god: The Reaper, Amanita Charm, Jotunn''s Revenge, The Crusher, Shield of
    the Phoenix, Chandra''s Grace, Kinetic Cuirass, Eye of Providence, Phoenix Feather,
    Shield Splitter, Runeforged Hammer, Hydra''s Lament, Spectral Armor, Bloodforge,
    Berserker''s Shield, Avenging Blade, Spirit Robe, Genji''s Guard, Eye of the Storm,
    Tyrfing, Golden Blade, Erosion, Lernaean Bow, Breastplate of Valor, Pharaoh''s
    Curse, Tekko-Kagi.'
  slot_scores:
    Eye of Providence:
      total: 0.38
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.27
    Jotunn's Revenge:
      total: 0.41
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.38
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.37
    Devourer's Gauntlet:
      total: 0.45
      efficiency: 0.29
      win: 0.55
      pick: 0.54
      fit: 0.52
    Riptalon:
      total: 0.42
      efficiency: 0.27
      win: 0.59
      pick: 0.22
      fit: 0.61
    The Crusher:
      total: 0.4
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.33
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Devourer's Gauntlet
  - Runeforged Hammer
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Titan's Bane
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Reaper, The Crusher, Avenging Blade, Titan''s
    Bane, Runeforged Hammer, Hydra''s Lament, Tekko-Kagi, Chandra''s Grace, Amanita
    Charm, Oath-Sworn Spear, Shield of the Phoenix, Screeching Gargoyle, Tyrfing,
    Golden Blade, Bloodforge, Spectral Armor, Kinetic Cuirass, Lernaean Bow, Heartseeker,
    Berserker''s Shield, Void Stone, Pendulum Blade, Damaru, Eye of Providence, Eye
    of the Storm, Shield Splitter.'
  slot_scores:
    Avenging Blade:
      total: 0.41
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.64
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.52
    Devourer's Gauntlet:
      total: 0.45
      efficiency: 0.29
      win: 0.55
      pick: 0.54
      fit: 0.47
    Runeforged Hammer:
      total: 0.38
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.34
    The Crusher:
      total: 0.43
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.55
    Titan's Bane:
      total: 0.38
      efficiency: 0.37
      win: 0.48
      pick: 0.14
      fit: 0.45
  starter: *id001
  aspect: Aspect of Strife
---
