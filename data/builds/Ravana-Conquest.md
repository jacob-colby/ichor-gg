---
type: smite-build
god: Ravana
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rakshasa King
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.17
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.3
    win_rate: 0.56
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.29
      win_rate: 0.47
    - name: Daybreak Gavel
      pick_rate: 0.09
      win_rate: 0.42
  - name: Shifter's Shield
    pick_rate: 0.16
    win_rate: 0.5
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.09
      win_rate: 0.63
    - name: Barbed Carver
      pick_rate: 0.08
      win_rate: 0.39
  - name: Sanguine Lash
    pick_rate: 0.1
    win_rate: 0.47
    alternates:
    - name: The Crusher
      pick_rate: 0.09
      win_rate: 0.62
    - name: The Reaper
      pick_rate: 0.09
      win_rate: 0.5
  - name: Heartseeker
    pick_rate: 0.14
    win_rate: 0.41
    alternates:
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.65
    - name: Genji's Guard
      pick_rate: 0.05
      win_rate: 0.5
  - name: Hide of the Nemean Lion
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Heartseeker
      pick_rate: 0.07
      win_rate: 0.64
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.61
  - name: Titan's Bane
    pick_rate: 0.05
    win_rate: 0.67
    alternates:
    - name: Lucerne Hammer
      pick_rate: 0.05
      win_rate: 0.55
    - name: Avatar's Parashu
      pick_rate: 0.05
      win_rate: 0.7
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.26
    win_rate: 0.58
  - name: Bumba's Cudgel
    pick_rate: 0.2
    win_rate: 0.36
  - name: Hunter's Cowl
    pick_rate: 0.18
    win_rate: 0.64
  source_url: https://smitebrain.com/gods/ravana/
  last_verified: '2026-09-27'
  god_win_rate: 0.5124378109452736
  god_matches_won: 206
  god_matches_played: 402
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-27'
  god_matches_analyzed: 5610
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
  - The Crusher
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, The Crusher, Amanita Charm, Runeforged Hammer, Kinetic
    Cuirass, Genji''s Guard, Shield Splitter, Eye of the Storm, Breastplate of Valor,
    Hydra''s Lament, Berserker''s Shield, Avenging Blade, Shield of the Phoenix, The
    Reaper, Erosion, Eye of Providence, Draconic Scale, Pendulum Blade, Arondight,
    Hide of the Nemean Lion, Midgardian Mail, Golden Blade, Screeching Gargoyle, Stone
    of Binding, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.47
      pick: 0.29
      fit: 0.58
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.61
      pick: 0.11
      fit: 0.36
    The Crusher:
      total: 0.53
      efficiency: 0.47
      win: 0.62
      pick: 0.14
      fit: 0.55
    Titan's Bane:
      total: 0.56
      efficiency: 0.47
      win: 0.67
      pick: 0.15
      fit: 0.55
    Avatar's Parashu:
      total: 0.55
      efficiency: 0.45
      win: 0.7
      pick: 0.15
      fit: 0.45
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
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
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
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
    Tears, The Crusher, Genji''s Guard, Amanita Charm, Breastplate of Valor, Hydra''s
    Lament, Runeforged Hammer, Kinetic Cuirass, Shield Splitter, Eye of the Storm,
    Berserker''s Shield, Avenging Blade, The Reaper, Shield of the Phoenix, Transcendence,
    Arondight, Screeching Gargoyle, Erosion, Eye of Providence, Oni Hunter''s Garb,
    Hide of the Nemean Lion, Stone of Binding, Draconic Scale, Pendulum Blade, Midgardian
    Mail, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.08
      fit: 0.25
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.47
      pick: 0.29
      fit: 0.52
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.61
      pick: 0.11
      fit: 0.25
    Titan's Bane:
      total: 0.54
      efficiency: 0.47
      win: 0.67
      pick: 0.15
      fit: 0.44
    Avatar's Parashu:
      total: 0.53
      efficiency: 0.45
      win: 0.7
      pick: 0.15
      fit: 0.34
  community_ordered:
  - Genji's Guard
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Freya''s Tears, The Crusher, Amanita Charm, Genji''s Guard, Breastplate of
    Valor, Runeforged Hammer, Kinetic Cuirass, Hydra''s Lament, Berserker''s Shield,
    Shield of the Phoenix, The Reaper, Shield Splitter, Eye of the Storm, Pendulum
    Blade, Avenging Blade, Screeching Gargoyle, Arondight, Erosion, Eye of Providence,
    Hide of the Nemean Lion, Draconic Scale, Stone of Binding, Midgardian Mail, Leviathan''s
    Hide, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.47
      pick: 0.29
      fit: 0.56
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.61
      pick: 0.11
      fit: 0.32
    The Crusher:
      total: 0.52
      efficiency: 0.47
      win: 0.62
      pick: 0.14
      fit: 0.5
    Titan's Bane:
      total: 0.55
      efficiency: 0.47
      win: 0.67
      pick: 0.15
      fit: 0.5
    Avatar's Parashu:
      total: 0.54
      efficiency: 0.45
      win: 0.7
      pick: 0.15
      fit: 0.4
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.5
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
  - Shield of the Phoenix
  - Freya's Tears
  - Titan's Bane
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Avatar's Parashu
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Shield of the Phoenix, The Crusher, Kinetic
    Cuirass, The Reaper, Runeforged Hammer, Genji''s Guard, Shield Splitter, Breastplate
    of Valor, Eye of the Storm, Berserker''s Shield, Erosion, Yogi''s Necklace, Eye
    of Providence, Hydra''s Lament, Draconic Scale, Phoenix Feather, Avenging Blade,
    Chandra''s Grace, Glorious Pridwen, Hide of the Nemean Lion, Stone of Binding,
    Midgardian Mail, Magi''s Cloak, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.47
      pick: 0.29
      fit: 0.49
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.76
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.61
      pick: 0.11
      fit: 0.42
    Titan's Bane:
      total: 0.55
      efficiency: 0.47
      win: 0.67
      pick: 0.15
      fit: 0.48
    Avatar's Parashu:
      total: 0.54
      efficiency: 0.45
      win: 0.7
      pick: 0.15
      fit: 0.38
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.81
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
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
  - Freya's Tears
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
    for this god: The Crusher, Freya''s Tears, Avenging Blade, Amanita Charm, The
    Reaper, Screeching Gargoyle, Runeforged Hammer, Stone of Binding, Genji''s Guard,
    Kinetic Cuirass, Void Shield, Breastplate of Valor, Void Stone, Hydra''s Lament,
    Shield Splitter, Pendulum Blade, Eye of the Storm, Berserker''s Shield, Shield
    of the Phoenix, Tekko-Kagi, Erosion, Eye of Providence, Draconic Scale, Arondight,
    Daybreak Gavel.'
  slot_scores:
    Avenging Blade:
      total: 0.51
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.75
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.47
      pick: 0.29
      fit: 0.67
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.61
      pick: 0.11
      fit: 0.28
    The Crusher:
      total: 0.55
      efficiency: 0.47
      win: 0.62
      pick: 0.14
      fit: 0.67
    Titan's Bane:
      total: 0.58
      efficiency: 0.47
      win: 0.67
      pick: 0.15
      fit: 0.67
    Avatar's Parashu:
      total: 0.57
      efficiency: 0.45
      win: 0.7
      pick: 0.15
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
  - Titan's Bane
  flex_slots:
  - Golden Blade
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
    this god: Freya''s Tears, Berserker''s Shield, Golden Blade, Amanita Charm, Riptalon,
    Genji''s Guard, Tyrfing, Silverbranch Bow, Kinetic Cuirass, Breastplate of Valor,
    Toxic Blade, Runeforged Hammer, Lernaean Bow, The Reaper, Pharaoh''s Curse, Tekko-Kagi,
    Shogun''s Ofuda, Hydra''s Lament, Shield Splitter, Eye of the Storm, Shield of
    the Phoenix, Avenging Blade, Dominance, Erosion, Eye of Providence, Screeching
    Gargoyle, Daybreak Gavel.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.47
      pick: 0.29
      fit: 0.31
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.61
      pick: 0.11
      fit: 0.22
    Riptalon:
      total: 0.49
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.55
    Titan's Bane:
      total: 0.52
      efficiency: 0.47
      win: 0.67
      pick: 0.15
      fit: 0.33
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Breastplate of Valor
  - Avatar's Parashu
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Genji''s Guard, Breastplate
    of Valor, The Crusher, Amanita Charm, Hydra''s Lament, Shield of the Phoenix,
    Kinetic Cuirass, Screeching Gargoyle, Runeforged Hammer, Berserker''s Shield,
    Arondight, Gladiator''s Shield, Eye of Erebus, Pendulum Blade, Shield Splitter,
    Prophetic Cloak, Chandra''s Grace, Eye of the Storm, Erosion, Eye of Providence,
    Avenging Blade, Draconic Scale, Midgardian Mail, Stone of Binding, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.08
      fit: 0.43
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.47
      pick: 0.29
      fit: 0.59
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.61
      pick: 0.11
      fit: 0.52
    Titan's Bane:
      total: 0.53
      efficiency: 0.47
      win: 0.67
      pick: 0.15
      fit: 0.34
    Avatar's Parashu:
      total: 0.52
      efficiency: 0.45
      win: 0.7
      pick: 0.15
      fit: 0.24
  community_ordered:
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
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
    Stone of Binding, Hide of the Nemean Lion.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.47
      pick: 0.29
      fit: 0.58
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.5
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.61
      pick: 0.11
      fit: 0.36
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Freya's Tears
  starter: *id001
---
