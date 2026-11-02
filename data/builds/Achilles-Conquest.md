---
type: smite-build
god: Achilles
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prowess
  aspect_pick_rate: 0.14
  aspect_win_rate: 0.57
  slot_order:
  - name: Avenging Blade
    pick_rate: 0.18
    win_rate: 0.53
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.18
      win_rate: 0.51
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.54
  - name: Shifter's Shield
    pick_rate: 0.13
    win_rate: 0.5
    alternates:
    - name: Dagger of Frenzy
      pick_rate: 0.09
      win_rate: 0.5
    - name: Hydra's Lament
      pick_rate: 0.08
      win_rate: 0.52
  - name: Freya's Tears
    pick_rate: 0.12
    win_rate: 0.55
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.53
    - name: Brawler’s Beat Stick
      pick_rate: 0.08
      win_rate: 0.5
  - name: Brawler’s Beat Stick
    pick_rate: 0.08
    win_rate: 0.44
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.48
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.57
  - name: Hide of the Nemean Lion
    pick_rate: 0.06
    win_rate: 0.61
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.57
    - name: Blinking Abyss
      pick_rate: 0.05
      win_rate: 0.61
  - name: Blinking Abyss
    pick_rate: 0.07
    win_rate: 0.42
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.09
      win_rate: 0.57
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.76
  community_starters:
  - name: Sundering Axe
    pick_rate: 0.19
    win_rate: 0.63
  - name: Hunter's Cowl
    pick_rate: 0.15
    win_rate: 0.49
  - name: Bluestone Brooch
    pick_rate: 0.12
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/achilles/
  last_verified: '2026-11-02'
  god_win_rate: 0.514018691588785
  god_matches_won: 220
  god_matches_played: 428
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14397
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Berserker''s Shield, Runeforged Hammer,
    Shield Splitter, Kinetic Cuirass, Hide of the Nemean Lion, Titan''s Bane, Genji''s
    Guard, Hydra''s Lament, Heartseeker, The Crusher, The Reaper, Breastplate of Valor,
    Oni Hunter''s Garb, Wyrmskin Hide, Erosion, Eye of Providence, Draconic Scale,
    Golden Blade, Midgardian Mail, Shield of the Phoenix, Tekko-Kagi, Leviathan''s
    Hide, Arondight, Ancile, Stone of Binding.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.63
      win: 0.52
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.56
    Shield Splitter:
      total: 0.5
      efficiency: 0.54
      win: 0.52
      pick: 0.0
      fit: 0.54
    Runeforged Hammer:
      total: 0.5
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.52
      efficiency: 0.62
      win: 0.52
      pick: 0.0
      fit: 0.46
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
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Genji''s Guard, Hydra''s Lament, Amanita Charm, Breastplate of Valor,
    Berserker''s Shield, Runeforged Hammer, Titan''s Bane, Shield Splitter, Kinetic
    Cuirass, Heartseeker, Oni Hunter''s Garb, The Crusher, Arondight, Shield of the
    Phoenix, The Reaper, Transcendence, Screeching Gargoyle, Midgardian Mail, Yogi''s
    Necklace, Erosion, Leviathan''s Hide, Tekko-Kagi, Wyrmskin Hide, Eye of Providence,
    Draconic Scale, Chandra''s Grace, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.52
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.52
    Transcendence:
      total: 0.45
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.28
    Hydra's Lament:
      total: 0.49
      efficiency: 0.52
      win: 0.52
      pick: 0.11
      fit: 0.49
    Freya's Tears:
      total: 0.49
      efficiency: 0.55
      win: 0.55
      pick: 0.19
      fit: 0.25
    Amanita Charm:
      total: 0.49
      efficiency: 0.62
      win: 0.52
      pick: 0.0
      fit: 0.27
  community_ordered:
  - Hydra's Lament
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield of the Phoenix,
    Berserker''s Shield, Shield Splitter, The Reaper, Runeforged Hammer, Phoenix Feather,
    Genji''s Guard, Yogi''s Necklace, Titan''s Bane, Erosion, Eye of Providence, Draconic
    Scale, Oni Hunter''s Garb, Hydra''s Lament, Breastplate of Valor, Chandra''s Grace,
    Midgardian Mail, Wyrmskin Hide, Heartseeker, Leviathan''s Hide, The Crusher, Stone
    of Binding, Ancile, Glorious Pridwen.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.63
      win: 0.52
      pick: 0.0
      fit: 0.38
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.65
    Shield Splitter:
      total: 0.51
      efficiency: 0.54
      win: 0.52
      pick: 0.0
      fit: 0.58
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.72
    Amanita Charm:
      total: 0.58
      efficiency: 0.62
      win: 0.52
      pick: 0.0
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Heartseeker
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Titan''s Bane, Amanita Charm, Heartseeker, The
    Crusher, Berserker''s Shield, The Reaper, Stone of Binding, Runeforged Hammer,
    Kinetic Cuirass, Screeching Gargoyle, Shield Splitter, Void Stone, Void Shield,
    Genji''s Guard, Tekko-Kagi, Hydra''s Lament, Pendulum Blade, Breastplate of Valor,
    Avatar''s Parashu, Toxic Blade, Oni Hunter''s Garb, Erosion, Midgardian Mail,
    Eye of Providence, Draconic Scale, Wyrmskin Hide, Shield of the Phoenix.'
  slot_scores:
    Avenging Blade:
      total: 0.52
      efficiency: 0.45
      win: 0.53
      pick: 0.18
      fit: 0.78
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.65
    The Crusher:
      total: 0.5
      efficiency: 0.45
      win: 0.52
      pick: 0.0
      fit: 0.71
    Titan's Bane:
      total: 0.52
      efficiency: 0.51
      win: 0.52
      pick: 0.0
      fit: 0.71
    Heartseeker:
      total: 0.5
      efficiency: 0.41
      win: 0.52
      pick: 0.0
      fit: 0.81
    Amanita Charm:
      total: 0.5
      efficiency: 0.62
      win: 0.52
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Avenging Blade
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Toxic Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Tekko-Kagi
  - Amanita Charm
  flex_slots:
  - Toxic Blade
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Jotunn''s Revenge, Golden Blade, Amanita Charm,
    Toxic Blade, Tekko-Kagi, Tyrfing, Silverbranch Bow, Genji''s Guard, Riptalon,
    Kinetic Cuirass, Runeforged Hammer, Pharaoh''s Curse, Lernaean Bow, The Reaper,
    Shield Splitter, Titan''s Bane, Breastplate of Valor, Shogun''s Ofuda, Hydra''s
    Lament, Oni Hunter''s Garb, Dominance, Qin''s Blade, Midgardian Mail, Heartseeker,
    Erosion, The Crusher, Leviathan''s Hide.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.62
    Toxic Blade:
      total: 0.49
      efficiency: 0.46
      win: 0.52
      pick: 0.0
      fit: 0.62
    Berserker's Shield:
      total: 0.54
      efficiency: 0.7
      win: 0.52
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.27
    Tekko-Kagi:
      total: 0.48
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.49
      efficiency: 0.62
      win: 0.52
      pick: 0.0
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Hydra's Lament
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Breastplate of Valor, Hydra''s Lament, Amanita Charm, Shield of the Phoenix, Berserker''s
    Shield, Screeching Gargoyle, Kinetic Cuirass, Arondight, Runeforged Hammer, Chandra''s
    Grace, Shield Splitter, Titan''s Bane, Gladiator''s Shield, Prophetic Cloak, Pendulum
    Blade, Eye of Erebus, Oni Hunter''s Garb, Midgardian Mail, Erosion, Regrowth Striders,
    Eye of Providence, Leviathan''s Hide, Heartseeker, Draconic Scale, The Crusher,
    Damaru.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.52
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.61
      win: 0.52
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.59
    Hydra's Lament:
      total: 0.5
      efficiency: 0.52
      win: 0.52
      pick: 0.11
      fit: 0.55
    Freya's Tears:
      total: 0.53
      efficiency: 0.55
      win: 0.55
      pick: 0.19
      fit: 0.52
    Amanita Charm:
      total: 0.5
      efficiency: 0.62
      win: 0.52
      pick: 0.0
      fit: 0.31
  community_ordered:
  - Hydra's Lament
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Berserker''s Shield,
    Runeforged Hammer, Shield Splitter, Kinetic Cuirass, Titan''s Bane, Genji''s Guard,
    Heartseeker, The Crusher, Hydra''s Lament, The Reaper, Breastplate of Valor, Oni
    Hunter''s Garb, Wyrmskin Hide, Erosion, Eye of Providence, Draconic Scale, Golden
    Blade, Midgardian Mail, Shield of the Phoenix, Tekko-Kagi, Leviathan''s Hide,
    Arondight, Ancile, Hide of the Nemean Lion, Stone of Binding.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.63
      win: 0.52
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.56
    Shield Splitter:
      total: 0.5
      efficiency: 0.54
      win: 0.52
      pick: 0.0
      fit: 0.54
    Runeforged Hammer:
      total: 0.5
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.52
      efficiency: 0.62
      win: 0.52
      pick: 0.0
      fit: 0.46
  starter: *id001
---
