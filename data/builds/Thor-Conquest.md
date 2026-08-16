---
type: smite-build
god: Thor
mode: Conquest
builds:
- source: community
  aspect: Aspect of Thunderstruck
  aspect_pick_rate: 0.28
  aspect_win_rate: 0.58
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.6
    win_rate: 0.52
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.57
    - name: Runeforged Hammer
      pick_rate: 0.06
      win_rate: 0.62
  - name: Hydra's Lament
    pick_rate: 0.25
    win_rate: 0.48
    alternates:
    - name: Barbed Carver
      pick_rate: 0.17
      win_rate: 0.52
    - name: Transcendence
      pick_rate: 0.1
      win_rate: 0.59
  - name: Barbed Carver
    pick_rate: 0.12
    win_rate: 0.45
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.11
      win_rate: 0.54
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.59
  - name: Heartseeker
    pick_rate: 0.26
    win_rate: 0.49
    alternates:
    - name: Titan's Bane
      pick_rate: 0.14
      win_rate: 0.5
    - name: Shifter's Shield
      pick_rate: 0.05
      win_rate: 0.68
  - name: Titan's Bane
    pick_rate: 0.12
    win_rate: 0.49
    alternates:
    - name: Heartseeker
      pick_rate: 0.13
      win_rate: 0.57
    - name: The Crusher
      pick_rate: 0.05
      win_rate: 0.7
  - name: Lucerne Hammer
    pick_rate: 0.07
    win_rate: 0.56
    alternates:
    - name: Skeggox
      pick_rate: 0.06
      win_rate: 0.57
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.63
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.33
    win_rate: 0.6
  - name: Bumba's Cudgel
    pick_rate: 0.22
    win_rate: 0.44
  - name: Bluestone Brooch
    pick_rate: 0.18
    win_rate: 0.72
  source_url: https://smitebrain.com/gods/thor/
  last_verified: '2026-08-16'
  god_win_rate: 0.5475409836065573
  god_matches_won: 334
  god_matches_played: 610
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-16'
  god_matches_analyzed: 6103
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Runeforged Hammer, Kinetic Cuirass, Amanita Charm, Genji''s
    Guard, Berserker''s Shield, Eye of the Storm, Shield Splitter, Oni Hunter''s Garb,
    The Reaper, Golden Blade, Shifter''s Shield, Avenging Blade, Shield of the Phoenix,
    Freya''s Tears, Spectral Armor, Breastplate of Valor, Erosion, Eye of Providence,
    Damaru, Draconic Scale, Pharaoh''s Curse, Leviathan''s Hide, Midgardian Mail,
    Lernaean Bow, Wyrmskin Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.59
      pick: 0.12
      fit: 0.18
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.52
      pick: 0.6
      fit: 0.55
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.55
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.55
      win: 0.62
      pick: 0.06
      fit: 0.58
    The Crusher:
      total: 0.64
      efficiency: 0.64
      win: 0.7
      pick: 0.11
      fit: 0.61
    Amanita Charm:
      total: 0.54
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.45
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
  - Runeforged Hammer
  - The Crusher
  flex_slots:
  - Breastplate of Valor
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: The
    Crusher, Genji''s Guard, Runeforged Hammer, Breastplate of Valor, Kinetic Cuirass,
    Amanita Charm, Berserker''s Shield, Oni Hunter''s Garb, Freya''s Tears, Transcendence,
    Shield of the Phoenix, Eye of the Storm, The Reaper, Shield Splitter, Golden Blade,
    Damaru, Spectral Armor, Avenging Blade, Shifter''s Shield, Yogi''s Necklace, Lernaean
    Bow, Erosion, Pharaoh''s Curse, Leviathan''s Hide, Chandra''s Grace, Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.59
      pick: 0.12
      fit: 0.26
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.52
      pick: 0.6
      fit: 0.53
    Transcendence:
      total: 0.5
      efficiency: 0.52
      win: 0.59
      pick: 0.14
      fit: 0.29
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.55
      win: 0.62
      pick: 0.06
      fit: 0.42
    The Crusher:
      total: 0.61
      efficiency: 0.64
      win: 0.7
      pick: 0.11
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Runeforged Hammer
  - The Crusher
  flex_slots:
  - Kinetic Cuirass
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    god: The Crusher, Genji''s Guard, Runeforged Hammer, Kinetic Cuirass, Amanita
    Charm, Breastplate of Valor, Berserker''s Shield, Freya''s Tears, Shield of the
    Phoenix, Oni Hunter''s Garb, The Reaper, Spectral Armor, Eye of the Storm, Shifter''s
    Shield, Pendulum Blade, Shield Splitter, Golden Blade, Chandra''s Grace, Avenging
    Blade, Damaru, Screeching Gargoyle, Riptalon, Erosion, Pharaoh''s Curse, Eye of
    Providence, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.59
      pick: 0.12
      fit: 0.24
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.52
      pick: 0.6
      fit: 0.56
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.37
    Transcendence:
      total: 0.48
      efficiency: 0.52
      win: 0.59
      pick: 0.14
      fit: 0.16
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.55
      win: 0.62
      pick: 0.06
      fit: 0.37
    The Crusher:
      total: 0.62
      efficiency: 0.64
      win: 0.7
      pick: 0.11
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass,
    Runeforged Hammer, The Reaper, Genji''s Guard, Berserker''s Shield, Oni Hunter''s
    Garb, Shifter''s Shield, Eye of the Storm, Chandra''s Grace, Shield Splitter,
    Erosion, Phoenix Feather, Freya''s Tears, Eye of Providence, Spectral Armor, Riptalon,
    Draconic Scale, Breastplate of Valor, Golden Blade, Avenging Blade, Pharaoh''s
    Curse, Leviathan''s Hide, Midgardian Mail, Ancile.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.52
      pick: 0.6
      fit: 0.45
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.65
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.72
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.55
      win: 0.62
      pick: 0.06
      fit: 0.55
    The Crusher:
      total: 0.62
      efficiency: 0.64
      win: 0.7
      pick: 0.11
      fit: 0.51
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Runeforged Hammer
  - The Crusher
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
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Runeforged Hammer, Avenging Blade, Genji''s Guard,
    The Reaper, Kinetic Cuirass, Amanita Charm, Berserker''s Shield, Void Shield,
    Stone of Binding, Screeching Gargoyle, Oni Hunter''s Garb, Tekko-Kagi, Void Stone,
    Riptalon, Eye of the Storm, Breastplate of Valor, Shield Splitter, Pendulum Blade,
    Silverbranch Bow, Freya''s Tears, Golden Blade, Shield of the Phoenix, Spectral
    Armor, Damaru.'
  slot_scores:
    Avenging Blade:
      total: 0.54
      efficiency: 0.48
      win: 0.57
      pick: 0.0
      fit: 0.77
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.59
      pick: 0.12
      fit: 0.14
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.64
      win: 0.52
      pick: 0.6
      fit: 0.66
    Transcendence:
      total: 0.49
      efficiency: 0.52
      win: 0.59
      pick: 0.14
      fit: 0.23
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.55
      win: 0.62
      pick: 0.06
      fit: 0.47
    The Crusher:
      total: 0.65
      efficiency: 0.64
      win: 0.7
      pick: 0.11
      fit: 0.72
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Riptalon
  - The Crusher
  flex_slots:
  - Genji's Guard
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Berserker''s Shield, Golden Blade, Riptalon, Genji''s Guard,
    Runeforged Hammer, Kinetic Cuirass, Amanita Charm, Silverbranch Bow, Pharaoh''s
    Curse, Tyrfing, Lernaean Bow, Toxic Blade, Oni Hunter''s Garb, Shogun''s Ofuda,
    Breastplate of Valor, Freya''s Tears, The Reaper, Spectral Armor, Shield of the
    Phoenix, Shifter''s Shield, Tekko-Kagi, Eye of the Storm, Erosion, Shield Splitter,
    Dominance, Eros'' Bow.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.62
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.59
      pick: 0.12
      fit: 0.1
    Berserker's Shield:
      total: 0.55
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.52
      pick: 0.6
      fit: 0.27
    Riptalon:
      total: 0.53
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.59
    The Crusher:
      total: 0.6
      efficiency: 0.64
      win: 0.7
      pick: 0.11
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Freya's Tears
  - The Crusher
  flex_slots:
  - Freya's Tears
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: The Crusher, Genji''s Guard, Breastplate
    of Valor, Freya''s Tears, Shield of the Phoenix, Runeforged Hammer, Kinetic Cuirass,
    Amanita Charm, Berserker''s Shield, Chandra''s Grace, Screeching Gargoyle, Oni
    Hunter''s Garb, Gladiator''s Shield, Arondight, Spectral Armor, Shifter''s Shield,
    Pendulum Blade, Prophetic Cloak, Erosion, Eye of the Storm, Pharaoh''s Curse,
    Eye of Providence, Leviathan''s Hide, Shield Splitter, Midgardian Mail, Golden
    Blade, The Reaper.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.59
      pick: 0.12
      fit: 0.44
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.64
      win: 0.52
      pick: 0.6
      fit: 0.6
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.53
    The Crusher:
      total: 0.6
      efficiency: 0.64
      win: 0.7
      pick: 0.11
      fit: 0.35
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
  - Runeforged Hammer
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, Kinetic Cuirass, Amanita Charm, Runeforged
    Hammer, Berserker''s Shield, Genji''s Guard, Eye of the Storm, Shield Splitter,
    Oni Hunter''s Garb, The Reaper, Golden Blade, Avenging Blade, Shield of the Phoenix,
    Freya''s Tears, Spectral Armor, Breastplate of Valor, Erosion, Shifter''s Shield,
    Eye of Providence, Damaru, Draconic Scale, Pharaoh''s Curse, Leviathan''s Hide,
    Midgardian Mail, Lernaean Bow, Wyrmskin Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.52
      pick: 0.6
      fit: 0.55
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.55
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.55
      win: 0.62
      pick: 0.06
      fit: 0.58
    The Crusher:
      total: 0.64
      efficiency: 0.64
      win: 0.7
      pick: 0.11
      fit: 0.61
    Amanita Charm:
      total: 0.54
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.45
  starter: *id001
---
