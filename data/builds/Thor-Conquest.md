---
type: smite-build
god: Thor
mode: Conquest
builds:
- source: community
  aspect: Aspect of Thunderstruck
  aspect_pick_rate: 0.3
  aspect_win_rate: 0.56
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.58
    win_rate: 0.52
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.6
    - name: Runeforged Hammer
      pick_rate: 0.07
      win_rate: 0.58
  - name: Hydra's Lament
    pick_rate: 0.26
    win_rate: 0.49
    alternates:
    - name: Barbed Carver
      pick_rate: 0.16
      win_rate: 0.54
    - name: Transcendence
      pick_rate: 0.09
      win_rate: 0.58
  - name: Barbed Carver
    pick_rate: 0.12
    win_rate: 0.46
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.11
      win_rate: 0.54
    - name: The Reaper
      pick_rate: 0.09
      win_rate: 0.56
  - name: Heartseeker
    pick_rate: 0.29
    win_rate: 0.53
    alternates:
    - name: Titan's Bane
      pick_rate: 0.11
      win_rate: 0.45
    - name: The Crusher
      pick_rate: 0.05
      win_rate: 0.57
  - name: Titan's Bane
    pick_rate: 0.12
    win_rate: 0.53
    alternates:
    - name: Heartseeker
      pick_rate: 0.13
      win_rate: 0.58
    - name: Avatar's Parashu
      pick_rate: 0.04
      win_rate: 0.61
  - name: Skeggox
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.52
    - name: Magi's Cloak
      pick_rate: 0.05
      win_rate: 0.63
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.34
    win_rate: 0.61
  - name: Bumba's Cudgel
    pick_rate: 0.23
    win_rate: 0.44
  - name: Bluestone Brooch
    pick_rate: 0.19
    win_rate: 0.64
  source_url: https://smitebrain.com/gods/thor/
  last_verified: '2026-08-24'
  god_win_rate: 0.5405405405405406
  god_matches_won: 1020
  god_matches_played: 1887
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-24'
  god_matches_analyzed: 17273
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Runeforged Hammer
  - Shifter's Shield
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Runeforged Hammer, Amanita Charm, Kinetic Cuirass, Shield Splitter,
    Eye of the Storm, The Crusher, Avatar''s Parashu, The Reaper, Freya''s Tears,
    Avenging Blade, Berserker''s Shield, Genji''s Guard, Breastplate of Valor, Transcendence,
    Erosion, Eye of Providence, Golden Blade, Draconic Scale, Shield of the Phoenix,
    Daybreak Gavel, Midgardian Mail, Stone of Binding, Tyrfing, Pendulum Blade, Hide
    of the Nemean Lion.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.52
      pick: 0.58
      fit: 0.55
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.58
      pick: 0.12
      fit: 0.3
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.07
      fit: 0.58
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.6
      pick: 0.16
      fit: 0.45
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.53
      pick: 0.48
      fit: 0.71
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
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
  - Runeforged Hammer
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Runeforged
    Hammer, Genji''s Guard, Amanita Charm, Breastplate of Valor, Freya''s Tears, Kinetic
    Cuirass, Transcendence, The Crusher, Shield Splitter, Eye of the Storm, The Reaper,
    Berserker''s Shield, Avenging Blade, Shield of the Phoenix, Arondight, Daybreak
    Gavel, Screeching Gargoyle, Erosion, Eye of Providence, Oni Hunter''s Garb, Pendulum
    Blade, Stone of Binding, Draconic Scale, Midgardian Mail, Tyrfing.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.52
      pick: 0.58
      fit: 0.53
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.58
      pick: 0.12
      fit: 0.29
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.57
      win: 0.58
      pick: 0.07
      fit: 0.42
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.53
      pick: 0.48
      fit: 0.62
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.26
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Runeforged Hammer
  - Shifter's Shield
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
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
    god: Runeforged Hammer, Amanita Charm, Genji''s Guard, Breastplate of Valor, Freya''s
    Tears, The Crusher, Kinetic Cuirass, Avatar''s Parashu, The Reaper, Shield Splitter,
    Berserker''s Shield, Shield of the Phoenix, Eye of the Storm, Pendulum Blade,
    Screeching Gargoyle, Avenging Blade, Daybreak Gavel, Arondight, Erosion, Eye of
    Providence, Stone of Binding, Draconic Scale, Midgardian Mail, Hide of the Nemean
    Lion.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.52
      pick: 0.58
      fit: 0.56
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.58
      pick: 0.12
      fit: 0.16
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.57
      win: 0.58
      pick: 0.07
      fit: 0.37
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.6
      pick: 0.16
      fit: 0.27
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.53
      pick: 0.48
      fit: 0.6
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Reaper
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - The Reaper
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Amanita Charm, Runeforged Hammer, Kinetic Cuirass, The Reaper, Shield
    of the Phoenix, Shield Splitter, Eye of the Storm, Freya''s Tears, Berserker''s
    Shield, Erosion, Genji''s Guard, Eye of Providence, Breastplate of Valor, Yogi''s
    Necklace, Draconic Scale, The Crusher, Avenging Blade, Phoenix Feather, Stone
    of Binding, Midgardian Mail, Chandra''s Grace, Daybreak Gavel, Hide of the Nemean
    Lion, Leviathan''s Hide.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.52
      pick: 0.58
      fit: 0.45
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.65
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.07
      fit: 0.55
    The Reaper:
      total: 0.54
      efficiency: 0.5
      win: 0.56
      pick: 0.14
      fit: 0.71
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.6
      pick: 0.16
      fit: 0.55
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Transcendence
  - Runeforged Hammer
  - The Crusher
  - Heartseeker
  flex_slots:
  - Runeforged Hammer
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Avenging Blade, Runeforged Hammer, Avatar''s Parashu,
    The Reaper, Amanita Charm, Stone of Binding, Kinetic Cuirass, Void Shield, Screeching
    Gargoyle, Shield Splitter, Void Stone, Eye of the Storm, Freya''s Tears, Genji''s
    Guard, Breastplate of Valor, Pendulum Blade, Berserker''s Shield, Tekko-Kagi,
    Erosion, Eye of Providence, Daybreak Gavel, Toxic Blade, Shield of the Phoenix,
    Draconic Scale.'
  slot_scores:
    Avenging Blade:
      total: 0.53
      efficiency: 0.49
      win: 0.55
      pick: 0.0
      fit: 0.77
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.52
      pick: 0.58
      fit: 0.66
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.58
      pick: 0.12
      fit: 0.23
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.57
      win: 0.58
      pick: 0.07
      fit: 0.47
    The Crusher:
      total: 0.53
      efficiency: 0.47
      win: 0.57
      pick: 0.08
      fit: 0.72
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.53
      pick: 0.48
      fit: 0.82
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Runeforged Hammer
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Golden Blade, Amanita Charm, Runeforged Hammer,
    Riptalon, Tyrfing, Silverbranch Bow, Toxic Blade, The Reaper, Kinetic Cuirass,
    Lernaean Bow, Genji''s Guard, Breastplate of Valor, Tekko-Kagi, Freya''s Tears,
    Pharaoh''s Curse, Shogun''s Ofuda, Shield Splitter, Eye of the Storm, Dominance,
    Daybreak Gavel, Avenging Blade, Erosion, Qin''s Blade, Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.62
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.52
      pick: 0.58
      fit: 0.27
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.57
      win: 0.58
      pick: 0.07
      fit: 0.33
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.26
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Shifter's Shield
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Freya''s Tears, Amanita Charm, Shield of the Phoenix, Runeforged Hammer, Screeching
    Gargoyle, Kinetic Cuirass, Arondight, Berserker''s Shield, Gladiator''s Shield,
    Pendulum Blade, Eye of Erebus, Shield Splitter, Prophetic Cloak, The Crusher,
    Chandra''s Grace, Eye of the Storm, Daybreak Gavel, Erosion, Eye of Providence,
    Avenging Blade, Draconic Scale, Stone of Binding, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.44
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.52
      pick: 0.58
      fit: 0.6
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.53
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.6
      pick: 0.16
      fit: 0.3
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.3
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
    Genji''s Guard, Breastplate of Valor, The Crusher, The Reaper, Erosion, Eye of
    Providence, Golden Blade, Draconic Scale, Shield of the Phoenix, Daybreak Gavel,
    Avatar''s Parashu, Midgardian Mail, Stone of Binding, Tyrfing, Pendulum Blade,
    Transcendence, Hide of the Nemean Lion.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.52
      pick: 0.58
      fit: 0.55
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.55
    Shield Splitter:
      total: 0.52
      efficiency: 0.55
      win: 0.55
      pick: 0.0
      fit: 0.56
    Eye of the Storm:
      total: 0.52
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.61
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.07
      fit: 0.58
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.45
  starter: *id001
---
