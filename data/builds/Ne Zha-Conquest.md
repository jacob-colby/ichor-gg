---
type: smite-build
god: Ne Zha
mode: Conquest
builds:
- source: community
  aspect: Aspect of Righteous Flame
  aspect_pick_rate: 0.37
  aspect_win_rate: 0.6
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.37
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.6
    - name: Rage
      pick_rate: 0.09
      win_rate: 0.8
  - name: Shifter's Shield
    pick_rate: 0.17
    win_rate: 0.56
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.13
      win_rate: 0.43
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 1.0
  - name: Deathbringer
    pick_rate: 0.21
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.8
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 1.0
  - name: Heartseeker
    pick_rate: 0.14
    win_rate: 0.43
    alternates:
    - name: Titan's Bane
      pick_rate: 0.12
      win_rate: 0.5
    - name: Spirit Robe
      pick_rate: 0.08
      win_rate: 0.75
  - name: Titan's Bane
    pick_rate: 0.15
    win_rate: 0.57
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.09
      win_rate: 0.75
    - name: Kinetic Cuirass
      pick_rate: 0.06
      win_rate: 0.67
  - name: Engraved Guard
    pick_rate: 0.09
    win_rate: 1.0
    alternates:
    - name: Sage's Ring
      pick_rate: 0.06
      win_rate: 0.0
    - name: Void Shard
      pick_rate: 0.06
      win_rate: 0.5
  community_starters:
  - name: Bumba's Cudgel
    pick_rate: 0.17
    win_rate: 0.33
  - name: Bumba's Hammer
    pick_rate: 0.17
    win_rate: 0.89
  - name: Bluestone Pendant
    pick_rate: 0.13
    win_rate: 0.43
  source_url: https://smitebrain.com/gods/ne-zha/
  last_verified: '2026-08-13'
  god_win_rate: 0.5555555555555556
  god_matches_won: 30
  god_matches_played: 54
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-13'
  god_matches_analyzed: 2102
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Rage
  - The Reaper
  - The Crusher
  flex_slots:
  - Rage
  - The Reaper
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, The Crusher, The Reaper, Pendulum Blade, Kinetic
    Cuirass, Runeforged Hammer, Tekko-Kagi, Damaru, Lernaean Bow, Arondight, Golden
    Blade, Avatar''s Parashu, Avenging Blade, Shield Splitter, Riptalon, Dominance,
    Eye of the Storm, Tyrfing, Silverbranch Bow, Freya''s Tears, Berserker''s Shield,
    Shield of the Phoenix, Barbed Carver.'
  slot_scores:
    Genji's Guard:
      total: 0.65
      efficiency: 0.71
      win: 0.8
      pick: 0.16
      fit: 0.22
    Breastplate of Valor:
      total: 0.72
      efficiency: 0.66
      win: 1.0
      pick: 0.12
      fit: 0.22
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.66
      win: 0.5
      pick: 0.37
      fit: 1.0
    Rage:
      total: 0.57
      efficiency: 0.4
      win: 0.8
      pick: 0.09
      fit: 0.44
    The Reaper:
      total: 0.55
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.78
    The Crusher:
      total: 0.61
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.88
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Rage
  - The Crusher
  flex_slots:
  - Rage
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Breastplate of Valor, The Crusher, Kinetic Cuirass, The Reaper, Pendulum
    Blade, Riptalon, Runeforged Hammer, Silverbranch Bow, Freya''s Tears, Tekko-Kagi,
    Berserker''s Shield, Damaru, Lernaean Bow, Arondight, Shield of the Phoenix, Golden
    Blade, Amanita Charm, Screeching Gargoyle, Oni Hunter''s Garb, Chandra''s Grace,
    Avatar''s Parashu, Eye of Providence, Avenging Blade, Shield Splitter.'
  slot_scores:
    Genji's Guard:
      total: 0.65
      efficiency: 0.71
      win: 0.8
      pick: 0.16
      fit: 0.22
    Breastplate of Valor:
      total: 0.72
      efficiency: 0.66
      win: 1.0
      pick: 0.12
      fit: 0.22
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.66
      win: 0.5
      pick: 0.37
      fit: 0.78
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.1
    Rage:
      total: 0.54
      efficiency: 0.4
      win: 0.8
      pick: 0.09
      fit: 0.22
    The Crusher:
      total: 0.58
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Kinetic Cuirass, Amanita Charm, Shield of the
    Phoenix, Berserker''s Shield, The Crusher, The Reaper, Chandra''s Grace, Oni Hunter''s
    Garb, Freya''s Tears, Runeforged Hammer, Riptalon, Eye of the Storm, Shield Splitter,
    Phoenix Feather, Erosion, Spectral Armor, Eye of Providence, Pharaoh''s Curse,
    Draconic Scale, Golden Blade, Leviathan''s Hide, Avenging Blade, Midgardian Mail,
    Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.66
      efficiency: 0.71
      win: 0.8
      pick: 0.16
      fit: 0.27
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.36
    Breastplate of Valor:
      total: 0.73
      efficiency: 0.66
      win: 1.0
      pick: 0.12
      fit: 0.27
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.62
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.77
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.82
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - The Reaper
  - The Crusher
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Breastplate of Valor, The Crusher, The Reaper, Pendulum Blade, Tekko-Kagi,
    Riptalon, Kinetic Cuirass, Silverbranch Bow, Avenging Blade, Avatar''s Parashu,
    Screeching Gargoyle, Runeforged Hammer, Damaru, Lernaean Bow, Berserker''s Shield,
    Golden Blade, Arondight, Toxic Blade, Stone of Binding, Freya''s Tears, Shield
    Splitter, Void Shield, Amanita Charm, Shield of the Phoenix.'
  slot_scores:
    Genji's Guard:
      total: 0.64
      efficiency: 0.71
      win: 0.8
      pick: 0.16
      fit: 0.15
    Breastplate of Valor:
      total: 0.71
      efficiency: 0.66
      win: 1.0
      pick: 0.12
      fit: 0.15
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.66
      win: 0.5
      pick: 0.37
      fit: 1.0
    The Reaper:
      total: 0.56
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.85
    The Crusher:
      total: 0.62
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.95
    Titan's Bane:
      total: 0.56
      efficiency: 0.45
      win: 0.57
      pick: 0.32
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Breastplate of Valor
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Golden Blade
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Riptalon, Silverbranch Bow, Golden Blade, The
    Crusher, Berserker''s Shield, Kinetic Cuirass, Tyrfing, Lernaean Bow, Tekko-Kagi,
    Pharaoh''s Curse, Dominance, Toxic Blade, The Reaper, Runeforged Hammer, Shogun''s
    Ofuda, Damaru, Freya''s Tears, Eros'' Bow, Amanita Charm, Oni Hunter''s Garb,
    Qin''s Blade, Eye of Providence, Shield of the Phoenix, Yogi''s Necklace.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.64
    Genji's Guard:
      total: 0.63
      efficiency: 0.71
      win: 0.8
      pick: 0.16
      fit: 0.1
    Breastplate of Valor:
      total: 0.7
      efficiency: 0.66
      win: 1.0
      pick: 0.12
      fit: 0.1
    Riptalon:
      total: 0.56
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.74
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.64
    The Crusher:
      total: 0.54
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - The Crusher
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, The Crusher,
    Freya''s Tears, Kinetic Cuirass, Shield of the Phoenix, Pendulum Blade, Arondight,
    Screeching Gargoyle, Chandra''s Grace, Berserker''s Shield, Gladiator''s Shield,
    The Reaper, Runeforged Hammer, Riptalon, Damaru, Lernaean Bow, Prophetic Cloak,
    Amanita Charm, Silverbranch Bow, Oni Hunter''s Garb, Eye of Providence, Regrowth
    Striders, Golden Blade, Tekko-Kagi.'
  slot_scores:
    Genji's Guard:
      total: 0.69
      efficiency: 0.71
      win: 0.8
      pick: 0.16
      fit: 0.5
    Breastplate of Valor:
      total: 0.76
      efficiency: 0.66
      win: 1.0
      pick: 0.12
      fit: 0.5
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.66
      win: 0.5
      pick: 0.37
      fit: 0.85
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.67
      pick: 0.13
      fit: 0.1
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.5
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  flex_slots:
  - Pendulum Blade
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, The Reaper, Pendulum Blade, Runeforged Hammer,
    Tekko-Kagi, Damaru, Lernaean Bow, Arondight, Breastplate of Valor, Golden Blade,
    Avatar''s Parashu, Avenging Blade, Shield Splitter, Riptalon, Dominance, Eye of
    the Storm, Tyrfing, Silverbranch Bow, Freya''s Tears, Berserker''s Shield, Shield
    of the Phoenix, Barbed Carver, Kinetic Cuirass.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.66
      win: 0.5
      pick: 0.37
      fit: 1.0
    Hydra's Lament:
      total: 0.52
      efficiency: 0.58
      win: 0.43
      pick: 0.18
      fit: 0.77
    The Reaper:
      total: 0.55
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.78
    Pendulum Blade:
      total: 0.55
      efficiency: 0.41
      win: 0.57
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.61
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.88
    Heartseeker:
      total: 0.49
      efficiency: 0.45
      win: 0.43
      pick: 0.23
      fit: 0.88
  starter: *id001
---
