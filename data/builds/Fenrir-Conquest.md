---
type: smite-build
god: Fenrir
mode: Conquest
builds:
- source: community
  aspect: Aspect of Loyalty
  aspect_pick_rate: 0.25
  aspect_win_rate: 0.36
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.38
    win_rate: 0.63
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.44
    - name: Golden Blade
      pick_rate: 0.06
      win_rate: 0.14
  - name: Shifter's Shield
    pick_rate: 0.32
    win_rate: 0.5
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.09
      win_rate: 0.7
    - name: Sanguine Lash
      pick_rate: 0.07
      win_rate: 0.5
  - name: The Reaper
    pick_rate: 0.08
    win_rate: 0.67
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 0.35
    - name: Kinetic Cuirass
      pick_rate: 0.08
      win_rate: 0.67
  - name: Sundering Echo
    pick_rate: 0.08
    win_rate: 0.78
    alternates:
    - name: Titan's Bane
      pick_rate: 0.08
      win_rate: 0.5
    - name: Heartseeker
      pick_rate: 0.06
      win_rate: 0.33
  - name: Glorious Pridwen
    pick_rate: 0.13
    win_rate: 0.67
    alternates:
    - name: Heartseeker
      pick_rate: 0.07
      win_rate: 0.57
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.6
  - name: Magi's Cloak
    pick_rate: 0.07
    win_rate: 0.6
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.2
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.0
  source_url: https://smitebrain.com/gods/fenrir/
  last_verified: '2026-08-01'
  god_win_rate: 0.5087719298245614
  god_matches_won: 58
  god_matches_played: 114
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Runeforged Hammer
  - The Reaper
  - The Crusher
  - Heartseeker
  flex_slots:
  - Runeforged Hammer
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    this god: The Reaper, The Crusher, Hydra''s Lament, Runeforged Hammer, Heartseeker,
    Avatar''s Parashu, Lernaean Bow, Titan''s Bane, Pendulum Blade, Tekko-Kagi, Avenging
    Blade, Damaru, Arondight, Golden Blade, Shield Splitter, Eye of the Storm, Barbed
    Carver, Tyrfing, Genji''s Guard, Bloodforge, Riptalon, Transcendence, Berserker''s
    Shield, Wyrmskin Hide, Breastplate of Valor, Musashi''s Dual Swords, Oni Hunter''s
    Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.7
      efficiency: 0.69
      win: 0.63
      pick: 0.38
      fit: 1.0
    Hydra's Lament:
      total: 0.57
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.71
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.62
    The Reaper:
      total: 0.65
      efficiency: 0.59
      win: 0.67
      pick: 0.08
      fit: 0.91
    The Crusher:
      total: 0.62
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.56
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
  - Runeforged Hammer
  - The Reaper
  - The Crusher
  flex_slots:
  - Runeforged Hammer
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Reaper, The Crusher, Hydra''s Lament, Runeforged Hammer, Genji''s Guard,
    Heartseeker, Pendulum Blade, Avatar''s Parashu, Lernaean Bow, Arondight, Breastplate
    of Valor, Avenging Blade, Damaru, Titan''s Bane, Riptalon, Tekko-Kagi, Berserker''s
    Shield, Golden Blade, Shield of the Phoenix, Oni Hunter''s Garb, Chandra''s Grace,
    Yogi''s Necklace, Freya''s Tears, Kinetic Cuirass, Amanita Charm, Shield Splitter,
    Eye of the Storm.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.22
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.69
      win: 0.63
      pick: 0.38
      fit: 0.78
    Hydra's Lament:
      total: 0.55
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.54
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.32
    The Reaper:
      total: 0.6
      efficiency: 0.59
      win: 0.67
      pick: 0.08
      fit: 0.56
    The Crusher:
      total: 0.57
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Reaper
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Amanita Charm, Runeforged Hammer, Shield of the Phoenix,
    Kinetic Cuirass, The Crusher, Berserker''s Shield, Eye of Providence, Oni Hunter''s
    Garb, Avenging Blade, Hydra''s Lament, Eye of the Storm, Chandra''s Grace, Spectral
    Armor, Shield Splitter, Genji''s Guard, Golden Blade, Phoenix Feather, Riptalon,
    Pharaoh''s Curse, Erosion, Draconic Scale, Yogi''s Necklace, Lernaean Bow, Mantle
    Of Discord, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.69
      win: 0.63
      pick: 0.38
      fit: 0.44
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.66
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.54
    The Reaper:
      total: 0.62
      efficiency: 0.59
      win: 0.67
      pick: 0.08
      fit: 0.7
    The Crusher:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.5
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - The Reaper
  - The Crusher
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Avatar's Parashu
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Reaper, The Crusher, Heartseeker, Avatar''s Parashu, Avenging
    Blade, Titan''s Bane, Tekko-Kagi, Pendulum Blade, Hydra''s Lament, Runeforged
    Hammer, Riptalon, Lernaean Bow, Damaru, Golden Blade, Genji''s Guard, Arondight,
    Oath-Sworn Spear, Berserker''s Shield, Shield Splitter, Eye of the Storm, Barbed
    Carver, Oni Hunter''s Garb, Tyrfing, Yogi''s Necklace, Breastplate of Valor, Screeching
    Gargoyle, Bloodforge.'
  slot_scores:
    Avenging Blade:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.73
    Jotunn's Revenge:
      total: 0.7
      efficiency: 0.69
      win: 0.63
      pick: 0.38
      fit: 1.0
    The Reaper:
      total: 0.65
      efficiency: 0.59
      win: 0.67
      pick: 0.08
      fit: 0.94
    The Crusher:
      total: 0.62
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.56
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 1.0
    Avatar's Parashu:
      total: 0.56
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.94
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Jotunn's Revenge
  - The Reaper
  - Riptalon
  - The Crusher
  flex_slots:
  - Lernaean Bow
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Riptalon, Golden Blade, Lernaean Bow, The Crusher, Berserker''s
    Shield, Tyrfing, Hydra''s Lament, Runeforged Hammer, Tekko-Kagi, Pharaoh''s Curse,
    Genji''s Guard, Avenging Blade, Eros'' Bow, Damaru, Heartseeker, Shogun''s Ofuda,
    Oni Hunter''s Garb, Yogi''s Necklace, Avatar''s Parashu, Breastplate of Valor,
    Kinetic Cuirass, Barbed Carver, Qin''s Blade, Amanita Charm, Arondight, Spectral
    Armor.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.69
    Lernaean Bow:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.58
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.69
      win: 0.63
      pick: 0.38
      fit: 0.37
    The Reaper:
      total: 0.58
      efficiency: 0.59
      win: 0.67
      pick: 0.08
      fit: 0.44
    Riptalon:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.79
    The Crusher:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - The Crusher
  flex_slots:
  - The Crusher
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Hydra''s Lament, The Reaper, Genji''s
    Guard, The Crusher, Breastplate of Valor, Arondight, Pendulum Blade, Shield of
    the Phoenix, Chandra''s Grace, Freya''s Tears, Runeforged Hammer, Screeching Gargoyle,
    Lernaean Bow, Berserker''s Shield, Avenging Blade, Heartseeker, Damaru, Gladiator''s
    Shield, Oni Hunter''s Garb, Avatar''s Parashu, Yogi''s Necklace, Golden Blade,
    Riptalon, Kinetic Cuirass, Amanita Charm, Spectral Armor, Titan''s Bane.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.5
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.69
      win: 0.63
      pick: 0.38
      fit: 0.85
    Hydra's Lament:
      total: 0.58
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.75
    The Reaper:
      total: 0.57
      efficiency: 0.59
      win: 0.67
      pick: 0.08
      fit: 0.35
    The Crusher:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Runeforged Hammer
  - The Reaper
  - The Crusher
  - Heartseeker
  flex_slots:
  - Runeforged Hammer
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, Hydra''s Lament, The Reaper, Runeforged
    Hammer, Heartseeker, Avatar''s Parashu, Lernaean Bow, Titan''s Bane, Pendulum
    Blade, Tekko-Kagi, Avenging Blade, Damaru, Arondight, Golden Blade, Shield Splitter,
    Eye of the Storm, Barbed Carver, Tyrfing, Genji''s Guard, Bloodforge, Riptalon,
    Transcendence, Berserker''s Shield, Wyrmskin Hide, Breastplate of Valor, Musashi''s
    Dual Swords, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.7
      efficiency: 0.69
      win: 0.63
      pick: 0.38
      fit: 1.0
    Hydra's Lament:
      total: 0.57
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.71
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.62
    The Reaper:
      total: 0.65
      efficiency: 0.59
      win: 0.67
      pick: 0.08
      fit: 0.91
    The Crusher:
      total: 0.62
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.56
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
---
