---
type: smite-build
god: Ravana
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rakshasa King
  aspect_pick_rate: 0.06
  aspect_win_rate: 1.0
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.76
    win_rate: 0.63
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.15
      win_rate: 0.67
    - name: Shifter's Shield
      pick_rate: 0.02
      win_rate: 0.33
  - name: Sanguine Lash
    pick_rate: 0.51
    win_rate: 0.63
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.07
      win_rate: 0.64
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.64
  - name: Umbral Link
    pick_rate: 0.18
    win_rate: 0.61
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.22
      win_rate: 0.6
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.65
  - name: Freya's Tears
    pick_rate: 0.18
    win_rate: 0.64
    alternates:
    - name: Brawler’s Beat Stick
      pick_rate: 0.1
      win_rate: 0.27
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.78
  - name: Hide of the Nemean Lion
    pick_rate: 0.09
    win_rate: 0.62
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.56
    - name: Xibalban Effigy
      pick_rate: 0.08
      win_rate: 0.75
  - name: Xibalban Effigy
    pick_rate: 0.06
    win_rate: 0.57
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.5
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.67
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.44
    win_rate: 0.62
  - name: Bumba's Hammer
    pick_rate: 0.22
    win_rate: 0.71
  - name: Leather Cowl
    pick_rate: 0.12
    win_rate: 0.47
  source_url: https://smitebrain.com/gods/ravana/
  last_verified: '2026-10-08'
  god_win_rate: 0.6
  god_matches_won: 96
  god_matches_played: 160
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
  - Kinetic Cuirass
  - Runeforged Hammer
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Shifter's Shield
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Runeforged Hammer,
    Shield Splitter, Eye of the Storm, Genji''s Guard, Breastplate of Valor, Hydra''s
    Lament, Heartseeker, Berserker''s Shield, Avenging Blade, Shield of the Phoenix,
    Titan''s Bane, The Crusher, Erosion, The Reaper, Eye of Providence, Draconic Scale,
    Daybreak Gavel, Pendulum Blade, Arondight, Midgardian Mail, Golden Blade, Screeching
    Gargoyle, Stone of Binding, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.67
      pick: 0.15
      fit: 0.58
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.64
      pick: 0.1
      fit: 0.52
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.57
      win: 0.63
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.65
      pick: 0.17
      fit: 0.42
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.64
      pick: 0.3
      fit: 0.36
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Amanita Charm, Genji''s Guard, Breastplate of Valor, Hydra''s Lament,
    Runeforged Hammer, Kinetic Cuirass, Heartseeker, Shield Splitter, Eye of the Storm,
    Berserker''s Shield, Avenging Blade, Titan''s Bane, The Crusher, Shield of the
    Phoenix, Transcendence, Daybreak Gavel, The Reaper, Arondight, Screeching Gargoyle,
    Erosion, Eye of Providence, Oni Hunter''s Garb, Stone of Binding, Draconic Scale,
    Pendulum Blade, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.63
      pick: 0.0
      fit: 0.25
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.67
      pick: 0.15
      fit: 0.52
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.63
      pick: 0.0
      fit: 0.28
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.64
      pick: 0.3
      fit: 0.25
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.27
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, Amanita Charm, Genji''s Guard, Kinetic Cuirass, Breastplate
    of Valor, Runeforged Hammer, Heartseeker, Hydra''s Lament, Berserker''s Shield,
    Shield of the Phoenix, Titan''s Bane, Shield Splitter, The Crusher, Eye of the
    Storm, The Reaper, Pendulum Blade, Avenging Blade, Screeching Gargoyle, Daybreak
    Gavel, Arondight, Erosion, Eye of Providence, Draconic Scale, Avatar''s Parashu,
    Stone of Binding, Midgardian Mail, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.63
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.67
      pick: 0.15
      fit: 0.56
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.64
      pick: 0.1
      fit: 0.39
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.63
      pick: 0.0
      fit: 0.16
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.64
      pick: 0.3
      fit: 0.32
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.29
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shifter's Shield
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, Kinetic Cuirass,
    Runeforged Hammer, The Reaper, Shield Splitter, Genji''s Guard, Breastplate of
    Valor, Eye of the Storm, Berserker''s Shield, Erosion, Yogi''s Necklace, Eye of
    Providence, Hydra''s Lament, Draconic Scale, Phoenix Feather, Avenging Blade,
    Heartseeker, Chandra''s Grace, Glorious Pridwen, Stone of Binding, Midgardian
    Mail, Titan''s Bane, Daybreak Gavel, The Crusher, Magi''s Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.67
      pick: 0.15
      fit: 0.49
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.64
      pick: 0.1
      fit: 0.61
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.53
      win: 0.63
      pick: 0.0
      fit: 0.76
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.65
      pick: 0.17
      fit: 0.51
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.64
      pick: 0.3
      fit: 0.42
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.81
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Avenging Blade, Heartseeker, Amanita Charm, Kinetic
    Cuirass, Screeching Gargoyle, Titan''s Bane, Runeforged Hammer, Stone of Binding,
    The Crusher, Void Shield, The Reaper, Genji''s Guard, Breastplate of Valor, Void
    Stone, Hydra''s Lament, Shield Splitter, Pendulum Blade, Eye of the Storm, Berserker''s
    Shield, Avatar''s Parashu, Shield of the Phoenix, Daybreak Gavel, Tekko-Kagi,
    Erosion, Eye of Providence, Draconic Scale, Arondight.'
  slot_scores:
    Avenging Blade:
      total: 0.57
      efficiency: 0.49
      win: 0.63
      pick: 0.0
      fit: 0.75
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.67
      pick: 0.15
      fit: 0.67
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.63
      pick: 0.0
      fit: 0.21
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.64
      pick: 0.3
      fit: 0.28
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.63
      pick: 0.0
      fit: 0.77
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.33
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Riptalon
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Berserker''s Shield, Golden Blade, Amanita Charm,
    Kinetic Cuirass, Riptalon, Tyrfing, Silverbranch Bow, Genji''s Guard, Breastplate
    of Valor, Toxic Blade, Runeforged Hammer, Lernaean Bow, Pharaoh''s Curse, Tekko-Kagi,
    The Reaper, Shogun''s Ofuda, Hydra''s Lament, Shield Splitter, Heartseeker, Eye
    of the Storm, Shield of the Phoenix, Daybreak Gavel, Avenging Blade, Dominance,
    Erosion, Eye of Providence, Screeching Gargoyle.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.63
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.67
      pick: 0.15
      fit: 0.31
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.64
      pick: 0.3
      fit: 0.22
    Riptalon:
      total: 0.54
      efficiency: 0.51
      win: 0.63
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
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
  - Amanita Charm
  - Hydra's Lament
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Breastplate of Valor, Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Kinetic
    Cuirass, Screeching Gargoyle, Runeforged Hammer, Berserker''s Shield, Arondight,
    Gladiator''s Shield, Eye of Erebus, Pendulum Blade, Shield Splitter, Prophetic
    Cloak, Chandra''s Grace, Heartseeker, Eye of the Storm, Daybreak Gavel, Erosion,
    Eye of Providence, Avenging Blade, Draconic Scale, Midgardian Mail, Stone of Binding,
    Titan''s Bane, The Crusher.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.63
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.67
      pick: 0.15
      fit: 0.59
    Hydra's Lament:
      total: 0.56
      efficiency: 0.54
      win: 0.63
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.64
      pick: 0.3
      fit: 0.52
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.31
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
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
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Runeforged Hammer,
    Kinetic Cuirass, Shield Splitter, Eye of the Storm, Genji''s Guard, Breastplate
    of Valor, Hydra''s Lament, Heartseeker, Berserker''s Shield, Avenging Blade, Shield
    of the Phoenix, Titan''s Bane, The Crusher, Erosion, The Reaper, Eye of Providence,
    Draconic Scale, Daybreak Gavel, Pendulum Blade, Arondight, Midgardian Mail, Golden
    Blade, Screeching Gargoyle, Stone of Binding, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.67
      pick: 0.15
      fit: 0.58
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.64
      pick: 0.1
      fit: 0.52
    Shield Splitter:
      total: 0.55
      efficiency: 0.55
      win: 0.63
      pick: 0.0
      fit: 0.5
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.57
      win: 0.63
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.64
      pick: 0.3
      fit: 0.36
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
---
