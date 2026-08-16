---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.16
  aspect_win_rate: 0.5
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.38
    win_rate: 0.42
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.18
      win_rate: 0.59
    - name: Chronos' Pendant
      pick_rate: 0.1
      win_rate: 0.5
  - name: Genji's Guard
    pick_rate: 0.19
    win_rate: 0.52
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.64
    - name: Breastplate of Valor
      pick_rate: 0.13
      win_rate: 0.47
  - name: Breastplate of Valor
    pick_rate: 0.14
    win_rate: 0.54
    alternates:
    - name: Genji's Guard
      pick_rate: 0.23
      win_rate: 0.47
    - name: Gladiator's Shield
      pick_rate: 0.05
      win_rate: 0.71
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.61
    - name: Kinetic Cuirass
      pick_rate: 0.07
      win_rate: 0.53
  - name: Hide of the Nemean Lion
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.68
    - name: Draconic Scale
      pick_rate: 0.05
      win_rate: 0.36
  - name: Veve Charm
    pick_rate: 0.07
    win_rate: 0.63
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.67
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.71
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.28
    win_rate: 0.62
  - name: Bumba's Cudgel
    pick_rate: 0.27
    win_rate: 0.44
  - name: Bluestone Brooch
    pick_rate: 0.14
    win_rate: 0.49
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-08-16'
  god_win_rate: 0.5149253731343284
  god_matches_won: 138
  god_matches_played: 268
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-16'
  god_matches_analyzed: 6103
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Gladiator's Shield
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gladiator''s Shield, Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Rod of Tahuti, Freya''s Tears, The Crusher, Jotunn''s Revenge, Gluttonous Grimoire,
    Shield Splitter, Oni Hunter''s Garb, Shield of the Phoenix, Erosion, Eye of Providence,
    Eye of the Storm, Hydra''s Lament, Spectral Armor, Pharaoh''s Curse, Nimble Ring,
    Leviathan''s Hide, Soul Gem, Midgardian Mail, Mantle Of Discord, Golden Blade,
    Stone of Binding, Avenging Blade, Death Metal, Magi''s Cloak, Ancile, Screeching
    Gargoyle, Helm of Radiance, Shogun''s Ofuda, Damaru, Void Shield, Doublet of Binding,
    Hide of the Nemean Lion, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.52
      pick: 0.26
      fit: 0.31
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.64
      win: 0.54
      pick: 0.22
      fit: 0.31
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.53
      pick: 0.12
      fit: 0.67
    Gladiator's Shield:
      total: 0.55
      efficiency: 0.41
      win: 0.71
      pick: 0.08
      fit: 0.58
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.55
      win: 0.59
      pick: 0.18
      fit: 0.48
    Amanita Charm:
      total: 0.54
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.57
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Gladiator's Shield
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gladiator''s Shield, Shield of the Phoenix, Kinetic Cuirass,
    Soul Gem, Berserker''s Shield, Rod of Tahuti, Gluttonous Grimoire, Jotunn''s Revenge,
    The Crusher, Chandra''s Grace, Rod of Asclepius, Freya''s Tears, Oni Hunter''s
    Garb, The Reaper, Eye of the Storm, Erosion, Shield Splitter, Phoenix Feather,
    Eye of Providence, Hydra''s Lament, Spectral Armor, Golden Blade, Pharaoh''s Curse,
    Avenging Blade, Leviathan''s Hide, Nimble Ring, Midgardian Mail, Blood-Bound Book,
    Lifebinder, Glorious Pridwen, Riptalon, Bancroft''s Talon, Death Metal, Ancile,
    Shogun''s Ofuda, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.52
      pick: 0.26
      fit: 0.28
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.53
      pick: 0.12
      fit: 0.66
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.8
    Gladiator's Shield:
      total: 0.56
      efficiency: 0.41
      win: 0.71
      pick: 0.08
      fit: 0.6
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.55
      win: 0.59
      pick: 0.18
      fit: 0.54
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gladiator's Shield
  - Runeforged Hammer
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Kinetic Cuirass
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, The Crusher, Gluttonous Grimoire, Jotunn''s Revenge,
    Kinetic Cuirass, Amanita Charm, Soul Gem, Stone of Binding, Berserker''s Shield,
    Avenging Blade, Screeching Gargoyle, Freya''s Tears, Void Shield, Oni Hunter''s
    Garb, The Cosmic Horror, Void Stone, The Reaper, Spear of the Magus, Shield of
    the Phoenix, Shield Splitter, Hydra''s Lament, Spear of Desolation, Nimble Ring,
    Erosion, Spectral Armor, Eye of Providence, Eye of the Storm, Pharaoh''s Curse,
    Obsidian Shard, Riptalon, Leviathan''s Hide, Midgardian Mail, Heartseeker, Golden
    Blade, Silverbranch Bow, Mantle Of Discord, Draconic Scale.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.53
      pick: 0.12
      fit: 0.52
    Gladiator's Shield:
      total: 0.54
      efficiency: 0.41
      win: 0.71
      pick: 0.08
      fit: 0.45
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.55
      win: 0.59
      pick: 0.18
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Gladiator's Shield
  - Nimble Ring
  flex_slots:
  - Genji's Guard
  - Golden Blade
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Nimble Ring, Kinetic Cuirass, Rod of Tahuti, Amanita
    Charm, Gluttonous Grimoire, Golden Blade, The Crusher, Pharaoh''s Curse, Freya''s
    Tears, Jotunn''s Revenge, Riptalon, Oni Hunter''s Garb, Shield of the Phoenix,
    Soul Gem, Shogun''s Ofuda, Tyrfing, Spectral Armor, Erosion, Hydra''s Lament,
    Lernaean Bow, Silverbranch Bow, Shield Splitter, Eye of Providence, Eye of the
    Storm, Leviathan''s Hide, Midgardian Mail, Toxic Blade, Mantle Of Discord, Stone
    of Binding, Helm of Radiance, Death Metal, Screeching Gargoyle, Yogi''s Necklace,
    Damaru, Ancile, Draconic Scale.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.52
      pick: 0.26
      fit: 0.2
    Berserker's Shield:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.53
      pick: 0.12
      fit: 0.47
    Gladiator's Shield:
      total: 0.53
      efficiency: 0.41
      win: 0.71
      pick: 0.08
      fit: 0.41
    Nimble Ring:
      total: 0.52
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.3
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gladiator's Shield
  - Freya's Tears
  flex_slots:
  - Kinetic Cuirass
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    + fit + win/pick). Underrated for this god: Gladiator''s Shield, Freya''s Tears,
    Kinetic Cuirass, Jotunn''s Revenge, Shield of the Phoenix, Rod of Tahuti, Amanita
    Charm, Soul Gem, Gluttonous Grimoire, Hydra''s Lament, Berserker''s Shield, The
    Crusher, Screeching Gargoyle, Oni Hunter''s Garb, Nimble Ring, Chandra''s Grace,
    Spear of Desolation, Erosion, Spectral Armor, Eye of Providence, Chronos'' Pendant,
    Prophetic Cloak, Shield Splitter, Pharaoh''s Curse, Eye of the Storm, Leviathan''s
    Hide, Gem of Focus, Helm of Radiance, Midgardian Mail, Mantle Of Discord, Totem
    of Death, Stone of Binding, Arondight, Death Metal, Rod of Asclepius, The Cosmic
    Horror, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.52
      pick: 0.26
      fit: 0.48
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.64
      win: 0.54
      pick: 0.22
      fit: 0.48
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.53
      pick: 0.12
      fit: 0.55
    Gladiator's Shield:
      total: 0.57
      efficiency: 0.41
      win: 0.71
      pick: 0.08
      fit: 0.71
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gladiator's Shield
  - Runeforged Hammer
  - The Crusher
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, The Crusher, Kinetic Cuirass,
    Jotunn''s Revenge, Berserker''s Shield, Amanita Charm, Gluttonous Grimoire, Freya''s
    Tears, Nimble Ring, Shield Splitter, Hydra''s Lament, Oni Hunter''s Garb, Soul
    Gem, Golden Blade, Eye of the Storm, Shield of the Phoenix, Pharaoh''s Curse,
    Erosion, Spectral Armor, Eye of Providence, The Reaper, Lernaean Bow, Death Metal,
    Avenging Blade, Damaru, The Cosmic Horror, Shogun''s Ofuda, Leviathan''s Hide,
    Midgardian Mail, Spear of the Magus, Mantle Of Discord, Stone of Binding, Tekko-Kagi,
    Spear of Desolation, Tyrfing, Riptalon, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.52
      pick: 0.26
      fit: 0.23
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.53
      pick: 0.12
      fit: 0.52
    Gladiator's Shield:
      total: 0.54
      efficiency: 0.41
      win: 0.71
      pick: 0.08
      fit: 0.45
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.55
      win: 0.59
      pick: 0.18
      fit: 0.44
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Gladiator's Shield
  - Runeforged Hammer
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - The Crusher
  - Genji's Guard
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Gluttonous Grimoire,
    Kinetic Cuirass, The Crusher, Jotunn''s Revenge, Amanita Charm, Soul Gem, Berserker''s
    Shield, Nimble Ring, Freya''s Tears, Oni Hunter''s Garb, The Cosmic Horror, Shield
    Splitter, Shield of the Phoenix, Death Metal, Spear of the Magus, Hydra''s Lament,
    Erosion, Spear of Desolation, Eye of the Storm, Helm of Radiance, Spectral Armor,
    Eye of Providence, Rod of Asclepius, Pharaoh''s Curse, The Reaper, Obsidian Shard,
    Leviathan''s Hide, Golden Blade, Jade Scepter, Midgardian Mail, Avenging Blade,
    Mantle Of Discord, Damaru, Stone of Binding, Chronos'' Pendant, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.52
      pick: 0.26
      fit: 0.23
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.53
      pick: 0.12
      fit: 0.52
    Gladiator's Shield:
      total: 0.53
      efficiency: 0.41
      win: 0.71
      pick: 0.08
      fit: 0.45
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.55
      win: 0.59
      pick: 0.18
      fit: 0.4
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Rod of Tahuti, Freya''s Tears, The Crusher, Jotunn''s Revenge, Gluttonous Grimoire,
    Shield Splitter, Oni Hunter''s Garb, Shield of the Phoenix, Erosion, Eye of Providence,
    Eye of the Storm, Draconic Scale, Hydra''s Lament, Spectral Armor, Pharaoh''s
    Curse, Nimble Ring, Leviathan''s Hide, Soul Gem, Midgardian Mail, Mantle Of Discord,
    Golden Blade, Stone of Binding, Avenging Blade, Death Metal, Magi''s Cloak, Ancile,
    Screeching Gargoyle, Helm of Radiance, Shogun''s Ofuda, Damaru, Hide of the Nemean
    Lion, Gladiator''s Shield, Void Shield, Doublet of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.52
      pick: 0.26
      fit: 0.31
    Berserker's Shield:
      total: 0.52
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.53
      pick: 0.12
      fit: 0.67
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.52
    The Crusher:
      total: 0.52
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.54
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.57
  starter: *id001
---
