---
type: smite-build
god: Artio
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Denmother
  aspect_pick_rate: 0.47
  aspect_win_rate: 0.61
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.17
    win_rate: 0.6
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.57
    - name: Gauntlet of Thebes
      pick_rate: 0.15
      win_rate: 0.43
  - name: Prophetic Cloak
    pick_rate: 0.1
    win_rate: 0.61
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.51
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.56
  - name: Freya's Tears
    pick_rate: 0.17
    win_rate: 0.66
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.53
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.48
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.45
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.35
  - name: Hide of the Nemean Lion
    pick_rate: 0.05
    win_rate: 0.4
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.71
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.52
  - name: Olmec Blue
    pick_rate: 0.06
    win_rate: 0.69
    alternates:
    - name: Medal of Defense
      pick_rate: 0.06
      win_rate: 0.67
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.73
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.24
    win_rate: 0.57
  - name: Bluestone Pendant
    pick_rate: 0.13
    win_rate: 0.56
  - name: Bumba's Cudgel
    pick_rate: 0.12
    win_rate: 0.37
  source_url: https://smitebrain.com/gods/artio/
  last_verified: '2026-10-30'
  god_win_rate: 0.5425531914893617
  god_matches_won: 204
  god_matches_played: 376
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
  - Shield Splitter
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield
    Splitter, Runeforged Hammer, Eye of the Storm, Breastplate of Valor, Erosion,
    Berserker''s Shield, Eye of Providence, Draconic Scale, Shield of the Phoenix,
    Hydra''s Lament, Gluttonous Grimoire, Stone of Binding, Avenging Blade, Helm of
    Radiance, Prophetic Cloak, Magi''s Cloak, Midgardian Mail, Oni Hunter''s Garb,
    Mantle Of Discord, Screeching Gargoyle, Leviathan''s Hide, Spear of Desolation,
    Void Shield, Daybreak Gavel, Rod of Asclepius, Ancile, Stampede, Heartseeker,
    Spectral Armor, Soul Gem, Spear of the Magus, Void Stone, Lotus Sickle, Jade Scepter,
    Hide of the Nemean Lion.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.66
    Shield Splitter:
      total: 0.55
      efficiency: 0.55
      win: 0.58
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.66
      pick: 0.26
      fit: 0.5
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.57
      pick: 0.17
      fit: 0.56
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.56
  community_ordered:
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
  - Shield of the Phoenix
  - Runeforged Hammer
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Shield of the Phoenix, Jotunn''s Revenge,
    Kinetic Cuirass, Rod of Asclepius, Runeforged Hammer, Shield Splitter, Soul Gem,
    Eye of the Storm, Berserker''s Shield, Erosion, Ethereal Staff, Breastplate of
    Valor, Eye of Providence, Yogi''s Necklace, The Reaper, Draconic Scale, Hydra''s
    Lament, Phoenix Feather, Gluttonous Grimoire, Avenging Blade, Chandra''s Grace,
    Lifebinder, Glorious Pridwen, Midgardian Mail, Helm of Radiance, Stone of Binding,
    Oni Hunter''s Garb, Daybreak Gavel, Leviathan''s Hide, Void Shield, Magi''s Cloak,
    Sphere of Negation, Ancile, Spear of Desolation, Stampede, Screeching Gargoyle,
    Hide of the Nemean Lion.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.8
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.54
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.66
      pick: 0.26
      fit: 0.46
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Avenging Blade
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Avenging Blade
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire,
    Stone of Binding, Avenging Blade, Kinetic Cuirass, Screeching Gargoyle, Spear
    of Desolation, Spear of the Magus, Void Shield, Soul Gem, Heartseeker, Obsidian
    Shard, Void Stone, Shield Splitter, Runeforged Hammer, Breastplate of Valor, Titan''s
    Bane, The Crusher, Berserker''s Shield, Eye of the Storm, The Reaper, Hydra''s
    Lament, Erosion, Eye of Providence, Shield of the Phoenix, Doom Orb, Draconic
    Scale, Helm of Radiance, The World Stone, Dreamer''s Idol, Pendulum Blade, Avatar''s
    Parashu, Magi''s Cloak, Daybreak Gavel, Midgardian Mail, Oni Hunter''s Garb, Rod
    of Asclepius.'
  slot_scores:
    Stone of Binding:
      total: 0.54
      efficiency: 0.5
      win: 0.58
      pick: 0.0
      fit: 0.68
    Avenging Blade:
      total: 0.54
      efficiency: 0.49
      win: 0.58
      pick: 0.0
      fit: 0.69
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.56
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.5
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.66
      pick: 0.26
      fit: 0.36
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.4
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
    Nimble Ring, Kinetic Cuirass, Golden Blade, Gluttonous Grimoire, Tyrfing, Breastplate
    of Valor, Soul Gem, Runeforged Hammer, Pharaoh''s Curse, Shield Splitter, Riptalon,
    Lernaean Bow, Silverbranch Bow, Shogun''s Ofuda, Toxic Blade, Erosion, Helm of
    Radiance, Hydra''s Lament, Shield of the Phoenix, Eye of the Storm, Eye of Providence,
    Draconic Scale, Stone of Binding, Daybreak Gavel, Spear of Desolation, Spear of
    the Magus, Bragi''s Harp, Magi''s Cloak, The Reaper, Tekko-Kagi, Midgardian Mail,
    Rod of Asclepius, Screeching Gargoyle, Avenging Blade, Dominance.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.55
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.66
      pick: 0.26
      fit: 0.31
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.35
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
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Prophetic Cloak — magical protection
    swap_item: Prophetic Cloak
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Spear
    of Desolation, Hydra''s Lament, Soul Gem, Prophetic Cloak, Lotus Sickle, Screeching
    Gargoyle, Chronos'' Pendant, Berserker''s Shield, Shield Splitter, Gluttonous
    Grimoire, Runeforged Hammer, Helm of Radiance, Gladiator''s Shield, Erosion, Eye
    of Providence, Draconic Scale, Gem of Focus, Arondight, Eye of the Storm, Stone
    of Binding, Eye of Erebus, Rod of Asclepius, Spear of the Magus, Magi''s Cloak,
    Midgardian Mail, Chandra''s Grace, Daybreak Gavel, Obsidian Shard, Oni Hunter''s
    Garb, Jade Scepter, Glorious Pridwen, Mantle Of Discord, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.53
      pick: 0.17
      fit: 0.48
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.56
      pick: 0.12
      fit: 0.48
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.53
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.66
      pick: 0.26
      fit: 0.63
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.43
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
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer, Golden
    Blade, Gluttonous Grimoire, Eye of the Storm, Breastplate of Valor, Hydra''s Lament,
    Heartseeker, Lernaean Bow, Spear of Desolation, Tekko-Kagi, Spear of the Magus,
    Avenging Blade, Tyrfing, Erosion, Eye of Providence, Shield of the Phoenix, Soul
    Gem, Titan''s Bane, The Crusher, Helm of Radiance, Draconic Scale, Obsidian Shard,
    Stone of Binding, Pharaoh''s Curse, The Reaper, Nimble Ring, Silverbranch Bow,
    Magi''s Cloak, Shogun''s Ofuda, Daybreak Gavel, Midgardian Mail, Toxic Blade,
    Bragi''s Harp.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.5
    Shield Splitter:
      total: 0.53
      efficiency: 0.55
      win: 0.58
      pick: 0.0
      fit: 0.51
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.66
      pick: 0.26
      fit: 0.36
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Spear of Desolation, Spear
    of the Magus, Shield Splitter, Soul Gem, Runeforged Hammer, Helm of Radiance,
    Obsidian Shard, Breastplate of Valor, Berserker''s Shield, Eye of the Storm, Hydra''s
    Lament, Rod of Asclepius, Lotus Sickle, Heartseeker, Erosion, Jade Scepter, Eye
    of Providence, Shield of the Phoenix, Draconic Scale, Doom Orb, Death Metal, Avenging
    Blade, Stone of Binding, Wish-Granting Pearl, The World Stone, Chronos'' Pendant,
    Titan''s Bane, The Crusher, Dreamer''s Idol, Triton''s Conch, Helm of Darkness,
    Magi''s Cloak, Daybreak Gavel, Midgardian Mail.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.5
      win: 0.58
      pick: 0.0
      fit: 0.18
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.42
    Transcendence:
      total: 0.47
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.18
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.66
      pick: 0.26
      fit: 0.36
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.85
      win: 0.58
      pick: 0.0
      fit: 0.34
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
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
    Underrated for this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Kinetic
    Cuirass, Shield Splitter, Breastplate of Valor, Runeforged Hammer, Eye of the
    Storm, Erosion, Berserker''s Shield, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Hydra''s Lament, Gluttonous Grimoire, Stone of Binding, Avenging
    Blade, Helm of Radiance, Magi''s Cloak, Midgardian Mail, Oni Hunter''s Garb, Mantle
    Of Discord, Screeching Gargoyle, Leviathan''s Hide, Hide of the Nemean Lion, Spear
    of Desolation, Void Shield, Daybreak Gavel, Rod of Asclepius, Ancile, Stampede,
    Heartseeker, Spectral Armor, Soul Gem, Spear of the Magus, Prophetic Cloak, Void
    Stone, Lotus Sickle, Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.53
      pick: 0.17
      fit: 0.31
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.66
    Shield Splitter:
      total: 0.55
      efficiency: 0.55
      win: 0.58
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.66
      pick: 0.26
      fit: 0.5
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
