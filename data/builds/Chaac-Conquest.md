---
type: smite-build
god: Chaac
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fulmination
  aspect_pick_rate: 0.09
  aspect_win_rate: 0.5
  slot_order:
  - name: Daybreak Gavel
    pick_rate: 0.4
    win_rate: 0.51
    alternates:
    - name: Heartwood Charm
      pick_rate: 0.29
      win_rate: 0.61
    - name: Chronos' Pendant
      pick_rate: 0.06
      win_rate: 0.33
  - name: Chronos' Pendant
    pick_rate: 0.24
    win_rate: 0.62
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.59
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.43
  - name: Rod of Asclepius
    pick_rate: 0.2
    win_rate: 0.58
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.36
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.7
  - name: Breastplate of Valor
    pick_rate: 0.15
    win_rate: 0.41
    alternates:
    - name: Rod of Asclepius
      pick_rate: 0.09
      win_rate: 0.54
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.58
  - name: Rod of Tahuti
    pick_rate: 0.16
    win_rate: 0.62
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.43
    - name: Draconic Scale
      pick_rate: 0.05
      win_rate: 0.5
  - name: Hide of the Nemean Lion
    pick_rate: 0.08
    win_rate: 0.67
    alternates:
    - name: Shield
      pick_rate: 0.07
      win_rate: 0.8
    - name: Evil Eye
      pick_rate: 0.05
      win_rate: 0.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.24
    win_rate: 0.53
  - name: Blood-soaked Shroud
    pick_rate: 0.19
    win_rate: 0.55
  - name: Bluestone Pendant
    pick_rate: 0.18
    win_rate: 0.56
  source_url: https://smitebrain.com/gods/chaac/
  last_verified: '2026-09-16'
  god_win_rate: 0.5555555555555556
  god_matches_won: 85
  god_matches_played: 153
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-16'
  god_matches_analyzed: 9166
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Hide of the Nemean Lion
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Freya''s Tears, Kinetic Cuirass, Gluttonous
    Grimoire, Shield Splitter, Spear of Desolation, Runeforged Hammer, Spear of the
    Magus, Helm of Radiance, Soul Gem, Berserker''s Shield, Obsidian Shard, Eye of
    the Storm, Erosion, Eye of Providence, Hydra''s Lament, Heartseeker, Shield of
    the Phoenix, Stone of Binding, Magi''s Cloak, Avenging Blade, Jade Scepter, Doom
    Orb, Screeching Gargoyle, Wish-Granting Pearl, Mantle Of Discord, Helm of Darkness,
    Midgardian Mail, Titan''s Bane, Death Metal, The Crusher, The World Stone, Draconic
    Scale, Genji''s Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.55
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.52
      win: 0.67
      pick: 0.25
      fit: 0.29
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.58
      pick: 0.13
      fit: 0.4
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.59
      pick: 0.15
      fit: 0.45
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Hide of the Nemean Lion
  - Freya's Tears
  - Shifter's Shield
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Hide of the Nemean Lion
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Hide of the Nemean Lion
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Amanita Charm, Freya''s Tears, Gluttonous Grimoire, Kinetic Cuirass,
    Spear of Desolation, Shield Splitter, Spear of the Magus, Hydra''s Lament, Runeforged
    Hammer, Helm of Radiance, Soul Gem, Obsidian Shard, Heartseeker, Berserker''s
    Shield, Eye of the Storm, Wish-Granting Pearl, Doom Orb, Ancient Signet, The World
    Stone, Shield of the Phoenix, Erosion, Death Metal, Jade Scepter, Stone of Binding,
    Eye of Providence, Avenging Blade, Screeching Gargoyle, Magi''s Cloak, Titan''s
    Bane, Helm of Darkness, Triton''s Conch, The Crusher, Oni Hunter''s Garb, Genji''s
    Guard, Draconic Scale.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.45
    Hydra's Lament:
      total: 0.52
      efficiency: 0.54
      win: 0.58
      pick: 0.0
      fit: 0.44
    Hide of the Nemean Lion:
      total: 0.53
      efficiency: 0.52
      win: 0.67
      pick: 0.25
      fit: 0.23
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.58
      pick: 0.13
      fit: 0.35
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.62
      pick: 0.35
      fit: 0.36
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Hide of the Nemean Lion
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
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
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, Amanita Charm, Freya''s Tears, Gluttonous Grimoire, Spear
    of Desolation, Kinetic Cuirass, Soul Gem, Spear of the Magus, Obsidian Shard,
    Shield Splitter, Runeforged Hammer, Helm of Radiance, Berserker''s Shield, Hydra''s
    Lament, Heartseeker, Shield of the Phoenix, Eye of the Storm, Erosion, Doom Orb,
    Eye of Providence, Screeching Gargoyle, Stone of Binding, The World Stone, Titan''s
    Bane, The Crusher, Dreamer''s Idol, Magi''s Cloak, Jade Scepter, The Reaper, Wish-Granting
    Pearl, Avenging Blade, Mantle Of Discord, Midgardian Mail, Ancient Signet, Genji''s
    Guard, Draconic Scale.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.14
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.48
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.14
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.58
      pick: 0.13
      fit: 0.41
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.62
      pick: 0.35
      fit: 0.34
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Rod of Tahuti
  - Rod of Asclepius
  - Amanita Charm
  flex_slots:
  - Hide of the Nemean Lion
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Soul Gem, Shield of the Phoenix, Gluttonous
    Grimoire, Kinetic Cuirass, Freya''s Tears, Ethereal Staff, The Reaper, Runeforged
    Hammer, Spear of Desolation, Spear of the Magus, Shield Splitter, Berserker''s
    Shield, Lifebinder, Obsidian Shard, Helm of Radiance, Eye of the Storm, Yogi''s
    Necklace, Sphere of Negation, Hydra''s Lament, Erosion, Heartseeker, Phoenix Feather,
    Eye of Providence, Chandra''s Grace, Avenging Blade, Blood-Bound Book, Jade Scepter,
    Wish-Granting Pearl, Stone of Binding, Doom Orb, Glorious Pridwen, Midgardian
    Mail, Titan''s Bane, Draconic Scale, Genji''s Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.53
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.52
      win: 0.67
      pick: 0.25
      fit: 0.3
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.62
      pick: 0.35
      fit: 0.31
    Rod of Asclepius:
      total: 0.57
      efficiency: 0.57
      win: 0.58
      pick: 0.31
      fit: 0.62
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.73
  community_ordered:
  - Hide of the Nemean Lion
  - Rod of Tahuti
  - Rod of Asclepius
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire, Stone of
    Binding, Freya''s Tears, Spear of Desolation, Spear of the Magus, Avenging Blade,
    Kinetic Cuirass, Screeching Gargoyle, Soul Gem, Obsidian Shard, Void Shield, Heartseeker,
    Void Stone, Shield Splitter, Runeforged Hammer, Helm of Radiance, Berserker''s
    Shield, Doom Orb, Titan''s Bane, The Crusher, The World Stone, Eye of the Storm,
    Hydra''s Lament, Dreamer''s Idol, Erosion, The Reaper, Eye of Providence, Shield
    of the Phoenix, Magi''s Cloak, Jade Scepter, Wish-Granting Pearl, Mantle Of Discord,
    Midgardian Mail, Draconic Scale, Genji''s Guard.'
  slot_scores:
    Stone of Binding:
      total: 0.54
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.67
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.58
      pick: 0.13
      fit: 0.34
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.62
      pick: 0.35
      fit: 0.4
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Gluttonous Grimoire
  - Rod of Tahuti
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
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Jotunn''s Revenge, Gluttonous Grimoire, Nimble
    Ring, Amanita Charm, Freya''s Tears, Soul Gem, Kinetic Cuirass, Golden Blade,
    Riptalon, Spear of the Magus, Spear of Desolation, Silverbranch Bow, Helm of Radiance,
    Runeforged Hammer, Tyrfing, Shield Splitter, Obsidian Shard, Lernaean Bow, Pharaoh''s
    Curse, Toxic Blade, Shogun''s Ofuda, The Reaper, Hydra''s Lament, Stone of Binding,
    Erosion, Tekko-Kagi, Bragi''s Harp, Shield of the Phoenix, Eye of Providence,
    Eye of the Storm, Bracer of The Abyss, Heartseeker, Magi''s Cloak, Screeching
    Gargoyle, Genji''s Guard, Draconic Scale.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.45
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.33
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.6
      win: 0.58
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.62
      pick: 0.35
      fit: 0.21
  community_ordered:
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Jotunn's Revenge
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Chronos' Pendant
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Freya''s Tears,
    Amanita Charm, Spear of Desolation, Kinetic Cuirass, Soul Gem, Shield of the Phoenix,
    Hydra''s Lament, Screeching Gargoyle, Gluttonous Grimoire, Berserker''s Shield,
    Shield Splitter, Spear of the Magus, Runeforged Hammer, Helm of Radiance, Prophetic
    Cloak, Erosion, Obsidian Shard, Eye of Providence, Stone of Binding, Gladiator''s
    Shield, Genji''s Guard, Eye of the Storm, Arondight, Gem of Focus, Magi''s Cloak,
    Heartseeker, Eye of Erebus, Mantle Of Discord, Midgardian Mail, Pendulum Blade,
    Glorious Pridwen, Jade Scepter, Chandra''s Grace, Draconic Scale.'
  slot_scores:
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.55
      win: 0.62
      pick: 0.33
      fit: 0.37
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.51
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.58
      pick: 0.13
      fit: 0.58
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.62
      pick: 0.35
      fit: 0.22
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Chronos' Pendant
  - Freya's Tears
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
    Tears, Gluttonous Grimoire, Genji''s Guard, Shield Splitter, Spear of Desolation,
    Runeforged Hammer, Spear of the Magus, Helm of Radiance, Soul Gem, Berserker''s
    Shield, Obsidian Shard, Eye of the Storm, Erosion, Eye of Providence, Hydra''s
    Lament, Draconic Scale, Heartseeker, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Avenging Blade, Jade Scepter, Doom Orb, Screeching Gargoyle, Wish-Granting
    Pearl, Mantle Of Discord, Helm of Darkness, Midgardian Mail, Titan''s Bane, Death
    Metal, The Crusher, The World Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.47
      efficiency: 0.66
      win: 0.43
      pick: 0.12
      fit: 0.24
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.58
      pick: 0.13
      fit: 0.4
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.62
      pick: 0.35
      fit: 0.3
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
---
