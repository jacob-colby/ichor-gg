---
type: smite-build
god: Artio
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Denmother
  aspect_pick_rate: 0.29
  aspect_win_rate: 0.69
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.23
    win_rate: 0.38
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.13
      win_rate: 0.59
    - name: Yogi's Necklace
      pick_rate: 0.12
      win_rate: 0.73
  - name: Genji's Guard
    pick_rate: 0.18
    win_rate: 0.48
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.64
    - name: Breastplate of Valor
      pick_rate: 0.11
      win_rate: 0.21
  - name: Breastplate of Valor
    pick_rate: 0.14
    win_rate: 0.76
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.5
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.46
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.5
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.11
      win_rate: 0.67
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.33
  - name: Freya's Tears
    pick_rate: 0.05
    win_rate: 0.8
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.33
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.8
  - name: Legionnaire Armor
    pick_rate: 0.11
    win_rate: 0.67
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.5
    - name: Draconic Scale
      pick_rate: 0.08
      win_rate: 1.0
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.38
    win_rate: 0.33
  - name: Bluestone Brooch
    pick_rate: 0.25
    win_rate: 0.61
  - name: Selflessness
    pick_rate: 0.13
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/artio/
  last_verified: '2026-08-15'
  god_win_rate: 0.5079365079365079
  god_matches_won: 64
  god_matches_played: 126
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-15'
  god_matches_analyzed: 4746
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Rod of Tahuti
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Kinetic Cuirass, Amanita Charm, Rod of Tahuti, Berserker''s
    Shield, Jotunn''s Revenge, The Crusher, Gluttonous Grimoire, Shield Splitter,
    Shield of the Phoenix, Oni Hunter''s Garb, Runeforged Hammer, Erosion, Eye of
    the Storm, Eye of Providence, Hydra''s Lament, Spectral Armor, Nimble Ring, Soul
    Gem, Pharaoh''s Curse, Leviathan''s Hide, Golden Blade, Midgardian Mail, Avenging
    Blade, Mantle Of Discord, Death Metal, Stone of Binding, Ancile, Damaru, Screeching
    Gargoyle, Magi''s Cloak, Helm of Radiance, Shogun''s Ofuda, Gladiator''s Shield,
    Hide of the Nemean Lion, Void Shield, Doublet of Binding.'
  slot_scores:
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.64
      win: 0.76
      pick: 0.22
      fit: 0.31
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.59
      win: 0.7
      pick: 0.0
      fit: 0.66
    Freya's Tears:
      total: 0.65
      efficiency: 0.59
      win: 0.8
      pick: 0.11
      fit: 0.5
    Draconic Scale:
      total: 0.72
      efficiency: 0.5
      win: 1.0
      pick: 0.25
      fit: 0.56
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.77
      win: 0.7
      pick: 0.0
      fit: 0.11
    Amanita Charm:
      total: 0.62
      efficiency: 0.63
      win: 0.7
      pick: 0.0
      fit: 0.56
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Shield of the Phoenix, Kinetic Cuirass,
    Soul Gem, Berserker''s Shield, Rod of Tahuti, Gluttonous Grimoire, Jotunn''s Revenge,
    The Crusher, Chandra''s Grace, Rod of Asclepius, Runeforged Hammer, Oni Hunter''s
    Garb, The Reaper, Eye of the Storm, Erosion, Shield Splitter, Phoenix Feather,
    Eye of Providence, Hydra''s Lament, Spectral Armor, Golden Blade, Pharaoh''s Curse,
    Leviathan''s Hide, Avenging Blade, Nimble Ring, Midgardian Mail, Blood-Bound Book,
    Lifebinder, Glorious Pridwen, Riptalon, Bancroft''s Talon, Death Metal, Ancile,
    Shogun''s Ofuda, Gladiator''s Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.64
      win: 0.76
      pick: 0.22
      fit: 0.28
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.59
      win: 0.7
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.63
      efficiency: 0.57
      win: 0.7
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.64
      efficiency: 0.59
      win: 0.8
      pick: 0.11
      fit: 0.46
    Draconic Scale:
      total: 0.72
      efficiency: 0.5
      win: 1.0
      pick: 0.25
      fit: 0.56
    Amanita Charm:
      total: 0.66
      efficiency: 0.63
      win: 0.7
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Freya's Tears
  - Gluttonous Grimoire
  - Draconic Scale
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Gluttonous Grimoire
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, The Crusher, Freya''s Tears, Gluttonous Grimoire,
    Jotunn''s Revenge, Kinetic Cuirass, Amanita Charm, Soul Gem, Avenging Blade, Berserker''s
    Shield, Stone of Binding, Screeching Gargoyle, Void Shield, The Cosmic Horror,
    Oni Hunter''s Garb, The Reaper, Spear of the Magus, Void Stone, Runeforged Hammer,
    Shield of the Phoenix, Spear of Desolation, Hydra''s Lament, Nimble Ring, Shield
    Splitter, Spectral Armor, Erosion, Eye of the Storm, Eye of Providence, Obsidian
    Shard, Riptalon, Pharaoh''s Curse, Heartseeker, Leviathan''s Hide, Silverbranch
    Bow, Golden Blade, Midgardian Mail, Titan''s Bane.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.64
      win: 0.7
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.8
      pick: 0.11
      fit: 0.36
    Gluttonous Grimoire:
      total: 0.62
      efficiency: 0.63
      win: 0.7
      pick: 0.0
      fit: 0.58
    Draconic Scale:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.25
      fit: 0.4
    The Crusher:
      total: 0.62
      efficiency: 0.64
      win: 0.7
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.77
      win: 0.7
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Breastplate of Valor
  - Nimble Ring
  - Freya's Tears
  - Draconic Scale
  flex_slots:
  - Nimble Ring
  - Golden Blade
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
    this god: Freya''s Tears, Berserker''s Shield, Nimble Ring, Rod of Tahuti, Kinetic
    Cuirass, Amanita Charm, Gluttonous Grimoire, Golden Blade, The Crusher, Pharaoh''s
    Curse, Jotunn''s Revenge, Riptalon, Oni Hunter''s Garb, Soul Gem, Shield of the
    Phoenix, Tyrfing, Shogun''s Ofuda, Runeforged Hammer, Silverbranch Bow, Lernaean
    Bow, Hydra''s Lament, Spectral Armor, Yogi''s Necklace, Erosion, Shield Splitter,
    Eye of Providence, Eye of the Storm, Leviathan''s Hide, Toxic Blade, Midgardian
    Mail, Mantle Of Discord, Death Metal, Helm of Radiance, Stone of Binding, Screeching
    Gargoyle, Damaru, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.58
      efficiency: 0.53
      win: 0.7
      pick: 0.0
      fit: 0.55
    Berserker's Shield:
      total: 0.61
      efficiency: 0.66
      win: 0.7
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.64
      win: 0.76
      pick: 0.22
      fit: 0.19
    Nimble Ring:
      total: 0.6
      efficiency: 0.68
      win: 0.7
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.8
      pick: 0.11
      fit: 0.31
    Draconic Scale:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.25
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Freya's Tears
  - Draconic Scale
  - Rod of Tahuti
  flex_slots:
  - Shield of the Phoenix
  - Rod of Tahuti
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Jotunn''s Revenge,
    Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass, Amanita Charm, Soul Gem,
    Gluttonous Grimoire, Hydra''s Lament, Berserker''s Shield, The Crusher, Screeching
    Gargoyle, Oni Hunter''s Garb, Chronos'' Pendant, Chandra''s Grace, Nimble Ring,
    Spear of Desolation, Gladiator''s Shield, Erosion, Spectral Armor, Prophetic Cloak,
    Eye of Providence, Runeforged Hammer, Shield Splitter, Gem of Focus, Pharaoh''s
    Curse, Eye of the Storm, Leviathan''s Hide, Helm of Radiance, Midgardian Mail,
    Totem of Death, Arondight, Rod of Asclepius, Mantle Of Discord, Death Metal, Stone
    of Binding, The Cosmic Horror.'
  slot_scores:
    Breastplate of Valor:
      total: 0.65
      efficiency: 0.64
      win: 0.76
      pick: 0.22
      fit: 0.48
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.64
      win: 0.7
      pick: 0.0
      fit: 0.47
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.57
      win: 0.7
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.66
      efficiency: 0.59
      win: 0.8
      pick: 0.11
      fit: 0.63
    Draconic Scale:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.25
      fit: 0.43
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.77
      win: 0.7
      pick: 0.0
      fit: 0.14
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Draconic Scale
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Breastplate of Valor
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Freya''s Tears, Rod of Tahuti, The Crusher,
    Jotunn''s Revenge, Gluttonous Grimoire, Berserker''s Shield, Kinetic Cuirass,
    Amanita Charm, Runeforged Hammer, Nimble Ring, Hydra''s Lament, Soul Gem, Shield
    Splitter, Oni Hunter''s Garb, Golden Blade, Eye of the Storm, Shield of the Phoenix,
    Pharaoh''s Curse, Spectral Armor, Erosion, The Reaper, Lernaean Bow, Eye of Providence,
    Death Metal, Avenging Blade, Damaru, The Cosmic Horror, Shogun''s Ofuda, Leviathan''s
    Hide, Spear of the Magus, Midgardian Mail, Tekko-Kagi, Spear of Desolation, Tyrfing,
    Riptalon, Mantle Of Discord, Stone of Binding.'
  slot_scores:
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.64
      win: 0.76
      pick: 0.22
      fit: 0.22
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.64
      win: 0.7
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.8
      pick: 0.11
      fit: 0.36
    Draconic Scale:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.25
      fit: 0.4
    The Crusher:
      total: 0.61
      efficiency: 0.64
      win: 0.7
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.7
      pick: 0.0
      fit: 0.19
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Breastplate of Valor
  - Freya's Tears
  - Gluttonous Grimoire
  - Draconic Scale
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Breastplate of Valor
  - The Crusher
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Freya''s Tears, Gluttonous
    Grimoire, The Crusher, Jotunn''s Revenge, Kinetic Cuirass, Amanita Charm, Soul
    Gem, Berserker''s Shield, Nimble Ring, The Cosmic Horror, Oni Hunter''s Garb,
    Runeforged Hammer, Death Metal, Spear of the Magus, Hydra''s Lament, Shield of
    the Phoenix, Shield Splitter, Spear of Desolation, Eye of the Storm, Helm of Radiance,
    Spectral Armor, Erosion, Eye of Providence, Rod of Asclepius, The Reaper, Obsidian
    Shard, Golden Blade, Chronos'' Pendant, Pharaoh''s Curse, Jade Scepter, Leviathan''s
    Hide, Avenging Blade, Midgardian Mail, Damaru, Triton''s Conch, Ethereal Staff.'
  slot_scores:
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.64
      win: 0.76
      pick: 0.22
      fit: 0.22
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.8
      pick: 0.11
      fit: 0.36
    Gluttonous Grimoire:
      total: 0.62
      efficiency: 0.63
      win: 0.7
      pick: 0.0
      fit: 0.56
    Draconic Scale:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.25
      fit: 0.4
    The Crusher:
      total: 0.6
      efficiency: 0.64
      win: 0.7
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.77
      win: 0.7
      pick: 0.0
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Rod of Tahuti, Berserker''s
    Shield, Jotunn''s Revenge, The Crusher, Freya''s Tears, Gluttonous Grimoire, Shield
    Splitter, Shield of the Phoenix, Oni Hunter''s Garb, Runeforged Hammer, Erosion,
    Eye of the Storm, Eye of Providence, Hydra''s Lament, Spectral Armor, Nimble Ring,
    Soul Gem, Pharaoh''s Curse, Leviathan''s Hide, Golden Blade, Midgardian Mail,
    Avenging Blade, Mantle Of Discord, Death Metal, Stone of Binding, Ancile, Damaru,
    Screeching Gargoyle, Magi''s Cloak, Helm of Radiance, Shogun''s Ofuda, Gladiator''s
    Shield, Hide of the Nemean Lion, Void Shield, Doublet of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.48
      pick: 0.25
      fit: 0.31
    Berserker's Shield:
      total: 0.6
      efficiency: 0.66
      win: 0.7
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
      win: 0.7
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.59
      win: 0.7
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.77
      win: 0.7
      pick: 0.0
      fit: 0.11
    Amanita Charm:
      total: 0.62
      efficiency: 0.63
      win: 0.7
      pick: 0.0
      fit: 0.56
  starter: *id001
---
