---
type: smite-build
god: Thor
mode: Conquest
builds:
- source: community
  aspect: Aspect of Thunderstruck
  aspect_pick_rate: 0.48
  aspect_win_rate: 0.53
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.48
    win_rate: 0.49
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.16
      win_rate: 0.71
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.67
  - name: Hydra's Lament
    pick_rate: 0.19
    win_rate: 0.35
    alternates:
    - name: Barbed Carver
      pick_rate: 0.13
      win_rate: 0.43
    - name: Transcendence
      pick_rate: 0.09
      win_rate: 0.8
  - name: Barbed Carver
    pick_rate: 0.13
    win_rate: 0.38
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.13
      win_rate: 0.77
    - name: Heartseeker
      pick_rate: 0.12
      win_rate: 0.58
  - name: Heartseeker
    pick_rate: 0.25
    win_rate: 0.48
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.5
    - name: Brawler’s Beat Stick
      pick_rate: 0.07
      win_rate: 0.86
  - name: Titan's Bane
    pick_rate: 0.13
    win_rate: 0.36
    alternates:
    - name: Avatar's Parashu
      pick_rate: 0.13
      win_rate: 0.36
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.83
  - name: Skeggox
    pick_rate: 0.11
    win_rate: 0.71
    alternates:
    - name: Lucerne Hammer
      pick_rate: 0.1
      win_rate: 0.33
    - name: Engraved Guard
      pick_rate: 0.08
      win_rate: 0.4
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.34
    win_rate: 0.5
  - name: Bluestone Brooch
    pick_rate: 0.17
    win_rate: 0.67
  - name: Bumba's Cudgel
    pick_rate: 0.14
    win_rate: 0.47
  source_url: https://smitebrain.com/gods/thor/
  last_verified: '2026-10-07'
  god_win_rate: 0.5660377358490566
  god_matches_won: 60
  god_matches_played: 106
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-07'
  god_matches_analyzed: 939
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Transcendence
  - Shifter's Shield
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Transcendence, Shifter''s Shield, Amanita Charm, Runeforged Hammer,
    Kinetic Cuirass, Shield Splitter, Eye of the Storm, Avenging Blade, Berserker''s
    Shield, Genji''s Guard, Breastplate of Valor, The Crusher, The Reaper, Erosion,
    Eye of Providence, Golden Blade, Draconic Scale, Shield of the Phoenix, Daybreak
    Gavel, Midgardian Mail, Stone of Binding, Tyrfing, Pendulum Blade, Hide of the
    Nemean Lion.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.58
      efficiency: 0.42
      win: 0.86
      pick: 0.12
      fit: 0.26
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.49
      pick: 0.48
      fit: 0.55
    Transcendence:
      total: 0.59
      efficiency: 0.53
      win: 0.8
      pick: 0.12
      fit: 0.3
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.67
      pick: 0.11
      fit: 0.45
    Heartseeker:
      total: 0.51
      efficiency: 0.47
      win: 0.48
      pick: 0.42
      fit: 0.71
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Transcendence
  - Shifter's Shield
  - Heartseeker
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Shifter's Shield
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Transcendence,
    Shifter''s Shield, Genji''s Guard, Amanita Charm, Breastplate of Valor, Runeforged
    Hammer, Kinetic Cuirass, Shield Splitter, Eye of the Storm, Berserker''s Shield,
    Avenging Blade, The Crusher, Shield of the Phoenix, The Reaper, Arondight, Daybreak
    Gavel, Screeching Gargoyle, Erosion, Eye of Providence, Oni Hunter''s Garb, Pendulum
    Blade, Stone of Binding, Draconic Scale, Midgardian Mail, Tyrfing.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.56
      efficiency: 0.42
      win: 0.86
      pick: 0.12
      fit: 0.15
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.49
      pick: 0.48
      fit: 0.53
    Transcendence:
      total: 0.59
      efficiency: 0.53
      win: 0.8
      pick: 0.12
      fit: 0.29
    Freya's Tears:
      total: 0.49
      efficiency: 0.61
      win: 0.5
      pick: 0.17
      fit: 0.26
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.67
      pick: 0.11
      fit: 0.26
    Heartseeker:
      total: 0.49
      efficiency: 0.47
      win: 0.48
      pick: 0.42
      fit: 0.62
  community_ordered:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Shifter's Shield
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Shifter's Shield
  - Heartseeker
  flex_slots:
  - Freya's Tears
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Shifter''s Shield, Amanita Charm, Genji''s Guard, Breastplate of Valor, Runeforged
    Hammer, Kinetic Cuirass, Shield Splitter, The Crusher, Berserker''s Shield, Shield
    of the Phoenix, The Reaper, Eye of the Storm, Pendulum Blade, Screeching Gargoyle,
    Avenging Blade, Daybreak Gavel, Arondight, Erosion, Eye of Providence, Stone of
    Binding, Draconic Scale, Midgardian Mail, Magi''s Cloak, Hide of the Nemean Lion.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.56
      efficiency: 0.42
      win: 0.86
      pick: 0.12
      fit: 0.16
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.49
      pick: 0.48
      fit: 0.56
    Transcendence:
      total: 0.57
      efficiency: 0.53
      win: 0.8
      pick: 0.12
      fit: 0.16
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.5
      pick: 0.17
      fit: 0.32
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.67
      pick: 0.11
      fit: 0.27
    Heartseeker:
      total: 0.49
      efficiency: 0.47
      win: 0.48
      pick: 0.42
      fit: 0.6
  community_ordered:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Shifter's Shield
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix,
    Runeforged Hammer, The Reaper, Shield Splitter, Eye of the Storm, Berserker''s
    Shield, Erosion, Genji''s Guard, Eye of Providence, Breastplate of Valor, Yogi''s
    Necklace, Draconic Scale, Avenging Blade, Phoenix Feather, Stone of Binding, Midgardian
    Mail, Chandra''s Grace, The Crusher, Daybreak Gavel, Hide of the Nemean Lion,
    Magi''s Cloak, Leviathan''s Hide.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.59
      efficiency: 0.42
      win: 0.86
      pick: 0.12
      fit: 0.34
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.49
      pick: 0.48
      fit: 0.45
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.48
      pick: 0.0
      fit: 0.65
    Transcendence:
      total: 0.59
      efficiency: 0.53
      win: 0.8
      pick: 0.12
      fit: 0.24
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.67
      pick: 0.11
      fit: 0.55
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Transcendence
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Brawler’s Beat Stick
  - Avenging Blade
  - Jotunn's Revenge
  - Transcendence
  - Shifter's Shield
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    for this god: Shifter''s Shield, Avenging Blade, Amanita Charm, The Crusher, Stone
    of Binding, Runeforged Hammer, The Reaper, Kinetic Cuirass, Void Shield, Screeching
    Gargoyle, Shield Splitter, Void Stone, Eye of the Storm, Genji''s Guard, Breastplate
    of Valor, Pendulum Blade, Berserker''s Shield, Tekko-Kagi, Erosion, Eye of Providence,
    Daybreak Gavel, Toxic Blade, Shield of the Phoenix, Draconic Scale.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.57
      efficiency: 0.42
      win: 0.86
      pick: 0.12
      fit: 0.2
    Avenging Blade:
      total: 0.51
      efficiency: 0.49
      win: 0.48
      pick: 0.0
      fit: 0.77
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.49
      pick: 0.48
      fit: 0.66
    Transcendence:
      total: 0.58
      efficiency: 0.53
      win: 0.8
      pick: 0.12
      fit: 0.23
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.67
      pick: 0.11
      fit: 0.34
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.48
      pick: 0.42
      fit: 0.82
  community_ordered:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Transcendence
  - Shifter's Shield
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Brawler’s Beat Stick
  - Berserker's Shield
  - Transcendence
  - Shifter's Shield
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Berserker''s Shield, Golden Blade, Amanita Charm,
    Riptalon, Tyrfing, Silverbranch Bow, Toxic Blade, Kinetic Cuirass, Lernaean Bow,
    Runeforged Hammer, Genji''s Guard, Breastplate of Valor, Tekko-Kagi, Pharaoh''s
    Curse, The Reaper, Shogun''s Ofuda, Shield Splitter, Eye of the Storm, Dominance,
    Daybreak Gavel, Avenging Blade, Erosion, Qin''s Blade, Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.52
      win: 0.48
      pick: 0.0
      fit: 0.62
    Brawler’s Beat Stick:
      total: 0.56
      efficiency: 0.42
      win: 0.86
      pick: 0.12
      fit: 0.15
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.48
      pick: 0.0
      fit: 0.42
    Transcendence:
      total: 0.57
      efficiency: 0.53
      win: 0.8
      pick: 0.12
      fit: 0.12
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.67
      pick: 0.11
      fit: 0.26
    Riptalon:
      total: 0.48
      efficiency: 0.51
      win: 0.48
      pick: 0.0
      fit: 0.59
  community_ordered:
  - Brawler’s Beat Stick
  - Transcendence
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Freya's Tears
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Shifter''s Shield, Genji''s Guard,
    Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Screeching Gargoyle,
    Kinetic Cuirass, Runeforged Hammer, Arondight, Berserker''s Shield, Gladiator''s
    Shield, Pendulum Blade, Eye of Erebus, Shield Splitter, Prophetic Cloak, Chandra''s
    Grace, Eye of the Storm, Daybreak Gavel, Erosion, Eye of Providence, Avenging
    Blade, Draconic Scale, Stone of Binding, Midgardian Mail, The Crusher.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.57
      efficiency: 0.42
      win: 0.86
      pick: 0.12
      fit: 0.18
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.49
      pick: 0.48
      fit: 0.6
    Transcendence:
      total: 0.57
      efficiency: 0.53
      win: 0.8
      pick: 0.12
      fit: 0.11
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.17
      fit: 0.53
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.67
      pick: 0.11
      fit: 0.3
  community_ordered:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Shifter's Shield
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
      total: 0.58
      efficiency: 0.72
      win: 0.49
      pick: 0.48
      fit: 0.55
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.48
      pick: 0.0
      fit: 0.55
    Shield Splitter:
      total: 0.49
      efficiency: 0.55
      win: 0.48
      pick: 0.0
      fit: 0.56
    Eye of the Storm:
      total: 0.49
      efficiency: 0.52
      win: 0.48
      pick: 0.0
      fit: 0.61
    Runeforged Hammer:
      total: 0.5
      efficiency: 0.57
      win: 0.48
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
---
