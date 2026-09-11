---
type: smite-build
god: Ravana
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rakshasa King
  aspect_pick_rate: 0.04
  aspect_win_rate: 0.27
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.41
    win_rate: 0.49
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.42
    - name: Daybreak Gavel
      pick_rate: 0.11
      win_rate: 0.59
  - name: Shifter's Shield
    pick_rate: 0.14
    win_rate: 0.57
    alternates:
    - name: Barbed Carver
      pick_rate: 0.13
      win_rate: 0.47
    - name: The Crusher
      pick_rate: 0.13
      win_rate: 0.49
  - name: The Reaper
    pick_rate: 0.13
    win_rate: 0.46
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.49
    - name: Barbed Carver
      pick_rate: 0.1
      win_rate: 0.56
  - name: Heartseeker
    pick_rate: 0.22
    win_rate: 0.54
    alternates:
    - name: Titan's Bane
      pick_rate: 0.06
      win_rate: 0.52
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.67
  - name: Titan's Bane
    pick_rate: 0.06
    win_rate: 0.55
    alternates:
    - name: Heartseeker
      pick_rate: 0.09
      win_rate: 0.55
    - name: Avatar's Parashu
      pick_rate: 0.06
      win_rate: 0.74
  - name: Lucerne Hammer
    pick_rate: 0.07
    win_rate: 0.29
    alternates:
    - name: Skeggox
      pick_rate: 0.06
      win_rate: 0.62
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.8
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.31
    win_rate: 0.56
  - name: Bumba's Cudgel
    pick_rate: 0.2
    win_rate: 0.36
  - name: Bluestone Brooch
    pick_rate: 0.1
    win_rate: 0.59
  source_url: https://smitebrain.com/gods/ravana/
  last_verified: '2026-09-11'
  god_win_rate: 0.5
  god_matches_won: 186
  god_matches_played: 372
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-11'
  god_matches_analyzed: 3080
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - Freya's Tears
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Avatar''s Parashu, Amanita Charm, Runeforged Hammer,
    Kinetic Cuirass, Shield Splitter, Eye of the Storm, Genji''s Guard, Breastplate
    of Valor, Hydra''s Lament, Daybreak Gavel, Berserker''s Shield, Avenging Blade,
    Titan''s Bane, Shield of the Phoenix, Erosion, Eye of Providence, Draconic Scale,
    Pendulum Blade, Arondight, Midgardian Mail, Golden Blade, Screeching Gargoyle,
    Stone of Binding, Hide of the Nemean Lion.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.49
      pick: 0.41
      fit: 0.58
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.52
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.08
      fit: 0.36
    Avatar's Parashu:
      total: 0.57
      efficiency: 0.45
      win: 0.74
      pick: 0.13
      fit: 0.45
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Avatar's Parashu
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Heartseeker
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Freya''s
    Tears, Amanita Charm, Genji''s Guard, Breastplate of Valor, Hydra''s Lament, Runeforged
    Hammer, Kinetic Cuirass, Daybreak Gavel, Shield Splitter, Eye of the Storm, Berserker''s
    Shield, Titan''s Bane, Avenging Blade, Shield of the Phoenix, Transcendence, Arondight,
    Screeching Gargoyle, Erosion, Eye of Providence, Oni Hunter''s Garb, Stone of
    Binding, Draconic Scale, Pendulum Blade, Midgardian Mail, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.49
      pick: 0.41
      fit: 0.52
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.67
      pick: 0.08
      fit: 0.25
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.54
      pick: 0.37
      fit: 0.62
    Avatar's Parashu:
      total: 0.55
      efficiency: 0.45
      win: 0.74
      pick: 0.13
      fit: 0.34
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.27
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Heartseeker
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Freya''s Tears, Avatar''s Parashu, Amanita Charm, Genji''s Guard, Breastplate
    of Valor, Runeforged Hammer, Kinetic Cuirass, Hydra''s Lament, Daybreak Gavel,
    Titan''s Bane, Berserker''s Shield, Shield of the Phoenix, Shield Splitter, Eye
    of the Storm, Pendulum Blade, Avenging Blade, Screeching Gargoyle, Arondight,
    Erosion, Eye of Providence, Draconic Scale, Stone of Binding, Midgardian Mail,
    Hide of the Nemean Lion, Leviathan''s Hide.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.49
      pick: 0.41
      fit: 0.56
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.16
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.08
      fit: 0.32
    Heartseeker:
      total: 0.51
      efficiency: 0.47
      win: 0.54
      pick: 0.37
      fit: 0.6
    Avatar's Parashu:
      total: 0.56
      efficiency: 0.45
      win: 0.74
      pick: 0.13
      fit: 0.4
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.29
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Shield of the Phoenix, Kinetic Cuirass,
    Runeforged Hammer, Shield Splitter, Genji''s Guard, Breastplate of Valor, Eye
    of the Storm, Berserker''s Shield, Daybreak Gavel, Erosion, Yogi''s Necklace,
    Eye of Providence, Hydra''s Lament, Draconic Scale, Phoenix Feather, Avenging
    Blade, Chandra''s Grace, Titan''s Bane, Glorious Pridwen, Stone of Binding, Midgardian
    Mail, Hide of the Nemean Lion, Magi''s Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.49
      pick: 0.41
      fit: 0.49
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.61
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.76
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.08
      fit: 0.42
    Avatar's Parashu:
      total: 0.55
      efficiency: 0.45
      win: 0.74
      pick: 0.13
      fit: 0.38
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.81
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Freya's Tears
  - Heartseeker
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Avenging Blade
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Avatar''s Parashu, Freya''s Tears, Avenging Blade, Amanita Charm,
    Titan''s Bane, Screeching Gargoyle, Runeforged Hammer, Stone of Binding, Kinetic
    Cuirass, Void Shield, Genji''s Guard, Breastplate of Valor, Void Stone, Daybreak
    Gavel, Hydra''s Lament, Shield Splitter, Pendulum Blade, Eye of the Storm, Berserker''s
    Shield, Shield of the Phoenix, Tekko-Kagi, Erosion, Eye of Providence, Draconic
    Scale, Arondight.'
  slot_scores:
    Avenging Blade:
      total: 0.53
      efficiency: 0.49
      win: 0.55
      pick: 0.0
      fit: 0.75
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.49
      pick: 0.41
      fit: 0.67
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.67
      pick: 0.08
      fit: 0.28
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.54
      pick: 0.37
      fit: 0.77
    Avatar's Parashu:
      total: 0.58
      efficiency: 0.45
      win: 0.74
      pick: 0.13
      fit: 0.57
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.33
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Heartseeker
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Riptalon
  - Avatar's Parashu
  flex_slots:
  - Golden Blade
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Freya''s Tears, Berserker''s Shield, Golden Blade, Amanita Charm, Riptalon,
    Tyrfing, Silverbranch Bow, Genji''s Guard, Kinetic Cuirass, Breastplate of Valor,
    Toxic Blade, Daybreak Gavel, Runeforged Hammer, Lernaean Bow, Pharaoh''s Curse,
    Tekko-Kagi, Shogun''s Ofuda, Hydra''s Lament, Shield Splitter, Eye of the Storm,
    Shield of the Phoenix, Avenging Blade, Dominance, Erosion, Eye of Providence,
    Screeching Gargoyle.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.49
      pick: 0.41
      fit: 0.31
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.67
      pick: 0.08
      fit: 0.22
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.55
    Avatar's Parashu:
      total: 0.53
      efficiency: 0.45
      win: 0.74
      pick: 0.13
      fit: 0.23
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Avatar's Parashu
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Genji''s Guard, Breastplate
    of Valor, Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Kinetic Cuirass,
    Screeching Gargoyle, Daybreak Gavel, Runeforged Hammer, Berserker''s Shield, Arondight,
    Gladiator''s Shield, Eye of Erebus, Pendulum Blade, Shield Splitter, Prophetic
    Cloak, Chandra''s Grace, Eye of the Storm, Erosion, Eye of Providence, Avenging
    Blade, Titan''s Bane, Draconic Scale, Midgardian Mail, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.49
      pick: 0.41
      fit: 0.59
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.08
      fit: 0.52
    Avatar's Parashu:
      total: 0.53
      efficiency: 0.45
      win: 0.74
      pick: 0.13
      fit: 0.24
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.31
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Runeforged Hammer
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Runeforged Hammer, Kinetic Cuirass, Freya''s
    Tears, Shield Splitter, Eye of the Storm, Genji''s Guard, Breastplate of Valor,
    Hydra''s Lament, Berserker''s Shield, Avenging Blade, Shield of the Phoenix, Titan''s
    Bane, Erosion, Eye of Providence, Draconic Scale, Daybreak Gavel, Pendulum Blade,
    Arondight, Midgardian Mail, Golden Blade, Screeching Gargoyle, Stone of Binding,
    Hide of the Nemean Lion, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.49
      pick: 0.41
      fit: 0.58
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.51
      efficiency: 0.55
      win: 0.55
      pick: 0.0
      fit: 0.5
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.08
      fit: 0.36
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  starter: *id001
---
