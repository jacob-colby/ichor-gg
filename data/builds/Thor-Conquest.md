---
type: smite-build
god: Thor
mode: Conquest
builds:
- source: community
  aspect: Aspect of Thunderstruck
  aspect_pick_rate: 0.49
  aspect_win_rate: 0.56
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.42
    win_rate: 0.54
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.2
      win_rate: 0.63
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.65
  - name: Hydra's Lament
    pick_rate: 0.19
    win_rate: 0.42
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.13
      win_rate: 0.69
    - name: Barbed Carver
      pick_rate: 0.12
      win_rate: 0.5
  - name: Heartseeker
    pick_rate: 0.13
    win_rate: 0.67
    alternates:
    - name: Barbed Carver
      pick_rate: 0.1
      win_rate: 0.5
    - name: Hydra's Lament
      pick_rate: 0.1
      win_rate: 0.74
  - name: Freya's Tears
    pick_rate: 0.1
    win_rate: 0.56
    alternates:
    - name: Heartseeker
      pick_rate: 0.23
      win_rate: 0.56
    - name: Brawler’s Beat Stick
      pick_rate: 0.06
      win_rate: 0.73
  - name: Avatar's Parashu
    pick_rate: 0.1
    win_rate: 0.53
    alternates:
    - name: Titan's Bane
      pick_rate: 0.1
      win_rate: 0.44
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.83
  - name: Skeggox
    pick_rate: 0.12
    win_rate: 0.85
    alternates:
    - name: Engraved Guard
      pick_rate: 0.07
      win_rate: 0.38
    - name: Lucerne Hammer
      pick_rate: 0.06
      win_rate: 0.29
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.29
    win_rate: 0.59
  - name: Bluestone Brooch
    pick_rate: 0.19
    win_rate: 0.62
  - name: Bumba's Cudgel
    pick_rate: 0.13
    win_rate: 0.56
  source_url: https://smitebrain.com/gods/thor/
  last_verified: '2026-10-08'
  god_win_rate: 0.5918367346938775
  god_matches_won: 116
  god_matches_played: 196
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-08'
  god_matches_analyzed: 1596
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
  - Runeforged Hammer
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Amanita Charm, Runeforged Hammer, Kinetic Cuirass,
    Shield Splitter, Eye of the Storm, Avenging Blade, Berserker''s Shield, Genji''s
    Guard, Breastplate of Valor, The Crusher, The Reaper, Erosion, Eye of Providence,
    Golden Blade, Draconic Scale, Shield of the Phoenix, Daybreak Gavel, Midgardian
    Mail, Stone of Binding, Tyrfing, Pendulum Blade, Transcendence, Hide of the Nemean
    Lion.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.54
      pick: 0.42
      fit: 0.55
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.3
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.58
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.65
      pick: 0.13
      fit: 0.45
    Heartseeker:
      total: 0.58
      efficiency: 0.47
      win: 0.67
      pick: 0.2
      fit: 0.71
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Jotunn's Revenge
  - Shifter's Shield
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
  - Shifter's Shield
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
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Shifter''s
    Shield, Genji''s Guard, Amanita Charm, Breastplate of Valor, Runeforged Hammer,
    Kinetic Cuirass, Shield Splitter, Eye of the Storm, Berserker''s Shield, Avenging
    Blade, The Crusher, Shield of the Phoenix, Transcendence, The Reaper, Arondight,
    Daybreak Gavel, Screeching Gargoyle, Erosion, Eye of Providence, Oni Hunter''s
    Garb, Pendulum Blade, Stone of Binding, Draconic Scale, Midgardian Mail, Tyrfing.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.54
      pick: 0.42
      fit: 0.53
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.29
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.65
      pick: 0.13
      fit: 0.26
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.67
      pick: 0.2
      fit: 0.62
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Jotunn's Revenge
  - Shifter's Shield
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Shifter's Shield
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Shifter''s Shield, Amanita Charm, Genji''s Guard, Breastplate of Valor, Runeforged
    Hammer, Kinetic Cuirass, Shield Splitter, The Crusher, Berserker''s Shield, Shield
    of the Phoenix, The Reaper, Eye of the Storm, Pendulum Blade, Screeching Gargoyle,
    Avenging Blade, Daybreak Gavel, Arondight, Erosion, Eye of Providence, Stone of
    Binding, Draconic Scale, Midgardian Mail, Magi''s Cloak, Hide of the Nemean Lion.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.54
      pick: 0.42
      fit: 0.56
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.16
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.56
      pick: 0.17
      fit: 0.32
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.65
      pick: 0.13
      fit: 0.27
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.67
      pick: 0.2
      fit: 0.6
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.27
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Brawler’s Beat Stick — magical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shifter''s Shield, Kinetic Cuirass, Shield of the Phoenix,
    Runeforged Hammer, The Reaper, Shield Splitter, Eye of the Storm, Berserker''s
    Shield, Erosion, Genji''s Guard, Eye of Providence, Breastplate of Valor, Yogi''s
    Necklace, Draconic Scale, Avenging Blade, Phoenix Feather, Stone of Binding, Midgardian
    Mail, Chandra''s Grace, The Crusher, Daybreak Gavel, Hide of the Nemean Lion,
    Magi''s Cloak, Leviathan''s Hide.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.54
      pick: 0.42
      fit: 0.45
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.65
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.72
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.65
      pick: 0.13
      fit: 0.55
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.67
      pick: 0.2
      fit: 0.61
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Jotunn's Revenge
  - Shifter's Shield
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Transcendence
  - Shifter's Shield
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
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Brawler’s Beat Stick — physical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Shifter''s Shield, Avenging Blade, Amanita Charm, The Crusher, Stone
    of Binding, Runeforged Hammer, The Reaper, Kinetic Cuirass, Void Shield, Screeching
    Gargoyle, Shield Splitter, Void Stone, Eye of the Storm, Genji''s Guard, Breastplate
    of Valor, Pendulum Blade, Berserker''s Shield, Tekko-Kagi, Erosion, Eye of Providence,
    Daybreak Gavel, Toxic Blade, Shield of the Phoenix, Draconic Scale.'
  slot_scores:
    Avenging Blade:
      total: 0.54
      efficiency: 0.49
      win: 0.55
      pick: 0.0
      fit: 0.77
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.54
      pick: 0.42
      fit: 0.66
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.23
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.65
      pick: 0.13
      fit: 0.34
    Heartseeker:
      total: 0.6
      efficiency: 0.47
      win: 0.67
      pick: 0.2
      fit: 0.82
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.34
  community_ordered:
  - Jotunn's Revenge
  - Shifter's Shield
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - Heartseeker
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
    swap: Brawler’s Beat Stick — physical protection
    swap_item: Brawler’s Beat Stick
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Shifter''s Shield, Golden Blade, Amanita Charm,
    Riptalon, Tyrfing, Silverbranch Bow, Toxic Blade, Kinetic Cuirass, Lernaean Bow,
    Runeforged Hammer, Genji''s Guard, Breastplate of Valor, Tekko-Kagi, Pharaoh''s
    Curse, The Reaper, Shogun''s Ofuda, Shield Splitter, Eye of the Storm, Dominance,
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
      total: 0.56
      efficiency: 0.72
      win: 0.54
      pick: 0.42
      fit: 0.27
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.65
      pick: 0.13
      fit: 0.26
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.67
      pick: 0.2
      fit: 0.45
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.59
  community_ordered:
  - Jotunn's Revenge
  - Shifter's Shield
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Heartseeker
  flex_slots:
  - Breastplate of Valor
  - Shifter's Shield
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Shifter''s Shield, Amanita Charm, Shield of the Phoenix, Screeching Gargoyle,
    Kinetic Cuirass, Runeforged Hammer, Arondight, Berserker''s Shield, Gladiator''s
    Shield, Pendulum Blade, Eye of Erebus, Shield Splitter, Prophetic Cloak, Chandra''s
    Grace, Eye of the Storm, Daybreak Gavel, Erosion, Eye of Providence, Avenging
    Blade, Draconic Scale, Stone of Binding, Midgardian Mail, The Crusher.'
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
      win: 0.54
      pick: 0.42
      fit: 0.6
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.56
      pick: 0.17
      fit: 0.53
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.65
      pick: 0.13
      fit: 0.3
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.67
      pick: 0.2
      fit: 0.45
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Heartseeker
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
    Splitter, Eye of the Storm, Shifter''s Shield, Avenging Blade, Berserker''s Shield,
    Genji''s Guard, Breastplate of Valor, The Crusher, The Reaper, Erosion, Eye of
    Providence, Golden Blade, Draconic Scale, Shield of the Phoenix, Daybreak Gavel,
    Midgardian Mail, Stone of Binding, Tyrfing, Pendulum Blade, Transcendence, Hide
    of the Nemean Lion.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.54
      pick: 0.42
      fit: 0.55
    Kinetic Cuirass:
      total: 0.53
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
      total: 0.53
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
---
