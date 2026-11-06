---
type: smite-build
god: Charon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Tollkeeper
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.5
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.19
    win_rate: 0.4
    alternates:
    - name: Yogi's Necklace
      pick_rate: 0.15
      win_rate: 0.63
    - name: Prophetic Cloak
      pick_rate: 0.1
      win_rate: 0.8
  - name: Shifter's Shield
    pick_rate: 0.15
    win_rate: 0.63
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.67
    - name: Stampede
      pick_rate: 0.12
      win_rate: 0.33
  - name: Shell of Rebuke
    pick_rate: 0.14
    win_rate: 0.29
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.25
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.75
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 0.4
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.13
      win_rate: 0.67
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.33
  - name: Ethereal Staff
    pick_rate: 0.08
    win_rate: 0.33
    alternates:
    - name: Sage's Ring
      pick_rate: 0.08
      win_rate: 0.0
    - name: Olmec Blue
      pick_rate: 0.05
      win_rate: 0.5
  - name: Captain's Ring
    pick_rate: 0.08
    win_rate: 0.0
    alternates:
    - name: Oracle Staff
      pick_rate: 0.08
      win_rate: 1.0
    - name: Spectral Armor
      pick_rate: 0.08
      win_rate: 0.5
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.37
    win_rate: 0.58
  - name: Bluestone Brooch
    pick_rate: 0.31
    win_rate: 0.63
  - name: War Flag
    pick_rate: 0.1
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/charon/
  last_verified: '2026-11-06'
  god_win_rate: 0.5576923076923077
  god_matches_won: 29
  god_matches_played: 52
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Prophetic Cloak, Amanita Charm, Kinetic Cuirass,
    Rod of Tahuti, Draconic Scale, Gluttonous Grimoire, Shield of the Phoenix, Erosion,
    Soul Gem, Eye of Providence, Oni Hunter''s Garb, Helm of Darkness, Stone of Binding,
    Midgardian Mail, Magi''s Cloak, Mantle Of Discord, Screeching Gargoyle, Leviathan''s
    Hide, Spear of Desolation, Helm of Radiance, Hide of the Nemean Lion, Gladiator''s
    Shield, Lotus Sickle, Ancile, Blood-Bound Book, Void Stone, Genji''s Guard.'
  slot_scores:
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.63
      win: 0.75
      pick: 0.12
      fit: 0.35
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.61
      win: 0.4
      pick: 0.0
      fit: 0.74
    Prophetic Cloak:
      total: 0.61
      efficiency: 0.45
      win: 0.8
      pick: 0.1
      fit: 0.57
    Freya's Tears:
      total: 0.49
      efficiency: 0.61
      win: 0.4
      pick: 0.18
      fit: 0.57
    Shifter's Shield:
      total: 0.56
      efficiency: 0.5
      win: 0.63
      pick: 0.2
      fit: 0.64
    Amanita Charm:
      total: 0.51
      efficiency: 0.68
      win: 0.4
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Breastplate of Valor
  - Prophetic Cloak
  - Freya's Tears
  - Shifter's Shield
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Yogi's Necklace
  - Breastplate of Valor
  - Kinetic Cuirass
  - Prophetic Cloak
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Yogi''s Necklace, Amanita Charm, Shield of the
    Phoenix, Soul Gem, Kinetic Cuirass, Rod of Tahuti, Gluttonous Grimoire, Blood-Bound
    Book, Phoenix Feather, Draconic Scale, Erosion, Oni Hunter''s Garb, Eye of Providence,
    Chandra''s Grace, Midgardian Mail, Bancroft''s Talon, Rod of Asclepius, Regrowth
    Striders, Glorious Pridwen, Leviathan''s Hide, Soul Locket, Hide of the Nemean
    Lion, Spear of Desolation, Gladiator''s Shield, Screeching Gargoyle, Genji''s
    Guard.'
  slot_scores:
    Yogi's Necklace:
      total: 0.57
      efficiency: 0.56
      win: 0.63
      pick: 0.15
      fit: 0.54
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.63
      win: 0.75
      pick: 0.12
      fit: 0.32
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.61
      win: 0.4
      pick: 0.0
      fit: 0.72
    Prophetic Cloak:
      total: 0.6
      efficiency: 0.45
      win: 0.8
      pick: 0.1
      fit: 0.51
    Shifter's Shield:
      total: 0.56
      efficiency: 0.5
      win: 0.63
      pick: 0.2
      fit: 0.62
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.4
      pick: 0.0
      fit: 0.92
  community_ordered:
  - Yogi's Necklace
  - Breastplate of Valor
  - Prophetic Cloak
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Yogi's Necklace
  - Breastplate of Valor
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Breastplate of Valor, Rod of Tahuti, Amanita Charm, Gluttonous Grimoire,
    Soul Gem, Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation, Stone of
    Binding, Void Stone, Void Shield, Obsidian Shard, Shield of the Phoenix, Draconic
    Scale, Spear of the Magus, Oni Hunter''s Garb, Erosion, Eye of Providence, Dreamer''s
    Idol, Midgardian Mail, Helm of Radiance, Doom Orb, Lotus Sickle, Helm of Darkness,
    Blood-Bound Book, Leviathan''s Hide, Magi''s Cloak, Genji''s Guard.'
  slot_scores:
    Yogi's Necklace:
      total: 0.51
      efficiency: 0.56
      win: 0.63
      pick: 0.15
      fit: 0.13
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.63
      win: 0.75
      pick: 0.12
      fit: 0.25
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.61
      win: 0.4
      pick: 0.0
      fit: 0.55
    Prophetic Cloak:
      total: 0.58
      efficiency: 0.45
      win: 0.8
      pick: 0.1
      fit: 0.41
    Freya's Tears:
      total: 0.46
      efficiency: 0.61
      win: 0.4
      pick: 0.18
      fit: 0.41
    Shifter's Shield:
      total: 0.54
      efficiency: 0.5
      win: 0.63
      pick: 0.2
      fit: 0.45
  community_ordered:
  - Yogi's Necklace
  - Breastplate of Valor
  - Prophetic Cloak
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Breastplate of Valor
  - Prophetic Cloak
  - Nimble Ring
  - Bragi's Harp
  - Shifter's Shield
  - Eros' Bow
  flex_slots:
  - Bragi's Harp
  - Eros' Bow
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Rod of Tahuti, Amanita Charm, Kinetic Cuirass,
    Gluttonous Grimoire, Soul Gem, Shield of the Phoenix, Nimble Ring, Oni Hunter''s
    Garb, Draconic Scale, Erosion, Spear of Desolation, Eye of Providence, Bragi''s
    Harp, Lotus Sickle, Blood-Bound Book, Helm of Radiance, Screeching Gargoyle, Midgardian
    Mail, Eros'' Bow, Stone of Binding, Leviathan''s Hide, Magi''s Cloak, Helm of
    Darkness, Mantle Of Discord, Hide of the Nemean Lion, Ancient Signet, Genji''s
    Guard.'
  slot_scores:
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.63
      win: 0.75
      pick: 0.12
      fit: 0.2
    Prophetic Cloak:
      total: 0.57
      efficiency: 0.45
      win: 0.8
      pick: 0.1
      fit: 0.33
    Nimble Ring:
      total: 0.42
      efficiency: 0.57
      win: 0.4
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.41
      efficiency: 0.47
      win: 0.4
      pick: 0.0
      fit: 0.44
    Shifter's Shield:
      total: 0.52
      efficiency: 0.5
      win: 0.63
      pick: 0.2
      fit: 0.36
    Eros' Bow:
      total: 0.41
      efficiency: 0.5
      win: 0.4
      pick: 0.0
      fit: 0.34
  community_ordered:
  - Breastplate of Valor
  - Prophetic Cloak
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Yogi's Necklace
  - Breastplate of Valor
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Prophetic Cloak,
    Rod of Tahuti, Amanita Charm, Soul Gem, Kinetic Cuirass, Shield of the Phoenix,
    Spear of Desolation, Lotus Sickle, Screeching Gargoyle, Gluttonous Grimoire, Chronos''
    Pendant, Genji''s Guard, Gladiator''s Shield, Draconic Scale, Oni Hunter''s Garb,
    Erosion, Eye of Providence, Helm of Radiance, Blood-Bound Book, Gem of Focus,
    Heartwood Charm, Helm of Darkness, Midgardian Mail, Chandra''s Grace, Stone of
    Binding, Leviathan''s Hide, Regrowth Striders.'
  slot_scores:
    Yogi's Necklace:
      total: 0.5
      efficiency: 0.56
      win: 0.63
      pick: 0.15
      fit: 0.12
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.63
      win: 0.75
      pick: 0.12
      fit: 0.45
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.61
      win: 0.4
      pick: 0.0
      fit: 0.52
    Prophetic Cloak:
      total: 0.61
      efficiency: 0.45
      win: 0.8
      pick: 0.1
      fit: 0.6
    Freya's Tears:
      total: 0.49
      efficiency: 0.61
      win: 0.4
      pick: 0.18
      fit: 0.6
    Shifter's Shield:
      total: 0.53
      efficiency: 0.5
      win: 0.63
      pick: 0.2
      fit: 0.42
  community_ordered:
  - Yogi's Necklace
  - Breastplate of Valor
  - Prophetic Cloak
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Yogi's Necklace
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Prophetic Cloak
  - Shifter's Shield
  flex_slots:
  - Berserker's Shield
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Breastplate of Valor, Rod of Tahuti, Berserker''s
    Shield, Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield Splitter, Gluttonous
    Grimoire, Soul Gem, The Reaper, Tyrfing, Runeforged Hammer, Spear of Desolation,
    Hydra''s Lament, Shield of the Phoenix, Golden Blade, The Crusher, Oni Hunter''s
    Garb, Draconic Scale, Heartseeker, Erosion, Eye of Providence, Death Metal, Tekko-Kagi,
    Titan''s Bane, Lotus Sickle, Screeching Gargoyle, Midgardian Mail, Bragi''s Harp,
    Helm of Radiance, Blood-Bound Book, Obsidian Shard, Stone of Binding, Avenging
    Blade, Nimble Ring, Leviathan''s Hide, Arondight, Helm of Darkness, Magi''s Cloak,
    Genji''s Guard.'
  slot_scores:
    Yogi's Necklace:
      total: 0.5
      efficiency: 0.56
      win: 0.63
      pick: 0.15
      fit: 0.11
    Berserker's Shield:
      total: 0.48
      efficiency: 0.72
      win: 0.4
      pick: 0.0
      fit: 0.33
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.63
      win: 0.75
      pick: 0.12
      fit: 0.21
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 0.42
    Prophetic Cloak:
      total: 0.57
      efficiency: 0.45
      win: 0.8
      pick: 0.1
      fit: 0.35
    Shifter's Shield:
      total: 0.53
      efficiency: 0.5
      win: 0.63
      pick: 0.2
      fit: 0.39
  community_ordered:
  - Yogi's Necklace
  - Breastplate of Valor
  - Prophetic Cloak
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Yogi's Necklace
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Prophetic Cloak
  - Shifter's Shield
  flex_slots:
  - Kinetic Cuirass
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Rod of Tahuti,
    Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Soul Gem, Jotunn''s Revenge,
    Shield Splitter, Spear of Desolation, Berserker''s Shield, The Reaper, Lotus Sickle,
    Helm of Radiance, Blood-Bound Book, Runeforged Hammer, Shield of the Phoenix,
    Obsidian Shard, Death Metal, Oni Hunter''s Garb, Draconic Scale, Helm of Darkness,
    Hydra''s Lament, Spear of the Magus, Ancient Signet, The Crusher, Erosion, Eye
    of Providence, Polynomicon, Heartseeker, Dreamer''s Idol, Chronos'' Pendant, Midgardian
    Mail, Screeching Gargoyle, Stone of Binding, Jade Scepter, Titan''s Bane, Leviathan''s
    Hide, Tyrfing, Magi''s Cloak, Genji''s Guard.'
  slot_scores:
    Yogi's Necklace:
      total: 0.5
      efficiency: 0.56
      win: 0.63
      pick: 0.15
      fit: 0.11
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.63
      win: 0.75
      pick: 0.12
      fit: 0.21
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.65
      win: 0.4
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.61
      win: 0.4
      pick: 0.0
      fit: 0.49
    Prophetic Cloak:
      total: 0.57
      efficiency: 0.45
      win: 0.8
      pick: 0.1
      fit: 0.35
    Shifter's Shield:
      total: 0.53
      efficiency: 0.5
      win: 0.63
      pick: 0.2
      fit: 0.39
  community_ordered:
  - Yogi's Necklace
  - Breastplate of Valor
  - Prophetic Cloak
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  - Erosion
  flex_slots:
  - Draconic Scale
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Genji''s
    Guard, Draconic Scale, Gluttonous Grimoire, Shield of the Phoenix, Erosion, Breastplate
    of Valor, Soul Gem, Eye of Providence, Oni Hunter''s Garb, Helm of Darkness, Stone
    of Binding, Midgardian Mail, Magi''s Cloak, Mantle Of Discord, Screeching Gargoyle,
    Leviathan''s Hide, Spear of Desolation, Helm of Radiance, Hide of the Nemean Lion,
    Gladiator''s Shield, Lotus Sickle, Ancile, Prophetic Cloak, Blood-Bound Book,
    Void Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.42
      efficiency: 0.71
      win: 0.25
      pick: 0.12
      fit: 0.35
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.61
      win: 0.4
      pick: 0.0
      fit: 0.74
    Freya's Tears:
      total: 0.49
      efficiency: 0.61
      win: 0.4
      pick: 0.18
      fit: 0.57
    Draconic Scale:
      total: 0.46
      efficiency: 0.53
      win: 0.4
      pick: 0.0
      fit: 0.64
    Amanita Charm:
      total: 0.51
      efficiency: 0.68
      win: 0.4
      pick: 0.0
      fit: 0.64
    Erosion:
      total: 0.46
      efficiency: 0.51
      win: 0.4
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
