---
type: smite-build
god: Ymir
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.18
    win_rate: 0.61
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.18
      win_rate: 0.58
    - name: Avenging Blade
      pick_rate: 0.12
      win_rate: 0.52
  - name: Berserker's Shield
    pick_rate: 0.22
    win_rate: 0.6
    alternates:
    - name: Stampede
      pick_rate: 0.15
      win_rate: 0.6
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.51
  - name: Kinetic Cuirass
    pick_rate: 0.1
    win_rate: 0.6
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.6
    - name: Berserker's Shield
      pick_rate: 0.09
      win_rate: 0.59
  - name: Freya's Tears
    pick_rate: 0.12
    win_rate: 0.61
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.1
      win_rate: 0.67
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.59
  - name: Hussar's Wings
    pick_rate: 0.05
    win_rate: 0.72
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.63
    - name: Kinetic Cuirass
      pick_rate: 0.05
      win_rate: 0.6
  - name: Medal of Defense
    pick_rate: 0.08
    win_rate: 0.61
    alternates:
    - name: Sage's Ring
      pick_rate: 0.06
      win_rate: 0.67
    - name: Veve Charm
      pick_rate: 0.06
      win_rate: 0.71
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.26
    win_rate: 0.66
  - name: Leather Cowl
    pick_rate: 0.25
    win_rate: 0.49
  - name: Warrior's Axe
    pick_rate: 0.1
    win_rate: 0.58
  source_url: https://smitebrain.com/gods/ymir/
  last_verified: '2026-11-02'
  god_win_rate: 0.5800627943485086
  god_matches_won: 739
  god_matches_played: 1274
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14397
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Hussar's Wings
  - Amanita Charm
  - Erosion
  flex_slots:
  - Genji's Guard
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Hussar''s Wings, Genji''s Guard, Rod of Tahuti, Erosion,
    Eye of Providence, Draconic Scale, Breastplate of Valor, Shield of the Phoenix,
    Helm of Darkness, Oni Hunter''s Garb, Stone of Binding, Magi''s Cloak, Midgardian
    Mail, Mantle Of Discord, Leviathan''s Hide, Helm of Radiance, Screeching Gargoyle,
    Prophetic Cloak, Ancile, Hide of the Nemean Lion, Void Stone, Xibalban Effigy,
    Void Shield, Gladiator''s Shield, Spectral Armor, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.53
      win: 0.6
      pick: 0.16
      fit: 0.82
    Freya's Tears:
      total: 0.57
      efficiency: 0.55
      win: 0.61
      pick: 0.2
      fit: 0.64
    Hussar's Wings:
      total: 0.56
      efficiency: 0.36
      win: 0.72
      pick: 0.11
      fit: 0.72
    Amanita Charm:
      total: 0.59
      efficiency: 0.62
      win: 0.6
      pick: 0.0
      fit: 0.72
    Erosion:
      total: 0.55
      efficiency: 0.48
      win: 0.6
      pick: 0.0
      fit: 0.72
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Hussar's Wings
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Hussar's Wings
  - Amanita Charm
  flex_slots:
  - Hussar's Wings
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Genji''s Guard, Rod of Tahuti,
    Phoenix Feather, Erosion, Eye of Providence, Draconic Scale, Yogi''s Necklace,
    Ethereal Staff, Breastplate of Valor, Chandra''s Grace, Oni Hunter''s Garb, Glorious
    Pridwen, Midgardian Mail, Soul Gem, Leviathan''s Hide, Helm of Darkness, Rod of
    Asclepius, Stone of Binding, Regrowth Striders, Ancile, Hide of the Nemean Lion,
    Sphere of Negation, Magi''s Cloak, Void Stone, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.53
      win: 0.6
      pick: 0.16
      fit: 0.8
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.56
      efficiency: 0.55
      win: 0.61
      pick: 0.2
      fit: 0.57
    Hussar's Wings:
      total: 0.56
      efficiency: 0.36
      win: 0.72
      pick: 0.11
      fit: 0.7
    Amanita Charm:
      total: 0.64
      efficiency: 0.62
      win: 0.6
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Hussar's Wings
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Screeching Gargoyle, Obsidian Shard, Genji''s Guard, Spear of Desolation, Soul
    Gem, Void Stone, Void Shield, Breastplate of Valor, Spear of the Magus, Erosion,
    Doom Orb, Eye of Providence, Draconic Scale, The World Stone, Oni Hunter''s Garb,
    Shield of the Phoenix, Helm of Darkness, Midgardian Mail, Helm of Radiance, Magi''s
    Cloak, Mantle Of Discord, Leviathan''s Hide, Dreamer''s Idol, Shifter''s Shield.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.54
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.65
    Stone of Binding:
      total: 0.55
      efficiency: 0.47
      win: 0.6
      pick: 0.0
      fit: 0.74
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.53
      win: 0.6
      pick: 0.16
      fit: 0.58
    Freya's Tears:
      total: 0.54
      efficiency: 0.55
      win: 0.61
      pick: 0.2
      fit: 0.42
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.81
      win: 0.6
      pick: 0.0
      fit: 0.4
    Amanita Charm:
      total: 0.56
      efficiency: 0.62
      win: 0.6
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Nimble Ring
  - Bragi's Harp
  - Eros' Bow
  - Amanita Charm
  flex_slots:
  - Eros' Bow
  - Bragi's Harp
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Genji''s Guard, Breastplate
    of Valor, Eros'' Bow, Oni Hunter''s Garb, Erosion, Eye of Providence, Stone of
    Binding, Helm of Radiance, Draconic Scale, Shield of the Phoenix, Midgardian Mail,
    Soul Gem, Screeching Gargoyle, Sundering Echo, Helm of Darkness, Magi''s Cloak,
    Leviathan''s Hide, Mantle Of Discord, Blood-Bound Book, Gluttonous Grimoire, Bragi''s
    Harp, Bracer of The Abyss, Ancile, Hide of the Nemean Lion, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.2
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.53
      win: 0.6
      pick: 0.16
      fit: 0.48
    Nimble Ring:
      total: 0.53
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.48
      efficiency: 0.41
      win: 0.6
      pick: 0.0
      fit: 0.45
    Eros' Bow:
      total: 0.5
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.35
    Amanita Charm:
      total: 0.54
      efficiency: 0.62
      win: 0.6
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Prophetic Cloak — magical protection
    swap_item: Prophetic Cloak
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Amanita Charm, Rod of Tahuti, Shield of the Phoenix, Screeching Gargoyle, Chronos''
    Pendant, Prophetic Cloak, Soul Gem, Erosion, Gladiator''s Shield, Eye of Providence,
    Helm of Radiance, Helm of Darkness, Oni Hunter''s Garb, Draconic Scale, Stone
    of Binding, Heartwood Charm, Gem of Focus, Chandra''s Grace, Spear of Desolation,
    Midgardian Mail, Magi''s Cloak, Sundering Echo, Glorious Pridwen, Mantle Of Discord,
    Leviathan''s Hide, Shifter''s Shield.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.53
      efficiency: 0.49
      win: 0.6
      pick: 0.0
      fit: 0.58
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.53
      win: 0.6
      pick: 0.16
      fit: 0.55
    Freya's Tears:
      total: 0.57
      efficiency: 0.55
      win: 0.61
      pick: 0.2
      fit: 0.64
    Amanita Charm:
      total: 0.55
      efficiency: 0.62
      win: 0.6
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita
    Charm, Shield Splitter, Genji''s Guard, Golden Blade, Tekko-Kagi, Titan''s Bane,
    Runeforged Hammer, Breastplate of Valor, Gluttonous Grimoire, Hydra''s Lament,
    Obsidian Shard, Tyrfing, Spear of Desolation, Sundering Echo, Erosion, Heartseeker,
    Soul Gem, Toxic Blade, Oni Hunter''s Garb, The Crusher, Eye of Providence, Lernaean
    Bow, Draconic Scale, Stone of Binding, Silverbranch Bow, Shield of the Phoenix,
    Helm of Radiance, Midgardian Mail, Pharaoh''s Curse, The Reaper, Helm of Darkness,
    Magi''s Cloak, Screeching Gargoyle, Wyrmskin Hide, Spear of the Magus, Mantle
    Of Discord, Avenging Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.22
    Berserker's Shield:
      total: 0.59
      efficiency: 0.7
      win: 0.6
      pick: 0.3
      fit: 0.36
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.53
      win: 0.6
      pick: 0.16
      fit: 0.52
    Shield Splitter:
      total: 0.54
      efficiency: 0.54
      win: 0.6
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.55
      efficiency: 0.62
      win: 0.6
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Genji''s Guard, Gluttonous Grimoire, Shield Splitter, Obsidian
    Shard, Spear of Desolation, Soul Gem, Sundering Echo, Breastplate of Valor, Helm
    of Radiance, Titan''s Bane, Runeforged Hammer, Helm of Darkness, Spear of the
    Magus, Golden Blade, Tekko-Kagi, Hydra''s Lament, Erosion, Oni Hunter''s Garb,
    Death Metal, Nimble Ring, Eye of Providence, Doom Orb, Draconic Scale, Stone of
    Binding, The World Stone, Shield of the Phoenix, Heartseeker, Eros'' Bow, Midgardian
    Mail, Tyrfing, The Crusher, Toxic Blade, Magi''s Cloak, Jade Scepter, Screeching
    Gargoyle, Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.22
    Berserker's Shield:
      total: 0.58
      efficiency: 0.7
      win: 0.6
      pick: 0.3
      fit: 0.3
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.53
      win: 0.6
      pick: 0.16
      fit: 0.5
    Freya's Tears:
      total: 0.53
      efficiency: 0.55
      win: 0.61
      pick: 0.2
      fit: 0.36
    Amanita Charm:
      total: 0.55
      efficiency: 0.62
      win: 0.6
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Genji''s Guard, Rod of Tahuti, Erosion,
    Eye of Providence, Draconic Scale, Breastplate of Valor, Shifter''s Shield, Shield
    of the Phoenix, Helm of Darkness, Oni Hunter''s Garb, Stone of Binding, Magi''s
    Cloak, Midgardian Mail, Mantle Of Discord, Leviathan''s Hide, Helm of Radiance,
    Screeching Gargoyle, Prophetic Cloak, Ancile, Hide of the Nemean Lion, Void Stone,
    Xibalban Effigy, Void Shield, Hussar''s Wings, Gladiator''s Shield, Spectral Armor.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.47
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.53
      win: 0.6
      pick: 0.16
      fit: 0.82
    Freya's Tears:
      total: 0.57
      efficiency: 0.55
      win: 0.61
      pick: 0.2
      fit: 0.64
    Amanita Charm:
      total: 0.59
      efficiency: 0.62
      win: 0.6
      pick: 0.0
      fit: 0.72
    Erosion:
      total: 0.55
      efficiency: 0.48
      win: 0.6
      pick: 0.0
      fit: 0.72
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Hussar's Wings
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Hussar's Wings
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Genji''s Guard, Rod
    of Tahuti, Erosion, Eye of Providence, Draconic Scale, Breastplate of Valor, Shifter''s
    Shield, Shield of the Phoenix, Helm of Darkness, Oni Hunter''s Garb, Stone of
    Binding, Magi''s Cloak, Midgardian Mail, Mantle Of Discord, Leviathan''s Hide,
    Helm of Radiance, Screeching Gargoyle, Prophetic Cloak, Ancile, Hide of the Nemean
    Lion, Void Stone, Xibalban Effigy, Void Shield, Hussar''s Wings, Gladiator''s
    Shield, Spectral Armor.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.53
      win: 0.6
      pick: 0.16
      fit: 0.82
    Freya's Tears:
      total: 0.57
      efficiency: 0.55
      win: 0.61
      pick: 0.2
      fit: 0.64
    Hussar's Wings:
      total: 0.56
      efficiency: 0.36
      win: 0.72
      pick: 0.11
      fit: 0.72
    Amanita Charm:
      total: 0.59
      efficiency: 0.62
      win: 0.6
      pick: 0.0
      fit: 0.72
    Erosion:
      total: 0.55
      efficiency: 0.48
      win: 0.6
      pick: 0.0
      fit: 0.72
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Hussar's Wings
  swaps:
  - added: Hussar's Wings
    removed: Eye of Providence
    reason: community 72% win over 64 matches (vs 58% on this god), taking the model's
      weakest slot from Eye of Providence
  starter: *id001
---
