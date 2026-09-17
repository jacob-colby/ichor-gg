---
type: smite-build
god: Athena
mode: Conquest
builds:
- source: community
  aspect: Aspect of War
  aspect_pick_rate: 0.22
  aspect_win_rate: 0.54
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.23
    win_rate: 0.61
    alternates:
    - name: Stampede
      pick_rate: 0.19
      win_rate: 0.62
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.56
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.57
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.12
      win_rate: 0.58
    - name: Stampede
      pick_rate: 0.11
      win_rate: 0.64
  - name: Freya's Tears
    pick_rate: 0.18
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.54
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.58
  - name: Shell of Rebuke
    pick_rate: 0.12
    win_rate: 0.69
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.69
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.6
  - name: Spirit Robe
    pick_rate: 0.05
    win_rate: 0.8
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.56
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.8
  - name: Hide of the Nemean Lion
    pick_rate: 0.06
    win_rate: 0.71
    alternates:
    - name: Olmec Blue
      pick_rate: 0.05
      win_rate: 0.83
    - name: Engraved Guard
      pick_rate: 0.04
      win_rate: 0.62
  community_starters:
  - name: Selflessness
    pick_rate: 0.28
    win_rate: 0.54
  - name: Bumba's Hammer
    pick_rate: 0.21
    win_rate: 0.65
  - name: Bumba's Cudgel
    pick_rate: 0.18
    win_rate: 0.58
  source_url: https://smitebrain.com/gods/athena/
  last_verified: '2026-09-17'
  god_win_rate: 0.583941605839416
  god_matches_won: 400
  god_matches_played: 685
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-17'
  god_matches_analyzed: 10391
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Freya's Tears
  - Amanita Charm
  - Erosion
  flex_slots:
  - Jotunn's Revenge
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Jotunn''s Revenge, Erosion,
    Eye of Providence, Draconic Scale, Berserker''s Shield, Breastplate of Valor,
    Shifter''s Shield, Shield Splitter, Shield of the Phoenix, Stone of Binding, Magi''s
    Cloak, Eye of the Storm, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord,
    Midgardian Mail, Runeforged Hammer, Screeching Gargoyle, Leviathan''s Hide, Void
    Shield, Ancile, Oni Hunter''s Garb, Helm of Darkness, Xibalban Effigy, Void Stone,
    Spear of Desolation, Spectral Armor, Hussar''s Wings, Rod of Asclepius, Gladiator''s
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
    Hide of the Nemean Lion:
      total: 0.58
      efficiency: 0.52
      win: 0.71
      pick: 0.18
      fit: 0.44
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.55
      pick: 0.28
      fit: 0.62
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
  - Hide of the Nemean Lion
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Rod of Asclepius, Jotunn''s Revenge, Soul Gem, Berserker''s Shield, Erosion, Eye
    of Providence, Draconic Scale, Shifter''s Shield, Ethereal Staff, Breastplate
    of Valor, Phoenix Feather, Gluttonous Grimoire, Yogi''s Necklace, Shield Splitter,
    Chandra''s Grace, Runeforged Hammer, Glorious Pridwen, Eye of the Storm, Lifebinder,
    Midgardian Mail, Stone of Binding, Helm of Radiance, Leviathan''s Hide, Void Shield,
    Magi''s Cloak, Ancile, Oni Hunter''s Garb, Daybreak Gavel, Sphere of Negation,
    Screeching Gargoyle, Void Stone, Mantle Of Discord, Spectral Armor, Gladiator''s
    Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
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
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.55
      pick: 0.28
      fit: 0.54
    Hide of the Nemean Lion:
      total: 0.58
      efficiency: 0.52
      win: 0.71
      pick: 0.18
      fit: 0.46
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Freya's Tears
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Hide of the Nemean Lion
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation,
    Void Shield, Spear of the Magus, Soul Gem, Void Stone, Obsidian Shard, Avenging
    Blade, Breastplate of Valor, Berserker''s Shield, Heartseeker, Erosion, Shield
    Splitter, Eye of Providence, Draconic Scale, Shield of the Phoenix, Shifter''s
    Shield, Doom Orb, Helm of Radiance, Runeforged Hammer, The World Stone, Titan''s
    Bane, Magi''s Cloak, The Crusher, Dreamer''s Idol, Eye of the Storm, Mantle Of
    Discord, Midgardian Mail, The Reaper, Daybreak Gavel, Rod of Asclepius, Leviathan''s
    Hide, Hydra''s Lament.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.55
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.66
    Stone of Binding:
      total: 0.57
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
    Hide of the Nemean Lion:
      total: 0.56
      efficiency: 0.52
      win: 0.71
      pick: 0.18
      fit: 0.31
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Hide of the Nemean Lion
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Nimble Ring, Kinetic Cuirass, Golden Blade, Gluttonous Grimoire, Breastplate of
    Valor, Tyrfing, Shield Splitter, Soul Gem, Runeforged Hammer, Pharaoh''s Curse,
    Riptalon, Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Helm of Radiance,
    Eye of Providence, Stone of Binding, Eye of the Storm, Shield of the Phoenix,
    Hydra''s Lament, Toxic Blade, Draconic Scale, Shifter''s Shield, Magi''s Cloak,
    Screeching Gargoyle, Daybreak Gavel, The Reaper, Spear of Desolation, Spear of
    the Magus, Bragi''s Harp, Midgardian Mail, Mantle Of Discord, Tekko-Kagi, Rod
    of Asclepius, Avenging Blade.'
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
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.52
      win: 0.71
      pick: 0.18
      fit: 0.24
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Hide of the Nemean Lion
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
  - Breastplate of Valor
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
    Amanita Charm, Breastplate of Valor, Kinetic Cuirass, Shield of the Phoenix, Spear
    of Desolation, Hydra''s Lament, Screeching Gargoyle, Soul Gem, Chronos'' Pendant,
    Shield Splitter, Berserker''s Shield, Erosion, Helm of Radiance, Runeforged Hammer,
    Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield, Draconic Scale, Stone
    of Binding, Shifter''s Shield, Eye of the Storm, Arondight, Gem of Focus, Magi''s
    Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus, Mantle Of Discord,
    Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Chandra''s Grace, Obsidian
    Shard, Leviathan''s Hide, Jade Scepter, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.57
      pick: 0.22
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.58
      pick: 0.14
      fit: 0.48
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.55
      pick: 0.28
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
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Hide of the Nemean Lion
  - Shield Splitter
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
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer, Golden
    Blade, Eye of the Storm, Breastplate of Valor, Gluttonous Grimoire, Hydra''s Lament,
    Heartseeker, Tyrfing, Lernaean Bow, Erosion, Spear of Desolation, Tekko-Kagi,
    Spear of the Magus, Eye of Providence, Avenging Blade, Shield of the Phoenix,
    Stone of Binding, Draconic Scale, Helm of Radiance, Soul Gem, Titan''s Bane, Silverbranch
    Bow, Shifter''s Shield, The Crusher, Obsidian Shard, Pharaoh''s Curse, Magi''s
    Cloak, Toxic Blade, The Reaper, Nimble Ring, Shogun''s Ofuda, Screeching Gargoyle,
    Mantle Of Discord, Midgardian Mail.'
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
      total: 0.55
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.52
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.52
      win: 0.71
      pick: 0.18
      fit: 0.27
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Hide of the Nemean Lion
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Shield Splitter, Spear of
    Desolation, Spear of the Magus, Runeforged Hammer, Helm of Radiance, Soul Gem,
    Obsidian Shard, Breastplate of Valor, Berserker''s Shield, Eye of the Storm, Hydra''s
    Lament, Rod of Asclepius, Heartseeker, Erosion, Eye of Providence, Shield of the
    Phoenix, Stone of Binding, Draconic Scale, Shifter''s Shield, Doom Orb, Jade Scepter,
    Death Metal, Wish-Granting Pearl, Avenging Blade, Magi''s Cloak, Chronos'' Pendant,
    The World Stone, Helm of Darkness, Titan''s Bane, The Crusher, Ancient Signet,
    Screeching Gargoyle, Mantle Of Discord, Dreamer''s Idol, Midgardian Mail.'
  slot_scores:
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
    Shield Splitter:
      total: 0.54
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.48
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.52
      win: 0.71
      pick: 0.18
      fit: 0.27
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.41
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Hide of the Nemean Lion
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
    Of Discord, Midgardian Mail, Runeforged Hammer, Screeching Gargoyle, Leviathan''s
    Hide, Void Shield, Ancile, Oni Hunter''s Garb, Helm of Darkness, Xibalban Effigy,
    Void Stone, Spear of Desolation, Spectral Armor, Hussar''s Wings, Rod of Asclepius,
    Gladiator''s Shield, Daybreak Gavel, Soul Gem, Doublet of Binding, Hydra''s Lament.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.57
      pick: 0.22
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
      total: 0.57
      efficiency: 0.61
      win: 0.55
      pick: 0.28
      fit: 0.62
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.56
      pick: 0.09
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
  - Kinetic Cuirass
  - Shell of Rebuke
  - Spirit Robe
  - Freya's Tears
  - Shifter's Shield
  - Rod of Tahuti
  flex_slots:
  - Spirit Robe
  - Shell of Rebuke
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
    Gargoyle, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s Garb, Helm of
    Darkness, Xibalban Effigy, Void Stone, Spear of Desolation, Spectral Armor, Hussar''s
    Wings, Rod of Asclepius, Gladiator''s Shield, Daybreak Gavel, Soul Gem, Doublet
    of Binding, Hydra''s Lament.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.78
    Shell of Rebuke:
      total: 0.49
      efficiency: 0.28
      win: 0.69
      pick: 0.2
      fit: 0.49
    Spirit Robe:
      total: 0.56
      efficiency: 0.34
      win: 0.8
      pick: 0.11
      fit: 0.49
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.55
      pick: 0.28
      fit: 0.62
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.56
      pick: 0.09
      fit: 0.68
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.13
  community_ordered:
  - Shell of Rebuke
  - Spirit Robe
  - Freya's Tears
  - Shifter's Shield
  swaps:
  - added: Spirit Robe
    removed: Genji's Guard
    reason: community 80% win over 34 matches (vs 58% on this god), taking the model's
      weakest slot from Genji's Guard
  - added: Shell of Rebuke
    removed: Jotunn's Revenge
    reason: community 69% win over 82 matches (vs 58% on this god), taking the model's
      weakest slot from Jotunn's Revenge
  starter: *id001
---
