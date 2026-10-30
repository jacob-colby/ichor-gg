---
type: smite-build
god: Ravana
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rakshasa King
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.55
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.6
    win_rate: 0.52
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.18
      win_rate: 0.45
    - name: Transcendence
      pick_rate: 0.06
      win_rate: 0.49
  - name: Sanguine Lash
    pick_rate: 0.27
    win_rate: 0.57
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.49
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 0.47
  - name: Kinetic Cuirass
    pick_rate: 0.15
    win_rate: 0.58
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.09
      win_rate: 0.48
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.56
  - name: Freya's Tears
    pick_rate: 0.18
    win_rate: 0.52
    alternates:
    - name: Heartseeker
      pick_rate: 0.1
      win_rate: 0.47
    - name: Kinetic Cuirass
      pick_rate: 0.1
      win_rate: 0.53
  - name: Hide of the Nemean Lion
    pick_rate: 0.06
    win_rate: 0.38
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.63
    - name: Heartseeker
      pick_rate: 0.06
      win_rate: 0.64
  - name: Medal of Defense
    pick_rate: 0.06
    win_rate: 0.54
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.08
      win_rate: 0.53
    - name: Freya's Tears
      pick_rate: 0.04
      win_rate: 0.47
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.24
    win_rate: 0.57
  - name: Hunter's Cowl
    pick_rate: 0.23
    win_rate: 0.56
  - name: Leather Cowl
    pick_rate: 0.17
    win_rate: 0.4
  source_url: https://smitebrain.com/gods/ravana/
  last_verified: '2026-10-30'
  god_win_rate: 0.4847682119205298
  god_matches_won: 366
  god_matches_played: 755
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-30'
  god_matches_analyzed: 10706
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Runeforged Hammer
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Runeforged Hammer, Shield Splitter, Eye of the Storm,
    Genji''s Guard, Breastplate of Valor, Hydra''s Lament, Avenging Blade, Berserker''s
    Shield, Shield of the Phoenix, Titan''s Bane, The Crusher, Erosion, The Reaper,
    Eye of Providence, Draconic Scale, Daybreak Gavel, Pendulum Blade, Arondight,
    Midgardian Mail, Golden Blade, Screeching Gargoyle, Stone of Binding, Avatar''s
    Parashu, Hide of the Nemean Lion.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.45
      pick: 0.18
      fit: 0.58
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.58
      pick: 0.23
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
      total: 0.52
      efficiency: 0.61
      win: 0.52
      pick: 0.3
      fit: 0.36
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
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
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Amanita
    Charm, Genji''s Guard, Breastplate of Valor, Hydra''s Lament, Runeforged Hammer,
    Shield Splitter, Eye of the Storm, Berserker''s Shield, Avenging Blade, Titan''s
    Bane, The Crusher, Shield of the Phoenix, Transcendence, Daybreak Gavel, The Reaper,
    Arondight, Screeching Gargoyle, Erosion, Eye of Providence, Oni Hunter''s Garb,
    Stone of Binding, Draconic Scale, Pendulum Blade, Midgardian Mail, Hide of the
    Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.25
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.45
      pick: 0.18
      fit: 0.52
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.58
      pick: 0.23
      fit: 0.37
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.52
      pick: 0.3
      fit: 0.25
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.27
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
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
  - Genji's Guard
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
    god: Amanita Charm, Genji''s Guard, Breastplate of Valor, Runeforged Hammer, Hydra''s
    Lament, Shield of the Phoenix, Titan''s Bane, Shield Splitter, Berserker''s Shield,
    The Crusher, Eye of the Storm, The Reaper, Pendulum Blade, Avenging Blade, Screeching
    Gargoyle, Daybreak Gavel, Arondight, Erosion, Eye of Providence, Draconic Scale,
    Avatar''s Parashu, Stone of Binding, Midgardian Mail, Leviathan''s Hide, Hide
    of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.45
      pick: 0.18
      fit: 0.56
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.58
      pick: 0.23
      fit: 0.39
    Transcendence:
      total: 0.43
      efficiency: 0.53
      win: 0.49
      pick: 0.06
      fit: 0.16
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.52
      pick: 0.3
      fit: 0.32
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.29
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
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
  - Shield of the Phoenix
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
    this god: Amanita Charm, Shield of the Phoenix, Runeforged Hammer, The Reaper,
    Shield Splitter, Genji''s Guard, Breastplate of Valor, Eye of the Storm, Berserker''s
    Shield, Erosion, Yogi''s Necklace, Eye of Providence, Hydra''s Lament, Draconic
    Scale, Phoenix Feather, Avenging Blade, Chandra''s Grace, Glorious Pridwen, Stone
    of Binding, Midgardian Mail, Titan''s Bane, Daybreak Gavel, The Crusher, Magi''s
    Cloak, Hide of the Nemean Lion.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.45
      pick: 0.18
      fit: 0.49
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.58
      pick: 0.23
      fit: 0.61
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.53
      win: 0.49
      pick: 0.0
      fit: 0.76
    Shifter's Shield:
      total: 0.5
      efficiency: 0.55
      win: 0.49
      pick: 0.15
      fit: 0.51
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.52
      pick: 0.3
      fit: 0.42
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.49
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
  - Kinetic Cuirass
  - Freya's Tears
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Heartseeker
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
    for this god: Avenging Blade, Amanita Charm, Screeching Gargoyle, Titan''s Bane,
    Runeforged Hammer, Stone of Binding, The Crusher, Void Shield, The Reaper, Genji''s
    Guard, Breastplate of Valor, Void Stone, Hydra''s Lament, Shield Splitter, Pendulum
    Blade, Eye of the Storm, Avatar''s Parashu, Berserker''s Shield, Shield of the
    Phoenix, Daybreak Gavel, Tekko-Kagi, Erosion, Eye of Providence, Draconic Scale,
    Arondight.'
  slot_scores:
    Avenging Blade:
      total: 0.51
      efficiency: 0.49
      win: 0.49
      pick: 0.0
      fit: 0.75
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.45
      pick: 0.18
      fit: 0.67
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.58
      pick: 0.23
      fit: 0.43
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.52
      pick: 0.3
      fit: 0.28
    Heartseeker:
      total: 0.5
      efficiency: 0.47
      win: 0.47
      pick: 0.17
      fit: 0.77
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.33
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Golden Blade, Amanita Charm, Riptalon, Tyrfing,
    Silverbranch Bow, Genji''s Guard, Breastplate of Valor, Toxic Blade, Runeforged
    Hammer, Lernaean Bow, Pharaoh''s Curse, Tekko-Kagi, The Reaper, Shogun''s Ofuda,
    Hydra''s Lament, Shield Splitter, Eye of the Storm, Shield of the Phoenix, Daybreak
    Gavel, Avenging Blade, Dominance, Erosion, Eye of Providence, Screeching Gargoyle.'
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
      win: 0.47
      pick: 0.14
      fit: 0.4
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.45
      pick: 0.18
      fit: 0.31
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.58
      pick: 0.23
      fit: 0.36
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.52
      pick: 0.3
      fit: 0.22
    Riptalon:
      total: 0.48
      efficiency: 0.51
      win: 0.49
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
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
  - Breastplate of Valor
  - Amanita Charm
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Screeching Gargoyle, Runeforged
    Hammer, Arondight, Berserker''s Shield, Gladiator''s Shield, Eye of Erebus, Pendulum
    Blade, Shield Splitter, Prophetic Cloak, Chandra''s Grace, Eye of the Storm, Daybreak
    Gavel, Erosion, Eye of Providence, Avenging Blade, Draconic Scale, Midgardian
    Mail, Stone of Binding, Titan''s Bane, The Crusher.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.49
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.45
      pick: 0.18
      fit: 0.59
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.58
      pick: 0.23
      fit: 0.41
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.52
      pick: 0.3
      fit: 0.52
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.31
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
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
    Underrated for this god: Amanita Charm, Runeforged Hammer, Shield Splitter, Eye
    of the Storm, Genji''s Guard, Breastplate of Valor, Hydra''s Lament, Berserker''s
    Shield, Avenging Blade, Shield of the Phoenix, Titan''s Bane, The Crusher, Erosion,
    The Reaper, Eye of Providence, Draconic Scale, Daybreak Gavel, Pendulum Blade,
    Arondight, Midgardian Mail, Golden Blade, Screeching Gargoyle, Stone of Binding,
    Hide of the Nemean Lion, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.45
      pick: 0.18
      fit: 0.58
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.58
      pick: 0.23
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
      total: 0.52
      efficiency: 0.61
      win: 0.52
      pick: 0.3
      fit: 0.36
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.49
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Eye of the Storm
  - Runeforged Hammer
  - Sanguine Lash
  - Freya's Tears
  flex_slots:
  - Eye of the Storm
  - Sanguine Lash
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
    Shield Splitter, Eye of the Storm, Genji''s Guard, Breastplate of Valor, Hydra''s
    Lament, Berserker''s Shield, Avenging Blade, Shield of the Phoenix, Titan''s Bane,
    The Crusher, Erosion, The Reaper, Eye of Providence, Draconic Scale, Daybreak
    Gavel, Pendulum Blade, Arondight, Midgardian Mail, Golden Blade, Screeching Gargoyle,
    Stone of Binding, Hide of the Nemean Lion, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.45
      pick: 0.18
      fit: 0.58
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.58
      pick: 0.23
      fit: 0.52
    Eye of the Storm:
      total: 0.49
      efficiency: 0.52
      win: 0.49
      pick: 0.0
      fit: 0.57
    Runeforged Hammer:
      total: 0.5
      efficiency: 0.57
      win: 0.49
      pick: 0.0
      fit: 0.55
    Sanguine Lash:
      total: 0.47
      efficiency: 0.36
      win: 0.57
      pick: 0.37
      fit: 0.48
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.52
      pick: 0.3
      fit: 0.36
  community_ordered:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Sanguine Lash
  - Freya's Tears
  swaps:
  - added: Sanguine Lash
    removed: Shield Splitter
    reason: community 57% win over 204 matches (vs 48% on this god), taking the model's
      weakest slot from Shield Splitter
  starter: *id001
---
