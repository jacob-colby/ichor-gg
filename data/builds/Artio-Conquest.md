---
type: smite-build
god: Artio
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Denmother
  aspect_pick_rate: 0.65
  aspect_win_rate: 0.57
  slot_order:
  - name: Heartwood Charm
    pick_rate: 0.24
    win_rate: 0.61
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.15
      win_rate: 0.86
    - name: Lifebinder
      pick_rate: 0.11
      win_rate: 0.5
  - name: Genji's Guard
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Heartwood Charm
      pick_rate: 0.19
      win_rate: 0.5
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.86
  - name: Breastplate of Valor
    pick_rate: 0.13
    win_rate: 0.75
    alternates:
    - name: Genji's Guard
      pick_rate: 0.2
      win_rate: 0.44
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.63
  - name: Freya's Tears
    pick_rate: 0.1
    win_rate: 0.67
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.75
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.63
  - name: Shell of Rebuke
    pick_rate: 0.14
    win_rate: 0.6
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.6
    - name: Rod of Asclepius
      pick_rate: 0.06
      win_rate: 1.0
  - name: Medallion
    pick_rate: 0.1
    win_rate: 0.75
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 1.0
    - name: Cleric's Cloak
      pick_rate: 0.05
      win_rate: 0.0
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.17
    win_rate: 0.25
  - name: Sands Of Time
    pick_rate: 0.16
    win_rate: 0.6
  - name: Bumba's Hammer
    pick_rate: 0.14
    win_rate: 0.69
  source_url: https://smitebrain.com/gods/artio/
  last_verified: '2026-09-10'
  god_win_rate: 0.574468085106383
  god_matches_won: 54
  god_matches_played: 94
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-10'
  god_matches_analyzed: 1308
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Daybreak Gavel
  - Freya's Tears
  - Rod of Asclepius
  flex_slots:
  - Jotunn's Revenge
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Asclepius, Daybreak Gavel, Rod of Tahuti, Amanita Charm, Jotunn''s
    Revenge, Kinetic Cuirass, Shield Splitter, Shifter''s Shield, Runeforged Hammer,
    Eye of the Storm, Berserker''s Shield, Erosion, Eye of Providence, Draconic Scale,
    Shield of the Phoenix, Hydra''s Lament, Stone of Binding, Gluttonous Grimoire,
    Avenging Blade, Helm of Radiance, Magi''s Cloak, Midgardian Mail, Mantle Of Discord,
    Screeching Gargoyle, Heartseeker, Leviathan''s Hide, Spear of Desolation, Void
    Shield, Stampede, Ancile, Genji''s Guard, Oni Hunter''s Garb, Prophetic Cloak,
    Soul Gem, Void Stone, Spectral Armor, Spear of the Magus, Arondight, Xibalban
    Effigy.'
  slot_scores:
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.65
      win: 0.75
      pick: 0.2
      fit: 0.31
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.66
    Daybreak Gavel:
      total: 0.63
      efficiency: 0.59
      win: 0.86
      pick: 0.15
      fit: 0.17
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.17
      fit: 0.5
    Rod of Asclepius:
      total: 0.69
      efficiency: 0.57
      win: 1.0
      pick: 0.13
      fit: 0.23
  community_ordered:
  - Breastplate of Valor
  - Daybreak Gavel
  - Freya's Tears
  - Rod of Asclepius
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Daybreak Gavel
  - Freya's Tears
  - Amanita Charm
  - Rod of Asclepius
  flex_slots:
  - Freya's Tears
  - Jotunn's Revenge
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Asclepius, Daybreak Gavel, Amanita Charm, Rod of Tahuti, Jotunn''s
    Revenge, Shield of the Phoenix, Kinetic Cuirass, Runeforged Hammer, Shield Splitter,
    Shifter''s Shield, Soul Gem, Eye of the Storm, Berserker''s Shield, Erosion, Ethereal
    Staff, Eye of Providence, The Reaper, Draconic Scale, Yogi''s Necklace, Phoenix
    Feather, Hydra''s Lament, Gluttonous Grimoire, Avenging Blade, Chandra''s Grace,
    Glorious Pridwen, Stone of Binding, Midgardian Mail, Helm of Radiance, Magi''s
    Cloak, Leviathan''s Hide, Sphere of Negation, Void Shield, Stampede, Ancile, Screeching
    Gargoyle, Oni Hunter''s Garb, Heartseeker, Genji''s Guard, Lifebinder.'
  slot_scores:
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.65
      win: 0.75
      pick: 0.2
      fit: 0.28
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.39
    Daybreak Gavel:
      total: 0.63
      efficiency: 0.59
      win: 0.86
      pick: 0.15
      fit: 0.21
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.17
      fit: 0.46
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.86
    Rod of Asclepius:
      total: 0.74
      efficiency: 0.57
      win: 1.0
      pick: 0.13
      fit: 0.57
  community_ordered:
  - Breastplate of Valor
  - Daybreak Gavel
  - Freya's Tears
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Daybreak Gavel
  - Freya's Tears
  - Rod of Tahuti
  - Rod of Asclepius
  flex_slots:
  - Jotunn's Revenge
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Asclepius, Rod of Tahuti, Daybreak Gavel, Jotunn''s Revenge,
    Amanita Charm, Stone of Binding, Gluttonous Grimoire, Avenging Blade, Kinetic
    Cuirass, Screeching Gargoyle, Spear of Desolation, Heartseeker, Spear of the Magus,
    Void Shield, Soul Gem, Void Stone, Obsidian Shard, Shield Splitter, Runeforged
    Hammer, Shifter''s Shield, Titan''s Bane, The Crusher, Berserker''s Shield, Eye
    of the Storm, The Reaper, Hydra''s Lament, Erosion, Eye of Providence, Shield
    of the Phoenix, Doom Orb, Draconic Scale, Helm of Radiance, The World Stone, Pendulum
    Blade, Dreamer''s Idol, Avatar''s Parashu, Magi''s Cloak, Midgardian Mail, Mantle
    Of Discord, Genji''s Guard.'
  slot_scores:
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.75
      pick: 0.2
      fit: 0.22
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.56
    Daybreak Gavel:
      total: 0.62
      efficiency: 0.59
      win: 0.86
      pick: 0.15
      fit: 0.12
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.17
      fit: 0.36
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.35
    Rod of Asclepius:
      total: 0.68
      efficiency: 0.57
      win: 1.0
      pick: 0.13
      fit: 0.16
  community_ordered:
  - Breastplate of Valor
  - Daybreak Gavel
  - Freya's Tears
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Breastplate of Valor
  - Daybreak Gavel
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
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Asclepius, Daybreak Gavel, Rod of Tahuti, Berserker''s Shield,
    Jotunn''s Revenge, Amanita Charm, Nimble Ring, Kinetic Cuirass, Golden Blade,
    Gluttonous Grimoire, Tyrfing, Shifter''s Shield, Runeforged Hammer, Soul Gem,
    Shield Splitter, Pharaoh''s Curse, Riptalon, Lernaean Bow, Silverbranch Bow, Shogun''s
    Ofuda, Toxic Blade, Hydra''s Lament, Erosion, Helm of Radiance, Eye of the Storm,
    Shield of the Phoenix, Eye of Providence, Stone of Binding, Draconic Scale, Magi''s
    Cloak, The Reaper, Bragi''s Harp, Tekko-Kagi, Screeching Gargoyle, Spear of Desolation,
    Spear of the Magus, Avenging Blade, Midgardian Mail, Mantle Of Discord, Genji''s
    Guard.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.55
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.65
      win: 0.75
      pick: 0.2
      fit: 0.19
    Daybreak Gavel:
      total: 0.62
      efficiency: 0.59
      win: 0.86
      pick: 0.15
      fit: 0.11
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.3
    Rod of Asclepius:
      total: 0.68
      efficiency: 0.57
      win: 1.0
      pick: 0.13
      fit: 0.14
  community_ordered:
  - Breastplate of Valor
  - Daybreak Gavel
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Daybreak Gavel
  - Freya's Tears
  - Rod of Asclepius
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
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
    + fit + win/pick). Underrated for this god: Rod of Asclepius, Daybreak Gavel,
    Jotunn''s Revenge, Rod of Tahuti, Amanita Charm, Shield of the Phoenix, Kinetic
    Cuirass, Spear of Desolation, Hydra''s Lament, Soul Gem, Screeching Gargoyle,
    Genji''s Guard, Shifter''s Shield, Chronos'' Pendant, Berserker''s Shield, Shield
    Splitter, Prophetic Cloak, Runeforged Hammer, Gluttonous Grimoire, Helm of Radiance,
    Gladiator''s Shield, Erosion, Eye of Providence, Arondight, Gem of Focus, Draconic
    Scale, Eye of the Storm, Stone of Binding, Eye of Erebus, Spear of the Magus,
    Magi''s Cloak, Chandra''s Grace, Midgardian Mail, Glorious Pridwen, Obsidian Shard,
    Mantle Of Discord, Jade Scepter, Wish-Granting Pearl, Avenging Blade.'
  slot_scores:
    Breastplate of Valor:
      total: 0.65
      efficiency: 0.65
      win: 0.75
      pick: 0.2
      fit: 0.48
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.53
    Daybreak Gavel:
      total: 0.62
      efficiency: 0.59
      win: 0.86
      pick: 0.15
      fit: 0.13
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.67
      pick: 0.17
      fit: 0.63
    Rod of Asclepius:
      total: 0.69
      efficiency: 0.57
      win: 1.0
      pick: 0.13
      fit: 0.23
  community_ordered:
  - Breastplate of Valor
  - Daybreak Gavel
  - Freya's Tears
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Daybreak Gavel
  - Freya's Tears
  - Rod of Asclepius
  flex_slots:
  - Freya's Tears
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    win/pick). Underrated for this god: Daybreak Gavel, Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged
    Hammer, Golden Blade, Eye of the Storm, Gluttonous Grimoire, Shifter''s Shield,
    Hydra''s Lament, Heartseeker, Lernaean Bow, Tekko-Kagi, Spear of Desolation, Tyrfing,
    Avenging Blade, Spear of the Magus, Erosion, Titan''s Bane, Eye of Providence,
    Shield of the Phoenix, Soul Gem, The Crusher, Helm of Radiance, Draconic Scale,
    Obsidian Shard, Stone of Binding, Pharaoh''s Curse, The Reaper, Nimble Ring, Silverbranch
    Bow, Magi''s Cloak, Shogun''s Ofuda, Screeching Gargoyle, Bragi''s Harp, Toxic
    Blade, Genji''s Guard.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.35
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.75
      pick: 0.2
      fit: 0.22
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.47
    Daybreak Gavel:
      total: 0.62
      efficiency: 0.59
      win: 0.86
      pick: 0.15
      fit: 0.12
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.17
      fit: 0.36
    Rod of Asclepius:
      total: 0.68
      efficiency: 0.57
      win: 1.0
      pick: 0.13
      fit: 0.16
  community_ordered:
  - Breastplate of Valor
  - Daybreak Gavel
  - Freya's Tears
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Daybreak Gavel
  - Freya's Tears
  - Rod of Asclepius
  flex_slots:
  - Freya's Tears
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Asclepius, Rod of Tahuti, Daybreak
    Gavel, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass,
    Spear of Desolation, Spear of the Magus, Shield Splitter, Runeforged Hammer, Soul
    Gem, Helm of Radiance, Obsidian Shard, Shifter''s Shield, Berserker''s Shield,
    Eye of the Storm, Hydra''s Lament, Heartseeker, Erosion, Eye of Providence, Shield
    of the Phoenix, Doom Orb, Jade Scepter, Draconic Scale, Death Metal, Stone of
    Binding, Wish-Granting Pearl, Avenging Blade, Chronos'' Pendant, The World Stone,
    Titan''s Bane, The Crusher, Ancient Signet, Magi''s Cloak, Triton''s Conch, Dreamer''s
    Idol, Helm of Darkness, Screeching Gargoyle, Genji''s Guard.'
  slot_scores:
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.75
      pick: 0.2
      fit: 0.22
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.5
    Daybreak Gavel:
      total: 0.62
      efficiency: 0.59
      win: 0.86
      pick: 0.15
      fit: 0.12
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.17
      fit: 0.36
    Rod of Asclepius:
      total: 0.7
      efficiency: 0.57
      win: 1.0
      pick: 0.13
      fit: 0.31
  community_ordered:
  - Breastplate of Valor
  - Daybreak Gavel
  - Freya's Tears
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
    Screeching Gargoyle, Heartseeker, Leviathan''s Hide, Spear of Desolation, Void
    Shield, Stampede, Daybreak Gavel, Ancile, Rod of Asclepius, Oni Hunter''s Garb,
    Prophetic Cloak, Soul Gem, Void Stone, Spectral Armor, Spear of the Magus, Arondight,
    Xibalban Effigy.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.66
    Shield Splitter:
      total: 0.56
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.17
      fit: 0.5
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.56
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Freya's Tears
  starter: *id001
---
