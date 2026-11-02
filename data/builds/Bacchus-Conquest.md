---
type: smite-build
god: Bacchus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Revelry
  aspect_pick_rate: 0.55
  aspect_win_rate: 0.58
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.37
    win_rate: 0.62
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.17
      win_rate: 0.51
    - name: Stampede
      pick_rate: 0.11
      win_rate: 0.49
  - name: Berserker's Shield
    pick_rate: 0.27
    win_rate: 0.62
    alternates:
    - name: Stampede
      pick_rate: 0.11
      win_rate: 0.48
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.61
  - name: Kinetic Cuirass
    pick_rate: 0.13
    win_rate: 0.62
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.55
    - name: Berserker's Shield
      pick_rate: 0.09
      win_rate: 0.59
  - name: Freya's Tears
    pick_rate: 0.16
    win_rate: 0.57
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.1
      win_rate: 0.63
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.61
  - name: Hide of the Nemean Lion
    pick_rate: 0.05
    win_rate: 0.54
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.71
    - name: Kinetic Cuirass
      pick_rate: 0.08
      win_rate: 0.66
  - name: Medal of Defense
    pick_rate: 0.08
    win_rate: 0.62
    alternates:
    - name: Sage's Ring
      pick_rate: 0.07
      win_rate: 0.62
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.67
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.26
    win_rate: 0.67
  - name: Leather Cowl
    pick_rate: 0.17
    win_rate: 0.52
  - name: Bluestone Pendant
    pick_rate: 0.13
    win_rate: 0.39
  source_url: https://smitebrain.com/gods/bacchus/
  last_verified: '2026-10-30'
  god_win_rate: 0.5658409387222947
  god_matches_won: 434
  god_matches_played: 767
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-30'
  god_matches_analyzed: 10706
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Genji's Guard
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
    this god: Amanita Charm, Rod of Tahuti, Shifter''s Shield, Genji''s Guard, Erosion,
    Breastplate of Valor, Jotunn''s Revenge, Eye of Providence, Draconic Scale, Shield
    Splitter, Shield of the Phoenix, Stone of Binding, Magi''s Cloak, Eye of the Storm,
    Gluttonous Grimoire, Helm of Radiance, Mantle Of Discord, Midgardian Mail, Runeforged
    Hammer, Oni Hunter''s Garb, Screeching Gargoyle, Leviathan''s Hide, Prophetic
    Cloak, Void Shield, Ancile, Helm of Darkness, Spectral Armor, Hussar''s Wings,
    Spear of Desolation, Void Stone, Xibalban Effigy, Gladiator''s Shield, Rod of
    Asclepius, Daybreak Gavel, Hydra''s Lament, Doublet of Binding, Soul Gem, Hide
    of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.1
      fit: 0.37
    Berserker's Shield:
      total: 0.57
      efficiency: 0.6
      win: 0.62
      pick: 0.37
      fit: 0.44
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.57
      win: 0.62
      pick: 0.2
      fit: 0.78
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.57
      pick: 0.27
      fit: 0.62
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.68
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Shield of the Phoenix
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Rod of Asclepius,
    Shifter''s Shield, Genji''s Guard, Jotunn''s Revenge, Soul Gem, Erosion, Eye of
    Providence, Breastplate of Valor, Draconic Scale, Ethereal Staff, Phoenix Feather,
    Yogi''s Necklace, Gluttonous Grimoire, Chandra''s Grace, Shield Splitter, Runeforged
    Hammer, Eye of the Storm, Glorious Pridwen, Midgardian Mail, Lifebinder, Oni Hunter''s
    Garb, Stone of Binding, Helm of Radiance, Leviathan''s Hide, Void Shield, Ancile,
    Magi''s Cloak, Daybreak Gavel, Spectral Armor, Sphere of Negation, Gladiator''s
    Shield, Void Stone, Screeching Gargoyle, Spear of Desolation, Hide of the Nemean
    Lion.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.6
      win: 0.62
      pick: 0.37
      fit: 0.46
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.9
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.57
      win: 0.62
      pick: 0.2
      fit: 0.76
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.57
      pick: 0.27
      fit: 0.54
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.66
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Screeching Gargoyle, Spear of Desolation, Genji''s Guard,
    Void Shield, Spear of the Magus, Soul Gem, Breastplate of Valor, Obsidian Shard,
    Void Stone, Shifter''s Shield, Avenging Blade, Erosion, Eye of Providence, Shield
    Splitter, Heartseeker, Draconic Scale, Shield of the Phoenix, Doom Orb, Helm of
    Radiance, The World Stone, Runeforged Hammer, Titan''s Bane, Magi''s Cloak, Dreamer''s
    Idol, The Crusher, Eye of the Storm, Midgardian Mail, Mantle Of Discord, Oni Hunter''s
    Garb, The Reaper, Daybreak Gavel, Leviathan''s Hide, Rod of Asclepius, Hide of
    the Nemean Lion.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.55
      efficiency: 0.5
      win: 0.61
      pick: 0.0
      fit: 0.66
    Stone of Binding:
      total: 0.56
      efficiency: 0.5
      win: 0.61
      pick: 0.0
      fit: 0.74
    Berserker's Shield:
      total: 0.55
      efficiency: 0.6
      win: 0.62
      pick: 0.37
      fit: 0.31
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.57
      win: 0.62
      pick: 0.2
      fit: 0.58
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Nimble Ring
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Golden Blade
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Nimble Ring, Genji''s
    Guard, Golden Blade, Gluttonous Grimoire, Breastplate of Valor, Tyrfing, Shifter''s
    Shield, Shield Splitter, Soul Gem, Pharaoh''s Curse, Runeforged Hammer, Riptalon,
    Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Helm of Radiance, Eye
    of Providence, Hydra''s Lament, Toxic Blade, Shield of the Phoenix, Eye of the
    Storm, Stone of Binding, Draconic Scale, Magi''s Cloak, Daybreak Gavel, Spear
    of the Magus, Spear of Desolation, Midgardian Mail, Screeching Gargoyle, The Reaper,
    Bragi''s Harp, Tekko-Kagi, Oni Hunter''s Garb, Rod of Asclepius, Mantle Of Discord.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.62
      pick: 0.37
      fit: 0.43
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.21
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.57
      win: 0.62
      pick: 0.2
      fit: 0.47
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.3
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Genji''s Guard, Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Spear
    of Desolation, Hydra''s Lament, Soul Gem, Lotus Sickle, Screeching Gargoyle, Shifter''s
    Shield, Chronos'' Pendant, Shield Splitter, Prophetic Cloak, Helm of Radiance,
    Erosion, Gluttonous Grimoire, Runeforged Hammer, Eye of Providence, Gladiator''s
    Shield, Draconic Scale, Stone of Binding, Eye of the Storm, Gem of Focus, Arondight,
    Magi''s Cloak, Spear of the Magus, Rod of Asclepius, Eye of Erebus, Midgardian
    Mail, Mantle Of Discord, Oni Hunter''s Garb, Glorious Pridwen, Daybreak Gavel,
    Obsidian Shard, Chandra''s Grace, Jade Scepter, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.61
      pick: 0.1
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.64
      win: 0.61
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.57
      win: 0.62
      pick: 0.2
      fit: 0.55
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.57
      pick: 0.27
      fit: 0.64
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
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
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    Charm, Shield Splitter, Genji''s Guard, Runeforged Hammer, Golden Blade, Breastplate
    of Valor, Eye of the Storm, Shifter''s Shield, Gluttonous Grimoire, Hydra''s Lament,
    Heartseeker, Tyrfing, Erosion, Spear of Desolation, Lernaean Bow, Spear of the
    Magus, Eye of Providence, Tekko-Kagi, Avenging Blade, Draconic Scale, Shield of
    the Phoenix, Helm of Radiance, Stone of Binding, Soul Gem, Titan''s Bane, Obsidian
    Shard, The Crusher, Pharaoh''s Curse, Silverbranch Bow, Magi''s Cloak, The Reaper,
    Toxic Blade, Nimble Ring, Shogun''s Ofuda, Midgardian Mail, Daybreak Gavel, Screeching
    Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.61
      pick: 0.1
      fit: 0.23
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.62
      pick: 0.37
      fit: 0.36
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.57
      win: 0.62
      pick: 0.2
      fit: 0.52
    Shield Splitter:
      total: 0.55
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Gluttonous Grimoire, Genji''s Guard, Spear of Desolation, Shield
    Splitter, Spear of the Magus, Breastplate of Valor, Helm of Radiance, Soul Gem,
    Runeforged Hammer, Obsidian Shard, Shifter''s Shield, Eye of the Storm, Hydra''s
    Lament, Rod of Asclepius, Erosion, Eye of Providence, Lotus Sickle, Heartseeker,
    Draconic Scale, Shield of the Phoenix, Jade Scepter, Stone of Binding, Doom Orb,
    Death Metal, Avenging Blade, Wish-Granting Pearl, The World Stone, Magi''s Cloak,
    Chronos'' Pendant, Helm of Darkness, Titan''s Bane, The Crusher, Dreamer''s Idol,
    Triton''s Conch, Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.5
      win: 0.61
      pick: 0.0
      fit: 0.18
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.57
      win: 0.62
      pick: 0.2
      fit: 0.52
    Transcendence:
      total: 0.49
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.18
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.85
      win: 0.61
      pick: 0.0
      fit: 0.33
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Shifter''s Shield, Genji''s
    Guard, Erosion, Breastplate of Valor, Jotunn''s Revenge, Eye of Providence, Draconic
    Scale, Shield Splitter, Shield of the Phoenix, Stone of Binding, Magi''s Cloak,
    Eye of the Storm, Gluttonous Grimoire, Helm of Radiance, Mantle Of Discord, Midgardian
    Mail, Runeforged Hammer, Oni Hunter''s Garb, Screeching Gargoyle, Leviathan''s
    Hide, Hide of the Nemean Lion, Prophetic Cloak, Void Shield, Ancile, Helm of Darkness,
    Spectral Armor, Hussar''s Wings, Spear of Desolation, Void Stone, Xibalban Effigy,
    Gladiator''s Shield, Rod of Asclepius, Daybreak Gavel, Hydra''s Lament, Doublet
    of Binding, Soul Gem.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.1
      fit: 0.37
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.57
      win: 0.62
      pick: 0.2
      fit: 0.78
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.57
      pick: 0.27
      fit: 0.62
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.68
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.68
    Erosion:
      total: 0.56
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
---
