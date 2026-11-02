---
type: smite-build
god: Athena
mode: Conquest
builds:
- source: community
  aspect: Aspect of War
  aspect_pick_rate: 0.22
  aspect_win_rate: 0.58
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.32
    win_rate: 0.57
    alternates:
    - name: Stampede
      pick_rate: 0.17
      win_rate: 0.56
    - name: Hydra's Lament
      pick_rate: 0.05
      win_rate: 0.68
  - name: Stampede
    pick_rate: 0.14
    win_rate: 0.59
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.6
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.46
  - name: Freya's Tears
    pick_rate: 0.17
    win_rate: 0.52
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.11
      win_rate: 0.57
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.64
  - name: Shell of Rebuke
    pick_rate: 0.12
    win_rate: 0.59
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.59
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.51
  - name: Deathbringer
    pick_rate: 0.05
    win_rate: 0.63
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.68
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.55
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.67
    - name: Sage's Ring
      pick_rate: 0.05
      win_rate: 0.67
  community_starters:
  - name: Bumba's Cudgel
    pick_rate: 0.29
    win_rate: 0.52
  - name: Bumba's Hammer
    pick_rate: 0.25
    win_rate: 0.67
  - name: Selflessness
    pick_rate: 0.19
    win_rate: 0.52
  source_url: https://smitebrain.com/gods/athena/
  last_verified: '2026-10-30'
  god_win_rate: 0.5588235294117647
  god_matches_won: 418
  god_matches_played: 748
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
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Genji''s Guard, Shifter''s
    Shield, Erosion, Breastplate of Valor, Eye of Providence, Jotunn''s Revenge, Draconic
    Scale, Berserker''s Shield, Shield Splitter, Shield of the Phoenix, Hydra''s Lament,
    Stone of Binding, Magi''s Cloak, Gluttonous Grimoire, Helm of Radiance, Eye of
    the Storm, Mantle Of Discord, Midgardian Mail, Oni Hunter''s Garb, Runeforged
    Hammer, Screeching Gargoyle, Leviathan''s Hide, Hide of the Nemean Lion, Prophetic
    Cloak, Void Shield, Ancile, Helm of Darkness, Spectral Armor, Spear of Desolation,
    Hussar''s Wings, Void Stone, Xibalban Effigy, Rod of Asclepius, Gladiator''s Shield,
    Daybreak Gavel, Soul Gem, Doublet of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.64
      pick: 0.12
      fit: 0.37
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.61
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.78
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.68
    Amanita Charm:
      total: 0.6
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
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
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
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Genji''s Guard, Rod of Asclepius, Shifter''s Shield, Jotunn''s Revenge, Soul Gem,
    Erosion, Berserker''s Shield, Eye of Providence, Breastplate of Valor, Draconic
    Scale, Ethereal Staff, Phoenix Feather, Gluttonous Grimoire, Yogi''s Necklace,
    Chandra''s Grace, Shield Splitter, Runeforged Hammer, Eye of the Storm, Glorious
    Pridwen, Midgardian Mail, Lifebinder, Oni Hunter''s Garb, Stone of Binding, Helm
    of Radiance, Leviathan''s Hide, Hide of the Nemean Lion, Void Shield, Ancile,
    Magi''s Cloak, Daybreak Gavel, Spectral Armor, Sphere of Negation, Gladiator''s
    Shield, Void Stone, Spear of Desolation, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.64
      pick: 0.12
      fit: 0.34
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.9
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
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Genji''s Guard,
    Stone of Binding, Gluttonous Grimoire, Kinetic Cuirass, Screeching Gargoyle, Spear
    of Desolation, Spear of the Magus, Void Shield, Soul Gem, Obsidian Shard, Breastplate
    of Valor, Void Stone, Shifter''s Shield, Avenging Blade, Berserker''s Shield,
    Erosion, Eye of Providence, Shield Splitter, Heartseeker, Draconic Scale, Shield
    of the Phoenix, Doom Orb, Helm of Radiance, The World Stone, Runeforged Hammer,
    Dreamer''s Idol, Titan''s Bane, Magi''s Cloak, The Crusher, Eye of the Storm,
    Midgardian Mail, Mantle Of Discord, Oni Hunter''s Garb, The Reaper, Daybreak Gavel,
    Rod of Asclepius, Leviathan''s Hide, Hide of the Nemean Lion.'
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
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.64
      pick: 0.12
      fit: 0.26
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
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
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Genji''s Guard, Jotunn''s
    Revenge, Nimble Ring, Kinetic Cuirass, Hydra''s Lament, Golden Blade, Gluttonous
    Grimoire, Breastplate of Valor, Tyrfing, Shifter''s Shield, Shield Splitter, Soul
    Gem, Pharaoh''s Curse, Runeforged Hammer, Riptalon, Lernaean Bow, Shogun''s Ofuda,
    Silverbranch Bow, Erosion, Helm of Radiance, Eye of Providence, Shield of the
    Phoenix, Toxic Blade, Eye of the Storm, Stone of Binding, Draconic Scale, Magi''s
    Cloak, Daybreak Gavel, Spear of the Magus, Spear of Desolation, Midgardian Mail,
    Screeching Gargoyle, Bragi''s Harp, The Reaper, Tekko-Kagi, Oni Hunter''s Garb,
    Rod of Asclepius, Mantle Of Discord.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.64
      pick: 0.12
      fit: 0.2
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.2
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
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Hydra's Lament
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Rod of Tahuti, Jotunn''s
    Revenge, Hydra''s Lament, Breastplate of Valor, Amanita Charm, Kinetic Cuirass,
    Shield of the Phoenix, Spear of Desolation, Soul Gem, Lotus Sickle, Screeching
    Gargoyle, Shifter''s Shield, Chronos'' Pendant, Shield Splitter, Berserker''s
    Shield, Prophetic Cloak, Helm of Radiance, Erosion, Gluttonous Grimoire, Runeforged
    Hammer, Eye of Providence, Gladiator''s Shield, Draconic Scale, Stone of Binding,
    Eye of the Storm, Gem of Focus, Arondight, Magi''s Cloak, Spear of the Magus,
    Rod of Asclepius, Eye of Erebus, Midgardian Mail, Mantle Of Discord, Oni Hunter''s
    Garb, Glorious Pridwen, Daybreak Gavel, Obsidian Shard, Chandra''s Grace, Jade
    Scepter, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.64
      pick: 0.12
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
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.52
      pick: 0.26
      fit: 0.64
    Hydra's Lament:
      total: 0.58
      efficiency: 0.54
      win: 0.68
      pick: 0.05
      fit: 0.52
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Hydra's Lament
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
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
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita
    Charm, Berserker''s Shield, Hydra''s Lament, Genji''s Guard, Kinetic Cuirass,
    Shield Splitter, Runeforged Hammer, Golden Blade, Breastplate of Valor, Gluttonous
    Grimoire, Eye of the Storm, Shifter''s Shield, Tyrfing, Heartseeker, Erosion,
    Spear of Desolation, Lernaean Bow, Spear of the Magus, Eye of Providence, Tekko-Kagi,
    Avenging Blade, Draconic Scale, Shield of the Phoenix, Helm of Radiance, Soul
    Gem, Stone of Binding, Titan''s Bane, Obsidian Shard, Silverbranch Bow, The Crusher,
    Pharaoh''s Curse, Toxic Blade, Magi''s Cloak, The Reaper, Nimble Ring, Shogun''s
    Ofuda, Midgardian Mail, Daybreak Gavel, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.64
      pick: 0.12
      fit: 0.23
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.52
    Hydra's Lament:
      total: 0.56
      efficiency: 0.54
      win: 0.68
      pick: 0.05
      fit: 0.4
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
  - Hydra's Lament
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
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
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Genji''s Guard, Hydra''s Lament, Kinetic Cuirass, Gluttonous Grimoire,
    Spear of Desolation, Shield Splitter, Spear of the Magus, Breastplate of Valor,
    Helm of Radiance, Soul Gem, Runeforged Hammer, Obsidian Shard, Shifter''s Shield,
    Berserker''s Shield, Eye of the Storm, Rod of Asclepius, Erosion, Eye of Providence,
    Lotus Sickle, Heartseeker, Draconic Scale, Shield of the Phoenix, Jade Scepter,
    Stone of Binding, Doom Orb, Death Metal, Avenging Blade, Wish-Granting Pearl,
    The World Stone, Magi''s Cloak, Chronos'' Pendant, Helm of Darkness, Titan''s
    Bane, The Crusher, Dreamer''s Idol, Triton''s Conch, Midgardian Mail, Daybreak
    Gavel.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.5
      win: 0.61
      pick: 0.0
      fit: 0.18
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.64
      pick: 0.12
      fit: 0.23
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.41
    Transcendence:
      total: 0.48
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
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s
    Shield, Genji''s Guard, Erosion, Breastplate of Valor, Eye of Providence, Jotunn''s
    Revenge, Draconic Scale, Berserker''s Shield, Shield Splitter, Shield of the Phoenix,
    Stone of Binding, Magi''s Cloak, Gluttonous Grimoire, Helm of Radiance, Eye of
    the Storm, Mantle Of Discord, Midgardian Mail, Oni Hunter''s Garb, Runeforged
    Hammer, Screeching Gargoyle, Leviathan''s Hide, Hide of the Nemean Lion, Prophetic
    Cloak, Void Shield, Ancile, Helm of Darkness, Spectral Armor, Spear of Desolation,
    Hussar''s Wings, Void Stone, Xibalban Effigy, Rod of Asclepius, Gladiator''s Shield,
    Daybreak Gavel, Soul Gem, Doublet of Binding, Hydra''s Lament.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.64
      pick: 0.12
      fit: 0.37
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.52
      pick: 0.26
      fit: 0.62
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.68
    Amanita Charm:
      total: 0.6
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
  - Freya's Tears
  starter: *id001
---
