---
type: smite-build
god: Athena
mode: Conquest
builds:
- source: community
  aspect: Aspect of War
  aspect_pick_rate: 0.21
  aspect_win_rate: 0.56
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.23
    win_rate: 0.61
    alternates:
    - name: Stampede
      pick_rate: 0.17
      win_rate: 0.55
    - name: Gauntlet of Thebes
      pick_rate: 0.1
      win_rate: 0.57
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.6
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.14
      win_rate: 0.6
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.45
  - name: Breastplate of Valor
    pick_rate: 0.14
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.53
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.57
  - name: Shell of Rebuke
    pick_rate: 0.05
    win_rate: 0.63
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.54
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.68
  - name: Hide of the Nemean Lion
    pick_rate: 0.07
    win_rate: 0.55
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.74
    - name: Spirit Robe
      pick_rate: 0.05
      win_rate: 0.65
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.62
    alternates:
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.58
    - name: Olmec Blue
      pick_rate: 0.04
      win_rate: 0.65
  community_starters:
  - name: Selflessness
    pick_rate: 0.16
    win_rate: 0.53
  - name: Bumba's Cudgel
    pick_rate: 0.15
    win_rate: 0.57
  - name: Bumba's Hammer
    pick_rate: 0.15
    win_rate: 0.66
  source_url: https://smitebrain.com/gods/athena/
  last_verified: '2026-08-10'
  god_win_rate: 0.5703794369645043
  god_matches_won: 466
  god_matches_played: 817
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-10'
  god_matches_analyzed: 17490
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
  - Dwarven Plate
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Dwarven Plate
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Berserker''s Shield, Freya''s Tears,
    Gluttonous Grimoire, Oni Hunter''s Garb, Erosion, Shield of the Phoenix, Eye of
    Providence, Draconic Scale, Spectral Armor, Jotunn''s Revenge, Pharaoh''s Curse,
    Shield Splitter, Soul Gem, Leviathan''s Hide, Mantle Of Discord, Stone of Binding,
    Midgardian Mail, The Crusher, Eye of the Storm, Helm of Radiance, Shogun''s Ofuda,
    Magi''s Cloak, Runeforged Hammer, Hydra''s Lament, Ancile, Gladiator''s Shield,
    Xibalban Effigy, Void Shield, Screeching Gargoyle, Prophetic Cloak, Doublet of
    Binding, Rod of Asclepius, Yogi''s Necklace, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.37
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.22
      fit: 0.37
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.78
    Shifter's Shield:
      total: 0.57
      efficiency: 0.52
      win: 0.61
      pick: 0.23
      fit: 0.68
    Dwarven Plate:
      total: 0.54
      efficiency: 0.35
      win: 0.74
      pick: 0.11
      fit: 0.49
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.68
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
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
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
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Berserker''s
    Shield, Soul Gem, Gluttonous Grimoire, Rod of Asclepius, Oni Hunter''s Garb, Freya''s
    Tears, Chandra''s Grace, Erosion, Eye of Providence, Phoenix Feather, Draconic
    Scale, Spectral Armor, Jotunn''s Revenge, Pharaoh''s Curse, Leviathan''s Hide,
    Blood-Bound Book, Bancroft''s Talon, Midgardian Mail, Lifebinder, Runeforged Hammer,
    Eye of the Storm, The Crusher, Glorious Pridwen, Shogun''s Ofuda, Shield Splitter,
    Riptalon, Hydra''s Lament, Gladiator''s Shield, Ancile, Void Shield, The Reaper,
    Yogi''s Necklace, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.34
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.66
      win: 0.6
      pick: 0.22
      fit: 0.34
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.9
    Shifter's Shield:
      total: 0.57
      efficiency: 0.52
      win: 0.61
      pick: 0.23
      fit: 0.66
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Shifter's Shield
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Dwarven Plate — physical protection
    swap_item: Dwarven Plate
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Jotunn''s Revenge, Kinetic Cuirass, The Crusher,
    Soul Gem, Amanita Charm, Berserker''s Shield, Stone of Binding, Screeching Gargoyle,
    Freya''s Tears, Spear of the Magus, Void Shield, Oni Hunter''s Garb, The Cosmic
    Horror, Void Stone, Shield of the Phoenix, Avenging Blade, Spear of Desolation,
    Erosion, Eye of Providence, Spectral Armor, Obsidian Shard, Riptalon, Pharaoh''s
    Curse, Draconic Scale, Silverbranch Bow, The Reaper, Shield Splitter, Hydra''s
    Lament, Leviathan''s Hide, Helm of Radiance, Runeforged Hammer, Mantle Of Discord,
    Midgardian Mail, Heartseeker, Shogun''s Ofuda, Doom Orb.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.26
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.6
      pick: 0.22
      fit: 0.26
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.58
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.63
    Shifter's Shield:
      total: 0.54
      efficiency: 0.52
      win: 0.61
      pick: 0.23
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Shifter's Shield
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Dwarven Plate — physical protection
    swap_item: Dwarven Plate
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Golden Blade, Pharaoh''s Curse, Jotunn''s Revenge, Riptalon, The Crusher, Freya''s
    Tears, Oni Hunter''s Garb, Soul Gem, Lernaean Bow, Shogun''s Ofuda, Hydra''s Lament,
    Shield of the Phoenix, Silverbranch Bow, Tyrfing, Runeforged Hammer, Spectral
    Armor, Erosion, Shield Splitter, Eye of Providence, Bracer of The Abyss, Draconic
    Scale, Eye of the Storm, Helm of Radiance, Leviathan''s Hide, Death Metal, Midgardian
    Mail, Mantle Of Discord, Yogi''s Necklace, Stone of Binding, Dominance, Eros''
    Bow, Spear of the Magus, Damaru.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.2
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.66
      win: 0.6
      pick: 0.22
      fit: 0.2
    Shifter's Shield:
      total: 0.52
      efficiency: 0.52
      win: 0.61
      pick: 0.23
      fit: 0.37
    Pharaoh's Curse:
      total: 0.49
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Jotunn''s Revenge,
    Kinetic Cuirass, Shield of the Phoenix, Soul Gem, Amanita Charm, Gluttonous Grimoire,
    Berserker''s Shield, Hydra''s Lament, Oni Hunter''s Garb, Screeching Gargoyle,
    Chronos'' Pendant, The Crusher, Spear of Desolation, Chandra''s Grace, Gladiator''s
    Shield, Erosion, Spectral Armor, Eye of Providence, Prophetic Cloak, Shield Splitter,
    Pharaoh''s Curse, Runeforged Hammer, Draconic Scale, Helm of Radiance, Gem of
    Focus, Leviathan''s Hide, Eye of the Storm, Death Metal, Midgardian Mail, Mantle
    Of Discord, Rod of Asclepius, Stone of Binding, Spear of the Magus, Arondight,
    Jade Scepter, Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.48
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.66
      win: 0.6
      pick: 0.22
      fit: 0.48
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.53
      efficiency: 0.52
      win: 0.61
      pick: 0.23
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Shifter's Shield
  flex_slots:
  - Berserker's Shield
  - Gluttonous Grimoire
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Berserker''s Shield, Gluttonous
    Grimoire, The Crusher, Kinetic Cuirass, Amanita Charm, Hydra''s Lament, Freya''s
    Tears, Soul Gem, Runeforged Hammer, Shield Splitter, Oni Hunter''s Garb, Pharaoh''s
    Curse, Golden Blade, Lernaean Bow, Eye of the Storm, Shield of the Phoenix, Death
    Metal, Erosion, Spectral Armor, Eye of Providence, Spear of the Magus, Damaru,
    The Reaper, Shogun''s Ofuda, Draconic Scale, Avenging Blade, The Cosmic Horror,
    Leviathan''s Hide, Helm of Radiance, Riptalon, Midgardian Mail, Mantle Of Discord,
    Stone of Binding, Heartseeker, Tekko-Kagi, Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.23
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.36
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.6
      pick: 0.22
      fit: 0.23
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.41
    Shifter's Shield:
      total: 0.53
      efficiency: 0.52
      win: 0.61
      pick: 0.23
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Shifter's Shield
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Dwarven Plate — physical protection
    swap_item: Dwarven Plate
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge,
    Kinetic Cuirass, The Crusher, Amanita Charm, Soul Gem, Berserker''s Shield, Freya''s
    Tears, Spear of the Magus, Oni Hunter''s Garb, Death Metal, Hydra''s Lament, Runeforged
    Hammer, The Cosmic Horror, Shield Splitter, Helm of Radiance, Shield of the Phoenix,
    Spear of Desolation, Erosion, Eye of the Storm, Spectral Armor, Rod of Asclepius,
    Eye of Providence, Pharaoh''s Curse, Jade Scepter, Obsidian Shard, Draconic Scale,
    Chronos'' Pendant, Golden Blade, Damaru, Leviathan''s Hide, Lernaean Bow, The
    Reaper, Blood-Bound Book, Bancroft''s Talon, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.23
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.6
      pick: 0.22
      fit: 0.23
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.52
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.53
      efficiency: 0.52
      win: 0.61
      pick: 0.23
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Freya''s Tears, Gluttonous Grimoire, Oni Hunter''s Garb, Erosion, Shield of the
    Phoenix, Eye of Providence, Draconic Scale, Spectral Armor, Jotunn''s Revenge,
    Pharaoh''s Curse, Shield Splitter, Soul Gem, Leviathan''s Hide, Mantle Of Discord,
    Stone of Binding, Midgardian Mail, The Crusher, Eye of the Storm, Helm of Radiance,
    Shogun''s Ofuda, Magi''s Cloak, Runeforged Hammer, Hydra''s Lament, Ancile, Gladiator''s
    Shield, Xibalban Effigy, Void Shield, Screeching Gargoyle, Prophetic Cloak, Doublet
    of Binding, Rod of Asclepius, Yogi''s Necklace, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.6
      pick: 0.22
      fit: 0.37
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.44
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.22
      fit: 0.37
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.62
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.68
  starter: *id001
---
