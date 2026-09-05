---
type: smite-build
god: Ares
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Stampede
    pick_rate: 0.26
    win_rate: 0.55
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.18
      win_rate: 0.6
    - name: Circe's Hexstone
      pick_rate: 0.1
      win_rate: 0.7
  - name: Genji's Guard
    pick_rate: 0.12
    win_rate: 0.43
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.11
      win_rate: 0.74
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.44
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.6
  - name: Freya's Tears
    pick_rate: 0.14
    win_rate: 0.65
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.13
      win_rate: 0.65
    - name: Breastplate of Valor
      pick_rate: 0.06
      win_rate: 0.6
  - name: Draconic Scale
    pick_rate: 0.05
    win_rate: 0.42
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.53
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.69
  - name: Veve Charm
    pick_rate: 0.07
    win_rate: 0.56
    alternates:
    - name: Captain's Ring
      pick_rate: 0.06
      win_rate: 0.63
    - name: Sage's Ring
      pick_rate: 0.06
      win_rate: 0.75
  community_starters:
  - name: Selflessness
    pick_rate: 0.26
    win_rate: 0.51
  - name: Heroism
    pick_rate: 0.17
    win_rate: 0.6
  - name: Warrior's Axe
    pick_rate: 0.15
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/ares/
  last_verified: '2026-09-05'
  god_win_rate: 0.5501730103806228
  god_matches_won: 159
  god_matches_played: 289
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-09-05'
  god_matches_analyzed: 13197
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Jotunn's Revenge
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
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s Shield, Breastplate
    of Valor, Jotunn''s Revenge, Erosion, Eye of Providence, Berserker''s Shield,
    Shield Splitter, Shield of the Phoenix, Stone of Binding, Magi''s Cloak, Eye of
    the Storm, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord, Runeforged
    Hammer, Screeching Gargoyle, Midgardian Mail, Prophetic Cloak, Hide of the Nemean
    Lion, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s Garb, Spear of Desolation,
    Helm of Darkness, Xibalban Effigy, Gladiator''s Shield, Void Stone, Spectral Armor,
    Hussar''s Wings, Rod of Asclepius, Hydra''s Lament, Daybreak Gavel, Soul Gem,
    Doublet of Binding, Draconic Scale.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.1
      fit: 0.38
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.27
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.77
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.65
      pick: 0.23
      fit: 0.62
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.6
      pick: 0.0
      fit: 0.67
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Breastplate of Valor
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
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shifter's Shield
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Jotunn''s Revenge, Rod of Asclepius, Shifter''s Shield, Breastplate of Valor,
    Soul Gem, Berserker''s Shield, Erosion, Eye of Providence, Ethereal Staff, Phoenix
    Feather, Chandra''s Grace, Yogi''s Necklace, Gluttonous Grimoire, Shield Splitter,
    Glorious Pridwen, Runeforged Hammer, Eye of the Storm, Midgardian Mail, Stone
    of Binding, Lifebinder, Hide of the Nemean Lion, Helm of Radiance, Leviathan''s
    Hide, Void Shield, Magi''s Cloak, Ancile, Screeching Gargoyle, Oni Hunter''s Garb,
    Daybreak Gavel, Gladiator''s Shield, Sphere of Negation, Spear of Desolation,
    Void Stone, Mantle Of Discord, Draconic Scale.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.28
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.75
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.65
      pick: 0.23
      fit: 0.55
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.6
      pick: 0.0
      fit: 0.65
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.95
  community_ordered:
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
  - Kinetic Cuirass
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Kinetic Cuirass, Screeching Gargoyle, Breastplate of Valor,
    Spear of Desolation, Void Shield, Spear of the Magus, Soul Gem, Void Stone, Shifter''s
    Shield, Obsidian Shard, Avenging Blade, Berserker''s Shield, Heartseeker, Erosion,
    Shield Splitter, Eye of Providence, Shield of the Phoenix, Doom Orb, Helm of Radiance,
    Runeforged Hammer, The World Stone, Titan''s Bane, Magi''s Cloak, The Crusher,
    Dreamer''s Idol, Eye of the Storm, Mantle Of Discord, The Reaper, Midgardian Mail,
    Daybreak Gavel, Hydra''s Lament, Hide of the Nemean Lion, Rod of Asclepius, Leviathan''s
    Hide, Draconic Scale.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.55
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.67
    Stone of Binding:
      total: 0.56
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.74
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.57
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.65
      pick: 0.23
      fit: 0.44
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.47
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
    Nimble Ring, Kinetic Cuirass, Breastplate of Valor, Golden Blade, Gluttonous Grimoire,
    Tyrfing, Shifter''s Shield, Shield Splitter, Soul Gem, Runeforged Hammer, Pharaoh''s
    Curse, Riptalon, Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Helm
    of Radiance, Hydra''s Lament, Shield of the Phoenix, Stone of Binding, Eye of
    Providence, Eye of the Storm, Toxic Blade, Magi''s Cloak, Screeching Gargoyle,
    Daybreak Gavel, Spear of Desolation, The Reaper, Spear of the Magus, Midgardian
    Mail, Bragi''s Harp, Mantle Of Discord, Tekko-Kagi, Rod of Asclepius, Avenging
    Blade, Draconic Scale.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.53
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.29
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.65
      pick: 0.23
      fit: 0.34
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.36
  community_ordered:
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
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
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
    Breastplate of Valor, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear
    of Desolation, Hydra''s Lament, Screeching Gargoyle, Soul Gem, Shifter''s Shield,
    Chronos'' Pendant, Shield Splitter, Berserker''s Shield, Prophetic Cloak, Erosion,
    Helm of Radiance, Runeforged Hammer, Gluttonous Grimoire, Eye of Providence, Gladiator''s
    Shield, Stone of Binding, Eye of the Storm, Arondight, Gem of Focus, Magi''s Cloak,
    Rod of Asclepius, Eye of Erebus, Spear of the Magus, Mantle Of Discord, Glorious
    Pridwen, Midgardian Mail, Daybreak Gavel, Chandra''s Grace, Obsidian Shard, Hide
    of the Nemean Lion, Leviathan''s Hide, Jade Scepter, Void Shield, Draconic Scale.'
  slot_scores:
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.6
      pick: 0.1
      fit: 0.48
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.65
      pick: 0.23
      fit: 0.64
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
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
    Of Discord, Runeforged Hammer, Screeching Gargoyle, Midgardian Mail, Prophetic
    Cloak, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s
    Garb, Spear of Desolation, Helm of Darkness, Xibalban Effigy, Gladiator''s Shield,
    Void Stone, Spectral Armor, Hussar''s Wings, Rod of Asclepius, Hydra''s Lament,
    Daybreak Gavel, Soul Gem, Doublet of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.43
      pick: 0.16
      fit: 0.38
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.27
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.77
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.65
      pick: 0.23
      fit: 0.62
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.6
      pick: 0.0
      fit: 0.67
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
