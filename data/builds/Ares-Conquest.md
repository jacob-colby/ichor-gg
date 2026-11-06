---
type: smite-build
god: Ares
mode: Conquest
builds:
- source: community
  aspect: Aspect of Reverberation
  aspect_pick_rate: 0.27
  aspect_win_rate: 0.56
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.4
    win_rate: 0.58
    alternates:
    - name: Stampede
      pick_rate: 0.15
      win_rate: 0.67
    - name: Circe's Hexstone
      pick_rate: 0.12
      win_rate: 0.71
  - name: Stampede
    pick_rate: 0.24
    win_rate: 0.48
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.69
    - name: Kinetic Cuirass
      pick_rate: 0.12
      win_rate: 0.79
  - name: Shell of Rebuke
    pick_rate: 0.16
    win_rate: 0.68
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.36
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.8
  - name: Freya's Tears
    pick_rate: 0.24
    win_rate: 0.74
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.12
      win_rate: 0.62
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.56
  - name: Genji's Guard
    pick_rate: 0.05
    win_rate: 0.4
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.57
    - name: Kinetic Cuirass
      pick_rate: 0.05
      win_rate: 0.4
  - name: Olmec Blue
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Veve Charm
      pick_rate: 0.11
      win_rate: 0.57
    - name: Medal of Defense
      pick_rate: 0.08
      win_rate: 0.8
  community_starters:
  - name: Selflessness
    pick_rate: 0.29
    win_rate: 0.57
  - name: Heroism
    pick_rate: 0.16
    win_rate: 0.74
  - name: Bluestone Pendant
    pick_rate: 0.08
    win_rate: 0.4
  source_url: https://smitebrain.com/gods/ares/
  last_verified: '2026-11-06'
  god_win_rate: 0.5833333333333334
  god_matches_won: 70
  god_matches_played: 120
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
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Draconic Scale
  - Shield Splitter
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Berserker''s Shield, Shield of the Phoenix,
    Draconic Scale, Shield Splitter, Gluttonous Grimoire, Breastplate of Valor, Soul
    Gem, Erosion, Eye of Providence, Shifter''s Shield, Oni Hunter''s Garb, Jotunn''s
    Revenge, Stone of Binding, Midgardian Mail, Screeching Gargoyle, Helm of Darkness,
    Magi''s Cloak, Mantle Of Discord, Leviathan''s Hide, Spear of Desolation, Hide
    of the Nemean Lion, Helm of Radiance, Gladiator''s Shield, Lotus Sickle, Runeforged
    Hammer, Prophetic Cloak, Ancile, Blood-Bound Book, Void Stone, Phoenix Feather,
    Hydra''s Lament, Void Shield, Spectral Armor, The Reaper, Doublet of Binding,
    Hussar''s Wings, Genji''s Guard.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.66
      win: 0.63
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.68
      efficiency: 0.61
      win: 0.79
      pick: 0.16
      fit: 0.7
    Shield Splitter:
      total: 0.56
      efficiency: 0.58
      win: 0.63
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.74
      pick: 0.4
      fit: 0.56
    Draconic Scale:
      total: 0.56
      efficiency: 0.53
      win: 0.63
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Soul Gem, Rod of Tahuti, Berserker''s
    Shield, Phoenix Feather, Blood-Bound Book, Gluttonous Grimoire, The Reaper, Yogi''s
    Necklace, Draconic Scale, Ethereal Staff, Chandra''s Grace, Breastplate of Valor,
    Oni Hunter''s Garb, Erosion, Jotunn''s Revenge, Shield Splitter, Eye of Providence,
    Shifter''s Shield, Regrowth Striders, Midgardian Mail, Glorious Pridwen, Bancroft''s
    Talon, Leviathan''s Hide, Rod of Asclepius, Runeforged Hammer, Spear of Desolation,
    Hide of the Nemean Lion, Soul Locket, Screeching Gargoyle, Gladiator''s Shield,
    Lotus Sickle, Ancile, Stone of Binding, Helm of Darkness, Void Stone, Helm of
    Radiance, Genji''s Guard.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.66
      win: 0.63
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.68
      efficiency: 0.61
      win: 0.79
      pick: 0.16
      fit: 0.68
    Shield of the Phoenix:
      total: 0.61
      efficiency: 0.57
      win: 0.63
      pick: 0.0
      fit: 0.84
    Freya's Tears:
      total: 0.64
      efficiency: 0.61
      win: 0.74
      pick: 0.4
      fit: 0.49
    Draconic Scale:
      total: 0.56
      efficiency: 0.53
      win: 0.63
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.65
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Screeching Gargoyle
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Gluttonous Grimoire, Soul Gem, Jotunn''s
    Revenge, Screeching Gargoyle, Stone of Binding, Spear of Desolation, Berserker''s
    Shield, Void Stone, Void Shield, The Reaper, Breastplate of Valor, Shield Splitter,
    Shield of the Phoenix, Obsidian Shard, Draconic Scale, Avenging Blade, Oni Hunter''s
    Garb, Spear of the Magus, The Crusher, Erosion, Eye of Providence, Heartseeker,
    Dreamer''s Idol, Shifter''s Shield, Midgardian Mail, Titan''s Bane, Lotus Sickle,
    Helm of Radiance, Leviathan''s Hide, Doom Orb, Runeforged Hammer, Blood-Bound
    Book, Magi''s Cloak, Mantle Of Discord, Helm of Darkness, Hide of the Nemean Lion,
    Hydra''s Lament, Genji''s Guard.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.57
      efficiency: 0.53
      win: 0.63
      pick: 0.0
      fit: 0.65
    Stone of Binding:
      total: 0.56
      efficiency: 0.49
      win: 0.63
      pick: 0.0
      fit: 0.71
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.66
      efficiency: 0.61
      win: 0.79
      pick: 0.16
      fit: 0.54
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.74
      pick: 0.4
      fit: 0.41
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.44
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Tyrfing, Jotunn''s
    Revenge, Shield Splitter, Golden Blade, Breastplate of Valor, Gluttonous Grimoire,
    Soul Gem, Shield of the Phoenix, Oni Hunter''s Garb, Nimble Ring, Draconic Scale,
    Runeforged Hammer, Shogun''s Ofuda, Hydra''s Lament, Pharaoh''s Curse, Erosion,
    Spear of Desolation, Eye of Providence, Lotus Sickle, Toxic Blade, Screeching
    Gargoyle, Bragi''s Harp, Shifter''s Shield, Midgardian Mail, The Reaper, Blood-Bound
    Book, Helm of Radiance, Stone of Binding, Eros'' Bow, Lernaean Bow, Dominance,
    Leviathan''s Hide, Silverbranch Bow, Magi''s Cloak, Mantle Of Discord, Hide of
    the Nemean Lion, Genji''s Guard.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.51
      win: 0.63
      pick: 0.0
      fit: 0.53
    Berserker's Shield:
      total: 0.6
      efficiency: 0.72
      win: 0.63
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.65
      efficiency: 0.61
      win: 0.79
      pick: 0.16
      fit: 0.46
    Tyrfing:
      total: 0.55
      efficiency: 0.53
      win: 0.63
      pick: 0.0
      fit: 0.53
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.74
      pick: 0.4
      fit: 0.34
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Soul
    Gem, Jotunn''s Revenge, Breastplate of Valor, Shield of the Phoenix, Spear of
    Desolation, Lotus Sickle, Berserker''s Shield, Screeching Gargoyle, Hydra''s Lament,
    Gluttonous Grimoire, Shield Splitter, Chronos'' Pendant, Gladiator''s Shield,
    Draconic Scale, Oni Hunter''s Garb, Prophetic Cloak, Arondight, Erosion, Eye of
    Providence, Helm of Radiance, Runeforged Hammer, Blood-Bound Book, Shifter''s
    Shield, Gem of Focus, Heartwood Charm, Helm of Darkness, Midgardian Mail, Chandra''s
    Grace, Stone of Binding, Leviathan''s Hide, Regrowth Striders, Ancient Signet,
    Magi''s Cloak, Mantle Of Discord, The Reaper, Hide of the Nemean Lion, Eye of
    Erebus, Genji''s Guard.'
  slot_scores:
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.63
      win: 0.63
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.65
      efficiency: 0.61
      win: 0.79
      pick: 0.16
      fit: 0.52
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.74
      pick: 0.4
      fit: 0.6
    Spear of Desolation:
      total: 0.56
      efficiency: 0.6
      win: 0.63
      pick: 0.0
      fit: 0.42
    Soul Gem:
      total: 0.58
      efficiency: 0.58
      win: 0.63
      pick: 0.0
      fit: 0.59
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
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
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Amanita
    Charm, Jotunn''s Revenge, Shield Splitter, Gluttonous Grimoire, Soul Gem, The
    Reaper, Tyrfing, Breastplate of Valor, Runeforged Hammer, Hydra''s Lament, Golden
    Blade, Spear of Desolation, Shield of the Phoenix, The Crusher, Oni Hunter''s
    Garb, Draconic Scale, Heartseeker, Erosion, Eye of Providence, Tekko-Kagi, Titan''s
    Bane, Death Metal, Screeching Gargoyle, Shifter''s Shield, Lotus Sickle, Midgardian
    Mail, Stone of Binding, Bragi''s Harp, Helm of Radiance, Blood-Bound Book, Obsidian
    Shard, Arondight, Avenging Blade, Leviathan''s Hide, Magi''s Cloak, Mantle Of
    Discord, Nimble Ring, Genji''s Guard.'
  slot_scores:
    Berserker's Shield:
      total: 0.59
      efficiency: 0.72
      win: 0.63
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.65
      efficiency: 0.61
      win: 0.79
      pick: 0.16
      fit: 0.49
    Shield Splitter:
      total: 0.56
      efficiency: 0.58
      win: 0.63
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.74
      pick: 0.4
      fit: 0.36
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Genji''s Guard, Berserker''s
    Shield, Shield of the Phoenix, Draconic Scale, Shield Splitter, Gluttonous Grimoire,
    Breastplate of Valor, Soul Gem, Erosion, Eye of Providence, Shifter''s Shield,
    Oni Hunter''s Garb, Jotunn''s Revenge, Stone of Binding, Midgardian Mail, Screeching
    Gargoyle, Helm of Darkness, Magi''s Cloak, Mantle Of Discord, Leviathan''s Hide,
    Spear of Desolation, Hide of the Nemean Lion, Helm of Radiance, Gladiator''s Shield,
    Lotus Sickle, Runeforged Hammer, Prophetic Cloak, Ancile, Blood-Bound Book, Void
    Stone, Phoenix Feather, Hydra''s Lament, Void Shield, Spectral Armor, The Reaper,
    Doublet of Binding, Hussar''s Wings.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.66
      win: 0.63
      pick: 0.0
      fit: 0.39
    Genji's Guard:
      total: 0.49
      efficiency: 0.71
      win: 0.4
      pick: 0.11
      fit: 0.34
    Kinetic Cuirass:
      total: 0.68
      efficiency: 0.61
      win: 0.79
      pick: 0.16
      fit: 0.7
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.74
      pick: 0.4
      fit: 0.56
    Draconic Scale:
      total: 0.56
      efficiency: 0.53
      win: 0.63
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
---
