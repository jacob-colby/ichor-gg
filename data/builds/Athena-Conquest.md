---
type: smite-build
god: Athena
mode: Conquest
builds:
- source: community
  aspect: Aspect of War
  aspect_pick_rate: 0.24
  aspect_win_rate: 0.54
  slot_order:
  - name: Stampede
    pick_rate: 0.25
    win_rate: 0.57
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.22
      win_rate: 0.57
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.5
  - name: Genji's Guard
    pick_rate: 0.14
    win_rate: 0.6
    alternates:
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.55
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.54
  - name: Freya's Tears
    pick_rate: 0.14
    win_rate: 0.61
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.55
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.62
  - name: Shell of Rebuke
    pick_rate: 0.14
    win_rate: 0.63
    alternates:
    - name: Freya's Tears
      pick_rate: 0.15
      win_rate: 0.57
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.44
  - name: Spirit Robe
    pick_rate: 0.05
    win_rate: 0.85
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.61
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.76
  - name: Engraved Guard
    pick_rate: 0.05
    win_rate: 0.63
    alternates:
    - name: Veve Charm
      pick_rate: 0.04
      win_rate: 0.71
    - name: Olmec Blue
      pick_rate: 0.04
      win_rate: 0.5
  community_starters:
  - name: Selflessness
    pick_rate: 0.22
    win_rate: 0.55
  - name: Bumba's Cudgel
    pick_rate: 0.15
    win_rate: 0.45
  - name: Bumba's Hammer
    pick_rate: 0.14
    win_rate: 0.61
  source_url: https://smitebrain.com/gods/athena/
  last_verified: '2026-10-03'
  god_win_rate: 0.5696821515892421
  god_matches_won: 466
  god_matches_played: 818
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-10-03'
  god_matches_analyzed: 12830
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s Shield, Jotunn''s
    Revenge, Erosion, Eye of Providence, Draconic Scale, Berserker''s Shield, Shield
    Splitter, Shield of the Phoenix, Stone of Binding, Magi''s Cloak, Breastplate
    of Valor, Eye of the Storm, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord,
    Midgardian Mail, Runeforged Hammer, Screeching Gargoyle, Hide of the Nemean Lion,
    Prophetic Cloak, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s Garb, Helm
    of Darkness, Xibalban Effigy, Void Stone, Spear of Desolation, Spectral Armor,
    Hussar''s Wings, Rod of Asclepius, Gladiator''s Shield, Daybreak Gavel, Soul Gem,
    Doublet of Binding, Hydra''s Lament.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.19
      fit: 0.37
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.61
      pick: 0.22
      fit: 0.62
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.62
      pick: 0.12
      fit: 0.68
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Spirit Robe
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Shifter''s Shield, Rod of Asclepius, Jotunn''s Revenge, Soul Gem, Berserker''s
    Shield, Erosion, Eye of Providence, Draconic Scale, Ethereal Staff, Phoenix Feather,
    Gluttonous Grimoire, Yogi''s Necklace, Shield Splitter, Chandra''s Grace, Runeforged
    Hammer, Glorious Pridwen, Eye of the Storm, Lifebinder, Midgardian Mail, Stone
    of Binding, Breastplate of Valor, Hide of the Nemean Lion, Helm of Radiance, Leviathan''s
    Hide, Void Shield, Magi''s Cloak, Ancile, Oni Hunter''s Garb, Daybreak Gavel,
    Sphere of Negation, Screeching Gargoyle, Void Stone, Mantle Of Discord, Spectral
    Armor, Gladiator''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.76
    Spirit Robe:
      total: 0.61
      efficiency: 0.34
      win: 0.85
      pick: 0.11
      fit: 0.71
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.61
      pick: 0.22
      fit: 0.54
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.62
      pick: 0.12
      fit: 0.66
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Spirit Robe
  - Freya's Tears
  - Shifter's Shield
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
  - Kinetic Cuirass
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Kinetic Cuirass, Screeching Gargoyle, Shifter''s Shield,
    Spear of Desolation, Void Shield, Spear of the Magus, Soul Gem, Void Stone, Obsidian
    Shard, Avenging Blade, Berserker''s Shield, Heartseeker, Erosion, Shield Splitter,
    Eye of Providence, Draconic Scale, Shield of the Phoenix, Doom Orb, Breastplate
    of Valor, Helm of Radiance, Runeforged Hammer, The World Stone, Titan''s Bane,
    Magi''s Cloak, The Crusher, Dreamer''s Idol, Eye of the Storm, Mantle Of Discord,
    Midgardian Mail, The Reaper, Daybreak Gavel, Hide of the Nemean Lion, Rod of Asclepius,
    Leviathan''s Hide, Hydra''s Lament.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.55
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.66
    Stone of Binding:
      total: 0.56
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.74
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.58
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.61
      pick: 0.22
      fit: 0.43
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Nimble Ring, Kinetic Cuirass, Golden Blade, Gluttonous Grimoire, Shifter''s Shield,
    Tyrfing, Shield Splitter, Soul Gem, Runeforged Hammer, Pharaoh''s Curse, Riptalon,
    Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Helm of Radiance, Breastplate
    of Valor, Eye of Providence, Stone of Binding, Eye of the Storm, Shield of the
    Phoenix, Hydra''s Lament, Toxic Blade, Draconic Scale, Magi''s Cloak, Screeching
    Gargoyle, Daybreak Gavel, The Reaper, Spear of Desolation, Spear of the Magus,
    Bragi''s Harp, Midgardian Mail, Mantle Of Discord, Tekko-Kagi, Rod of Asclepius,
    Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.2
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.61
      pick: 0.22
      fit: 0.33
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Freya's Tears
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
  - Kinetic Cuirass
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Breastplate of Valor, Shifter''s
    Shield, Spear of Desolation, Hydra''s Lament, Screeching Gargoyle, Soul Gem, Chronos''
    Pendant, Shield Splitter, Berserker''s Shield, Prophetic Cloak, Erosion, Helm
    of Radiance, Runeforged Hammer, Gluttonous Grimoire, Eye of Providence, Gladiator''s
    Shield, Draconic Scale, Stone of Binding, Eye of the Storm, Arondight, Gem of
    Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus, Mantle
    Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Chandra''s Grace,
    Obsidian Shard, Hide of the Nemean Lion, Leviathan''s Hide, Jade Scepter, Void
    Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.6
      pick: 0.19
      fit: 0.48
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.54
      pick: 0.12
      fit: 0.48
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.61
      pick: 0.22
      fit: 0.64
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
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
  - Kinetic Cuirass
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Shifter''s Shield, Runeforged
    Hammer, Golden Blade, Eye of the Storm, Gluttonous Grimoire, Hydra''s Lament,
    Heartseeker, Tyrfing, Lernaean Bow, Erosion, Spear of Desolation, Tekko-Kagi,
    Spear of the Magus, Eye of Providence, Avenging Blade, Shield of the Phoenix,
    Stone of Binding, Draconic Scale, Breastplate of Valor, Helm of Radiance, Soul
    Gem, Titan''s Bane, Silverbranch Bow, The Crusher, Obsidian Shard, Pharaoh''s
    Curse, Magi''s Cloak, Toxic Blade, The Reaper, Nimble Ring, Shogun''s Ofuda, Screeching
    Gargoyle, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.54
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.61
      pick: 0.22
      fit: 0.38
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Shifter''s Shield, Shield
    Splitter, Spear of Desolation, Spear of the Magus, Runeforged Hammer, Helm of
    Radiance, Soul Gem, Obsidian Shard, Berserker''s Shield, Eye of the Storm, Hydra''s
    Lament, Rod of Asclepius, Heartseeker, Erosion, Eye of Providence, Shield of the
    Phoenix, Stone of Binding, Draconic Scale, Breastplate of Valor, Doom Orb, Jade
    Scepter, Death Metal, Wish-Granting Pearl, Avenging Blade, Magi''s Cloak, Chronos''
    Pendant, The World Stone, Helm of Darkness, Titan''s Bane, The Crusher, Ancient
    Signet, Screeching Gargoyle, Mantle Of Discord, Dreamer''s Idol, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.6
      pick: 0.19
      fit: 0.23
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.61
      pick: 0.22
      fit: 0.38
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.62
      pick: 0.12
      fit: 0.42
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s
    Shield, Jotunn''s Revenge, Breastplate of Valor, Erosion, Eye of Providence, Draconic
    Scale, Berserker''s Shield, Shield Splitter, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Eye of the Storm, Helm of Radiance, Gluttonous Grimoire, Mantle
    Of Discord, Midgardian Mail, Runeforged Hammer, Screeching Gargoyle, Hide of the
    Nemean Lion, Prophetic Cloak, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s
    Garb, Helm of Darkness, Xibalban Effigy, Void Stone, Spear of Desolation, Spectral
    Armor, Hussar''s Wings, Rod of Asclepius, Gladiator''s Shield, Daybreak Gavel,
    Soul Gem, Doublet of Binding, Hydra''s Lament.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.19
      fit: 0.37
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.61
      pick: 0.22
      fit: 0.62
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.62
      pick: 0.12
      fit: 0.68
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Spirit Robe
  - Freya's Tears
  - Shifter's Shield
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Spirit Robe
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic
    Cuirass, Shifter''s Shield, Jotunn''s Revenge, Breastplate of Valor, Erosion,
    Eye of Providence, Draconic Scale, Berserker''s Shield, Shield Splitter, Shield
    of the Phoenix, Stone of Binding, Magi''s Cloak, Eye of the Storm, Helm of Radiance,
    Gluttonous Grimoire, Mantle Of Discord, Midgardian Mail, Runeforged Hammer, Screeching
    Gargoyle, Hide of the Nemean Lion, Prophetic Cloak, Leviathan''s Hide, Void Shield,
    Ancile, Oni Hunter''s Garb, Helm of Darkness, Xibalban Effigy, Void Stone, Spear
    of Desolation, Spectral Armor, Hussar''s Wings, Rod of Asclepius, Gladiator''s
    Shield, Daybreak Gavel, Soul Gem, Doublet of Binding, Hydra''s Lament.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.25
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.78
    Spirit Robe:
      total: 0.58
      efficiency: 0.34
      win: 0.85
      pick: 0.11
      fit: 0.49
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.61
      pick: 0.22
      fit: 0.62
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.62
      pick: 0.12
      fit: 0.68
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.13
  community_ordered:
  - Spirit Robe
  - Freya's Tears
  - Shifter's Shield
  swaps:
  - added: Spirit Robe
    removed: Genji's Guard
    reason: community 85% win over 41 matches (vs 57% on this god), taking the model's
      weakest slot from Genji's Guard
  starter: *id001
---
