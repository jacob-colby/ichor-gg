---
type: smite-build
god: Ravana
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rakshasa King
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.3
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.36
    win_rate: 0.58
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.29
      win_rate: 0.43
    - name: Daybreak Gavel
      pick_rate: 0.07
      win_rate: 0.4
  - name: Shifter's Shield
    pick_rate: 0.13
    win_rate: 0.45
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.13
      win_rate: 0.63
    - name: Hydra's Lament
      pick_rate: 0.08
      win_rate: 0.43
  - name: Sanguine Lash
    pick_rate: 0.1
    win_rate: 0.52
    alternates:
    - name: The Reaper
      pick_rate: 0.08
      win_rate: 0.48
    - name: The Crusher
      pick_rate: 0.08
      win_rate: 0.54
  - name: Heartseeker
    pick_rate: 0.14
    win_rate: 0.38
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.57
    - name: The Reaper
      pick_rate: 0.05
      win_rate: 0.7
  - name: Hide of the Nemean Lion
    pick_rate: 0.06
    win_rate: 0.56
    alternates:
    - name: Heartseeker
      pick_rate: 0.06
      win_rate: 0.55
    - name: Titan's Bane
      pick_rate: 0.05
      win_rate: 0.46
  - name: Shell of Rebuke
    pick_rate: 0.04
    win_rate: 0.53
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.04
      win_rate: 0.67
    - name: Titan's Bane
      pick_rate: 0.04
      win_rate: 0.6
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.25
    win_rate: 0.56
  - name: Hunter's Cowl
    pick_rate: 0.23
    win_rate: 0.6
  - name: Bumba's Cudgel
    pick_rate: 0.19
    win_rate: 0.36
  source_url: https://smitebrain.com/gods/ravana/
  last_verified: '2026-09-29'
  god_win_rate: 0.4975369458128079
  god_matches_won: 303
  god_matches_played: 609
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-29'
  god_matches_analyzed: 8229
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
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Kinetic Cuirass
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
    this god: Freya''s Tears, Amanita Charm, Titan''s Bane, Runeforged Hammer, Kinetic
    Cuirass, Shield Splitter, Eye of the Storm, Genji''s Guard, Breastplate of Valor,
    The Crusher, Berserker''s Shield, Avenging Blade, Hide of the Nemean Lion, Shield
    of the Phoenix, Erosion, Eye of Providence, Draconic Scale, Pendulum Blade, Arondight,
    Midgardian Mail, Golden Blade, The Reaper, Screeching Gargoyle, Hydra''s Lament,
    Stone of Binding, Avatar''s Parashu, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.43
      pick: 0.29
      fit: 0.58
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.52
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.57
      pick: 0.13
      fit: 0.36
    Titan's Bane:
      total: 0.52
      efficiency: 0.47
      win: 0.6
      pick: 0.12
      fit: 0.55
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Freya''s
    Tears, Titan''s Bane, Amanita Charm, Genji''s Guard, Breastplate of Valor, Runeforged
    Hammer, Kinetic Cuirass, The Crusher, Shield Splitter, Eye of the Storm, Berserker''s
    Shield, Avenging Blade, Hide of the Nemean Lion, Shield of the Phoenix, Hydra''s
    Lament, Transcendence, Arondight, Screeching Gargoyle, Erosion, Eye of Providence,
    Oni Hunter''s Garb, Stone of Binding, Draconic Scale, Pendulum Blade, Midgardian
    Mail, The Reaper, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.52
      pick: 0.0
      fit: 0.25
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.43
      pick: 0.29
      fit: 0.52
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.57
      pick: 0.13
      fit: 0.25
    Titan's Bane:
      total: 0.51
      efficiency: 0.47
      win: 0.6
      pick: 0.12
      fit: 0.44
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.27
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Freya''s Tears, Titan''s Bane, Amanita Charm, Genji''s Guard, Breastplate
    of Valor, Runeforged Hammer, Kinetic Cuirass, The Crusher, Berserker''s Shield,
    Shield of the Phoenix, Shield Splitter, Hide of the Nemean Lion, Eye of the Storm,
    Pendulum Blade, Avenging Blade, Screeching Gargoyle, Arondight, Erosion, The Reaper,
    Eye of Providence, Draconic Scale, Hydra''s Lament, Avatar''s Parashu, Stone of
    Binding, Midgardian Mail, Leviathan''s Hide, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.52
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.43
      pick: 0.29
      fit: 0.56
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.16
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.57
      pick: 0.13
      fit: 0.32
    Titan's Bane:
      total: 0.52
      efficiency: 0.47
      win: 0.6
      pick: 0.12
      fit: 0.5
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.29
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Titan's Bane
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
    this god: Amanita Charm, Freya''s Tears, Shield of the Phoenix, Kinetic Cuirass,
    Titan''s Bane, Runeforged Hammer, Shield Splitter, Genji''s Guard, Breastplate
    of Valor, Eye of the Storm, The Reaper, Berserker''s Shield, Hide of the Nemean
    Lion, Erosion, Yogi''s Necklace, Eye of Providence, Draconic Scale, Phoenix Feather,
    The Crusher, Avenging Blade, Chandra''s Grace, Glorious Pridwen, Stone of Binding,
    Midgardian Mail, Magi''s Cloak, Hydra''s Lament, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.43
      pick: 0.29
      fit: 0.49
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.61
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.76
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.57
      pick: 0.13
      fit: 0.42
    Titan's Bane:
      total: 0.51
      efficiency: 0.47
      win: 0.6
      pick: 0.12
      fit: 0.48
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.81
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - The Crusher
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    for this god: Titan''s Bane, Freya''s Tears, Avenging Blade, The Crusher, Amanita
    Charm, Screeching Gargoyle, Runeforged Hammer, Stone of Binding, Kinetic Cuirass,
    Void Shield, Genji''s Guard, Breastplate of Valor, Void Stone, Shield Splitter,
    Pendulum Blade, The Reaper, Eye of the Storm, Berserker''s Shield, Avatar''s Parashu,
    Shield of the Phoenix, Tekko-Kagi, Erosion, Eye of Providence, Draconic Scale,
    Arondight, Hydra''s Lament, Daybreak Gavel.'
  slot_scores:
    Avenging Blade:
      total: 0.52
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.75
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.43
      pick: 0.29
      fit: 0.67
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.57
      pick: 0.13
      fit: 0.28
    The Crusher:
      total: 0.51
      efficiency: 0.47
      win: 0.54
      pick: 0.12
      fit: 0.67
    Titan's Bane:
      total: 0.54
      efficiency: 0.47
      win: 0.6
      pick: 0.12
      fit: 0.67
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.33
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
  - Titan's Bane
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
  - Amanita Charm
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Freya''s Tears, Golden Blade, Amanita Charm, Riptalon,
    Tyrfing, Silverbranch Bow, Genji''s Guard, Kinetic Cuirass, Breastplate of Valor,
    Toxic Blade, Runeforged Hammer, Lernaean Bow, Pharaoh''s Curse, Tekko-Kagi, Shogun''s
    Ofuda, Shield Splitter, Eye of the Storm, Shield of the Phoenix, The Reaper, Avenging
    Blade, Dominance, Erosion, Eye of Providence, Screeching Gargoyle, Hydra''s Lament,
    Daybreak Gavel.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.43
      pick: 0.29
      fit: 0.31
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.57
      pick: 0.13
      fit: 0.22
    Riptalon:
      total: 0.49
      efficiency: 0.51
      win: 0.52
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.52
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
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Genji''s Guard, Breastplate
    of Valor, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Titan''s Bane,
    Screeching Gargoyle, Runeforged Hammer, Berserker''s Shield, Arondight, Gladiator''s
    Shield, Hydra''s Lament, Eye of Erebus, Pendulum Blade, Shield Splitter, Prophetic
    Cloak, Chandra''s Grace, The Crusher, Eye of the Storm, Erosion, Eye of Providence,
    Avenging Blade, Draconic Scale, Midgardian Mail, Stone of Binding, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.52
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.43
      pick: 0.29
      fit: 0.59
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.41
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.57
      pick: 0.13
      fit: 0.52
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.52
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
    Underrated for this god: Amanita Charm, Runeforged Hammer, Kinetic Cuirass, Freya''s
    Tears, Shield Splitter, Eye of the Storm, Genji''s Guard, Breastplate of Valor,
    Hydra''s Lament, Berserker''s Shield, Avenging Blade, Shield of the Phoenix, Titan''s
    Bane, The Crusher, Erosion, The Reaper, Eye of Providence, Draconic Scale, Daybreak
    Gavel, Pendulum Blade, Arondight, Midgardian Mail, Golden Blade, Screeching Gargoyle,
    Stone of Binding, Hide of the Nemean Lion, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.43
      pick: 0.29
      fit: 0.58
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.5
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.5
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.57
      pick: 0.13
      fit: 0.36
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Devourer's Gauntlet
  - Eye of the Storm
  - Runeforged Hammer
  - Freya's Tears
  flex_slots:
  - Eye of the Storm
  - Devourer's Gauntlet
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Runeforged Hammer,
    Kinetic Cuirass, Freya''s Tears, Shield Splitter, Eye of the Storm, Genji''s Guard,
    Breastplate of Valor, Hydra''s Lament, Berserker''s Shield, Avenging Blade, Shield
    of the Phoenix, Titan''s Bane, The Crusher, Erosion, The Reaper, Eye of Providence,
    Draconic Scale, Daybreak Gavel, Pendulum Blade, Arondight, Midgardian Mail, Golden
    Blade, Screeching Gargoyle, Stone of Binding, Hide of the Nemean Lion, Avatar''s
    Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.43
      pick: 0.29
      fit: 0.58
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.52
    Devourer's Gauntlet:
      total: 0.42
      efficiency: 0.29
      win: 0.58
      pick: 0.36
      fit: 0.27
    Eye of the Storm:
      total: 0.5
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.57
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.57
      pick: 0.13
      fit: 0.36
  community_ordered:
  - Jotunn's Revenge
  - Devourer's Gauntlet
  - Freya's Tears
  swaps:
  - added: Devourer's Gauntlet
    removed: Shield Splitter
    reason: community 58% win over 219 matches (vs 50% on this god), taking the model's
      weakest slot from Shield Splitter
  starter: *id001
---
