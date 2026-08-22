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
    pick_rate: 0.57
    win_rate: 0.52
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.59
    - name: Runeforged Hammer
      pick_rate: 0.07
      win_rate: 0.58
  - name: Hydra's Lament
    pick_rate: 0.25
    win_rate: 0.49
    alternates:
    - name: Barbed Carver
      pick_rate: 0.16
      win_rate: 0.54
    - name: Transcendence
      pick_rate: 0.1
      win_rate: 0.58
  - name: Barbed Carver
    pick_rate: 0.11
    win_rate: 0.45
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.12
      win_rate: 0.55
    - name: The Reaper
      pick_rate: 0.1
      win_rate: 0.55
  - name: Heartseeker
    pick_rate: 0.29
    win_rate: 0.53
    alternates:
    - name: Titan's Bane
      pick_rate: 0.11
      win_rate: 0.47
    - name: The Crusher
      pick_rate: 0.05
      win_rate: 0.58
  - name: Titan's Bane
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Heartseeker
      pick_rate: 0.13
      win_rate: 0.6
    - name: Avatar's Parashu
      pick_rate: 0.04
      win_rate: 0.65
  - name: Skeggox
    pick_rate: 0.08
    win_rate: 0.57
    alternates:
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.5
    - name: Magi's Cloak
      pick_rate: 0.05
      win_rate: 0.6
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.34
    win_rate: 0.61
  - name: Bumba's Cudgel
    pick_rate: 0.22
    win_rate: 0.44
  - name: Bluestone Brooch
    pick_rate: 0.19
    win_rate: 0.63
  source_url: https://smitebrain.com/gods/thor/
  last_verified: '2026-08-22'
  god_win_rate: 0.5421293272371
  god_matches_won: 830
  god_matches_played: 1531
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-22'
  god_matches_analyzed: 14126
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Runeforged Hammer, Amanita Charm, Kinetic Cuirass, Berserker''s
    Shield, Shield Splitter, Eye of the Storm, Golden Blade, Freya''s Tears, Avenging
    Blade, Genji''s Guard, Breastplate of Valor, Shield of the Phoenix, Spectral Armor,
    Tekko-Kagi, Erosion, Tyrfing, Mantle Of Discord, Eye of Providence, Stone of Binding,
    Draconic Scale, Leviathan''s Hide, Lernaean Bow, Pharaoh''s Curse.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.52
      pick: 0.57
      fit: 0.55
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.55
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.07
      fit: 0.58
    The Crusher:
      total: 0.56
      efficiency: 0.57
      win: 0.58
      pick: 0.08
      fit: 0.61
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.56
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
  - The Crusher
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: The
    Crusher, Runeforged Hammer, Genji''s Guard, Amanita Charm, Breastplate of Valor,
    Berserker''s Shield, Kinetic Cuirass, Freya''s Tears, Shield Splitter, Transcendence,
    Shield of the Phoenix, Eye of the Storm, Golden Blade, Avenging Blade, Spectral
    Armor, Mantle Of Discord, Stone of Binding, Lernaean Bow, Tyrfing, Arondight,
    Daybreak Gavel, Tekko-Kagi, Leviathan''s Hide, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.52
      pick: 0.57
      fit: 0.53
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.58
      pick: 0.14
      fit: 0.29
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.57
      win: 0.58
      pick: 0.07
      fit: 0.42
    The Crusher:
      total: 0.53
      efficiency: 0.57
      win: 0.58
      pick: 0.08
      fit: 0.45
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.53
      pick: 0.48
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Runeforged Hammer
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Crusher, Amanita Charm, Berserker''s Shield, Kinetic Cuirass, Runeforged
    Hammer, Genji''s Guard, Breastplate of Valor, Freya''s Tears, Shield of the Phoenix,
    Shield Splitter, Eye of the Storm, Golden Blade, Pendulum Blade, Tekko-Kagi, Silverbranch
    Bow, Spectral Armor, Screeching Gargoyle, Mantle Of Discord, Stone of Binding,
    Avenging Blade, Toxic Blade, Riptalon, Daybreak Gavel, Arondight.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.19
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.52
      pick: 0.57
      fit: 0.56
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.37
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.57
      win: 0.58
      pick: 0.07
      fit: 0.37
    The Crusher:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.08
      fit: 0.5
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.56
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
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Berserker''s
    Shield, Runeforged Hammer, The Crusher, Shield Splitter, Eye of the Storm, Freya''s
    Tears, Phoenix Feather, Golden Blade, Riptalon, Erosion, Genji''s Guard, Eye of
    Providence, Breastplate of Valor, Spectral Armor, Yogi''s Necklace, Draconic Scale,
    Mantle Of Discord, Stone of Binding, Avenging Blade, Chandra''s Grace, Leviathan''s
    Hide, Pharaoh''s Curse.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.38
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.52
      pick: 0.57
      fit: 0.45
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.65
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.72
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.59
      pick: 0.16
      fit: 0.55
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - The Crusher
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - The Reaper
  - Transcendence
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
    for this god: The Crusher, Avatar''s Parashu, Avenging Blade, Runeforged Hammer,
    Amanita Charm, Stone of Binding, Kinetic Cuirass, Berserker''s Shield, Tekko-Kagi,
    Void Shield, Screeching Gargoyle, Silverbranch Bow, Shield Splitter, Toxic Blade,
    Void Stone, Riptalon, Eye of the Storm, Freya''s Tears, Genji''s Guard, Golden
    Blade, Breastplate of Valor, Pendulum Blade, Shield of the Phoenix, Spectral Armor.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.52
      pick: 0.57
      fit: 0.66
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.58
      pick: 0.14
      fit: 0.23
    The Reaper:
      total: 0.54
      efficiency: 0.55
      win: 0.55
      pick: 0.16
      fit: 0.62
    The Crusher:
      total: 0.57
      efficiency: 0.57
      win: 0.58
      pick: 0.08
      fit: 0.72
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.53
      pick: 0.48
      fit: 0.82
    Avatar's Parashu:
      total: 0.55
      efficiency: 0.45
      win: 0.65
      pick: 0.09
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Riptalon
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Golden Blade, Amanita Charm, Riptalon, Kinetic
    Cuirass, The Crusher, Tyrfing, Silverbranch Bow, Runeforged Hammer, Pharaoh''s
    Curse, Toxic Blade, Lernaean Bow, Shogun''s Ofuda, Genji''s Guard, Breastplate
    of Valor, Tekko-Kagi, Freya''s Tears, Shield Splitter, Shield of the Phoenix,
    Spectral Armor, Mantle Of Discord, Stone of Binding, Eye of the Storm, Dominance,
    Daybreak Gavel.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.62
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.52
      pick: 0.57
      fit: 0.27
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.36
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.26
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Freya''s Tears, Shield of the Phoenix, Amanita Charm, Kinetic Cuirass, Berserker''s
    Shield, The Crusher, Runeforged Hammer, Screeching Gargoyle, Arondight, Chandra''s
    Grace, Gladiator''s Shield, Pendulum Blade, Eye of Erebus, Shield Splitter, Prophetic
    Cloak, Spectral Armor, Mantle Of Discord, Stone of Binding, Eye of the Storm,
    Golden Blade, Daybreak Gavel, Leviathan''s Hide, Erosion.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.44
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.52
      pick: 0.57
      fit: 0.6
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.4
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.56
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
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, The Crusher, Berserker''s
    Shield, Runeforged Hammer, Shield Splitter, Eye of the Storm, Golden Blade, Freya''s
    Tears, Avenging Blade, Genji''s Guard, Breastplate of Valor, Shield of the Phoenix,
    Spectral Armor, Tekko-Kagi, Erosion, Tyrfing, Mantle Of Discord, Eye of Providence,
    Stone of Binding, Draconic Scale, Leviathan''s Hide, Lernaean Bow, Pharaoh''s
    Curse.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.52
      pick: 0.57
      fit: 0.55
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.55
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.07
      fit: 0.58
    The Crusher:
      total: 0.56
      efficiency: 0.57
      win: 0.58
      pick: 0.08
      fit: 0.61
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.45
  starter: *id001
---
