---
type: smite-build
god: Sun Wukong
mode: Conquest
builds:
- source: community
  aspect: Aspect of Transformation
  aspect_pick_rate: 0.12
  aspect_win_rate: 0.28
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.42
    win_rate: 0.46
    alternates:
    - name: Scepter of Dominion
      pick_rate: 0.06
      win_rate: 0.2
    - name: Runeforged Hammer
      pick_rate: 0.05
      win_rate: 0.5
  - name: Gladiator's Shield
    pick_rate: 0.1
    win_rate: 0.41
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.49
    - name: Prophetic Cloak
      pick_rate: 0.09
      win_rate: 0.42
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.38
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.39
    - name: Soul Gem
      pick_rate: 0.08
      win_rate: 0.7
  - name: Freya's Tears
    pick_rate: 0.09
    win_rate: 0.54
    alternates:
    - name: Gladiator's Shield
      pick_rate: 0.09
      win_rate: 0.48
    - name: Obsidian Shard
      pick_rate: 0.07
      win_rate: 0.65
  - name: Hide of the Nemean Lion
    pick_rate: 0.06
    win_rate: 0.43
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.31
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.67
  - name: Engraved Guard
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Triton's Conch
      pick_rate: 0.05
      win_rate: 0.5
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.4
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.3
    win_rate: 0.55
  - name: Bluestone Pendant
    pick_rate: 0.2
    win_rate: 0.44
  - name: Archmage's Gem
    pick_rate: 0.08
    win_rate: 0.55
  source_url: https://smitebrain.com/gods/sun-wukong/
  last_verified: '2026-09-03'
  god_win_rate: 0.46387832699619774
  god_matches_won: 122
  god_matches_played: 263
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-09-03'
  god_matches_analyzed: 10626
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Runeforged Hammer
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Berserker's Shield
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield, Runeforged Hammer,
    Amanita Charm, Kinetic Cuirass, Shield Splitter, Eye of the Storm, Avenging Blade,
    Gluttonous Grimoire, Lernaean Bow, Breastplate of Valor, Hydra''s Lament, Erosion,
    Pharaoh''s Curse, Eye of Providence, Heartseeker, Draconic Scale, Shogun''s Ofuda,
    Golden Blade, Shield of the Phoenix, Tekko-Kagi, Bragi''s Harp, Rod of Asclepius,
    Daybreak Gavel, Nimble Ring, Helm of Radiance, Midgardian Mail, Stone of Binding,
    Dominance, Spear of the Magus, Titan''s Bane, Death Metal, Leviathan''s Hide,
    Jade Scepter, The Crusher, Void Shield, Hide of the Nemean Lion.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.46
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.46
      pick: 0.0
      fit: 0.37
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.05
      fit: 0.56
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.86
      win: 0.46
      pick: 0.0
      fit: 0.12
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.65
      pick: 0.12
      fit: 0.22
    Soul Gem:
      total: 0.54
      efficiency: 0.52
      win: 0.7
      pick: 0.12
      fit: 0.26
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Amanita Charm, Rod of Tahuti, Berserker''s Shield, Runeforged
    Hammer, Jotunn''s Revenge, Kinetic Cuirass, Shield of the Phoenix, Rod of Asclepius,
    Shield Splitter, Eye of the Storm, Erosion, Ethereal Staff, The Reaper, Breastplate
    of Valor, Eye of Providence, Yogi''s Necklace, Draconic Scale, Phoenix Feather,
    Gluttonous Grimoire, Avenging Blade, Pharaoh''s Curse, Shogun''s Ofuda, Lernaean
    Bow, Hydra''s Lament, Lifebinder, Stone of Binding, Midgardian Mail, Helm of Radiance,
    Chandra''s Grace, Daybreak Gavel, Magi''s Cloak, Leviathan''s Hide, Sphere of
    Negation, Void Shield, Stampede, Heartseeker, Ancile, Hide of the Nemean Lion.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.46
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.54
      pick: 0.15
      fit: 0.37
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.86
      win: 0.46
      pick: 0.0
      fit: 0.1
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.65
      pick: 0.12
      fit: 0.2
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.84
    Soul Gem:
      total: 0.58
      efficiency: 0.52
      win: 0.7
      pick: 0.12
      fit: 0.54
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Freya's Tears
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    for this god: Soul Gem, Rod of Tahuti, Obsidian Shard, Jotunn''s Revenge, Gluttonous
    Grimoire, Berserker''s Shield, Runeforged Hammer, Avenging Blade, Amanita Charm,
    Heartseeker, Spear of the Magus, Stone of Binding, Spear of Desolation, Tekko-Kagi,
    Titan''s Bane, Kinetic Cuirass, The Crusher, Void Shield, Screeching Gargoyle,
    The Reaper, Void Stone, Breastplate of Valor, Shield Splitter, Doom Orb, Eye of
    the Storm, The World Stone, Avatar''s Parashu, Hydra''s Lament, Lernaean Bow,
    Dreamer''s Idol, Pendulum Blade, Nimble Ring, Daybreak Gavel, Helm of Radiance,
    Erosion, Pharaoh''s Curse, Rod of Asclepius, Eye of Providence, Shield of the
    Phoenix.'
  slot_scores:
    Berserker's Shield:
      total: 0.49
      efficiency: 0.68
      win: 0.46
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.46
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.54
      pick: 0.15
      fit: 0.2
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.46
      pick: 0.0
      fit: 0.39
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.65
      pick: 0.12
      fit: 0.49
    Soul Gem:
      total: 0.58
      efficiency: 0.52
      win: 0.7
      pick: 0.12
      fit: 0.52
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Nimble Ring
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Rod of Tahuti, Obsidian Shard, Berserker''s Shield, Nimble
    Ring, Golden Blade, Jotunn''s Revenge, Amanita Charm, Runeforged Hammer, Gluttonous
    Grimoire, Tyrfing, Riptalon, Kinetic Cuirass, Lernaean Bow, Silverbranch Bow,
    Toxic Blade, Pharaoh''s Curse, Breastplate of Valor, Shogun''s Ofuda, Shield Splitter,
    Tekko-Kagi, Bragi''s Harp, Eye of the Storm, Hydra''s Lament, The Reaper, Daybreak
    Gavel, Dominance, Avenging Blade, Helm of Radiance, Bracer of The Abyss, Rod of
    Asclepius, Spear of the Magus, Erosion, Shield of the Phoenix, Eye of Providence,
    Qin''s Blade, Vital Amplifier, Heartseeker, Draconic Scale.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.52
      win: 0.46
      pick: 0.0
      fit: 0.65
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.46
      pick: 0.0
      fit: 0.45
    Nimble Ring:
      total: 0.49
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.36
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.86
      win: 0.46
      pick: 0.0
      fit: 0.08
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.65
      pick: 0.12
      fit: 0.18
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.7
      pick: 0.12
      fit: 0.29
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
  - Breastplate of Valor
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, Rod of
    Tahuti, Obsidian Shard, Breastplate of Valor, Berserker''s Shield, Amanita Charm,
    Spear of Desolation, Hydra''s Lament, Shield of the Phoenix, Runeforged Hammer,
    Chronos'' Pendant, Kinetic Cuirass, Screeching Gargoyle, Gluttonous Grimoire,
    Arondight, Gem of Focus, Nimble Ring, Eye of Erebus, Helm of Radiance, Rod of
    Asclepius, Shield Splitter, Spear of the Magus, Chandra''s Grace, Eye of the Storm,
    Daybreak Gavel, Erosion, Pharaoh''s Curse, Jade Scepter, Lernaean Bow, Eye of
    Providence, Wish-Granting Pearl, Avenging Blade, Gladiator''s Shield, Totem of
    Death, Draconic Scale, Pendulum Blade, Shogun''s Ofuda, Prophetic Cloak.'
  slot_scores:
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.46
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.54
      pick: 0.15
      fit: 0.52
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.86
      win: 0.46
      pick: 0.0
      fit: 0.15
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.65
      pick: 0.12
      fit: 0.25
    Soul Gem:
      total: 0.59
      efficiency: 0.52
      win: 0.7
      pick: 0.12
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield,
    Amanita Charm, Runeforged Hammer, Kinetic Cuirass, Shield Splitter, Eye of the
    Storm, Avenging Blade, Gluttonous Grimoire, Lernaean Bow, Breastplate of Valor,
    Hydra''s Lament, Erosion, Pharaoh''s Curse, Eye of Providence, Heartseeker, Draconic
    Scale, Shogun''s Ofuda, Golden Blade, Shield of the Phoenix, Tekko-Kagi, Bragi''s
    Harp, Rod of Asclepius, Daybreak Gavel, Nimble Ring, Helm of Radiance, Midgardian
    Mail, Stone of Binding, Dominance, Hide of the Nemean Lion, Spear of the Magus,
    Titan''s Bane, Death Metal, Leviathan''s Hide, Jade Scepter, The Crusher, Void
    Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.46
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.46
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.56
      win: 0.46
      pick: 0.0
      fit: 0.55
    Shield Splitter:
      total: 0.48
      efficiency: 0.55
      win: 0.46
      pick: 0.0
      fit: 0.51
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.05
      fit: 0.56
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.45
  starter: *id001
---
