---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.14
  aspect_win_rate: 0.51
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.4
    win_rate: 0.53
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.19
      win_rate: 0.56
    - name: Chronos' Pendant
      pick_rate: 0.07
      win_rate: 0.48
  - name: Genji's Guard
    pick_rate: 0.2
    win_rate: 0.48
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.65
    - name: Breastplate of Valor
      pick_rate: 0.14
      win_rate: 0.57
  - name: Breastplate of Valor
    pick_rate: 0.14
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.21
      win_rate: 0.58
    - name: Gladiator's Shield
      pick_rate: 0.06
      win_rate: 0.51
  - name: Shell of Rebuke
    pick_rate: 0.1
    win_rate: 0.66
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.6
    - name: Breastplate of Valor
      pick_rate: 0.06
      win_rate: 0.55
  - name: Hide of the Nemean Lion
    pick_rate: 0.08
    win_rate: 0.41
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.72
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.85
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.47
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.73
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.69
  community_starters:
  - name: Bumba's Cudgel
    pick_rate: 0.31
    win_rate: 0.45
  - name: Bumba's Hammer
    pick_rate: 0.28
    win_rate: 0.66
  - name: Bluestone Brooch
    pick_rate: 0.1
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-08-21'
  god_win_rate: 0.537261698440208
  god_matches_won: 310
  god_matches_played: 577
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-21'
  god_matches_analyzed: 12786
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Runeforged Hammer
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Rod of Tahuti, The Crusher, Jotunn''s Revenge, Gluttonous Grimoire, Shield Splitter,
    Oni Hunter''s Garb, Shield of the Phoenix, Erosion, Eye of Providence, Eye of
    the Storm, Draconic Scale, Hydra''s Lament, Spectral Armor, Pharaoh''s Curse,
    Nimble Ring, Leviathan''s Hide, Soul Gem, Midgardian Mail, Mantle Of Discord,
    Golden Blade, Stone of Binding, Avenging Blade, Death Metal, Magi''s Cloak, Ancile,
    Screeching Gargoyle, Helm of Radiance, Shogun''s Ofuda, Damaru, Void Shield, Doublet
    of Binding, Wyrmskin Hide, Gladiator''s Shield.'
  slot_scores:
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
      pick: 0.0
      fit: 0.67
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.55
      win: 0.56
      pick: 0.19
      fit: 0.48
    Freya's Tears:
      total: 0.67
      efficiency: 0.59
      win: 0.85
      pick: 0.13
      fit: 0.52
    Shifter's Shield:
      total: 0.53
      efficiency: 0.52
      win: 0.53
      pick: 0.4
      fit: 0.57
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
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Runeforged Hammer
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass,
    Soul Gem, Berserker''s Shield, Rod of Tahuti, Gluttonous Grimoire, Jotunn''s Revenge,
    The Crusher, Chandra''s Grace, Ethereal Staff, Rod of Asclepius, Yogi''s Necklace,
    Oni Hunter''s Garb, The Reaper, Eye of the Storm, Erosion, Shield Splitter, Phoenix
    Feather, Eye of Providence, Hydra''s Lament, Spectral Armor, Draconic Scale, Golden
    Blade, Pharaoh''s Curse, Avenging Blade, Leviathan''s Hide, Nimble Ring, Midgardian
    Mail, Blood-Bound Book, Lifebinder, Glorious Pridwen, Riptalon, Bancroft''s Talon,
    Death Metal, Ancile, Shogun''s Ofuda.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.8
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.55
      win: 0.56
      pick: 0.19
      fit: 0.54
    Freya's Tears:
      total: 0.66
      efficiency: 0.59
      win: 0.85
      pick: 0.13
      fit: 0.46
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
  - Runeforged Hammer
  - Freya's Tears
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
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Freya''s Tears, Rod of Tahuti, The Crusher, Gluttonous Grimoire,
    Jotunn''s Revenge, Kinetic Cuirass, Amanita Charm, Soul Gem, Stone of Binding,
    Berserker''s Shield, Avenging Blade, Screeching Gargoyle, Void Shield, Oni Hunter''s
    Garb, The Cosmic Horror, Void Stone, The Reaper, Spear of the Magus, Shield of
    the Phoenix, Shield Splitter, Obsidian Shard, Hydra''s Lament, Spear of Desolation,
    Nimble Ring, Erosion, Heartseeker, Spectral Armor, Eye of Providence, Eye of the
    Storm, Titan''s Bane, Draconic Scale, Pharaoh''s Curse, Riptalon, Leviathan''s
    Hide, Midgardian Mail, Golden Blade, Silverbranch Bow, Mantle Of Discord.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.52
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.55
      win: 0.56
      pick: 0.19
      fit: 0.38
    Freya's Tears:
      total: 0.65
      efficiency: 0.59
      win: 0.85
      pick: 0.13
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
  - Berserker's Shield
  - Kinetic Cuirass
  - Nimble Ring
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Berserker''s Shield, Nimble Ring, Rod of Tahuti, Kinetic
    Cuirass, Amanita Charm, Gluttonous Grimoire, Golden Blade, The Crusher, Pharaoh''s
    Curse, Jotunn''s Revenge, Riptalon, Oni Hunter''s Garb, Shield of the Phoenix,
    Soul Gem, Shogun''s Ofuda, Tyrfing, Spectral Armor, Erosion, Hydra''s Lament,
    Lernaean Bow, Silverbranch Bow, Shield Splitter, Eye of Providence, Draconic Scale,
    Eye of the Storm, Leviathan''s Hide, Dominance, Midgardian Mail, Toxic Blade,
    Mantle Of Discord, Stone of Binding, Helm of Radiance, Death Metal, Screeching
    Gargoyle, Yogi''s Necklace, Damaru, Ancile.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.54
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
      pick: 0.0
      fit: 0.47
    Nimble Ring:
      total: 0.52
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.64
      efficiency: 0.59
      win: 0.85
      pick: 0.13
      fit: 0.33
    Amanita Charm:
      total: 0.51
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.37
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
  - Kinetic Cuirass
  - Shield of the Phoenix
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Jotunn''s Revenge,
    Kinetic Cuirass, Shield of the Phoenix, Rod of Tahuti, Amanita Charm, Soul Gem,
    Gluttonous Grimoire, Hydra''s Lament, Berserker''s Shield, The Crusher, Screeching
    Gargoyle, Oni Hunter''s Garb, Nimble Ring, Chandra''s Grace, Spear of Desolation,
    Erosion, Gladiator''s Shield, Spectral Armor, Eye of Providence, Prophetic Cloak,
    Totem of Death, Shield Splitter, Draconic Scale, Pharaoh''s Curse, Chronos'' Pendant,
    Eye of the Storm, Leviathan''s Hide, Gem of Focus, Helm of Radiance, Midgardian
    Mail, Mantle Of Discord, Stone of Binding, Arondight, Ethereal Staff, Death Metal,
    Rod of Asclepius, The Cosmic Horror.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.48
      pick: 0.27
      fit: 0.48
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.64
      win: 0.53
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
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.69
      efficiency: 0.59
      win: 0.85
      pick: 0.13
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Freya''s Tears, Rod of Tahuti, The Crusher,
    Jotunn''s Revenge, Kinetic Cuirass, Berserker''s Shield, Amanita Charm, Gluttonous
    Grimoire, Nimble Ring, Shield Splitter, Hydra''s Lament, Oni Hunter''s Garb, Soul
    Gem, Golden Blade, Eye of the Storm, Shield of the Phoenix, Pharaoh''s Curse,
    Erosion, Spectral Armor, Eye of Providence, The Reaper, Lernaean Bow, Draconic
    Scale, Death Metal, Avenging Blade, Damaru, The Cosmic Horror, Shogun''s Ofuda,
    Leviathan''s Hide, Heartseeker, Midgardian Mail, Spear of the Magus, Dominance,
    Titan''s Bane, Mantle Of Discord, Stone of Binding, Obsidian Shard, Tekko-Kagi.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.65
      efficiency: 0.59
      win: 0.85
      pick: 0.13
      fit: 0.38
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.52
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Jotunn's Revenge
  - Runeforged Hammer
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Rod of Tahuti, Gluttonous
    Grimoire, The Crusher, Kinetic Cuirass, Jotunn''s Revenge, Amanita Charm, Soul
    Gem, Berserker''s Shield, Nimble Ring, Oni Hunter''s Garb, The Cosmic Horror,
    Shield Splitter, Shield of the Phoenix, Death Metal, Spear of the Magus, Hydra''s
    Lament, Obsidian Shard, Erosion, Spear of Desolation, Eye of the Storm, Helm of
    Radiance, Spectral Armor, Eye of Providence, Ethereal Staff, Draconic Scale, Rod
    of Asclepius, Pharaoh''s Curse, The Reaper, Leviathan''s Hide, Golden Blade, Jade
    Scepter, Midgardian Mail, Avenging Blade, Mantle Of Discord, Damaru, Stone of
    Binding, Chronos'' Pendant.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.52
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.55
      win: 0.56
      pick: 0.19
      fit: 0.4
    Freya's Tears:
      total: 0.65
      efficiency: 0.59
      win: 0.85
      pick: 0.13
      fit: 0.38
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
    Screeching Gargoyle, Helm of Radiance, Shogun''s Ofuda, Damaru, Gladiator''s Shield,
    Void Shield, Doublet of Binding, Wyrmskin Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.48
      pick: 0.27
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
      pick: 0.0
      fit: 0.67
    Freya's Tears:
      total: 0.67
      efficiency: 0.59
      win: 0.85
      pick: 0.13
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
