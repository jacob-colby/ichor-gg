---
type: smite-build
god: Fenrir
mode: Conquest
builds:
- source: community
  aspect: Aspect of Loyalty
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.57
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.35
    win_rate: 0.48
    alternates:
    - name: The Reaper
      pick_rate: 0.15
      win_rate: 0.55
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.9
  - name: Shifter's Shield
    pick_rate: 0.24
    win_rate: 0.53
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.1
      win_rate: 0.43
    - name: Sanguine Lash
      pick_rate: 0.08
      win_rate: 0.5
  - name: Genji's Guard
    pick_rate: 0.07
    win_rate: 0.6
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.08
      win_rate: 0.5
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.09
    win_rate: 0.67
    alternates:
    - name: Heartseeker
      pick_rate: 0.07
      win_rate: 0.4
    - name: Avenging Blade
      pick_rate: 0.07
      win_rate: 0.2
  - name: Heartseeker
    pick_rate: 0.14
    win_rate: 0.44
    alternates:
    - name: Sundering Echo
      pick_rate: 0.08
      win_rate: 0.8
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 1.0
  - name: Mantle Of Discord
    pick_rate: 0.1
    win_rate: 0.75
    alternates:
    - name: Medal of Defense
      pick_rate: 0.1
      win_rate: 0.75
    - name: Hunter's Bow
      pick_rate: 0.07
      win_rate: 0.67
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.29
    win_rate: 0.48
  - name: Bumba's Cudgel
    pick_rate: 0.15
    win_rate: 0.55
  - name: Death's Embrace
    pick_rate: 0.1
    win_rate: 0.71
  source_url: https://smitebrain.com/gods/fenrir/
  last_verified: '2026-08-14'
  god_win_rate: 0.5694444444444444
  god_matches_won: 41
  god_matches_played: 72
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - The Reaper
  - Pendulum Blade
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Titan's Bane
  - Pendulum Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, The Reaper, Titan''s Bane, Pendulum Blade, Tekko-Kagi,
    Runeforged Hammer, Damaru, Lernaean Bow, Genji''s Guard, Avatar''s Parashu, Golden
    Blade, Shield Splitter, Arondight, Riptalon, Dominance, Eye of the Storm, Tyrfing,
    Hydra''s Lament, Silverbranch Bow, Breastplate of Valor, Berserker''s Shield,
    Barbed Carver, Deathbringer, Transcendence, Bloodforge, Musashi''s Dual Swords,
    Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.66
      win: 0.48
      pick: 0.35
      fit: 1.0
    Hide of the Nemean Lion:
      total: 0.63
      efficiency: 0.5
      win: 1.0
      pick: 0.13
      fit: 0.0
    The Reaper:
      total: 0.57
      efficiency: 0.52
      win: 0.55
      pick: 0.15
      fit: 0.91
    Pendulum Blade:
      total: 0.55
      efficiency: 0.41
      win: 0.57
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.63
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 1.0
    Titan's Bane:
      total: 0.55
      efficiency: 0.45
      win: 0.57
      pick: 0.0
      fit: 0.91
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Freya's Tears
  - Mantle Of Discord
  - The Crusher
  flex_slots:
  - Freya's Tears
  - Mantle Of Discord
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Crusher, Genji''s Guard, Breastplate of Valor, Pendulum Blade, The Reaper,
    Riptalon, Titan''s Bane, Runeforged Hammer, Silverbranch Bow, Tekko-Kagi, Berserker''s
    Shield, Damaru, Lernaean Bow, Arondight, Shield of the Phoenix, Hydra''s Lament,
    Kinetic Cuirass, Golden Blade, Amanita Charm, Screeching Gargoyle, Oni Hunter''s
    Garb, Chandra''s Grace, Avatar''s Parashu, Eye of Providence, Shield Splitter,
    Avenging Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.6
      pick: 0.11
      fit: 0.22
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.66
      win: 0.48
      pick: 0.35
      fit: 0.78
    Hide of the Nemean Lion:
      total: 0.63
      efficiency: 0.5
      win: 1.0
      pick: 0.13
      fit: 0.0
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.67
      pick: 0.15
      fit: 0.22
    Mantle Of Discord:
      total: 0.54
      efficiency: 0.53
      win: 0.75
      pick: 0.31
      fit: 0.0
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
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hide of the Nemean Lion
  - Freya's Tears
  - Mantle Of Discord
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Berserker''s
    Shield, Genji''s Guard, The Crusher, The Reaper, Oni Hunter''s Garb, Runeforged
    Hammer, Eye of the Storm, Riptalon, Chandra''s Grace, Shield Splitter, Erosion,
    Phoenix Feather, Breastplate of Valor, Eye of Providence, Spectral Armor, Pharaoh''s
    Curse, Draconic Scale, Golden Blade, Leviathan''s Hide, Midgardian Mail, Shogun''s
    Ofuda, Hydra''s Lament, Avenging Blade.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.73
    Hide of the Nemean Lion:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.13
      fit: 0.39
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.67
      pick: 0.15
      fit: 0.38
    Mantle Of Discord:
      total: 0.59
      efficiency: 0.53
      win: 0.75
      pick: 0.31
      fit: 0.34
    Amanita Charm:
      total: 0.61
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Hide of the Nemean Lion
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, The Reaper, Titan''s Bane, Tekko-Kagi, Pendulum Blade,
    Riptalon, Silverbranch Bow, Avatar''s Parashu, Genji''s Guard, Runeforged Hammer,
    Damaru, Lernaean Bow, Screeching Gargoyle, Breastplate of Valor, Toxic Blade,
    Berserker''s Shield, Golden Blade, Shield Splitter, Stone of Binding, Dominance,
    Eye of the Storm, Oath-Sworn Spear, Tyrfing, Arondight, Kinetic Cuirass, Hydra''s
    Lament, Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.66
      win: 0.48
      pick: 0.35
      fit: 1.0
    Hide of the Nemean Lion:
      total: 0.63
      efficiency: 0.5
      win: 1.0
      pick: 0.13
      fit: 0.0
    The Reaper:
      total: 0.58
      efficiency: 0.52
      win: 0.55
      pick: 0.15
      fit: 0.94
    Tekko-Kagi:
      total: 0.56
      efficiency: 0.45
      win: 0.57
      pick: 0.0
      fit: 0.94
    The Crusher:
      total: 0.63
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 1.0
    Titan's Bane:
      total: 0.56
      efficiency: 0.45
      win: 0.57
      pick: 0.0
      fit: 0.94
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Hide of the Nemean Lion
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - The Crusher
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Silverbranch Bow, Golden Blade, The Crusher, Berserker''s
    Shield, Tyrfing, Lernaean Bow, Genji''s Guard, Tekko-Kagi, Toxic Blade, Dominance,
    Pharaoh''s Curse, The Reaper, Breastplate of Valor, Runeforged Hammer, Shogun''s
    Ofuda, Damaru, Eros'' Bow, Qin''s Blade, Kinetic Cuirass, Amanita Charm, Oni Hunter''s
    Garb, Eye of Providence, Dagger of Frenzy, Titan''s Bane, Hydra''s Lament.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.69
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.31
    Hide of the Nemean Lion:
      total: 0.63
      efficiency: 0.5
      win: 1.0
      pick: 0.13
      fit: 0.0
    Riptalon:
      total: 0.57
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.69
    The Crusher:
      total: 0.54
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Freya's Tears
  - The Crusher
  flex_slots:
  - Breastplate of Valor
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    The Crusher, Shield of the Phoenix, Pendulum Blade, Arondight, Screeching Gargoyle,
    Chandra''s Grace, Hydra''s Lament, Berserker''s Shield, Gladiator''s Shield, Runeforged
    Hammer, The Reaper, Riptalon, Damaru, Lernaean Bow, Prophetic Cloak, Kinetic Cuirass,
    Amanita Charm, Silverbranch Bow, Oni Hunter''s Garb, Eye of Providence, Regrowth
    Striders, Golden Blade, Titan''s Bane, Tekko-Kagi.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.6
      pick: 0.11
      fit: 0.5
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.66
      win: 0.48
      pick: 0.35
      fit: 0.85
    Hide of the Nemean Lion:
      total: 0.63
      efficiency: 0.5
      win: 1.0
      pick: 0.13
      fit: 0.0
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.67
      pick: 0.15
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
    Parashu, Golden Blade, Genji''s Guard, Avenging Blade, Shield Splitter, Arondight,
    Riptalon, Dominance, Eye of the Storm, Tyrfing, Silverbranch Bow, Breastplate
    of Valor, Berserker''s Shield, Barbed Carver, Deathbringer, Transcendence, Bloodforge,
    Musashi''s Dual Swords.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.66
      win: 0.48
      pick: 0.35
      fit: 1.0
    Hydra's Lament:
      total: 0.51
      efficiency: 0.58
      win: 0.43
      pick: 0.14
      fit: 0.71
    The Reaper:
      total: 0.57
      efficiency: 0.52
      win: 0.55
      pick: 0.15
      fit: 0.91
    The Crusher:
      total: 0.63
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.52
      efficiency: 0.45
      win: 0.44
      pick: 0.3
      fit: 1.0
    Titan's Bane:
      total: 0.55
      efficiency: 0.45
      win: 0.57
      pick: 0.0
      fit: 0.91
  starter: *id001
---
