---
type: smite-build
god: Ravana
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rakshasa King
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.46
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.38
    win_rate: 0.44
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.2
      win_rate: 0.47
    - name: Barbed Carver
      pick_rate: 0.06
      win_rate: 0.42
  - name: Barbed Carver
    pick_rate: 0.14
    win_rate: 0.5
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.09
      win_rate: 0.48
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.51
  - name: The Reaper
    pick_rate: 0.12
    win_rate: 0.54
    alternates:
    - name: Barbed Carver
      pick_rate: 0.08
      win_rate: 0.35
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.49
  - name: Heartseeker
    pick_rate: 0.22
    win_rate: 0.47
    alternates:
    - name: Genji's Guard
      pick_rate: 0.05
      win_rate: 0.37
    - name: Titan's Bane
      pick_rate: 0.05
      win_rate: 0.41
  - name: Titan's Bane
    pick_rate: 0.07
    win_rate: 0.59
    alternates:
    - name: Heartseeker
      pick_rate: 0.1
      win_rate: 0.55
    - name: Blinking Abyss
      pick_rate: 0.05
      win_rate: 0.52
  - name: Avatar's Parashu
    pick_rate: 0.06
    win_rate: 0.53
    alternates:
    - name: Skeggox
      pick_rate: 0.05
      win_rate: 0.21
    - name: Axe
      pick_rate: 0.05
      win_rate: 0.61
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.3
    win_rate: 0.5
  - name: Bumba's Cudgel
    pick_rate: 0.19
    win_rate: 0.39
  - name: Bluestone Brooch
    pick_rate: 0.11
    win_rate: 0.54
  source_url: https://smitebrain.com/gods/ravana/
  last_verified: '2026-08-30'
  god_win_rate: 0.47810858143607704
  god_matches_won: 546
  god_matches_played: 1142
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-30'
  god_matches_analyzed: 5563
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - Heartseeker
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Runeforged Hammer, Kinetic Cuirass, Freya''s Tears, Shield
    Splitter, Eye of the Storm, Hydra''s Lament, Breastplate of Valor, Berserker''s
    Shield, Avenging Blade, Shield of the Phoenix, The Crusher, Erosion, Eye of Providence,
    Draconic Scale, Daybreak Gavel, Pendulum Blade, Arondight, Midgardian Mail, Golden
    Blade, Screeching Gargoyle, Stone of Binding, Hide of the Nemean Lion, Genji''s
    Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.44
      pick: 0.38
      fit: 0.58
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.49
      pick: 0.0
      fit: 0.52
    Runeforged Hammer:
      total: 0.5
      efficiency: 0.57
      win: 0.49
      pick: 0.0
      fit: 0.55
    Heartseeker:
      total: 0.49
      efficiency: 0.47
      win: 0.47
      pick: 0.37
      fit: 0.65
    Titan's Bane:
      total: 0.52
      efficiency: 0.47
      win: 0.59
      pick: 0.15
      fit: 0.55
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.42
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Breastplate of Valor, Hydra''s Lament, Runeforged Hammer, Freya''s Tears,
    Kinetic Cuirass, Shield Splitter, Eye of the Storm, Berserker''s Shield, Avenging
    Blade, The Crusher, Shield of the Phoenix, Transcendence, Daybreak Gavel, Arondight,
    Screeching Gargoyle, Erosion, Genji''s Guard, Eye of Providence, Oni Hunter''s
    Garb, Stone of Binding, Draconic Scale, Pendulum Blade, Midgardian Mail, Hide
    of the Nemean Lion.'
  slot_scores:
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.44
      pick: 0.38
      fit: 0.52
    Transcendence:
      total: 0.45
      efficiency: 0.53
      win: 0.49
      pick: 0.0
      fit: 0.28
    Heartseeker:
      total: 0.49
      efficiency: 0.47
      win: 0.47
      pick: 0.37
      fit: 0.62
    Titan's Bane:
      total: 0.5
      efficiency: 0.47
      win: 0.59
      pick: 0.15
      fit: 0.44
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Amanita Charm, Breastplate of Valor, Freya''s Tears, Runeforged Hammer, Kinetic
    Cuirass, Hydra''s Lament, Berserker''s Shield, Shield of the Phoenix, Shield Splitter,
    The Crusher, Eye of the Storm, Pendulum Blade, Avenging Blade, Screeching Gargoyle,
    Daybreak Gavel, Arondight, Erosion, Eye of Providence, Draconic Scale, Stone of
    Binding, Midgardian Mail, Genji''s Guard, Hide of the Nemean Lion, Leviathan''s
    Hide.'
  slot_scores:
    Breastplate of Valor:
      total: 0.48
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.44
      pick: 0.38
      fit: 0.56
    Transcendence:
      total: 0.43
      efficiency: 0.53
      win: 0.49
      pick: 0.0
      fit: 0.16
    Heartseeker:
      total: 0.48
      efficiency: 0.47
      win: 0.47
      pick: 0.37
      fit: 0.6
    Titan's Bane:
      total: 0.51
      efficiency: 0.47
      win: 0.59
      pick: 0.15
      fit: 0.5
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.29
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - The Reaper
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Freya''s Tears,
    Runeforged Hammer, Shield Splitter, Breastplate of Valor, Eye of the Storm, Berserker''s
    Shield, Erosion, Hydra''s Lament, Yogi''s Necklace, Eye of Providence, Draconic
    Scale, Phoenix Feather, Avenging Blade, Chandra''s Grace, Glorious Pridwen, Stone
    of Binding, Midgardian Mail, Daybreak Gavel, The Crusher, Hide of the Nemean Lion,
    Magi''s Cloak, Genji''s Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.44
      pick: 0.38
      fit: 0.49
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.49
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.49
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.53
      efficiency: 0.5
      win: 0.54
      pick: 0.19
      fit: 0.68
    Titan's Bane:
      total: 0.51
      efficiency: 0.47
      win: 0.59
      pick: 0.15
      fit: 0.48
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.81
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Avenging Blade
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Avenging Blade, Amanita Charm, Screeching Gargoyle, Runeforged Hammer,
    Stone of Binding, The Crusher, Kinetic Cuirass, Void Shield, Freya''s Tears, Breastplate
    of Valor, Void Stone, Hydra''s Lament, Shield Splitter, Pendulum Blade, Eye of
    the Storm, Berserker''s Shield, Shield of the Phoenix, Daybreak Gavel, Tekko-Kagi,
    Erosion, Eye of Providence, Draconic Scale, Arondight, Genji''s Guard.'
  slot_scores:
    Avenging Blade:
      total: 0.51
      efficiency: 0.49
      win: 0.49
      pick: 0.0
      fit: 0.75
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.44
      pick: 0.38
      fit: 0.67
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.49
      pick: 0.0
      fit: 0.21
    The Reaper:
      total: 0.51
      efficiency: 0.5
      win: 0.54
      pick: 0.19
      fit: 0.57
    Heartseeker:
      total: 0.51
      efficiency: 0.47
      win: 0.47
      pick: 0.37
      fit: 0.77
    Titan's Bane:
      total: 0.54
      efficiency: 0.47
      win: 0.59
      pick: 0.15
      fit: 0.67
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - The Reaper
  - Riptalon
  - Titan's Bane
  flex_slots:
  - Titan's Bane
  - Riptalon
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Golden Blade, Amanita Charm, Riptalon, Tyrfing,
    Silverbranch Bow, Kinetic Cuirass, Breastplate of Valor, Toxic Blade, Freya''s
    Tears, Runeforged Hammer, Lernaean Bow, Pharaoh''s Curse, Tekko-Kagi, Hydra''s
    Lament, Shogun''s Ofuda, Shield Splitter, Eye of the Storm, Shield of the Phoenix,
    Daybreak Gavel, Avenging Blade, Dominance, Erosion, Eye of Providence, Screeching
    Gargoyle, Genji''s Guard.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.52
      win: 0.49
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.49
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.44
      pick: 0.38
      fit: 0.31
    The Reaper:
      total: 0.49
      efficiency: 0.55
      win: 0.54
      pick: 0.19
      fit: 0.3
    Riptalon:
      total: 0.48
      efficiency: 0.51
      win: 0.49
      pick: 0.0
      fit: 0.55
    Titan's Bane:
      total: 0.49
      efficiency: 0.47
      win: 0.59
      pick: 0.15
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Hydra's Lament
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Freya''s Tears,
    Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Kinetic Cuirass, Screeching
    Gargoyle, Runeforged Hammer, Genji''s Guard, Berserker''s Shield, Arondight, Gladiator''s
    Shield, Eye of Erebus, Pendulum Blade, Shield Splitter, Prophetic Cloak, Chandra''s
    Grace, Eye of the Storm, Daybreak Gavel, Erosion, Eye of Providence, Avenging
    Blade, Draconic Scale, Midgardian Mail, Stone of Binding, The Crusher.'
  slot_scores:
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.44
      pick: 0.38
      fit: 0.59
    Hydra's Lament:
      total: 0.49
      efficiency: 0.54
      win: 0.48
      pick: 0.12
      fit: 0.55
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.49
      pick: 0.0
      fit: 0.52
    Titan's Bane:
      total: 0.49
      efficiency: 0.47
      win: 0.59
      pick: 0.15
      fit: 0.34
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.31
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
    Hydra''s Lament, Berserker''s Shield, Avenging Blade, Shield of the Phoenix, The
    Crusher, Erosion, Eye of Providence, Draconic Scale, Daybreak Gavel, Pendulum
    Blade, Arondight, Midgardian Mail, Golden Blade, Screeching Gargoyle, Stone of
    Binding, Hide of the Nemean Lion.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.44
      pick: 0.38
      fit: 0.58
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.49
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.49
      efficiency: 0.55
      win: 0.49
      pick: 0.0
      fit: 0.5
    Runeforged Hammer:
      total: 0.5
      efficiency: 0.57
      win: 0.49
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.49
      efficiency: 0.61
      win: 0.49
      pick: 0.0
      fit: 0.36
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.42
  starter: *id001
---
