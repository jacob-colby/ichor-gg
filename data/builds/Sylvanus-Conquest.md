---
type: smite-build
god: Sylvanus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Grover's Wrath
  aspect_pick_rate: 0.2
  aspect_win_rate: 0.45
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.3
    win_rate: 0.56
    alternates:
    - name: Tyrfing
      pick_rate: 0.17
      win_rate: 0.33
    - name: Circe's Hexstone
      pick_rate: 0.15
      win_rate: 0.71
  - name: Freya's Tears
    pick_rate: 0.16
    win_rate: 0.7
    alternates:
    - name: Stampede
      pick_rate: 0.15
      win_rate: 0.52
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.69
  - name: Shell of Rebuke
    pick_rate: 0.19
    win_rate: 0.73
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.36
    - name: Berserker's Shield
      pick_rate: 0.09
      win_rate: 0.5
  - name: Genji's Guard
    pick_rate: 0.08
    win_rate: 0.64
    alternates:
    - name: Freya's Tears
      pick_rate: 0.16
      win_rate: 0.73
    - name: Shell of Rebuke
      pick_rate: 0.12
      win_rate: 0.63
  - name: Captain's Ring
    pick_rate: 0.03
    win_rate: 1.0
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.89
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.57
  - name: Olmec Blue
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Sage's Ring
      pick_rate: 0.08
      win_rate: 1.0
    - name: Medal of Defense
      pick_rate: 0.07
      win_rate: 0.8
  community_starters:
  - name: Selflessness
    pick_rate: 0.23
    win_rate: 0.48
  - name: War Flag
    pick_rate: 0.15
    win_rate: 0.62
  - name: Heroism
    pick_rate: 0.14
    win_rate: 0.65
  source_url: https://smitebrain.com/gods/sylvanus/
  last_verified: '2026-11-06'
  god_win_rate: 0.5774647887323944
  god_matches_won: 82
  god_matches_played: 142
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
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Genji''s Guard, Soul
    Gem, Gluttonous Grimoire, Shield of the Phoenix, Breastplate of Valor, Draconic
    Scale, Erosion, Eye of Providence, Oni Hunter''s Garb, Spear of Desolation, Shifter''s
    Shield, Helm of Darkness, Lotus Sickle, Helm of Radiance, Screeching Gargoyle,
    Stone of Binding, Midgardian Mail, Blood-Bound Book, Magi''s Cloak, Mantle Of
    Discord, Leviathan''s Hide, Gladiator''s Shield, Hide of the Nemean Lion, Prophetic
    Cloak, Chronos'' Pendant, Ancile.'
  slot_scores:
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.63
      win: 0.67
      pick: 0.0
      fit: 0.36
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.64
      pick: 0.13
      fit: 0.36
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.67
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.7
      pick: 0.22
      fit: 0.56
    Draconic Scale:
      total: 0.57
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.63
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Shield of the Phoenix, Rod of Tahuti, Kinetic
    Cuirass, Blood-Bound Book, Gluttonous Grimoire, Genji''s Guard, Phoenix Feather,
    Ethereal Staff, Yogi''s Necklace, Breastplate of Valor, Chandra''s Grace, Draconic
    Scale, Oni Hunter''s Garb, Bancroft''s Talon, Spear of Desolation, Erosion, Eye
    of Providence, Rod of Asclepius, Lotus Sickle, Shifter''s Shield, Soul Locket,
    Regrowth Striders, Glorious Pridwen, Midgardian Mail, Helm of Radiance, Screeching
    Gargoyle, Helm of Darkness.'
  slot_scores:
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.63
      win: 0.67
      pick: 0.0
      fit: 0.33
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.64
      pick: 0.13
      fit: 0.33
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.65
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.7
      pick: 0.22
      fit: 0.5
    Amanita Charm:
      total: 0.67
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.85
    Soul Gem:
      total: 0.63
      efficiency: 0.58
      win: 0.67
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Screeching Gargoyle
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
    for this god: Rod of Tahuti, Soul Gem, Gluttonous Grimoire, Amanita Charm, Kinetic
    Cuirass, Spear of Desolation, Screeching Gargoyle, Genji''s Guard, Stone of Binding,
    Void Stone, Void Shield, Obsidian Shard, Breastplate of Valor, Shield of the Phoenix,
    Spear of the Magus, Draconic Scale, Dreamer''s Idol, Oni Hunter''s Garb, Lotus
    Sickle, Erosion, Eye of Providence, Helm of Radiance, Blood-Bound Book, Doom Orb,
    Shifter''s Shield, Helm of Darkness, Midgardian Mail, The World Stone, Leviathan''s
    Hide.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.59
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.66
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.7
      pick: 0.22
      fit: 0.41
    Spear of Desolation:
      total: 0.59
      efficiency: 0.6
      win: 0.67
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.82
      win: 0.67
      pick: 0.0
      fit: 0.4
    Soul Gem:
      total: 0.61
      efficiency: 0.58
      win: 0.67
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Eros' Bow
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Eros' Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Genji''s Guard, Soul
    Gem, Gluttonous Grimoire, Breastplate of Valor, Nimble Ring, Shield of the Phoenix,
    Spear of Desolation, Oni Hunter''s Garb, Lotus Sickle, Draconic Scale, Blood-Bound
    Book, Bragi''s Harp, Helm of Radiance, Screeching Gargoyle, Erosion, Eros'' Bow,
    Eye of Providence, Ancient Signet, Midgardian Mail, Shifter''s Shield, Helm of
    Darkness, Stone of Binding, Death Metal, Leviathan''s Hide, Bracer of The Abyss,
    Chronos'' Pendant.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.44
    Nimble Ring:
      total: 0.55
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.32
    Bragi's Harp:
      total: 0.54
      efficiency: 0.47
      win: 0.67
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.7
      pick: 0.22
      fit: 0.33
    Eros' Bow:
      total: 0.53
      efficiency: 0.5
      win: 0.67
      pick: 0.0
      fit: 0.36
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.34
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Spear of Desolation
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Rod of Tahuti, Amanita
    Charm, Soul Gem, Kinetic Cuirass, Breastplate of Valor, Shield of the Phoenix,
    Spear of Desolation, Lotus Sickle, Screeching Gargoyle, Gluttonous Grimoire, Chronos''
    Pendant, Gladiator''s Shield, Draconic Scale, Oni Hunter''s Garb, Prophetic Cloak,
    Erosion, Eye of Providence, Helm of Radiance, Blood-Bound Book, Shifter''s Shield,
    Gem of Focus, Heartwood Charm, Helm of Darkness, Midgardian Mail, Chandra''s Grace,
    Stone of Binding, Leviathan''s Hide, Regrowth Striders.'
  slot_scores:
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.63
      win: 0.67
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.61
      efficiency: 0.71
      win: 0.64
      pick: 0.13
      fit: 0.45
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.7
      pick: 0.22
      fit: 0.6
    Spear of Desolation:
      total: 0.58
      efficiency: 0.6
      win: 0.67
      pick: 0.0
      fit: 0.42
    Soul Gem:
      total: 0.59
      efficiency: 0.58
      win: 0.67
      pick: 0.0
      fit: 0.59
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge,
    Kinetic Cuirass, Genji''s Guard, Soul Gem, Gluttonous Grimoire, Shield Splitter,
    Spear of Desolation, The Reaper, Breastplate of Valor, Golden Blade, Runeforged
    Hammer, Hydra''s Lament, Shield of the Phoenix, Oni Hunter''s Garb, The Crusher,
    Lotus Sickle, Draconic Scale, Death Metal, Heartseeker, Blood-Bound Book, Helm
    of Radiance, Erosion, Obsidian Shard, Screeching Gargoyle, Bragi''s Harp, Eye
    of Providence, Tekko-Kagi, Nimble Ring, Titan''s Bane, Shifter''s Shield, Midgardian
    Mail, Berserker''s Shield, Helm of Darkness, Arondight, Ancient Signet, Spear
    of the Magus, Toxic Blade, Stone of Binding.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.42
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.64
      pick: 0.13
      fit: 0.22
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.46
    Shield Splitter:
      total: 0.57
      efficiency: 0.58
      win: 0.67
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.7
      pick: 0.22
      fit: 0.35
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Soul
    Gem, Jotunn''s Revenge, Gluttonous Grimoire, Kinetic Cuirass, Genji''s Guard,
    Spear of Desolation, Shield Splitter, Breastplate of Valor, Lotus Sickle, The
    Reaper, Shield of the Phoenix, Blood-Bound Book, Helm of Radiance, Runeforged
    Hammer, Hydra''s Lament, Obsidian Shard, Death Metal, Oni Hunter''s Garb, Draconic
    Scale, Helm of Darkness, Spear of the Magus, Ancient Signet, The Crusher, Chronos''
    Pendant, Erosion, Screeching Gargoyle, Eye of Providence, Polynomicon, Heartseeker,
    Dreamer''s Idol, Shifter''s Shield, Midgardian Mail, Stone of Binding, Jade Scepter,
    Titan''s Bane, Leviathan''s Hide, Magi''s Cloak, Berserker''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.4
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.64
      pick: 0.13
      fit: 0.23
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.7
      pick: 0.22
      fit: 0.37
    Spear of Desolation:
      total: 0.57
      efficiency: 0.6
      win: 0.67
      pick: 0.0
      fit: 0.4
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Genji''s
    Guard, Soul Gem, Gluttonous Grimoire, Shield of the Phoenix, Breastplate of Valor,
    Draconic Scale, Erosion, Eye of Providence, Oni Hunter''s Garb, Spear of Desolation,
    Shifter''s Shield, Helm of Darkness, Lotus Sickle, Helm of Radiance, Screeching
    Gargoyle, Stone of Binding, Midgardian Mail, Blood-Bound Book, Magi''s Cloak,
    Mantle Of Discord, Leviathan''s Hide, Gladiator''s Shield, Hide of the Nemean
    Lion, Prophetic Cloak, Chronos'' Pendant, Ancile.'
  slot_scores:
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.63
      win: 0.67
      pick: 0.0
      fit: 0.36
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.64
      pick: 0.13
      fit: 0.36
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.61
      win: 0.67
      pick: 0.0
      fit: 0.67
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.7
      pick: 0.22
      fit: 0.56
    Draconic Scale:
      total: 0.57
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.63
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
