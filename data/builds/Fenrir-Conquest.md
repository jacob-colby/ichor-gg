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
  - Pendulum Blade
  - Titan's Bane
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
    this god: The Crusher, The Reaper, Pendulum Blade, Titan''s Bane, Tekko-Kagi,
    Runeforged Hammer, Damaru, Genji''s Guard, Lernaean Bow, Avatar''s Parashu, Golden
    Blade, Transcendence, Arondight, Shield Splitter, Eye of the Storm, Tyrfing, Riptalon,
    Dominance, Hydra''s Lament, Silverbranch Bow, Breastplate of Valor, Deathbringer,
    Barbed Carver, Berserker''s Shield, Musashi''s Dual Swords, Bloodforge, Avenging
    Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.64
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
      efficiency: 0.64
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
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Freya's Tears
  - The Crusher
  flex_slots:
  - Freya's Tears
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: The
    Crusher, Genji''s Guard, Breastplate of Valor, Runeforged Hammer, The Reaper,
    Damaru, Transcendence, Pendulum Blade, Lernaean Bow, Hydra''s Lament, Arondight,
    Oni Hunter''s Garb, Berserker''s Shield, Golden Blade, Titan''s Bane, Tekko-Kagi,
    Dominance, Kinetic Cuirass, Shield Splitter, Amanita Charm, Shield of the Phoenix,
    Eye of the Storm, Tyrfing, Eye of Providence, Yogi''s Necklace, Avenging Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.6
      pick: 0.11
      fit: 0.24
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.48
      pick: 0.35
      fit: 0.71
    Hide of the Nemean Lion:
      total: 0.63
      efficiency: 0.5
      win: 1.0
      pick: 0.13
      fit: 0.0
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.67
      pick: 0.15
      fit: 0.14
    The Crusher:
      total: 0.57
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 0.57
  starter: *id001
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
    god: The Crusher, Genji''s Guard, The Reaper, Pendulum Blade, Breastplate of Valor,
    Runeforged Hammer, Titan''s Bane, Tekko-Kagi, Riptalon, Arondight, Damaru, Silverbranch
    Bow, Shield of the Phoenix, Berserker''s Shield, Lernaean Bow, Kinetic Cuirass,
    Amanita Charm, Screeching Gargoyle, Golden Blade, Chandra''s Grace, Hydra''s Lament,
    Eye of Providence, Transcendence, Oni Hunter''s Garb, Avatar''s Parashu, Avenging
    Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.6
      pick: 0.11
      fit: 0.22
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
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
      total: 0.53
      efficiency: 0.52
      win: 0.75
      pick: 0.31
      fit: 0.0
    The Crusher:
      total: 0.58
      efficiency: 0.64
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
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, The Crusher,
    Genji''s Guard, Berserker''s Shield, The Reaper, Runeforged Hammer, Oni Hunter''s
    Garb, Eye of the Storm, Chandra''s Grace, Erosion, Shield Splitter, Phoenix Feather,
    Eye of Providence, Spectral Armor, Draconic Scale, Riptalon, Breastplate of Valor,
    Golden Blade, Pharaoh''s Curse, Leviathan''s Hide, Midgardian Mail, Ancile, Hydra''s
    Lament, Avenging Blade.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.56
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
      efficiency: 0.52
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
    Damaru, Toxic Blade, Lernaean Bow, Screeching Gargoyle, Golden Blade, Transcendence,
    Breastplate of Valor, Berserker''s Shield, Shield Splitter, Eye of the Storm,
    Stone of Binding, Tyrfing, Oath-Sworn Spear, Arondight, Kinetic Cuirass, Hydra''s
    Lament, Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.64
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
      efficiency: 0.44
      win: 0.57
      pick: 0.0
      fit: 0.94
    The Crusher:
      total: 0.63
      efficiency: 0.64
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
  - Tyrfing
  - Hide of the Nemean Lion
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Silverbranch Bow
  - Tyrfing
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, The Crusher, Golden Blade, Silverbranch Bow, Tyrfing, Berserker''s
    Shield, Genji''s Guard, Lernaean Bow, Toxic Blade, Tekko-Kagi, The Reaper, Pharaoh''s
    Curse, Dominance, Runeforged Hammer, Breastplate of Valor, Damaru, Shogun''s Ofuda,
    Kinetic Cuirass, Amanita Charm, Qin''s Blade, Eye of Providence, Oni Hunter''s
    Garb, Eros'' Bow, Transcendence, Hydra''s Lament, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.69
    Tyrfing:
      total: 0.54
      efficiency: 0.46
      win: 0.57
      pick: 0.0
      fit: 0.79
    Hide of the Nemean Lion:
      total: 0.63
      efficiency: 0.5
      win: 1.0
      pick: 0.13
      fit: 0.0
    Riptalon:
      total: 0.56
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.69
    The Crusher:
      total: 0.55
      efficiency: 0.64
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
    Chandra''s Grace, Hydra''s Lament, Gladiator''s Shield, The Reaper, Runeforged
    Hammer, Berserker''s Shield, Prophetic Cloak, Kinetic Cuirass, Damaru, Amanita
    Charm, Riptalon, Eye of Providence, Oni Hunter''s Garb, Regrowth Striders, Lernaean
    Bow, Silverbranch Bow, Titan''s Bane, Golden Blade, Tekko-Kagi.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.69
      win: 0.6
      pick: 0.11
      fit: 0.5
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.64
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
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, The Reaper, Hydra''s Lament, Pendulum Blade,
    Titan''s Bane, Tekko-Kagi, Runeforged Hammer, Damaru, Lernaean Bow, Avatar''s
    Parashu, Golden Blade, Transcendence, Avenging Blade, Arondight, Shield Splitter,
    Genji''s Guard, Eye of the Storm, Tyrfing, Riptalon, Dominance, Silverbranch Bow,
    Breastplate of Valor, Deathbringer, Barbed Carver, Berserker''s Shield, Musashi''s
    Dual Swords, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.64
      win: 0.48
      pick: 0.35
      fit: 1.0
    Transcendence:
      total: 0.52
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.52
    Hydra's Lament:
      total: 0.5
      efficiency: 0.56
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
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.51
      efficiency: 0.41
      win: 0.44
      pick: 0.3
      fit: 1.0
  starter: *id001
---
