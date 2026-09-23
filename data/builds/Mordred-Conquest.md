---
type: smite-build
god: Mordred
mode: Conquest
builds:
- source: community
  aspect: Aspect of Rage
  aspect_pick_rate: 0.04
  aspect_win_rate: 0.5
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.34
    win_rate: 0.41
    alternates:
    - name: Bracer of The Abyss
      pick_rate: 0.22
      win_rate: 0.55
    - name: Devourer's Gauntlet
      pick_rate: 0.12
      win_rate: 0.5
  - name: Blood-Bound Book
    pick_rate: 0.14
    win_rate: 0.57
    alternates:
    - name: Shield of the Phoenix
      pick_rate: 0.12
      win_rate: 0.67
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.0
  - name: Shield of the Phoenix
    pick_rate: 0.13
    win_rate: 0.33
    alternates:
    - name: Nimble Ring
      pick_rate: 0.13
      win_rate: 0.33
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.6
  - name: Freya's Tears
    pick_rate: 0.16
    win_rate: 0.14
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.25
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.5
  - name: Draconic Scale
    pick_rate: 0.07
    win_rate: 0.0
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.67
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.33
  - name: Circle of Protection
    pick_rate: 0.08
    win_rate: 1.0
    alternates:
    - name: Survivor's Sash
      pick_rate: 0.08
      win_rate: 0.0
    - name: Medal of Defense
      pick_rate: 0.08
      win_rate: 1.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.36
    win_rate: 0.44
  - name: Bluestone Pendant
    pick_rate: 0.22
    win_rate: 0.45
  - name: Hunter's Cowl
    pick_rate: 0.14
    win_rate: 0.29
  source_url: https://smitebrain.com/gods/mordred/
  last_verified: '2026-09-23'
  god_win_rate: 0.44
  god_matches_won: 22
  god_matches_played: 50
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-23'
  god_matches_analyzed: 962
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Shifter's Shield
  - Shell of Rebuke
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Shield
    Splitter, Breastplate of Valor, Runeforged Hammer, Berserker''s Shield, Eye of
    the Storm, Gluttonous Grimoire, Erosion, Eye of Providence, Hydra''s Lament, Stone
    of Binding, Heartseeker, Spear of Desolation, Helm of Radiance, Magi''s Cloak,
    Spear of the Magus, Soul Gem, Avenging Blade, Mantle Of Discord, Screeching Gargoyle,
    Midgardian Mail, Obsidian Shard, Titan''s Bane, The Crusher, Daybreak Gavel, Leviathan''s
    Hide, Void Shield, Stampede, Ancile, Rod of Asclepius, Oni Hunter''s Garb, The
    Reaper, Prophetic Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.72
      win: 0.37
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.56
      win: 0.37
      pick: 0.0
      fit: 0.61
    Shield Splitter:
      total: 0.44
      efficiency: 0.55
      win: 0.37
      pick: 0.0
      fit: 0.56
    Shifter's Shield:
      total: 0.47
      efficiency: 0.55
      win: 0.41
      pick: 0.34
      fit: 0.51
    Shell of Rebuke:
      total: 0.46
      efficiency: 0.28
      win: 0.67
      pick: 0.15
      fit: 0.37
    Amanita Charm:
      total: 0.47
      efficiency: 0.65
      win: 0.37
      pick: 0.0
      fit: 0.51
  community_ordered:
  - Shifter's Shield
  - Shell of Rebuke
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Blood-Bound Book
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shifter's Shield
  - Shell of Rebuke
  - Rod of Tahuti
  flex_slots:
  - Shell of Rebuke
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Jotunn''s Revenge, Amanita Charm, Breastplate of Valor, Gluttonous
    Grimoire, Kinetic Cuirass, Spear of Desolation, Shield Splitter, Spear of the
    Magus, Hydra''s Lament, Runeforged Hammer, Helm of Radiance, Soul Gem, Obsidian
    Shard, Heartseeker, Berserker''s Shield, Eye of the Storm, Rod of Asclepius, Wish-Granting
    Pearl, Doom Orb, Ancient Signet, The World Stone, Erosion, Death Metal, Chronos''
    Pendant, Jade Scepter, Stone of Binding, Eye of Providence, Avenging Blade, Screeching
    Gargoyle, Magi''s Cloak, Titan''s Bane, Helm of Darkness, Triton''s Conch, The
    Crusher, Daybreak Gavel, Oni Hunter''s Garb.'
  slot_scores:
    Blood-Bound Book:
      total: 0.46
      efficiency: 0.48
      win: 0.57
      pick: 0.19
      fit: 0.18
    Breastplate of Valor:
      total: 0.44
      efficiency: 0.65
      win: 0.37
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.72
      win: 0.37
      pick: 0.0
      fit: 0.45
    Shifter's Shield:
      total: 0.45
      efficiency: 0.55
      win: 0.41
      pick: 0.34
      fit: 0.36
    Shell of Rebuke:
      total: 0.45
      efficiency: 0.28
      win: 0.67
      pick: 0.15
      fit: 0.26
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.86
      win: 0.37
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Blood-Bound Book
  - Shifter's Shield
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Blood-Bound Book
  - Jotunn's Revenge
  - Shifter's Shield
  - Shell of Rebuke
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Shell of Rebuke
  - Spear of Desolation
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire, Spear
    of Desolation, Kinetic Cuirass, Breastplate of Valor, Soul Gem, Spear of the Magus,
    Obsidian Shard, Shield Splitter, Runeforged Hammer, Helm of Radiance, Berserker''s
    Shield, Hydra''s Lament, Heartseeker, Eye of the Storm, Erosion, Doom Orb, Rod
    of Asclepius, Eye of Providence, Screeching Gargoyle, Stone of Binding, Chronos''
    Pendant, The World Stone, Titan''s Bane, The Crusher, Dreamer''s Idol, Magi''s
    Cloak, Jade Scepter, The Reaper, Wish-Granting Pearl, Avenging Blade, Daybreak
    Gavel, Mantle Of Discord, Midgardian Mail, Ancient Signet.'
  slot_scores:
    Blood-Bound Book:
      total: 0.46
      efficiency: 0.48
      win: 0.57
      pick: 0.19
      fit: 0.14
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.72
      win: 0.37
      pick: 0.0
      fit: 0.48
    Shifter's Shield:
      total: 0.45
      efficiency: 0.55
      win: 0.41
      pick: 0.34
      fit: 0.38
    Shell of Rebuke:
      total: 0.45
      efficiency: 0.28
      win: 0.67
      pick: 0.15
      fit: 0.27
    Spear of Desolation:
      total: 0.44
      efficiency: 0.57
      win: 0.37
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.86
      win: 0.37
      pick: 0.0
      fit: 0.34
  community_ordered:
  - Blood-Bound Book
  - Shifter's Shield
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Blood-Bound Book
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Shell of Rebuke
  - Amanita Charm
  flex_slots:
  - Shell of Rebuke
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Kinetic Cuirass, Soul
    Gem, Rod of Asclepius, The Reaper, Runeforged Hammer, Shield Splitter, Breastplate
    of Valor, Gluttonous Grimoire, Eye of the Storm, Berserker''s Shield, Ethereal
    Staff, Yogi''s Necklace, Erosion, Eye of Providence, Hydra''s Lament, Phoenix
    Feather, Chandra''s Grace, Heartseeker, Avenging Blade, Spear of Desolation, Lifebinder,
    Spear of the Magus, Glorious Pridwen, Stone of Binding, Helm of Radiance, Midgardian
    Mail, Daybreak Gavel, Obsidian Shard, Titan''s Bane, Sphere of Negation, Magi''s
    Cloak, The Crusher, Screeching Gargoyle.'
  slot_scores:
    Blood-Bound Book:
      total: 0.49
      efficiency: 0.48
      win: 0.57
      pick: 0.19
      fit: 0.35
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.72
      win: 0.37
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.56
      win: 0.37
      pick: 0.0
      fit: 0.6
    Shifter's Shield:
      total: 0.47
      efficiency: 0.55
      win: 0.41
      pick: 0.34
      fit: 0.5
    Shell of Rebuke:
      total: 0.45
      efficiency: 0.28
      win: 0.67
      pick: 0.15
      fit: 0.31
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.37
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Blood-Bound Book
  - Shifter's Shield
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Shell of Rebuke
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Kinetic Cuirass
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
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Kinetic Cuirass, Avenging Blade, Screeching Gargoyle, Void
    Shield, Spear of Desolation, Breastplate of Valor, Heartseeker, Spear of the Magus,
    Shield Splitter, Void Stone, Soul Gem, Obsidian Shard, Runeforged Hammer, Berserker''s
    Shield, Titan''s Bane, The Crusher, Eye of the Storm, Erosion, The Reaper, Hydra''s
    Lament, Eye of Providence, Helm of Radiance, Doom Orb, The World Stone, Magi''s
    Cloak, Pendulum Blade, Dreamer''s Idol, Avatar''s Parashu, Mantle Of Discord,
    Midgardian Mail, Daybreak Gavel, Rod of Asclepius.'
  slot_scores:
    Stone of Binding:
      total: 0.45
      efficiency: 0.51
      win: 0.37
      pick: 0.0
      fit: 0.7
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.37
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.56
      win: 0.37
      pick: 0.0
      fit: 0.52
    Shifter's Shield:
      total: 0.46
      efficiency: 0.55
      win: 0.41
      pick: 0.34
      fit: 0.42
    Shell of Rebuke:
      total: 0.45
      efficiency: 0.28
      win: 0.67
      pick: 0.15
      fit: 0.3
    Amanita Charm:
      total: 0.46
      efficiency: 0.65
      win: 0.37
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Shifter's Shield
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Blood-Bound Book
  - Berserker's Shield
  - Jotunn's Revenge
  - Bracer of The Abyss
  - Nimble Ring
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge, Amanita Charm,
    Gluttonous Grimoire, Kinetic Cuirass, Golden Blade, Breastplate of Valor, Soul
    Gem, Riptalon, Tyrfing, Silverbranch Bow, Shield Splitter, Runeforged Hammer,
    Pharaoh''s Curse, Lernaean Bow, Toxic Blade, Shogun''s Ofuda, Helm of Radiance,
    Erosion, Spear of the Magus, The Reaper, Spear of Desolation, Stone of Binding,
    Hydra''s Lament, Eye of Providence, Eye of the Storm, Tekko-Kagi, Obsidian Shard,
    Magi''s Cloak, Heartseeker, Daybreak Gavel, Screeching Gargoyle, Midgardian Mail,
    Mantle Of Discord, Rod of Asclepius.'
  slot_scores:
    Blood-Bound Book:
      total: 0.47
      efficiency: 0.54
      win: 0.57
      pick: 0.19
      fit: 0.09
    Berserker's Shield:
      total: 0.47
      efficiency: 0.68
      win: 0.37
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.72
      win: 0.37
      pick: 0.0
      fit: 0.26
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.52
      win: 0.55
      pick: 0.22
      fit: 0.21
    Nimble Ring:
      total: 0.43
      efficiency: 0.65
      win: 0.33
      pick: 0.2
      fit: 0.28
    Rod of Tahuti:
      total: 0.49
      efficiency: 0.86
      win: 0.37
      pick: 0.0
      fit: 0.13
  community_ordered:
  - Blood-Bound Book
  - Bracer of The Abyss
  - Nimble Ring
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shifter's Shield
  - Shell of Rebuke
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Shell of Rebuke
  - Spear of Desolation
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Breastplate of Valor, Amanita Charm, Spear of Desolation, Kinetic Cuirass, Soul
    Gem, Hydra''s Lament, Screeching Gargoyle, Gluttonous Grimoire, Berserker''s Shield,
    Chronos'' Pendant, Shield Splitter, Runeforged Hammer, Helm of Radiance, Prophetic
    Cloak, Spear of the Magus, Erosion, Eye of Providence, Stone of Binding, Gladiator''s
    Shield, Obsidian Shard, Eye of the Storm, Arondight, Gem of Focus, Magi''s Cloak,
    Rod of Asclepius, Eye of Erebus, Mantle Of Discord, Midgardian Mail, Daybreak
    Gavel, Heartseeker, Pendulum Blade, Glorious Pridwen, Chandra''s Grace, Jade Scepter.'
  slot_scores:
    Breastplate of Valor:
      total: 0.46
      efficiency: 0.65
      win: 0.37
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.72
      win: 0.37
      pick: 0.0
      fit: 0.5
    Shifter's Shield:
      total: 0.46
      efficiency: 0.55
      win: 0.41
      pick: 0.34
      fit: 0.41
    Shell of Rebuke:
      total: 0.45
      efficiency: 0.28
      win: 0.67
      pick: 0.15
      fit: 0.29
    Spear of Desolation:
      total: 0.44
      efficiency: 0.57
      win: 0.37
      pick: 0.0
      fit: 0.5
    Amanita Charm:
      total: 0.46
      efficiency: 0.65
      win: 0.37
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Shifter's Shield
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Blood-Bound Book
  - Book of Thoth
  - Jotunn's Revenge
  - Shifter's Shield
  - Transcendence
  - Rod of Tahuti
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shell of Rebuke — physical protection
    swap_item: Shell of Rebuke
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita
    Charm, Gluttonous Grimoire, Kinetic Cuirass, Spear of Desolation, Breastplate
    of Valor, Soul Gem, Spear of the Magus, Helm of Radiance, Obsidian Shard, Shield
    Splitter, Runeforged Hammer, Berserker''s Shield, Rod of Asclepius, Hydra''s Lament,
    Eye of the Storm, Chronos'' Pendant, Erosion, Jade Scepter, Doom Orb, Heartseeker,
    Eye of Providence, Wish-Granting Pearl, Stone of Binding, The World Stone, Death
    Metal, Ancient Signet, Helm of Darkness, Screeching Gargoyle, Dreamer''s Idol,
    Magi''s Cloak, Avenging Blade, Ethereal Staff, Triton''s Conch, Daybreak Gavel,
    Mantle Of Discord.'
  slot_scores:
    Blood-Bound Book:
      total: 0.47
      efficiency: 0.48
      win: 0.57
      pick: 0.19
      fit: 0.21
    Book of Thoth:
      total: 0.38
      efficiency: 0.51
      win: 0.37
      pick: 0.0
      fit: 0.21
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.72
      win: 0.37
      pick: 0.0
      fit: 0.4
    Shifter's Shield:
      total: 0.45
      efficiency: 0.55
      win: 0.41
      pick: 0.34
      fit: 0.39
    Transcendence:
      total: 0.37
      efficiency: 0.53
      win: 0.37
      pick: 0.0
      fit: 0.15
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.86
      win: 0.37
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Blood-Bound Book
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Blood-Bound Book
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Shell of Rebuke
  - Rod of Tahuti
  flex_slots:
  - Shell of Rebuke
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Shield Splitter, Breastplate
    of Valor, Spear of Desolation, Spear of the Magus, Runeforged Hammer, Helm of
    Radiance, Soul Gem, Obsidian Shard, Berserker''s Shield, Eye of the Storm, Hydra''s
    Lament, Rod of Asclepius, Heartseeker, Erosion, Eye of Providence, Stone of Binding,
    Doom Orb, Jade Scepter, Death Metal, Wish-Granting Pearl, Avenging Blade, Magi''s
    Cloak, Chronos'' Pendant, The World Stone, Helm of Darkness, Titan''s Bane, The
    Crusher, Ancient Signet, Screeching Gargoyle, Mantle Of Discord, Dreamer''s Idol,
    Midgardian Mail.'
  slot_scores:
    Blood-Bound Book:
      total: 0.46
      efficiency: 0.48
      win: 0.57
      pick: 0.19
      fit: 0.18
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.72
      win: 0.37
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.56
      win: 0.37
      pick: 0.0
      fit: 0.52
    Shifter's Shield:
      total: 0.46
      efficiency: 0.55
      win: 0.41
      pick: 0.34
      fit: 0.42
    Shell of Rebuke:
      total: 0.45
      efficiency: 0.28
      win: 0.67
      pick: 0.15
      fit: 0.3
    Rod of Tahuti:
      total: 0.51
      efficiency: 0.86
      win: 0.37
      pick: 0.0
      fit: 0.33
  community_ordered:
  - Blood-Bound Book
  - Shifter's Shield
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shield Splitter
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
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Kinetic
    Cuirass, Shield Splitter, Breastplate of Valor, Runeforged Hammer, Berserker''s
    Shield, Eye of the Storm, Gluttonous Grimoire, Erosion, Eye of Providence, Hydra''s
    Lament, Stone of Binding, Heartseeker, Spear of Desolation, Helm of Radiance,
    Magi''s Cloak, Spear of the Magus, Soul Gem, Avenging Blade, Mantle Of Discord,
    Screeching Gargoyle, Midgardian Mail, Obsidian Shard, Titan''s Bane, The Crusher,
    Daybreak Gavel, Leviathan''s Hide, Void Shield, Stampede, Ancile, Rod of Asclepius,
    Oni Hunter''s Garb, The Reaper, Prophetic Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.72
      win: 0.37
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.56
      win: 0.37
      pick: 0.0
      fit: 0.61
    Shield Splitter:
      total: 0.44
      efficiency: 0.55
      win: 0.37
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.36
      efficiency: 0.61
      win: 0.14
      pick: 0.27
      fit: 0.47
    Rod of Tahuti:
      total: 0.49
      efficiency: 0.86
      win: 0.37
      pick: 0.0
      fit: 0.19
    Amanita Charm:
      total: 0.47
      efficiency: 0.65
      win: 0.37
      pick: 0.0
      fit: 0.51
  community_ordered:
  - Freya's Tears
  starter: *id001
---
