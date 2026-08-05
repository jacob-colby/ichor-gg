---
type: smite-build
god: Athena
mode: Conquest
builds:
- source: community
  aspect: Aspect of War
  aspect_pick_rate: 0.19
  aspect_win_rate: 0.58
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.29
    win_rate: 0.6
    alternates:
    - name: Stampede
      pick_rate: 0.15
      win_rate: 0.56
    - name: Gauntlet of Thebes
      pick_rate: 0.07
      win_rate: 0.47
  - name: Breastplate of Valor
    pick_rate: 0.18
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.66
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.39
  - name: Genji's Guard
    pick_rate: 0.21
    win_rate: 0.44
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.17
      win_rate: 0.68
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.6
  - name: Freya's Tears
    pick_rate: 0.07
    win_rate: 0.44
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.7
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.45
  - name: Hide of the Nemean Lion
    pick_rate: 0.07
    win_rate: 0.31
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.89
    - name: Freya's Tears
      pick_rate: 0.04
      win_rate: 0.63
  - name: Engraved Guard
    pick_rate: 0.1
    win_rate: 0.7
    alternates:
    - name: Spirit Robe
      pick_rate: 0.07
      win_rate: 0.71
    - name: Legionnaire Armor
      pick_rate: 0.06
      win_rate: 0.5
  source_url: https://smitebrain.com/gods/athena/
  last_verified: '2026-08-01'
  god_win_rate: 0.5341880341880342
  god_matches_won: 125
  god_matches_played: 234
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shifter's Shield
  - Dwarven Plate
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Breastplate of Valor
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Berserker''s Shield,
    Gluttonous Grimoire, Oni Hunter''s Garb, Erosion, Shield of the Phoenix, Stampede,
    Draconic Scale, Spectral Armor, Freya''s Tears, Shield Splitter, Pharaoh''s Curse,
    Jotunn''s Revenge, Runeforged Hammer, Leviathan''s Hide, Eye of the Storm, Soul
    Gem, The Crusher, Midgardian Mail, Stone of Binding, Mantle Of Discord, Hydra''s
    Lament, Yogi''s Necklace, Helm of Radiance, Magi''s Cloak, Shogun''s Ofuda, Rod
    of Asclepius, Ancile, Gladiator''s Shield, Void Shield, Prophetic Cloak, Screeching
    Gargoyle, Doublet of Binding, Xibalban Effigy, Hide of the Nemean Lion.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.68
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.18
      fit: 0.37
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.78
    Shifter's Shield:
      total: 0.58
      efficiency: 0.56
      win: 0.6
      pick: 0.29
      fit: 0.68
    Dwarven Plate:
      total: 0.61
      efficiency: 0.37
      win: 0.89
      pick: 0.05
      fit: 0.49
    Amanita Charm:
      total: 0.56
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.68
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Dwarven Plate
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Eye of Providence
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
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Eye of Providence,
    Berserker''s Shield, Soul Gem, Gluttonous Grimoire, Rod of Asclepius, Oni Hunter''s
    Garb, Chandra''s Grace, Stampede, Erosion, Phoenix Feather, Draconic Scale, Spectral
    Armor, Runeforged Hammer, Pharaoh''s Curse, Lifebinder, Jotunn''s Revenge, Leviathan''s
    Hide, Yogi''s Necklace, Eye of the Storm, Freya''s Tears, Blood-Bound Book, Midgardian
    Mail, Shield Splitter, The Crusher, Bancroft''s Talon, Glorious Pridwen, Hydra''s
    Lament, Shogun''s Ofuda, Gladiator''s Shield, The Reaper, Ancile, Jade Scepter,
    Void Shield, Hide of the Nemean Lion.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.66
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.9
    Shifter's Shield:
      total: 0.58
      efficiency: 0.56
      win: 0.6
      pick: 0.29
      fit: 0.66
    Dwarven Plate:
      total: 0.59
      efficiency: 0.37
      win: 0.89
      pick: 0.05
      fit: 0.41
    Amanita Charm:
      total: 0.6
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Shifter's Shield
  - Dwarven Plate
  - The Crusher
  flex_slots:
  - Jotunn's Revenge
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Amanita Charm, Jotunn''s Revenge, The Crusher,
    Kinetic Cuirass, Soul Gem, Berserker''s Shield, Eye of Providence, Stone of Binding,
    Oni Hunter''s Garb, Screeching Gargoyle, Spear of the Magus, Void Shield, Avenging
    Blade, The Cosmic Horror, Void Stone, Shield of the Phoenix, Spear of Desolation,
    Erosion, Spectral Armor, Runeforged Hammer, Draconic Scale, Obsidian Shard, Pharaoh''s
    Curse, Shield Splitter, Hydra''s Lament, The Reaper, Yogi''s Necklace, Freya''s
    Tears, Riptalon, Silverbranch Bow, Leviathan''s Hide, Helm of Radiance, Midgardian
    Mail, Eye of the Storm, Rod of Asclepius, Heartseeker.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.56
      pick: 0.18
      fit: 0.26
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.63
    Shifter's Shield:
      total: 0.55
      efficiency: 0.56
      win: 0.6
      pick: 0.29
      fit: 0.48
    Dwarven Plate:
      total: 0.58
      efficiency: 0.37
      win: 0.89
      pick: 0.05
      fit: 0.34
    The Crusher:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Breastplate of Valor
  - Shifter's Shield
  - Dwarven Plate
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass,
    Golden Blade, Eye of Providence, Pharaoh''s Curse, Oni Hunter''s Garb, The Crusher,
    Jotunn''s Revenge, Riptalon, Runeforged Hammer, Lernaean Bow, Hydra''s Lament,
    Soul Gem, Shogun''s Ofuda, Tyrfing, Shield of the Phoenix, Shield Splitter, Silverbranch
    Bow, Spectral Armor, Yogi''s Necklace, Erosion, Eye of the Storm, Bracer of The
    Abyss, Draconic Scale, Dominance, Death Metal, Rod of Asclepius, Freya''s Tears,
    Helm of Radiance, Leviathan''s Hide, Bragi''s Harp, Avenging Blade, Midgardian
    Mail, Eros'' Bow, Hide of the Nemean Lion.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.56
      pick: 0.18
      fit: 0.2
    Shifter's Shield:
      total: 0.53
      efficiency: 0.56
      win: 0.6
      pick: 0.29
      fit: 0.37
    Dwarven Plate:
      total: 0.57
      efficiency: 0.37
      win: 0.89
      pick: 0.05
      fit: 0.26
    Pharaoh's Curse:
      total: 0.49
      efficiency: 0.58
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
  - Shifter's Shield
  - Dwarven Plate
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    + fit + win/pick). Underrated for this god: Amanita Charm, Jotunn''s Revenge,
    Kinetic Cuirass, Shield of the Phoenix, Hydra''s Lament, Soul Gem, Berserker''s
    Shield, Eye of Providence, Gluttonous Grimoire, Freya''s Tears, Oni Hunter''s
    Garb, The Crusher, Screeching Gargoyle, Chronos'' Pendant, Runeforged Hammer,
    Spear of Desolation, Gladiator''s Shield, Chandra''s Grace, Erosion, Shield Splitter,
    Spectral Armor, Prophetic Cloak, Draconic Scale, Pharaoh''s Curse, Yogi''s Necklace,
    Helm of Radiance, Rod of Asclepius, Eye of the Storm, Gem of Focus, Arondight,
    Death Metal, Leviathan''s Hide, Midgardian Mail, Jade Scepter, Spear of the Magus,
    Stone of Binding, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.44
      pick: 0.21
      fit: 0.48
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.56
      pick: 0.18
      fit: 0.48
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.46
    Shifter's Shield:
      total: 0.55
      efficiency: 0.56
      win: 0.6
      pick: 0.29
      fit: 0.45
    Dwarven Plate:
      total: 0.58
      efficiency: 0.37
      win: 0.89
      pick: 0.05
      fit: 0.32
    Amanita Charm:
      total: 0.53
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shifter's Shield
  - Dwarven Plate
  - The Crusher
  flex_slots:
  - The Crusher
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Berserker''s Shield, The Crusher, Jotunn''s
    Revenge, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Eye of Providence,
    Runeforged Hammer, Hydra''s Lament, Shield Splitter, Oni Hunter''s Garb, Soul
    Gem, Golden Blade, Eye of the Storm, Lernaean Bow, Pharaoh''s Curse, Shield of
    the Phoenix, Death Metal, Avenging Blade, Spectral Armor, Erosion, The Reaper,
    Yogi''s Necklace, Spear of the Magus, Draconic Scale, Damaru, Shogun''s Ofuda,
    Freya''s Tears, Leviathan''s Hide, The Cosmic Horror, Dominance, Helm of Radiance,
    Rod of Asclepius, Heartseeker, Tekko-Kagi, Midgardian Mail, Bragi''s Harp.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.36
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.56
      pick: 0.18
      fit: 0.23
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
    Shifter's Shield:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.29
      fit: 0.42
    Dwarven Plate:
      total: 0.58
      efficiency: 0.37
      win: 0.89
      pick: 0.05
      fit: 0.3
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Shifter's Shield
  - Dwarven Plate
  - The Crusher
  flex_slots:
  - The Crusher
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Amanita Charm,
    The Crusher, Jotunn''s Revenge, Kinetic Cuirass, Berserker''s Shield, Soul Gem,
    Eye of Providence, Runeforged Hammer, Oni Hunter''s Garb, Hydra''s Lament, Death
    Metal, Spear of the Magus, Shield Splitter, The Cosmic Horror, Helm of Radiance,
    Rod of Asclepius, Shield of the Phoenix, Eye of the Storm, Spectral Armor, Erosion,
    Spear of Desolation, Jade Scepter, Yogi''s Necklace, Pharaoh''s Curse, Avenging
    Blade, Draconic Scale, Golden Blade, Obsidian Shard, Triton''s Conch, The Reaper,
    Freya''s Tears, Lernaean Bow, Chronos'' Pendant, Leviathan''s Hide, Damaru, Ethereal
    Staff.'
  slot_scores:
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.56
      pick: 0.18
      fit: 0.23
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.41
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.29
      fit: 0.42
    Dwarven Plate:
      total: 0.58
      efficiency: 0.37
      win: 0.89
      pick: 0.05
      fit: 0.3
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Berserker''s
    Shield, Freya''s Tears, Gluttonous Grimoire, Oni Hunter''s Garb, Erosion, Shield
    of the Phoenix, Draconic Scale, Spectral Armor, Shield Splitter, Pharaoh''s Curse,
    Jotunn''s Revenge, Runeforged Hammer, Leviathan''s Hide, Eye of the Storm, Soul
    Gem, The Crusher, Midgardian Mail, Stone of Binding, Mantle Of Discord, Hydra''s
    Lament, Yogi''s Necklace, Hide of the Nemean Lion, Helm of Radiance, Magi''s Cloak,
    Shogun''s Ofuda, Stampede, Rod of Asclepius, Ancile, Gladiator''s Shield, Void
    Shield, Prophetic Cloak, Screeching Gargoyle, Doublet of Binding, Xibalban Effigy.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.68
    Genji's Guard:
      total: 0.52
      efficiency: 0.72
      win: 0.44
      pick: 0.21
      fit: 0.37
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.5
      efficiency: 0.59
      win: 0.44
      pick: 0.07
      fit: 0.62
    Amanita Charm:
      total: 0.56
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.68
  starter: *id001
---
