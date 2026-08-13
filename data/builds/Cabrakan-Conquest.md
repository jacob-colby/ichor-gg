---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.16
  aspect_win_rate: 0.62
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.38
    win_rate: 0.33
    alternates:
    - name: Chronos' Pendant
      pick_rate: 0.15
      win_rate: 0.58
    - name: Runeforged Hammer
      pick_rate: 0.15
      win_rate: 0.83
  - name: Genji's Guard
    pick_rate: 0.19
    win_rate: 0.53
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.77
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.27
  - name: Breastplate of Valor
    pick_rate: 0.16
    win_rate: 0.67
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.42
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.5
  - name: The Cosmic Horror
    pick_rate: 0.11
    win_rate: 0.75
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.75
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.71
  - name: Staff of Myrddin
    pick_rate: 0.09
    win_rate: 0.67
    alternates:
    - name: Draconic Scale
      pick_rate: 0.08
      win_rate: 0.4
    - name: Kinetic Cuirass
      pick_rate: 0.06
      win_rate: 0.5
  - name: Dwarven Plate
    pick_rate: 0.07
    win_rate: 0.67
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.05
      win_rate: 1.0
    - name: Mana Tome
      pick_rate: 0.05
      win_rate: 1.0
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.25
    win_rate: 0.65
  - name: Bumba's Cudgel
    pick_rate: 0.2
    win_rate: 0.5
  - name: Bluestone Brooch
    pick_rate: 0.19
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-08-13'
  god_win_rate: 0.5443037974683544
  god_matches_won: 43
  god_matches_played: 79
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-13'
  god_matches_analyzed: 2102
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Runeforged Hammer
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Amanita Charm, Berserker''s Shield, Gluttonous Grimoire,
    Jotunn''s Revenge, Freya''s Tears, The Crusher, Oni Hunter''s Garb, Shield Splitter,
    Shield of the Phoenix, Erosion, Hydra''s Lament, Eye of Providence, Eye of the
    Storm, Kinetic Cuirass, Spectral Armor, Pharaoh''s Curse, Soul Gem, Leviathan''s
    Hide, Golden Blade, Mantle Of Discord, Stone of Binding, Midgardian Mail, Death
    Metal, Helm of Radiance, Avenging Blade, Shogun''s Ofuda, Magi''s Cloak, Lernaean
    Bow, Damaru, Ancile, Screeching Gargoyle, Yogi''s Necklace, Void Shield, Hide
    of the Nemean Lion, Xibalban Effigy.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.37
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.66
      win: 0.67
      pick: 0.25
      fit: 0.31
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.62
      pick: 0.0
      fit: 0.37
    Runeforged Hammer:
      total: 0.65
      efficiency: 0.55
      win: 0.83
      pick: 0.15
      fit: 0.48
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.44
      win: 1.0
      pick: 0.15
      fit: 0.1
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.62
      pick: 0.0
      fit: 0.57
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Shield of the Phoenix
  - Runeforged Hammer
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Amanita Charm, Shield of the Phoenix, Soul Gem, Berserker''s
    Shield, Gluttonous Grimoire, Jotunn''s Revenge, Rod of Asclepius, Chandra''s Grace,
    The Crusher, Oni Hunter''s Garb, Freya''s Tears, Hydra''s Lament, Eye of the Storm,
    The Reaper, Shield Splitter, Erosion, Phoenix Feather, Eye of Providence, Spectral
    Armor, Pharaoh''s Curse, Blood-Bound Book, Kinetic Cuirass, Bancroft''s Talon,
    Golden Blade, Leviathan''s Hide, Riptalon, Avenging Blade, Lifebinder, Midgardian
    Mail, Death Metal, Shogun''s Ofuda, Glorious Pridwen, Yogi''s Necklace, Lernaean
    Bow, Damaru.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.38
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.66
      win: 0.67
      pick: 0.25
      fit: 0.28
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.8
    Runeforged Hammer:
      total: 0.65
      efficiency: 0.55
      win: 0.83
      pick: 0.15
      fit: 0.54
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.44
      win: 1.0
      pick: 0.15
      fit: 0.11
    Amanita Charm:
      total: 0.63
      efficiency: 0.63
      win: 0.62
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Runeforged Hammer
  - Gluttonous Grimoire
  - The Cosmic Horror
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Runeforged Hammer, Gluttonous Grimoire, Jotunn''s Revenge, The Crusher,
    Amanita Charm, Soul Gem, Berserker''s Shield, Stone of Binding, Avenging Blade,
    Screeching Gargoyle, Freya''s Tears, Void Shield, Spear of the Magus, Oni Hunter''s
    Garb, Void Stone, Hydra''s Lament, Shield of the Phoenix, The Reaper, Shield Splitter,
    Spear of Desolation, Erosion, Spectral Armor, Riptalon, Eye of Providence, Obsidian
    Shard, Eye of the Storm, Pharaoh''s Curse, Heartseeker, Kinetic Cuirass, Silverbranch
    Bow, Leviathan''s Hide, Death Metal, Golden Blade, Helm of Radiance, Midgardian
    Mail.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.66
      win: 0.62
      pick: 0.0
      fit: 0.54
    Runeforged Hammer:
      total: 0.63
      efficiency: 0.55
      win: 0.83
      pick: 0.15
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.6
      efficiency: 0.66
      win: 0.62
      pick: 0.0
      fit: 0.56
    The Cosmic Horror:
      total: 0.6
      efficiency: 0.58
      win: 0.75
      pick: 0.18
      fit: 0.34
    The Crusher:
      total: 0.59
      efficiency: 0.63
      win: 0.62
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.44
      win: 1.0
      pick: 0.15
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Breastplate of Valor
  - Runeforged Hammer
  - Rod of Tahuti
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Berserker''s Shield, Gluttonous Grimoire, Amanita
    Charm, Golden Blade, Pharaoh''s Curse, Jotunn''s Revenge, Riptalon, The Crusher,
    Freya''s Tears, Oni Hunter''s Garb, Soul Gem, Shogun''s Ofuda, Lernaean Bow, Shield
    of the Phoenix, Silverbranch Bow, Hydra''s Lament, Tyrfing, Spectral Armor, Erosion,
    Shield Splitter, Eye of Providence, Bracer of The Abyss, Kinetic Cuirass, Eye
    of the Storm, Helm of Radiance, Leviathan''s Hide, Midgardian Mail, Mantle Of
    Discord, Yogi''s Necklace, Stone of Binding, Eros'' Bow, Death Metal, Dominance,
    Spear of the Magus, Rod of Asclepius.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.54
      win: 0.62
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.25
      fit: 0.2
    Runeforged Hammer:
      total: 0.62
      efficiency: 0.55
      win: 0.83
      pick: 0.15
      fit: 0.31
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.44
      win: 1.0
      pick: 0.15
      fit: 0.06
    Pharaoh's Curse:
      total: 0.55
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Runeforged Hammer
  - Freya's Tears
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    + fit + win/pick). Underrated for this god: Runeforged Hammer, Freya''s Tears,
    Jotunn''s Revenge, Shield of the Phoenix, Soul Gem, Amanita Charm, Gluttonous
    Grimoire, Berserker''s Shield, Hydra''s Lament, Oni Hunter''s Garb, Screeching
    Gargoyle, The Crusher, Spear of Desolation, Chandra''s Grace, Gladiator''s Shield,
    Erosion, Spectral Armor, Eye of Providence, Prophetic Cloak, Chronos'' Pendant,
    Pharaoh''s Curse, Shield Splitter, Helm of Radiance, Kinetic Cuirass, Gem of Focus,
    Leviathan''s Hide, Eye of the Storm, Mantle Of Discord, Midgardian Mail, Rod of
    Asclepius, Stone of Binding, Spear of the Magus, Death Metal, Arondight, Jade
    Scepter, Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.53
      pick: 0.26
      fit: 0.48
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.66
      win: 0.67
      pick: 0.25
      fit: 0.48
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.66
      win: 0.62
      pick: 0.0
      fit: 0.46
    Runeforged Hammer:
      total: 0.62
      efficiency: 0.55
      win: 0.83
      pick: 0.15
      fit: 0.32
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.62
      pick: 0.0
      fit: 0.64
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.44
      win: 1.0
      pick: 0.15
      fit: 0.13
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Runeforged Hammer
  - The Cosmic Horror
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Runeforged Hammer, Jotunn''s Revenge, Berserker''s
    Shield, Gluttonous Grimoire, The Crusher, Amanita Charm, Hydra''s Lament, Freya''s
    Tears, Soul Gem, Oni Hunter''s Garb, Shield Splitter, Pharaoh''s Curse, Golden
    Blade, Shield of the Phoenix, Lernaean Bow, Eye of the Storm, Erosion, Spectral
    Armor, Death Metal, Eye of Providence, Spear of the Magus, Shogun''s Ofuda, The
    Reaper, Damaru, Kinetic Cuirass, Avenging Blade, Riptalon, Leviathan''s Hide,
    Helm of Radiance, Midgardian Mail, Mantle Of Discord, Stone of Binding, Heartseeker,
    Tekko-Kagi, Silverbranch Bow.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.36
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.25
      fit: 0.23
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.66
      win: 0.62
      pick: 0.0
      fit: 0.45
    Runeforged Hammer:
      total: 0.64
      efficiency: 0.55
      win: 0.83
      pick: 0.15
      fit: 0.44
    The Cosmic Horror:
      total: 0.58
      efficiency: 0.58
      win: 0.75
      pick: 0.18
      fit: 0.19
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.44
      win: 1.0
      pick: 0.15
      fit: 0.19
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Runeforged Hammer
  - Gluttonous Grimoire
  - The Cosmic Horror
  - Rod of Tahuti
  flex_slots:
  - Breastplate of Valor
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Runeforged Hammer, Gluttonous Grimoire,
    Jotunn''s Revenge, The Crusher, Amanita Charm, Soul Gem, Berserker''s Shield,
    Freya''s Tears, Spear of the Magus, Oni Hunter''s Garb, Hydra''s Lament, Death
    Metal, Shield Splitter, Helm of Radiance, Shield of the Phoenix, Spear of Desolation,
    Erosion, Spectral Armor, Eye of the Storm, Rod of Asclepius, Eye of Providence,
    Pharaoh''s Curse, Obsidian Shard, Jade Scepter, Kinetic Cuirass, Golden Blade,
    Leviathan''s Hide, Blood-Bound Book, Lernaean Bow, The Reaper, Damaru, Bancroft''s
    Talon, Midgardian Mail, Mantle Of Discord, Chronos'' Pendant.'
  slot_scores:
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.25
      fit: 0.23
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.62
      pick: 0.0
      fit: 0.41
    Runeforged Hammer:
      total: 0.63
      efficiency: 0.55
      win: 0.83
      pick: 0.15
      fit: 0.4
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.66
      win: 0.62
      pick: 0.0
      fit: 0.55
    The Cosmic Horror:
      total: 0.6
      efficiency: 0.58
      win: 0.75
      pick: 0.18
      fit: 0.33
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.44
      win: 1.0
      pick: 0.15
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Gluttonous Grimoire, Jotunn''s Revenge, Freya''s Tears, The Crusher, Oni Hunter''s
    Garb, Shield Splitter, Shield of the Phoenix, Erosion, Hydra''s Lament, Eye of
    Providence, Runeforged Hammer, Eye of the Storm, Spectral Armor, Pharaoh''s Curse,
    Soul Gem, Leviathan''s Hide, Golden Blade, Mantle Of Discord, Stone of Binding,
    Midgardian Mail, Death Metal, Helm of Radiance, Avenging Blade, Shogun''s Ofuda,
    Magi''s Cloak, Lernaean Bow, Damaru, Ancile, Screeching Gargoyle, Yogi''s Necklace,
    Void Shield, Hide of the Nemean Lion, Xibalban Effigy.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.53
      pick: 0.26
      fit: 0.31
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.62
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.5
      pick: 0.13
      fit: 0.67
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.62
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.62
      pick: 0.0
      fit: 0.57
  starter: *id001
---
