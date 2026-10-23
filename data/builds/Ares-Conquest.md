---
type: smite-build
god: Ares
mode: Conquest
builds:
- source: community
  aspect: Aspect of Reverberation
  aspect_pick_rate: 0.29
  aspect_win_rate: 0.46
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.27
    win_rate: 0.59
    alternates:
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.5
    - name: Yogi's Necklace
      pick_rate: 0.1
      win_rate: 0.58
  - name: Stampede
    pick_rate: 0.24
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.58
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.55
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.63
    alternates:
    - name: Freya's Tears
      pick_rate: 0.16
      win_rate: 0.53
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.64
  - name: Freya's Tears
    pick_rate: 0.14
    win_rate: 0.44
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.63
    - name: Shell of Rebuke
      pick_rate: 0.12
      win_rate: 0.69
  - name: Draconic Scale
    pick_rate: 0.06
    win_rate: 0.67
    alternates:
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.67
    - name: Breastplate of Valor
      pick_rate: 0.05
      win_rate: 0.8
  - name: Sage's Ring
    pick_rate: 0.08
    win_rate: 1.0
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.75
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.5
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.15
    win_rate: 0.5
  - name: Selflessness
    pick_rate: 0.15
    win_rate: 0.5
  - name: War Flag
    pick_rate: 0.11
    win_rate: 0.62
  source_url: https://smitebrain.com/gods/ares/
  last_verified: '2026-10-23'
  god_win_rate: 0.5210084033613446
  god_matches_won: 62
  god_matches_played: 119
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-23'
  god_matches_analyzed: 2743
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shifter's Shield
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Amanita Charm, Rod of Tahuti, Kinetic Cuirass,
    Draconic Scale, Shifter''s Shield, Jotunn''s Revenge, Erosion, Eye of Providence,
    Berserker''s Shield, Shield Splitter, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Eye of the Storm, Helm of Radiance, Gluttonous Grimoire, Mantle
    Of Discord, Runeforged Hammer, Screeching Gargoyle, Midgardian Mail, Prophetic
    Cloak, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s
    Garb, Spear of Desolation, Helm of Darkness, Xibalban Effigy, Gladiator''s Shield,
    Void Stone, Spectral Armor, Hussar''s Wings, Rod of Asclepius, Hydra''s Lament,
    Daybreak Gavel, Soul Gem, Doublet of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.63
      pick: 0.25
      fit: 0.38
    Breastplate of Valor:
      total: 0.65
      efficiency: 0.65
      win: 0.8
      pick: 0.11
      fit: 0.38
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.77
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.67
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.67
      pick: 0.13
      fit: 0.67
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Draconic Scale
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Draconic Scale
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Rod of Tahuti,
    Kinetic Cuirass, Draconic Scale, Jotunn''s Revenge, Rod of Asclepius, Shifter''s
    Shield, Soul Gem, Berserker''s Shield, Erosion, Eye of Providence, Ethereal Staff,
    Phoenix Feather, Chandra''s Grace, Gluttonous Grimoire, Shield Splitter, Glorious
    Pridwen, Runeforged Hammer, Eye of the Storm, Yogi''s Necklace, Midgardian Mail,
    Stone of Binding, Lifebinder, Hide of the Nemean Lion, Helm of Radiance, Leviathan''s
    Hide, Void Shield, Magi''s Cloak, Ancile, Screeching Gargoyle, Oni Hunter''s Garb,
    Daybreak Gavel, Gladiator''s Shield, Sphere of Negation, Spear of Desolation,
    Void Stone, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.63
      pick: 0.25
      fit: 0.35
    Breastplate of Valor:
      total: 0.65
      efficiency: 0.65
      win: 0.8
      pick: 0.11
      fit: 0.35
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.75
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.9
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.67
      pick: 0.13
      fit: 0.65
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.95
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Breastplate of Valor, Rod of Tahuti, Jotunn''s Revenge, Amanita
    Charm, Stone of Binding, Gluttonous Grimoire, Kinetic Cuirass, Draconic Scale,
    Screeching Gargoyle, Spear of Desolation, Void Shield, Spear of the Magus, Soul
    Gem, Void Stone, Shifter''s Shield, Obsidian Shard, Avenging Blade, Berserker''s
    Shield, Heartseeker, Erosion, Shield Splitter, Eye of Providence, Shield of the
    Phoenix, Doom Orb, Helm of Radiance, Runeforged Hammer, The World Stone, Titan''s
    Bane, Magi''s Cloak, The Crusher, Dreamer''s Idol, Eye of the Storm, Mantle Of
    Discord, The Reaper, Midgardian Mail, Daybreak Gavel, Hydra''s Lament, Hide of
    the Nemean Lion, Rod of Asclepius, Leviathan''s Hide.'
  slot_scores:
    Stone of Binding:
      total: 0.56
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.74
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.63
      pick: 0.25
      fit: 0.27
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.65
      win: 0.8
      pick: 0.11
      fit: 0.27
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.47
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
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
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Rod of Tahuti, Berserker''s Shield, Amanita Charm,
    Jotunn''s Revenge, Nimble Ring, Kinetic Cuirass, Draconic Scale, Golden Blade,
    Gluttonous Grimoire, Tyrfing, Shifter''s Shield, Shield Splitter, Soul Gem, Runeforged
    Hammer, Pharaoh''s Curse, Riptalon, Lernaean Bow, Shogun''s Ofuda, Silverbranch
    Bow, Erosion, Helm of Radiance, Hydra''s Lament, Shield of the Phoenix, Stone
    of Binding, Eye of Providence, Eye of the Storm, Toxic Blade, Magi''s Cloak, Screeching
    Gargoyle, Daybreak Gavel, Spear of Desolation, The Reaper, Spear of the Magus,
    Midgardian Mail, Bragi''s Harp, Mantle Of Discord, Tekko-Kagi, Rod of Asclepius,
    Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.53
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.65
      win: 0.8
      pick: 0.11
      fit: 0.21
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.29
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Breastplate of Valor
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Draconic Scale
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
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Rod of Tahuti,
    Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Draconic
    Scale, Spear of Desolation, Hydra''s Lament, Screeching Gargoyle, Soul Gem, Shifter''s
    Shield, Chronos'' Pendant, Shield Splitter, Berserker''s Shield, Prophetic Cloak,
    Erosion, Helm of Radiance, Runeforged Hammer, Gluttonous Grimoire, Eye of Providence,
    Gladiator''s Shield, Stone of Binding, Eye of the Storm, Arondight, Gem of Focus,
    Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus, Mantle Of
    Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Chandra''s Grace,
    Obsidian Shard, Hide of the Nemean Lion, Leviathan''s Hide, Jade Scepter, Void
    Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.63
      pick: 0.25
      fit: 0.48
    Breastplate of Valor:
      total: 0.67
      efficiency: 0.65
      win: 0.8
      pick: 0.11
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
    Draconic Scale:
      total: 0.55
      efficiency: 0.5
      win: 0.67
      pick: 0.13
      fit: 0.45
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
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
    Of Discord, Runeforged Hammer, Screeching Gargoyle, Midgardian Mail, Prophetic
    Cloak, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s
    Garb, Spear of Desolation, Helm of Darkness, Xibalban Effigy, Gladiator''s Shield,
    Void Stone, Spectral Armor, Hussar''s Wings, Rod of Asclepius, Hydra''s Lament,
    Daybreak Gavel, Soul Gem, Doublet of Binding.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.27
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.63
      pick: 0.25
      fit: 0.38
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.77
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.44
      pick: 0.23
      fit: 0.62
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.67
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
