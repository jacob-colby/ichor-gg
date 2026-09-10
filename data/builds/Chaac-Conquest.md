---
type: smite-build
god: Chaac
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fulmination
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.0
  slot_order:
  - name: Heartwood Charm
    pick_rate: 0.83
    win_rate: 0.66
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.06
      win_rate: 0.5
    - name: Blood-Bound Book
      pick_rate: 0.06
      win_rate: 0.5
  - name: Chronos' Pendant
    pick_rate: 0.69
    win_rate: 0.71
    alternates:
    - name: Chandra's Grace
      pick_rate: 0.06
      win_rate: 0.5
    - name: Breastplate of Valor
      pick_rate: 0.06
      win_rate: 1.0
  - name: Rod of Asclepius
    pick_rate: 0.57
    win_rate: 0.65
    alternates:
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.5
    - name: Chandra's Grace
      pick_rate: 0.06
      win_rate: 0.5
  - name: Breastplate of Valor
    pick_rate: 0.41
    win_rate: 0.5
    alternates:
    - name: Rod of Asclepius
      pick_rate: 0.15
      win_rate: 1.0
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.5
  - name: Rod of Tahuti
    pick_rate: 0.44
    win_rate: 0.71
    alternates:
    - name: Evil Eye
      pick_rate: 0.09
      win_rate: 0.33
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.5
  - name: Stygian Anchor
    pick_rate: 0.18
    win_rate: 1.0
    alternates:
    - name: Shield
      pick_rate: 0.12
      win_rate: 1.0
    - name: Ethereal Staff
      pick_rate: 0.12
      win_rate: 0.5
  community_starters:
  - name: Blood-soaked Shroud
    pick_rate: 0.51
    win_rate: 0.67
  - name: Vampiric Shroud
    pick_rate: 0.17
    win_rate: 0.67
  - name: Bluestone Brooch
    pick_rate: 0.09
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/chaac/
  last_verified: '2026-09-10'
  god_win_rate: 0.6285714285714286
  god_matches_won: 22
  god_matches_played: 35
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
  - Chronos' Pendant
  - Rod of Asclepius
  - Breastplate of Valor
  - Stygian Anchor
  - Jotunn's Revenge
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Freya''s Tears, Kinetic Cuirass, Genji''s
    Guard, Gluttonous Grimoire, Shield Splitter, Shifter''s Shield, Spear of Desolation,
    Runeforged Hammer, Spear of the Magus, Helm of Radiance, Soul Gem, Berserker''s
    Shield, Obsidian Shard, Eye of the Storm, Erosion, Eye of Providence, Hydra''s
    Lament, Draconic Scale, Heartseeker, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Avenging Blade, Jade Scepter, Doom Orb, Screeching Gargoyle, Wish-Granting
    Pearl, Daybreak Gavel, Mantle Of Discord, Helm of Darkness, Midgardian Mail, Titan''s
    Bane, Death Metal, The Crusher, The World Stone, Hide of the Nemean Lion.'
  slot_scores:
    Chronos' Pendant:
      total: 0.59
      efficiency: 0.55
      win: 0.71
      pick: 0.94
      fit: 0.24
    Rod of Asclepius:
      total: 0.58
      efficiency: 0.57
      win: 0.65
      pick: 0.89
      fit: 0.28
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.68
      fit: 0.24
    Stygian Anchor:
      total: 0.68
      efficiency: 0.45
      win: 1.0
      pick: 0.55
      fit: 0.32
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.4
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.71
      pick: 0.95
      fit: 0.3
  community_ordered:
  - Chronos' Pendant
  - Rod of Asclepius
  - Breastplate of Valor
  - Stygian Anchor
  - Rod of Tahuti
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: mana-stack
  slot_order:
  - Chronos' Pendant
  - Rod of Asclepius
  - Breastplate of Valor
  - Stygian Anchor
  - Jotunn's Revenge
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Amanita Charm, Genji''s Guard, Freya''s Tears, Gluttonous Grimoire, Kinetic
    Cuirass, Spear of Desolation, Shield Splitter, Spear of the Magus, Hydra''s Lament,
    Runeforged Hammer, Helm of Radiance, Soul Gem, Obsidian Shard, Heartseeker, Shifter''s
    Shield, Berserker''s Shield, Eye of the Storm, Wish-Granting Pearl, Doom Orb,
    Ancient Signet, The World Stone, Shield of the Phoenix, Erosion, Death Metal,
    Jade Scepter, Stone of Binding, Eye of Providence, Avenging Blade, Draconic Scale,
    Screeching Gargoyle, Daybreak Gavel, Magi''s Cloak, Titan''s Bane, Helm of Darkness,
    Triton''s Conch, The Crusher, Oni Hunter''s Garb.'
  slot_scores:
    Chronos' Pendant:
      total: 0.6
      efficiency: 0.55
      win: 0.71
      pick: 0.94
      fit: 0.27
    Rod of Asclepius:
      total: 0.58
      efficiency: 0.57
      win: 0.65
      pick: 0.89
      fit: 0.29
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.68
      fit: 0.29
    Stygian Anchor:
      total: 0.67
      efficiency: 0.45
      win: 1.0
      pick: 0.55
      fit: 0.26
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.86
      win: 0.71
      pick: 0.95
      fit: 0.36
  community_ordered:
  - Chronos' Pendant
  - Rod of Asclepius
  - Breastplate of Valor
  - Stygian Anchor
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Chronos' Pendant
  - Rod of Asclepius
  - Breastplate of Valor
  - Stygian Anchor
  - Jotunn's Revenge
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, Amanita Charm, Freya''s Tears, Genji''s Guard, Gluttonous
    Grimoire, Spear of Desolation, Kinetic Cuirass, Soul Gem, Spear of the Magus,
    Obsidian Shard, Shield Splitter, Shifter''s Shield, Runeforged Hammer, Helm of
    Radiance, Berserker''s Shield, Hydra''s Lament, Heartseeker, Shield of the Phoenix,
    Eye of the Storm, Erosion, Doom Orb, Eye of Providence, Screeching Gargoyle, Stone
    of Binding, Draconic Scale, The World Stone, Titan''s Bane, The Crusher, Dreamer''s
    Idol, Magi''s Cloak, Daybreak Gavel, Jade Scepter, The Reaper, Wish-Granting Pearl,
    Avenging Blade, Mantle Of Discord, Midgardian Mail, Ancient Signet.'
  slot_scores:
    Chronos' Pendant:
      total: 0.6
      efficiency: 0.55
      win: 0.71
      pick: 0.94
      fit: 0.27
    Rod of Asclepius:
      total: 0.57
      efficiency: 0.57
      win: 0.65
      pick: 0.89
      fit: 0.25
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.68
      fit: 0.27
    Stygian Anchor:
      total: 0.68
      efficiency: 0.45
      win: 1.0
      pick: 0.55
      fit: 0.27
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.72
      efficiency: 0.86
      win: 0.71
      pick: 0.95
      fit: 0.34
  community_ordered:
  - Chronos' Pendant
  - Rod of Asclepius
  - Breastplate of Valor
  - Stygian Anchor
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Chronos' Pendant
  - Jotunn's Revenge
  - Rod of Asclepius
  - Stygian Anchor
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Jotunn's Revenge
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Soul Gem, Shield of the Phoenix, Gluttonous
    Grimoire, Kinetic Cuirass, Freya''s Tears, Genji''s Guard, The Reaper, Runeforged
    Hammer, Spear of Desolation, Spear of the Magus, Shield Splitter, Shifter''s Shield,
    Berserker''s Shield, Lifebinder, Obsidian Shard, Helm of Radiance, Eye of the
    Storm, Yogi''s Necklace, Sphere of Negation, Chandra''s Grace, Hydra''s Lament,
    Erosion, Heartseeker, Phoenix Feather, Eye of Providence, Blood-Bound Book, Draconic
    Scale, Avenging Blade, Jade Scepter, Wish-Granting Pearl, Daybreak Gavel, Stone
    of Binding, Doom Orb, Glorious Pridwen, Midgardian Mail, Titan''s Bane.'
  slot_scores:
    Chronos' Pendant:
      total: 0.6
      efficiency: 0.55
      win: 0.71
      pick: 0.94
      fit: 0.24
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.42
    Rod of Asclepius:
      total: 0.63
      efficiency: 0.57
      win: 0.65
      pick: 0.89
      fit: 0.62
    Stygian Anchor:
      total: 0.67
      efficiency: 0.45
      win: 1.0
      pick: 0.55
      fit: 0.26
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.71
      pick: 0.95
      fit: 0.31
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.73
  community_ordered:
  - Chronos' Pendant
  - Rod of Asclepius
  - Stygian Anchor
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Chronos' Pendant
  - Rod of Asclepius
  - Breastplate of Valor
  - Stygian Anchor
  - Jotunn's Revenge
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Breastplate of Valor
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
    for this god: Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire, Stone of
    Binding, Spear of Desolation, Spear of the Magus, Freya''s Tears, Avenging Blade,
    Kinetic Cuirass, Screeching Gargoyle, Genji''s Guard, Soul Gem, Obsidian Shard,
    Void Shield, Heartseeker, Void Stone, Shield Splitter, Runeforged Hammer, Shifter''s
    Shield, Helm of Radiance, Berserker''s Shield, Doom Orb, Titan''s Bane, The Crusher,
    The World Stone, Eye of the Storm, Hydra''s Lament, Dreamer''s Idol, Erosion,
    The Reaper, Eye of Providence, Shield of the Phoenix, Draconic Scale, Magi''s
    Cloak, Daybreak Gavel, Jade Scepter, Wish-Granting Pearl, Mantle Of Discord, Midgardian
    Mail.'
  slot_scores:
    Chronos' Pendant:
      total: 0.59
      efficiency: 0.55
      win: 0.71
      pick: 0.94
      fit: 0.2
    Rod of Asclepius:
      total: 0.57
      efficiency: 0.57
      win: 0.65
      pick: 0.89
      fit: 0.24
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.68
      fit: 0.21
    Stygian Anchor:
      total: 0.68
      efficiency: 0.45
      win: 1.0
      pick: 0.55
      fit: 0.27
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.73
      efficiency: 0.86
      win: 0.71
      pick: 0.95
      fit: 0.4
  community_ordered:
  - Chronos' Pendant
  - Rod of Asclepius
  - Breastplate of Valor
  - Stygian Anchor
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Chronos' Pendant
  - Berserker's Shield
  - Stygian Anchor
  - Rod of Tahuti
  - Nimble Ring
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
    this god: Berserker''s Shield, Jotunn''s Revenge, Gluttonous Grimoire, Nimble
    Ring, Amanita Charm, Soul Gem, Genji''s Guard, Freya''s Tears, Kinetic Cuirass,
    Golden Blade, Riptalon, Spear of the Magus, Spear of Desolation, Silverbranch
    Bow, Helm of Radiance, Shifter''s Shield, Runeforged Hammer, Tyrfing, Shield Splitter,
    Obsidian Shard, Lernaean Bow, Pharaoh''s Curse, Toxic Blade, Shogun''s Ofuda,
    The Reaper, Hydra''s Lament, Stone of Binding, Erosion, Tekko-Kagi, Bragi''s Harp,
    Shield of the Phoenix, Eye of Providence, Eye of the Storm, Daybreak Gavel, Bracer
    of The Abyss, Heartseeker, Draconic Scale, Magi''s Cloak, Screeching Gargoyle.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.45
    Chronos' Pendant:
      total: 0.58
      efficiency: 0.55
      win: 0.71
      pick: 0.94
      fit: 0.16
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.37
    Stygian Anchor:
      total: 0.67
      efficiency: 0.45
      win: 1.0
      pick: 0.55
      fit: 0.22
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.71
      pick: 0.95
      fit: 0.21
    Nimble Ring:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.33
  community_ordered:
  - Chronos' Pendant
  - Stygian Anchor
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Rod of Asclepius
  - Breastplate of Valor
  - Stygian Anchor
  - Jotunn's Revenge
  - Rod of Tahuti
  flex_slots:
  - Breastplate of Valor
  - Jotunn's Revenge
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Freya''s Tears,
    Genji''s Guard, Amanita Charm, Spear of Desolation, Kinetic Cuirass, Soul Gem,
    Shield of the Phoenix, Hydra''s Lament, Screeching Gargoyle, Gluttonous Grimoire,
    Shifter''s Shield, Berserker''s Shield, Shield Splitter, Spear of the Magus, Runeforged
    Hammer, Helm of Radiance, Prophetic Cloak, Erosion, Obsidian Shard, Eye of Providence,
    Stone of Binding, Draconic Scale, Gladiator''s Shield, Eye of the Storm, Arondight,
    Gem of Focus, Magi''s Cloak, Daybreak Gavel, Heartseeker, Eye of Erebus, Mantle
    Of Discord, Midgardian Mail, Pendulum Blade, Chandra''s Grace, Hide of the Nemean
    Lion, Glorious Pridwen, Jade Scepter.'
  slot_scores:
    Chronos' Pendant:
      total: 0.61
      efficiency: 0.55
      win: 0.71
      pick: 0.94
      fit: 0.37
    Rod of Asclepius:
      total: 0.57
      efficiency: 0.57
      win: 0.65
      pick: 0.89
      fit: 0.2
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.68
      fit: 0.43
    Stygian Anchor:
      total: 0.68
      efficiency: 0.45
      win: 1.0
      pick: 0.55
      fit: 0.29
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.7
      efficiency: 0.86
      win: 0.71
      pick: 0.95
      fit: 0.22
  community_ordered:
  - Chronos' Pendant
  - Rod of Asclepius
  - Breastplate of Valor
  - Stygian Anchor
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Genji's Guard
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Freya''s
    Tears, Gluttonous Grimoire, Genji''s Guard, Shield Splitter, Shifter''s Shield,
    Spear of Desolation, Runeforged Hammer, Spear of the Magus, Helm of Radiance,
    Soul Gem, Berserker''s Shield, Obsidian Shard, Eye of the Storm, Erosion, Eye
    of Providence, Hydra''s Lament, Draconic Scale, Heartseeker, Shield of the Phoenix,
    Stone of Binding, Magi''s Cloak, Avenging Blade, Jade Scepter, Doom Orb, Screeching
    Gargoyle, Wish-Granting Pearl, Mantle Of Discord, Helm of Darkness, Midgardian
    Mail, Titan''s Bane, Death Metal, The Crusher, Daybreak Gavel, The World Stone,
    Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.13
      fit: 0.24
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.5
      pick: 0.09
      fit: 0.4
    Rod of Tahuti:
      total: 0.71
      efficiency: 0.86
      win: 0.71
      pick: 0.95
      fit: 0.3
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
---
