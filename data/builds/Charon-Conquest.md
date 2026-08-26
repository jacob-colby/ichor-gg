---
type: smite-build
god: Charon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Tollkeeper
  aspect_pick_rate: 0.43
  aspect_win_rate: 0.63
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.19
    win_rate: 0.71
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.17
    - name: Gauntlet of Thebes
      pick_rate: 0.14
      win_rate: 0.2
  - name: The Cosmic Horror
    pick_rate: 0.22
    win_rate: 0.63
    alternates:
    - name: Totem of Death
      pick_rate: 0.22
      win_rate: 0.63
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.4
  - name: Damaru
    pick_rate: 0.14
    win_rate: 0.8
    alternates:
    - name: Totem of Death
      pick_rate: 0.14
      win_rate: 0.4
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.25
  - name: Soul Reaver
    pick_rate: 0.09
    win_rate: 0.33
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.67
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.33
  - name: Omen Drum
    pick_rate: 0.09
    win_rate: 1.0
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.33
    - name: Oracle Staff
      pick_rate: 0.06
      win_rate: 1.0
  - name: Rod of Tahuti
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Spectral Armor
      pick_rate: 0.09
      win_rate: 0.0
    - name: Draconic Scale
      pick_rate: 0.09
      win_rate: 0.5
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.38
    win_rate: 0.21
  - name: Bluestone Brooch
    pick_rate: 0.32
    win_rate: 0.5
  - name: Conduit Gem
    pick_rate: 0.14
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/charon/
  last_verified: '2026-08-26'
  god_win_rate: 0.40540540540540543
  god_matches_won: 15
  god_matches_played: 37
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-26'
  god_matches_analyzed: 888
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Draconic Scale
  - Omen Drum
  - Amanita Charm
  flex_slots:
  - Omen Drum
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Freya''s Tears, Breastplate of Valor,
    Erosion, Eye of Providence, Shield of the Phoenix, Stone of Binding, Magi''s Cloak,
    Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord, Midgardian Mail, Screeching
    Gargoyle, Prophetic Cloak, Hide of the Nemean Lion, Helm of Darkness, Leviathan''s
    Hide, Void Shield, Stampede, Ancile, Oni Hunter''s Garb, Xibalban Effigy, Hussar''s
    Wings.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.64
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.71
      pick: 0.19
      fit: 0.29
    Draconic Scale:
      total: 0.52
      efficiency: 0.5
      win: 0.5
      pick: 0.28
      fit: 0.71
    Omen Drum:
      total: 0.52
      efficiency: 0.18
      win: 1.0
      pick: 0.19
      fit: 0.0
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Spear of Desolation
  - Omen Drum
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Omen Drum
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Freya''s Tears,
    Rod of Asclepius, Soul Gem, Erosion, Eye of Providence, Breastplate of Valor,
    Ethereal Staff, Gluttonous Grimoire, Phoenix Feather, Yogi''s Necklace, Chandra''s
    Grace, Glorious Pridwen, Lifebinder, Midgardian Mail, Stone of Binding, Helm of
    Radiance, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Stampede, Magi''s
    Cloak, Ancile.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.57
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.71
      pick: 0.19
      fit: 0.3
    Omen Drum:
      total: 0.52
      efficiency: 0.18
      win: 1.0
      pick: 0.19
      fit: 0.0
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Spear of Desolation
  - The Cosmic Horror
  - Omen Drum
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - The Cosmic Horror
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Stone of Binding, Gluttonous Grimoire, Kinetic Cuirass,
    Freya''s Tears, Screeching Gargoyle, Spear of the Magus, Soul Gem, Void Shield,
    Breastplate of Valor, Obsidian Shard, Void Stone, Erosion, Eye of Providence,
    Shield of the Phoenix, Doom Orb, Helm of Radiance, The World Stone, Dreamer''s
    Idol, Magi''s Cloak, Mantle Of Discord, Midgardian Mail, Rod of Asclepius, Hide
    of the Nemean Lion.'
  slot_scores:
    Stone of Binding:
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.75
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.71
      pick: 0.19
      fit: 0.51
    The Cosmic Horror:
      total: 0.52
      efficiency: 0.45
      win: 0.63
      pick: 0.3
      fit: 0.41
    Omen Drum:
      total: 0.52
      efficiency: 0.18
      win: 1.0
      pick: 0.19
      fit: 0.0
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.5
      pick: 0.28
      fit: 0.41
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Spear of Desolation
  - Omen Drum
  - Rod of Tahuti
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Nimble Ring, Kinetic Cuirass, Freya''s Tears, Gluttonous
    Grimoire, Breastplate of Valor, Soul Gem, Helm of Radiance, Erosion, Stone of
    Binding, Eye of Providence, Shield of the Phoenix, Magi''s Cloak, Screeching Gargoyle,
    Daybreak Gavel, Spear of the Magus, Bragi''s Harp, Rod of Asclepius, Midgardian
    Mail, Mantle Of Discord, Bracer of The Abyss, Obsidian Shard, Hide of the Nemean
    Lion, Leviathan''s Hide.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.44
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.71
      pick: 0.19
      fit: 0.15
    Omen Drum:
      total: 0.6
      efficiency: 0.41
      win: 1.0
      pick: 0.19
      fit: 0.0
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.5
      pick: 0.28
      fit: 0.08
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Freya's Tears
  - Spear of Desolation
  - Omen Drum
  - Totem of Death
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Totem of Death
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Screeching Gargoyle, Soul
    Gem, Chronos'' Pendant, Prophetic Cloak, Erosion, Helm of Radiance, Gluttonous
    Grimoire, Eye of Providence, Gladiator''s Shield, Stone of Binding, Gem of Focus,
    Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus, Mantle Of
    Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.64
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.71
      pick: 0.19
      fit: 0.46
    Omen Drum:
      total: 0.6
      efficiency: 0.41
      win: 1.0
      pick: 0.19
      fit: 0.0
    Totem of Death:
      total: 0.52
      efficiency: 0.4
      win: 0.63
      pick: 0.3
      fit: 0.52
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Spear of Desolation
  - Damaru
  - Omen Drum
  - Rod of Tahuti
  flex_slots:
  - Damaru
  - Berserker's Shield
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Berserker''s Shield, Amanita
    Charm, Kinetic Cuirass, Freya''s Tears, Shield Splitter, Runeforged Hammer, Breastplate
    of Valor, Golden Blade, Gluttonous Grimoire, Eye of the Storm, Hydra''s Lament,
    Heartseeker, Lernaean Bow, Tyrfing, Erosion, Spear of the Magus, Tekko-Kagi, Eye
    of Providence, Avenging Blade, Helm of Radiance, Soul Gem, Stone of Binding, Shield
    of the Phoenix, Obsidian Shard, Titan''s Bane, The Crusher, Pharaoh''s Curse,
    Magi''s Cloak, Nimble Ring, Silverbranch Bow, The Reaper, Shogun''s Ofuda, Screeching
    Gargoyle, Toxic Blade, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.45
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.71
      pick: 0.19
      fit: 0.28
    Damaru:
      total: 0.52
      efficiency: 0.32
      win: 0.8
      pick: 0.22
      fit: 0.22
    Omen Drum:
      total: 0.6
      efficiency: 0.41
      win: 1.0
      pick: 0.19
      fit: 0.0
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.5
      pick: 0.28
      fit: 0.2
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Damaru
  - Omen Drum
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Damaru
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm,
    Kinetic Cuirass, Gluttonous Grimoire, Freya''s Tears, Shield Splitter, Breastplate
    of Valor, Spear of the Magus, Runeforged Hammer, Helm of Radiance, Soul Gem, Obsidian
    Shard, Berserker''s Shield, Eye of the Storm, Hydra''s Lament, Rod of Asclepius,
    Heartseeker, Erosion, Eye of Providence, Shield of the Phoenix, Stone of Binding,
    Doom Orb, Jade Scepter, Death Metal, Wish-Granting Pearl, Avenging Blade, Magi''s
    Cloak, Chronos'' Pendant, The World Stone, Helm of Darkness, Titan''s Bane, The
    Crusher, Ancient Signet, Screeching Gargoyle, Mantle Of Discord, Dreamer''s Idol,
    Midgardian Mail.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.41
    Spear of Desolation:
      total: 0.59
      efficiency: 0.57
      win: 0.71
      pick: 0.19
      fit: 0.41
    Damaru:
      total: 0.51
      efficiency: 0.32
      win: 0.8
      pick: 0.22
      fit: 0.18
    Omen Drum:
      total: 0.6
      efficiency: 0.41
      win: 1.0
      pick: 0.19
      fit: 0.0
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.5
      pick: 0.28
      fit: 0.33
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Freya''s Tears, Breastplate
    of Valor, Erosion, Eye of Providence, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord, Midgardian
    Mail, Screeching Gargoyle, Prophetic Cloak, Hide of the Nemean Lion, Helm of Darkness,
    Leviathan''s Hide, Void Shield, Stampede, Ancile, Oni Hunter''s Garb, Xibalban
    Effigy, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.66
      win: 0.4
      pick: 0.19
      fit: 0.39
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.38
      efficiency: 0.55
      win: 0.17
      pick: 0.16
      fit: 0.71
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
---
