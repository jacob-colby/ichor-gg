---
type: smite-build
god: Kuzenbo
mode: Conquest
builds:
- source: community
  aspect: Aspect of Spirits
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.44
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.3
    win_rate: 0.46
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.35
    - name: Mystical Mail
      pick_rate: 0.09
      win_rate: 0.49
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.48
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.12
      win_rate: 0.56
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.51
  - name: Freya's Tears
    pick_rate: 0.14
    win_rate: 0.44
    alternates:
    - name: Genji's Guard
      pick_rate: 0.17
      win_rate: 0.45
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.46
  - name: Hide of the Nemean Lion
    pick_rate: 0.13
    win_rate: 0.43
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.52
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.47
  - name: Shell of Rebuke
    pick_rate: 0.05
    win_rate: 0.69
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.14
      win_rate: 0.6
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.4
  - name: Medal of Defense
    pick_rate: 0.1
    win_rate: 0.44
    alternates:
    - name: Olmec Blue
      pick_rate: 0.06
      win_rate: 0.27
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.44
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.22
    win_rate: 0.37
  - name: Bluestone Brooch
    pick_rate: 0.21
    win_rate: 0.57
  - name: Selflessness
    pick_rate: 0.12
    win_rate: 0.35
  source_url: https://smitebrain.com/gods/kuzenbo/
  last_verified: '2026-11-04'
  god_win_rate: 0.44170096021947874
  god_matches_won: 644
  god_matches_played: 1458
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-03'
  god_matches_analyzed: 14667
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  - Shell of Rebuke
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shell of Rebuke
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Soul Gem, Breastplate of Valor, Erosion, Eye of Providence, Draconic Scale, Oni
    Hunter''s Garb, Shield of the Phoenix, Helm of Darkness, Stone of Binding, Helm
    of Radiance, Midgardian Mail, Magi''s Cloak, Leviathan''s Hide, Mantle Of Discord,
    Spear of Desolation, Screeching Gargoyle, Ancile, Obsidian Shard, Stampede, Void
    Stone, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.48
      pick: 0.2
      fit: 0.34
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.45
      pick: 0.0
      fit: 0.72
    Prophetic Cloak:
      total: 0.5
      efficiency: 0.44
      win: 0.56
      pick: 0.16
      fit: 0.55
    Freya's Tears:
      total: 0.49
      efficiency: 0.58
      win: 0.44
      pick: 0.22
      fit: 0.55
    Shell of Rebuke:
      total: 0.48
      efficiency: 0.29
      win: 0.69
      pick: 0.11
      fit: 0.43
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.62
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Freya's Tears
  - Shell of Rebuke
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Prophetic Cloak
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Soul Gem, Shield of the Phoenix, Kinetic
    Cuirass, Gluttonous Grimoire, Blood-Bound Book, Phoenix Feather, Ethereal Staff,
    Erosion, Yogi''s Necklace, Eye of Providence, Breastplate of Valor, Draconic Scale,
    Oni Hunter''s Garb, Chandra''s Grace, Midgardian Mail, Glorious Pridwen, Bancroft''s
    Talon, Leviathan''s Hide, Helm of Darkness, Regrowth Striders, Helm of Radiance,
    Sphere of Negation, Stone of Binding, Spear of Desolation, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.69
      win: 0.48
      pick: 0.2
      fit: 0.32
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.45
      pick: 0.0
      fit: 0.72
    Prophetic Cloak:
      total: 0.49
      efficiency: 0.44
      win: 0.56
      pick: 0.16
      fit: 0.51
    Freya's Tears:
      total: 0.49
      efficiency: 0.58
      win: 0.44
      pick: 0.22
      fit: 0.51
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.92
    Soul Gem:
      total: 0.52
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.78
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Gluttonous Grimoire
  - Spear of Desolation
  - Obsidian Shard
  - Rod of Tahuti
  flex_slots:
  - Spear of Desolation
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Gluttonous Grimoire, Soul Gem, Amanita Charm, Stone
    of Binding, Spear of Desolation, Obsidian Shard, Kinetic Cuirass, Screeching Gargoyle,
    Void Stone, Void Shield, Spear of the Magus, Breastplate of Valor, Doom Orb, Oni
    Hunter''s Garb, Erosion, The World Stone, Eye of Providence, Helm of Radiance,
    Draconic Scale, Shield of the Phoenix, Helm of Darkness, Dreamer''s Idol, Midgardian
    Mail, Magi''s Cloak, Leviathan''s Hide, Shifter''s Shield.'
  slot_scores:
    Stone of Binding:
      total: 0.48
      efficiency: 0.5
      win: 0.45
      pick: 0.0
      fit: 0.7
    Genji's Guard:
      total: 0.5
      efficiency: 0.69
      win: 0.48
      pick: 0.2
      fit: 0.24
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.59
      win: 0.45
      pick: 0.0
      fit: 0.71
    Spear of Desolation:
      total: 0.48
      efficiency: 0.59
      win: 0.45
      pick: 0.0
      fit: 0.48
    Obsidian Shard:
      total: 0.48
      efficiency: 0.58
      win: 0.45
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.45
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Prophetic Cloak — magical protection
    swap_item: Prophetic Cloak
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass, Gluttonous
    Grimoire, Breastplate of Valor, Soul Gem, Oni Hunter''s Garb, Helm of Radiance,
    Obsidian Shard, Erosion, Spear of Desolation, Eye of Providence, Midgardian Mail,
    Shield of the Phoenix, Stone of Binding, Draconic Scale, Helm of Darkness, Bragi''s
    Harp, Blood-Bound Book, Screeching Gargoyle, Magi''s Cloak, Leviathan''s Hide,
    Mantle Of Discord, Ancient Signet, Bracer of The Abyss, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.69
      win: 0.48
      pick: 0.2
      fit: 0.19
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.56
      win: 0.45
      pick: 0.0
      fit: 0.45
    Bracer of The Abyss:
      total: 0.42
      efficiency: 0.52
      win: 0.45
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.47
      efficiency: 0.63
      win: 0.45
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.43
      efficiency: 0.45
      win: 0.45
      pick: 0.0
      fit: 0.45
    Amanita Charm:
      total: 0.48
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Prophetic Cloak
  - Freya's Tears
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Breastplate of Valor
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Soul Gem, Amanita Charm,
    Breastplate of Valor, Spear of Desolation, Kinetic Cuirass, Gluttonous Grimoire,
    Shield of the Phoenix, Screeching Gargoyle, Chronos'' Pendant, Helm of Radiance,
    Oni Hunter''s Garb, Erosion, Obsidian Shard, Helm of Darkness, Eye of Providence,
    Gem of Focus, Gladiator''s Shield, Heartwood Charm, Draconic Scale, Midgardian
    Mail, Stone of Binding, Blood-Bound Book, Magi''s Cloak, Chandra''s Grace, Leviathan''s
    Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.48
      pick: 0.2
      fit: 0.45
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.63
      win: 0.45
      pick: 0.0
      fit: 0.45
    Prophetic Cloak:
      total: 0.5
      efficiency: 0.44
      win: 0.56
      pick: 0.16
      fit: 0.58
    Freya's Tears:
      total: 0.5
      efficiency: 0.58
      win: 0.44
      pick: 0.22
      fit: 0.58
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.86
      win: 0.45
      pick: 0.0
      fit: 0.13
    Soul Gem:
      total: 0.5
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.61
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Prophetic Cloak — magical protection
    swap_item: Prophetic Cloak
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s
    Revenge, Amanita Charm, Shield Splitter, Gluttonous Grimoire, Soul Gem, Kinetic
    Cuirass, Runeforged Hammer, The Reaper, Tekko-Kagi, Titan''s Bane, Golden Blade,
    Hydra''s Lament, Nimble Ring, Breastplate of Valor, Obsidian Shard, Spear of Desolation,
    Tyrfing, The Crusher, Lernaean Bow, Oni Hunter''s Garb, Avenging Blade, Helm of
    Radiance, Heartseeker, Erosion, Eye of Providence, Toxic Blade, Arondight, Spear
    of the Magus, Death Metal, Shield of the Phoenix, Midgardian Mail, Stone of Binding,
    Draconic Scale, Helm of Darkness, Silverbranch Bow, Pharaoh''s Curse, Screeching
    Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.69
      win: 0.48
      pick: 0.2
      fit: 0.2
    Berserker's Shield:
      total: 0.51
      efficiency: 0.74
      win: 0.45
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.67
      win: 0.45
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.56
      win: 0.45
      pick: 0.0
      fit: 0.47
    Shield Splitter:
      total: 0.48
      efficiency: 0.59
      win: 0.45
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Gluttonous Grimoire
  - Rod of Tahuti
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
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Gluttonous Grimoire,
    Jotunn''s Revenge, Soul Gem, Amanita Charm, Shield Splitter, Berserker''s Shield,
    Kinetic Cuirass, Spear of Desolation, Obsidian Shard, Runeforged Hammer, Helm
    of Radiance, The Reaper, Titan''s Bane, Breastplate of Valor, Spear of the Magus,
    Hydra''s Lament, Helm of Darkness, Blood-Bound Book, Death Metal, Ancient Signet,
    Oni Hunter''s Garb, The Crusher, Erosion, Doom Orb, Jade Scepter, Eye of Providence,
    The World Stone, Avenging Blade, Shield of the Phoenix, Midgardian Mail, Chronos''
    Pendant, Draconic Scale, Stone of Binding, Heartseeker, Screeching Gargoyle, Magi''s
    Cloak, Arondight, Leviathan''s Hide.'
  slot_scores:
    Book of Thoth:
      total: 0.4
      efficiency: 0.49
      win: 0.45
      pick: 0.0
      fit: 0.17
    Genji's Guard:
      total: 0.5
      efficiency: 0.69
      win: 0.48
      pick: 0.2
      fit: 0.2
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.67
      win: 0.45
      pick: 0.0
      fit: 0.39
    Transcendence:
      total: 0.41
      efficiency: 0.53
      win: 0.45
      pick: 0.0
      fit: 0.17
    Gluttonous Grimoire:
      total: 0.5
      efficiency: 0.59
      win: 0.45
      pick: 0.0
      fit: 0.6
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.45
      pick: 0.0
      fit: 0.31
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  - Erosion
  flex_slots:
  - Breastplate of Valor
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Gluttonous
    Grimoire, Soul Gem, Breastplate of Valor, Erosion, Eye of Providence, Draconic
    Scale, Oni Hunter''s Garb, Shield of the Phoenix, Helm of Darkness, Shifter''s
    Shield, Stone of Binding, Helm of Radiance, Midgardian Mail, Magi''s Cloak, Leviathan''s
    Hide, Mantle Of Discord, Spear of Desolation, Screeching Gargoyle, Ancile, Obsidian
    Shard, Stampede, Void Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.48
      pick: 0.2
      fit: 0.34
    Breastplate of Valor:
      total: 0.47
      efficiency: 0.63
      win: 0.45
      pick: 0.0
      fit: 0.34
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.45
      pick: 0.0
      fit: 0.72
    Freya's Tears:
      total: 0.49
      efficiency: 0.58
      win: 0.44
      pick: 0.22
      fit: 0.55
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.62
    Erosion:
      total: 0.47
      efficiency: 0.51
      win: 0.45
      pick: 0.0
      fit: 0.62
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shell of Rebuke
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Shell of Rebuke
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic
    Cuirass, Gluttonous Grimoire, Soul Gem, Breastplate of Valor, Erosion, Eye of
    Providence, Draconic Scale, Oni Hunter''s Garb, Shield of the Phoenix, Helm of
    Darkness, Shifter''s Shield, Stone of Binding, Helm of Radiance, Midgardian Mail,
    Magi''s Cloak, Leviathan''s Hide, Mantle Of Discord, Spear of Desolation, Screeching
    Gargoyle, Ancile, Obsidian Shard, Stampede, Void Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.48
      pick: 0.2
      fit: 0.34
    Breastplate of Valor:
      total: 0.47
      efficiency: 0.63
      win: 0.45
      pick: 0.0
      fit: 0.34
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.45
      pick: 0.0
      fit: 0.72
    Freya's Tears:
      total: 0.49
      efficiency: 0.58
      win: 0.44
      pick: 0.22
      fit: 0.55
    Shell of Rebuke:
      total: 0.48
      efficiency: 0.29
      win: 0.69
      pick: 0.11
      fit: 0.43
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.62
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Shell of Rebuke
  swaps:
  - added: Shell of Rebuke
    removed: Erosion
    reason: community 69% win over 73 matches (vs 44% on this god), taking the model's
      weakest slot from Erosion
  starter: *id001
---
