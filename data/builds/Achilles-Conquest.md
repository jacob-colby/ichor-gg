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
  last_verified: '2026-11-03'
  god_win_rate: 0.514018691588785
  god_matches_won: 220
  god_matches_played: 428
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14484
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
  - Berserker's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    this god: Jotunn''s Revenge, Amanita Charm, Shield Splitter, Runeforged Hammer,
    Berserker''s Shield, Kinetic Cuirass, Titan''s Bane, Hydra''s Lament, Genji''s
    Guard, The Crusher, Heartseeker, The Reaper, Oni Hunter''s Garb, Wyrmskin Hide,
    Erosion, Breastplate of Valor, Eye of Providence, Golden Blade, Midgardian Mail,
    Draconic Scale, Tekko-Kagi, Shield of the Phoenix, Arondight, Leviathan''s Hide,
    Tyrfing, Avatar''s Parashu, Ancile.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.67
      win: 0.52
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.52
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.56
    Shield Splitter:
      total: 0.52
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.54
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
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
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Berserker's Shield
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
    Revenge, Genji''s Guard, Hydra''s Lament, Amanita Charm, Berserker''s Shield,
    Runeforged Hammer, Shield Splitter, Breastplate of Valor, Titan''s Bane, Kinetic
    Cuirass, Heartseeker, Oni Hunter''s Garb, The Crusher, Arondight, The Reaper,
    Transcendence, Shield of the Phoenix, Midgardian Mail, Screeching Gargoyle, Tekko-Kagi,
    Yogi''s Necklace, Erosion, Leviathan''s Hide, Eye of Providence, Wyrmskin Hide,
    Tyrfing, Draconic Scale, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.69
      win: 0.52
      pick: 0.0
      fit: 0.25
    Berserker's Shield:
      total: 0.49
      efficiency: 0.67
      win: 0.52
      pick: 0.0
      fit: 0.19
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.67
      win: 0.52
      pick: 0.0
      fit: 0.52
    Hydra's Lament:
      total: 0.51
      efficiency: 0.56
      win: 0.52
      pick: 0.11
      fit: 0.49
    Freya's Tears:
      total: 0.5
      efficiency: 0.58
      win: 0.55
      pick: 0.19
      fit: 0.25
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
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
  - Shield of the Phoenix
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
    this god: Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield Splitter,
    Berserker''s Shield, Shield of the Phoenix, The Reaper, Runeforged Hammer, Genji''s
    Guard, Phoenix Feather, Yogi''s Necklace, Titan''s Bane, Erosion, Eye of Providence,
    Hydra''s Lament, Oni Hunter''s Garb, Draconic Scale, Breastplate of Valor, Midgardian
    Mail, The Crusher, Wyrmskin Hide, Chandra''s Grace, Leviathan''s Hide, Heartseeker,
    Stone of Binding, Magi''s Cloak, Ancile.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.67
      win: 0.52
      pick: 0.0
      fit: 0.38
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.67
      win: 0.52
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.65
    Shield Splitter:
      total: 0.53
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.58
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.72
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
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
  - The Crusher
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Titan''s Bane, Amanita Charm, The Crusher, Heartseeker,
    Berserker''s Shield, The Reaper, Shield Splitter, Runeforged Hammer, Stone of
    Binding, Kinetic Cuirass, Genji''s Guard, Screeching Gargoyle, Void Stone, Void
    Shield, Tekko-Kagi, Hydra''s Lament, Avatar''s Parashu, Pendulum Blade, Breastplate
    of Valor, Oni Hunter''s Garb, Toxic Blade, Midgardian Mail, Erosion, Eye of Providence,
    Wyrmskin Hide, Arondight, Draconic Scale.'
  slot_scores:
    Avenging Blade:
      total: 0.54
      efficiency: 0.49
      win: 0.53
      pick: 0.18
      fit: 0.78
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.52
      pick: 0.0
      fit: 0.65
    The Crusher:
      total: 0.51
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.71
    Titan's Bane:
      total: 0.53
      efficiency: 0.54
      win: 0.52
      pick: 0.0
      fit: 0.71
    Heartseeker:
      total: 0.51
      efficiency: 0.43
      win: 0.52
      pick: 0.0
      fit: 0.81
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
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
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Tekko-Kagi
  - Amanita Charm
  flex_slots:
  - Tekko-Kagi
  - Tyrfing
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Golden Blade, Jotunn''s Revenge, Amanita Charm,
    Tekko-Kagi, Tyrfing, Toxic Blade, Silverbranch Bow, Genji''s Guard, Kinetic Cuirass,
    Runeforged Hammer, Shield Splitter, Riptalon, Lernaean Bow, The Reaper, Pharaoh''s
    Curse, Titan''s Bane, Hydra''s Lament, Breastplate of Valor, Shogun''s Ofuda,
    Oni Hunter''s Garb, Dominance, The Crusher, Midgardian Mail, Qin''s Blade, Erosion,
    Heartseeker, Eye of Providence.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.62
    Berserker's Shield:
      total: 0.56
      efficiency: 0.74
      win: 0.52
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.67
      win: 0.52
      pick: 0.0
      fit: 0.27
    Tyrfing:
      total: 0.5
      efficiency: 0.5
      win: 0.52
      pick: 0.0
      fit: 0.6
    Tekko-Kagi:
      total: 0.5
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
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
  - Transcendence
  - Hydra's Lament
  - Freya's Tears
  flex_slots:
  - Hydra's Lament
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Breastplate of Valor, Hydra''s Lament, Amanita Charm, Shield of the Phoenix, Berserker''s
    Shield, Screeching Gargoyle, Kinetic Cuirass, Arondight, Runeforged Hammer, Shield
    Splitter, Titan''s Bane, Gladiator''s Shield, Chandra''s Grace, Oni Hunter''s
    Garb, Eye of Erebus, Pendulum Blade, Prophetic Cloak, Midgardian Mail, Erosion,
    Damaru, The Crusher, Regrowth Striders, Eye of Providence, Leviathan''s Hide,
    Draconic Scale, Heartseeker.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.52
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.63
      win: 0.52
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.52
      pick: 0.0
      fit: 0.59
    Transcendence:
      total: 0.43
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.1
    Hydra's Lament:
      total: 0.52
      efficiency: 0.56
      win: 0.52
      pick: 0.11
      fit: 0.55
    Freya's Tears:
      total: 0.54
      efficiency: 0.58
      win: 0.55
      pick: 0.19
      fit: 0.52
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
  - Berserker's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Shield Splitter, Runeforged
    Hammer, Berserker''s Shield, Kinetic Cuirass, Titan''s Bane, Genji''s Guard, The
    Crusher, Hydra''s Lament, Heartseeker, The Reaper, Oni Hunter''s Garb, Wyrmskin
    Hide, Erosion, Breastplate of Valor, Eye of Providence, Golden Blade, Midgardian
    Mail, Draconic Scale, Tekko-Kagi, Shield of the Phoenix, Arondight, Leviathan''s
    Hide, Tyrfing, Avatar''s Parashu, Ancile.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.67
      win: 0.52
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.52
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.56
    Shield Splitter:
      total: 0.52
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.54
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.46
  starter: *id001
---
