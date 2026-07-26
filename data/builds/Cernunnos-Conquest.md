---
type: smite-build
god: Cernunnos
mode: Conquest
builds:
- source: community
  aspect: Aspect of Strife
  aspect_pick_rate: 0.44
  aspect_win_rate: 0.58
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.54
    win_rate: 0.57
    alternates:
    - name: Tyrfing
      pick_rate: 0.09
      win_rate: 0.67
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.58
  - name: Dagger of Frenzy
    pick_rate: 0.36
    win_rate: 0.57
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.64
    - name: Tyrfing
      pick_rate: 0.07
      win_rate: 0.47
  - name: Bracer of The Abyss
    pick_rate: 0.15
    win_rate: 0.58
    alternates:
    - name: Riptalon
      pick_rate: 0.14
      win_rate: 0.59
    - name: Berserker's Shield
      pick_rate: 0.09
      win_rate: 0.61
  - name: Riptalon
    pick_rate: 0.19
    win_rate: 0.57
    alternates:
    - name: Titan's Bane
      pick_rate: 0.13
      win_rate: 0.53
    - name: The Executioner
      pick_rate: 0.08
      win_rate: 0.56
  - name: Titan's Bane
    pick_rate: 0.13
    win_rate: 0.49
    alternates:
    - name: Riptalon
      pick_rate: 0.11
      win_rate: 0.62
    - name: Qin's Blade
      pick_rate: 0.07
      win_rate: 0.59
  - name: Hunter's Bow
    pick_rate: 0.07
    win_rate: 0.61
    alternates:
    - name: Titan's Bane
      pick_rate: 0.07
      win_rate: 0.69
    - name: Riptalon
      pick_rate: 0.05
      win_rate: 0.72
  source_url: https://smitebrain.com/gods/cernunnos/
  last_verified: '2026-07-25'
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
    Tekko-Kagi, Lernaean Bow, Runeforged Hammer, Golden Blade, Damaru, Avenging Blade,
    Berserker''s Shield, Rage, Titan''s Bane, Shield Splitter, Genji''s Guard, Spectral
    Armor, Demon Blade, Kinetic Cuirass, Eye of the Storm, Pharaoh''s Curse, Eros''
    Bow, Barbed Carver, Musashi''s Dual Swords, Eye of Providence, Chandra''s Grace,
    Transcendence.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.44
    Tyrfing:
      total: 0.43
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.51
    Hydra's Lament:
      total: 0.44
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.37
    The Reaper:
      total: 0.44
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.44
    Tekko-Kagi:
      total: 0.43
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.58
    The Crusher:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.45
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, The Crusher, The Reaper, Hydra''s Lament, Tyrfing,
    Tekko-Kagi, Lernaean Bow, Damaru, Runeforged Hammer, Golden Blade, Rage, Berserker''s
    Shield, Avenging Blade, Genji''s Guard, Titan''s Bane, Shield Splitter, Spectral
    Armor, Demon Blade, Kinetic Cuirass, Musashi''s Dual Swords, Pharaoh''s Curse,
    Eye of Providence, Eros'' Bow, Chandra''s Grace, Eye of the Storm, Barbed Carver,
    Breastplate of Valor.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.41
    Rage:
      total: 0.41
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.44
      efficiency: 0.43
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
      total: 0.39
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 0.64
    The Crusher:
      total: 0.46
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
  - Runeforged Hammer
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  flex_slots:
  - Tekko-Kagi
  - Runeforged Hammer
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
    Blade, Damaru, Titan''s Bane, Berserker''s Shield, Spectral Armor, Shield Splitter,
    Chandra''s Grace, Kinetic Cuirass, Rage, Breastplate of Valor, Eye of Providence,
    Pendulum Blade, Arondight, Eye of the Storm, Shield of the Phoenix, Heartseeker,
    Pharaoh''s Curse, Eros'' Bow.'
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
    Runeforged Hammer:
      total: 0.42
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.23
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
    this god: The Reaper, Jotunn''s Revenge, Amanita Charm, The Crusher, Shield of
    the Phoenix, Chandra''s Grace, Shield Splitter, Hydra''s Lament, Kinetic Cuirass,
    Eye of Providence, Runeforged Hammer, Phoenix Feather, Berserker''s Shield, Tyrfing,
    Spectral Armor, Genji''s Guard, Bloodforge, Lernaean Bow, Spirit Robe, Tekko-Kagi,
    Golden Blade, Avenging Blade, Damaru, Eye of the Storm, Pharaoh''s Curse, Breastplate
    of Valor.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.3
    Shield Splitter:
      total: 0.42
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.32
    Hydra's Lament:
      total: 0.42
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.29
    The Reaper:
      total: 0.47
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.6
    The Crusher:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.34
    Amanita Charm:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  flex_slots:
  - Tekko-Kagi
  - Hydra's Lament
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
    Hydra''s Lament, Tyrfing, Titan''s Bane, Runeforged Hammer, Lernaean Bow, Oath-Sworn
    Spear, Golden Blade, Screeching Gargoyle, Damaru, Berserker''s Shield, Heartseeker,
    Pendulum Blade, Rage, Shield Splitter, Genji''s Guard, Spectral Armor, Kinetic
    Cuirass, Eye of Providence, Eye of the Storm, Void Stone, Chandra''s Grace, Pharaoh''s
    Curse.'
  slot_scores:
    Avenging Blade:
      total: 0.45
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.55
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.53
    Hydra's Lament:
      total: 0.43
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.33
    The Reaper:
      total: 0.46
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.53
    Tekko-Kagi:
      total: 0.44
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.65
    The Crusher:
      total: 0.48
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.55
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
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
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
    Golden Blade, Tyrfing, Damaru, Tekko-Kagi, Spectral Armor, Bloodforge, Lernaean
    Bow, Berserker''s Shield, Kinetic Cuirass, Eye of the Storm, Eye of Providence,
    Rage, Titan''s Bane, Shield Splitter, Phoenix Feather, Genji''s Guard, Barbed
    Carver.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.41
    Hydra's Lament:
      total: 0.43
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.36
    Devourer's Gauntlet:
      total: 0.46
      efficiency: 0.28
      win: 0.57
      pick: 0.54
      fit: 0.5
    Runeforged Hammer:
      total: 0.44
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.37
    The Reaper:
      total: 0.47
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.66
    The Crusher:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.42
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Rage
  - The Reaper
  - Musashi's Dual Swords
  - Damaru
  - The Crusher
  flex_slots:
  - Rage
  - Musashi's Dual Swords
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
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
    Berserker''s Shield, Avenging Blade, Lernaean Bow, Tekko-Kagi, Spectral Armor,
    Damaru, Kinetic Cuirass, Bloodforge, Eye of Providence, Rage, Pharaoh''s Curse,
    Eros'' Bow, Eye of the Storm, Phoenix Feather, Genji''s Guard, Shield Splitter,
    Yogi''s Necklace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.36
    Rage:
      total: 0.4
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.36
    The Reaper:
      total: 0.47
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.6
    Musashi's Dual Swords:
      total: 0.38
      efficiency: 0.3
      win: 0.5
      pick: 0.0
      fit: 0.36
    Damaru:
      total: 0.41
      efficiency: 0.38
      win: 0.5
      pick: 0.0
      fit: 0.36
    The Crusher:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.37
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: burst
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Hydra's Lament
  - Runeforged Hammer
  - The Reaper
  - The Crusher
  flex_slots:
  - Runeforged Hammer
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
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
    god: Jotunn''s Revenge, The Reaper, The Crusher, Chandra''s Grace, Hydra''s Lament,
    Runeforged Hammer, Shield of the Phoenix, Amanita Charm, Avenging Blade, Spectral
    Armor, Tekko-Kagi, Golden Blade, Kinetic Cuirass, Genji''s Guard, Tyrfing, Eye
    of Providence, Bloodforge, Berserker''s Shield, Lernaean Bow, Damaru, Titan''s
    Bane, Eye of the Storm, Phoenix Feather, Shield Splitter, Rage, Breastplate of
    Valor, Yogi''s Necklace.'
  slot_scores:
    Avenging Blade:
      total: 0.41
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.3
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.44
    Hydra's Lament:
      total: 0.43
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.35
    Runeforged Hammer:
      total: 0.43
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.3
    The Reaper:
      total: 0.47
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.61
    The Crusher:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.41
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Reaper
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Amanita Charm, Jotunn''s Revenge, The Crusher, Shield of
    the Phoenix, Chandra''s Grace, Kinetic Cuirass, Eye of Providence, Runeforged
    Hammer, Phoenix Feather, Hydra''s Lament, Spectral Armor, Shield Splitter, Bloodforge,
    Berserker''s Shield, Avenging Blade, Genji''s Guard, Eye of the Storm, Spirit
    Robe, Golden Blade, Tyrfing, Erosion, Lernaean Bow, Damaru, Pharaoh''s Curse,
    Breastplate of Valor.'
  slot_scores:
    Eye of Providence:
      total: 0.43
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.29
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.36
    The Reaper:
      total: 0.47
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.62
    The Crusher:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.33
    Amanita Charm:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.56
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Hydra's Lament
  - Runeforged Hammer
  - The Reaper
  - The Crusher
  flex_slots:
  - Runeforged Hammer
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Resolute Mantle — CC-immunity / cleanse
    swap_item: Resolute Mantle
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
    for this god: Jotunn''s Revenge, The Reaper, The Crusher, Avenging Blade, Runeforged
    Hammer, Chandra''s Grace, Hydra''s Lament, Tekko-Kagi, Amanita Charm, Shield of
    the Phoenix, Titan''s Bane, Oath-Sworn Spear, Golden Blade, Screeching Gargoyle,
    Spectral Armor, Tyrfing, Kinetic Cuirass, Damaru, Bloodforge, Lernaean Bow, Berserker''s
    Shield, Eye of Providence, Void Stone, Eye of the Storm, Heartseeker, Shield Splitter,
    Genji''s Guard.'
  slot_scores:
    Avenging Blade:
      total: 0.46
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.63
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.5
    Hydra's Lament:
      total: 0.43
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.32
    Runeforged Hammer:
      total: 0.43
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.33
    The Reaper:
      total: 0.49
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.74
    The Crusher:
      total: 0.47
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.53
  starter: *id001
  aspect: Aspect of Strife
---
