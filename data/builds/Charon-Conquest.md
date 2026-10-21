---
type: smite-build
god: Charon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Tollkeeper
  aspect_pick_rate: 0.25
  aspect_win_rate: 0.67
  slot_order:
  - name: Prophetic Cloak
    pick_rate: 0.17
    win_rate: 0.75
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 1.0
    - name: Spear of Desolation
      pick_rate: 0.13
      win_rate: 0.67
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.25
    alternates:
    - name: The World Stone
      pick_rate: 0.08
      win_rate: 1.0
    - name: Chronos' Pendant
      pick_rate: 0.08
      win_rate: 0.5
  - name: Stampede
    pick_rate: 0.13
    win_rate: 0.67
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 1.0
    - name: Gladiator's Shield
      pick_rate: 0.09
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.17
    win_rate: 0.25
    alternates:
    - name: Omen Drum
      pick_rate: 0.09
      win_rate: 1.0
    - name: The Executioner
      pick_rate: 0.09
      win_rate: 0.5
  - name: Totem of Death
    pick_rate: 0.1
    win_rate: 1.0
    alternates:
    - name: Midgardian Mail
      pick_rate: 0.05
      win_rate: 1.0
    - name: Genji's Guard
      pick_rate: 0.05
      win_rate: 1.0
  - name: Olmec Blue
    pick_rate: 0.2
    win_rate: 1.0
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.0
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 1.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.33
    win_rate: 0.88
  - name: Bluestone Pendant
    pick_rate: 0.33
    win_rate: 0.63
  - name: Conduit Gem
    pick_rate: 0.13
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/charon/
  last_verified: '2026-10-21'
  god_win_rate: 0.6666666666666666
  god_matches_won: 16
  god_matches_played: 24
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-21'
  god_matches_analyzed: 814
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Midgardian Mail
  - Shifter's Shield
  - The World Stone
  - Totem of Death
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Rod of Tahuti
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Prophetic Cloak — physical protection
    swap_item: Prophetic Cloak
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Midgardian Mail, Amanita Charm, Rod of Tahuti, Kinetic
    Cuirass, Breastplate of Valor, Erosion, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous
    Grimoire, Mantle Of Discord, Screeching Gargoyle, Spear of Desolation, Hide of
    the Nemean Lion, Helm of Darkness, Leviathan''s Hide, Void Shield, Ancile, Oni
    Hunter''s Garb, Xibalban Effigy, Hussar''s Wings.'
  slot_scores:
    Midgardian Mail:
      total: 0.71
      efficiency: 0.53
      win: 1.0
      pick: 0.11
      fit: 0.46
    Shifter's Shield:
      total: 0.76
      efficiency: 0.55
      win: 1.0
      pick: 0.13
      fit: 0.71
    The World Stone:
      total: 0.66
      efficiency: 0.52
      win: 1.0
      pick: 0.11
      fit: 0.15
    Totem of Death:
      total: 0.65
      efficiency: 0.4
      win: 1.0
      pick: 0.22
      fit: 0.33
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.67
      pick: 0.0
      fit: 0.15
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Midgardian Mail
  - Shifter's Shield
  - The World Stone
  - Totem of Death
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Midgardian Mail
  - Shifter's Shield
  - The World Stone
  - Totem of Death
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Totem of Death
  - Rod of Tahuti
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Midgardian Mail, Amanita Charm, Shield of the Phoenix,
    Rod of Tahuti, Kinetic Cuirass, Rod of Asclepius, Soul Gem, Erosion, Eye of Providence,
    Breastplate of Valor, Draconic Scale, Ethereal Staff, Gluttonous Grimoire, Phoenix
    Feather, Yogi''s Necklace, Chandra''s Grace, Glorious Pridwen, Lifebinder, Stone
    of Binding, Helm of Radiance, Hide of the Nemean Lion, Leviathan''s Hide, Void
    Shield, Magi''s Cloak, Ancile.'
  slot_scores:
    Midgardian Mail:
      total: 0.71
      efficiency: 0.53
      win: 1.0
      pick: 0.11
      fit: 0.48
    Shifter's Shield:
      total: 0.75
      efficiency: 0.55
      win: 1.0
      pick: 0.13
      fit: 0.7
    The World Stone:
      total: 0.66
      efficiency: 0.52
      win: 1.0
      pick: 0.11
      fit: 0.16
    Totem of Death:
      total: 0.65
      efficiency: 0.4
      win: 1.0
      pick: 0.22
      fit: 0.34
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.67
      pick: 0.0
      fit: 0.16
    Amanita Charm:
      total: 0.68
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Midgardian Mail
  - Shifter's Shield
  - The World Stone
  - Totem of Death
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Midgardian Mail
  - Shifter's Shield
  - The World Stone
  - Totem of Death
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Totem of Death
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Shifter''s Shield, The World Stone, Midgardian Mail, Rod of Tahuti,
    Amanita Charm, Stone of Binding, Gluttonous Grimoire, Kinetic Cuirass, Spear of
    Desolation, Screeching Gargoyle, Spear of the Magus, Soul Gem, Void Shield, Breastplate
    of Valor, Obsidian Shard, Void Stone, Erosion, Eye of Providence, Draconic Scale,
    Shield of the Phoenix, Doom Orb, Helm of Radiance, Dreamer''s Idol, Magi''s Cloak,
    Mantle Of Discord, Rod of Asclepius, Hide of the Nemean Lion.'
  slot_scores:
    Midgardian Mail:
      total: 0.69
      efficiency: 0.53
      win: 1.0
      pick: 0.11
      fit: 0.32
    Shifter's Shield:
      total: 0.72
      efficiency: 0.55
      win: 1.0
      pick: 0.13
      fit: 0.49
    The World Stone:
      total: 0.7
      efficiency: 0.52
      win: 1.0
      pick: 0.11
      fit: 0.41
    Totem of Death:
      total: 0.64
      efficiency: 0.4
      win: 1.0
      pick: 0.22
      fit: 0.26
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.67
      pick: 0.0
      fit: 0.41
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Midgardian Mail
  - Shifter's Shield
  - The World Stone
  - Totem of Death
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Midgardian Mail
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Shifter's Shield
  - The World Stone
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
    this god: Shifter''s Shield, Midgardian Mail, Rod of Tahuti, Amanita Charm, Nimble
    Ring, Kinetic Cuirass, Gluttonous Grimoire, Breastplate of Valor, Soul Gem, Helm
    of Radiance, Erosion, Stone of Binding, Eye of Providence, Shield of the Phoenix,
    Draconic Scale, Spear of Desolation, Magi''s Cloak, Screeching Gargoyle, Daybreak
    Gavel, Spear of the Magus, Bragi''s Harp, Rod of Asclepius, Mantle Of Discord,
    Bracer of The Abyss, Obsidian Shard, Hide of the Nemean Lion, Leviathan''s Hide.'
  slot_scores:
    Midgardian Mail:
      total: 0.68
      efficiency: 0.53
      win: 1.0
      pick: 0.11
      fit: 0.23
    Bracer of The Abyss:
      total: 0.52
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.57
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.52
      efficiency: 0.44
      win: 0.67
      pick: 0.0
      fit: 0.44
    Shifter's Shield:
      total: 0.7
      efficiency: 0.55
      win: 1.0
      pick: 0.13
      fit: 0.36
    The World Stone:
      total: 0.65
      efficiency: 0.52
      win: 1.0
      pick: 0.11
      fit: 0.08
  community_ordered:
  - Midgardian Mail
  - Shifter's Shield
  - The World Stone
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Midgardian Mail
  - Prophetic Cloak
  - Shifter's Shield
  - The World Stone
  - Totem of Death
  flex_slots:
  - Breastplate of Valor
  - Prophetic Cloak
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Shifter''s Shield, Midgardian Mail,
    Rod of Tahuti, Breastplate of Valor, Amanita Charm, Kinetic Cuirass, Shield of
    the Phoenix, Spear of Desolation, Screeching Gargoyle, Soul Gem, Erosion, Helm
    of Radiance, Gluttonous Grimoire, Eye of Providence, Draconic Scale, Stone of
    Binding, Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of
    the Magus, Mantle Of Discord, Glorious Pridwen, Daybreak Gavel, Chronos'' Pendant,
    Gladiator''s Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.48
    Midgardian Mail:
      total: 0.68
      efficiency: 0.53
      win: 1.0
      pick: 0.11
      fit: 0.29
    Prophetic Cloak:
      total: 0.6
      efficiency: 0.44
      win: 0.75
      pick: 0.17
      fit: 0.64
    Shifter's Shield:
      total: 0.72
      efficiency: 0.55
      win: 1.0
      pick: 0.13
      fit: 0.45
    The World Stone:
      total: 0.66
      efficiency: 0.52
      win: 1.0
      pick: 0.11
      fit: 0.13
    Totem of Death:
      total: 0.68
      efficiency: 0.4
      win: 1.0
      pick: 0.22
      fit: 0.52
  community_ordered:
  - Midgardian Mail
  - Prophetic Cloak
  - Shifter's Shield
  - The World Stone
  - Totem of Death
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Midgardian Mail
  - Shifter's Shield
  - The World Stone
  - Totem of Death
  - Rod of Tahuti
  flex_slots:
  - Rod of Tahuti
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    win/pick). Underrated for this god: Shifter''s Shield, Midgardian Mail, Rod of
    Tahuti, Jotunn''s Revenge, Berserker''s Shield, Amanita Charm, Kinetic Cuirass,
    Shield Splitter, Runeforged Hammer, Breastplate of Valor, Golden Blade, Gluttonous
    Grimoire, Eye of the Storm, Hydra''s Lament, Spear of Desolation, Heartseeker,
    Lernaean Bow, Tyrfing, Erosion, Spear of the Magus, Tekko-Kagi, Eye of Providence,
    Avenging Blade, Helm of Radiance, Soul Gem, Stone of Binding, Shield of the Phoenix,
    Draconic Scale, Obsidian Shard, Titan''s Bane, The Crusher, Pharaoh''s Curse,
    Magi''s Cloak, Nimble Ring, Silverbranch Bow, The Reaper, Shogun''s Ofuda, Screeching
    Gargoyle, Toxic Blade, Mantle Of Discord.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.45
    Midgardian Mail:
      total: 0.68
      efficiency: 0.53
      win: 1.0
      pick: 0.11
      fit: 0.27
    Shifter's Shield:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.13
      fit: 0.41
    The World Stone:
      total: 0.67
      efficiency: 0.52
      win: 1.0
      pick: 0.11
      fit: 0.2
    Totem of Death:
      total: 0.63
      efficiency: 0.4
      win: 1.0
      pick: 0.22
      fit: 0.23
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.67
      pick: 0.0
      fit: 0.2
  community_ordered:
  - Midgardian Mail
  - Shifter's Shield
  - The World Stone
  - Totem of Death
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Midgardian Mail
  - Shifter's Shield
  - The World Stone
  - Totem of Death
  - Rod of Tahuti
  flex_slots:
  - Rod of Tahuti
  - Jotunn's Revenge
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Shifter''s Shield, The World Stone,
    Midgardian Mail, Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass,
    Gluttonous Grimoire, Spear of Desolation, Shield Splitter, Breastplate of Valor,
    Spear of the Magus, Runeforged Hammer, Helm of Radiance, Soul Gem, Obsidian Shard,
    Berserker''s Shield, Eye of the Storm, Hydra''s Lament, Rod of Asclepius, Heartseeker,
    Erosion, Eye of Providence, Shield of the Phoenix, Stone of Binding, Draconic
    Scale, Doom Orb, Jade Scepter, Death Metal, Wish-Granting Pearl, Avenging Blade,
    Magi''s Cloak, Helm of Darkness, Titan''s Bane, The Crusher, Ancient Signet, Screeching
    Gargoyle, Mantle Of Discord, Dreamer''s Idol, Chronos'' Pendant.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.41
    Midgardian Mail:
      total: 0.68
      efficiency: 0.53
      win: 1.0
      pick: 0.11
      fit: 0.27
    Shifter's Shield:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.13
      fit: 0.42
    The World Stone:
      total: 0.69
      efficiency: 0.52
      win: 1.0
      pick: 0.11
      fit: 0.33
    Totem of Death:
      total: 0.65
      efficiency: 0.4
      win: 1.0
      pick: 0.22
      fit: 0.36
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.67
      pick: 0.0
      fit: 0.33
  community_ordered:
  - Midgardian Mail
  - Shifter's Shield
  - The World Stone
  - Totem of Death
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s
    Shield, Breastplate of Valor, Erosion, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous
    Grimoire, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Hide of the
    Nemean Lion, Helm of Darkness, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s
    Garb, Xibalban Effigy, Spear of Desolation, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.41
      efficiency: 0.66
      win: 0.25
      pick: 0.23
      fit: 0.39
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.81
    Shifter's Shield:
      total: 0.76
      efficiency: 0.55
      win: 1.0
      pick: 0.13
      fit: 0.71
    Freya's Tears:
      total: 0.44
      efficiency: 0.61
      win: 0.25
      pick: 0.28
      fit: 0.64
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.71
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
---
