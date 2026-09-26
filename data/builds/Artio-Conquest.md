---
type: smite-build
god: Artio
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Denmother
  aspect_pick_rate: 0.57
  aspect_win_rate: 0.5
  slot_order:
  - name: Chandra's Grace
    pick_rate: 0.15
    win_rate: 0.37
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.45
    - name: Rod of Asclepius
      pick_rate: 0.1
      win_rate: 0.72
  - name: Breastplate of Valor
    pick_rate: 0.12
    win_rate: 0.59
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.56
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.56
  - name: Freya's Tears
    pick_rate: 0.14
    win_rate: 0.38
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.55
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.29
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.45
    alternates:
    - name: Freya's Tears
      pick_rate: 0.15
      win_rate: 0.46
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.5
  - name: Genji's Guard
    pick_rate: 0.05
    win_rate: 0.88
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.63
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.54
  - name: Shield
    pick_rate: 0.07
    win_rate: 0.43
    alternates:
    - name: Mana Tome
      pick_rate: 0.06
      win_rate: 0.83
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.83
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.17
    win_rate: 0.5
  - name: Bluestone Pendant
    pick_rate: 0.17
    win_rate: 0.34
  - name: Bumba's Hammer
    pick_rate: 0.14
    win_rate: 0.69
  source_url: https://smitebrain.com/gods/artio/
  last_verified: '2026-09-26'
  god_win_rate: 0.518918918918919
  god_matches_won: 96
  god_matches_played: 185
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-26'
  god_matches_analyzed: 4198
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Genji''s Guard, Rod of Tahuti, Amanita Charm, Rod of Asclepius, Jotunn''s
    Revenge, Kinetic Cuirass, Shield Splitter, Shifter''s Shield, Runeforged Hammer,
    Eye of the Storm, Berserker''s Shield, Erosion, Eye of Providence, Draconic Scale,
    Shield of the Phoenix, Hydra''s Lament, Stone of Binding, Gluttonous Grimoire,
    Avenging Blade, Helm of Radiance, Magi''s Cloak, Midgardian Mail, Mantle Of Discord,
    Screeching Gargoyle, Hide of the Nemean Lion, Heartseeker, Leviathan''s Hide,
    Spear of Desolation, Void Shield, Stampede, Daybreak Gavel, Ancile, Oni Hunter''s
    Garb, Prophetic Cloak, Soul Gem, Void Stone, Spectral Armor, Spear of the Magus,
    Arondight, Xibalban Effigy.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.06
    Genji's Guard:
      total: 0.68
      efficiency: 0.66
      win: 0.88
      pick: 0.11
      fit: 0.31
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.59
      pick: 0.16
      fit: 0.31
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.39
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.22
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  - Rod of Asclepius
  flex_slots:
  - Kinetic Cuirass
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Genji''s Guard, Rod of Asclepius, Amanita Charm, Rod of Tahuti, Jotunn''s
    Revenge, Shield of the Phoenix, Kinetic Cuirass, Shifter''s Shield, Runeforged
    Hammer, Shield Splitter, Soul Gem, Eye of the Storm, Berserker''s Shield, Erosion,
    Ethereal Staff, Eye of Providence, The Reaper, Draconic Scale, Yogi''s Necklace,
    Phoenix Feather, Hydra''s Lament, Gluttonous Grimoire, Avenging Blade, Glorious
    Pridwen, Lifebinder, Stone of Binding, Midgardian Mail, Helm of Radiance, Daybreak
    Gavel, Hide of the Nemean Lion, Magi''s Cloak, Leviathan''s Hide, Sphere of Negation,
    Void Shield, Stampede, Ancile, Screeching Gargoyle, Oni Hunter''s Garb, Heartseeker,
    Chandra''s Grace.'
  slot_scores:
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.59
      pick: 0.16
      fit: 0.28
    Genji's Guard:
      total: 0.67
      efficiency: 0.66
      win: 0.88
      pick: 0.11
      fit: 0.28
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.66
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.86
    Rod of Asclepius:
      total: 0.61
      efficiency: 0.57
      win: 0.72
      pick: 0.1
      fit: 0.57
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Rod of Asclepius
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    for this god: Genji''s Guard, Rod of Tahuti, Jotunn''s Revenge, Rod of Asclepius,
    Amanita Charm, Stone of Binding, Gluttonous Grimoire, Avenging Blade, Kinetic
    Cuirass, Screeching Gargoyle, Spear of Desolation, Heartseeker, Spear of the Magus,
    Void Shield, Soul Gem, Shifter''s Shield, Void Stone, Obsidian Shard, Shield Splitter,
    Runeforged Hammer, Titan''s Bane, The Crusher, Berserker''s Shield, Eye of the
    Storm, The Reaper, Hydra''s Lament, Erosion, Eye of Providence, Shield of the
    Phoenix, Doom Orb, Draconic Scale, Helm of Radiance, The World Stone, Pendulum
    Blade, Dreamer''s Idol, Avatar''s Parashu, Magi''s Cloak, Daybreak Gavel, Midgardian
    Mail, Mantle Of Discord.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.04
    Genji's Guard:
      total: 0.66
      efficiency: 0.66
      win: 0.88
      pick: 0.11
      fit: 0.22
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.56
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.16
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.56
      pick: 0.0
      fit: 0.35
    Rod of Asclepius:
      total: 0.55
      efficiency: 0.57
      win: 0.72
      pick: 0.1
      fit: 0.16
  community_ordered:
  - Genji's Guard
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Rod of Asclepius
  flex_slots:
  - Nimble Ring
  - Golden Blade
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Genji''s Guard, Rod of Tahuti, Berserker''s Shield, Rod of Asclepius,
    Jotunn''s Revenge, Amanita Charm, Nimble Ring, Kinetic Cuirass, Golden Blade,
    Gluttonous Grimoire, Shifter''s Shield, Tyrfing, Runeforged Hammer, Soul Gem,
    Shield Splitter, Pharaoh''s Curse, Riptalon, Lernaean Bow, Silverbranch Bow, Shogun''s
    Ofuda, Toxic Blade, Hydra''s Lament, Erosion, Helm of Radiance, Eye of the Storm,
    Shield of the Phoenix, Eye of Providence, Stone of Binding, Draconic Scale, Daybreak
    Gavel, Magi''s Cloak, The Reaper, Bragi''s Harp, Tekko-Kagi, Screeching Gargoyle,
    Spear of Desolation, Spear of the Magus, Avenging Blade, Midgardian Mail, Mantle
    Of Discord.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.55
    Genji's Guard:
      total: 0.66
      efficiency: 0.66
      win: 0.88
      pick: 0.11
      fit: 0.19
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.3
    Rod of Asclepius:
      total: 0.55
      efficiency: 0.57
      win: 0.72
      pick: 0.1
      fit: 0.14
  community_ordered:
  - Genji's Guard
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Spear of Desolation
  - Rod of Asclepius
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Jotunn''s Revenge,
    Rod of Tahuti, Rod of Asclepius, Amanita Charm, Shield of the Phoenix, Kinetic
    Cuirass, Spear of Desolation, Hydra''s Lament, Soul Gem, Screeching Gargoyle,
    Shifter''s Shield, Chronos'' Pendant, Berserker''s Shield, Shield Splitter, Prophetic
    Cloak, Runeforged Hammer, Gluttonous Grimoire, Helm of Radiance, Gladiator''s
    Shield, Erosion, Eye of Providence, Arondight, Gem of Focus, Draconic Scale, Eye
    of the Storm, Stone of Binding, Eye of Erebus, Spear of the Magus, Magi''s Cloak,
    Midgardian Mail, Glorious Pridwen, Daybreak Gavel, Obsidian Shard, Mantle Of Discord,
    Jade Scepter, Hide of the Nemean Lion, Wish-Granting Pearl, Avenging Blade, Chandra''s
    Grace.'
  slot_scores:
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.59
      pick: 0.16
      fit: 0.48
    Genji's Guard:
      total: 0.7
      efficiency: 0.66
      win: 0.88
      pick: 0.11
      fit: 0.48
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.53
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.47
    Rod of Asclepius:
      total: 0.56
      efficiency: 0.57
      win: 0.72
      pick: 0.1
      fit: 0.23
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Rod of Asclepius
  flex_slots:
  - Breastplate of Valor
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Genji''s Guard, Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged
    Hammer, Shifter''s Shield, Golden Blade, Eye of the Storm, Gluttonous Grimoire,
    Hydra''s Lament, Heartseeker, Lernaean Bow, Tekko-Kagi, Spear of Desolation, Tyrfing,
    Avenging Blade, Spear of the Magus, Erosion, Titan''s Bane, Eye of Providence,
    Shield of the Phoenix, Soul Gem, The Crusher, Helm of Radiance, Draconic Scale,
    Obsidian Shard, Stone of Binding, Pharaoh''s Curse, The Reaper, Nimble Ring, Silverbranch
    Bow, Magi''s Cloak, Shogun''s Ofuda, Screeching Gargoyle, Daybreak Gavel, Bragi''s
    Harp, Toxic Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.35
    Genji's Guard:
      total: 0.66
      efficiency: 0.66
      win: 0.88
      pick: 0.11
      fit: 0.22
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.59
      pick: 0.16
      fit: 0.22
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.5
    Rod of Asclepius:
      total: 0.55
      efficiency: 0.57
      win: 0.72
      pick: 0.1
      fit: 0.16
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Rod of Asclepius
  flex_slots:
  - Transcendence
  - Book of Thoth
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Rod of Tahuti, Rod
    of Asclepius, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass,
    Spear of Desolation, Spear of the Magus, Shield Splitter, Shifter''s Shield, Runeforged
    Hammer, Soul Gem, Helm of Radiance, Obsidian Shard, Berserker''s Shield, Eye of
    the Storm, Hydra''s Lament, Heartseeker, Erosion, Eye of Providence, Shield of
    the Phoenix, Doom Orb, Jade Scepter, Draconic Scale, Death Metal, Stone of Binding,
    Wish-Granting Pearl, Avenging Blade, Chronos'' Pendant, The World Stone, Titan''s
    Bane, The Crusher, Ancient Signet, Magi''s Cloak, Triton''s Conch, Dreamer''s
    Idol, Helm of Darkness, Screeching Gargoyle, Daybreak Gavel.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.18
    Genji's Guard:
      total: 0.66
      efficiency: 0.66
      win: 0.88
      pick: 0.11
      fit: 0.22
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.42
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.18
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.56
      pick: 0.0
      fit: 0.34
    Rod of Asclepius:
      total: 0.57
      efficiency: 0.57
      win: 0.72
      pick: 0.1
      fit: 0.31
  community_ordered:
  - Genji's Guard
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: model
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Kinetic
    Cuirass, Shield Splitter, Shifter''s Shield, Genji''s Guard, Runeforged Hammer,
    Eye of the Storm, Berserker''s Shield, Erosion, Eye of Providence, Draconic Scale,
    Shield of the Phoenix, Hydra''s Lament, Stone of Binding, Gluttonous Grimoire,
    Avenging Blade, Helm of Radiance, Magi''s Cloak, Midgardian Mail, Mantle Of Discord,
    Screeching Gargoyle, Hide of the Nemean Lion, Heartseeker, Leviathan''s Hide,
    Spear of Desolation, Void Shield, Stampede, Daybreak Gavel, Ancile, Rod of Asclepius,
    Oni Hunter''s Garb, Prophetic Cloak, Soul Gem, Void Stone, Spectral Armor, Spear
    of the Magus, Arondight, Xibalban Effigy.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.66
    Shield Splitter:
      total: 0.54
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.47
      efficiency: 0.61
      win: 0.38
      pick: 0.22
      fit: 0.5
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.56
      pick: 0.14
      fit: 0.56
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
---
