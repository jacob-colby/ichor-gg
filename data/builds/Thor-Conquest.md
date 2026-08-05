---
type: smite-build
god: Thor
mode: Conquest
builds:
- source: community
  aspect: Aspect of Thunderstruck
  aspect_pick_rate: 0.31
  aspect_win_rate: 0.54
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.55
    win_rate: 0.55
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.53
    - name: Hydra's Lament
      pick_rate: 0.08
      win_rate: 0.49
  - name: Hydra's Lament
    pick_rate: 0.24
    win_rate: 0.56
    alternates:
    - name: Barbed Carver
      pick_rate: 0.12
      win_rate: 0.57
    - name: Transcendence
      pick_rate: 0.12
      win_rate: 0.53
  - name: Barbed Carver
    pick_rate: 0.12
    win_rate: 0.49
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.13
      win_rate: 0.45
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.6
  - name: Heartseeker
    pick_rate: 0.22
    win_rate: 0.53
    alternates:
    - name: Titan's Bane
      pick_rate: 0.17
      win_rate: 0.62
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.47
  - name: Titan's Bane
    pick_rate: 0.13
    win_rate: 0.45
    alternates:
    - name: Heartseeker
      pick_rate: 0.16
      win_rate: 0.61
    - name: Lucerne Hammer
      pick_rate: 0.08
      win_rate: 0.42
  - name: Skeggox
    pick_rate: 0.06
    win_rate: 0.61
    alternates:
    - name: Titan's Bane
      pick_rate: 0.07
      win_rate: 0.55
    - name: Lucerne Hammer
      pick_rate: 0.06
      win_rate: 0.47
  source_url: https://smitebrain.com/gods/thor/
  last_verified: '2026-08-01'
  god_win_rate: 0.5449640287769785
  god_matches_won: 303
  god_matches_played: 556
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Amanita Charm, Runeforged Hammer, Berserker''s Shield,
    Kinetic Cuirass, Eye of Providence, Eye of the Storm, Genji''s Guard, Oni Hunter''s
    Garb, Shield Splitter, Avenging Blade, Golden Blade, The Reaper, Spectral Armor,
    Lernaean Bow, Shield of the Phoenix, Breastplate of Valor, Yogi''s Necklace, Erosion,
    Damaru, Freya''s Tears, Pharaoh''s Curse, Draconic Scale, Leviathan''s Hide, Wyrmskin
    Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.66
      win: 0.55
      pick: 0.55
      fit: 0.55
    Hydra's Lament:
      total: 0.54
      efficiency: 0.61
      win: 0.56
      pick: 0.24
      fit: 0.44
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.58
    The Crusher:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.61
    Amanita Charm:
      total: 0.53
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    god: The Crusher, Genji''s Guard, Berserker''s Shield, Amanita Charm, Kinetic
    Cuirass, Runeforged Hammer, Breastplate of Valor, Eye of Providence, Oni Hunter''s
    Garb, Shield of the Phoenix, Freya''s Tears, The Reaper, Yogi''s Necklace, Avenging
    Blade, Shield Splitter, Eye of the Storm, Spectral Armor, Golden Blade, Pendulum
    Blade, Lernaean Bow, Pharaoh''s Curse, Damaru, Riptalon, Chandra''s Grace, Erosion.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.24
    Berserker's Shield:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.19
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.66
      win: 0.55
      pick: 0.55
      fit: 0.56
    Hydra's Lament:
      total: 0.54
      efficiency: 0.61
      win: 0.56
      pick: 0.24
      fit: 0.42
    The Crusher:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.5
    Amanita Charm:
      total: 0.5
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hydra's Lament
  - Amanita Charm
  flex_slots:
  - Hydra's Lament
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Berserker''s
    Shield, The Crusher, Eye of Providence, The Reaper, Runeforged Hammer, Oni Hunter''s
    Garb, Genji''s Guard, Eye of the Storm, Shield Splitter, Chandra''s Grace, Erosion,
    Phoenix Feather, Spectral Armor, Avenging Blade, Riptalon, Golden Blade, Freya''s
    Tears, Draconic Scale, Pharaoh''s Curse, Breastplate of Valor, Yogi''s Necklace,
    Leviathan''s Hide, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.38
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.55
      pick: 0.55
      fit: 0.45
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.65
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.72
    Hydra's Lament:
      total: 0.53
      efficiency: 0.61
      win: 0.56
      pick: 0.24
      fit: 0.38
    Amanita Charm:
      total: 0.59
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  flex_slots:
  - Heartseeker
  - The Reaper
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Avenging Blade, The Reaper, Amanita Charm, Berserker''s
    Shield, Runeforged Hammer, Kinetic Cuirass, Eye of Providence, Genji''s Guard,
    Oni Hunter''s Garb, Void Shield, Stone of Binding, Tekko-Kagi, Eye of the Storm,
    Riptalon, Shield Splitter, Screeching Gargoyle, Void Stone, Golden Blade, Pendulum
    Blade, Silverbranch Bow, Breastplate of Valor, Yogi''s Necklace, Lernaean Bow,
    Titan''s Bane.'
  slot_scores:
    Avenging Blade:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.77
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.66
      win: 0.55
      pick: 0.55
      fit: 0.66
    Hydra's Lament:
      total: 0.53
      efficiency: 0.61
      win: 0.56
      pick: 0.24
      fit: 0.36
    The Reaper:
      total: 0.51
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.62
    The Crusher:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.72
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.53
      pick: 0.22
      fit: 0.72
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - Riptalon
  - The Crusher
  flex_slots:
  - Riptalon
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Berserker''s Shield, Golden Blade, Riptalon, The Crusher, Amanita Charm,
    Silverbranch Bow, Kinetic Cuirass, Pharaoh''s Curse, Genji''s Guard, Lernaean
    Bow, Tyrfing, Runeforged Hammer, Eye of Providence, Oni Hunter''s Garb, Shogun''s
    Ofuda, Toxic Blade, Breastplate of Valor, Yogi''s Necklace, Dominance, The Reaper,
    Spectral Armor, Tekko-Kagi, Shield of the Phoenix, Avenging Blade, Freya''s Tears,
    Shield Splitter.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.62
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.55
      pick: 0.55
      fit: 0.27
    Hydra's Lament:
      total: 0.52
      efficiency: 0.61
      win: 0.56
      pick: 0.24
      fit: 0.25
    Riptalon:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.59
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Hydra's Lament
  - Freya's Tears
  flex_slots:
  - Shield of the Phoenix
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Shield of the Phoenix, Freya''s Tears, The Crusher, Berserker''s Shield, Amanita
    Charm, Kinetic Cuirass, Eye of Providence, Runeforged Hammer, Oni Hunter''s Garb,
    Chandra''s Grace, Screeching Gargoyle, Gladiator''s Shield, Arondight, Yogi''s
    Necklace, Pendulum Blade, Spectral Armor, Pharaoh''s Curse, Eye of the Storm,
    Shield Splitter, Avenging Blade, Prophetic Cloak, Erosion, Golden Blade, Leviathan''s
    Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.44
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.66
      win: 0.55
      pick: 0.55
      fit: 0.6
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.56
    Hydra's Lament:
      total: 0.56
      efficiency: 0.61
      win: 0.56
      pick: 0.24
      fit: 0.56
    Freya's Tears:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.53
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, Amanita Charm, Runeforged Hammer, Berserker''s
    Shield, Kinetic Cuirass, Eye of Providence, Eye of the Storm, Genji''s Guard,
    Oni Hunter''s Garb, Shield Splitter, Avenging Blade, Golden Blade, The Reaper,
    Spectral Armor, Lernaean Bow, Shield of the Phoenix, Breastplate of Valor, Yogi''s
    Necklace, Erosion, Damaru, Freya''s Tears, Pharaoh''s Curse, Draconic Scale, Leviathan''s
    Hide, Wyrmskin Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.66
      win: 0.55
      pick: 0.55
      fit: 0.55
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.55
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.58
    The Crusher:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.61
    Amanita Charm:
      total: 0.53
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: *id001
---
