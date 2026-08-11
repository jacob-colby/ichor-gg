---
type: smite-build
god: Fenrir
mode: Conquest
builds:
- source: community
  aspect: Aspect of Loyalty
  aspect_pick_rate: 0.2
  aspect_win_rate: 0.51
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.35
    win_rate: 0.54
    alternates:
    - name: Golden Blade
      pick_rate: 0.11
      win_rate: 0.57
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.53
  - name: Shifter's Shield
    pick_rate: 0.34
    win_rate: 0.6
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.08
      win_rate: 0.64
    - name: Hydra's Lament
      pick_rate: 0.07
      win_rate: 0.5
  - name: Berserker's Shield
    pick_rate: 0.1
    win_rate: 0.52
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 0.49
    - name: Kinetic Cuirass
      pick_rate: 0.07
      win_rate: 0.67
  - name: Heartseeker
    pick_rate: 0.09
    win_rate: 0.6
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.06
      win_rate: 0.61
    - name: Sundering Echo
      pick_rate: 0.05
      win_rate: 0.61
  - name: Glorious Pridwen
    pick_rate: 0.07
    win_rate: 0.61
    alternates:
    - name: Titan's Bane
      pick_rate: 0.05
      win_rate: 0.5
    - name: Barbed Carver
      pick_rate: 0.05
      win_rate: 0.6
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.38
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.04
      win_rate: 0.27
    - name: Olmec Blue
      pick_rate: 0.03
      win_rate: 0.78
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.24
    win_rate: 0.55
  - name: Bumba's Cudgel
    pick_rate: 0.15
    win_rate: 0.62
  - name: Death's Embrace
    pick_rate: 0.13
    win_rate: 0.66
  source_url: https://smitebrain.com/gods/fenrir/
  last_verified: '2026-08-10'
  god_win_rate: 0.5478260869565217
  god_matches_won: 252
  god_matches_played: 460
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-10'
  god_matches_analyzed: 17490
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  flex_slots:
  - Hydra's Lament
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, The Reaper, Hydra''s Lament, Kinetic Cuirass, Golden Blade,
    Titan''s Bane, Pendulum Blade, Tekko-Kagi, Barbed Carver, Runeforged Hammer, Damaru,
    Lernaean Bow, Avatar''s Parashu, Avenging Blade, Genji''s Guard, Shield Splitter,
    Arondight, Dominance, Eye of the Storm, Riptalon, Tyrfing, Silverbranch Bow, Breastplate
    of Valor, Transcendence, Musashi''s Dual Swords, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.66
      win: 0.54
      pick: 0.35
      fit: 1.0
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.67
      pick: 0.11
      fit: 0.1
    Hydra's Lament:
      total: 0.54
      efficiency: 0.58
      win: 0.5
      pick: 0.1
      fit: 0.71
    The Reaper:
      total: 0.54
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.91
    The Crusher:
      total: 0.6
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.58
      efficiency: 0.45
      win: 0.6
      pick: 0.15
      fit: 1.0
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - The Crusher
  - Heartseeker
  flex_slots:
  - Hydra's Lament
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Crusher, Kinetic Cuirass, Hydra''s Lament, Genji''s Guard, The Reaper,
    Breastplate of Valor, Pendulum Blade, Golden Blade, Titan''s Bane, Riptalon, Runeforged
    Hammer, Tekko-Kagi, Silverbranch Bow, Freya''s Tears, Damaru, Lernaean Bow, Arondight,
    Shield of the Phoenix, Amanita Charm, Screeching Gargoyle, Oni Hunter''s Garb,
    Avatar''s Parashu, Avenging Blade, Chandra''s Grace, Eye of Providence, Shield
    Splitter.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.22
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.66
      win: 0.54
      pick: 0.35
      fit: 0.78
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.67
      pick: 0.11
      fit: 0.1
    Hydra's Lament:
      total: 0.51
      efficiency: 0.58
      win: 0.5
      pick: 0.1
      fit: 0.54
    The Crusher:
      total: 0.54
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.66
    Heartseeker:
      total: 0.53
      efficiency: 0.45
      win: 0.6
      pick: 0.15
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Glorious Pridwen — physical protection
    swap_item: Glorious Pridwen
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Shield of the Phoenix, Shogun''s Ofuda,
    The Crusher, Golden Blade, The Reaper, Genji''s Guard, Oni Hunter''s Garb, Runeforged
    Hammer, Eye of the Storm, Shield Splitter, Riptalon, Chandra''s Grace, Erosion,
    Phoenix Feather, Hydra''s Lament, Freya''s Tears, Breastplate of Valor, Eye of
    Providence, Spectral Armor, Draconic Scale, Pharaoh''s Curse, Avenging Blade,
    Leviathan''s Hide, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.52
      pick: 0.16
      fit: 0.39
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.66
      win: 0.54
      pick: 0.35
      fit: 0.44
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.59
      win: 0.67
      pick: 0.11
      fit: 0.66
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.73
    Shifter's Shield:
      total: 0.56
      efficiency: 0.52
      win: 0.6
      pick: 0.46
      fit: 0.56
    Amanita Charm:
      total: 0.57
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Titan's Bane
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, The Reaper, Titan''s Bane, Kinetic Cuirass, Tekko-Kagi,
    Pendulum Blade, Riptalon, Silverbranch Bow, Hydra''s Lament, Avenging Blade, Avatar''s
    Parashu, Golden Blade, Runeforged Hammer, Genji''s Guard, Damaru, Lernaean Bow,
    Screeching Gargoyle, Toxic Blade, Breastplate of Valor, Shield Splitter, Stone
    of Binding, Dominance, Eye of the Storm, Oath-Sworn Spear, Tyrfing, Arondight.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.66
      win: 0.54
      pick: 0.35
      fit: 1.0
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.67
      pick: 0.11
      fit: 0.1
    The Reaper:
      total: 0.55
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.94
    The Crusher:
      total: 0.6
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.58
      efficiency: 0.45
      win: 0.6
      pick: 0.15
      fit: 1.0
    Titan's Bane:
      total: 0.53
      efficiency: 0.45
      win: 0.5
      pick: 0.11
      fit: 0.94
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Berserker's Shield
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, Riptalon, Kinetic Cuirass, Silverbranch Bow, The Crusher,
    Shogun''s Ofuda, Tyrfing, Lernaean Bow, Tekko-Kagi, Hydra''s Lament, Genji''s
    Guard, Toxic Blade, Dominance, The Reaper, Pharaoh''s Curse, Breastplate of Valor,
    Runeforged Hammer, Damaru, Eros'' Bow, Qin''s Blade, Amanita Charm, Oni Hunter''s
    Garb, Eye of Providence, Freya''s Tears, Dagger of Frenzy, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.54
      win: 0.57
      pick: 0.11
      fit: 0.69
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.52
      pick: 0.16
      fit: 0.31
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.54
      pick: 0.35
      fit: 0.37
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.67
      pick: 0.11
      fit: 0.1
    Riptalon:
      total: 0.54
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - The Crusher
  flex_slots:
  - Kinetic Cuirass
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Hydra''s Lament, Breastplate
    of Valor, Kinetic Cuirass, The Crusher, Freya''s Tears, Shield of the Phoenix,
    Pendulum Blade, Arondight, Screeching Gargoyle, Chandra''s Grace, Golden Blade,
    The Reaper, Gladiator''s Shield, Runeforged Hammer, Damaru, Lernaean Bow, Riptalon,
    Prophetic Cloak, Amanita Charm, Silverbranch Bow, Oni Hunter''s Garb, Titan''s
    Bane, Eye of Providence, Regrowth Striders, Tekko-Kagi.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.5
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.66
      win: 0.54
      pick: 0.35
      fit: 0.85
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.67
      pick: 0.11
      fit: 0.1
    Hydra's Lament:
      total: 0.55
      efficiency: 0.58
      win: 0.5
      pick: 0.1
      fit: 0.75
    The Crusher:
      total: 0.51
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, The Reaper, Hydra''s Lament, Titan''s Bane,
    Pendulum Blade, Tekko-Kagi, Runeforged Hammer, Damaru, Lernaean Bow, Avatar''s
    Parashu, Golden Blade, Avenging Blade, Genji''s Guard, Shield Splitter, Arondight,
    Dominance, Eye of the Storm, Riptalon, Tyrfing, Silverbranch Bow, Breastplate
    of Valor, Barbed Carver, Transcendence, Musashi''s Dual Swords, Bloodforge, Kinetic
    Cuirass.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.66
      win: 0.54
      pick: 0.35
      fit: 1.0
    Hydra's Lament:
      total: 0.54
      efficiency: 0.58
      win: 0.5
      pick: 0.1
      fit: 0.71
    The Reaper:
      total: 0.54
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.91
    The Crusher:
      total: 0.6
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.58
      efficiency: 0.45
      win: 0.6
      pick: 0.15
      fit: 1.0
    Titan's Bane:
      total: 0.52
      efficiency: 0.45
      win: 0.5
      pick: 0.11
      fit: 0.91
  starter: *id001
---
