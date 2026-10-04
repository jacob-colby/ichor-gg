---
type: smite-build
god: Ravana
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rakshasa King
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.31
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.5
    win_rate: 0.57
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.24
      win_rate: 0.49
    - name: Daybreak Gavel
      pick_rate: 0.05
      win_rate: 0.47
  - name: Sanguine Lash
    pick_rate: 0.23
    win_rate: 0.61
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.48
    - name: Barbed Carver
      pick_rate: 0.07
      win_rate: 0.48
  - name: Shifter's Shield
    pick_rate: 0.09
    win_rate: 0.64
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.13
      win_rate: 0.54
    - name: The Reaper
      pick_rate: 0.07
      win_rate: 0.57
  - name: Heartseeker
    pick_rate: 0.12
    win_rate: 0.45
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.59
    - name: Gluttonous Grimoire
      pick_rate: 0.06
      win_rate: 0.54
  - name: Hide of the Nemean Lion
    pick_rate: 0.07
    win_rate: 0.52
    alternates:
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.71
    - name: Heartseeker
      pick_rate: 0.05
      win_rate: 0.53
  - name: Shell of Rebuke
    pick_rate: 0.04
    win_rate: 0.62
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.61
    - name: Axe
      pick_rate: 0.04
      win_rate: 0.69
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.29
    win_rate: 0.65
  - name: Bumba's Hammer
    pick_rate: 0.22
    win_rate: 0.59
  - name: Bumba's Cudgel
    pick_rate: 0.15
    win_rate: 0.42
  source_url: https://smitebrain.com/gods/ravana/
  last_verified: '2026-10-04'
  god_win_rate: 0.5375722543352601
  god_matches_won: 651
  god_matches_played: 1211
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-10-04'
  god_matches_analyzed: 14293
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
  - Shifter's Shield
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
    this god: Shifter''s Shield, Amanita Charm, Runeforged Hammer, Kinetic Cuirass,
    Shield Splitter, Eye of the Storm, Genji''s Guard, Breastplate of Valor, Hydra''s
    Lament, Berserker''s Shield, Avenging Blade, Shield of the Phoenix, Titan''s Bane,
    The Reaper, The Crusher, Erosion, Eye of Providence, Draconic Scale, Pendulum
    Blade, Arondight, Midgardian Mail, Golden Blade, Screeching Gargoyle, Stone of
    Binding, Avatar''s Parashu, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.49
      pick: 0.24
      fit: 0.58
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.52
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.59
      pick: 0.15
      fit: 0.36
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.64
      pick: 0.14
      fit: 0.42
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
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
  - Shifter's Shield
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Shifter''s
    Shield, Amanita Charm, Genji''s Guard, Breastplate of Valor, Hydra''s Lament,
    Runeforged Hammer, Kinetic Cuirass, Shield Splitter, Eye of the Storm, Berserker''s
    Shield, Avenging Blade, Titan''s Bane, The Reaper, The Crusher, Shield of the
    Phoenix, Transcendence, Arondight, Screeching Gargoyle, Erosion, Eye of Providence,
    Oni Hunter''s Garb, Stone of Binding, Draconic Scale, Pendulum Blade, Midgardian
    Mail, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.25
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.49
      pick: 0.24
      fit: 0.52
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.59
      pick: 0.15
      fit: 0.25
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.64
      pick: 0.14
      fit: 0.27
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.27
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Shifter's Shield
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
    god: Shifter''s Shield, Amanita Charm, Genji''s Guard, Breastplate of Valor, Runeforged
    Hammer, Kinetic Cuirass, Hydra''s Lament, Berserker''s Shield, Shield of the Phoenix,
    Titan''s Bane, Shield Splitter, The Reaper, The Crusher, Eye of the Storm, Pendulum
    Blade, Avenging Blade, Screeching Gargoyle, Arondight, Erosion, Eye of Providence,
    Draconic Scale, Avatar''s Parashu, Stone of Binding, Midgardian Mail, Leviathan''s
    Hide, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.49
      pick: 0.24
      fit: 0.56
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.16
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.59
      pick: 0.15
      fit: 0.32
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.64
      pick: 0.14
      fit: 0.29
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.29
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
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
    this god: Amanita Charm, Shifter''s Shield, Shield of the Phoenix, Kinetic Cuirass,
    The Reaper, Runeforged Hammer, Shield Splitter, Genji''s Guard, Breastplate of
    Valor, Eye of the Storm, Berserker''s Shield, Erosion, Yogi''s Necklace, Eye of
    Providence, Hydra''s Lament, Draconic Scale, Phoenix Feather, Avenging Blade,
    Chandra''s Grace, Glorious Pridwen, Stone of Binding, Midgardian Mail, Titan''s
    Bane, The Crusher, Magi''s Cloak, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.49
      pick: 0.24
      fit: 0.49
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.61
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.76
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.59
      pick: 0.15
      fit: 0.42
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.64
      pick: 0.14
      fit: 0.51
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.81
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Avenging Blade
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Avenging Blade, Shifter''s Shield, Amanita Charm, Screeching Gargoyle,
    Titan''s Bane, Runeforged Hammer, Stone of Binding, The Reaper, The Crusher, Kinetic
    Cuirass, Void Shield, Genji''s Guard, Breastplate of Valor, Void Stone, Hydra''s
    Lament, Shield Splitter, Pendulum Blade, Eye of the Storm, Berserker''s Shield,
    Avatar''s Parashu, Shield of the Phoenix, Tekko-Kagi, Erosion, Eye of Providence,
    Draconic Scale, Arondight, Daybreak Gavel.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.52
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.59
    Avenging Blade:
      total: 0.54
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.75
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.49
      pick: 0.24
      fit: 0.67
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.59
      pick: 0.15
      fit: 0.28
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.64
      pick: 0.14
      fit: 0.33
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.33
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
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
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Golden Blade, Shifter''s Shield, Amanita Charm,
    Riptalon, Tyrfing, Silverbranch Bow, Genji''s Guard, Kinetic Cuirass, Breastplate
    of Valor, Toxic Blade, Runeforged Hammer, Lernaean Bow, The Reaper, Pharaoh''s
    Curse, Tekko-Kagi, Shogun''s Ofuda, Hydra''s Lament, Shield Splitter, Eye of the
    Storm, Shield of the Phoenix, Avenging Blade, Dominance, Erosion, Eye of Providence,
    Screeching Gargoyle, Daybreak Gavel.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.49
      pick: 0.24
      fit: 0.31
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.64
      pick: 0.14
      fit: 0.26
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.26
  community_ordered:
  - Jotunn's Revenge
  - Shifter's Shield
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
  - Shifter's Shield
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Shifter''s Shield, Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Kinetic
    Cuirass, Screeching Gargoyle, Runeforged Hammer, Berserker''s Shield, Arondight,
    Gladiator''s Shield, Eye of Erebus, Pendulum Blade, Shield Splitter, Prophetic
    Cloak, Chandra''s Grace, Eye of the Storm, Erosion, Eye of Providence, Avenging
    Blade, Draconic Scale, Midgardian Mail, Stone of Binding, Titan''s Bane, The Crusher,
    Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.49
      pick: 0.24
      fit: 0.59
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.59
      pick: 0.15
      fit: 0.52
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.64
      pick: 0.14
      fit: 0.31
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.31
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
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
    Underrated for this god: Amanita Charm, Runeforged Hammer, Kinetic Cuirass, Shield
    Splitter, Eye of the Storm, Genji''s Guard, Breastplate of Valor, Hydra''s Lament,
    Shifter''s Shield, Berserker''s Shield, Avenging Blade, Shield of the Phoenix,
    Titan''s Bane, The Crusher, Erosion, The Reaper, Eye of Providence, Draconic Scale,
    Daybreak Gavel, Pendulum Blade, Arondight, Midgardian Mail, Golden Blade, Screeching
    Gargoyle, Stone of Binding, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.49
      pick: 0.24
      fit: 0.58
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.52
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.5
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.59
      pick: 0.15
      fit: 0.36
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
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
  - Eye of the Storm
  - Runeforged Hammer
  - Sanguine Lash
  - Shifter's Shield
  flex_slots:
  - Shifter's Shield
  - Sanguine Lash
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Runeforged Hammer,
    Kinetic Cuirass, Shield Splitter, Eye of the Storm, Genji''s Guard, Breastplate
    of Valor, Hydra''s Lament, Shifter''s Shield, Berserker''s Shield, Avenging Blade,
    Shield of the Phoenix, Titan''s Bane, The Crusher, Erosion, The Reaper, Eye of
    Providence, Draconic Scale, Daybreak Gavel, Pendulum Blade, Arondight, Midgardian
    Mail, Golden Blade, Screeching Gargoyle, Stone of Binding, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.49
      pick: 0.24
      fit: 0.58
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.52
    Eye of the Storm:
      total: 0.52
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.57
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.55
    Sanguine Lash:
      total: 0.49
      efficiency: 0.36
      win: 0.61
      pick: 0.31
      fit: 0.48
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.64
      pick: 0.14
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Sanguine Lash
  - Shifter's Shield
  swaps:
  - added: Sanguine Lash
    removed: Shield Splitter
    reason: community 61% win over 279 matches (vs 54% on this god), taking the model's
      weakest slot from Shield Splitter
  - added: Shifter's Shield
    removed: Freya's Tears
    reason: community 64% win over 109 matches (vs 54% on this god), taking the model's
      weakest slot from Freya's Tears
  starter: *id001
---
