---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.11
  aspect_win_rate: 0.32
  slot_order:
  - name: Runeforged Hammer
    pick_rate: 0.44
    win_rate: 0.63
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.13
      win_rate: 0.57
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.65
  - name: Shifter's Shield
    pick_rate: 0.13
    win_rate: 0.71
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.59
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.72
  - name: Freya's Tears
    pick_rate: 0.15
    win_rate: 0.59
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.65
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.68
  - name: Genji's Guard
    pick_rate: 0.11
    win_rate: 0.55
    alternates:
    - name: Freya's Tears
      pick_rate: 0.15
      win_rate: 0.71
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.62
  - name: Shell of Rebuke
    pick_rate: 0.06
    win_rate: 0.64
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.67
    - name: Kinetic Cuirass
      pick_rate: 0.06
      win_rate: 0.46
  - name: Sage's Ring
    pick_rate: 0.09
    win_rate: 0.86
    alternates:
    - name: Draconic Scale
      pick_rate: 0.07
      win_rate: 0.64
    - name: Veve Charm
      pick_rate: 0.07
      win_rate: 0.7
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.3
    win_rate: 0.62
  - name: Bumba's Cudgel
    pick_rate: 0.29
    win_rate: 0.55
  - name: Bluestone Pendant
    pick_rate: 0.1
    win_rate: 0.58
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-10-30'
  god_win_rate: 0.5666666666666667
  god_matches_won: 153
  god_matches_played: 270
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
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - Shield Splitter
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Shield
    Splitter, Breastplate of Valor, Eye of the Storm, Erosion, Berserker''s Shield,
    Eye of Providence, Shield of the Phoenix, Hydra''s Lament, Stone of Binding, Helm
    of Radiance, Gluttonous Grimoire, Magi''s Cloak, Avenging Blade, Midgardian Mail,
    Mantle Of Discord, Oni Hunter''s Garb, Screeching Gargoyle, Leviathan''s Hide,
    Hide of the Nemean Lion, Void Shield, Ancile, Spear of Desolation, Stampede, Daybreak
    Gavel, Rod of Asclepius, Prophetic Cloak, Spectral Armor, Heartseeker, Void Stone,
    Helm of Darkness, Spear of the Magus, Xibalban Effigy, Soul Gem.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.69
      win: 0.64
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.57
      win: 0.68
      pick: 0.14
      fit: 0.67
    Runeforged Hammer:
      total: 0.57
      efficiency: 0.56
      win: 0.63
      pick: 0.44
      fit: 0.48
    Shield Splitter:
      total: 0.57
      efficiency: 0.55
      win: 0.64
      pick: 0.0
      fit: 0.63
    Shifter's Shield:
      total: 0.61
      efficiency: 0.55
      win: 0.71
      pick: 0.18
      fit: 0.57
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Kinetic Cuirass
  - Runeforged Hammer
  - Shifter's Shield
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Shield of the Phoenix,
    Jotunn''s Revenge, Rod of Asclepius, Shield Splitter, Soul Gem, Eye of the Storm,
    Berserker''s Shield, Breastplate of Valor, Erosion, Ethereal Staff, Eye of Providence,
    Yogi''s Necklace, The Reaper, Hydra''s Lament, Phoenix Feather, Gluttonous Grimoire,
    Avenging Blade, Chandra''s Grace, Lifebinder, Glorious Pridwen, Midgardian Mail,
    Stone of Binding, Oni Hunter''s Garb, Helm of Radiance, Daybreak Gavel, Leviathan''s
    Hide, Hide of the Nemean Lion, Void Shield, Magi''s Cloak, Sphere of Negation,
    Ancile, Stampede, Spear of Desolation, Screeching Gargoyle.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.69
      win: 0.64
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.57
      win: 0.68
      pick: 0.14
      fit: 0.66
    Runeforged Hammer:
      total: 0.58
      efficiency: 0.56
      win: 0.63
      pick: 0.44
      fit: 0.54
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.53
      win: 0.64
      pick: 0.0
      fit: 0.8
    Shifter's Shield:
      total: 0.6
      efficiency: 0.55
      win: 0.71
      pick: 0.18
      fit: 0.56
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Kinetic Cuirass
  - Runeforged Hammer
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Avenging Blade
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Kinetic Cuirass, Amanita Charm,
    Stone of Binding, Gluttonous Grimoire, Avenging Blade, Screeching Gargoyle, Void
    Shield, Spear of Desolation, Spear of the Magus, Shield Splitter, Void Stone,
    Heartseeker, Soul Gem, Breastplate of Valor, Obsidian Shard, Berserker''s Shield,
    Titan''s Bane, The Crusher, Eye of the Storm, Erosion, The Reaper, Hydra''s Lament,
    Eye of Providence, Shield of the Phoenix, Helm of Radiance, Doom Orb, The World
    Stone, Magi''s Cloak, Dreamer''s Idol, Pendulum Blade, Midgardian Mail, Daybreak
    Gavel, Oni Hunter''s Garb, Avatar''s Parashu, Mantle Of Discord.'
  slot_scores:
    Stone of Binding:
      total: 0.57
      efficiency: 0.5
      win: 0.64
      pick: 0.0
      fit: 0.7
    Avenging Blade:
      total: 0.56
      efficiency: 0.49
      win: 0.64
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.69
      win: 0.64
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.57
      win: 0.68
      pick: 0.14
      fit: 0.52
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.71
      pick: 0.18
      fit: 0.42
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Kinetic Cuirass
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Nimble Ring
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Golden Blade
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Kinetic Cuirass, Amanita Charm,
    Jotunn''s Revenge, Nimble Ring, Golden Blade, Gluttonous Grimoire, Breastplate
    of Valor, Tyrfing, Shield Splitter, Pharaoh''s Curse, Soul Gem, Riptalon, Lernaean
    Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Helm of Radiance, Eye of Providence,
    Toxic Blade, Shield of the Phoenix, Hydra''s Lament, Eye of the Storm, Stone of
    Binding, Magi''s Cloak, Daybreak Gavel, Spear of the Magus, Midgardian Mail, Spear
    of Desolation, Screeching Gargoyle, The Reaper, Bragi''s Harp, Tekko-Kagi, Oni
    Hunter''s Garb, Mantle Of Discord, Rod of Asclepius.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.64
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.57
      win: 0.68
      pick: 0.14
      fit: 0.47
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.3
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.71
      pick: 0.18
      fit: 0.37
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Kinetic Cuirass
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Amanita Charm
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Kinetic Cuirass, Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Spear
    of Desolation, Hydra''s Lament, Soul Gem, Lotus Sickle, Screeching Gargoyle, Chronos''
    Pendant, Shield Splitter, Berserker''s Shield, Prophetic Cloak, Helm of Radiance,
    Erosion, Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield, Stone of
    Binding, Eye of the Storm, Gem of Focus, Arondight, Magi''s Cloak, Spear of the
    Magus, Rod of Asclepius, Eye of Erebus, Midgardian Mail, Mantle Of Discord, Oni
    Hunter''s Garb, Glorious Pridwen, Daybreak Gavel, Obsidian Shard, Chandra''s Grace,
    Jade Scepter, Leviathan''s Hide.'
  slot_scores:
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.64
      win: 0.62
      pick: 0.13
      fit: 0.48
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.69
      win: 0.64
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.57
      win: 0.68
      pick: 0.14
      fit: 0.55
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.59
      pick: 0.23
      fit: 0.64
    Shifter's Shield:
      total: 0.59
      efficiency: 0.55
      win: 0.71
      pick: 0.18
      fit: 0.45
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Runeforged Hammer
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Kinetic
    Cuirass, Amanita Charm, Berserker''s Shield, Shield Splitter, Breastplate of Valor,
    Golden Blade, Eye of the Storm, Gluttonous Grimoire, Hydra''s Lament, Heartseeker,
    Erosion, Lernaean Bow, Spear of Desolation, Eye of Providence, Spear of the Magus,
    Tekko-Kagi, Tyrfing, Avenging Blade, Shield of the Phoenix, Helm of Radiance,
    Stone of Binding, Soul Gem, Titan''s Bane, The Crusher, Obsidian Shard, Pharaoh''s
    Curse, Magi''s Cloak, The Reaper, Nimble Ring, Silverbranch Bow, Shogun''s Ofuda,
    Midgardian Mail, Daybreak Gavel, Screeching Gargoyle, Oni Hunter''s Garb.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.69
      win: 0.64
      pick: 0.0
      fit: 0.45
    Runeforged Hammer:
      total: 0.57
      efficiency: 0.56
      win: 0.63
      pick: 0.44
      fit: 0.44
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.57
      win: 0.68
      pick: 0.14
      fit: 0.52
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.71
      pick: 0.18
      fit: 0.42
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Runeforged Hammer
  - Kinetic Cuirass
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Runeforged Hammer
  - Kinetic Cuirass
  - Shifter's Shield
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Kinetic Cuirass, Amanita Charm, Gluttonous Grimoire, Spear of Desolation, Shield
    Splitter, Spear of the Magus, Helm of Radiance, Breastplate of Valor, Soul Gem,
    Obsidian Shard, Berserker''s Shield, Eye of the Storm, Hydra''s Lament, Rod of
    Asclepius, Erosion, Eye of Providence, Lotus Sickle, Heartseeker, Shield of the
    Phoenix, Jade Scepter, Stone of Binding, Doom Orb, Death Metal, Avenging Blade,
    Wish-Granting Pearl, The World Stone, Magi''s Cloak, Chronos'' Pendant, Helm of
    Darkness, Titan''s Bane, The Crusher, Dreamer''s Idol, Triton''s Conch, Midgardian
    Mail, Daybreak Gavel.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.69
      win: 0.64
      pick: 0.0
      fit: 0.41
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.56
      win: 0.63
      pick: 0.44
      fit: 0.4
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.57
      win: 0.68
      pick: 0.14
      fit: 0.52
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.71
      pick: 0.18
      fit: 0.42
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.85
      win: 0.64
      pick: 0.0
      fit: 0.33
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Runeforged Hammer
  - Kinetic Cuirass
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Jotunn''s
    Revenge, Shield Splitter, Breastplate of Valor, Eye of the Storm, Erosion, Berserker''s
    Shield, Eye of Providence, Shield of the Phoenix, Hydra''s Lament, Stone of Binding,
    Helm of Radiance, Gluttonous Grimoire, Magi''s Cloak, Avenging Blade, Midgardian
    Mail, Mantle Of Discord, Oni Hunter''s Garb, Screeching Gargoyle, Leviathan''s
    Hide, Hide of the Nemean Lion, Void Shield, Ancile, Spear of Desolation, Stampede,
    Daybreak Gavel, Rod of Asclepius, Prophetic Cloak, Spectral Armor, Heartseeker,
    Void Stone, Helm of Darkness, Spear of the Magus, Xibalban Effigy, Soul Gem.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.69
      win: 0.64
      pick: 0.0
      fit: 0.37
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.55
      pick: 0.18
      fit: 0.31
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.57
      win: 0.68
      pick: 0.14
      fit: 0.67
    Shield Splitter:
      total: 0.57
      efficiency: 0.55
      win: 0.64
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.59
      pick: 0.23
      fit: 0.52
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
---
