---
type: smite-build
god: Ravana
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rakshasa King
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.15
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.33
    win_rate: 0.57
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.3
      win_rate: 0.44
    - name: Daybreak Gavel
      pick_rate: 0.08
      win_rate: 0.44
  - name: Shifter's Shield
    pick_rate: 0.15
    win_rate: 0.47
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.11
      win_rate: 0.63
    - name: Barbed Carver
      pick_rate: 0.08
      win_rate: 0.45
  - name: The Reaper
    pick_rate: 0.09
    win_rate: 0.52
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.09
      win_rate: 0.47
    - name: The Crusher
      pick_rate: 0.09
      win_rate: 0.58
  - name: Heartseeker
    pick_rate: 0.14
    win_rate: 0.4
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.61
    - name: Genji's Guard
      pick_rate: 0.05
      win_rate: 0.43
  - name: Hide of the Nemean Lion
    pick_rate: 0.06
    win_rate: 0.52
    alternates:
    - name: Heartseeker
      pick_rate: 0.06
      win_rate: 0.61
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.61
  - name: Titan's Bane
    pick_rate: 0.05
    win_rate: 0.6
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.71
    - name: Avatar's Parashu
      pick_rate: 0.04
      win_rate: 0.67
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.26
    win_rate: 0.55
  - name: Bumba's Cudgel
    pick_rate: 0.2
    win_rate: 0.38
  - name: Hunter's Cowl
    pick_rate: 0.2
    win_rate: 0.62
  source_url: https://smitebrain.com/gods/ravana/
  last_verified: '2026-09-28'
  god_win_rate: 0.5
  god_matches_won: 259
  god_matches_played: 518
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-28'
  god_matches_analyzed: 7013
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Titan's Bane
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Freya''s Tears, Avatar''s Parashu, Amanita Charm, The Crusher, Runeforged
    Hammer, Kinetic Cuirass, Shield Splitter, Eye of the Storm, Breastplate of Valor,
    Hydra''s Lament, Berserker''s Shield, Avenging Blade, Shield of the Phoenix, The
    Reaper, Erosion, Eye of Providence, Draconic Scale, Pendulum Blade, Arondight,
    Hide of the Nemean Lion, Midgardian Mail, Golden Blade, Genji''s Guard, Screeching
    Gargoyle, Stone of Binding, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.44
      pick: 0.3
      fit: 0.58
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.61
      pick: 0.12
      fit: 0.36
    The Crusher:
      total: 0.52
      efficiency: 0.47
      win: 0.58
      pick: 0.14
      fit: 0.55
    Titan's Bane:
      total: 0.53
      efficiency: 0.47
      win: 0.6
      pick: 0.15
      fit: 0.55
    Avatar's Parashu:
      total: 0.53
      efficiency: 0.45
      win: 0.67
      pick: 0.12
      fit: 0.45
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Breastplate of Valor
  - Hydra's Lament
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Freya''s
    Tears, Amanita Charm, Breastplate of Valor, The Crusher, Hydra''s Lament, Runeforged
    Hammer, Kinetic Cuirass, Shield Splitter, Eye of the Storm, Berserker''s Shield,
    Avenging Blade, The Reaper, Genji''s Guard, Shield of the Phoenix, Transcendence,
    Arondight, Screeching Gargoyle, Erosion, Eye of Providence, Oni Hunter''s Garb,
    Hide of the Nemean Lion, Stone of Binding, Draconic Scale, Pendulum Blade, Midgardian
    Mail, Daybreak Gavel.'
  slot_scores:
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.44
      pick: 0.3
      fit: 0.52
    Hydra's Lament:
      total: 0.5
      efficiency: 0.54
      win: 0.52
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.61
      pick: 0.12
      fit: 0.25
    Titan's Bane:
      total: 0.51
      efficiency: 0.47
      win: 0.6
      pick: 0.15
      fit: 0.44
    Avatar's Parashu:
      total: 0.52
      efficiency: 0.45
      win: 0.67
      pick: 0.12
      fit: 0.34
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - The Crusher
  - Amanita Charm
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Freya''s Tears, Avatar''s Parashu, The Crusher, Amanita Charm, Breastplate
    of Valor, Runeforged Hammer, Kinetic Cuirass, Hydra''s Lament, Berserker''s Shield,
    Shield of the Phoenix, The Reaper, Shield Splitter, Eye of the Storm, Pendulum
    Blade, Avenging Blade, Genji''s Guard, Screeching Gargoyle, Arondight, Erosion,
    Eye of Providence, Hide of the Nemean Lion, Draconic Scale, Stone of Binding,
    Midgardian Mail, Leviathan''s Hide, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.44
      pick: 0.3
      fit: 0.56
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.61
      pick: 0.12
      fit: 0.32
    The Crusher:
      total: 0.51
      efficiency: 0.47
      win: 0.58
      pick: 0.14
      fit: 0.5
    Titan's Bane:
      total: 0.52
      efficiency: 0.47
      win: 0.6
      pick: 0.15
      fit: 0.5
    Avatar's Parashu:
      total: 0.53
      efficiency: 0.45
      win: 0.67
      pick: 0.12
      fit: 0.4
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.29
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
  - Titan's Bane
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
  - Kinetic Cuirass
  - Avatar's Parashu
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
    The Reaper, Runeforged Hammer, Shield Splitter, The Crusher, Breastplate of Valor,
    Eye of the Storm, Berserker''s Shield, Erosion, Yogi''s Necklace, Eye of Providence,
    Hydra''s Lament, Draconic Scale, Phoenix Feather, Avenging Blade, Chandra''s Grace,
    Glorious Pridwen, Hide of the Nemean Lion, Stone of Binding, Midgardian Mail,
    Magi''s Cloak, Genji''s Guard, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.44
      pick: 0.3
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
      total: 0.56
      efficiency: 0.61
      win: 0.61
      pick: 0.12
      fit: 0.42
    Avatar's Parashu:
      total: 0.52
      efficiency: 0.45
      win: 0.67
      pick: 0.12
      fit: 0.38
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.52
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
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - The Crusher
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    for this god: Avatar''s Parashu, Freya''s Tears, The Crusher, Avenging Blade,
    Amanita Charm, The Reaper, Screeching Gargoyle, Runeforged Hammer, Stone of Binding,
    Kinetic Cuirass, Void Shield, Breastplate of Valor, Void Stone, Hydra''s Lament,
    Shield Splitter, Pendulum Blade, Eye of the Storm, Berserker''s Shield, Shield
    of the Phoenix, Tekko-Kagi, Erosion, Eye of Providence, Draconic Scale, Genji''s
    Guard, Arondight, Daybreak Gavel.'
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
      win: 0.44
      pick: 0.3
      fit: 0.67
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.61
      pick: 0.12
      fit: 0.28
    The Crusher:
      total: 0.53
      efficiency: 0.47
      win: 0.58
      pick: 0.14
      fit: 0.67
    Titan's Bane:
      total: 0.54
      efficiency: 0.47
      win: 0.6
      pick: 0.15
      fit: 0.67
    Avatar's Parashu:
      total: 0.55
      efficiency: 0.45
      win: 0.67
      pick: 0.12
      fit: 0.57
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - The Crusher
  - Titan's Bane
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
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Riptalon
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Freya''s Tears, Golden Blade, Amanita Charm, Riptalon,
    Tyrfing, Silverbranch Bow, Kinetic Cuirass, Breastplate of Valor, Toxic Blade,
    Runeforged Hammer, Lernaean Bow, The Reaper, Pharaoh''s Curse, Tekko-Kagi, Shogun''s
    Ofuda, Hydra''s Lament, Shield Splitter, Eye of the Storm, Shield of the Phoenix,
    Avenging Blade, Dominance, Erosion, Eye of Providence, Genji''s Guard, Screeching
    Gargoyle, Daybreak Gavel.'
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
      total: 0.51
      efficiency: 0.72
      win: 0.44
      pick: 0.3
      fit: 0.31
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.61
      pick: 0.12
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
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Hydra's Lament
  - Avatar's Parashu
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
    + fit + win/pick). Underrated for this god: Freya''s Tears, Breastplate of Valor,
    Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Kinetic Cuirass, Genji''s
    Guard, Screeching Gargoyle, The Crusher, Runeforged Hammer, Berserker''s Shield,
    Arondight, Gladiator''s Shield, Eye of Erebus, Pendulum Blade, Shield Splitter,
    Prophetic Cloak, Chandra''s Grace, Eye of the Storm, Erosion, Eye of Providence,
    Avenging Blade, Draconic Scale, Midgardian Mail, Stone of Binding, Daybreak Gavel.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.44
      pick: 0.3
      fit: 0.59
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.52
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.61
      pick: 0.12
      fit: 0.52
    Avatar's Parashu:
      total: 0.5
      efficiency: 0.45
      win: 0.67
      pick: 0.12
      fit: 0.24
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.52
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
    Hydra''s Lament, Berserker''s Shield, Avenging Blade, Shield of the Phoenix, The
    Crusher, Erosion, The Reaper, Eye of Providence, Draconic Scale, Daybreak Gavel,
    Pendulum Blade, Arondight, Midgardian Mail, Golden Blade, Screeching Gargoyle,
    Stone of Binding, Hide of the Nemean Lion, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.44
      pick: 0.3
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
      total: 0.55
      efficiency: 0.61
      win: 0.61
      pick: 0.12
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
---
