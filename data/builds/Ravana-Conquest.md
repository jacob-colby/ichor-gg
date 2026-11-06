---
type: smite-build
god: Ravana
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rakshasa King
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.5
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.4
    win_rate: 0.45
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.32
      win_rate: 0.66
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.33
  - name: Sanguine Lash
    pick_rate: 0.17
    win_rate: 0.39
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.09
      win_rate: 0.77
    - name: Berserker's Shield
      pick_rate: 0.08
      win_rate: 0.55
  - name: Barbed Carver
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.58
    - name: The Crusher
      pick_rate: 0.09
      win_rate: 0.5
  - name: Heartseeker
    pick_rate: 0.25
    win_rate: 0.61
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.54
    - name: Kinetic Cuirass
      pick_rate: 0.06
      win_rate: 0.25
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 0.42
    alternates:
    - name: Titan's Bane
      pick_rate: 0.08
      win_rate: 0.78
    - name: Sundering Echo
      pick_rate: 0.06
      win_rate: 0.29
  - name: Blinking Abyss
    pick_rate: 0.06
    win_rate: 0.6
    alternates:
    - name: Mote of Chaos
      pick_rate: 0.06
      win_rate: 1.0
    - name: Sundering Echo
      pick_rate: 0.06
      win_rate: 0.6
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.24
    win_rate: 0.48
  - name: Bumba's Hammer
    pick_rate: 0.22
    win_rate: 0.71
  - name: Leather Cowl
    pick_rate: 0.21
    win_rate: 0.45
  source_url: https://smitebrain.com/gods/ravana/
  last_verified: '2026-11-06'
  god_win_rate: 0.5289855072463768
  god_matches_won: 73
  god_matches_played: 138
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - Titan's Bane
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Heartseeker
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
    this god: Hydra''s Lament, Amanita Charm, Kinetic Cuirass, Genji''s Guard, Shield
    Splitter, Runeforged Hammer, Berserker''s Shield, Shield of the Phoenix, Breastplate
    of Valor, Oni Hunter''s Garb, Draconic Scale, The Reaper, Avenging Blade, Arondight,
    Erosion, Eye of Providence, Wyrmskin Hide, Midgardian Mail, Tyrfing, Screeching
    Gargoyle, Leviathan''s Hide, Hide of the Nemean Lion, The Crusher, Golden Blade,
    Gladiator''s Shield, Shifter''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.65
      win: 0.66
      pick: 0.32
      fit: 0.58
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.58
      pick: 0.14
      fit: 0.52
    Hydra's Lament:
      total: 0.62
      efficiency: 0.55
      win: 0.77
      pick: 0.12
      fit: 0.49
    Titan's Bane:
      total: 0.61
      efficiency: 0.48
      win: 0.78
      pick: 0.17
      fit: 0.55
    Heartseeker:
      total: 0.55
      efficiency: 0.45
      win: 0.61
      pick: 0.42
      fit: 0.65
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - Titan's Bane
  - Heartseeker
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Titan's Bane
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Hydra''s
    Lament, Genji''s Guard, Amanita Charm, Kinetic Cuirass, Breastplate of Valor,
    Shield Splitter, Runeforged Hammer, Berserker''s Shield, Oni Hunter''s Garb, Shield
    of the Phoenix, The Reaper, Arondight, Avenging Blade, Tyrfing, Screeching Gargoyle,
    Draconic Scale, Yogi''s Necklace, Midgardian Mail, Erosion, Leviathan''s Hide,
    Eye of Providence, Hide of the Nemean Lion, Transcendence, The Crusher, Wyrmskin
    Hide, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.58
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.65
      win: 0.66
      pick: 0.32
      fit: 0.52
    Transcendence:
      total: 0.48
      efficiency: 0.5
      win: 0.58
      pick: 0.0
      fit: 0.28
    Hydra's Lament:
      total: 0.62
      efficiency: 0.55
      win: 0.77
      pick: 0.12
      fit: 0.49
    Titan's Bane:
      total: 0.59
      efficiency: 0.48
      win: 0.78
      pick: 0.17
      fit: 0.44
    Heartseeker:
      total: 0.55
      efficiency: 0.45
      win: 0.61
      pick: 0.42
      fit: 0.62
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Titan's Bane
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Titan's Bane
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Hydra''s Lament, Genji''s Guard, Amanita Charm, Kinetic Cuirass, Breastplate
    of Valor, Shield of the Phoenix, Berserker''s Shield, Shield Splitter, Runeforged
    Hammer, The Reaper, Oni Hunter''s Garb, Screeching Gargoyle, Arondight, Draconic
    Scale, Midgardian Mail, The Crusher, Avenging Blade, Erosion, Pendulum Blade,
    Leviathan''s Hide, Eye of Providence, Tyrfing, Avatar''s Parashu, Gladiator''s
    Shield, Hide of the Nemean Lion, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.58
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.65
      win: 0.66
      pick: 0.32
      fit: 0.56
    Transcendence:
      total: 0.46
      efficiency: 0.5
      win: 0.58
      pick: 0.0
      fit: 0.16
    Hydra's Lament:
      total: 0.61
      efficiency: 0.55
      win: 0.77
      pick: 0.12
      fit: 0.42
    Titan's Bane:
      total: 0.6
      efficiency: 0.48
      win: 0.78
      pick: 0.17
      fit: 0.5
    Heartseeker:
      total: 0.54
      efficiency: 0.45
      win: 0.61
      pick: 0.42
      fit: 0.6
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Titan's Bane
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hydra's Lament
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Kinetic Cuirass,
    Genji''s Guard, Shield Splitter, The Reaper, Phoenix Feather, Berserker''s Shield,
    Yogi''s Necklace, Runeforged Hammer, Draconic Scale, Breastplate of Valor, Chandra''s
    Grace, Oni Hunter''s Garb, Erosion, Eye of Providence, Midgardian Mail, Regrowth
    Striders, Leviathan''s Hide, Avenging Blade, Glorious Pridwen, Wyrmskin Hide,
    Hide of the Nemean Lion, The Crusher, Shifter''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.65
      win: 0.66
      pick: 0.32
      fit: 0.49
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.58
      pick: 0.14
      fit: 0.61
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.76
    Hydra's Lament:
      total: 0.61
      efficiency: 0.55
      win: 0.77
      pick: 0.12
      fit: 0.43
    Titan's Bane:
      total: 0.6
      efficiency: 0.48
      win: 0.78
      pick: 0.17
      fit: 0.48
    Amanita Charm:
      total: 0.62
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.81
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Titan's Bane
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Transcendence
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Hydra''s Lament, Amanita Charm, Kinetic Cuirass, Avenging Blade,
    Genji''s Guard, Screeching Gargoyle, The Reaper, Shield Splitter, Stone of Binding,
    Void Stone, Runeforged Hammer, Berserker''s Shield, Void Shield, Breastplate of
    Valor, The Crusher, Shield of the Phoenix, Avatar''s Parashu, Oni Hunter''s Garb,
    Pendulum Blade, Draconic Scale, Tekko-Kagi, Arondight, Midgardian Mail, Erosion,
    Tyrfing, Eye of Providence.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.65
      win: 0.66
      pick: 0.32
      fit: 0.67
    Transcendence:
      total: 0.47
      efficiency: 0.5
      win: 0.58
      pick: 0.0
      fit: 0.21
    Hydra's Lament:
      total: 0.61
      efficiency: 0.55
      win: 0.77
      pick: 0.12
      fit: 0.4
    Titan's Bane:
      total: 0.63
      efficiency: 0.48
      win: 0.78
      pick: 0.17
      fit: 0.67
    Heartseeker:
      total: 0.57
      efficiency: 0.45
      win: 0.61
      pick: 0.42
      fit: 0.77
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.33
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Titan's Bane
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Titan's Bane
  flex_slots:
  - Tyrfing
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Hydra''s Lament, Berserker''s Shield, Amanita Charm, Kinetic Cuirass,
    Tyrfing, Genji''s Guard, Golden Blade, Toxic Blade, The Reaper, Breastplate of
    Valor, Silverbranch Bow, Shield Splitter, Runeforged Hammer, Shield of the Phoenix,
    Tekko-Kagi, Riptalon, Oni Hunter''s Garb, Shogun''s Ofuda, Lernaean Bow, Pharaoh''s
    Curse, Dominance, Draconic Scale, Midgardian Mail, Screeching Gargoyle, Qin''s
    Blade, Erosion, The Crusher.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.11
      fit: 0.4
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.66
      pick: 0.32
      fit: 0.31
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.58
    Hydra's Lament:
      total: 0.59
      efficiency: 0.55
      win: 0.77
      pick: 0.12
      fit: 0.29
    Titan's Bane:
      total: 0.58
      efficiency: 0.48
      win: 0.78
      pick: 0.17
      fit: 0.33
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Genji''s Guard, Breastplate
    of Valor, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Screeching Gargoyle,
    Berserker''s Shield, Arondight, Gladiator''s Shield, Shield Splitter, Chandra''s
    Grace, Runeforged Hammer, Oni Hunter''s Garb, Eye of Erebus, Prophetic Cloak,
    Draconic Scale, Damaru, Midgardian Mail, Regrowth Striders, Erosion, Pendulum
    Blade, Eye of Providence, Leviathan''s Hide, Hide of the Nemean Lion, The Crusher,
    Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.58
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.65
      win: 0.66
      pick: 0.32
      fit: 0.59
    Hydra's Lament:
      total: 0.63
      efficiency: 0.55
      win: 0.77
      pick: 0.12
      fit: 0.55
    Titan's Bane:
      total: 0.58
      efficiency: 0.48
      win: 0.78
      pick: 0.17
      fit: 0.34
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.31
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Berserker's Shield
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Genji''s Guard, Shield
    Splitter, Berserker''s Shield, Runeforged Hammer, Hydra''s Lament, Shield of the
    Phoenix, The Crusher, Breastplate of Valor, Oni Hunter''s Garb, Draconic Scale,
    The Reaper, Avenging Blade, Arondight, Erosion, Eye of Providence, Wyrmskin Hide,
    Midgardian Mail, Tyrfing, Shifter''s Shield, Screeching Gargoyle, Leviathan''s
    Hide, Hide of the Nemean Lion, Golden Blade, Gladiator''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.58
      pick: 0.0
      fit: 0.24
    Berserker's Shield:
      total: 0.53
      efficiency: 0.66
      win: 0.55
      pick: 0.11
      fit: 0.31
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.65
      win: 0.66
      pick: 0.32
      fit: 0.58
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.58
      pick: 0.14
      fit: 0.52
    Shield Splitter:
      total: 0.54
      efficiency: 0.58
      win: 0.58
      pick: 0.0
      fit: 0.5
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  starter: *id001
---
