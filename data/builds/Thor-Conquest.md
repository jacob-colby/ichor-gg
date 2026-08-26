---
type: smite-build
god: Thor
mode: Conquest
builds:
- source: community
  aspect: Aspect of Thunderstruck
  aspect_pick_rate: 0.27
  aspect_win_rate: 0.63
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.51
    win_rate: 0.65
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.25
      win_rate: 0.56
    - name: Runeforged Hammer
      pick_rate: 0.04
      win_rate: 0.75
  - name: Hydra's Lament
    pick_rate: 0.3
    win_rate: 0.57
    alternates:
    - name: Barbed Carver
      pick_rate: 0.12
      win_rate: 0.58
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.5
  - name: The Reaper
    pick_rate: 0.13
    win_rate: 0.62
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.73
    - name: Barbed Carver
      pick_rate: 0.11
      win_rate: 0.36
  - name: Heartseeker
    pick_rate: 0.23
    win_rate: 0.59
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.5
    - name: Barbed Carver
      pick_rate: 0.07
      win_rate: 0.86
  - name: Titan's Bane
    pick_rate: 0.13
    win_rate: 0.45
    alternates:
    - name: Heartseeker
      pick_rate: 0.07
      win_rate: 0.83
    - name: Lucerne Hammer
      pick_rate: 0.07
      win_rate: 0.67
  - name: Skeggox
    pick_rate: 0.08
    win_rate: 0.75
    alternates:
    - name: Engraved Guard
      pick_rate: 0.08
      win_rate: 0.25
    - name: Draconic Scale
      pick_rate: 0.06
      win_rate: 0.67
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.35
    win_rate: 0.74
  - name: Bumba's Cudgel
    pick_rate: 0.26
    win_rate: 0.54
  - name: Bluestone Brooch
    pick_rate: 0.15
    win_rate: 0.73
  source_url: https://smitebrain.com/gods/thor/
  last_verified: '2026-08-26'
  god_win_rate: 0.6
  god_matches_won: 60
  god_matches_played: 100
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-26'
  god_matches_analyzed: 888
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Runeforged Hammer
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Amanita Charm, Kinetic Cuirass, Shield Splitter,
    Eye of the Storm, Freya''s Tears, Avenging Blade, Berserker''s Shield, Breastplate
    of Valor, The Crusher, Erosion, Eye of Providence, Golden Blade, Shield of the
    Phoenix, Daybreak Gavel, Avatar''s Parashu, Midgardian Mail, Stone of Binding,
    Tyrfing, Pendulum Blade, Transcendence, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.73
      pick: 0.17
      fit: 0.18
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.65
      pick: 0.51
      fit: 0.55
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.3
    Runeforged Hammer:
      total: 0.62
      efficiency: 0.57
      win: 0.75
      pick: 0.04
      fit: 0.58
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.59
      pick: 0.38
      fit: 0.71
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.45
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
  - Runeforged Hammer
  - Heartseeker
  flex_slots:
  - Hydra's Lament
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Runeforged
    Hammer, Amanita Charm, Breastplate of Valor, Freya''s Tears, Kinetic Cuirass,
    Shield Splitter, Eye of the Storm, Berserker''s Shield, Avenging Blade, The Crusher,
    Shield of the Phoenix, Transcendence, Arondight, Daybreak Gavel, Screeching Gargoyle,
    Erosion, Eye of Providence, Oni Hunter''s Garb, Pendulum Blade, Stone of Binding,
    Midgardian Mail, Tyrfing.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.73
      pick: 0.17
      fit: 0.26
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.65
      pick: 0.51
      fit: 0.53
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.29
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.57
      pick: 0.41
      fit: 0.49
    Runeforged Hammer:
      total: 0.6
      efficiency: 0.57
      win: 0.75
      pick: 0.04
      fit: 0.42
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.59
      pick: 0.38
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Runeforged Hammer
  - Heartseeker
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Runeforged Hammer, Amanita Charm, Breastplate of Valor, Freya''s Tears, Kinetic
    Cuirass, Shield Splitter, The Crusher, Berserker''s Shield, Shield of the Phoenix,
    Eye of the Storm, Pendulum Blade, Screeching Gargoyle, Avenging Blade, Daybreak
    Gavel, Arondight, Erosion, Avatar''s Parashu, Eye of Providence, Stone of Binding,
    Midgardian Mail, Magi''s Cloak, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.73
      pick: 0.17
      fit: 0.24
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.65
      pick: 0.51
      fit: 0.56
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.16
    Runeforged Hammer:
      total: 0.59
      efficiency: 0.57
      win: 0.75
      pick: 0.04
      fit: 0.37
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.59
      pick: 0.38
      fit: 0.6
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Runeforged Hammer
  - The Reaper
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - The Reaper
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Runeforged Hammer, Kinetic Cuirass, Shield of the Phoenix,
    Shield Splitter, Eye of the Storm, Freya''s Tears, Berserker''s Shield, Erosion,
    Eye of Providence, Breastplate of Valor, Yogi''s Necklace, Avenging Blade, Phoenix
    Feather, Stone of Binding, Midgardian Mail, Chandra''s Grace, The Crusher, Daybreak
    Gavel, Hide of the Nemean Lion, Magi''s Cloak, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.73
      pick: 0.17
      fit: 0.21
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.65
      pick: 0.51
      fit: 0.45
    Runeforged Hammer:
      total: 0.62
      efficiency: 0.57
      win: 0.75
      pick: 0.04
      fit: 0.55
    The Reaper:
      total: 0.57
      efficiency: 0.5
      win: 0.62
      pick: 0.2
      fit: 0.71
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.67
      pick: 0.18
      fit: 0.55
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Runeforged Hammer
  - Heartseeker
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
    for this god: Runeforged Hammer, Avenging Blade, Amanita Charm, The Crusher, Stone
    of Binding, Kinetic Cuirass, Void Shield, Screeching Gargoyle, Shield Splitter,
    Void Stone, Avatar''s Parashu, Eye of the Storm, Freya''s Tears, Breastplate of
    Valor, Pendulum Blade, Berserker''s Shield, Tekko-Kagi, Erosion, Eye of Providence,
    Daybreak Gavel, Toxic Blade, Shield of the Phoenix.'
  slot_scores:
    Avenging Blade:
      total: 0.56
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.77
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.73
      pick: 0.17
      fit: 0.14
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.72
      win: 0.65
      pick: 0.51
      fit: 0.66
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.23
    Runeforged Hammer:
      total: 0.61
      efficiency: 0.57
      win: 0.75
      pick: 0.04
      fit: 0.47
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.59
      pick: 0.38
      fit: 0.82
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Runeforged Hammer
  - Riptalon
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
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Berserker''s Shield, Golden Blade, Amanita Charm,
    Riptalon, Tyrfing, Silverbranch Bow, Toxic Blade, Kinetic Cuirass, Lernaean Bow,
    Breastplate of Valor, Tekko-Kagi, Freya''s Tears, Pharaoh''s Curse, Shogun''s
    Ofuda, Shield Splitter, Eye of the Storm, Dominance, Daybreak Gavel, Avenging
    Blade, Erosion, Qin''s Blade, Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.62
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.73
      pick: 0.17
      fit: 0.1
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.65
      pick: 0.51
      fit: 0.27
    Runeforged Hammer:
      total: 0.59
      efficiency: 0.57
      win: 0.75
      pick: 0.04
      fit: 0.33
    Riptalon:
      total: 0.54
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Runeforged Hammer
  - Freya's Tears
  flex_slots:
  - Freya's Tears
  - Hydra's Lament
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
    + fit + win/pick). Underrated for this god: Runeforged Hammer, Breastplate of
    Valor, Freya''s Tears, Amanita Charm, Shield of the Phoenix, Screeching Gargoyle,
    Kinetic Cuirass, Arondight, Berserker''s Shield, Gladiator''s Shield, Pendulum
    Blade, Eye of Erebus, Shield Splitter, Prophetic Cloak, Chandra''s Grace, Eye
    of the Storm, Daybreak Gavel, Erosion, Eye of Providence, Avenging Blade, Stone
    of Binding, Midgardian Mail, The Crusher.'
  slot_scores:
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.73
      pick: 0.17
      fit: 0.44
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.65
      pick: 0.51
      fit: 0.6
    Hydra's Lament:
      total: 0.55
      efficiency: 0.54
      win: 0.57
      pick: 0.41
      fit: 0.56
    Runeforged Hammer:
      total: 0.59
      efficiency: 0.57
      win: 0.75
      pick: 0.04
      fit: 0.33
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.53
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Eye of the Storm
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Eye of the Storm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Runeforged Hammer, Kinetic Cuirass, Shield
    Splitter, Eye of the Storm, Freya''s Tears, Avenging Blade, Berserker''s Shield,
    Breastplate of Valor, The Crusher, Erosion, Eye of Providence, Golden Blade, Shield
    of the Phoenix, Daybreak Gavel, Avatar''s Parashu, Midgardian Mail, Stone of Binding,
    Tyrfing, Pendulum Blade, Transcendence, Hide of the Nemean Lion.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.65
      pick: 0.51
      fit: 0.55
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.55
    Shield Splitter:
      total: 0.55
      efficiency: 0.55
      win: 0.6
      pick: 0.0
      fit: 0.56
    Eye of the Storm:
      total: 0.54
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.61
    Runeforged Hammer:
      total: 0.62
      efficiency: 0.57
      win: 0.75
      pick: 0.04
      fit: 0.58
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.45
  starter: *id001
---
